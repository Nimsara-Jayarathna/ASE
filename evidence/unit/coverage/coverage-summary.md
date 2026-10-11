# ResearchTrack Unit + Mocking Coverage

| Scope | Line coverage | Branch coverage | Lines | Branches |
|---|---:|---:|---:|---:|
| All production source (filtered generated/bootstrap code) | **65.7%** | **52.3%** | 9162/13935 | 2173/4156 |
| Business logic quality-gate scope | **75.8%** | **62.7%** | 5897/7779 | 1680/2680 |

The business scope is intentionally limited to `Features` classes and the Gateway policy layer. Controllers, DTO-only contracts, EF persistence plumbing, migrations, generated/bootstrap code, and external infrastructure adapters are not used to inflate or depress the unit-test quality gate.

## Evidence

- Unit/mock tests run with `Category!=DatabaseIntegration`.
- Raw Cobertura files: `artifacts/test-results/unit/raw/`.
- Full-source HTML: `artifacts/coverage/all-source/index.html`.
- Business HTML: `artifacts/coverage/business/index.html`.
- Database integration tests remain a separate suite.
