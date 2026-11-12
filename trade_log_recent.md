# 2026-11-12

Live cycle (Thursday). Mode `live`, strategy version `1737086`. One buy was placed: a new SKM position. No sell rule fired. Open positions: 5 of 5.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and −$1.55 over the trailing week (−1.55%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $99.13
  - open-position cost basis: $42.09
  - unrealized P&L: +$2.28
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $41.42 vs. $37.64 average cost (+10.1%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached (the first is at +15%).
  - It is 12.6% over its $11.87 target, so there is no trim.
- **CNC:** holding.
  - Price $69.87 vs. $68.28 average cost (+2.3%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 4.8% over target, so there is no trim.
- **NWL:** holding.
  - Price $5.87 vs. $5.82 average cost (+0.9%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 2.2% over its $5.94 target, so there is no trim.
- **FROG:** holding.
  - Price $105.14 vs. $100.71 average cost (+4.4%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 3.5% over target, so there is no trim.

**Candidates** (from Wednesday afternoon's Phase A; one slot was open):
- **SKM** (new, medium): approved and sized at $11.90.
  - Passed the buy gate: 1.2% below its thesis price and 7.7% above its 20-day average.
- **TTEK** (new, medium): skipped by the buy gate. It opened 6.2% above its thesis price ($37.53 → $39.84); the gap cap is 3%.
- **REZI, AXGN** (new, medium): skipped by the buy gate. They are 26.2% and 28.9% above their 20-day averages; the cap is 10%.
- **ROIV, FROG** (held, top-up): skipped by the buy gate. They are 11.9% and 11.7% above their 20-day averages.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09) and the sell re-entry lock.
- **CNC** (held, top-up): passed the gate. No top-up: it is already above its $11.90 target ($12.44).

**Orders placed:**
- SKM buy, $11.90 market order: filled 0.350929 shares at $33.9099.

Cash: $42.86. Open positions: 5 of 5 (ROIV, CNC, NWL, FROG, SKM).
