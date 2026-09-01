# ORB Sierra Historical-Data Repair Audit

**Status:** Complete  
**Repair date:** August 31, 2026  
**Inference endpoint:** December 31, 2023

## Trigger

An official-calendar reconciliation of the pre-repair Databento OHLCV source found 439 scheduled NQ sessions and 440 scheduled ES sessions absent from the 2011–2017 baseline. Databento separately documents a legacy CME MDP2 OHLCV defect affecting data before May 21, 2017. Draft 4 and every pre-repair output were frozen before replacement data were inspected.

## Frozen repair design

The repair protocol was frozen before the repaired NQ/ES headline estimates or YM/RTY extension results were inspected. It required a uniform Sierra Chart Historical Data Service source, quarterly outright contracts, prior-session total-volume contract selection, raw unadjusted prices, exact one-minute aggregation, and a complete 09:30–13:59 New York research window.

Protocol SHA-256:

```text
dd1e6bd545dedd5ca45663cf46c5bb86633d53672533ce11a27c19e9c698aa2a
```

## Source inventory and reconstruction

The source inventory contains 186 of 186 expected non-empty contract files: 53 NQ, 53 ES, 53 YM, and 27 RTY files. March 2024 contracts were included because they can be the prior-session volume leader during the final trading days of December 2023. This endpoint correction was made before repaired headline results were computed.

All source headers and record sizes validated. Across approximately 18.96 million source records, 797 records were out of timestamp order and none had invalid price or volume fields. Records were aggregated into minute dictionaries and sorted before continuous-series construction, so the final outputs are ordered and unique by minute.

The sanitized source manifest removes server paths and session-volume caches while preserving contract symbols, source hashes, record counts, timestamp bounds, validation counts, minute-file hashes, and continuous-output metadata.

## Calendar reconciliation

The repaired NQ baseline contains 1,748 scheduled full-window sessions, of which 3 are absent from source, 29 are observed but incomplete, 1,716 contain all 270 bars, and 1,693 generate signals. The corresponding ES chain is 1,748, 4, 27, 1,717, and 1,703. Complete-window coverage is therefore 98.17% for NQ and 98.23% for ES, compared with approximately 75% in the defective source.

For 2018–2023, the repaired complete-session and signal counts reproduce the legacy counts exactly. The few remaining absent baseline dates are recorded individually in the calendar audit.

## Unaffected-period reconciliation

For 2018–2023, the repaired and legacy sources choose the same contract symbol on every common NQ and ES bar. They produce exactly the same signal dates: 1,470 NQ and 1,483 ES. Outcome categories agree on every trade. Gross R differs on 20 NQ dates and 11 ES dates because of small vendor-level OHLC differences; only 4 NQ dates and 1 ES date have different opening-range risk width.

## Repaired headline results

The repaired late-minus-baseline change is +0.1152798R for NQ and +0.1101464R for ES. The pre-repair values were +0.1205R and +0.1022R. Thus the main descriptive result survives recovery of roughly one quarter of the former baseline calendar.

| Market | Measure | Pre-repair | Repaired |
|---|---|---:|---:|
| NQ | Baseline trades | 1,287 | 1,693 |
| NQ | Baseline net expectancy | -0.049R | -0.044R |
| NQ | Late-minus-baseline change | +0.1205R | +0.1153R |
| ES | Baseline trades | 1,296 | 1,703 |
| ES | Baseline net expectancy | -0.058R | -0.066R |
| ES | Late-minus-baseline change | +0.1022R | +0.1101R |

The late-period trade sets are unchanged. The before-and-after contrast therefore isolates the material effect of repairing the defective baseline rather than a redefinition of the headline periods.

Under intact six-month grouping, the repaired intervals are [-0.0169R, +0.2474R] for NQ and [-0.0302R, +0.2505R] for ES. Both continue to include zero.

The payoff-rule-independent close-horizon signed-return changes are +0.1284R for NQ and +0.1279R for ES. None of the 30 path contrasts survives Benjamini–Hochberg correction.

The repaired large-contract friction shares in the 2022–2023 comparison are 10.0% for NQ and 9.2% for ES. Under the one-tenth point-value counterfactual they become 52.6% and 50.4%, while gross outcome components remain unchanged by construction.

The frozen YM extension changes from +0.0616R before repair to +0.0732R after repair and remains below the +0.08R magnitude threshold. RTY now contains 105 baseline trades, clears the frozen count threshold, has the same positive sign, and produces only +0.0059R. The joint magnitude criterion therefore still fails, now because both evaluated extensions are below +0.08R.

## Canonical hashes

```text
NQ  6567af5416544f9b6cfe728823149b05fe0737dd746fec91868268ff87e2432a
ES  a054658ea943b673d70dc20d6c8b9d997b1afbde52e58f35410bc7bc7ccfdb20
YM  ea2b082566311dfd24ed926ace2315e9bb65f91a8da5e2689eab102a800a83b4
RTY c91c89a033086051b5228ab77be5336851fc32b39bd789dc1fd9110bbf9f27c1
```

Public source manifest SHA-256:

```text
4416fb67c27e021590bae4175f39da7bdb28979c9d3231d302181e5b705db893
```

## Evidentiary conclusion

The repair changes the provenance and sample size materially but not the paper's central hierarchy of claims. The historical economic shift remains large and positive but uncertain under coarse serial-dependence treatment. The signal-content evidence remains suggestive and multiplicity-sensitive. The point-value scaling identity and the separation of cost scale from eligibility scale remain exact accounting results.
