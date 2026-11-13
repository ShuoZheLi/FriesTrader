# 2026-11-13

Live cycle (Friday). Mode `live`, strategy version `cf1468c`. No orders were placed: no sell rule fired, all 5 slots were full, and no held position was below its target size. Open positions: 5 of 5.

This cycle ran at about 09:38 CT through a retry. The Robinhood connector failed to connect (502) when the 08:35 CT trigger fired.

**Loss-limit check:** clear.
- Realized P&L is $0.00 today and −$0.08 over the trailing week (−0.08%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $98.54
  - open-position cost basis: $53.99
  - unrealized P&L: +$1.69
  - all-time realized P&L: −$3.15

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $39.75 vs. $37.64 average cost (+5.6%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached (the first is at +15%).
  - It is 8.5% over its $11.82 target, so there is no trim.
- **CNC:** holding.
  - Price $68.95 vs. $68.28 average cost (+1.0%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 3.9% over target, so there is no trim.
- **NWL:** holding.
  - Price $5.72 vs. $5.82 average cost (−1.8%).
  - The volatility-scaled stop is 12.7%, so it did not trigger.
  - It is at its $5.91 target, so there is no trim.
- **FROG:** holding.
  - Price $108.41 vs. $100.71 average cost (+7.6%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 7.2% over target, so there is no trim.
- **SKM:** holding.
  - Price $34.18 vs. $33.91 average cost (+0.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 1.5% over target, so there is no trim.

**Candidates** (from Thursday afternoon's Phase A):
- **TTEK, HTFL, SONO, NIQ** (new, medium) and **INGM, AVAH** (new, low, dilution flag): no open slots (5 of 5 held). Skipped without a price re-check.
- **FROG** (held, top-up): skipped by the buy gate. It is 12.9% above its 20-day average; the cap is 10%.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09). The sell re-entry lock no longer applies, because the price is below the $5.74 sell price.
- **ROIV, CNC, SKM** (held, top-up): passed the gate. No top-up: each is already above its $11.82 target ($12.83, $12.29 and $12.00).

**Orders placed:** none.

Cash: $42.86. Open positions: 5 of 5 (ROIV, CNC, NWL, FROG, SKM).
