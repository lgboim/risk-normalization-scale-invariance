#!/usr/bin/env python3
"""Reconcile the ORB sample chain to an independent CME-equity calendar.

The calendar implementation is provided by ``pandas_market_calendars`` under
the ``CME_Equity`` name.  The audit distinguishes scheduled sessions that can
contain the full 09:30--13:59 ET research window from scheduled shortened
sessions, dates represented in the local vendor extract, exact 270-bar
sessions, and sessions that produce a headline trade.
"""

from __future__ import annotations

import csv
import gzip
import json
from collections import Counter, defaultdict
from datetime import date, datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas_market_calendars as mcal

import orb_paper_lineage_audit as lineage


HERE = Path(__file__).resolve().parent
OUT = HERE / "orb_official_calendar_reconciliation.json"
TABLE = HERE / "orb_official_calendar_reconciliation.csv"
MISSING = HERE / "orb_official_calendar_missing_dates.csv"
NY = ZoneInfo("America/New_York")
PERIODS = ("2011-2017", "2018-2019", "2020-2021", "2022-2023", "2024-2026")
AUDIT_START = date(2011, 1, 1)


def observed_days(market: str) -> dict[date, Counter[int]]:
    output: dict[date, Counter[int]] = defaultdict(Counter)
    with gzip.open(lineage.SOURCES[market], "rt", newline="") as handle:
        for raw in csv.DictReader(handle):
            dt = datetime.fromisoformat(raw["ts_event"].replace("Z", "+00:00")).astimezone(NY)
            if not AUDIT_START <= dt.date() <= lineage.END:
                continue
            minute = dt.hour * 60 + dt.minute
            if 570 <= minute < 840:
                output[dt.date()][minute] += 1
    return output


def calendar_days() -> tuple[set[date], set[date], dict[date, str]]:
    calendar = mcal.get_calendar("CME_Equity")
    schedule = calendar.schedule(AUDIT_START.isoformat(), lineage.END.isoformat())
    full: set[date] = set()
    shortened: set[date] = set()
    closes: dict[date, str] = {}
    for index, row in schedule.iterrows():
        day = index.date()
        close = row["market_close"].tz_convert(NY)
        closes[day] = close.isoformat()
        if close.time().replace(tzinfo=None) >= time(14, 0):
            full.add(day)
        else:
            shortened.add(day)
    return full, shortened, closes


def main() -> None:
    raw = {market: observed_days(market) for market in ("NQ", "ES")}
    expected_full, shortened, closes = calendar_days()
    payload = {
        "status": "independent_CME_equity_calendar_reconciliation",
        "calendar_implementation": "pandas_market_calendars:CME_Equity",
        "full_window_definition": "scheduled market close at or after 14:00 America/New_York",
        "research_window": "09:30-13:59 America/New_York",
        "markets": {},
    }
    rows: list[dict] = []
    missing_rows: list[dict] = []
    for market in ("NQ", "ES"):
        complete = lineage.load_sessions(market)
        trades = lineage.trades(complete, capped=False)
        trade_days = {date.fromisoformat(row["day"]) for row in trades}
        observed = set(raw[market])
        payload["markets"][market] = {}
        for period in PERIODS:
            expected = {day for day in expected_full if lineage.era(day) == period}
            scheduled_short = {day for day in shortened if lineage.era(day) == period}
            represented = {day for day in observed if lineage.era(day) == period}
            full = {day for day in complete if lineage.era(day) == period}
            signals = {day for day in trade_days if lineage.era(day) == period}
            missing_source = expected - represented
            partial = (expected & represented) - full
            row = {
                "market": market,
                "period": period,
                "calendar_full_window_sessions": len(expected),
                "calendar_scheduled_short_sessions": len(scheduled_short),
                "source_observed_full_window_dates": len(expected & represented),
                "calendar_sessions_absent_from_source": len(missing_source),
                "source_observed_but_not_270_bars": len(partial),
                "complete_270_bar_sessions": len(expected & full),
                "headline_signals": len(expected & signals),
                "source_coverage_rate": len(expected & represented) / len(expected) if expected else None,
                "complete_calendar_rate": len(expected & full) / len(expected) if expected else None,
            }
            payload["markets"][market][period] = row
            rows.append(row)
            for day in sorted(missing_source):
                missing_rows.append({
                    "market": market,
                    "date": day.isoformat(),
                    "period": period,
                    "classification": "scheduled_full_window_absent_from_source",
                    "scheduled_close": closes[day],
                })
            for day in sorted(partial):
                missing_rows.append({
                    "market": market,
                    "date": day.isoformat(),
                    "period": period,
                    "classification": "source_observed_incomplete_270_bar_window",
                    "scheduled_close": closes[day],
                })
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    with TABLE.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    with MISSING.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=missing_rows[0].keys())
        writer.writeheader()
        writer.writerows(missing_rows)
    print(json.dumps({"results": str(OUT), "table": str(TABLE), "exceptions": str(MISSING)}))


if __name__ == "__main__":
    main()
