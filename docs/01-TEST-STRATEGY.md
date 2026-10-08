# Test Strategy

## Objective
Validate ResearchTrack latency, throughput, correctness, saturation behavior, write behavior, complete submission lifecycle behavior, and Jira webhook ingestion against the deployed production-like Azure environment.

## Environment
- Target API: `https://api.researchtrack.blipzo.xyz`
- External runner: persistent VPS
- Tool: k6
- Dedicated ResearchTrack test project
- Authenticated supervisor/student test accounts
- Jira/GitHub integration routes included where applicable

## Method
Baseline profiles were repeated before thresholds were finalized. Final evidence runs were then executed with those runtime thresholds in place. Business metrics exclude login and warm-up requests. Warm-up still exercises the deployed system but avoids mixing authentication/cold-start behavior into the custom business latency gate.

## Workload separation
Smoke is appropriate as a continuous deployment gate. Heavy or side-effecting profiles are intentionally controlled/manual to avoid unnecessary stress, external integration load, and test-data churn.

## Quality dimensions
- p50/p90/p95/p99/max latency
- measured request throughput
- business failure rate
- correctness checks
- HTTP status distribution
- HTTP 429 count
- dropped iterations and active VUs
- endpoint-level metrics
- workflow/artifact traceability
