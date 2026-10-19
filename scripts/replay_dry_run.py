#!/usr/bin/env python3
# Part of FriesTrader (https://github.com/YizhiSong/FriesTrader), MIT License -- see LICENSE
"""Replay a dry run as a paper portfolio, to estimate what it would have
earned.

A dry run never holds anything, so trade_log.jsonl alone can't say
whether the strategy makes money: slots never fill, and no stop-loss or
take-profit ever fires. This script takes every dry-run buy Phase B
logged ("stage": "order", "would_execute": true, not placed), fills it
at its logged quote_ask, then walks forward day by day over historical
daily bars, applying the same exits Phase B would have:

- each trading day, before that day's buys: scripts/stop_loss.py, then
  scripts/take_profit.py, at that day's open (approximating Phase B's
  quote a few minutes after the open), with the risk_rules.json
  parameters and the same 20-day closes / trailing-high inputs;
- scripts/pnl_pct.py's daily/weekly loss-limit halt on paper realized
  losses, against --starting-cash;
- max_concurrent_positions and min_cash_buffer_pct on the paper
  portfolio, the sell re-entry lock, and the wash-sale buy guard on
  paper loss sales.

Not replayed (logged as limitations): thesis-driven exit_existing sells
and conviction trims (Phase A never researched paper positions), top-ups
of paper positions, and top-ups of real holdings. Rules are read from
the current risk_rules.json, not the version each day ran under.

--historicals takes one or more saved get_equity_historicals responses
(interval="day"), covering every bought symbol from ~30 calendar days
before its first dry-run buy through --end-date, plus --benchmark if
given. A bought symbol with no bars is an error, never skipped.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))


def run_script(name, args):
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, name), *args],
                       capture_output=True, text=True)
    if p.returncode != 0:
        print(json.dumps({"error": f"{name} failed: {p.stderr.strip() or p.stdout.strip()}"}),
              file=sys.stderr)
        sys.exit(1)
    return json.loads(p.stdout)


def fmt(values):
    return ",".join(repr(float(v)) for v in values)


def load_bars(paths):
    bars = {}
    for path in paths:
        doc = json.load(open(path))
        results = doc.get("data", doc).get("results", [])
        for r in results:
            series = bars.setdefault(r["symbol"], {})
            for b in r.get("bars", []):
                if b.get("interpolated"):
                    continue
                series[b["begins_at"][:10]] = {
                    "open": float(b["open_price"]), "close": float(b["close_price"]),
                    "high": float(b["high_price"]),
                }
    return bars


def load_dry_run_buys(path):
    buys = []
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        e = json.loads(line)
        if e.get("stage") != "order" or not e.get("would_execute") or e.get("placed"):
            continue
        side = e.get("action") or e.get("side") or ("buy" if "quote_ask" in e else "sell")
        if side != "buy":
            continue
        buys.append(e)
    return buys


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--trade-log", default="trade_log.jsonl")
    p.add_argument("--risk-rules", default="risk_rules.json")
    p.add_argument("--historicals", nargs="+", required=True,
                    help="saved get_equity_historicals (interval=day) response files")
    p.add_argument("--starting-cash", type=float, required=True,
                    help="paper starting cash, e.g. the account's cash when the dry run began")
    p.add_argument("--benchmark", help="symbol to compare against, e.g. SPY (must be in --historicals)")
    p.add_argument("--end-date", help="last day to replay (ISO date); default: last bar available")
    args = p.parse_args()

    rules = json.load(open(args.risk_rules))
    sl, ps, ll = rules["stop_loss"], rules["position_sizing"], rules["loss_limits"]
    ws = rules["wash_sale_avoidance"]
    tiers = ",".join(f'{t["gain_pct"]}:{t["sell_fraction_of_position"]}' for t in rules["take_profit"]["tiers"])
    lock_max_days = rules["sell_reentry_lock"]["gain_close_max_trading_days"]

    bars = load_bars(args.historicals)
    buys = load_dry_run_buys(args.trade_log)
    if not buys:
        print(json.dumps({"error": "no dry-run buys (stage=order, would_execute=true) in trade log"}),
              file=sys.stderr)
        sys.exit(1)
    missing = sorted({b["symbol"] for b in buys if b["symbol"] not in bars}
                     | ({args.benchmark} if args.benchmark and args.benchmark not in bars else set()))
    if missing:
        print(json.dumps({"error": f"no historicals for: {', '.join(missing)}"}), file=sys.stderr)
        sys.exit(1)

    start = min(b["date"] for b in buys)
    end = args.end_date or max(d for s in bars.values() for d in s)
    days = sorted({d for s in bars.values() for d in s if start <= d <= end})
    buys_by_day = {}
    for b in buys:
        buys_by_day.setdefault(b["date"], []).append(b)

    cash = args.starting_cash
    held = {}            # symbol -> open paper position
    positions = []       # every paper position, open or closed, for the report
    last_sell = {}       # symbol -> {"date", "price", "was_gain"}
    loss_sales = {}      # symbol -> [dates of paper sales realizing a loss]
    realized = []        # (date, pnl_usd)
    skipped, equity_curve = [], []

    def mark(symbol, day, field):
        series = bars[symbol]
        if day in series:
            return series[day][field]
        prior = [d for d in series if d < day]
        return series[max(prior)]["close"] if prior else held[symbol]["avg_cost"]

    def sell(pos, day, price, quantity, reason):
        nonlocal cash
        quantity = min(quantity, pos["quantity"])
        pnl = (price - pos["avg_cost"]) * quantity
        cash += price * quantity
        pos["quantity"] -= quantity
        pos["exits"].append({"date": day, "reason": reason, "price": round(price, 4),
                             "quantity": round(quantity, 6), "pnl_usd": round(pnl, 2)})
        realized.append((day, pnl))
        if pnl < 0:
            loss_sales.setdefault(pos["symbol"], []).append(day)
        if pos["quantity"] <= 1e-9:
            pos["status"] = "closed"
            del held[pos["symbol"]]
            last_sell[pos["symbol"]] = {"date": day, "price": price, "was_gain": price > pos["avg_cost"]}

    for day in days:
        # Step 5/6: exits on every paper position, before any of today's buys
        for symbol in list(held):
            pos = held[symbol]
            if day not in bars[symbol] or day <= pos["entry_date"]:
                continue
            price = bars[symbol][day]["open"]
            prior = sorted(d for d in bars[symbol] if d < day)
            closes = [bars[symbol][d]["close"] for d in prior[-sl["volatility_lookback_trading_days"]:]]
            sl_args = ["--average-cost", repr(pos["avg_cost"]), "--current-price", repr(price),
                       "--mode", sl["mode"], "--hard-stop-pct", repr(sl["hard_stop_pct"]),
                       "--volatility-multiplier", repr(sl["volatility_stdev_multiplier"]),
                       "--min-stop-pct", repr(sl["min_stop_pct"]), "--max-stop-pct", repr(sl["max_stop_pct"]),
                       "--fallback-stop-pct", repr(sl["fallback_stop_pct"]), "--min-bars", "10"]
            if closes:
                sl_args += ["--daily-closes", fmt(closes)]
            if pos["tiers_fired"]:
                highs = [bars[symbol][d]["high"] for d in prior if d >= pos["entry_date"]]
                sl_args += ["--take-profit-tier-fired", "--daily-highs", fmt(highs),
                            "--trailing-high-since", pos["entry_date"]]
            stop = run_script("stop_loss.py", sl_args)
            if stop["triggered"]:
                sell(pos, day, price, pos["quantity"], "stop_loss")
                continue
            tp_args = ["--average-cost", repr(pos["avg_cost"]), "--current-price", repr(price),
                       "--quantity", repr(pos["quantity"]), "--tiers", tiers]
            if pos["tiers_fired"]:
                tp_args += ["--already-fired", fmt(sorted(pos["tiers_fired"]))]
            tp = run_script("take_profit.py", tp_args)
            for fired in tp["fired_this_cycle"]:
                pos["tiers_fired"].add(fired["tier_gain_pct"])
                sell(pos, day, price, fired["quantity_sold"], f'take_profit_{fired["tier_gain_pct"]}')

        # Step 7: loss-limit halt on paper realized P&L
        d = datetime.date.fromisoformat(day)
        week_start = (d - datetime.timedelta(days=d.weekday())).isoformat()
        halt = run_script("pnl_pct.py", [
            "--daily-realized-usd", repr(sum(x for dd, x in realized if dd == day)),
            "--weekly-realized-usd", repr(sum(x for dd, x in realized if week_start <= dd <= day)),
            "--net-deposits-usd", repr(args.starting_cash),
            "--daily-limit-pct", repr(ll["daily_loss_limit_pct_of_account"]),
            "--weekly-limit-pct", repr(ll["weekly_loss_limit_pct_of_account"])])

        # Step 8: today's dry-run buys, in logged order
        for b in buys_by_day.get(day, []):
            symbol, reason = b["symbol"], None
            equity = cash + sum(p["quantity"] * mark(s, day, "open") for s, p in held.items())
            dollar_amount, ask = b.get("dollar_amount"), b.get("quote_ask")
            lock = last_sell.get(symbol)
            if b.get("position_action") == "top_up":
                reason = "top-up of a real holding -- not part of the paper portfolio"
            elif dollar_amount is None or ask is None:
                reason = "order entry has no dollar_amount/quote_ask"
            elif halt["entries_halted"]:
                reason = f"paper loss-limit halt: {halt['halt_reason']}"
            elif symbol in held:
                reason = "already held in the paper portfolio (a real run would have seen a top-up)"
            elif len(held) >= ps["max_concurrent_positions"]:
                reason = f"no open slot -- paper portfolio already holds {len(held)} positions"
            elif lock and ask > lock["price"] and not (
                    lock["was_gain"] and sum(1 for x in days if lock["date"] < x <= day) >= lock_max_days):
                reason = f"sell re-entry lock -- sold at {lock['price']:.4f} on {lock['date']}"
            elif ws["enabled"] and any(
                    (d - datetime.date.fromisoformat(x)).days <= ws["lookback_window_days"]
                    for x in loss_sales.get(symbol, [])):
                reason = "wash sale guard -- paper loss sale within the lookback window"
            elif cash - dollar_amount < ps["min_cash_buffer_pct"] * equity:
                reason = f"paper cash ${cash:.2f} too low for ${dollar_amount:.2f} with the cash buffer"
            if reason:
                skipped.append({"date": day, "symbol": symbol, "proposal_date": b.get("proposal_date"),
                                "reason": reason})
                continue
            cash -= dollar_amount
            pos = {"symbol": symbol, "proposal_date": b.get("proposal_date"), "entry_date": day,
                   "avg_cost": float(ask), "quantity": dollar_amount / ask, "cost_usd": dollar_amount,
                   "tiers_fired": set(), "exits": [], "status": "open"}
            held[symbol] = pos
            positions.append(pos)

        equity_curve.append({"date": day, "value": round(
            cash + sum(p["quantity"] * mark(s, day, "close") for s, p in held.items()), 2)})

    peak, max_dd = 0.0, 0.0
    for point in equity_curve:
        peak = max(peak, point["value"])
        max_dd = max(max_dd, (peak - point["value"]) / peak if peak else 0.0)

    report = []
    for pos in positions:
        realized_pnl = sum(x["pnl_usd"] for x in pos["exits"])
        entry = {"symbol": pos["symbol"], "proposal_date": pos["proposal_date"],
                 "entry_date": pos["entry_date"], "entry_price": round(pos["avg_cost"], 4),
                 "cost_usd": round(pos["cost_usd"], 2), "status": pos["status"], "exits": pos["exits"],
                 "realized_pnl_usd": round(realized_pnl, 2)}
        if pos["status"] == "open":
            last = mark(pos["symbol"], end, "close")
            entry["remaining_quantity"] = round(pos["quantity"], 6)
            entry["unrealized_pnl_usd"] = round((last - pos["avg_cost"]) * pos["quantity"], 2)
        entry["total_pnl_usd"] = round(realized_pnl + entry.get("unrealized_pnl_usd", 0.0), 2)
        report.append(entry)

    closed = [r for r in report if r["status"] == "closed"]
    ending_value = equity_curve[-1]["value"] if equity_curve else args.starting_cash
    out = {
        "window": {"start": start, "end": end, "trading_days": len(days)},
        "starting_cash": args.starting_cash,
        "ending_value": ending_value,
        "return_pct": round(ending_value / args.starting_cash - 1, 6),
        "max_drawdown_pct": round(max_dd, 6),
        "positions_opened": len(report),
        "closed_positions": len(closed),
        "closed_win_rate": round(sum(r["total_pnl_usd"] > 0 for r in closed) / len(closed), 4) if closed else None,
        "realized_pnl_usd": round(sum(x for _, x in realized), 2),
    }
    if args.benchmark:
        series = bars[args.benchmark]
        bench_days = [x for x in days if x in series]
        out["benchmark"] = {"symbol": args.benchmark, "return_pct": round(
            series[bench_days[-1]]["close"] / series[bench_days[0]]["open"] - 1, 6)}
    out.update({
        "positions": report,
        "skipped_buys": skipped,
        "equity_curve": equity_curve,
        "limitations": [
            "exits are checked at each day's open, approximating Phase B's quote shortly after the open",
            "exit_existing and conviction_trim sells are not replayed (no paper-position theses)",
            "paper positions are never topped up; real-holding top-ups are skipped",
            "rules come from the current risk_rules.json, not each day's strategy_version",
        ],
    })
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
