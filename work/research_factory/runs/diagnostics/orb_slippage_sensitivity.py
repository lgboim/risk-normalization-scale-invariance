#!/usr/bin/env python3
"""Fixed adverse-tick sensitivity on the paper's exact headline trades."""
from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

import orb_paper_lineage_audit as lineage

HERE = Path(__file__).resolve().parent
OUT = HERE / "orb_slippage_sensitivity.csv"
PERIODS = ("2011-2017", "2018-2019", "2020-2021", "2022-2023")
SLIPPAGE_TICKS_PER_SIDE = (0, 1, 2, 4)
TICK_POINTS = .25


def main() -> None:
    fields = ("market", "mapping", "period", "slippage_ticks_per_side", "n",
              "gross_mean_r", "cost_drag_r", "net_mean_r", "delta_vs_2011_2017_r")
    output: list[dict[str, object]] = []
    for market in ("NQ", "ES"):
        trades = lineage.trades(lineage.load_sessions(market), capped=False)
        for contract, point_value in lineage.POINT_VALUES[market].items():
            mapping = "large_contract" if contract == "full" else "micro_scale_counterfactual"
            for ticks in SLIPPAGE_TICKS_PER_SIDE:
                total_cost_usd = lineage.COST + 2 * ticks * TICK_POINTS * point_value
                period_rows: dict[str, dict[str, float | int]] = {}
                for period in PERIODS:
                    rows = lineage.select(trades, period)
                    gross = statistics.fmean(float(row["gross_r"]) for row in rows)
                    drag = statistics.fmean(total_cost_usd / (point_value * float(row["risk"]))
                                            for row in rows)
                    period_rows[period] = {"n": len(rows), "gross": gross,
                                           "drag": drag, "net": gross - drag}
                baseline = float(period_rows["2011-2017"]["net"])
                for period in PERIODS:
                    row = period_rows[period]
                    output.append({
                        "market": market, "mapping": mapping, "period": period,
                        "slippage_ticks_per_side": ticks, "n": row["n"],
                        "gross_mean_r": row["gross"], "cost_drag_r": row["drag"],
                        "net_mean_r": row["net"],
                        "delta_vs_2011_2017_r": (None if period == "2011-2017"
                                                   else float(row["net"]) - baseline),
                    })
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    print(json.dumps({"output": str(OUT), "rows": len(output),
                      "slippage_ticks_per_side": SLIPPAGE_TICKS_PER_SIDE}))


if __name__ == "__main__":
    main()
