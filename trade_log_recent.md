# 2026-11-06

Live cycle (Friday). Mode `live`, strategy version `f9f2ceb`. One order was placed: CLF was sold as an `exit_existing`. There were no buys, so 3 of 5 slots are in use.

**Loss-limit check:** clear.
- Realized P&L is −$1.47 today (−1.47%) and −$3.07 this week (−3.07%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $96.75
  - open-position cost basis: $36.07
  - unrealized P&L: −$0.18
  - all-time realized P&L: −$3.07

**Held positions** (stop-loss, take-profit and trim checks):
- **CLF:** sold.
  - Thursday's Phase A marked it `exit_existing`.
  - The early-exit guard did not apply: the position was opened 10-20, more than 5 trading days ago.
  - Sold 0.911794 shares, filled at $11.54, realizing −$1.47.
  - No wash-sale flag: the position is fully closed.
  - Before the sale, the stop had not triggered. Price was $11.555 vs. $13.15 average cost, a 12.1% drawdown. The stop is 15.00%: 20-day volatility 6.04% × 2.5, capped at the 15% maximum.
- **ROIV:** holding.
  - Price $37.19 vs. $37.64 average cost (−1.2%).
  - The stop is 7.11% and was not triggered. No take-profit tier was reached, and there is no trim.
- **CNC:** holding.
  - Price $72.22 vs. $68.28 average cost (+5.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached; the first tier is at +15%.
  - It is 11.5% over its $11.61 target, so there is no trim.
- **NWL:** holding.
  - Price $5.40 vs. $5.82 average cost (−7.2%).
  - The stop is 12.39% and was not triggered. No take-profit tier was reached.
  - Conviction is low, so the target is $5.80. The position is 89% over target: overweight cycle 2 of 3.

**Candidates** (from Thursday afternoon's Phase A; two slots were open after the CLF sale):
- **BSY, U, MGNI, FWONK** (new, medium): all skipped by the buy gate after their post-earnings jumps.
  - They are 13.6%, 21.9%, 16.8% and 13.7% above their 20-day averages; the cap is 10%.
  - U also gapped 4.3% above its thesis price; the cap is 3%.
- **ADMA** (new, low): skipped by the buy gate. It is 19.7% above its 20-day average, and its low conviction would also have blocked a new entry.
- **ROIV** (held, top-up): skipped for the earnings blackout. Its next earnings is 2026-11-09, 1 trading day away.
- **CNC** (held, medium, top-up): passed the gate. No top-up: it is already above its $11.61 target ($12.95).
- **NWL** (held, low, top-up): passed the gate. No top-up: it is already above its $5.80 target ($10.96).

**Orders placed:**
- CLF sell, 0.911794 shares. Filled at $11.54. Order `6aede635-e374-4be1-8359-27f4c67ef724`.

Cash: $60.86. Open positions: 3 of 5 (ROIV, CNC, NWL).
