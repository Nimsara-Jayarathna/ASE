# ResearchTrack SE3112 — Testing Pipeline Evidence

This repository is the consolidated evidence package for the **SE3112 Advanced Software Engineering — Microservice Testing Pipeline** assessment for ResearchTrack.

The evidence is organized by the four individual testing contributions so that each member's proof can be reviewed independently while still forming one assessment-level testing story.

## Evidence structure

```text
.
├── README.md
├── EVIDENCE_INDEX.md
├── SE3112_ResearchTrack_Testing_Team_Plan.md
├── docs/
│   └── EVIDENCE-STRUCTURE.md
└── evidence/
    ├── unit/             # Sachith — Unit Testing & Mocking
    ├── load/             # Nimsara — Load & Performance Testing
    ├── mutation/         # Pamudi — Mutation Testing
    └── code-quality/     # Nimthara — Code Quality & Metrics (final gate pass + artifacts)
```

## Current status

| Contribution | Owner | Evidence state |
|---|---|---|
| Unit Testing & Mocking | Sachith | **Integrated** — final coverage artifact and reports included |
| Load & Performance Testing | Nimsara | **Integrated** — seven final k6 evidence runs retained |
| Mutation Testing | Pamudi | **Integrated** — successful final project-wide Stryker artifact and reports included |
| Code Quality & Metrics | Nimthara | **Integrated** — completed SonarQube Cloud Quality Gate with verified OpenCover evidence |

## Unit Testing & Mocking — current final evidence

The supplied GitHub Actions artifact `unit-mocking-coverage-38112130327-1.zip` has been preserved unchanged under `evidence/unit/source-artifacts/` and extracted into `evidence/unit/coverage/` for direct review.

| Scope | Line coverage | Branch coverage | Covered lines | Covered branches |
|---|---:|---:|---:|---:|
| All production source (filtered generated/bootstrap code) | **65.7%** | **52.3%** | 9,162 / 13,935 | 2,173 / 4,156 |
| Business-logic quality-gate scope | **75.8%** | **62.7%** | 5,897 / 7,779 | 1,680 / 2,680 |

The business scope is intentionally focused on service `Features` logic and the Gateway policy layer. Controllers, DTO-only contracts, EF persistence plumbing, migrations, generated/bootstrap code, and external infrastructure adapters are not used to artificially raise or lower the business-quality gate.

Open `evidence/unit/README.md` for the unit/mocking evidence guide and `evidence/unit/coverage/business/index.html` for the primary human-readable coverage report.

## Load & Performance Testing

The existing final k6 package has been retained and moved under `evidence/load/` without changing its evidence content. It includes Smoke, Load, Stress, Spike, Write, Lifecycle, and Webhook runs together with their original GitHub artifact ZIPs.

Open `evidence/load/README.md` for the full performance-testing evidence package.

## Mutation Testing

The final successful GitHub Actions mutation artifact is integrated under `evidence/mutation/`. The complete `all` run achieved a **69.99%** weighted mutation score and passed every service regression floor plus the **65.00% overall gate**.

Open `evidence/mutation/README.md` for the evidence guide and `evidence/mutation/reports/mutation-summary.md` for the final project-wide summary.

## Code Quality & Metrics

Nimthara's final SonarQube Cloud evidence is fully integrated. The verified **Quality Gate is OK** (all six conditions), with **96.7% new-code coverage** against the 80% threshold, **60.2% overall coverage**, and **seven** authentic OpenCover reports from existing .NET unit-test suites. The build-aware SonarScanner 11.3.0 scanned eight production projects. All original downloaded artifacts (including the earlier failed coverage runs) are preserved byte-for-byte.

Open `evidence/code-quality/README.md` for the complete evidence guide, `evidence/code-quality/reports/quality-evolution.html` for an offline summary, and `evidence/code-quality/final-run/quality-gate.json` for the authoritative six-condition gate decision. **`SONAR_ENFORCE_GATE` still needs operational confirmation** in the GitHub environment if strict future failure enforcement is required.

## Evidence handling rule

Original GitHub Actions artifact ZIPs are kept unchanged under each contribution's `source-artifacts/` directory. Extracted, human-readable evidence is stored beside them. This preserves provenance while keeping the submission easy to inspect during the viva.
