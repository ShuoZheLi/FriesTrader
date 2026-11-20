#!/usr/bin/env python3
# Part of FriesTrader (https://github.com/YizhiSong/FriesTrader)
# Copyright (c) 2026 Yizhi Song, MIT License -- see LICENSE
"""Decide whether to trim one held position ahead of its next earnings
report, per risk_rules.json pre_earnings_trim / PHASE_B_TASK.md Step 5.

The trim window is the last --trading-days-before trading days before
the report (1 = the trading day before). A report scheduled for today
counts only when it is not before the open (timing "pm" or unknown) --
an "am" report today has already happened, so trimming now would sell
after the event rather than before it.

Exempt: a position whose conviction is "high" AND whose breakeven stop
is armed (stop_loss.py's breakeven_armed) -- it is already protected
against turning into a loss. A trim fires once per earnings report.
"""
import argparse
import json
import math
import sys


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--quantity", type=float, required=True,
                   help="position quantity as it stands now (shares_available_for_sells)")
    p.add_argument("--sell-fraction", type=float, required=True,
                   help="pre_earnings_trim.sell_fraction")
    p.add_argument("--trading-days-before", type=int, required=True,
                   help="pre_earnings_trim.trading_days_before")
    p.add_argument("--trading-days-until-earnings", type=int, default=None,
                   help="trading days from today to the next unreported report.date (0 if today); "
                        "omit if there is no unreported entry")
    p.add_argument("--earnings-timing", choices=["am", "pm", "unknown"], default="unknown")
    p.add_argument("--report-date", default=None, help="the report.date, passed through for logging")
    p.add_argument("--conviction", choices=["low", "medium", "high"], required=True,
                   help="this cycle's thesis conviction for the position")
    p.add_argument("--breakeven-armed", choices=["true", "false"], required=True,
                   help="stop_loss.py's breakeven_armed for this position this cycle")
    p.add_argument("--already-trimmed-for-report", action="store_true",
                   help="a pre_earnings_trim already fired for this same report.date this holding period")
    args = p.parse_args()

    if not 0 < args.sell_fraction <= 1:
        print(json.dumps({"error": "sell_fraction must be in (0, 1]"}), file=sys.stderr)
        sys.exit(1)

    result = {"report_date": args.report_date, "earnings_timing": args.earnings_timing,
              "trading_days_until_earnings": args.trading_days_until_earnings}

    tdays = args.trading_days_until_earnings
    if tdays is None:
        in_window = False
        result["notes"] = "no unreported earnings date"
    elif tdays == 0:
        in_window = args.earnings_timing != "am"
        if not in_window:
            result["notes"] = "report was before today's open -- already happened"
    else:
        in_window = 1 <= tdays <= args.trading_days_before

    exempt = args.conviction == "high" and args.breakeven_armed == "true"
    triggered = in_window and not exempt and not args.already_trimmed_for_report

    result.update({
        "in_window": in_window,
        "exempt_high_conviction_breakeven": exempt,
        "already_trimmed_for_report": args.already_trimmed_for_report,
        "triggered": triggered,
    })
    if triggered:
        qty = math.floor(args.quantity * args.sell_fraction * 1e6) / 1e6
        result["sell_fraction"] = args.sell_fraction
        result["quantity_before"] = round(args.quantity, 6)
        result["quantity_to_sell"] = qty
        result["action"] = "sell_partial_position" if qty < args.quantity else "sell_full_position"
    else:
        result["action"] = "hold_monitor"
    print(json.dumps(result))


if __name__ == "__main__":
    main()
