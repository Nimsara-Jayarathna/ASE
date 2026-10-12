# Code Quality Evidence — Integrity Manifest

Original GitHub Actions artifact ZIPs were copied **byte-for-byte** from the uploaded files. Derived documents and offline HTML summaries do not replace raw evidence. The final `.zip` and all seven OpenCover reports are listed below.

## Original source artifact ZIPs

| Path relative to `evidence/code-quality/` | Bytes | SHA-256 |
|---|---:|---|
| `source-artifacts/01-pre-coverage-baseline.zip` | 2,175 | `6036cf223e51f49ca954967b107ec2e49ab7f45fa693de448963c0177bc63cd2` |
| `source-artifacts/02-missing-coverage.zip` | 2,233 | `e3bae6df9b0cc848e2b95abb372c6fe8a27072273f0ebf497253c99ec11df17d` |
| `source-artifacts/03-coverage-before-targeted-tests.zip` | 534,477 | `833b1e965b4dc1e7cb94abfb512e35877ed938f0c5ba587fd0cfe500f2d5ed12` |
| `source-artifacts/04-final-quality-gate-pass.zip` | 534,445 | `f35b014ff0353edd8de59d8b0455f37169c5fbca625fd68d77e14eb70462b6fd` |

## Final run — OpenCover XML reports

| Path relative to `evidence/code-quality/` | Bytes | SHA-256 |
|---|---:|---|
| `final-run/coverage/ResearchTrack.AuthService.Tests/c4391454-24e0-4571-b2cf-be02fbef7dfc/coverage.opencover.xml` | 842,534 | `45a005ccc0a4b24927db0b97cbc34f2fb09dc1fc9dda1e0fe5cdbdd209682e41` |
| `final-run/coverage/ResearchTrack.Gateway.Tests/e8960977-05e0-4182-9d43-ded7cd433009/coverage.opencover.xml` | 209,567 | `18214bb6b77319d0c6909a1461ecd6f34845f95d38d19644dc6d5047a390b849` |
| `final-run/coverage/ResearchTrack.GitHubService.Tests/d226584b-594e-4cac-87ed-7541f56dd1bb/coverage.opencover.xml` | 3,139,692 | `a431d244a7284bb6e13004cc1b45c55509c15369f7889e72b509862f7b2eb16e` |
| `final-run/coverage/ResearchTrack.JiraService.Tests/25bc6f1d-459c-470e-843e-c96fe198ba23/coverage.opencover.xml` | 1,311,214 | `460072fd9d5c508612c300f9726c41721c977871f9958a5d5cb85beeb21cf533` |
| `final-run/coverage/ResearchTrack.MeetingService.Tests/e878c331-a3af-4ca0-8406-757b76f75a51/coverage.opencover.xml` | 551,406 | `1a38d03cd8c3d118639bdc6110bf438aae1a8b738912607380586254e9e9483c` |
| `final-run/coverage/ResearchTrack.ProjectService.Tests/0e920fb6-4cde-4cab-961d-a0f38b9d5091/coverage.opencover.xml` | 682,412 | `c4aa15dd2695d9d2e7d3613012dcc5d97c0454fc074e9f83fa651b014328c842` |
| `final-run/coverage/ResearchTrack.SubmissionService.Tests/b05d9ffc-8a2b-4580-b0be-8dc76c7e1aa2/coverage.opencover.xml` | 1,022,634 | `969f09e8f4e42c074bbab013b3e8f649378e0583c1bb34e0afc8af20ba71f215` |

## Final analysis identity

- Cloud project: `Nimsara-Jayarathna_researchtrack-backend`
- Analysis ID: `a2ec6507-83b5-429d-bb4e-5c8831f70c86`
- Compute engine: `SUCCESS`
- Quality gate: `OK`
- Six conditions: `OK`
- `ignoredConditions`: `false`

Run `python3 evidence/code-quality/scripts/verify-evidence.py` from the ASE repository root to check the SHA-256 values and inspect the original archived JSON/coverage files.
