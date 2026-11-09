# 2026-11-09

Live cycle (Monday). Mode `live`, strategy version `67bda35`. Two orders were placed: a conviction trim on NWL, and a new entry in FROG. Open positions are now 4 of 5.

**Loss-limit check:** clear.
- Realized P&L is −$0.08 today (−0.08%) and −$2.62 over the trailing week (−2.62%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $98.09
  - open-position cost basis: $30.32
  - unrealized P&L: +$1.24
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $39.98 vs. $37.64 average cost (+6.2%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 9.9% over its $11.73 target, so there is no trim.
  - Fiscal Q2 was reported this morning: EPS −$0.27 vs. a −$0.46 estimate.
- **CNC:** holding.
  - Price $70.15 vs. $68.28 average cost (+2.7%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 6.5% over its $11.73 target, so there is no trim.
- **NWL:** trimmed.
  - Price $5.67 vs. $5.82 average cost (−2.6%).
  - The stop is 12.38% and was not triggered. No take-profit tier was reached.
  - Conviction is low and the position was 96% over its $5.86 target for a third consecutive cycle, so the conviction trim fired.
  - Sold 0.987654 shares at $5.74 (about $5.67), realizing −$0.08.
  - Possible wash-sale flag: the 1.034057 shares still held are the rest of the same 11-03 purchase. This is informational only.

**Candidates** (from Friday afternoon's Phase A):
- **Weekend-gap check:** one search per candidate found no Saturday or Sunday news that contradicts any thesis.
- **FROG** (new, medium): passed the gate.
  - The price is 0.3% below the thesis price and 7.6% above its 20-day average.
  - Approved and sized at $11.77, then bought.
- **VNT** and **LION** (new, medium): skipped by the buy gate. They are 21.1% and 19.5% above their 20-day averages; the cap is 10%.
- **EXTR** and **GH** (new, medium): skipped by the buy gate. They opened 3.6% and 3.9% above their thesis prices; the cap is 3%.
- **ROIV** (held, top-up): skipped by the buy gate. It opened 4.6% above its thesis price and is 13.2% above its 20-day average.
- **CNC** (held, top-up): passed the gate. No top-up: it is already above its $11.77 target ($12.51).
- **NWL** (held, top-up): not eligible, because it was trimmed this cycle.

**Orders placed:**
- NWL sell (conviction trim), 0.987654 shares. Filled at $5.74. Order `6af1daaa-80c9-4217-bac8-181a640ff211`.
- FROG buy, $11.77. Filled 0.11687 shares at $100.7099. Order `6af1dae6-7635-41fa-935d-4db0e1e197df`.

Cash: about $54.76. Open positions: 4 of 5 (ROIV, CNC, NWL, FROG).
