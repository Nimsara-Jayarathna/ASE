# Security Notes

- Do not commit real application passwords, cloud access keys, Jira client secrets, SSH private keys, rate-limit-bypass tokens, or temporary signed storage URLs.
- The evidence package contains only test results and non-secret configuration names.
- Preserve the original artifact ZIPs for traceability but review raw logs before public distribution.
- Gateway performance exemption must be temporary, IP-bound, token-protected, and restored after the run.
- Dedicated test accounts and a dedicated test project should be used for performance workloads.
