# ResearchTrack k6 — write

**Performance gate: PASS ✅**

Generated: 2026-10-07T16:04:03.877Z  
Target: https://api.researchtrack.blipzo.xyz  
Project: `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`  
Purpose: Bounded create/delete submission-requirement writes  
Workload: 1 iteration every 3 seconds for 30 seconds  
Execution mode: manual | Warm-up passes: 1 | Integrations: true | Gateway exemption: true
GitHub workflow: Azure Production - k6 Performance (VPS) | run 37643509472 attempt 1 | source SHA: `54dcbae67793a2103b6ef78502401bf4ab04b336`

## Executive summary

| Measure | Result | Target / meaning |
|---|---:|---|
| Business requests | 20 | Measured requests only |
| Throughput | 0.63 req/s | Business requests only |
| Business failure rate | 0.00% | < 2.00% |
| p50 latency | 256.13 ms | Median |
| p90 latency | 341.14 ms | Tail trend |
| p95 latency | 361.46 ms | < 600 ms |
| p99 latency | 412.18 ms | Extreme tail |
| Average latency | 276.44 ms | Informational |
| Min / max latency | 235.32 ms / 424.86 ms | Range |
| HTTP 429 responses | 0 | 0 |
| Correctness checks | 100.00% | > 99% |
| Iterations / dropped | 10 / 0 | Scheduler health |
| Max active VUs | 2 | Workload context |

## Runtime threshold configuration

- **Overall write p95:** 600 ms — source: GitHub/runtime variable (K6_WRITE_P95_MS).
- **Correctness gates:** business failure rate < 2.00%, checks > 99%, HTTP 429 = 0.
- **Endpoint-specific p95 gates:** none configured for operations measured in this run.

## HTTP outcome distribution

| Outcome | Count |
|---|---:|
| 2xx | 20 |
| 3xx | 0 |
| 4xx | 0 |
| 5xx | 0 |
| Network errors (status 0) | 0 |
| 429 (subset of 4xx) | 0 |

## Endpoint performance

| Operation | Method | Requests | Failure | Avg | p50 | p90 | p95 | p99 | Max | Target p95 | Gate | 4xx | 5xx | 429 |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|
| Create submission requirement | POST | 10 | 0.00% | 279.2 | 259.7 | 309.4 | 367.1 | 413.3 | 424.9 | — | Not gated | 0 | 0 | 0 |
| Delete submission requirement | DELETE | 10 | 0.00% | 273.7 | 251.8 | 341.1 | 349.6 | 356.4 | 358.1 | — | Not gated | 0 | 0 | 0 |

## Slowest endpoints by p95

1. **Create submission requirement** — p95 367.14 ms, p99 413.31 ms, failures 0.00%
2. **Delete submission requirement** — p95 349.63 ms, p99 356.43 ms, failures 0.00%

## Jira issues diagnostic

Jira issues was not measured in this run (integration routes disabled or profile does not use it).

## Failed / unhealthy endpoints

No endpoint recorded a business failure, 4xx, 5xx, or network error.

## Threshold evaluation

| Metric | Rule | Result |
|---|---|:---:|
| `researchtrack_business_failures` | `rate<0.02` | PASS ✅ |
| `checks` | `rate>0.99` | PASS ✅ |
| `researchtrack_http_429` | `count==0` | PASS ✅ |
| `researchtrack_business_duration` | `p(95)<600` | PASS ✅ |

## Interpretation notes

- Business latency excludes login and warm-up requests; endpoint tables are based on explicit ResearchTrack business-operation metrics.
- Profile p95 thresholds are runtime configuration. Change the corresponding GitHub Actions variable after baseline review; no source-code push is required.
- Optional endpoint p95 gates come from `K6_ENDPOINT_P95_THRESHOLDS_JSON`; this is useful for the observed Jira Issues tail without forcing every endpoint to share the same target.
- Warm-up requests execute before measured traffic to reduce cold-start/JIT/connection-pool distortion. They still exercise the deployed system but are not included in the custom business gate.
- A threshold failure is a valid test result; reports are generated and Azure/Gateway restoration still runs.
- Manual results measure the current deployment. The GitHub source SHA is traceability metadata, not proof that every deployed service image was built from that SHA.
