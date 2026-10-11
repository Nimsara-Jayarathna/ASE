# CI/CD Performance Runbook

## Automatic Smoke
After a successful production deployment, run the lightweight Smoke profile automatically. It validates authenticated end-to-end production readiness and latency without applying a heavy workload.

## Manual profiles
Use the normal `Azure Production - k6 Performance (VPS)` wrapper and select the required profile. Keep the one-run p95 override blank for final evidence so the configured runtime profile threshold is used.

## Heavy-run sequence
1. Capture current Azure runtime and Gateway state.
2. Discover the VPS public egress IP.
3. Apply the temporary performance exemption only when configured and authorized.
4. Execute k6 on the VPS.
5. Generate HTML, Markdown, JSON, CSV, and raw log evidence.
6. Upload artifacts even when a k6 threshold fails.
7. Restore Gateway and Azure state independently.
8. Verify restoration.

## Failure interpretation
A threshold failure is a valid test result and should not prevent evidence upload/restoration. `status=0` means k6 did not receive an HTTP response and should be investigated as network/readiness/timeout behavior rather than interpreted as a normal application status code.

## Scheduling recommendation
Keep automatic Smoke on production deployments. Heavy profiles should remain manual unless a deliberate nightly regression policy is required. If scheduled regression testing is added, start with Load rather than automatically running Stress/Spike/Lifecycle/Webhook every day.
