# ResearchTrack k6 — stress

**Performance gate: PASS ✅**

Generated: 2026-10-07T15:47:43.159Z  
Target: https://api.researchtrack.blipzo.xyz  
Project: `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`  
Purpose: Increasing demand to expose saturation and latency degradation  
Workload: Ramping arrival rate 5→10→25→40 req/s, then cooldown (135 seconds)  
Execution mode: manual | Warm-up passes: 1 | Integrations: true | Gateway exemption: true
GitHub workflow: Azure Production - k6 Performance (VPS) | run 37643438215 attempt 1 | source SHA: `54dcbae67793a2103b6ef78502401bf4ab04b336`

## Executive summary

| Measure | Result | Target / meaning |
|---|---:|---|
| Business requests | 2774 | Measured requests only |
| Throughput | 19.40 req/s | Business requests only |
| Business failure rate | 0.00% | < 5.00% |
| p50 latency | 270.10 ms | Median |
| p90 latency | 1927.80 ms | Tail trend |
| p95 latency | 2468.12 ms | < 3500 ms |
| p99 latency | 3784.08 ms | Extreme tail |
| Average latency | 580.61 ms | Informational |
| Min / max latency | 199.51 ms / 15219.47 ms | Range |
| HTTP 429 responses | 0 | 0 |
| Correctness checks | 100.00% | > 99% |
| Iterations / dropped | 2774 / 0 | Scheduler health |
| Max active VUs | 40 | Workload context |

## Runtime threshold configuration

- **Overall stress p95:** 3500 ms — source: GitHub/runtime variable (K6_STRESS_P95_MS).
- **Correctness gates:** business failure rate < 5.00%, checks > 99%, HTTP 429 = 0.
- **Endpoint-specific p95 gates:** none configured for operations measured in this run.

## HTTP outcome distribution

| Outcome | Count |
|---|---:|
| 2xx | 2774 |
| 3xx | 0 |
| 4xx | 0 |
| 5xx | 0 |
| Network errors (status 0) | 0 |
| 429 (subset of 4xx) | 0 |

## Endpoint performance

| Operation | Method | Requests | Failure | Avg | p50 | p90 | p95 | p99 | Max | Target p95 | Gate | 4xx | 5xx | 429 |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|
| Jira issues | GET | 373 | 0.00% | 2556.0 | 2251.0 | 3381.9 | 4406.9 | 9250.6 | 15219.5 | — | Not gated | 0 | 0 | 0 |
| Jira sprint progress | GET | 366 | 0.00% | 294.3 | 279.9 | 390.5 | 452.1 | 629.9 | 716.4 | — | Not gated | 0 | 0 | 0 |
| GitHub activity | GET | 369 | 0.00% | 285.5 | 277.7 | 321.5 | 376.4 | 482.8 | 653.1 | — | Not gated | 0 | 0 | 0 |
| Submission requirements | GET | 373 | 0.00% | 285.9 | 277.9 | 314.7 | 365.1 | 633.8 | 764.0 | — | Not gated | 0 | 0 | 0 |
| Submission history | GET | 372 | 0.00% | 291.4 | 278.0 | 324.0 | 347.4 | 510.7 | 1856.1 | — | Not gated | 0 | 0 | 0 |
| Project details | GET | 373 | 0.00% | 254.6 | 248.5 | 292.2 | 310.4 | 382.1 | 596.0 | — | Not gated | 0 | 0 | 0 |
| List projects | GET | 373 | 0.00% | 243.7 | 241.0 | 278.6 | 308.7 | 409.5 | 556.9 | — | Not gated | 0 | 0 | 0 |
| Supervisor dashboard | GET | 175 | 0.00% | 246.9 | 243.2 | 280.9 | 306.9 | 511.3 | 620.6 | — | Not gated | 0 | 0 | 0 |

## Slowest endpoints by p95

1. **Jira issues** — p95 4406.93 ms, p99 9250.62 ms, failures 0.00%
2. **Jira sprint progress** — p95 452.09 ms, p99 629.86 ms, failures 0.00%
3. **GitHub activity** — p95 376.42 ms, p99 482.80 ms, failures 0.00%
4. **Submission requirements** — p95 365.13 ms, p99 633.81 ms, failures 0.00%
5. **Submission history** — p95 347.35 ms, p99 510.70 ms, failures 0.00%

## Jira issues diagnostic

Jira issues recorded **373** measured request(s): p50 2251.02 ms, p90 3381.94 ms, p95 4406.93 ms, p99 9250.62 ms. Endpoint gate: **Not gated** (configure it after baseline runs if desired).

## Failed / unhealthy endpoints

No endpoint recorded a business failure, 4xx, 5xx, or network error.

## Threshold evaluation

| Metric | Rule | Result |
|---|---|:---:|
| `researchtrack_business_duration` | `p(95)<3500` | PASS ✅ |
| `researchtrack_http_429` | `count==0` | PASS ✅ |
| `researchtrack_business_failures` | `rate<0.05` | PASS ✅ |
| `checks` | `rate>0.99` | PASS ✅ |

## Interpretation notes

- Business latency excludes login and warm-up requests; endpoint tables are based on explicit ResearchTrack business-operation metrics.
- Profile p95 thresholds are runtime configuration. Change the corresponding GitHub Actions variable after baseline review; no source-code push is required.
- Optional endpoint p95 gates come from `K6_ENDPOINT_P95_THRESHOLDS_JSON`; this is useful for the observed Jira Issues tail without forcing every endpoint to share the same target.
- Warm-up requests execute before measured traffic to reduce cold-start/JIT/connection-pool distortion. They still exercise the deployed system but are not included in the custom business gate.
- A threshold failure is a valid test result; reports are generated and Azure/Gateway restoration still runs.
- Manual results measure the current deployment. The GitHub source SHA is traceability metadata, not proof that every deployed service image was built from that SHA.
