# 2026-11-04

Live cycle (Wednesday). Mode `live`, strategy version `c58f391`. Two orders were placed: RNG was sold as an `exit_existing`, and a new JAN position was bought. All five position slots are filled again.

**Loss-limit check:** clear.
- Realized P&L is −$0.80 today (−0.80%) and −$1.33 this week (−1.33%), so entries are not halted.
- `net_deposits_usd` is $100.00, computed from:
  - total value: $100.00
  - open-position cost basis: $48.06
  - unrealized P&L: +$1.33
  - all-time realized P&L: −$1.33

**Held positions** (stop-loss, take-profit and trim checks):
- **RNG:** sold.
  - Tuesday's Phase A marked it `exit_existing`: the second straight close was below the ~$79.42 pre-report level, after the early-exit guard window had passed (the opening buy was 10-26, 7 trading days ago).
  - Sold 0.244276 shares, filled at $79.47, realizing −$0.80.
  - No wash-sale flag: the position is fully closed.
  - Before the sale, the stop (8.80%) had not triggered: drawdown was 4.1%.
- **CLF:** holding.
  - Price $14.04 vs. $13.15 average cost (+6.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached, and there is no trim.
- **ROIV:** holding.
  - Price $36.45 vs. $37.64 average cost (−3.2%).
  - The stop is 6.07% and was not triggered. No take-profit tier was reached, and there is no trim.
- **CNC:** holding.
  - Price $71.70 vs. $68.28 average cost (+5.0%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - Conviction is low, so the target is $6.00. The position is 114% over target: overweight cycle 2 of 3. A trim fires next cycle if conviction stays below high and the overage stays above 25%.
- **NWL:** holding.
  - Price $5.96 vs. $5.82 average cost (+2.3%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached, and there is no trim.

**Candidates** (from Tuesday afternoon's Phase A; one slot opened after the RNG sale):
- **JAN** (new, medium): approved and bought for $12.00. It passed the buy gate:
  - gap +2.3% vs. thesis price; re-checked, with no invalidating news
  - 6.1% above its 20-day average
  - next earnings 74 trading days away
- **NBIX** (new, high): skipped by the buy gate. It is 16.2% above its 20-day average after its post-earnings jump.
- **GKOS** (new, medium): skipped by the buy gate. The price gapped 4.0% above the thesis price, and it is 31.0% above its 20-day average.
- **FISV** (new, low): skipped by the buy gate. The price gapped 4.3%, and it is 25.9% above its 20-day average.
- **INGM** (new, low, `dilution_risk`): passed the buy gate, but was rejected because its conviction is below the medium minimum for new entries.
- **CLF** (held, medium, top-up): passed the gate. No top-up: it is already above its $12.00 target.
- **ROIV** (held, top-up): skipped for the earnings blackout. Its next earnings is 2026-11-09, 3 trading days away.
- **CNC** (held, top-up): skipped by the buy gate. The price gapped 6.7% above the thesis price.
- **NWL** (held, top-up): skipped by the buy gate. The price gapped 6.5% above the thesis price.

**Orders placed:**
- RNG sell, 0.244276 shares. Filled at $79.47. Order `6aeb4326-c482-4105-9e3e-c6e95b72b170`.
- JAN buy, $12.00. Filled 0.396939 shares at $30.2313. Order `6aeb4371-f709-4533-bc78-4f4f61ac732e`.

Cash: about $38.61. Open positions: 5 of 5 (CLF, ROIV, CNC, NWL, JAN).
