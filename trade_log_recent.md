# 2026-10-23

Live cycle (Friday). Mode `live`, strategy version `39d7edd`. No orders were placed today.

**Loss-limit check:** clear. No realized P&L today or this week. `net_deposits_usd` is $100.00 (total value $100.18, open-position cost basis $36.13, unrealized +$0.18). Entries not halted.

**Held positions:**
- **AVTR**: holding. $16.96 vs. $16.51 average cost (+2.7%), a gain, so no stop was computed. No take-profit tier reached. The position is $12.33 vs. the $12.02 target, 2.6% over (trim trigger is 25%), so no trim.
- **CLF**: holding. $13.26 vs. $13.15 average cost (+0.8%), a gain, so no stop was computed. No take-profit tier reached. The position is $12.09 vs. the $12.02 target, so no trim.
- **ROIV**: holding. $36.90 vs. $37.64 average cost (−2.0%). The stop is 6.14% (20-day volatility 2.46% × 2.5), so it did not trigger. No take-profit tier reached, and no trim.

**Candidates** (from yesterday afternoon's Phase A):
- **WCN** (long, low, `active_litigation` flag, new): blocked. The price is 17.1% above its 20-day average ($159.16 → $186.45); the limit is 10%.
- **AVTR** (long, medium, top-up): blocked by the earnings blackout. Q3 earnings on Oct 28 are 3 trading days away.
- **CLF** (long, medium, top-up): passed the buy gate, but the position is already at its target size, so there is no top-up.
- **ROIV** (long, medium, top-up): passed the buy gate, but there is only $0.12 of headroom to target, below the $5.00 minimum top-up.
- **BBT** (long, low, new): passed the buy gate, but sizing rejected it. Low conviction is below the `medium` minimum for new entries.

Cash: $63.87, unchanged. Open positions: 3 of 4 (AVTR, CLF, ROIV).
