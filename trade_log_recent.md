# 2026-11-20

Live cycle (Friday). Mode `live`, strategy version `88bd75c` (first cycle under the new rules from PR #3). Two stop-loss sells were placed and filled: SKM was sold in full, and the rest of FROG was sold on its trailing stop. No buys. Open positions: 3 (ROIV, NWL, HTHT).

**Market regime:** risk-off. SPY at $713.58 is 6.3% below its 50-day average ($761.67), and VIX is 28.5 (above 25). New entries are capped at 3 positions and need high conviction.

**Loss-limit check:** clear.
- Realized P&L is −$1.66 today (−1.7%) and −$1.36 over the trailing week, so entries are not halted.
- `net_deposits_usd` is $100.00, computed after this cycle's sells from:
  - total value: $95.30
  - open-position cost basis: $30.00
  - unrealized P&L: −$0.18
  - all-time realized P&L: −$4.51

**Held positions** (stop-loss, take-profit, trim and pre-earnings checks):
- **SKM:** stop-loss triggered and sold.
  - It opened down 10% at $28.43, 16.2% below the $33.91 average cost.
  - The volatility-scaled stop was 6.6%.
- **FROG:** trailing stop triggered and sold.
  - Price $104.96 was 13.9% below its $121.85 high since entry, past the 10% cap.
  - The remaining shares still sold above the $100.74 average cost (+3.0%).
- **ROIV:** holding.
  - Price $38.90 vs. $37.64 average cost (+3.3%).
  - The breakeven stop is armed (peak gain +12.2%), so it sells if the price falls back to $37.64.
  - No take-profit tier was reached, and there is no trim.
- **NWL:** holding.
  - Price $5.40 vs. $5.82 average cost (−7.2%).
  - The volatility-scaled stop is 9.8%, so it did not trigger.
- **HTHT:** holding.
  - Price $51.42 vs. $52.06 average cost (−1.2%).
  - The volatility-scaled stop is 5.7%, so it did not trigger.
- **Pre-earnings trim:** none due. The next reports are ROIV and NWL on 2/5 and HTHT on 3/17.

**Candidates** (from Thursday afternoon's Phase A):
- **P** (new, medium) and **SLS** (new, low): no open slots (3 of 3 risk-off max held). Skipped without a price re-check.
- **FROG, SKM** (held, top-up): not eligible, because a stop-loss fired this cycle.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09).
- **ROIV, HTHT** (held, top-up): passed the gate. No top-up: both are already above target.

**Orders placed** (all live and filled):
- **SKM:** sell 0.350929 shares at $28.41 (about $9.97, realized −$1.93).
- **FROG:** sell 0.087652 shares at $103.78 (about $9.10, realized +$0.27).

Cash: $65.49. Open positions: 3 (ROIV, NWL, HTHT).
