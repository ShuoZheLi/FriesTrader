# Intraday Risk Check — Afternoon Stop-Loss / Take-Profit (Automated Daily Task)

_Part of [FriesTrader](https://github.com/YizhiSong/FriesTrader), Copyright (c) 2026 Yizhi Song, MIT License._

A second, sell-only pass over open positions, run every weekday around
2:15pm Central (about 1h45m before the close) as a cloud routine.

**Why it exists:** positions are fractional shares, which Robinhood only
accepts as regular-hours market orders, so a stop or a take-profit can't
rest at the broker as a stop/limit order. Phase B checks them once, at
8:35am. This run checks them a second time each day, so an intraday
move can still be acted on before the close.

**Scope — this run does ONLY:**
- `PHASE_B_TASK.md` Step 5's **stop-loss check** (including the
  breakeven stop) and **take-profit check**, for every open position;
- `PHASE_B_TASK.md` Step 6's **sell-execution procedure** for whatever
  those two checks trigger.

**It never:** buys or tops up anything, runs the conviction-trim or the
pre-earnings-trim check, sells an `exit_existing` candidate, runs the
loss-limit or market-regime checks, or touches `pending_proposals.jsonl`.
Those stay with Phase A and Phase B.

Authorized to place real live sell orders under exactly the same
live-order gate as Phase B (`execution.mode == "live"`, dry-run cycle
count at or above `execution.dry_run_min_cycles_before_live`, and no
blocking alert from `review_equity_order`). Do not add, remove, or
loosen any gate condition on your own judgment.

## Step 1 — Load state

1. Read `risk_rules.json` **fresh**. If `intraday_risk_check.enabled` is
   `false`, append only the Step 4 `intraday_summary` line with
   `"skipped": "intraday_risk_check.enabled is false"`, then commit and
   push (Step 5) and stop.
2. Determine today's date and time mechanically (e.g. `TZ='America/Chicago'
   date`). Record `strategy_version` = `git rev-parse --short HEAD`, taken
   now, before this run's own commit.
3. Read `trade_log.jsonl` and compute the dry-run cycle count exactly as
   `PHASE_B_TASK.md` Step 0 does (distinct dates with a `cycle_summary`
   entry where `mode: dry_run`).
4. Pull `get_equity_positions` (account from `risk_rules.json`). If there
   are no open positions, log the summary line (Step 4) and stop after
   committing.

## Step 2 — Stop-loss and take-profit checks

For each open position, gather the inputs and run the scripts exactly as
`PHASE_B_TASK.md` Step 5 specifies — the same `stop_loss.py` arguments
(including `--breakeven-trigger-pct`/`--peak-price` with daily highs
since the holding period's entry date through yesterday, and the
trailing-high inputs once a tier has fired) and the same
`take_profit.py` arguments (with every tier already fired this holding
period per `trade_log.jsonl`, including tiers fired by this morning's
Phase B or an earlier intraday run). Use a fresh `get_equity_quotes`
price taken now. Use the scripts' JSON output directly; never
hand-compute a stop, a drawdown or a tier.

- If `stop_loss.py` reports `triggered` — a full-position sell. Skip the
  take-profit check for that position this run.
- Otherwise, each entry of `take_profit.py`'s `fired_this_cycle` is a
  partial sell of its `quantity_sold`.
- If a script fails to run, don't guess and don't fall back to manual
  computation: log the stage with `"triggered": false, "action":
  "check_manually", "notes": "<script> failed to run — verify this
  position before the next Phase B"`, and sell nothing for that
  position this run.

Log one `"stage": "stop_loss"` and one `"stage": "take_profit"` line per
position (one take-profit line per fired tier, as in Phase B), shaped
exactly as in `PHASE_B_TASK.md` Step 5, each with `"run": "intraday"`.

## Step 3 — Sell execution

For every sell from Step 2, run `PHASE_B_TASK.md` Step 6's
"Execute sells now" procedure unchanged: the fixed order parameters
(`type: "market"`, `market_hours: "regular_hours"`, `time_in_force:
"gfd"`, `side: "sell"`, `quantity` as a decimal string rounded down to 6
decimals and capped at `shares_available_for_sells`), `review_equity_order`
first, the live-order gate, `place_equity_order` with a fresh UUID
`ref_id`, and the fill confirmation via `get_equity_orders` (check once,
wait ~15 seconds and check once more if not terminal — never more).
Apply the same wash-sale flag rule to loss-realizing sells.

Log each as `"stage": "order"` in Phase B's shape, plus `"run":
"intraday"` and `"sell_reason": "stop_loss"` or `"take_profit"`. Every
order entry carries `proposal_date`: the `date` of the latest
`"stage": "thesis"` line for that symbol in `pending_proposals.jsonl`,
or, if it has none, the `proposal_date` of the order that opened this
holding period.

## Step 4 — Logging

Append every line from Steps 2–3 to `trade_log.jsonl`, each with a real
`"timestamp"` (`HH:mm:ss`, Central, time-of-day only) and today's
`"date"`. Always end with exactly one summary line:

```json
{"date": "YYYY-MM-DD", "timestamp": "HH:mm:ss", "stage": "intraday_summary", "run": "intraday", "mode": "dry_run|live", "strategy_version": "abc1234", "positions_checked": N, "orders_reviewed": N, "orders_placed": N}
```

This is deliberately not a `cycle_summary`, so it never changes Phase B's
dry-run cycle count or daily accounting.

Then **append** (don't overwrite) a short section to
`trade_log_recent.md`: a `## Afternoon risk check (HH:MM)` heading, one
line per position (price vs. average cost, stop or tier status, and
whether anything triggered), and any orders placed (symbol, shares,
fill). If the file's `# YYYY-MM-DD` heading is not today's date (this
morning's Phase B didn't write one), start the file fresh with a
`# YYYY-MM-DD` heading first.

## Step 5 — Saving to the repo

```
git add trade_log.jsonl trade_log_recent.md
git commit -m "Intraday check <date> <timestamp>"
git push origin HEAD:main
```

If the push is rejected, run `git pull --rebase origin main` once, then
`git push origin HEAD:main` once more. If it still fails, stop retrying
and report the exact error. **Never** run `git checkout`, `git switch`,
`git reset`, `git stash`, `git merge`, `git branch -f`, or any
force-push to "fix" branch state.

## Hard rules

- Never change `execution.mode` or any `risk_rules.json` value.
- Never place a buy. Never call `place_equity_order` unless the
  live-order gate is open at that moment.
- A good thesis never cancels a stop-loss or a take-profit tier.
- If required data can't be retrieved (positions, quotes, historicals),
  sell nothing you can't justify from the scripts' output, and log
  exactly what failed.
