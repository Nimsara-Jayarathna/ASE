# Final Performance Results

These are the final evidence runs executed against `https://api.researchtrack.blipzo.xyz` using project `09a2eff6-2dde-4ce1-abfb-80dec08ad7f3`. All seven profiles passed their finalized runtime gates.

| Profile | Run | Requests | Throughput req/s | Failure | p50 ms | p90 ms | p95 ms | p99 ms | Max ms | Checks | 429 | Iter / dropped | Max VUs | p95 gate | Result |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| Smoke | 37643383515 | 55 | 0.98 | 0.00% | 280.51 | 1902.89 | **2357.58** | 4094.71 | 4673.99 | 100.00% | 0 | 55 / 0 | 2 | < 3000 ms | PASS ✅ |
| Load | 37643412866 | 930 | 6.52 | 0.00% | 268.63 | 2034.81 | **2718.20** | 4058.08 | 12094.29 | 100.00% | 0 | 930 / 0 | 25 | < 3000 ms | PASS ✅ |
| Stress | 37643438215 | 2774 | 19.40 | 0.00% | 270.10 | 1927.80 | **2468.12** | 3784.08 | 15219.47 | 100.00% | 0 | 2774 / 0 | 40 | < 3500 ms | PASS ✅ |
| Spike | 37643479581 | 1052 | 14.87 | 0.00% | 274.86 | 2078.24 | **2905.96** | 4688.58 | 7631.50 | 100.00% | 0 | 1052 / 2 | 42 | < 4500 ms | PASS ✅ |
| Write | 37643509472 | 20 | 0.63 | 0.00% | 256.13 | 341.14 | **361.46** | 412.18 | 424.86 | 100.00% | 0 | 10 / 0 | 2 | < 600 ms | PASS ✅ |
| Lifecycle | 37643554102 | 11 | 1.39 | 0.00% | 370.89 | 711.79 | **788.24** | 849.40 | 864.69 | 100.00% | 0 | 1 / 0 | 1 | < 1500 ms | PASS ✅ |
| Webhook | 37643585579 | 383 | 7.61 | 0.00% | 328.26 | 731.79 | **900.09** | 1011.04 | 1084.01 | 100.00% | 0 | 383 / 2 | 14 | < 1000 ms | PASS ✅ |

## Jira Issues diagnostic

`K6_ENDPOINT_P95_THRESHOLDS_JSON` is intentionally not configured. Jira Issues is retained as an endpoint diagnostic because its latency changes materially with workload intensity, while the rest of the measured endpoints remain much lower. A single endpoint-specific threshold shared across every profile would therefore be misleading.

| Profile | Jira Issues requests | p50 ms | p90 ms | p95 ms | p99 ms | Max ms | Failures |
|---|---:|---:|---:|---:|---:|---:|---:|
| Smoke | 8 | 2294.51 | 3923.08 | 4298.53 | 4598.90 | 4673.99 | 0.00% |
| Load | 126 | 2458.69 | 3757.95 | 4371.34 | 10068.50 | 12094.29 | 0.00% |
| Stress | 373 | 2251.02 | 3381.94 | 4406.93 | 9250.62 | 15219.47 | 0.00% |
| Spike | 150 | 2469.99 | 4390.57 | 4774.51 | 6130.71 | 7631.50 | 0.00% |

## Final findings

- Every final evidence profile passed its overall p95 threshold and correctness gates.
- Every final profile recorded 0 HTTP 429 responses, 0 measured business failures, and 100% correctness checks.
- Stress completed 2,774 measured requests at 19.40 req/s with no dropped iterations in the final run.
- Spike completed 1,052 measured requests at 14.87 req/s with only 2 dropped iterations and no business failures, showing short-lived scheduler pressure without correctness loss.
- Write completed 10 bounded create/delete cycles with p95 361.46 ms against a 600 ms gate.
- Lifecycle completed the complete 11-operation submission version workflow, including both S3 object PUT operations, with p95 788.24 ms against a 1,500 ms gate.
- Webhook processed 383 signed Jira webhook requests with p95 900.09 ms against a 1,000 ms gate and 0 failures.
- Jira Issues remains the dominant tail-latency contributor in read-heavy profiles and is reported diagnostically rather than forced under a misleading single endpoint threshold.
