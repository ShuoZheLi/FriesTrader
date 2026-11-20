#!/usr/bin/env python3
# Part of FriesTrader (https://github.com/YizhiSong/FriesTrader)
# Copyright (c) 2026 Yizhi Song, MIT License -- see LICENSE
"""Classify the market regime for one Phase B cycle, per
risk_rules.json market_regime / PHASE_B_TASK.md Step 7.

The market is risk-off when EITHER the benchmark (SPY) trades below the
simple moving average of its last --ma-lookback daily closes, OR the
volatility index (VIX) is above --vix-threshold. Missing data fails safe
to risk-off: fewer closes than the lookback, or no VIX reading.

Risk-off tightens new-entry capacity only: it returns a lower
effective max_concurrent_positions and a higher effective
min_new_entry_conviction for Step 7's capacity check and sizing script.
It never forces a sell of a position already held.
"""
import argparse
import json
import sys

CONVICTION_RANK = {"low": 0, "medium": 1, "high": 2}


def parse_float_list(s):
    if not s:
        return []
    return [float(x) for x in s.split(",")]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--benchmark-closes", type=parse_float_list, required=True,
                   help="benchmark daily closes, oldest first, non-interpolated, through yesterday")
    p.add_argument("--benchmark-price", type=float, required=True,
                   help="fresh benchmark price from get_equity_quotes")
    p.add_argument("--ma-lookback", type=int, required=True,
                   help="market_regime.ma_lookback_trading_days")
    p.add_argument("--vix", type=float, default=None,
                   help="fresh VIX value from get_index_quotes; omit if unavailable (fails safe to risk-off)")
    p.add_argument("--vix-threshold", type=float, required=True,
                   help="market_regime.vix_threshold")
    p.add_argument("--normal-max-positions", type=int, required=True,
                   help="position_sizing.max_concurrent_positions")
    p.add_argument("--risk-off-max-positions", type=int, required=True,
                   help="market_regime.risk_off_max_concurrent_positions")
    p.add_argument("--normal-min-conviction", choices=sorted(CONVICTION_RANK), required=True,
                   help="position_sizing.min_new_entry_conviction")
    p.add_argument("--risk-off-min-conviction", choices=sorted(CONVICTION_RANK), required=True,
                   help="market_regime.risk_off_min_new_entry_conviction")
    args = p.parse_args()

    reasons = []
    result = {"benchmark_price": round(args.benchmark_price, 6)}

    closes = args.benchmark_closes[-args.ma_lookback:]
    if len(closes) < args.ma_lookback:
        reasons.append(f"only {len(closes)} benchmark closes available, below the {args.ma_lookback}-day "
                       "lookback -- fail safe to risk-off")
        result["benchmark_ma"] = None
        result["benchmark_below_ma"] = None
    else:
        ma = sum(closes) / len(closes)
        below = args.benchmark_price < ma
        result["benchmark_ma"] = round(ma, 6)
        result["benchmark_below_ma"] = below
        result["benchmark_vs_ma_pct"] = round((args.benchmark_price - ma) / ma, 6)
        if below:
            reasons.append(f"benchmark {args.benchmark_price} is below its {args.ma_lookback}-day average "
                           f"{round(ma, 2)}")

    if args.vix is None:
        reasons.append("VIX unavailable -- fail safe to risk-off")
        result["vix"] = None
        result["vix_above_threshold"] = None
    else:
        above = args.vix > args.vix_threshold
        result["vix"] = round(args.vix, 4)
        result["vix_above_threshold"] = above
        if above:
            reasons.append(f"VIX {args.vix} is above {args.vix_threshold}")

    risk_off = len(reasons) > 0
    if risk_off:
        max_pos = min(args.normal_max_positions, args.risk_off_max_positions)
        min_conv = max(args.normal_min_conviction, args.risk_off_min_conviction, key=lambda c: CONVICTION_RANK[c])
    else:
        max_pos = args.normal_max_positions
        min_conv = args.normal_min_conviction

    result.update({
        "regime": "risk_off" if risk_off else "normal",
        "risk_off": risk_off,
        "reasons": reasons,
        "effective_max_concurrent_positions": max_pos,
        "effective_min_new_entry_conviction": min_conv,
    })
    print(json.dumps(result))


if __name__ == "__main__":
    main()
