# ResearchTrack — SonarQube Cloud genuine analysis evidence

Project key: `Nimsara-Jayarathna_researchtrack-backend`  
Analysis ID: `a2ec6507-83b5-429d-bb4e-5c8831f70c86`  
Compute engine: `SUCCESS`  
Quality gate: **OK**  
Scanner: SonarScanner for .NET 11.3.0, eight production project builds.

| Indicator | Measured value |
|---|---:|
| Lines of code | 27006 |
| Cyclomatic complexity | 4532 |
| Cognitive complexity | 2222 |
| Duplicated lines (%) | 2.4 |
| Code smells | 86 |
| Technical debt (minutes) | 95 |
| Overall test coverage (%) | 60.2 |
| Coverage on new code (%) | 96.66666666666667 |

Quality-gate enforcement is controlled by the GitHub Actions variable `SONAR_ENFORCE_GATE`.
This evidence is from the finished cloud analysis, not locally estimated metrics.
Raw JSON files: `ce-task.json`, `quality-gate.json`, `measures.json`.
Coverage reports produced: **7** (existing unit-test suites).
See `coverage-collection-summary.md` and `coverage/` for OpenCover evidence.

### Quality gate conditions (actual analysis)

| Condition | Status | Actual | Threshold |
|---|---|---:|---:|
| new_reliability_rating | OK | 1 | 1 |
| new_security_rating | OK | 1 | 1 |
| new_maintainability_rating | OK | 1 | 1 |
| new_coverage | OK | 96.7 | 80 |
| new_duplicated_lines_density | OK | 0.0 | 3 |
| new_security_hotspots_reviewed | OK | 100.0 | 100 |

Small-change conditions ignored: `false`
