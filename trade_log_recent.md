# 2026-11-16

Live cycle (Monday). Mode `live`, strategy version `fd546c8`. No orders were placed: no sell rule fired, all 5 slots were full, and no top-up passed both the gate and sizing. Open positions: 5 of 5.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and $0.00 over the trailing week, so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $100.04
  - open-position cost basis: $53.99
  - unrealized P&L: +$3.19
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $39.83 vs. $37.64 average cost (+5.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached (the first is at +15%).
  - It is 7.3% over its $11.98 target, so there is no trim.
- **CNC:** holding.
  - Price $74.34 vs. $68.28 average cost (+8.9%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 10.5% over target, so there is no trim.
- **NWL:** holding.
  - Price $5.75 vs. $5.82 average cost (−1.2%).
  - The volatility-scaled stop is 12.6%, so it did not trigger.
  - It is at its $5.99 target, so there is no trim.
- **FROG:** holding.
  - Price $109.60 vs. $100.71 average cost (+8.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 6.9% over target, so there is no trim.
- **SKM:** holding.
  - Price $34.57 vs. $33.91 average cost (+1.9%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 1.3% over target, so there is no trim.

**Monday weekend check:** one search per held position found no Saturday/Sunday news that contradicts its thesis.

**Candidates** (from Friday afternoon's Phase A):
- **WSE, CBRS** (new, medium): no open slots (5 of 5 held). Skipped without a price re-check.
- **CNC** (held, top-up): skipped by the buy gate. It opened 4.4% above its thesis price ($71.26 → $74.42); the gap cap is 3%.
- **FROG** (held, top-up): skipped by the buy gate. It is 13.0% above its 20-day average; the cap is 10%.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09) and the sell re-entry lock ($5.78 is above the $5.74 sell price).
- **ROIV, SKM** (held, top-up): passed the gate. No top-up: each is already above its $12.01 target ($12.86 and $12.20).

**Orders placed:** none.

Cash: $42.86. Open positions: 5 of 5 (ROIV, CNC, NWL, FROG, SKM).
