# Databento issue snapshot: incomplete historical CME Globex bars

- Retrieval date: 2026-09-01
- Canonical URL: https://issues.databento.com/roadmap/cme-globex-mdp2-data-has-incomplete-bars-for-many-days
- Displayed title: `CME Globex MDP2 data has incomplete bars for many days`
- Displayed status: `Fix in progress`
- Displayed tags: `bug`, `data-quality`
- Internal issue identifier shown in page metadata: `D-8175`

## Substantive content recorded at retrieval

The page metadata states that, on many dates before 2017-05-21, historical CME Globex OHLCV requests can return substantially fewer bars than traded intervals because much of a day's activity is folded into one bar. The page lists known affected dates but does not claim that the list is exhaustive.

The issue title uses `MDP2`, while the page description refers to `GLBX.MDP3`. The manuscript therefore describes the externally documented object as older CME Globex historical OHLCV data and does not rely on the feed-version label to attribute every failed session.

## Research-use boundary

The public record supports the existence and general pattern of the pre-2017 bar problem. The counts of 439 failed NQ sessions and 440 failed ES sessions are results of the project's independent calendar audit, not figures reported by Databento. The manuscript consequently says that the audit pattern is consistent with the documented issue rather than asserting that the public issue record proves every date-level attribution.
