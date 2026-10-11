# Unit Testing & Mocking — Final Evidence

**Owner:** Sachith  
**Assessment area:** Unit Testing & Mocking  
**Artifact source:** GitHub Actions run artifact `unit-mocking-coverage-38112130327-1.zip`

## What this evidence proves

This evidence captures the final backend unit/mock coverage result for ResearchTrack. The unit/mock suite is run with database-integration tests excluded (`Category!=DatabaseIntegration`) so the result represents fast, isolated unit/mocking verification rather than database integration coverage.

Two coverage views are retained:

| Scope | Line coverage | Branch coverage | Lines | Branches |
|---|---:|---:|---:|---:|
| All production source (filtered generated/bootstrap code) | **65.7%** | **52.3%** | 9,162 / 13,935 | 2,173 / 4,156 |
| Business-logic quality-gate scope | **75.8%** | **62.7%** | 5,897 / 7,779 | 1,680 / 2,680 |

## Why there are two scopes

The all-source result provides transparent repository-wide context. The business-quality-gate result focuses on the code where unit tests are expected to provide the most engineering value: service `Features` logic and Gateway policy logic.

Controllers, DTO-only contracts, EF persistence plumbing, migrations, generated/bootstrap code, and external infrastructure adapters are not used to inflate or depress the business gate.

## Files to open during the viva

Start with:

- `coverage/coverage-summary.md` — concise final metrics;
- `coverage/business/index.html` — primary business-logic HTML coverage report;
- `coverage/all-source/index.html` — transparent all-source coverage report;
- `coverage/business/Cobertura.xml` and `coverage/all-source/Cobertura.xml` — machine-readable evidence;
- `source-artifacts/unit-mocking-coverage-38112130327-1.zip` — unchanged original GitHub Actions artifact.

## Key business-scope examples

The report contains strong coverage in high-value services, including Auth, Gateway, Meeting, Project, Submission, Jira business logic, and selected GitHub integration/orchestration logic. Individual class-level percentages are available directly in the HTML and text summaries rather than duplicated manually here.

## Evidence provenance

The original Actions artifact is preserved unchanged. The `coverage/` directory is its extracted content. `MANIFEST.md` records SHA-256 checksums for the source ZIP and the principal summary/Cobertura files.
