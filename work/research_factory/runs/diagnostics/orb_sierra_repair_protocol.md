# ORB Sierra Chart Historical-Data Repair Protocol

**Status:** Frozen before inspecting repaired NQ/ES headline or YM/RTY replication results  
**Frozen:** 2026-08-31  
**Purpose:** Replace the defective legacy Databento OHLCV baseline with a uniform historical source and rerun the complete manuscript pipeline.

## Scope

- Headline markets: E-mini Nasdaq-100 (`NQ`) and E-mini S&P 500 (`ES`).
- Replication markets: E-mini Dow (`YM`) and E-mini Russell 2000 (`RTY`).
- Contracts: all quarterly NQ, ES, and YM outright contracts needed to cover sessions from 2011 through 2023, including the March 2024 contracts active in late December 2023; RTY begins with the September 2017 contract and follows the same endpoint convention.
- Source: Sierra Chart Historical Data Service, accessed under Service Package 3.
- Stored resolution: one-minute intraday records. This is the finest resolution required by the frozen ORB rule and avoids mixing tick- and minute-derived periods.
- Time zone: source records are UTC; research sessions are converted to `America/New_York` with daylight-saving transitions.
- Research window: 09:30 through 13:59 New York time.

## Canonical reconstruction

1. Download every in-scope quarterly NQ, ES, YM, and RTY contract from the same Sierra Chart pipeline.
2. Validate every `.scid` header, record size, monotonic timestamp order, price fields, volume fields, and first/last timestamp.
3. Aggregate source records to exact one-minute OHLCV bars when necessary. Empty minutes remain absent; they are not forward-filled.
4. Assign evening trading to the following New York trading date.
5. Select the daily continuous contract using total volume in the preceding eligible full session. Same-day volume is not used.
6. Preserve raw unadjusted prices across rolls.
7. Write the continuous research files only for the frozen 09:30--13:59 window; full-session contract records remain the source for prior-session volume selection.
8. Require all 270 bars from 09:30 through 13:59 for the headline session universe.
9. Reconcile scheduled sessions against an independent CME equity-index futures calendar and classify every exclusion.

## Frozen trading rule

- Opening range: 09:30 through 09:59.
- Entry search: 10:00 through 13:59.
- Entry: first one-sided break of either opening-range boundary.
- A minute crossing both boundaries is skipped; the search continues.
- Stop: one opening-range width.
- Target: `+1.5R`.
- Time exit: 13:59 close.
- Entry-bar stop is charged; entry-bar target is not credited.
- On later bars touching both stop and target, stop receives priority.
- Headline cost: four U.S. dollars round trip.
- Headline universe: no opening-range filter.

## Required validation before results are inspected

- Produce a contract-file inventory with SHA-256, size, record count, and timestamp bounds.
- Reconcile Sierra-derived one-minute bars against the unaffected Databento period from 2018 through 2023 at both bar and signal levels.
- Report contract-leader disagreements and determine whether they arise from volume definitions, roll timing, or source defects.
- Produce the calendar chain: scheduled session to source-observed session to complete 270-bar session to signal.
- Do not copy any pre-repair headline estimate into repaired outputs.

## Required reruns

The repaired source must regenerate the period table, headline deltas, serial-dependence calibration, signal-content audit, drift controls, decomposition, point-value counterfactual, eligibility analysis, execution sensitivity, frozen YM/RTY status where source-dependent, all figures, and the replication manifest.

The pre-repair manuscript remains archived and marked not for citation. No claim is retained merely because it appeared in the earlier draft.
