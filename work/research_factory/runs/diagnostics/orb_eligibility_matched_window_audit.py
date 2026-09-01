#!/usr/bin/env python3
"""Matched-calendar audit for the NQ 4--120 point eligibility extension."""
from __future__ import annotations

import csv
import gzip
import json
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "work/databento/continuous/NQ_volume_continuous_1m.csv.gz"
OUT = HERE / "orb_eligibility_matched_window_audit.json"
NY = ZoneInfo("America/New_York")
END = date(2026, 8, 26)


def complete_widths() -> dict[date, float]:
    grouped: defaultdict[date, list[tuple[int, float, float]]] = defaultdict(list)
    with gzip.open(SOURCE, "rt", newline="") as handle:
        for row in csv.DictReader(handle):
            timestamp = datetime.fromisoformat(row["ts_event"].replace("Z", "+00:00")).astimezone(NY)
            if not date(2023, 1, 1) <= timestamp.date() <= END:
                continue
            minute = timestamp.hour * 60 + timestamp.minute
            if 570 <= minute < 840:
                grouped[timestamp.date()].append((minute, float(row["high"]), float(row["low"])))

    widths = {}
    for day, rows in grouped.items():
        clocks = Counter(minute for minute, _, _ in rows)
        if len(clocks) != 270 or any(clocks.get(minute) != 1 for minute in range(570, 840)):
            continue
        opening = [(high, low) for minute, high, low in rows if minute < 600]
        widths[day] = max(high for high, _ in opening) - min(low for _, low in opening)
    return widths


def summarize(values: list[float]) -> dict[str, float | int]:
    passed = sum(4.0 <= width <= 120.0 for width in values)
    return {
        "complete_sessions": len(values),
        "eligible_sessions": passed,
        "eligibility_rate": passed / len(values),
        "below_lower_bound": sum(width < 4.0 for width in values),
        "above_upper_bound": sum(width > 120.0 for width in values),
    }


def main() -> None:
    widths = complete_widths()
    annual = {}
    matched = {}
    for year in range(2023, 2027):
        annual[str(year)] = summarize([width for day, width in widths.items() if day.year == year])
        matched[str(year)] = summarize([
            width for day, width in widths.items()
            if day.year == year and (day.month, day.day) <= (8, 26)
        ])
    payload = {
        "status": "posthoc_calendar_window_sensitivity",
        "source": str(SOURCE),
        "rule": "4 <= opening_range_width_points <= 120",
        "complete_session_rule": "exactly one bar for every minute from 09:30 through 13:59 America/New_York",
        "matched_window": "January 1 through August 26 of each year",
        "annual": annual,
        "matched": matched,
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
