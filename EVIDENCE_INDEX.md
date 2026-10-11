# ResearchTrack SE3112 — Master Evidence Index

## Contribution index

| Contribution | Owner | Status | Primary evidence |
|---|---|:---:|---|
| Unit Testing & Mocking | Sachith | ✅ Integrated | `evidence/unit/coverage/coverage-summary.md` |
| Load & Performance Testing | Nimsara | ✅ Integrated | `evidence/load/EVIDENCE_INDEX.md` |
| Mutation Testing | Pamudi | ✅ Integrated | `evidence/mutation/reports/mutation-summary.md` |
| Code Quality & Metrics | Nimthara | ⏳ Pending implementation/evidence | `evidence/code-quality/README.md` |

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

## Pending evidence

Only Code Quality & Metrics remains pending. Its final evidence will be integrated under `evidence/code-quality/` after Nimthara's implementation and final run.
