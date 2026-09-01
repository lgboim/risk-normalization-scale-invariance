# Contributing

Corrections that improve reproducibility, documentation, portability, or the accuracy of the public record are welcome.

## Before opening an issue

- Read `README.md`, `REPRODUCIBILITY.md`, and `LICENSE-SCOPE.md`.
- Check existing issues for the same question.
- Confirm that your command is being run from the repository root in an isolated Python environment.
- Do not upload licensed Sierra Chart or Databento data, credentials, vendor downloads, or other third-party material.

## Good issue reports

A useful report includes:

- the affected file and, where possible, line number;
- the expected and observed behavior;
- the exact command used;
- operating system and Python version;
- a minimal traceback or validation output;
- hashes for public inputs when a hash mismatch is involved.

## Pull requests

Keep changes narrowly scoped. Explain whether the change affects code, derived outputs, prose, metadata, or licensing. Run the repository quality workflow locally where practical:

```bash
python -m compileall -q work/research_factory/runs/diagnostics
python -m json.tool codemeta.json >/dev/null
python -m json.tool scale_invariance_public_replication_manifest.json >/dev/null
```

If a change alters a derived artifact, state which inputs and scripts produced it. Do not silently replace immutable Zenodo version 1.0 artifacts. Corrections should be documented in `CHANGELOG.md` and released as a new version when substantive.

## Research and citation scope

Issues and pull requests should distinguish among exact accounting identities, empirical estimates, post-hoc sensitivities, and claims about actual execution. New empirical claims require a stated estimand, data provenance, denominator, and reproducible derivation.

By contributing, you agree that original code contributions are licensed under MIT and original documentation or derived-data contributions are licensed under CC BY 4.0, consistent with `LICENSE-SCOPE.md`.
