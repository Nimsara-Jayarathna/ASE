# Viva Guide — Load & Performance Testing

## 30-second summary
“I designed and integrated production-environment performance testing using k6 from an external VPS. The suite uses real authenticated supervisor/student flows, seven workload profiles, runtime-configured p95 gates, correctness/error/429 gates, endpoint-level reporting, controlled Gateway rate-limit exemption, automatic post-deployment Smoke testing, and guaranteed Azure/Gateway restoration. Final evidence passed all seven profiles.”

## Why an external VPS?
It measures the deployed API through the real public Gateway/network path instead of only measuring localhost/container networking.

## Why p95 instead of average?
Average latency can hide slow-tail requests. p95 makes degradation visible for a meaningful portion of users while p99/max remain diagnostic.

## Why not one threshold for every endpoint?
Different operations have very different cost profiles. Jira Issues was consistently much slower and highly profile-dependent. A single endpoint-specific gate shared across all profiles would be misleading, so it remains diagnostic-only.

## Why is Smoke automatic but Stress/Spike manual?
Smoke is low impact and appropriate for every deployment. Stress/Spike intentionally create saturation pressure; Lifecycle and Write mutate data; Webhook generates integration traffic. Controlled execution is safer and gives cleaner evidence.

## Important final numbers
- Smoke p95 2357.58 ms < 3000 ms
- Load p95 2718.20 ms < 3000 ms
- Stress p95 2468.12 ms < 3500 ms
- Spike p95 2905.96 ms < 4500 ms
- Write p95 361.46 ms < 600 ms
- Lifecycle p95 788.24 ms < 1500 ms
- Webhook p95 900.09 ms < 1000 ms
- Final business failures: 0% on every profile
- Final checks: 100% on every profile
- Final HTTP 429: 0 on every profile

## Main technical finding
Jira Issues dominates read-profile tail latency. In the final evidence its p95 is around 4.3–4.8 seconds while most other read endpoints are a few hundred milliseconds. This is visible without turning it into a misleading one-size-fits-all endpoint gate.

## Capacity interpretation
Stress and Spike maintained correctness under higher demand. The final Stress run completed 2,774 requests at 19.40 req/s with no dropped iterations. The final Spike run showed only 2 dropped iterations while completed requests still had 0% business failures, showing scheduler/capacity pressure before functional correctness failure.

## Why Gateway bypass?
A single external load generator can be distorted by general IP rate limits. Heavy tests use a temporary exemption protected by both the discovered VPS egress IP and a dedicated token. The workflow restores the original Gateway state afterward.

## What happens if a threshold fails?
The run is marked as a performance failure, but reporting and state restoration still execute so the test remains auditable and does not leave the environment modified.
