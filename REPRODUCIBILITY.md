# Reproducibility guide

## Scope

This repository supports two levels of reproducibility:

1. **Public verification** checks the manuscript, derived audit outputs, figures, scripts, provenance records, and hashes without access to licensed market data.
2. **Full numerical reproduction** rebuilds the trade-level results and figures from independently licensed canonical Sierra Chart source files.

The package does not redistribute Sierra Chart or Databento data. Users are responsible for obtaining and using those sources under their own licences.

## Tested environment

The version 1.0 public package was checked with Python 3.14.6. The scripts use standard-library features available in Python 3.11 or later. The numerical dependencies used by the retained analyses are recorded in `requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Public verification without market data

Check Python syntax:

```bash
python -m compileall -q work/research_factory/runs/diagnostics
```

Check that the core retained files are present and generate a local hash manifest:

```bash
python work/research_factory/runs/diagnostics/reproduce_orb_scale_paper_package.py --manifest-only
```

The immutable version 1.0 inventory and SHA-256 values are stored in `scale_invariance_public_replication_manifest.json` and in the Zenodo record at https://doi.org/10.5281/zenodo.22230814.

## Licensed inputs for a full rebuild

Place the canonical one-minute continuous files at:

```text
work/sierra_repair/current/NQ_sierra_volume_continuous_1m.csv.gz
work/sierra_repair/current/ES_sierra_volume_continuous_1m.csv.gz
```

Expected SHA-256 values are recorded in:

```text
work/research_factory/runs/diagnostics/orb_sierra_rebuild_manifest_public.json
```

The expected schema includes UTC event timestamps and OHLC fields. The analysis converts timestamps to `America/New_York` and retains complete 09:30–13:59 windows containing exactly one record for each of 270 minutes. The repair protocol and coverage reconciliation are documented alongside the scripts.

## Full rebuild

From the repository root, run:

```bash
python work/research_factory/runs/diagnostics/reproduce_orb_scale_paper_package.py
```

The runner executes the lineage audit, dependence sensitivities, execution sensitivity, matched-window eligibility audit, figure generation, and fee-scale grid. It then writes a local manifest of the rebuilt artifacts.

The independent exchange-calendar script is retained for auditability but is not rerun by the main runner. Rebuilding that attachment requires `pandas-market-calendars`, which is included in `requirements.txt`.

## Expected limitations

The raw contract-file inventory was unavailable when version 1.0 was assembled. Exact within-file duplicate minute timestamps in the licensed raw contract files were not counted. No duplicate count is inferred from the continuous-source artifacts.

The eight-tick execution adjustment is a deliberately adverse sensitivity, not a calibrated slippage model. The moving-block calculation is a post-hoc dependence sensitivity and is not used as evidence of a structural break. These scope distinctions are stated in the manuscript and retained audit outputs.

## Reporting a reproduction problem

Open a reproduction issue using the repository template. Include the operating system, Python version, exact command, traceback, and hashes of any public inputs. Do not attach or paste licensed market data, private vendor URLs, access tokens, or credentials.
