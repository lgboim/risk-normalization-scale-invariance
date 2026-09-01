#!/usr/bin/env python3
"""Post-hoc moving-block bootstrap sensitivity for the scale-paper contrast."""
from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SERIES_DIR = ROOT / "work/sierra_repair/current"
os.environ["ORB_SERIES_DIR"] = str(SERIES_DIR)
os.environ["ORB_END_DATE"] = "2023-12-31"

import orb_paper_lineage_audit as lineage  # noqa: E402
import regime_open_runner as regime  # noqa: E402

OUT_JSON = HERE / "orb_scale_paper_block_bootstrap_sensitivity.json"
OUT_CSV = HERE / "orb_scale_paper_block_bootstrap_sensitivity.csv"
REPETITIONS = 20_000
BLOCK_TRADES = 10
SEED = 20_260_901


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> None:
    results = {}
    for offset, market in enumerate(("NQ", "ES")):
        rows = lineage.trades(lineage.load_sessions(market), capped=False)
        point_value = lineage.POINT_VALUES[market]["full"]
        for row in rows:
            row["net_r"] = (
                float(row["gross_r"])
                - lineage.COST / (point_value * float(row["risk"]))
            )
        baseline = [
            {"r": row["net_r"]}
            for row in rows
            if row["era"] == "2011-2017"
        ]
        late = [
            {"r": row["net_r"]}
            for row in rows
            if row["era"] == "2022-2023"
        ]
        result = regime.contrast(
            baseline,
            late,
            REPETITIONS,
            BLOCK_TRADES,
            SEED + offset,
        )
        results[market] = {
            "n_baseline": len(baseline),
            "n_late": len(late),
            "estimate_r": result["effect_mean_r"],
            "percentile_range_95": result["bootstrap_95pct"],
            "two_sided_block_permutation_p": result["pvalue"],
        }

    payload = {
        "status": "posthoc_sensitivity",
        "estimand": "trade-weighted 2022-2023 minus 2011-2017 benchmark net R",
        "method": (
            "separate circular moving-block bootstrap within each era; "
            "consecutive trade blocks"
        ),
        "block_length_trades": BLOCK_TRADES,
        "repetitions": REPETITIONS,
        "seed": SEED,
        "canonical_sources": {
            market: {
                "path": str(lineage.SOURCES[market].relative_to(ROOT)),
                "sha256": digest(lineage.SOURCES[market]),
            }
            for market in ("NQ", "ES")
        },
        "results": results,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "market",
                "n_baseline",
                "n_late",
                "estimate_r",
                "range_low",
                "range_high",
                "two_sided_block_permutation_p",
            ),
        )
        writer.writeheader()
        for market, result in results.items():
            writer.writerow(
                {
                    "market": market,
                    "n_baseline": result["n_baseline"],
                    "n_late": result["n_late"],
                    "estimate_r": result["estimate_r"],
                    "range_low": result["percentile_range_95"][0],
                    "range_high": result["percentile_range_95"][1],
                    "two_sided_block_permutation_p": result[
                        "two_sided_block_permutation_p"
                    ],
                }
            )
    print(json.dumps({"json": str(OUT_JSON), "csv": str(OUT_CSV)}))


if __name__ == "__main__":
    main()
