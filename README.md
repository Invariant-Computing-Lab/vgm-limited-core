# vgm-limited-core

CP03R1 source and reproducibility package. Portfolio codes: N005.

## What is included
Preserved VGM core only; the file explicitly omits full driver routines. Import/exit success cannot count as a full benchmark replay.

## Run the checks
Install the dependencies specified by the upstream requirements/environment files. This package includes exact original source where stated; use Python 3.11 or later.

```sh
python run_checks.py
```

The wrapper copies the source into a temporary directory, records stdout/stderr and returns nonzero when a declared check fails. Its output is `checks/RESULT.json`. It never submits a paper, contacts a publication service or pushes a repository. Review `RELEASE_SPEC.json` for the test scope.

Direct commands, from `.`:
```sh
python vgm_invariant_geometry_benchmark_v2.py
```

## Version and provenance
Recovered from the fixed source archives listed in the private delivery registry. Existing data and experiment tables remain historical unless a dated rerun says otherwise. `UPSTREAM_README.md`, when present, is the preserved source documentation and can contain old completion statements. Current status is only in `RELEASE_SPEC.json` and `checks/RESULT.json`.

## Limitations
Software tests are not independent biological, clinical, physical or mathematical validation. Review the original study's failed and untested claims before citing results. Missing components are not fabricated. This version is not automatically the latest code from other concurrent workstreams.

## Publication and licensing
This is a private staging package. Existing licence files retain their original meaning; no new blanket licence or third-party redistribution permission is granted. A human maintainer must approve authorship, rights, secrets and target-account settings before public upload.
## Verified packaging revision — 2026-10-20

Source omits full driver; import/zero exit would not count as a meaningful runtime check.

Runtime state: `PASS`. Rights and release approval are separate. See `RELEASE_VERIFICATION.json`. No paper or conference submission is included as a new software result.

## Runtime revision — 2026-10-21

Original limited core plus exact recovered CP04 finite-scope study passed. Full historical v2 driver still missing; not a full v2 replay.

Evidence: `RELEASE_VERIFICATION.json`. Rights and hosted/server/Windows checks are separate.

The recovered original `cp04/run_scope_study.py` supplies meaningful finite-scope checks, not the absent historical v2 driver. Use `python run_checks.py` for both declared commands.
