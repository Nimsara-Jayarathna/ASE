# ResearchTrack SE3112 — Master Evidence Index

## Contribution index

| Contribution | Owner | Status | Primary evidence |
|---|---|:---:|---|
| Unit Testing & Mocking | Sachith | ✅ Integrated | `evidence/unit/coverage/coverage-summary.md` |
| Load & Performance Testing | Nimsara | ✅ Integrated | `evidence/load/EVIDENCE_INDEX.md` |
| Mutation Testing | Pamudi | ⏳ Pending artifact integration | `evidence/mutation/README.md` |
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

## Pending evidence

Mutation evidence will be integrated under `evidence/mutation/` when the final GitHub Actions artifact is supplied. Code-quality evidence will follow the same structure under `evidence/code-quality/` after Nimthara's final run.
