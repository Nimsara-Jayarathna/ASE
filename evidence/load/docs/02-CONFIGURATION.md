# Performance Configuration

## Required production Environment variables

```env
K6_BASE_URL=https://api.researchtrack.blipzo.xyz
K6_PROJECT_ID=<dedicated-test-project-id>
K6_INCLUDE_INTEGRATIONS=true
K6_JIRA_PROJECT_KEY=SCRUM
K6_JIRA_ISSUE_KEY=SCRUM-179
K6_JIRA_ISSUE_ID=<real-Jira-internal-issue-id>

K6_SMOKE_P95_MS=3000
K6_LOAD_P95_MS=3000
K6_STRESS_P95_MS=3500
K6_SPIKE_P95_MS=4500
K6_WRITE_P95_MS=600
K6_LIFECYCLE_P95_MS=1500
K6_WEBHOOK_P95_MS=1000
```

`K6_ENDPOINT_P95_THRESHOLDS_JSON` is intentionally unset.

## Secrets
Keep credentials in GitHub Secrets/Environment Secrets only. The performance package must never contain real values for supervisor/student credentials, SSH private keys, the Gateway performance token, Jira client secret, cloud credentials, or signed object-store URLs.

For webhook signing, `K6_JIRA_WEBHOOK_CLIENT_SECRET` must match the secret expected by the deployed Jira webhook verifier.

## Caller-scope variables
If the parent deployment workflow evaluates a toggle before entering the reusable `production` Environment, keep that toggle as a repository-level Actions variable. Examples in this implementation include the automatic Smoke enablement and rate-limit-bypass enablement.
