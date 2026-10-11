# ResearchTrack k6 — smoke

**Performance gate: PASS ✅**

Generated: 2026-10-07T15:29:02.803Z  
Target: https://api.researchtrack.blipzo.xyz  
Project: `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`  
Purpose: Fast authenticated deployment-health and latency check  
Workload: 2 looping VUs for 45 seconds  
Execution mode: manual | Warm-up passes: 1 | Integrations: true | Gateway exemption: true
GitHub workflow: Azure Production - k6 Performance (VPS) | run 37643383515 attempt 1 | source SHA: `54dcbae67793a2103b6ef78502401bf4ab04b336`

## Executive summary

| Measure | Result | Target / meaning |
|---|---:|---|
| Business requests | 55 | Measured requests only |
| Throughput | 0.98 req/s | Business requests only |
| Business failure rate | 0.00% | < 1.00% |
| p50 latency | 280.51 ms | Median |
| p90 latency | 1902.89 ms | Tail trend |
| p95 latency | 2357.58 ms | < 3000 ms |
| p99 latency | 4094.71 ms | Extreme tail |
| Average latency | 608.59 ms | Informational |
| Min / max latency | 207.61 ms / 4673.99 ms | Range |
| HTTP 429 responses | 0 | 0 |
| Correctness checks | 100.00% | > 99% |
| Iterations / dropped | 55 / 0 | Scheduler health |
| Max active VUs | 2 | Workload context |

## Runtime threshold configuration

- **Overall smoke p95:** 3000 ms — source: GitHub/runtime variable (K6_SMOKE_P95_MS).
- **Correctness gates:** business failure rate < 1.00%, checks > 99%, HTTP 429 = 0.
- **Endpoint-specific p95 gates:** none configured for operations measured in this run.

## HTTP outcome distribution

| Outcome | Count |
|---|---:|
| 2xx | 55 |
| 3xx | 0 |
| 4xx | 0 |
| 5xx | 0 |
| Network errors (status 0) | 0 |
| 429 (subset of 4xx) | 0 |

## Endpoint performance

| Operation | Method | Requests | Failure | Avg | p50 | p90 | p95 | p99 | Max | Target p95 | Gate | 4xx | 5xx | 429 |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|
| Jira issues | GET | 8 | 0.00% | 2582.9 | 2294.5 | 3923.1 | 4298.5 | 4598.9 | 4674.0 | — | Not gated | 0 | 0 | 0 |
| GitHub activity | GET | 7 | 0.00% | 306.6 | 301.1 | 372.5 | 389.5 | 403.0 | 406.4 | — | Not gated | 0 | 0 | 0 |
| Submission requirements | GET | 8 | 0.00% | 291.2 | 304.0 | 324.6 | 341.2 | 354.6 | 357.9 | — | Not gated | 0 | 0 | 0 |
| Project details | GET | 7 | 0.00% | 263.0 | 275.6 | 320.7 | 321.6 | 322.4 | 322.5 | — | Not gated | 0 | 0 | 0 |
| Submission history | GET | 8 | 0.00% | 287.3 | 291.7 | 308.7 | 318.9 | 327.0 | 329.0 | — | Not gated | 0 | 0 | 0 |
| Jira sprint progress | GET | 7 | 0.00% | 269.2 | 279.8 | 297.8 | 307.6 | 315.5 | 317.5 | — | Not gated | 0 | 0 | 0 |
| List projects | GET | 7 | 0.00% | 240.4 | 251.0 | 270.5 | 275.5 | 279.5 | 280.5 | — | Not gated | 0 | 0 | 0 |
| Supervisor dashboard | GET | 3 | 0.00% | 208.8 | 209.0 | 209.5 | 209.6 | 209.6 | 209.6 | — | Not gated | 0 | 0 | 0 |

## Slowest endpoints by p95

1. **Jira issues** — p95 4298.53 ms, p99 4598.90 ms, failures 0.00%
2. **GitHub activity** — p95 389.47 ms, p99 403.04 ms, failures 0.00%
3. **Submission requirements** — p95 341.23 ms, p99 354.57 ms, failures 0.00%
4. **Project details** — p95 321.60 ms, p99 322.36 ms, failures 0.00%
5. **Submission history** — p95 318.89 ms, p99 327.01 ms, failures 0.00%

## Jira issues diagnostic

Jira issues recorded **8** measured request(s): p50 2294.51 ms, p90 3923.08 ms, p95 4298.53 ms, p99 4598.90 ms. Endpoint gate: **Not gated** (configure it after baseline runs if desired).

## Failed / unhealthy endpoints

No endpoint recorded a business failure, 4xx, 5xx, or network error.

## Threshold evaluation

| Metric | Rule | Result |
|---|---|:---:|
| `researchtrack_business_duration` | `p(95)<3000` | PASS ✅ |
| `researchtrack_http_429` | `count==0` | PASS ✅ |
| `checks` | `rate>0.99` | PASS ✅ |
| `researchtrack_business_failures` | `rate<0.01` | PASS ✅ |

## Interpretation notes

- Business latency excludes login and warm-up requests; endpoint tables are based on explicit ResearchTrack business-operation metrics.
- Profile p95 thresholds are runtime configuration. Change the corresponding GitHub Actions variable after baseline review; no source-code push is required.
- Optional endpoint p95 gates come from `K6_ENDPOINT_P95_THRESHOLDS_JSON`; this is useful for the observed Jira Issues tail without forcing every endpoint to share the same target.
- Warm-up requests execute before measured traffic to reduce cold-start/JIT/connection-pool distortion. They still exercise the deployed system but are not included in the custom business gate.
- A threshold failure is a valid test result; reports are generated and Azure/Gateway restoration still runs.
- Manual results measure the current deployment. The GitHub source SHA is traceability metadata, not proof that every deployed service image was built from that SHA.
