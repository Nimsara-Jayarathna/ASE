# ResearchTrack k6 — spike

**Performance gate: PASS ✅**

Generated: 2026-10-07T15:56:06.852Z  
Target: https://api.researchtrack.blipzo.xyz  
Project: `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`  
Purpose: Sudden traffic burst and recovery behaviour  
Workload: Arrival-rate spike 2→40→2 req/s (55 seconds)  
Execution mode: manual | Warm-up passes: 1 | Integrations: true | Gateway exemption: true
GitHub workflow: Azure Production - k6 Performance (VPS) | run 37643479581 attempt 1 | source SHA: `54dcbae67793a2103b6ef78502401bf4ab04b336`

## Executive summary

| Measure | Result | Target / meaning |
|---|---:|---|
| Business requests | 1052 | Measured requests only |
| Throughput | 14.87 req/s | Business requests only |
| Business failure rate | 0.00% | < 5.00% |
| p50 latency | 274.86 ms | Median |
| p90 latency | 2078.24 ms | Tail trend |
| p95 latency | 2905.96 ms | < 4500 ms |
| p99 latency | 4688.58 ms | Extreme tail |
| Average latency | 641.50 ms | Informational |
| Min / max latency | 201.18 ms / 7631.50 ms | Range |
| HTTP 429 responses | 0 | 0 |
| Correctness checks | 100.00% | > 99% |
| Iterations / dropped | 1052 / 2 | Scheduler health |
| Max active VUs | 42 | Workload context |

## Runtime threshold configuration

- **Overall spike p95:** 4500 ms — source: GitHub/runtime variable (K6_SPIKE_P95_MS).
- **Correctness gates:** business failure rate < 5.00%, checks > 99%, HTTP 429 = 0.
- **Endpoint-specific p95 gates:** none configured for operations measured in this run.

## HTTP outcome distribution

| Outcome | Count |
|---|---:|
| 2xx | 1052 |
| 3xx | 0 |
| 4xx | 0 |
| 5xx | 0 |
| Network errors (status 0) | 0 |
| 429 (subset of 4xx) | 0 |

## Endpoint performance

| Operation | Method | Requests | Failure | Avg | p50 | p90 | p95 | p99 | Max | Target p95 | Gate | 4xx | 5xx | 429 |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|
| Jira issues | GET | 150 | 0.00% | 2814.2 | 2470.0 | 4390.6 | 4774.5 | 6130.7 | 7631.5 | — | Not gated | 0 | 0 | 0 |
| Jira sprint progress | GET | 132 | 0.00% | 338.6 | 291.1 | 511.8 | 613.1 | 761.2 | 823.3 | — | Not gated | 0 | 0 | 0 |
| Submission history | GET | 144 | 0.00% | 292.1 | 286.3 | 332.1 | 360.9 | 456.0 | 595.7 | — | Not gated | 0 | 0 | 0 |
| Submission requirements | GET | 146 | 0.00% | 282.1 | 279.4 | 318.1 | 347.0 | 428.4 | 463.7 | — | Not gated | 0 | 0 | 0 |
| GitHub activity | GET | 136 | 0.00% | 290.1 | 280.2 | 316.3 | 334.9 | 396.2 | 1270.6 | — | Not gated | 0 | 0 | 0 |
| Supervisor dashboard | GET | 65 | 0.00% | 251.6 | 254.8 | 298.0 | 310.6 | 334.2 | 349.7 | — | Not gated | 0 | 0 | 0 |
| Project details | GET | 139 | 0.00% | 252.8 | 255.6 | 286.5 | 298.1 | 324.0 | 447.1 | — | Not gated | 0 | 0 | 0 |
| List projects | GET | 140 | 0.00% | 241.7 | 241.6 | 277.1 | 291.7 | 338.9 | 343.9 | — | Not gated | 0 | 0 | 0 |

## Slowest endpoints by p95

1. **Jira issues** — p95 4774.51 ms, p99 6130.71 ms, failures 0.00%
2. **Jira sprint progress** — p95 613.11 ms, p99 761.18 ms, failures 0.00%
3. **Submission history** — p95 360.90 ms, p99 455.98 ms, failures 0.00%
4. **Submission requirements** — p95 347.01 ms, p99 428.45 ms, failures 0.00%
5. **GitHub activity** — p95 334.93 ms, p99 396.19 ms, failures 0.00%

## Jira issues diagnostic

Jira issues recorded **150** measured request(s): p50 2469.99 ms, p90 4390.57 ms, p95 4774.51 ms, p99 6130.71 ms. Endpoint gate: **Not gated** (configure it after baseline runs if desired).

## Failed / unhealthy endpoints

No endpoint recorded a business failure, 4xx, 5xx, or network error.

## Threshold evaluation

| Metric | Rule | Result |
|---|---|:---:|
| `checks` | `rate>0.99` | PASS ✅ |
| `researchtrack_http_429` | `count==0` | PASS ✅ |
| `researchtrack_business_failures` | `rate<0.05` | PASS ✅ |
| `researchtrack_business_duration` | `p(95)<4500` | PASS ✅ |

## Interpretation notes

- Business latency excludes login and warm-up requests; endpoint tables are based on explicit ResearchTrack business-operation metrics.
- Profile p95 thresholds are runtime configuration. Change the corresponding GitHub Actions variable after baseline review; no source-code push is required.
- Optional endpoint p95 gates come from `K6_ENDPOINT_P95_THRESHOLDS_JSON`; this is useful for the observed Jira Issues tail without forcing every endpoint to share the same target.
- Warm-up requests execute before measured traffic to reduce cold-start/JIT/connection-pool distortion. They still exercise the deployed system but are not included in the custom business gate.
- A threshold failure is a valid test result; reports are generated and Azure/Gateway restoration still runs.
- Manual results measure the current deployment. The GitHub source SHA is traceability metadata, not proof that every deployed service image was built from that SHA.
