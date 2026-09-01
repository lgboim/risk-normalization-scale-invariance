#!/usr/bin/env python3
"""Rebuild and hash the core artifacts for the scale-invariance manuscript."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MANUSCRIPT = ROOT / "outputs/risk_normalization_scale_invariance_manuscript_draft_7_en.md"
FIGURES = ROOT / "outputs/figures"
SERIES = ROOT / "work/sierra_repair/current"
OUT = HERE / "orb_scale_paper_replication_manifest.json"

STEPS = (
    "orb_paper_lineage_audit.py",
    "orb_six_month_phase_sensitivity.py",
    "orb_scale_paper_block_bootstrap_sensitivity.py",
    "orb_slippage_sensitivity.py",
    "orb_eligibility_matched_window_audit.py",
    "orb_scale_paper_figures_draft6.py",
    "orb_fee_scale_grid.py",
)

ARTIFACTS = (
    "orb_paper_lineage_audit_results.json",
    "orb_paper_decomposition_audit_table.csv",
    "orb_six_month_phase_sensitivity.json",
    "orb_scale_paper_block_bootstrap_sensitivity.json",
    "orb_scale_paper_block_bootstrap_sensitivity.csv",
    "orb_slippage_sensitivity.csv",
    "orb_official_calendar_reconciliation.json",
    "orb_official_calendar_reconciliation.csv",
    "orb_official_calendar_missing_dates.csv",
    "orb_eligibility_matched_window_audit.json",
    "orb_fee_scale_grid.csv",
    "orb_fee_scale_grid.svg",
    "orb_fee_scale_grid.json",
    "orb_research_chronology_audit.md",
    "orb_eligibility_provenance_audit.md",
)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> None:
    manifest_only = "--manifest-only" in sys.argv[1:]
    env = dict(os.environ)
    env.update({
        "ORB_REPAIR_RUN": "1",
        "ORB_SERIES_DIR": str(SERIES),
        "ORB_END_DATE": "2023-12-31",
    })
    env.pop("ORB_LEGACY_RUN", None)
    if not manifest_only:
        for script in STEPS:
            subprocess.run([sys.executable, str(HERE / script)], cwd=HERE, env=env, check=True)

    paths = [HERE / name for name in (*STEPS, *ARTIFACTS)]
    paths.extend([
        Path(__file__).resolve(),
        HERE / "orb_official_calendar_reconciliation.py",
        MANUSCRIPT,
        ROOT / "outputs/risk_normalization_scale_invariance_final_audit.md",
        FIGURES / "figure1_annual_gross_drag_net.svg",
        FIGURES / "figure2_downscaling_frontier.svg",
        FIGURES / "figure3_eligibility_decomposition.svg",
    ])
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing scale-paper artifacts: " + ", ".join(missing))

    manifest = {
        "status": "scale_paper_core_reproduction_passed",
        "retained_audit_inputs": {
            "official_calendar_reconciliation": (
                "Hash-verified attachment retained from the independent CME-equity "
                "calendar audit; rebuilding it additionally requires pandas_market_calendars."
            )
        },
        "canonical_source_mode": {
            "ORB_REPAIR_RUN": "1",
            "ORB_SERIES_DIR": str(SERIES.relative_to(ROOT)),
            "ORB_END_DATE": "2023-12-31",
        },
        "files": {str(path.relative_to(ROOT)): digest(path) for path in paths},
    }
    OUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"manifest": str(OUT), "files": len(paths)}, indent=2))


if __name__ == "__main__":
    main()
