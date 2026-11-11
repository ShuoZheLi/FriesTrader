# 2026-11-11

Live cycle (Wednesday). Mode `live`, strategy version `cb211dc`. No orders were placed: no sell rule fired, and every buy candidate was blocked or rejected by sizing. Open positions: 4 of 5.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and −$1.82 over the trailing week (−1.82%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $99.45
  - open-position cost basis: $42.09
  - unrealized P&L: +$2.60
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $41.09 vs. $37.64 average cost (+9.2%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached (the first is at +15%).
  - It is 11.1% over its $11.93 target, so there is no trim.
- **CNC:** holding.
  - Price $70.72 vs. $68.28 average cost (+3.6%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 5.6% over target, so there is no trim.
- **NWL:** holding.
  - Price $5.85 vs. $5.82 average cost (+0.5%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is about at its $5.97 target, so there is no trim.
- **FROG:** holding.
  - Price $109.43 vs. $100.71 average cost (+8.7%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 7.2% over target, so there is no trim.

**Candidates** (from Tuesday afternoon's Phase A; one slot was open):
- **TGTX, TTWO** (new, medium): skipped by the buy gate. They are 10.8% and 11.5% above their 20-day averages; the cap is 10%.
- **LFST** (new, low, dilution flag): skipped by the buy gate. It is 12.5% above its 20-day average.
- **FA** (new, low, dilution flag): passed the gate. Rejected by sizing: low conviction is below the medium minimum for new entries.
- **ROIV** (held, top-up): skipped by the buy gate. It is 12.3% above its 20-day average.
- **FROG** (held, top-up): skipped by the buy gate. It opened 6.1% above its thesis price and is 16.5% above its 20-day average.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09) and the sell re-entry lock.
- **CNC** (held, top-up): passed the gate. No top-up: it is already above its $11.93 target ($12.60).

**Orders placed:** none.

Cash: $54.76. Open positions: 4 of 5 (ROIV, CNC, NWL, FROG).
