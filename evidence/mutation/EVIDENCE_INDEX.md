# Mutation Testing — Evidence Index

## Final GitHub Actions run

| Item | Final evidence |
|---|---|
| Workflow | Backend Mutation Testing |
| Run | #4 |
| Branch | `main` |
| Status | **Success** |
| Duration | 1h 21m 33s |
| Artifact | `mutation-evidence-all-38123145052-1.zip` |
| Artifact size shown by Actions | 3.22 MB |
| Artifact SHA-256 | `151f61ef8a86d3161e7ef6b016f0fb554f8c38a9683bb823a6efa36eebe3308b` |
| Overall mutation score | **69.99%** |
| Overall regression floor | **65.00%** |
| Overall gate | **PASS** |
| Killed | **1,950** |
| Survived | **836** |
| Timeout | **0** |
| No coverage | **0** |

## Primary evidence paths

| Evidence | Path |
|---|---|
| Project-wide summary | `reports/mutation-summary.md` |
| AuthService reports | `reports/auth/` |
| ProjectService reports | `reports/project/` |
| SubmissionService reports | `reports/submission/` |
| GitHubService reports | `reports/github/` |
| JiraService reports | `reports/jira/` |
| Gateway reports | `reports/gateway/` |
| MeetingService reports | `reports/meeting/` |
| Original Actions artifact | `source-artifacts/mutation-evidence-all-38123145052-1.zip` |
| Integrity manifest | `MANIFEST.md` |

## Final service gates

| Service | Score | Floor | Result |
|---|---:|---:|:---:|
| AuthService | 74.34% | 70.00% | **PASS** |
| ProjectService | 77.05% | 72.00% | **PASS** |
| SubmissionService | 63.26% | 58.00% | **PASS** |
| GitHubService | 65.48% | 60.00% | **PASS** |
| JiraService | 67.89% | 62.00% | **PASS** |
| Gateway | 78.08% | 72.00% | **PASS** |
| MeetingService | 74.00% | 68.00% | **PASS** |
| **Overall** | **69.99%** | **65.00%** | **PASS** |

## Viva navigation

Open `reports/mutation-summary.md` first. If a reviewer asks for proof behind a service score, navigate into that service directory and open the corresponding HTML report. The original Actions ZIP is retained separately to prove that the extracted reports came from the successful CI run.
