#!/usr/bin/env python3
"""Corrective audit: align the paper's signal universe and Shapley decomposition."""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import os
import statistics
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE / "orb_paper_lineage_audit_results.json"
AUDIT_TABLE = HERE / "orb_paper_decomposition_audit_table.csv"
NY = ZoneInfo("America/New_York")
END = date.fromisoformat(os.environ.get("ORB_END_DATE", "2026-08-26"))
COST = 4.0
_SERIES_DIR = os.environ.get("ORB_SERIES_DIR")
SOURCES = {
    "NQ": (Path(_SERIES_DIR) / "NQ_sierra_volume_continuous_1m.csv.gz"
           if _SERIES_DIR else ROOT / "work/databento/continuous/NQ_volume_continuous_1m.csv.gz"),
    "ES": (Path(_SERIES_DIR) / "ES_sierra_volume_continuous_1m.csv.gz"
           if _SERIES_DIR else ROOT / "work/databento/continuous/ES_volume_continuous_1m.csv.gz"),
}
POINT_VALUES = {
    "NQ": {"full": 20.0, "micro": 2.0},
    "ES": {"full": 50.0, "micro": 5.0},
}
EXPECTED_COUNTS = {
    "NQ": {"2011-2017": 1287, "2018-2019": 488, "2020-2021": 492, "2022-2023": 490},
    "ES": {"2011-2017": 1296, "2018-2019": 492, "2020-2021": 496, "2022-2023": 495},
}
REPAIRED_EXPECTED_COUNTS = {
    "NQ": {"2011-2017": 1693, "2018-2019": 488, "2020-2021": 492, "2022-2023": 490},
    "ES": {"2011-2017": 1703, "2018-2019": 492, "2020-2021": 496, "2022-2023": 495},
}
REPAIRED_SOURCE_SHA256 = {
    "NQ": "6567af5416544f9b6cfe728823149b05fe0737dd746fec91868268ff87e2432a",
    "ES": "a054658ea943b673d70dc20d6c8b9d997b1afbde52e58f35410bc7bc7ccfdb20",
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def era(day: date) -> str:
    if day.year <= 2017:
        return "2011-2017"
    if day.year <= 2019:
        return "2018-2019"
    if day.year <= 2021:
        return "2020-2021"
    if day.year <= 2023:
        return "2022-2023"
    return "2024-2026"


def load_sessions(root: str) -> dict[date, list[dict[str, float | int]]]:
    grouped: dict[date, list[dict[str, float | int]]] = defaultdict(list)
    with gzip.open(SOURCES[root], "rt", newline="") as handle:
        for raw in csv.DictReader(handle):
            dt = datetime.fromisoformat(raw["ts_event"].replace("Z", "+00:00")).astimezone(NY)
            if dt.date() < date(2011, 1, 1) or dt.date() > END:
                continue
            minute = dt.hour * 60 + dt.minute
            if 570 <= minute < 840:
                grouped[dt.date()].append({
                    "ts": int(dt.timestamp()), "minute": minute,
                    "o": float(raw["open"]), "h": float(raw["high"]),
                    "l": float(raw["low"]), "c": float(raw["close"]),
                })
    complete = {}
    for day, rows in grouped.items():
        rows.sort(key=lambda row: int(row["ts"]))
        clocks = Counter(int(row["minute"]) for row in rows)
        if len(clocks) == 270 and all(clocks.get(minute) == 1 for minute in range(570, 840)):
            complete[day] = rows
    return complete


def trades(sessions: dict[date, list[dict[str, float | int]]], capped: bool) -> list[dict[str, Any]]:
    output = []
    for day, rows in sorted(sessions.items()):
        opening, active = rows[:30], rows[30:]
        high = max(float(row["h"]) for row in opening)
        low = min(float(row["l"]) for row in opening)
        risk = high - low
        if risk <= 0 or (capped and not 4.0 <= risk <= 120.0):
            continue
        for index, bar in enumerate(active):
            up = float(bar["h"]) >= high
            down = float(bar["l"]) <= low
            if up and down:
                continue
            if not up and not down:
                continue
            direction = 1 if up else -1
            entry = max(high, float(bar["o"])) if direction > 0 else min(low, float(bar["o"]))
            stop = entry - direction * risk
            target = entry + direction * 1.5 * risk
            stop_entry = float(bar["l"]) <= stop if direction > 0 else float(bar["h"]) >= stop
            if stop_entry:
                outcome, gross = "stop", -1.0
            else:
                outcome, gross = "time", None
                for later in active[index + 1:]:
                    stop_hit = float(later["l"]) <= stop if direction > 0 else float(later["h"]) >= stop
                    target_hit = float(later["h"]) >= target if direction > 0 else float(later["l"]) <= target
                    if stop_hit or target_hit:
                        outcome = "stop" if stop_hit else "target"
                        gross = -1.0 if stop_hit else 1.5
                        break
                if gross is None:
                    gross = direction * (float(active[-1]["c"]) - entry) / risk
            output.append({"day": day.isoformat(), "era": era(day), "risk": risk,
                           "outcome": outcome, "gross_r": gross})
            break
    return output


def select(rows: list[dict[str, Any]], label: str) -> list[dict[str, Any]]:
    if label != "2022-2026":
        return [row for row in rows if row["era"] == label]
    return [row for row in rows if date(2022, 1, 1) <= date.fromisoformat(row["day"]) <= END]


def shapley(pre: list[dict[str, Any]], post: list[dict[str, Any]], point_value: float) -> dict[str, Any]:
    categories = ("target", "stop", "time")

    def components(rows: list[dict[str, Any]]) -> tuple[dict[str, float], dict[str, float], float, float]:
        probabilities = {name: sum(row["outcome"] == name for row in rows) / len(rows)
                         for name in categories}
        conditional = {name: statistics.fmean(float(row["gross_r"]) for row in rows
                                               if row["outcome"] == name)
                       for name in categories}
        gross = statistics.fmean(float(row["gross_r"]) for row in rows)
        cost_drag = statistics.fmean(COST / (point_value * float(row["risk"])) for row in rows)
        return probabilities, conditional, gross, cost_drag

    p0, m0, g0, c0 = components(pre)
    p1, m1, g1, c1 = components(post)
    frequency_by_category = {
        name: .5 * (p1[name] - p0[name]) * (m0[name] + m1[name]) for name in categories
    }
    magnitude_by_category = {
        name: .5 * (m1[name] - m0[name]) * (p0[name] + p1[name]) for name in categories
    }
    frequency = sum(frequency_by_category.values())
    magnitude = sum(magnitude_by_category.values())
    friction = c0 - c1
    direct = (g1 - c1) - (g0 - c0)
    reconstruction = frequency + magnitude + friction
    if abs(reconstruction - direct) > 1e-12:
        raise AssertionError("Shapley identity failed")
    return {
        "n_pre": len(pre), "n_post": len(post),
        "gross_r_pre": g0, "gross_r_post": g1,
        "cost_drag_r_pre": c0, "cost_drag_r_post": c1,
        "net_r_pre": g0 - c0, "net_r_post": g1 - c1, "net_r_change": direct,
        "frequency_r": frequency, "time_exit_magnitude_r": magnitude,
        "friction_r": friction, "friction_share": friction / direct if direct else None,
        "frequency_by_category": frequency_by_category,
        "magnitude_by_category": magnitude_by_category,
        "identity_error": reconstruction - direct,
    }


def main() -> None:
    repaired_run = os.environ.get("ORB_REPAIR_RUN") == "1"
    legacy_run = os.environ.get("ORB_LEGACY_RUN") == "1"
    if repaired_run == legacy_run:
        raise RuntimeError(
            "Choose exactly one explicit source mode: ORB_REPAIR_RUN=1 or ORB_LEGACY_RUN=1"
        )
    if repaired_run:
        if not _SERIES_DIR:
            raise RuntimeError("ORB_REPAIR_RUN=1 requires ORB_SERIES_DIR to be set explicitly")
        if END != date(2023, 12, 31):
            raise RuntimeError("The canonical repaired paper run requires ORB_END_DATE=2023-12-31")
        for root, path in SOURCES.items():
            actual_sha = digest(path)
            if actual_sha != REPAIRED_SOURCE_SHA256[root]:
                raise RuntimeError(
                    f"{root} repaired-source hash mismatch: {actual_sha}"
                )

    payload: dict[str, Any] = {
        "study": "corrective paper lineage audit",
        "status": "posthoc_correction_not_preregistered",
        "source_end": END.isoformat(),
        "fixed_round_trip_cost_usd": COST,
        "sources": {}, "markets": {},
    }
    for root in ("NQ", "ES"):
        sessions = load_sessions(root)
        uncapped = trades(sessions, capped=False)
        capped = trades(sessions, capped=True)
        counts = {label: len(select(uncapped, label)) for label in EXPECTED_COUNTS[root]}
        expected_counts = REPAIRED_EXPECTED_COUNTS[root] if repaired_run else EXPECTED_COUNTS[root]
        if counts != expected_counts:
            raise AssertionError(f"{root} headline parity failed: {counts}")
        market = {"complete_sessions": len(sessions), "headline_uncapped_counts": counts,
                  "capped_counts": {label: len(select(capped, label)) for label in
                                    ("2011-2017", "2018-2019", "2020-2021", "2022-2023", "2022-2026")},
                  "same_universe_decomposition": {}}
        pre = select(uncapped, "2011-2017")
        for contract, point_value in POINT_VALUES[root].items():
            market["same_universe_decomposition"][contract] = {
                label: shapley(pre, select(uncapped, label), point_value)
                for label in ("2018-2019", "2020-2021", "2022-2023", "2022-2026")
            }
        if root == "NQ":
            capped_pre = select(capped, "2011-2017")
            market["capped_micro_decomposition"] = {
                label: shapley(capped_pre, select(capped, label), POINT_VALUES[root]["micro"])
                for label in ("2018-2019", "2020-2021", "2022-2023", "2022-2026")
            }
        payload["sources"][root] = {"path": str(SOURCES[root].relative_to(ROOT)),
                                     "sha256": digest(SOURCES[root])}
        payload["markets"][root] = market
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    fields = [
        "market", "mapping", "period", "n_pre", "n_post",
        "gross_r_pre", "gross_r_post", "cost_drag_r_pre", "cost_drag_r_post",
        "net_r_pre", "net_r_post", "delta_net_r", "frequency_r",
        "time_exit_magnitude_r", "friction_r", "friction_share",
        "reconstructed_delta_r", "identity_error",
    ]
    with AUDIT_TABLE.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for root in ("NQ", "ES"):
            decompositions = payload["markets"][root]["same_universe_decomposition"]
            for contract in ("full", "micro"):
                mapping = "large_contract" if contract == "full" else "micro_scale_counterfactual"
                for period, result in decompositions[contract].items():
                    reconstructed = (result["frequency_r"] + result["time_exit_magnitude_r"]
                                     + result["friction_r"])
                    if abs(result["net_r_change"] - reconstructed) >= 1e-12:
                        raise AssertionError("Audit-table identity failed")
                    writer.writerow({
                        "market": root, "mapping": mapping, "period": period,
                        "n_pre": result["n_pre"], "n_post": result["n_post"],
                        "gross_r_pre": result["gross_r_pre"],
                        "gross_r_post": result["gross_r_post"],
                        "cost_drag_r_pre": result["cost_drag_r_pre"],
                        "cost_drag_r_post": result["cost_drag_r_post"],
                        "net_r_pre": result["net_r_pre"],
                        "net_r_post": result["net_r_post"],
                        "delta_net_r": result["net_r_change"],
                        "frequency_r": result["frequency_r"],
                        "time_exit_magnitude_r": result["time_exit_magnitude_r"],
                        "friction_r": result["friction_r"],
                        "friction_share": result["friction_share"],
                        "reconstructed_delta_r": reconstructed,
                        "identity_error": result["identity_error"],
                    })
    print(json.dumps({"output": str(OUT), "audit_table": str(AUDIT_TABLE),
                      "markets": list(payload["markets"])}))


if __name__ == "__main__":
    main()
