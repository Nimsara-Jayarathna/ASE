# ResearchTrack Mutation Testing — Final Project-Wide Business-Logic Evidence

Generated: 2026-10-11 09:19 UTC
Regression policy: `built-in final hardened fallback`

Mutation testing is intentionally scoped to high-value validation, authorization, security, state-transition, workflow, synchronization, and orchestration logic. Controllers, DTO-only contracts, generated code, migrations, and routine persistence/transport plumbing are excluded from the mutation denominator.

## Service summary and regression gates

| Service | Weighted score | Regression floor | Gate | Killed | Survived | Timeout | No coverage |
|---|---:|---:|:---:|---:|---:|---:|---:|
| AuthService | 74.34% | 70.00% | **PASS** | 423 | 146 | 0 | 0 |
| ProjectService | 77.05% | 72.00% | **PASS** | 366 | 109 | 0 | 0 |
| SubmissionService | 63.26% | 58.00% | **PASS** | 365 | 212 | 0 | 0 |
| GitHubService | 65.48% | 60.00% | **PASS** | 313 | 165 | 0 | 0 |
| JiraService | 67.89% | 62.00% | **PASS** | 315 | 149 | 0 | 0 |
| Gateway | 78.08% | 72.00% | **PASS** | 57 | 16 | 0 | 0 |
| MeetingService | 74.00% | 68.00% | **PASS** | 111 | 39 | 0 | 0 |
| **Overall selected business logic** | **69.99%** | **65.00%** | **PASS** | **1950** | **836** | **0** | **0** |

Regression floors are deliberately below the hardened baselines. They are intended to detect meaningful test-quality regressions without requiring every equivalent or low-value mutant to be killed.

## AuthService breakdown

| Subscope | Score | Killed | Survived | Timeout | No coverage | Ignored | Compile error | Report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Password policy | 100.00% | 38 | 0 | 0 | 0 | 18 | 0 | `auth/password-policy/reports/auth-password-policy-mutation-report.md` |
| Authentication | 91.23% | 52 | 5 | 0 | 0 | 24 | 0 | `auth/authentication/reports/auth-authentication-mutation-report.md` |
| Password reset | 76.70% | 79 | 24 | 0 | 0 | 33 | 3 | `auth/password-reset/reports/auth-password-reset-mutation-report.md` |
| Registration | 65.42% | 193 | 102 | 0 | 0 | 66 | 41 | `auth/registration/reports/auth-registration-mutation-report.md` |
| User account | 75.68% | 28 | 9 | 0 | 0 | 19 | 2 | `auth/user-account/reports/auth-user-account-mutation-report.md` |
| User directory | 84.62% | 33 | 6 | 0 | 0 | 14 | 2 | `auth/user-directory/reports/auth-user-directory-mutation-report.md` |

## ProjectService breakdown

| Subscope | Score | Killed | Survived | Timeout | No coverage | Ignored | Compile error | Report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Rules | 75.00% | 147 | 49 | 0 | 0 | 56 | 17 | `project/rules/reports/project-rules-mutation-report.md` |
| Project service | 77.61% | 208 | 60 | 0 | 0 | 58 | 11 | `project/project-service/reports/project-service-mutation-report.md` |
| Supervisor dashboard | 100.00% | 11 | 0 | 0 | 0 | 12 | 8 | `project/dashboard/reports/project-dashboard-mutation-report.md` |

## SubmissionService breakdown

| Subscope | Score | Killed | Survived | Timeout | No coverage | Ignored | Compile error | Report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Rules | 77.89% | 74 | 21 | 0 | 0 | 21 | 5 | `submission/rules/reports/submission-rules-mutation-report.md` |
| Requirement service | 60.27% | 88 | 58 | 0 | 0 | 20 | 7 | `submission/requirement-service/reports/submission-requirement-service-mutation-report.md` |
| Submission service | 60.42% | 203 | 133 | 0 | 0 | 38 | 12 | `submission/submission-service/reports/research-submission-service-mutation-report.md` |

## GitHubService breakdown

| Subscope | Score | Killed | Survived | Timeout | No coverage | Ignored | Compile error | Report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Repository URL | 87.23% | 41 | 6 | 0 | 0 | 17 | 0 | `github/repository-url/reports/github-repository-url-mutation-report.md` |
| Webhook signature | 78.57% | 11 | 3 | 0 | 0 | 11 | 11 | `github/webhook-signature/reports/github-webhook-signature-mutation-report.md` |
| Access request token | 77.78% | 14 | 4 | 0 | 0 | 13 | 0 | `github/access-token/reports/github-access-token-mutation-report.md` |
| Installation state | 57.39% | 66 | 49 | 0 | 0 | 38 | 1 | `github/installation-state/reports/github-installation-state-mutation-report.md` |
| Repository link | 59.46% | 66 | 45 | 0 | 0 | 44 | 6 | `github/repository-link/reports/github-repository-link-mutation-report.md` |
| Webhook event processor | 65.88% | 112 | 58 | 0 | 0 | 39 | 34 | `github/webhook-event/reports/github-webhook-event-mutation-report.md` |
| Reconciliation | 100.00% | 3 | 0 | 0 | 0 | 11 | 0 | `github/reconciliation/reports/github-reconciliation-policy-mutation-report.md` |

## JiraService breakdown

| Subscope | Score | Killed | Survived | Timeout | No coverage | Ignored | Compile error | Report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Issue mapper | 79.22% | 61 | 16 | 0 | 0 | 20 | 15 | `jira/issue-mapper/reports/jira-issue-mapper-mutation-report.md` |
| Sync state transitions | 83.33% | 10 | 2 | 0 | 0 | 14 | 0 | `jira/sync-state/reports/jira-sync-state-mutation-report.md` |
| Issue query | 63.89% | 23 | 13 | 0 | 0 | 14 | 11 | `jira/issue-query/reports/jira-issue-query-mutation-report.md` |
| Sprint progress | 65.91% | 29 | 15 | 0 | 0 | 13 | 12 | `jira/sprint-progress/reports/jira-sprint-progress-mutation-report.md` |
| Webhook | 65.08% | 192 | 103 | 0 | 0 | 52 | 53 | `jira/webhook/reports/jira-webhook-mutation-report.md` |

## Gateway breakdown

| Subscope | Score | Killed | Survived | Timeout | No coverage | Ignored | Compile error | Report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Performance rate-limit policy | 78.33% | 47 | 13 | 0 | 0 | 101 | 10 | `gateway/performance-rate-limit/reports/gateway-performance-rate-limit-mutation-report.md` |
| Trusted proxy forwarding | 76.92% | 10 | 3 | 0 | 0 | 148 | 10 | `gateway/trusted-proxy/reports/gateway-trusted-proxy-mutation-report.md` |

## MeetingService breakdown

| Subscope | Score | Killed | Survived | Timeout | No coverage | Ignored | Compile error | Report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Meeting channel service | 71.05% | 54 | 22 | 0 | 0 | 32 | 4 | `meeting/channel-service/reports/meeting-channel-service-mutation-report.md` |
| Meeting record service | 77.03% | 57 | 17 | 0 | 0 | 31 | 2 | `meeting/record-service/reports/meeting-record-service-mutation-report.md` |

## Interpretation

- `Killed` and `Timeout` are detected mutants.
- `Survived` means selected tests still passed; remaining survivors require review, not automatic score chasing.
- `No coverage` means the selected mutation harness did not execute the mutant.
- `Ignored` and `Compile error` are reported transparently and are not counted as surviving business mutants.
- Weighted service and overall scores use actual mutant counts; percentages are never averaged across unequal subscopes.
- Per-subscope Stryker `break` thresholds are evidence-based regression floors derived from hardened baselines.
- The project-wide gate is enforced only on the complete `all` run, where every service report is regenerated in the same execution.

## Final evidence checklist

- Normal xUnit unit/mock suites pass with `Category!=DatabaseIntegration`.
- Dedicated mutation harnesses pass before Stryker starts.
- HTML, JSON and Markdown Stryker reports are retained per subscope.
- `mutation-summary.md` records weighted service and overall scores plus regression-gate status.
- The final project-wide command is `bash ./scripts/mutation-baseline.sh all`.
