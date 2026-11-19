# 2026-11-19

Live cycle (Thursday). Mode `live`, strategy version `19210a9`. Three orders were placed and filled: CNC was sold (exit), FROG was trimmed by its first take-profit tier, and HTHT was bought as a new entry. Open positions: 5 of 5.

**Loss-limit check:** clear.
- Realized P&L is +$0.30 today and +$0.30 over the trailing week, so entries are not halted.
- `net_deposits_usd` is $100.00, computed after this cycle's sells from:
  - total value: $98.67
  - open-position cost basis: $38.89
  - unrealized P&L: +$1.52
  - all-time realized P&L: −$2.85

**Held positions** (stop-loss, take-profit and trim checks):
- **ROIV:** holding.
  - Price $39.07 vs. $37.64 average cost (+3.8%).
  - It is at a gain, so no stop was computed. No take-profit tier was reached.
  - It is 6.2% over its $11.86 target, so there is no trim.
- **CNC:** sold in full (Phase A's `exit_existing`).
  - The close of $67.42 broke the ~$68.03 invalidation level after the managed-care Medicare-audit selloff.
  - Price $66.97 vs. $68.28 average cost (−1.9%). The 10.7% stop did not trigger.
- **NWL:** holding.
  - Price $5.56 vs. $5.82 average cost (−4.5%).
  - The volatility-scaled stop is 12.5%, so it did not trigger.
  - It is near its $5.93 target, so there is no trim.
- **FROG:** the first take-profit tier fired.
  - Price $121.53 vs. $100.71 average cost (+20.7%).
  - The +15% tier sold 25% of the position (0.029218 shares). The +30% and +50% tiers remain.
  - No stop was computed (at a gain), and there is no trim.
- **SKM:** holding.
  - Price $32.73 vs. $33.91 average cost (−3.5%).
  - The volatility-scaled stop is 7.2%, so it did not trigger.
  - It is at its target, so there is no trim.

**Candidates** (from Wednesday afternoon's Phase A; CNC's exit freed 1 slot):
- **HTHT** (new, medium): approved and sized at $11.84. It passed the buy gate: ask $52.16 vs. $52.44 thesis price, and 5.7% above its 20-day average.
- **WWW** (new, medium): skipped by the buy gate. It is 15.5% above its 20-day average; the cap is 10%.
- **SLS** (new, low, dilution flag): skipped by the buy gate. It is 60.7% above its 20-day average.
- **FROG** (held, top-up): not eligible, because a take-profit tier fired this cycle.
- **NWL** (held, top-up): skipped by the wash-sale guard (loss-realizing trim on 11-09).
- **ROIV** (held, top-up): passed the gate. No top-up: it is already above its $11.84 target.
- **SKM** (held, top-up): passed the gate. No top-up: $0.37 of headroom is below the $5 minimum.

**Orders placed** (all live and filled):
- **CNC:** sell 0.178098 shares at $66.60 (about $11.86, realized −$0.30).
- **FROG:** sell 0.029218 shares at $121.28 (about $3.54, realized +$0.60).
- **HTHT:** buy $11.84 → 0.227429 shares at $52.06.

Cash: about $46.42. Open positions: 5 of 5 (ROIV, NWL, FROG, SKM, HTHT).
