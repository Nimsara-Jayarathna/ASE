# 01 — Implementation: Automated Static Analysis & Quality Metrics

## Objective and ownership

Nimthara's SE3112 contribution implements **automated Static Code Analysis and quality checks, demonstrating quality indicators/metrics** for the ResearchTrack `.NET 10` backend. The implementation lives in the separate `researchtrack-backend` GitHub repository; this ASE repository preserves its **final authentic run artifacts** rather than duplicating application source code.

## Static checks: fast native workflow

| Stage | Actual implementation | Outcome/evidence |
|---|---|---|
| Formatting | CSharpier 1.3.0 with pinned tool manifest and production-source `.editorconfig` | `bash ./scripts/code-quality.sh check ci` rejects formatting violations |
| Roslyn style | Selected IDE0005 / IDE0065 via `dotnet format style`, with migrations/generated source excluded | Unused imports and import placement are checked without rewriting EF migrations |
| Compilation | Eight production `.csproj` builds under Release/.NET 10 | Compilation errors fail the code-quality pipeline |
| Analyzer report | Opt-in Roslyn analyzers / SARIF | Additional indicators for manual review, without treating all inherited code smells as errors |

The code-quality workflow is `.github/workflows/backend-code-quality.yml` in `researchtrack-backend`. It is separate from the other students' Unit/Mocking, Mutation and Load workflows.

## SonarQube Cloud workflow

The backend workflow `.github/workflows/backend-sonarqube.yml` runs on `main` and can be dispatched manually. It uses the GitHub `production` environment for `SONAR_TOKEN` and the SonarQube organization/project settings, and pins **SonarScanner for .NET 11.3.0**.

```text
GitHub Actions: main / workflow_dispatch
              |
              v
         SonarScanner begin
              |
              v
         8 production project builds (.NET 10 Release)
              |
              v
         7 existing unit-test suites (Category!=DatabaseIntegration)
              |
              v
         Coverlet collector -> 7 OpenCover XML reports
              |
              v
         SonarScanner end -> Cloud compute engine
              |
              v
         Metrics + Quality Gate API reporting
              |
              v
         backend-sonarqube-analysis artifact
```

**Projects built:** BuildingBlocks.Api, Gateway, AuthService, GitHubService, JiraService, MeetingService, ProjectService, SubmissionService.

**Test suites collected:** AuthService.Tests, Gateway.Tests, GitHubService.Tests, JiraService.Tests, MeetingService.Tests, ProjectService.Tests, SubmissionService.Tests. These are seven existing group suites, executed without editing their original testing workflows.

The scanner imports the coverage through `sonar.cs.opencover.reportsPaths` and records the actual cloud response in `ce-task.json`, `quality-gate.json` and `measures.json`. A missing test result/collector XML fails collection rather than being silently reported as real 0% measured coverage.

## Quality gate semantics

SonarQube evaluates **new-code** ratings, coverage, duplication and hotspot review in the configured new-code period (the final JSON shows a 30-day period). **80% is the new-code coverage threshold, not a project-wide 80% threshold.** Overall coverage is **60.2%**.

The scanner script supports `SONAR_ENFORCE_GATE=true`, which makes a failing gate block a scanner job. The final source artifact proves the cloud gate **passed** but does not prove that environment variable is currently set to true; confirm this in GitHub settings as a final operational check.

## Why this is genuine analysis evidence

The final artifact contains SonarQube's **completed** compute-engine task with analysis ID and `SUCCESS`, measured statistics returned by the Cloud API, six condition results, and seven real OpenCover XML files. No figures are generated from assumptions. The original downloadable Actions ZIP is preserved byte-for-byte.
