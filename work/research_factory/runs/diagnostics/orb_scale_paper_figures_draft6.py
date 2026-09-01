#!/usr/bin/env python3
"""Generate the three evidence-bearing figures for the scale-invariance paper."""
from __future__ import annotations

import html
import json
import math
import statistics
from collections import defaultdict
from datetime import date
from pathlib import Path

import orb_paper_lineage_audit as lineage


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FIGURES = ROOT / "outputs/figures"
RESULTS = HERE / "orb_paper_lineage_audit_results.json"
ELIGIBILITY = HERE / "orb_eligibility_matched_window_audit.json"
OUT1 = FIGURES / "figure1_annual_gross_drag_net.svg"
OUT2 = FIGURES / "figure2_downscaling_frontier.svg"
OUT4 = FIGURES / "figure3_eligibility_decomposition.svg"

NAVY = "#17324d"
BLUE = "#2878b5"
RED = "#d44a5b"
TEAL = "#2a9d8f"
ORANGE = "#f39c34"
PURPLE = "#7b4ab5"
GRAY = "#73808c"
LIGHT = "#e6eaee"
MID = "#a7b0b8"
INK = "#17212b"


def txt(x, y, value, size=13, anchor="start", weight="normal", color=INK, rotate=None):
    transform = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{color}"{transform}>{html.escape(str(value))}</text>')


def line(x1, y1, x2, y2, color=LIGHT, width=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{width}"{extra}/>')


def path(points, color, width=2.5, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    coords = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}"{extra}/>'


def circle(x, y, color, radius=3.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{color}"/>'


def svg_start(width, height, title, subtitle=None):
    rows = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<g font-family="Inter, Arial, sans-serif">',
        txt(55, 42, title, 23, weight="bold"),
    ]
    if subtitle:
        rows.append(txt(55, 68, subtitle, 13, color="#4f5964"))
    return rows


def configure_lineage():
    lineage.END = date(2023, 12, 31)
    lineage.SOURCES = {
        root: ROOT / f"work/sierra_repair/current/{root}_sierra_volume_continuous_1m.csv.gz"
        for root in ("NQ", "ES")
    }


def annual_rows(market):
    sessions = lineage.load_sessions(market)
    rows = lineage.trades(sessions, capped=False)
    value = lineage.POINT_VALUES[market]["full"]
    by_year = defaultdict(list)
    for row in rows:
        by_year[int(row["day"][:4])].append(row)
    output = []
    for year in sorted(by_year):
        trades = by_year[year]
        gross = statistics.fmean(float(row["gross_r"]) for row in trades)
        drag = statistics.fmean(lineage.COST / (value * float(row["risk"])) for row in trades)
        output.append({"year": year, "gross": gross, "drag": drag, "net": gross - drag,
                       "count": len(trades)})
    return output


def figure1():
    width, height = 1400, 820
    rows = svg_start(width, height, "Annual gross payoff, fixed-dollar drag, and benchmark net payoff",
                     "Complete-session trade universe; fixed four-dollar round-trip component")
    panels = [("NQ", 90, 370), ("ES", 455, 735)]
    all_data = {market: annual_rows(market) for market, _, _ in panels}
    values = [row[field] for data in all_data.values() for row in data for field in ("gross", "net")]
    ymin, ymax = min(values) - .02, max(values) + .02
    for market, top, bottom in panels:
        data = all_data[market]
        left, right = 110, 1335
        years = [row["year"] for row in data]
        sx = lambda y: left + (y - years[0]) / (years[-1] - years[0]) * (right - left)
        sy = lambda v: bottom - (v - ymin) / (ymax - ymin) * (bottom - top)
        period_bands = (
            (2011, 2017.5, "2011–2017", "#f4f7f9"),
            (2017.5, 2019.5, "2018–2019", "#edf6f4"),
            (2019.5, 2021.5, "2020–2021", "#f4f7f9"),
            (2021.5, 2023, "2022–2023", "#edf6f4"),
        )
        for start, end, label, color in period_bands:
            x1, x2 = sx(start), sx(end)
            rows += [f'<rect x="{x1:.1f}" y="{top:.1f}" width="{x2-x1:.1f}" height="{bottom-top:.1f}" fill="{color}"/>',
                     txt((x1 + x2) / 2, top - 7, label, 9, "middle", color=GRAY)]
        for boundary in (2017.5, 2019.5, 2021.5):
            rows.append(line(sx(boundary), top, sx(boundary), bottom, MID, 1, "3,4"))
        rows += [txt(58, top + 15, market, 16, weight="bold"), line(left, top, left, bottom, GRAY),
                 line(left, bottom, right, bottom, GRAY)]
        for tick in (-.10, -.05, 0, .05, .10, .15):
            if ymin <= tick <= ymax:
                y = sy(tick)
                rows += [line(left, y, right, y, MID if tick == 0 else LIGHT, 1.4 if tick == 0 else 1),
                         txt(left - 12, y + 4, f"{tick:+.2f}", 11, "end")]
        for field, color, dash in (("gross", BLUE, None), ("drag", ORANGE, "5,4"), ("net", RED, None)):
            pts = [(sx(row["year"]), sy(row[field])) for row in data]
            rows.append(path(pts, color, 2.6, dash))
            rows += [circle(x, y, color, 3.2) for x, y in pts]
        for year in (2011, 2013, 2015, 2017, 2019, 2021, 2023):
            rows.append(txt(sx(year), bottom + 21, year, 10, "middle"))
        rows += [txt(25, (top + bottom) / 2, "Mean per trade (R)", 12, "middle", rotate=-90)]
    for idx, (label, color, dash) in enumerate((("Gross G", BLUE, None), ("Drag D", ORANGE, "5,4"), ("Benchmark net μ", RED, None))):
        x = 930 + idx * 125
        rows += [line(x, 58, x + 28, 58, color, 3, dash), txt(x + 35, 62, label, 11)]
    rows += ["</g>", "</svg>"]
    OUT1.write_text("\n".join(rows), encoding="utf-8")


def figure2():
    payload = json.loads(RESULTS.read_text())
    width, height = 1400, 620
    rows = svg_start(width, height, "Measured improvement rises while both period levels fall",
                     "Multiplier-only accounting frontier; realized trades and gross R outcomes are fixed")
    for pidx, market in enumerate(("NQ", "ES")):
        left = 95 + pidx * 690
        right = left + 585
        top, bottom = 105, 520
        dec = payload["markets"][market]["same_universe_decomposition"]["full"]["2022-2023"]
        g0, g1 = dec["gross_r_pre"], dec["gross_r_post"]
        d0, d1 = dec["cost_drag_r_pre"], dec["cost_drag_r_post"]
        lambdas = [10 ** (-2 + 2 * i / 200) for i in range(201)]
        series = {
            "Baseline benchmark net": [(v, g0 - d0 / v) for v in lambdas],
            "Late benchmark net": [(v, g1 - d1 / v) for v in lambdas],
            "Late − baseline": [(v, (g1 - g0) - (d1 - d0) / v) for v in lambdas],
        }
        allv = [y for values in series.values() for _, y in values]
        ymin, ymax = min(allv), max(allv)
        pad = .06 * (ymax - ymin)
        ymin, ymax = ymin - pad, ymax + pad
        sx = lambda v: left + (math.log10(v) + 2) / 2 * (right - left)
        sy = lambda v: bottom - (v - ymin) / (ymax - ymin) * (bottom - top)
        rows += [txt(left, 92, market, 16, weight="bold"), line(left, top, left, bottom, GRAY),
                 line(left, bottom, right, bottom, GRAY)]
        for frac in (0, .25, .5, .75, 1):
            tick = ymin + frac * (ymax - ymin)
            y = sy(tick)
            rows += [line(left, y, right, y, LIGHT), txt(left - 10, y + 4, f"{tick:+.2f}", 10, "end")]
        if ymin <= 0 <= ymax:
            rows.append(line(left, sy(0), right, sy(0), MID, 1.4))
        for value, label in ((.01, "0.01"), (.1, "0.1"), (1, "1")):
            x = sx(value)
            rows += [line(x, top, x, bottom, LIGHT, 1, "3,4"), txt(x, bottom + 22, label, 11, "middle")]
        colors = (("Baseline benchmark net", GRAY), ("Late benchmark net", TEAL), ("Late − baseline", PURPLE))
        for label, color in colors:
            pts = [(sx(x), sy(y)) for x, y in series[label]]
            rows.append(path(pts, color, 3))
            for anchor in (.1, 1):
                value = next(y for x, y in series[label] if abs(x - anchor) < 1e-12)
                rows += [circle(sx(anchor), sy(value), color, 4),
                         txt(sx(anchor) + (7 if anchor < 1 else -7), sy(value) - 7,
                             f"{value:+.3f}", 10, "start" if anchor < 1 else "end", color=color)]
        rows += [txt((left + right) / 2, 575, "Multiplier scale λ (log axis)", 12, "middle"),
                 txt(left - 58, (top + bottom) / 2, "Mean payoff / contrast (R)", 12, "middle", rotate=-90)]
    for idx, (label, color) in enumerate((("Baseline benchmark net", GRAY), ("Late benchmark net", TEAL), ("Late − baseline", PURPLE))):
        x = 720 + idx * 215
        rows += [line(x, 58, x + 25, 58, color, 3), txt(x + 31, 62, label, 11)]
    rows += [txt(1340, 605, "0.1 and 0.01 are accounting anchors, not execution backtests.", 10, "end", color=GRAY),
             "</g>", "</svg>"]
    OUT2.write_text("\n".join(rows), encoding="utf-8")


def ecdf(values):
    ordered = sorted(values)
    return [(value, 100 * (idx + 1) / len(ordered)) for idx, value in enumerate(ordered)]


def figure4():
    configure_lineage()
    sessions = lineage.load_sessions("NQ")
    trades = lineage.trades(sessions, capped=False)
    periods = {
        "2011–2017": [row for row in trades if 2011 <= int(row["day"][:4]) <= 2017],
        "2022–2023": [row for row in trades if 2022 <= int(row["day"][:4]) <= 2023],
    }
    session_widths = {label: [] for label in periods}
    for day, bars in sessions.items():
        label = "2011–2017" if 2011 <= day.year <= 2017 else "2022–2023" if 2022 <= day.year <= 2023 else None
        if label:
            opening = bars[:30]
            session_widths[label].append(max(float(x["h"]) for x in opening) - min(float(x["l"]) for x in opening))
    metrics = {}
    for label, values in periods.items():
        eligible = [row for row in values if 4 <= float(row["risk"]) <= 120]
        net = lambda row: float(row["gross_r"]) - 4 / (20 * float(row["risk"]))
        metrics[label] = {
            "retention": 100 * len(eligible) / len(values),
            "quality": statistics.fmean(net(row) for row in eligible),
            "candidate": sum(net(row) for row in eligible) / len(values),
            "harmonic": 1 / statistics.fmean(1 / float(row["risk"]) for row in eligible),
            "below": sum(float(row["risk"]) < 4 for row in values),
            "above": sum(float(row["risk"]) > 120 for row in values),
        }
    matched = json.loads(ELIGIBILITY.read_text())["matched"]
    width, height = 1400, 850
    rows = svg_start(width, height, "Absolute eligibility bounds change the opportunity set",
                     "Historical trade candidates and operational complete sessions use separate denominators")

    # Panel A: ECDF.
    left, right, top, bottom = 95, 760, 115, 400
    rows += [txt(55, 96, "A. Width distributions and fixed boundaries", 15, weight="bold"),
             line(left, top, left, bottom, GRAY), line(left, bottom, right, bottom, GRAY)]
    sx = lambda v: left + (math.log(max(v, 1)) - math.log(1)) / (math.log(500) - math.log(1)) * (right - left)
    sy = lambda v: bottom - v / 100 * (bottom - top)
    for tick in (0, 25, 50, 75, 100):
        rows += [line(left, sy(tick), right, sy(tick), LIGHT), txt(left - 10, sy(tick) + 4, tick, 10, "end")]
    for tick in (1, 4, 10, 30, 120, 500):
        rows.append(txt(sx(tick), bottom + 20, tick, 10, "middle"))
    for bound in (4, 120):
        rows += [line(sx(bound), top, sx(bound), bottom, RED, 1.7, "5,4"),
                 txt(sx(bound), top - 7, f"{bound} points", 10, "middle", color=RED)]
    for label, color in (("2011–2017", GRAY), ("2022–2023", TEAL)):
        rows.append(path([(sx(x), sy(y)) for x, y in ecdf(session_widths[label])], color, 2.6))
    rows += [txt(25, (top + bottom) / 2, "Cumulative share (%)", 11, "middle", rotate=-90),
             txt((left + right) / 2, 440, "Opening-range width (points, log axis)", 11, "middle"),
             txt(left, 463, "Boundary CDF locations (L−, U): 2011–2017 = 0.1%, 99.9%; 2022–2023 = 0.0%, 65.7%", 9, color=GRAY),
             line(510, 92, 535, 92, GRAY, 3), txt(542, 96, "2011–2017", 10),
             line(630, 92, 655, 92, TEAL, 3), txt(662, 96, "2022–2023", 10)]

    # Panel B: participation-quality decomposition.
    l2, r2, t2, b2 = 850, 1340, 115, 400
    rows += [txt(l2, 96, "B. Participation–quality decomposition", 15, weight="bold")]
    fields = (("retention", "Retention", "%"), ("quality", "Conditional benchmark net", "R"),
              ("candidate", "Benchmark net per candidate", "R"), ("harmonic", "Harmonic width", "points"))
    groupw = (r2 - l2) / len(fields)
    for idx, (field, label, unit) in enumerate(fields):
        center = l2 + groupw * (idx + .5)
        vals = [metrics[p][field] for p in ("2011–2017", "2022–2023")]
        raw_min, raw_max = min(vals + [0]), max(vals + [0])
        pad = max((raw_max - raw_min) * .15, .01 if unit == "R" else 2)
        vmin, vmax = raw_min - pad, raw_max + pad
        chart_top, chart_bottom = 145, 350
        syb = lambda value: chart_bottom - (value - vmin) / (vmax - vmin) * (chart_bottom - chart_top)
        zero = syb(0)
        rows += [line(center - 48, chart_top, center - 48, chart_bottom, LIGHT),
                 line(center - 48, zero, center + 48, zero, MID)]
        for off, period, color in ((-22, "2011–2017", GRAY), (22, "2022–2023", TEAL)):
            value = metrics[period][field]
            y = syb(value)
            rows += [line(center + off, zero, center + off, y, color, 3), circle(center + off, y, color, 5)]
            fmt = f"{value:.1f}" if unit in ("%", "points") else f"{value:+.3f}"
            rows.append(txt(center + off, y - 9 if value >= 0 else y + 16, fmt, 9, "middle", color=color))
        rows += [txt(center, b2 - 18, label, 9, "middle"), txt(center, b2 - 4, f"({unit})", 8, "middle", color=GRAY)]
    rows += [txt(l2, 430, "gray: 2011–2017    teal: 2022–2023; each metric uses its own labeled unit", 10, color=GRAY)]

    # Panel C: matched-window session eligibility.
    l3, r3, t3, b3 = 95, 760, 525, 785
    rows += [txt(55, 505, "C. Operational session eligibility, matched through August 26", 15, weight="bold"),
             line(l3, t3, l3, b3, GRAY), line(l3, b3, r3, b3, GRAY)]
    years = [2023, 2024, 2025, 2026]
    rates = [100 * matched[str(year)]["eligibility_rate"] for year in years]
    sx3 = lambda y: l3 + (y - 2023) / 3 * (r3 - l3)
    sy3 = lambda v: b3 - v / 100 * (b3 - t3)
    for tick in (0, 25, 50, 75, 100):
        rows += [line(l3, sy3(tick), r3, sy3(tick), LIGHT), txt(l3 - 10, sy3(tick) + 4, tick, 10, "end")]
    pts = [(sx3(y), sy3(v)) for y, v in zip(years, rates)]
    rows.append(path(pts, TEAL, 3))
    for (x, y), year, rate in zip(pts, years, rates):
        rows += [circle(x, y, TEAL, 4.5), txt(x, y - 10, f"{rate:.1f}%", 10, "middle", color=TEAL, weight="bold"),
                 txt(x, b3 + 20, year, 10, "middle")]
    rows += [txt(25, (t3 + b3) / 2, "Pass rate (%)", 11, "middle", rotate=-90),
             txt((l3 + r3) / 2, 825, "All matched-window rejections are above 120 points", 10, "middle", color=GRAY)]

    # Panel D: rejection counts.
    l4, r4, t4, b4 = 850, 1340, 525, 785
    rows += [txt(l4, 505, "D. Historical trade-candidate rejection counts", 15, weight="bold"),
             line(l4, b4, r4, b4, GRAY)]
    centers = (l4 + 140, l4 + 350)
    for center, period in zip(centers, ("2011–2017", "2022–2023")):
        below, above = metrics[period]["below"], metrics[period]["above"]
        maxv = max(metrics[p]["above"] + metrics[p]["below"] for p in metrics)
        scale = 190 / maxv
        base = b4 - 35
        for off, value, color, label in ((-24, below, BLUE, "below 4"), (24, above, RED, "above 120")):
            h = value * scale
            rows += [f'<rect x="{center+off-18:.1f}" y="{base-h:.1f}" width="36" height="{h:.1f}" fill="{color}"/>',
                     txt(center + off, base - h - 7, value, 10, "middle", color=color, weight="bold")]
        rows.append(txt(center, b4 + 18, period, 10, "middle"))
    rows += [line(1000, 815, 1025, 815, BLUE, 6), txt(1032, 819, "below 4", 10),
             line(1130, 815, 1155, 815, RED, 6), txt(1162, 819, "above 120", 10),
             "</g>", "</svg>"]
    OUT4.write_text("\n".join(rows), encoding="utf-8")


def main():
    FIGURES.mkdir(parents=True, exist_ok=True)
    configure_lineage()
    figure1()
    figure2()
    figure4()
    print(json.dumps({"figure1": str(OUT1), "figure2": str(OUT2), "figure3": str(OUT4)}))


if __name__ == "__main__":
    main()
