# 2026-11-17

Live cycle (Tuesday). Mode `live`, strategy version `88cf1dc`. No orders were placed: no sell rule fired, all 5 slots were full, and no top-up passed both the gate and sizing. Open positions: 5 of 5.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and $0.00 over the trailing week, so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $98.77
  - open-position cost basis: $53.99
  - unrealized P&L: +$1.92
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $38.52 vs. $37.64 average cost (+2.3%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached (the first is at +15%).
  - It is 4.6% over its $11.87 target, so there is no trim.
- **CNC:** holding.
  - Price $73.52 vs. $68.28 average cost (+7.7%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 10.3% over target, so there is no trim.
- **NWL:** holding.
  - Price $5.74 vs. $5.82 average cost (−1.4%).
  - The volatility-scaled stop is 12.6%, so it did not trigger.
  - It is at its $5.93 target, so there is no trim.
- **FROG:** holding.
  - Price $109.34 vs. $100.71 average cost (+8.6%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 7.7% over target, so there is no trim.
- **SKM:** holding.
  - Price $33.68 vs. $33.91 average cost (−0.7%).
  - The volatility-scaled stop is 7.6%, so it did not trigger.
  - It is at its target, so there is no trim.

**Candidates** (from Monday afternoon's Phase A):
- **CGON, CHYM, MBGL, TSN, WWW, HTHT, COLD** (new, medium): no open slots (5 of 5 held). Skipped without a price re-check.
- **FROG** (held, top-up): skipped by the buy gate. It is 11.8% above its 20-day average; the cap is 10%.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09) and the sell re-entry lock ($5.75 is above the $5.74 sell price).
- **ROIV, CNC** (held, top-up): passed the gate. No top-up: each is already above its $11.85 target ($12.38 and $13.09).
- **SKM** (held, top-up): passed the gate. No top-up: $0.04 of headroom is below the $5 minimum.

**Orders placed:** none.

Cash: $42.86. Open positions: 5 of 5 (ROIV, CNC, NWL, FROG, SKM).
