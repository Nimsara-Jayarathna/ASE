# ResearchTrack k6 — webhook

**Performance gate: PASS ✅**

Generated: 2026-10-07T16:19:26.998Z  
Target: https://api.researchtrack.blipzo.xyz  
Project: `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`  
Purpose: Signed Jira webhook burst and ingestion capacity  
Workload: Ramping signed webhook arrival rate 1→2→12 req/s (50 seconds)  
Execution mode: manual | Warm-up passes: 1 | Integrations: true | Gateway exemption: true
GitHub workflow: Azure Production - k6 Performance (VPS) | run 37643585579 attempt 1 | source SHA: `54dcbae67793a2103b6ef78502401bf4ab04b336`

## Executive summary

| Measure | Result | Target / meaning |
|---|---:|---|
| Business requests | 383 | Measured requests only |
| Throughput | 7.61 req/s | Business requests only |
| Business failure rate | 0.00% | < 2.00% |
| p50 latency | 328.26 ms | Median |
| p90 latency | 731.79 ms | Tail trend |
| p95 latency | 900.09 ms | < 1000 ms |
| p99 latency | 1011.04 ms | Extreme tail |
| Average latency | 414.95 ms | Informational |
| Min / max latency | 261.20 ms / 1084.01 ms | Range |
| HTTP 429 responses | 0 | 0 |
| Correctness checks | 100.00% | > 99% |
| Iterations / dropped | 383 / 2 | Scheduler health |
| Max active VUs | 14 | Workload context |

## Runtime threshold configuration

- **Overall webhook p95:** 1000 ms — source: GitHub/runtime variable (K6_WEBHOOK_P95_MS).
- **Correctness gates:** business failure rate < 2.00%, checks > 99%, HTTP 429 = 0.
- **Endpoint-specific p95 gates:** none configured for operations measured in this run.

## HTTP outcome distribution

| Outcome | Count |
|---|---:|
| 2xx | 383 |
| 3xx | 0 |
| 4xx | 0 |
| 5xx | 0 |
| Network errors (status 0) | 0 |
| 429 (subset of 4xx) | 0 |

## Endpoint performance

| Operation | Method | Requests | Failure | Avg | p50 | p90 | p95 | p99 | Max | Target p95 | Gate | 4xx | 5xx | 429 |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|
| Jira webhook ingestion | POST | 383 | 0.00% | 415.0 | 328.3 | 731.8 | 900.1 | 1011.0 | 1084.0 | — | Not gated | 0 | 0 | 0 |

## Slowest endpoints by p95

1. **Jira webhook ingestion** — p95 900.09 ms, p99 1011.04 ms, failures 0.00%

## Jira issues diagnostic

Jira issues was not measured in this run (integration routes disabled or profile does not use it).

## Failed / unhealthy endpoints

No endpoint recorded a business failure, 4xx, 5xx, or network error.

## Threshold evaluation

| Metric | Rule | Result |
|---|---|:---:|
| `researchtrack_http_429` | `count==0` | PASS ✅ |
| `checks` | `rate>0.99` | PASS ✅ |
| `researchtrack_business_failures` | `rate<0.02` | PASS ✅ |
| `researchtrack_business_duration` | `p(95)<1000` | PASS ✅ |

## Interpretation notes

- Business latency excludes login and warm-up requests; endpoint tables are based on explicit ResearchTrack business-operation metrics.
- Profile p95 thresholds are runtime configuration. Change the corresponding GitHub Actions variable after baseline review; no source-code push is required.
- Optional endpoint p95 gates come from `K6_ENDPOINT_P95_THRESHOLDS_JSON`; this is useful for the observed Jira Issues tail without forcing every endpoint to share the same target.
- Warm-up requests execute before measured traffic to reduce cold-start/JIT/connection-pool distortion. They still exercise the deployed system but are not included in the custom business gate.
- A threshold failure is a valid test result; reports are generated and Azure/Gateway restoration still runs.
- Manual results measure the current deployment. The GitHub source SHA is traceability metadata, not proof that every deployed service image was built from that SHA.
