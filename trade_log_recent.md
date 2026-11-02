# 2026-11-02

Live cycle (Monday). Mode `live`, strategy version `cd1200e`. One order was placed: AVTR, a full `exit_existing` sell. There were no buys, so 4 of 5 slots are now in use.

**Loss-limit check:** clear.
- Realized P&L is −$0.53 today and −$0.53 this week (−0.53% of net deposits), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $99.26
  - open-position cost basis: $56.50
  - unrealized P&L: −$0.21
  - all-time realized P&L: −$0.53

**Held positions** (stop-loss, take-profit and trim checks):
- **AVTR:** sold.
  - This was Friday's `exit_existing`: the 10-30 close was below the 20-day average, which is the thesis invalidation.
  - The early-exit guard does not apply, because the opening buy was on 10-19, 10 trading days ago.
  - Sold 0.726942 shares, filled at $15.7801, realizing −$0.53.
  - No wash-sale flag: the position is fully closed and there is no replacement lot.
  - Before the sale, the stop (5.00%, the floor) had not triggered: drawdown was 4.3%.
- **CLF:** holding.
  - Price $14.86 vs. $13.15 average cost (+13.0%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached; the first tier is at +15%.
  - The position is 13.8% over target; the trim trigger is 25%.
- **ROIV:** holding.
  - Price $36.64 vs. $37.64 average cost (−2.7%).
  - The stop is 6.01% (20-day volatility 2.40% × 2.5) and was not triggered. No take-profit tier was reached, and there is no trim.
- **RNG:** holding.
  - Price $78.13 vs. $82.73 average cost (−5.6%).
  - The stop is 8.50% (20-day volatility 3.40% × 2.5) and was not triggered. No take-profit tier was reached, and there is no trim.
- **CNC:** holding.
  - Price $66.44 vs. $68.28 average cost (−2.7%).
  - The stop is 5.00% (the floor) and was not triggered. No take-profit tier was reached, and there is no trim.

**Candidates** (from Friday afternoon's Phase A; one weekend-gap search was run for each):
- **BHC** (new, medium): skipped by the buy gate.
  - Price is 26.1% above its 20-day average ($6.46 → $8.15) after the Q3 earnings jump. The cap is 10%.
- **RGEN** (new, low, `governance_history`): passed the buy gate, but was rejected because its conviction is below the medium minimum for new entries.
  - The weekend search found the 10-30 $1.0B convertible-note deal. That adds dilution risk but does not reverse the thesis.
- **CLF** (held, medium, top-up): skipped by the buy gate.
  - Price gapped 4.3% above the thesis price ($14.26 → $14.87), and it is 13.2% above its 20-day average.
  - It is also already above its $11.91 target.
- **ROIV** (held, medium, top-up): skipped for the earnings blackout.
  - Its next earnings is 2026-11-09, 5 trading days away.
- **RNG** (held, high, top-up): passed the gate, but the top-up was skipped after a re-check of the gap against the thesis.
  - The ask gapped down 3.5% to $78.50, which is below the thesis invalidation level (a close back below the pre-report ~$79.42). No news explains the move.
- **CNC** (held, medium, top-up): passed the gate, but the top-up was skipped after the same re-check.
  - The ask gapped down 2.9% to $66.46, which is below the thesis invalidation level (back below the pre-report ~$68.03). No news explains the move.

**Orders placed:**
- AVTR sell, 0.726942 shares, filled at $15.7801. Order `6ae8abd5-44d1-4df5-ad54-38766045af05`.

Cash: $42.97. Open positions: 4 of 5 (CLF, ROIV, RNG, CNC).
