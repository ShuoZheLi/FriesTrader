# 2026-11-10

Live cycle (Tuesday). Mode `live`, strategy version `ee0bb51`. No orders were placed: no sell rule fired, and every buy candidate was blocked or already at target. Open positions: 4 of 5.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and −$2.62 over the trailing week (−2.62%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $98.10
  - open-position cost basis: $42.09
  - unrealized P&L: +$1.25
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $40.29 vs. $37.64 average cost (+7.0%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 10.4% over its $11.77 target, so there is no trim.
- **CNC:** holding.
  - Price $68.50 vs. $68.28 average cost (+0.3%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 3.7% over its $11.77 target, so there is no trim.
- **NWL:** holding.
  - Price $5.74 vs. $5.82 average cost (−1.4%).
  - The stop is 13.14% and was not triggered. No take-profit tier was reached.
  - It is about at its $5.89 target after yesterday's trim, so there is no trim.
- **FROG:** holding.
  - Price $104.50 vs. $100.71 average cost (+3.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 3.7% over its $11.77 target, so there is no trim.

**Candidates** (from Monday afternoon's Phase A; one slot was open):
- **TGTX, VIR, WRBY** (new, medium): skipped by the buy gate. They are 14.6%, 23.2% and 19.6% above their 20-day averages; the cap is 10%.
- **LFST, TIC** (new, low, with risk flags): skipped by the buy gate. They are 11.2% and 14.9% above their 20-day averages, and their low conviction would also have blocked a new entry.
- **ROIV, FROG** (held, top-up): skipped by the buy gate. They are 11.3% and 11.4% above their 20-day averages.
- **NWL** (held, top-up): skipped by the wash-sale guard, because of yesterday's loss-realizing trim.
- **CNC** (held, top-up): passed the gate. No top-up: it is already above its $11.77 target ($12.20).

**Orders placed:** none.

Cash: $54.76. Open positions: 4 of 5 (ROIV, CNC, NWL, FROG).
