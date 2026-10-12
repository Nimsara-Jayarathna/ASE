# Authentic SonarQube Analysis History

| Stage | Analysis ID | Cloud gate | New-code coverage | Code smells | Debt |
|---|---|:---:|---:|---:|---:|
| 01-pre-coverage-baseline | `117303d4-4803-402e-95cc-a9c75a0390a5` | **OK** | Not measured | 85 | 105 min |
| 02-missing-coverage | `ae49e808-6b21-4b84-847d-00bac82b336d` | **ERROR** | Not measured | 83 | 95 min |
| 03-coverage-before-targeted-tests | `b26378dd-ba0c-4b63-8afb-1a31cc617716` | **ERROR** | 73.3% | 86 | 95 min |
| 04-final-quality-gate-pass | `a2ec6507-83b5-429d-bb4e-5c8831f70c86` | **OK** | 96.7% | 86 | 95 min |

Data derived from the original, unchanged SonarQube API JSON artifacts in `../source-artifacts/`; each stage’s raw JSON is also extracted under `../history/`. Earlier missing coverage is **not** identical to 0% measured source coverage.
