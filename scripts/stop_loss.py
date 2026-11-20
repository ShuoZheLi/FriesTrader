#!/usr/bin/env python3
# Part of FriesTrader (https://github.com/YizhiSong/FriesTrader)
# Copyright (c) 2026 Yizhi Song, MIT License -- see LICENSE
"""Compute the stop-loss reference price, stop_pct, and trigger decision
for one position, per risk_rules.json/PHASE_B_TASK.md Step 5.

Sample standard deviation (ddof=1) is used for the volatility_scaled stdev,
the standard convention for a sample of daily returns (matches Excel
STDEV/pandas .std() default).

Breakeven stop (optional, --breakeven-trigger-pct): once the position's
peak gain since entry (the highest daily high since the holding period's
entry date, or the current price if higher, versus average cost) has
reached the trigger, the stop is raised to average cost -- the position
is sold in full as soon as the price is at or below average cost, so a
position that has been meaningfully in profit cannot turn into a loss.
This is a floor on top of the regular stop, never a loosening of it.
"""
import argparse
import json
import statistics
import sys


def parse_float_list(s):
    if not s:
        return []
    return [float(x) for x in s.split(",")]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--average-cost", type=float, required=True)
    p.add_argument("--current-price", type=float, required=True)
    p.add_argument("--mode", choices=["fixed", "volatility_scaled"], required=True)

    p.add_argument("--hard-stop-pct", type=float,
                    help="required when --mode fixed")

    p.add_argument("--volatility-multiplier", type=float,
                    help="required when --mode volatility_scaled")
    p.add_argument("--min-stop-pct", type=float,
                    help="required when --mode volatility_scaled")
    p.add_argument("--max-stop-pct", type=float,
                    help="required when --mode volatility_scaled")
    p.add_argument("--fallback-stop-pct", type=float,
                    help="required when --mode volatility_scaled")
    p.add_argument("--min-bars", type=int, default=10,
                    help="minimum usable daily-close bars before falling back (default 10)")
    p.add_argument("--daily-closes", type=parse_float_list, default=[],
                    help="split-adjusted daily closes, oldest first, non-interpolated bars only, "
                         "up to and including yesterday. Only needed when mode=volatility_scaled "
                         "and drawdown is positive.")

    p.add_argument("--take-profit-tier-fired", action="store_true",
                    help="set if any take-profit tier has fired this holding period")
    p.add_argument("--daily-highs", type=parse_float_list, default=[],
                    help="daily high_price bars from the holding period's entry date through "
                         "yesterday. Required when --take-profit-tier-fired is set.")
    p.add_argument("--trailing-high-since", default=None,
                    help="entry date of the current holding period, passed through for logging")

    p.add_argument("--breakeven-trigger-pct", type=float, default=None,
                    help="risk_rules.json stop_loss.breakeven_trigger_pct; omit to disable the breakeven stop")
    p.add_argument("--peak-price", type=float, default=None,
                    help="highest daily high_price since the holding period's entry date through "
                         "yesterday (omit if there is no completed bar yet, e.g. opened today)")

    args = p.parse_args()

    if args.mode == "fixed" and args.hard_stop_pct is None:
        print(json.dumps({"error": "--hard-stop-pct is required when --mode fixed"}), file=sys.stderr)
        sys.exit(1)
    if args.mode == "volatility_scaled" and None in (
        args.volatility_multiplier, args.min_stop_pct, args.max_stop_pct, args.fallback_stop_pct,
    ):
        print(json.dumps({"error": "--volatility-multiplier/--min-stop-pct/--max-stop-pct/"
                                    "--fallback-stop-pct are all required when --mode volatility_scaled"}),
              file=sys.stderr)
        sys.exit(1)
    if args.take_profit_tier_fired and not args.daily_highs:
        print(json.dumps({"error": "--daily-highs is required when --take-profit-tier-fired is set"}),
              file=sys.stderr)
        sys.exit(1)

    # Reference price
    if args.take_profit_tier_fired:
        stop_reference_basis = "trailing_high"
        stop_reference_price = max(args.daily_highs + [args.current_price])
    else:
        stop_reference_basis = "average_cost"
        stop_reference_price = args.average_cost

    drawdown_pct = (stop_reference_price - args.current_price) / stop_reference_price

    result = {
        "stop_reference_basis": stop_reference_basis,
        "stop_reference_price": round(stop_reference_price, 6),
        "drawdown_pct": round(drawdown_pct, 6),
    }
    if args.trailing_high_since:
        result["trailing_high_since"] = args.trailing_high_since

    stop_pct = None

    if args.mode == "fixed":
        # fixed mode always reports hard_stop_pct, regardless of drawdown sign
        stop_pct = args.hard_stop_pct
        result["stop_pct_used"] = round(stop_pct, 6)
    elif drawdown_pct <= 0:
        # volatility_scaled: skip the stdev computation on a gain, it could never trigger anyway
        result["stop_pct_used"] = None
        result["notes"] = "gain, stop not computed"
    else:  # volatility_scaled, drawdown positive
        if len(args.daily_closes) < args.min_bars:
            stop_pct = args.fallback_stop_pct
            result["stop_pct_used"] = round(stop_pct, 6)
            result["fallback_reason"] = (
                f"only {len(args.daily_closes)} usable bars available, below the {args.min_bars} minimum"
            )
        else:
            closes = args.daily_closes
            returns = [(closes[i] - closes[i - 1]) / closes[i - 1] for i in range(1, len(closes))]
            stdev = statistics.stdev(returns)  # sample stdev, ddof=1
            stop_pct = max(args.min_stop_pct, min(args.max_stop_pct, args.volatility_multiplier * stdev))
            result["stdev_20d"] = round(stdev, 6)
            result["stop_pct_used"] = round(stop_pct, 6)

    volatility_triggered = stop_pct is not None and drawdown_pct >= stop_pct

    breakeven_triggered = False
    if args.breakeven_trigger_pct is not None:
        if args.average_cost <= 0:
            print(json.dumps({"error": "average_cost must be positive"}), file=sys.stderr)
            sys.exit(1)
        peak_price = max([args.current_price] + ([args.peak_price] if args.peak_price is not None else []))
        peak_gain_pct = (peak_price - args.average_cost) / args.average_cost
        armed = peak_gain_pct >= args.breakeven_trigger_pct
        result["peak_gain_pct"] = round(peak_gain_pct, 6)
        result["breakeven_armed"] = armed
        if armed:
            result["breakeven_stop_price"] = round(args.average_cost, 6)
            breakeven_triggered = args.current_price <= args.average_cost

    triggered = volatility_triggered or breakeven_triggered
    result["triggered"] = triggered
    if triggered:
        result["trigger_reason"] = "volatility_stop" if volatility_triggered else "breakeven_stop"
    result["action"] = "sell_full_position" if triggered else "hold_monitor"

    print(json.dumps(result))


if __name__ == "__main__":
    main()
