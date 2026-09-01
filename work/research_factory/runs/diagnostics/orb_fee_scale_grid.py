#!/usr/bin/env python3
"""Render the analytical fixed-fee-by-multiplier grid for the scale paper."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "orb_paper_lineage_audit_results.json"
OUT_CSV = HERE / "orb_fee_scale_grid.csv"
OUT_JSON = HERE / "orb_fee_scale_grid.json"
OUT_SVG = HERE / "orb_fee_scale_grid.svg"

FEES = (0.04, 0.10, 0.40, 1.00, 2.00, 4.00, 8.00)
LAMBDAS = (0.01, 0.025, 0.05, 0.10, 0.25, 0.50, 1.00)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> None:
    payload = json.loads(INPUT.read_text())
    rows = []
    coefficients = {}
    for market in ("NQ", "ES"):
        full = payload["markets"][market]["same_universe_decomposition"]["full"]["2022-2023"]
        coefficient = full["friction_r"] / 4.0
        coefficients[market] = coefficient
        for fee in FEES:
            for lam in LAMBDAS:
                rows.append({
                    "market": market,
                    "fixed_fee_usd": fee,
                    "multiplier_scale_lambda": lam,
                    "effective_fixed_fee_usd": fee / lam,
                    "fixed_friction_contribution_r": coefficient * fee / lam,
                    "equivariance_fee_usd_from_four_dollar_anchor": 4.0 * lam,
                })

    with OUT_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    width, height = 1440, 760
    margin_left, margin_top = 115, 145
    cell_w, cell_h = 78, 58
    panel_gap = 105
    panel_w = len(LAMBDAS) * cell_w
    maximum = max(row["fixed_friction_contribution_r"] for row in rows)
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<g font-family="Inter, Arial, sans-serif" fill="#17212b">',
        '<text x="55" y="45" font-size="24" font-weight="700">Analytical fixed-fee-by-multiplier sensitivity</text>',
        '<text x="55" y="72" font-size="13" fill="#4f5964">Cells report J(K′, λ) in R; identical effective fee K′/λ gives identical values within a market.</text>',
    ]
    for panel, market in enumerate(("NQ", "ES")):
        x0 = margin_left + panel * (panel_w + panel_gap)
        svg.append(f'<text x="{x0}" y="112" font-size="18" font-weight="700">{market}</text>')
        for col, lam in enumerate(LAMBDAS):
            x = x0 + col * cell_w
            svg.append(f'<text x="{x + cell_w/2}" y="135" font-size="10" text-anchor="middle">λ={lam:g}</text>')
        market_rows = [row for row in rows if row["market"] == market]
        for row_idx, fee in enumerate(FEES):
            y = margin_top + row_idx * cell_h
            svg.append(f'<text x="{x0 - 12}" y="{y + 35}" font-size="11" text-anchor="end">K′=${fee:g}</text>')
            for col, lam in enumerate(LAMBDAS):
                value = next(row["fixed_friction_contribution_r"] for row in market_rows
                             if row["fixed_fee_usd"] == fee and row["multiplier_scale_lambda"] == lam)
                intensity = min(1.0, value / maximum)
                red = round(245 - 120 * intensity)
                green = round(249 - 150 * intensity)
                blue = round(252 - 80 * intensity)
                x = x0 + col * cell_w
                svg.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="rgb({red},{green},{blue})" stroke="#ffffff"/>')
                color = "#ffffff" if intensity > 0.55 else "#17212b"
                svg.append(f'<text x="{x + cell_w/2}" y="{y + 34}" font-size="10" text-anchor="middle" fill="{color}">{value:.4f}</text>')
        svg.append(f'<text x="{x0 + panel_w/2}" y="{margin_top + len(FEES)*cell_h + 38}" font-size="12" text-anchor="middle">Multiplier scale</text>')
    svg.extend([
        '<text x="55" y="715" font-size="11" fill="#4f5964">The grid is analytical: no price path, fill, or outcome category is rerun.</text>',
        '</g>',
        '</svg>',
    ])
    OUT_SVG.write_text("\n".join(svg))

    manifest = {
        "status": "analytical_grid",
        "formula": "J(K_prime, lambda) = (K_prime/lambda) * J(4,1)/4",
        "input": str(INPUT.name),
        "input_sha256": digest(INPUT),
        "fees_usd": FEES,
        "multiplier_scales": LAMBDAS,
        "market_coefficients_r_per_effective_dollar": coefficients,
        "outputs": {
            OUT_CSV.name: digest(OUT_CSV),
            OUT_SVG.name: digest(OUT_SVG),
        },
    }
    OUT_JSON.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
