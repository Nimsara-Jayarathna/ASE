# ResearchTrack k6 — load

**Performance gate: PASS ✅**

Generated: 2026-10-07T15:38:32.860Z  
Target: https://api.researchtrack.blipzo.xyz  
Project: `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`  
Purpose: Expected concurrent read workload and steady-state capacity  
Workload: Ramping arrival rate 2→4→10 req/s, then cooldown (135 seconds)  
Execution mode: manual | Warm-up passes: 1 | Integrations: true | Gateway exemption: true
GitHub workflow: Azure Production - k6 Performance (VPS) | run 37643412866 attempt 1 | source SHA: `54dcbae67793a2103b6ef78502401bf4ab04b336`

## Executive summary

| Measure | Result | Target / meaning |
|---|---:|---|
| Business requests | 930 | Measured requests only |
| Throughput | 6.52 req/s | Business requests only |
| Business failure rate | 0.00% | < 2.00% |
| p50 latency | 268.63 ms | Median |
| p90 latency | 2034.81 ms | Tail trend |
| p95 latency | 2718.20 ms | < 3000 ms |
| p99 latency | 4058.08 ms | Extreme tail |
| Average latency | 608.63 ms | Informational |
| Min / max latency | 200.97 ms / 12094.29 ms | Range |
| HTTP 429 responses | 0 | 0 |
| Correctness checks | 100.00% | > 99% |
| Iterations / dropped | 930 / 0 | Scheduler health |
| Max active VUs | 25 | Workload context |

## Runtime threshold configuration

- **Overall load p95:** 3000 ms — source: GitHub/runtime variable (K6_LOAD_P95_MS).
- **Correctness gates:** business failure rate < 2.00%, checks > 99%, HTTP 429 = 0.
- **Endpoint-specific p95 gates:** none configured for operations measured in this run.

## HTTP outcome distribution

| Outcome | Count |
|---|---:|
| 2xx | 930 |
| 3xx | 0 |
| 4xx | 0 |
| 5xx | 0 |
| Network errors (status 0) | 0 |
| 429 (subset of 4xx) | 0 |

## Endpoint performance

| Operation | Method | Requests | Failure | Avg | p50 | p90 | p95 | p99 | Max | Target p95 | Gate | 4xx | 5xx | 429 |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|
| Jira issues | GET | 126 | 0.00% | 2760.6 | 2458.7 | 3757.9 | 4371.3 | 10068.5 | 12094.3 | — | Not gated | 0 | 0 | 0 |
| Jira sprint progress | GET | 125 | 0.00% | 273.0 | 256.8 | 308.8 | 354.5 | 405.5 | 1117.0 | — | Not gated | 0 | 0 | 0 |
| GitHub activity | GET | 123 | 0.00% | 287.5 | 275.1 | 329.1 | 350.4 | 506.6 | 577.8 | — | Not gated | 0 | 0 | 0 |
| Submission history | GET | 124 | 0.00% | 292.6 | 274.9 | 326.9 | 346.9 | 643.0 | 824.7 | — | Not gated | 0 | 0 | 0 |
| Submission requirements | GET | 126 | 0.00% | 280.2 | 264.7 | 315.8 | 338.2 | 452.0 | 538.0 | — | Not gated | 0 | 0 | 0 |
| List projects | GET | 125 | 0.00% | 247.7 | 227.5 | 288.0 | 327.0 | 449.4 | 667.0 | — | Not gated | 0 | 0 | 0 |
| Project details | GET | 124 | 0.00% | 260.9 | 245.5 | 296.3 | 309.9 | 369.6 | 692.1 | — | Not gated | 0 | 0 | 0 |
| Supervisor dashboard | GET | 57 | 0.00% | 241.8 | 237.8 | 277.6 | 302.4 | 349.4 | 374.5 | — | Not gated | 0 | 0 | 0 |

## Slowest endpoints by p95

1. **Jira issues** — p95 4371.34 ms, p99 10068.50 ms, failures 0.00%
2. **Jira sprint progress** — p95 354.47 ms, p99 405.48 ms, failures 0.00%
3. **GitHub activity** — p95 350.37 ms, p99 506.65 ms, failures 0.00%
4. **Submission history** — p95 346.89 ms, p99 643.00 ms, failures 0.00%
5. **Submission requirements** — p95 338.16 ms, p99 451.98 ms, failures 0.00%

## Jira issues diagnostic

Jira issues recorded **126** measured request(s): p50 2458.69 ms, p90 3757.95 ms, p95 4371.34 ms, p99 10068.50 ms. Endpoint gate: **Not gated** (configure it after baseline runs if desired).

## Failed / unhealthy endpoints

No endpoint recorded a business failure, 4xx, 5xx, or network error.

## Threshold evaluation

| Metric | Rule | Result |
|---|---|:---:|
| `researchtrack_http_429` | `count==0` | PASS ✅ |
| `researchtrack_business_duration` | `p(95)<3000` | PASS ✅ |
| `checks` | `rate>0.99` | PASS ✅ |
| `researchtrack_business_failures` | `rate<0.02` | PASS ✅ |

## Interpretation notes

- Business latency excludes login and warm-up requests; endpoint tables are based on explicit ResearchTrack business-operation metrics.
- Profile p95 thresholds are runtime configuration. Change the corresponding GitHub Actions variable after baseline review; no source-code push is required.
- Optional endpoint p95 gates come from `K6_ENDPOINT_P95_THRESHOLDS_JSON`; this is useful for the observed Jira Issues tail without forcing every endpoint to share the same target.
- Warm-up requests execute before measured traffic to reduce cold-start/JIT/connection-pool distortion. They still exercise the deployed system but are not included in the custom business gate.
- A threshold failure is a valid test result; reports are generated and Azure/Gateway restoration still runs.
- Manual results measure the current deployment. The GitHub source SHA is traceability metadata, not proof that every deployed service image was built from that SHA.
