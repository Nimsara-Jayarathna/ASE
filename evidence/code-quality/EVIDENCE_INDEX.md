# Code Quality & Metrics — Evidence Index

## Primary evidence

| Claim | Evidence file |
|---|---|
| Final cloud analysis, scanner, metrics, actual gate | [`final-run/sonarqube-summary.md`](final-run/sonarqube-summary.md) |
| SonarQube compute-engine success, analysis ID, branch | [`final-run/ce-task.json`](final-run/ce-task.json) |
| Actual six cloud quality-gate conditions, thresholds, and small-change setting | [`final-run/quality-gate.json`](final-run/quality-gate.json) |
| Genuine SonarQube measures (LOC, debt, complexity, smells, coverage) | [`final-run/measures.json`](final-run/measures.json) |
| Cloud analysis submission task / dashboard URL | [`final-run/report-task.txt`](final-run/report-task.txt) |
| OpenCover collector summary — 7 suites | [`final-run/coverage-collection-summary.md`](final-run/coverage-collection-summary.md) |
| Exact coverage XML paths | [`final-run/coverage-files.txt`](final-run/coverage-files.txt) |
| Genuine XML reports | [`final-run/coverage/`](final-run/coverage/) (7 files) |
| Machine-readable gate table | [`reports/quality-gate-conditions.csv`](reports/quality-gate-conditions.csv) |
| Raw historic gate/metric comparisons | [`history/`](history/) (four runs) |
| Before/after CSV | [`reports/analysis-history.csv`](reports/analysis-history.csv) |
| Standalone offline presentation | [`reports/quality-evolution.html`](reports/quality-evolution.html) |
| Source artifact provenance and SHA-256 | [`MANIFEST.md`](MANIFEST.md) |

## Original, untouched GitHub Actions artifacts

| Stage | Artifact ZIP in this repository | Cloud gate | New-code coverage |
|---|---|---|---:|
| Initial build-aware baseline | [`source-artifacts/01-pre-coverage-baseline.zip`](source-artifacts/01-pre-coverage-baseline.zip) | OK; coverage not evaluated | Not measured |
| New-code coverage requirement activated; no imported coverage | [`source-artifacts/02-missing-coverage.zip`](source-artifacts/02-missing-coverage.zip) | ERROR | 0.0% |
| Seven existing test suites imported | [`source-artifacts/03-coverage-before-targeted-tests.zip`](source-artifacts/03-coverage-before-targeted-tests.zip) | ERROR | 73.3% |
| Targeted AuthService tests + 7 suites imported | [`source-artifacts/04-final-quality-gate-pass.zip`](source-artifacts/04-final-quality-gate-pass.zip) | **OK** | **96.7%** |

**Interpretation:** Only compare coverage between analyses using the same coverage scope. Changes in overall lines of code across the pre-coverage and coverage-enabled scans are not proof of application LOC growth. Code smells remain present on the overall codebase despite the final *new-code* gate pass.

## Assessment-oriented documents

- [`docs/01-IMPLEMENTATION.md`](docs/01-IMPLEMENTATION.md) — quality tools, scope and automation architecture.
- [`docs/02-FINAL-RESULTS.md`](docs/02-FINAL-RESULTS.md) — factual metrics and progression.
- [`docs/03-CI-CD-RUNBOOK.md`](docs/03-CI-CD-RUNBOOK.md) — reproduce scanning and gate checks.
- [`docs/04-VIVA-GUIDE.md`](docs/04-VIVA-GUIDE.md) — concise demonstration and likely questions.
- [`docs/05-FINDINGS-AND-LIMITATIONS.md`](docs/05-FINDINGS-AND-LIMITATIONS.md) — open findings and evidence boundaries.
