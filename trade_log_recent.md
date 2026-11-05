# 2026-11-05

Live cycle (Thursday). Mode `live`, strategy version `0e0ffbd`. One order was placed: JAN was sold as an `exit_existing`. There were no buys, so 4 of 5 slots are in use.

**Loss-limit check:** clear.
- Realized P&L is −$0.27 today (−0.27%) and −$1.60 this week (−1.60%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $99.97
  - open-position cost basis: $48.06
  - unrealized P&L: +$1.57
  - all-time realized P&L: −$1.60

**Held positions** (stop-loss, take-profit and trim checks):
- **JAN:** sold.
  - Wednesday's Phase A marked it `exit_existing` after JAN launched a 25M-share public offering after the 11-04 close. It had already completed a 16M-share offering in August, which the entry thesis had missed.
  - The early-exit guard applied, since the position was opened 11-04. It was satisfied because the offering is a new fact dated 11-04, after the 11-03 entry thesis.
  - Sold 0.396939 shares, filled at $29.5556, realizing −$0.27.
  - No wash-sale flag: the position is fully closed.
  - Before the sale, the stop (5.00%) had not triggered: drawdown was 2.4%.
- **CLF:** holding.
  - Price $12.83 vs. $13.15 average cost (−2.4%).
  - The stop is 13.84% (20-day volatility 5.54% × 2.5) and was not triggered. No take-profit tier was reached, and there is no trim.
- **ROIV:** holding.
  - Price $37.74 vs. $37.64 average cost (+0.3%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached, and there is no trim.
- **CNC:** holding.
  - Price $76.80 vs. $68.28 average cost (+12.5%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached; the first tier is at +15%.
  - Conviction is back to medium, so it is only 14.5% over its $12.00 target, and the overweight count resets to 0.
- **NWL:** holding.
  - Price $6.00 vs. $5.82 average cost (+3.1%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - Conviction is now low, so the target is $6.00. The position is 103% over target: overweight cycle 1 of 3.

**Candidates** (from Wednesday afternoon's Phase A; one slot opened after the JAN sale):
- **YOU, VRDN, SWK, FLYW** (new, medium): all skipped by the buy gate after their post-earnings jumps. They are 32.6%, 31.9%, 23.3% and 12.6% above their 20-day averages; the cap is 10%.
- **GXO, PFGC** (new, low): skipped by the buy gate. They are 16.7% and 15.2% above their 20-day averages, and their low conviction would also have blocked a new entry.
- **CLF** (held, medium, top-up): passed the gate. No top-up: the $0.39 of headroom is below the $5.00 minimum.
- **ROIV** (held, top-up): skipped for the earnings blackout. Its next earnings is 2026-11-09, 2 trading days away.
- **CNC** (held, top-up): skipped by the buy gate. It is 12.0% above its 20-day average.
- **NWL** (held, top-up): skipped by the buy gate. The price gapped 3.3% above the thesis price.

**Orders placed:**
- JAN sell, 0.396939 shares. Filled at $29.5556. Order `6aec948f-d01e-4326-b33c-67025b769917`.

Cash: $50.34. Open positions: 4 of 5 (CLF, ROIV, CNC, NWL).
