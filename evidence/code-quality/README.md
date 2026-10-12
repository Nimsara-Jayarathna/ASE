# Code Quality & Metrics — Final Verified Evidence

**Owner:** Nimthara  
**Assessment:** SE3112 — Advanced Software Engineering / Microservice Testing Pipeline  
**System:** ResearchTrack backend (.NET 10, eight production projects)  
**Evidence date:** 12 October 2026  
**Status:** **Integrated — SonarQube Cloud analysis successful; quality gate OK (6/6 conditions).**

## Start here

| Open | Why |
|---|---|
| [`final-run/sonarqube-summary.md`](final-run/sonarqube-summary.md) | Original run-generated summary with cloud analysis ID, measures and six conditions |
| [`docs/02-FINAL-RESULTS.md`](docs/02-FINAL-RESULTS.md) | Human-readable final results, thresholds and honest before/after table |
| [`reports/quality-evolution.html`](reports/quality-evolution.html) | Self-contained, offline graphical evidence page for presentation |
| [`EVIDENCE_INDEX.md`](EVIDENCE_INDEX.md) | Direct file-by-file evidence map |
| [`MANIFEST.md`](MANIFEST.md) | SHA-256 checksums and provenance for the original GitHub artifacts |

## Final confirmed result

| Measurement | Verified value |
|---|---:|
| Cloud compute engine | **SUCCESS** |
| SonarQube Quality Gate | **OK** |
| Conditions passing | **6 / 6** |
| New-code coverage | **96.7%** (required ≥ 80%) |
| Overall source coverage | **60.2%** |
| Coverage reports | **7 OpenCover XML files** |
| Duplicated lines | **2.4%** overall; **0.0%** new code |
| Lines of code | **27,006** |
| Cyclomatic complexity | **4,532** |
| Cognitive complexity | **2,222** |
| Code smells | **86** |
| Technical debt | **95 minutes** |

**Cloud analysis:** `a2ec6507-83b5-429d-bb4e-5c8831f70c86`  
**GitHub commit reported by the final run:** `797b60e` on `main` (from the supplied GitHub Actions log; the ZIP itself verifies analysis ID and branch, not GitHub run URL).  
**SonarQube dashboard:** https://sonarcloud.io/dashboard?id=Nimsara-Jayarathna_researchtrack-backend&branch=main

## How this was implemented

- `.github/workflows/backend-code-quality.yml` performs production CSharpier 1.3.0 checks, Roslyn unused-import style validation and eight Release builds on the backend repository.
- `.github/workflows/backend-sonarqube.yml` runs SonarScanner for .NET 11.3.0, compiles eight production projects, and executes seven existing xUnit suites with `coverlet.collector` to produce OpenCover XML for ingestion.
- The scanner publishes the completed cloud analysis and a GitHub Actions artifact called `backend-sonarqube-analysis`. The full **unaltered downloaded artifact** is stored at `source-artifacts/04-final-quality-gate-pass.zip`, and all its contents are extracted under `final-run/`.
- Security/reliability/maintainability ratings, new-code coverage, duplication and hotspot review are evaluated by SonarQube's cloud quality gate. The final `quality-gate.json` records **`ignoredConditions: false`**.

The SonarQube workflow's green job and the SonarQube cloud gate are distinct: a workflow can report success with a failed cloud gate if `SONAR_ENFORCE_GATE` is not enabled. **The final cloud gate was independently verified as `OK`; whether the GitHub environment enforces future failures must still be verified in Settings.**

## Historical analysis evidence

Four **unaltered original** analysis ZIPs preserve the sequence: initial scan, missing coverage, 73.3% new-code coverage, and the final 96.7% pass. Their raw JSON/summary files are extracted under `history/`; see [`reports/analysis-history.csv`](reports/analysis-history.csv) and [`docs/02-FINAL-RESULTS.md`](docs/02-FINAL-RESULTS.md). The final 7 OpenCover XML reports remain under `final-run/coverage/`.

**Evidence boundaries:** The artifact proves automated backend code-quality analysis and its genuine metrics. It does not prove frontend quality analysis, global 80% coverage, elimination of all historical code smells, or that a future failed gate is already configured to block CI. The individual unit/mocking, load and mutation evidence is separately preserved in their original folders.
