# 2026-11-03

Live cycle (Tuesday). Mode `live`, strategy version `c69fbf9`. One order was placed: a new NWL position. All five position slots are now filled.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and −$0.53 this week (−0.53% of net deposits), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $98.05
  - open-position cost basis: $56.50
  - unrealized P&L: −$1.42
  - all-time realized P&L: −$0.53

**Held positions** (stop-loss, take-profit and trim checks):
- **CLF:** holding.
  - Price $14.10 vs. $13.15 average cost (+7.2%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - The position is 9.3% over target; the trim trigger is 25%.
- **ROIV:** holding.
  - Price $36.39 vs. $37.64 average cost (−3.3%).
  - The stop is 6.22% (20-day volatility 2.49% × 2.5) and was not triggered. No take-profit tier was reached, and there is no trim.
- **RNG:** holding.
  - Price $76.11 vs. $82.73 average cost (−8.0%). The stop is 8.82% (20-day volatility 3.53% × 2.5) and was not triggered, but it is close.
  - No take-profit tier was reached.
  - Yesterday's Phase A lowered conviction to low, so the target is now $5.88. The position is 216% over target: overweight cycle 1 of 3 before a trim can fire.
- **CNC:** holding.
  - Price $66.80 vs. $68.28 average cost (−2.2%).
  - The stop is 5.00% (the floor) and was not triggered. No take-profit tier was reached.
  - Conviction is now low, so the target is $5.88. The position is 102% over target: overweight cycle 1 of 3 before a trim can fire.

**Candidates** (from Monday afternoon's Phase A):
- **NWL** (new, medium): approved and bought for $11.77. It passed the buy gate:
  - gap −1.8% vs. thesis price
  - 5.8% above its 20-day average
  - next earnings 64 trading days away
- **EL** (new, medium): passed the buy gate, but the last slot went to NWL, which ranks higher (16.3% vs. 13.7% below its 52-week high).
- **TEM** (new, medium): skipped by the buy gate.
  - The price gapped 5.1% above the thesis price ($78.47 → $82.46), and it is 18.0% above its 20-day average.
- **EXEL** (new, low, `active_litigation`): skipped by the buy gate.
  - It is 13.5% above its 20-day average. Its low conviction would also have blocked a new entry.
- **ROIV** (held, medium, top-up): skipped for the earnings blackout.
  - Its next earnings is 2026-11-09, 4 trading days away.
- **CLF** (held, medium, top-up): passed the gate. No top-up: it is already above its $11.77 target.
- **RNG** and **CNC** (held, low, top-ups): passed the gate. No top-up: both are well above their $5.88 low-tier target.
- **VG** (avoid): not processed.

**Orders placed:**
- NWL buy, $11.77. Filled 2.021711 shares at $5.8218. Order `6ae9f1bb-1181-4035-9776-06b6cad8e12a`.

Cash: about $31.20. Open positions: 5 of 5 (CLF, ROIV, RNG, CNC, NWL).
