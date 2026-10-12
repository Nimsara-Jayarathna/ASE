# ResearchTrack SE3112 — Master Evidence Index

## Contribution index

| Contribution | Owner | Status | Primary evidence |
|---|---|:---:|---|
| Unit Testing & Mocking | Sachith | ✅ Integrated | `evidence/unit/coverage/coverage-summary.md` |
| Load & Performance Testing | Nimsara | ✅ Integrated | `evidence/load/EVIDENCE_INDEX.md` |
| Mutation Testing | Pamudi | ✅ Integrated | `evidence/mutation/reports/mutation-summary.md` |
| Code Quality & Metrics | Nimthara | ✅ Integrated | `evidence/code-quality/README.md` |

## Unit Testing & Mocking

**Source GitHub Actions artifact:** `unit-mocking-coverage-38112130327-1.zip`

| Evidence | Path |
|---|---|
| Coverage summary | `evidence/unit/coverage/coverage-summary.md` |
| Coverage metrics environment file | `evidence/unit/coverage/coverage-metrics.env` |
| Business-scope HTML report | `evidence/unit/coverage/business/index.html` |
| Business-scope Cobertura XML | `evidence/unit/coverage/business/Cobertura.xml` |
| All-source HTML report | `evidence/unit/coverage/all-source/index.html` |
| All-source Cobertura XML | `evidence/unit/coverage/all-source/Cobertura.xml` |
| Original Actions artifact | `evidence/unit/source-artifacts/unit-mocking-coverage-38112130327-1.zip` |
| Integrity manifest | `evidence/unit/MANIFEST.md` |

### Final unit coverage

| Scope | Line | Branch |
|---|---:|---:|
| All production source | **65.7%** | **52.3%** |
| Business-logic quality-gate scope | **75.8%** | **62.7%** |

## Load & Performance Testing

The performance evidence remains complete under `evidence/load/`. See `evidence/load/EVIDENCE_INDEX.md` for the seven run IDs and per-profile report paths.

## Mutation Testing

**Source GitHub Actions artifact:** `mutation-evidence-all-38123145052-1.zip`

| Evidence | Path |
|---|---|
| Final project-wide mutation summary | `evidence/mutation/reports/mutation-summary.md` |
| Per-service HTML/JSON/Markdown reports | `evidence/mutation/reports/` |
| Mutation evidence guide | `evidence/mutation/README.md` |
| Mutation evidence index | `evidence/mutation/EVIDENCE_INDEX.md` |
| Original Actions artifact | `evidence/mutation/source-artifacts/mutation-evidence-all-38123145052-1.zip` |
| Integrity manifest | `evidence/mutation/MANIFEST.md` |

### Final mutation result

| Metric | Result |
|---|---:|
| Overall weighted mutation score | **69.99%** |
| Overall regression floor | **65.00%** |
| Overall gate | **PASS** |
| Killed mutants | **1,950** |
| Survived mutants | **836** |
| Timeout / No coverage | **0 / 0** |

All seven service-level regression gates passed.

## Code Quality & Metrics

**Final original GitHub Actions artifact:** `evidence/code-quality/source-artifacts/04-final-quality-gate-pass.zip`  
**Final SonarQube analysis ID:** `a2ec6507-83b5-429d-bb4e-5c8831f70c86`  
**Final cloud gate:** **OK**, all **6 / 6** conditions passed, `ignoredConditions=false`.

| Evidence | Path |
|---|---|
| Code Quality & Metrics guide | `evidence/code-quality/README.md` |
| Detailed evidence index | `evidence/code-quality/EVIDENCE_INDEX.md` |
| Genuine final SonarQube cloud summary | `evidence/code-quality/final-run/sonarqube-summary.md` |
| Six gate condition results | `evidence/code-quality/final-run/quality-gate.json` |
| Code-quality measures | `evidence/code-quality/final-run/measures.json` |
| Cloud compute engine proof | `evidence/code-quality/final-run/ce-task.json` |
| Seven real OpenCover reports | `evidence/code-quality/final-run/coverage/` |
| Before/after original artifacts and extracted JSON | `evidence/code-quality/source-artifacts/` and `evidence/code-quality/history/` |
| Standalone, offline comparison view | `evidence/code-quality/reports/quality-evolution.html` |
| Integrity manifest | `evidence/code-quality/MANIFEST.md` |
| Offline verification | `python3 evidence/code-quality/scripts/verify-evidence.py` |

### Final static-analysis metrics

| Indicator | Verified result |
|---|---:|
| New-code coverage | **96.7%** (threshold **80%**) |
| Overall test coverage | **60.2%** |
| Overall duplicated lines | **2.4%** |
| New-code duplicated lines | **0.0%** |
| Code smells | **86** |
| Technical debt | **95 minutes** |
| Lines of code | **27,006** |
| Cyclomatic / cognitive complexity | **4,532 / 2,222** |

**Status:** All four individual contribution areas now have integrated proof in this ASE evidence repository. Do not mistake the passing *new-code* gate for 80% overall coverage or for proof of the GitHub environment variable `SONAR_ENFORCE_GATE=true`.
