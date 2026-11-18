# 2026-11-18

Live cycle (Wednesday). Mode `live`, strategy version `9f4163b`. No orders were placed: no sell rule fired, all 5 slots were full, and no top-up passed both the gate and sizing. Open positions: 5 of 5.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and $0.00 over the trailing week, so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $98.57
  - open-position cost basis: $53.99
  - unrealized P&L: +$1.72
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $38.835 vs. $37.64 average cost (+3.2%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached (the first is at +15%).
  - It is 6.0% over its $11.82 target, so there is no trim.
- **CNC:** holding.
  - Price $71.66 vs. $68.28 average cost (+5.0%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 8.0% over target, so there is no trim.
- **NWL:** holding.
  - Price $5.71 vs. $5.82 average cost (−1.9%).
  - The volatility-scaled stop is 12.6%, so it did not trigger.
  - It is at its $5.91 target, so there is no trim.
- **FROG:** holding.
  - Price $107.525 vs. $100.71 average cost (+6.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 6.3% over target, so there is no trim.
- **SKM:** holding.
  - Price $33.82 vs. $33.91 average cost (−0.3%).
  - The volatility-scaled stop is 7.7%, so it did not trigger.
  - It is at its target, so there is no trim.

**Candidates** (from Tuesday afternoon's Phase A):
- **ACM, HTHT** (new, medium): no open slots (5 of 5 held). Skipped without a price re-check.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09) and the sell re-entry lock ($5.75 is above the $5.74 sell price).
- **ROIV, CNC, FROG, SKM** (held, top-up): passed the gate. No top-up: each is already at or above its $11.83 target ($12.54, $12.84, $12.52 and $11.87).

**Orders placed:** none.

Cash: $42.86. Open positions: 5 of 5 (ROIV, CNC, NWL, FROG, SKM).
