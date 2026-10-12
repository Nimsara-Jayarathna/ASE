# 03 — CI/CD Runbook and Reproduction

## Repositories

- Evidence package: `ASE` — read-only copies of verified GitHub Actions outputs.
- Implementation: `Nimsara-Jayarathna/researchtrack-backend`, `main`.
- SonarQube Cloud project: https://sonarcloud.io/dashboard?id=Nimsara-Jayarathna_researchtrack-backend&branch=main

## Native backend quality gate

Run in `researchtrack-backend` with .NET SDK 10 and NuGet connectivity:

```bash
bash ./scripts/code-quality.sh doctor
bash ./scripts/code-quality.sh setup
bash ./scripts/code-quality.sh check ci
# Optional detailed analyzer evidence:
bash ./scripts/code-quality.sh analyze final-analysis
```

GitHub Actions: **Backend Code Quality** — `.github/workflows/backend-code-quality.yml`. It checks formatting, import rules and eight production builds on pull requests/pushes to `main` and `develop`.

## Cloud static-analysis and coverage gate

In the **backend** repository, the job uses a GitHub Environment named `production` with:

| Item | Storage | Purpose |
|---|---|---|
| `SONAR_TOKEN` | Environment secret | Authenticates API/scanner upload; never commit |
| `SONAR_PROJECT_KEY` | Environment variable | `Nimsara-Jayarathna_researchtrack-backend` |
| `SONAR_ORGANIZATION` | Environment variable | `nimsara-jayarathna` |
| `SONAR_REGION` | Optional environment variable | Leave blank/default for EU |
| `SONAR_ENFORCE_GATE` | Environment variable | `true` to fail the job on a failed cloud gate; confirm current value in GitHub |

Main-branch workflow: **Backend SonarQube Cloud Analysis** — `.github/workflows/backend-sonarqube.yml`. It runs SonarScanner for .NET 11.3.0 and collects **7 OpenCover coverage reports** with the already configured `coverlet.collector`.

### Steps to demonstrate

1. Open GitHub → `researchtrack-backend` → Actions → **Backend SonarQube Cloud Analysis**.
2. Select the successful `main` run associated with analysis ID `a2ec6507-83b5-429d-bb4e-5c8831f70c86` (commit `797b60e` in the supplied log); check the summary states **Compute Engine SUCCESS**, **Quality Gate OK**, **96.7% new-code coverage**.
3. Download the `backend-sonarqube-analysis` artifact; inspect `ce-task.json`, `quality-gate.json`, `measures.json`.
4. Open the SonarQube dashboard for its actual online quality gate and measures.
5. Show the local evidence index in this `ASE` repository and open the seven collected OpenCover XML files.
6. For enforcement behavior, independently confirm `SONAR_ENFORCE_GATE=true` in Environment `production` (no screenshots or secrets of this setting are included here).

## Running the ASE evidence verifier

From the root of this `ASE` repository:

```bash
python3 evidence/code-quality/scripts/verify-evidence.py
```

The verifier checks that the four uploaded original Actions ZIPs match recorded SHA-256 digests and correspond to the extracted JSON; it also checks final cloud conditions and validates all seven extracted OpenCover XMLs. **This offline verifier does not rerun the cloud scanner or the production tests.**

## Avoid misleading demonstrations

- Do not claim that an overall 60.2% coverage rate passes an 80% whole-project requirement: the requirement is **80% coverage on new code**.
- Do not rely solely on a green GitHub job: the cloud quality-gate JSON must also show `OK`.
- Do not claim prior failed gate analyses were caused by .NET compilation failures. Their raw quality-gate JSON explicitly identifies new-code coverage failure.
- Do not erase or rerun other group members' tests/mutation/load workflows in the evidence repository; their finished artifacts are preserved as supplied.
