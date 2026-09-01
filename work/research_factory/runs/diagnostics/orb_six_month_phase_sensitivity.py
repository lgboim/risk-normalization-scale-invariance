#!/usr/bin/env python3
"""Post-hoc sensitivity of six-month inference to calendar-block phase.

The manuscript's reported grouping uses January--June and July--December
blocks.  This audit shifts the six-month calendar partition by zero through
five months while retaining all observations.  Non-aligned partitions can
therefore contain shorter leading and trailing edge blocks.  The point
estimate is unchanged; only the block-based uncertainty calculation varies.
"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import t as student_t

import orb_paper_lineage_audit as lineage

HERE = Path(__file__).resolve().parent
OUT = HERE / "orb_six_month_phase_sensitivity.json"
WIDTH = 6


def month_number(value: str) -> int:
    year, month = map(int, value.split("-"))
    return year * 12 + month - 1


def collapse(months: list[str], sums: np.ndarray, counts: np.ndarray,
             phase: int) -> tuple[np.ndarray, np.ndarray, list[dict]]:
    """Group months by a globally anchored six-month calendar partition."""
    grouped: dict[int, list[int]] = defaultdict(list)
    for index, month in enumerate(months):
        bucket = (month_number(month) - phase) // WIDTH
        grouped[bucket].append(index)

    block_sums, block_counts, metadata = [], [], []
    for bucket in sorted(grouped):
        indices = grouped[bucket]
        block_sums.append(float(sums[indices].sum()))
        block_counts.append(int(counts[indices].sum()))
        metadata.append({
            "first_month": months[indices[0]],
            "last_month": months[indices[-1]],
            "calendar_months_observed": len(indices),
            "trades": int(counts[indices].sum()),
        })
    return np.asarray(block_sums), np.asarray(block_counts), metadata


def infer(pre: tuple[list[str], np.ndarray, np.ndarray],
          late: tuple[list[str], np.ndarray, np.ndarray], phase: int) -> dict:
    aps, apn, ameta = collapse(*pre, phase)
    bps, bpn, bmeta = collapse(*late, phase)
    am = float(aps.sum() / apn.sum())
    bm = float(bps.sum() / bpn.sum())
    effect = bm - am
    au = aps - apn * am
    bu = bps - bpn * bm
    va = len(au) / (len(au) - 1) * float(au @ au) / float(apn.sum()) ** 2
    vb = len(bu) / (len(bu) - 1) * float(bu @ bu) / float(bpn.sum()) ** 2
    se = math.sqrt(va + vb)
    stat = effect / se
    df = min(len(au), len(bu)) - 1
    p = float(2 * student_t.sf(abs(stat), df))
    critical = float(student_t.ppf(0.975, df))
    return {
        "phase_months": phase,
        "effect_r": effect,
        "se_r": se,
        "t": stat,
        "df": df,
        "two_sided_p": p,
        "ci95_dual": [effect - critical * se, effect + critical * se],
        "pre_blocks": len(au),
        "late_blocks": len(bu),
        "pre_block_detail": ameta,
        "late_block_detail": bmeta,
    }


def monthly_arrays(market: str) -> dict[str, tuple[list[str], np.ndarray, np.ndarray]]:
    rows = lineage.trades(lineage.load_sessions(market), capped=False)
    point = lineage.POINT_VALUES[market]["full"]
    grouped = defaultdict(lambda: defaultdict(list))
    for row in rows:
        if row["era"] in ("2011-2017", "2022-2023"):
            value = float(row["gross_r"]) - lineage.COST / (point * float(row["risk"]))
            grouped[row["era"]][row["day"][:7]].append(value)

    result = {}
    for era in ("2011-2017", "2022-2023"):
        months = sorted(grouped[era])
        result[era] = (
            months,
            np.asarray([sum(grouped[era][month]) for month in months]),
            np.asarray([len(grouped[era][month]) for month in months]),
        )
    return result


def main() -> None:
    empirical = {}
    for market in ("NQ", "ES"):
        arrays = monthly_arrays(market)
        empirical[market] = [
            infer(arrays["2011-2017"], arrays["2022-2023"], phase)
            for phase in range(WIDTH)
        ]
    payload = {
        "status": "posthoc_block_phase_sensitivity",
        "primary_phase": 0,
        "primary_phase_definition": "January-June and July-December",
        "method": (
            "global six-month calendar partitions shifted by 0-5 months; "
            "all observations retained; shorter leading and trailing blocks allowed"
        ),
        "interpretation": (
            "The effect estimate is invariant to phase. Variations in intervals and p-values "
            "measure sensitivity of the deliberately coarse uncertainty calculation to block boundaries."
        ),
        "empirical": empirical,
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
