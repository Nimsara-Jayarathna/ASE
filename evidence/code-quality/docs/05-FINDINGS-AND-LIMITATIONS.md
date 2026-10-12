# 05 — Remaining Findings & Evidence Limitations

The completed run has **Quality Gate OK**, but that does **not** imply that every historical issue is resolved.

## Findings to review in the backend SonarQube dashboard

The final Actions log supplied with the final run listed these example annotations:

- `AuthCookieService.cs` — static rule asks for cookie `Secure` to be set. The production configuration enforces secure cookies outside local development/testing, but configuration-dependent values may still be reported by static analysis. Confirm the runtime behavior before classifying these findings.
- `DesignTimeDatabase.cs` — literal `design` credentials in an intentionally design-time scaffolding fallback. Review context in SonarQube; the warning alone does not establish a production leaked secret.
- `RegistrationService.cs` — supply appropriate timeout for outbound operations after checking existing cancellation behavior.
- `GitHubService/Program.cs` — consider asynchronous `RunAsync` host lifetime after functional review.
- `GitHubAccessRequestContracts.cs` — review value-type API request binding and validation to guard against under-posting.
- GitHub Ubuntu runner-image migration notice — runner maintenance, not a SonarQube source-code quality-gate failure.

Do not automatically mark these resolved or claim they were fixed in the final analysis. They did not cause the **new-code** quality gate to fail.

## Metric/assessment limits

| Claim | Evidence status |
|---|---|
| Successful .NET build-aware cloud analysis | **Directly proven** by final CE task status and scanner summary |
| 7 genuine coverage XML files | **Directly proven** by extracted nonempty OpenCover XML files |
| Six cloud gate conditions OK | **Directly proven** by final `quality-gate.json` |
| Quality gate passing without small-change exception | **Directly proven**: `ignoredConditions=false` |
| Future CI fails if cloud gate fails | **Conditional**: requires `SONAR_ENFORCE_GATE=true`; actual environment value is not in the artifact |
| ≥80% project-wide coverage | **Not proven** and **not claimed**: measured 60.2% overall |
| All 86 code smells eliminated | **False**: they remain in the final metric |
| Frontend static analysis | **Not part of this specific completed backend artifact** |
| Individual per-suite OpenCover % equals SonarQube aggregated % | **Not claimed**: these have different scopes/calculations |
| Codebase source modifications by this ASE ZIP | **None**: this repo holds evidence/docs, not production backend source changes |

## Evidence provenance

The final `backend-sonarqube-analysis` ZIP is included byte-for-byte in `source-artifacts/04-final-quality-gate-pass.zip`. Historic source artifacts are also preserved byte-for-byte; JSON summaries are extracted into `history/`. SHA-256 checksums are listed in `MANIFEST.md`.

These are **genuine artifacts uploaded from previous GitHub Actions runs**. The HTML overview/CSV comparisons in this repository are derived from the preserved JSON, explicitly labelled as summaries, and do not replace the raw cloud outputs.
