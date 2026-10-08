# ResearchTrack k6 — lifecycle

**Performance gate: PASS ✅**

Generated: 2026-10-07T16:11:27.739Z  
Target: https://api.researchtrack.blipzo.xyz  
Project: `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`  
Purpose: Full student/supervisor submission version lifecycle  
Workload: 1 VU × 1 complete lifecycle, max 3 minutes  
Execution mode: manual | Warm-up passes: 1 | Integrations: true | Gateway exemption: true
GitHub workflow: Azure Production - k6 Performance (VPS) | run 37643554102 attempt 1 | source SHA: `54dcbae67793a2103b6ef78502401bf4ab04b336`

## Executive summary

| Measure | Result | Target / meaning |
|---|---:|---|
| Business requests | 11 | Measured requests only |
| Throughput | 1.39 req/s | Business requests only |
| Business failure rate | 0.00% | < 1.00% |
| p50 latency | 370.89 ms | Median |
| p90 latency | 711.79 ms | Tail trend |
| p95 latency | 788.24 ms | < 1500 ms |
| p99 latency | 849.40 ms | Extreme tail |
| Average latency | 486.35 ms | Informational |
| Min / max latency | 195.32 ms / 864.69 ms | Range |
| HTTP 429 responses | 0 | 0 |
| Correctness checks | 100.00% | > 99% |
| Iterations / dropped | 1 / 0 | Scheduler health |
| Max active VUs | 1 | Workload context |

## Runtime threshold configuration

- **Overall lifecycle p95:** 1500 ms — source: GitHub/runtime variable (K6_LIFECYCLE_P95_MS).
- **Correctness gates:** business failure rate < 1.00%, checks > 99%, HTTP 429 = 0.
- **Endpoint-specific p95 gates:** none configured for operations measured in this run.

## HTTP outcome distribution

| Outcome | Count |
|---|---:|
| 2xx | 11 |
| 3xx | 0 |
| 4xx | 0 |
| 5xx | 0 |
| Network errors (status 0) | 0 |
| 429 (subset of 4xx) | 0 |

## Endpoint performance

| Operation | Method | Requests | Failure | Avg | p50 | p90 | p95 | p99 | Max | Target p95 | Gate | 4xx | 5xx | 429 |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|
| Complete v1 upload | POST | 1 | 0.00% | 864.7 | 864.7 | 864.7 | 864.7 | 864.7 | 864.7 | — | Not gated | 0 | 0 | 0 |
| Request submission changes | POST | 1 | 0.00% | 711.8 | 711.8 | 711.8 | 711.8 | 711.8 | 711.8 | — | Not gated | 0 | 0 | 0 |
| Create submission requirement | POST | 1 | 0.00% | 696.6 | 696.6 | 696.6 | 696.6 | 696.6 | 696.6 | — | Not gated | 0 | 0 | 0 |
| Complete v2 upload | POST | 1 | 0.00% | 659.5 | 659.5 | 659.5 | 659.5 | 659.5 | 659.5 | — | Not gated | 0 | 0 | 0 |
| Approve submission | POST | 1 | 0.00% | 650.8 | 650.8 | 650.8 | 650.8 | 650.8 | 650.8 | — | Not gated | 0 | 0 | 0 |
| Create v1 upload session | POST | 1 | 0.00% | 370.9 | 370.9 | 370.9 | 370.9 | 370.9 | 370.9 | — | Not gated | 0 | 0 | 0 |
| Create v2 upload session | POST | 1 | 0.00% | 347.6 | 347.6 | 347.6 | 347.6 | 347.6 | 347.6 | — | Not gated | 0 | 0 | 0 |
| Archive test requirement | POST | 1 | 0.00% | 331.7 | 331.7 | 331.7 | 331.7 | 331.7 | 331.7 | — | Not gated | 0 | 0 | 0 |
| Verify version history | GET | 1 | 0.00% | 320.1 | 320.1 | 320.1 | 320.1 | 320.1 | 320.1 | — | Not gated | 0 | 0 | 0 |
| Upload v1 object | PUT | 1 | 0.00% | 200.9 | 200.9 | 200.9 | 200.9 | 200.9 | 200.9 | — | Not gated | 0 | 0 | 0 |
| Upload v2 object | PUT | 1 | 0.00% | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | — | Not gated | 0 | 0 | 0 |

## Slowest endpoints by p95

1. **Complete v1 upload** — p95 864.69 ms, p99 864.69 ms, failures 0.00%
2. **Request submission changes** — p95 711.79 ms, p99 711.79 ms, failures 0.00%
3. **Create submission requirement** — p95 696.59 ms, p99 696.59 ms, failures 0.00%
4. **Complete v2 upload** — p95 659.52 ms, p99 659.52 ms, failures 0.00%
5. **Approve submission** — p95 650.82 ms, p99 650.82 ms, failures 0.00%

## Jira issues diagnostic

Jira issues was not measured in this run (integration routes disabled or profile does not use it).

## Failed / unhealthy endpoints

No endpoint recorded a business failure, 4xx, 5xx, or network error.

## Threshold evaluation

| Metric | Rule | Result |
|---|---|:---:|
| `checks` | `rate>0.99` | PASS ✅ |
| `researchtrack_http_429` | `count==0` | PASS ✅ |
| `researchtrack_business_failures` | `rate<0.01` | PASS ✅ |
| `researchtrack_business_duration` | `p(95)<1500` | PASS ✅ |

## Interpretation notes

- Business latency excludes login and warm-up requests; endpoint tables are based on explicit ResearchTrack business-operation metrics.
- Profile p95 thresholds are runtime configuration. Change the corresponding GitHub Actions variable after baseline review; no source-code push is required.
- Optional endpoint p95 gates come from `K6_ENDPOINT_P95_THRESHOLDS_JSON`; this is useful for the observed Jira Issues tail without forcing every endpoint to share the same target.
- Warm-up requests execute before measured traffic to reduce cold-start/JIT/connection-pool distortion. They still exercise the deployed system but are not included in the custom business gate.
- A threshold failure is a valid test result; reports are generated and Azure/Gateway restoration still runs.
- Manual results measure the current deployment. The GitHub source SHA is traceability metadata, not proof that every deployed service image was built from that SHA.
