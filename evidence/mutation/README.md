# Mutation Testing — Final Evidence

**Owner:** Pamudi  
**Assessment area:** Mutation Testing  
**GitHub Actions workflow:** Backend Mutation Testing  
**Final run:** `Backend Mutation Testing #4` on `main`  
**Run result:** **Success**  
**Duration:** 1h 21m 33s  
**Source artifact:** `mutation-evidence-all-38123145052-1.zip`

## What this evidence proves

This directory contains the final project-wide Stryker.NET mutation-testing evidence for the selected ResearchTrack backend business logic. The successful `all` run regenerated every included service/subscope in one execution, produced HTML/JSON/Markdown reports, and enforced the final regression gates.

The final project-wide weighted mutation score is **69.99%**, with **1,950 killed**, **836 survived**, **0 timeout**, and **0 no-coverage** mutants in the selected business-logic denominator. Every service-level regression gate and the overall **65.00%** project gate passed.

| Service | Weighted score | Regression floor | Gate | Killed | Survived |
|---|---:|---:|:---:|---:|---:|
| AuthService | 74.34% | 70.00% | **PASS** | 423 | 146 |
| ProjectService | 77.05% | 72.00% | **PASS** | 366 | 109 |
| SubmissionService | 63.26% | 58.00% | **PASS** | 365 | 212 |
| GitHubService | 65.48% | 60.00% | **PASS** | 313 | 165 |
| JiraService | 67.89% | 62.00% | **PASS** | 315 | 149 |
| Gateway | 78.08% | 72.00% | **PASS** | 57 | 16 |
| MeetingService | 74.00% | 68.00% | **PASS** | 111 | 39 |
| **Overall selected business logic** | **69.99%** | **65.00%** | **PASS** | **1,950** | **836** |

## Scope and interpretation

Mutation testing intentionally targets high-value validation, authorization, security, state-transition, workflow, synchronization, and orchestration logic. Controllers, DTO-only contracts, generated code, migrations, and routine persistence/transport plumbing are excluded from the selected mutation denominator.

`Killed` and `Timeout` are detected mutants. `Survived` means the selected tests still passed and the mutant remains for review. `No coverage` means the selected mutation harness did not execute the mutant. `Ignored` and `Compile error` are reported transparently but are not counted as surviving business mutants.

The weighted service and overall scores use actual mutant counts rather than averaging unequal subscope percentages.

## Files to open during the viva

Start with:

- `reports/mutation-summary.md` — primary project-wide summary and regression gates;
- `reports/<service>/<subscope>/reports/*.html` — human-readable Stryker detail;
- `reports/<service>/<subscope>/reports/*.json` — machine-readable mutation evidence;
- `reports/<service>/<subscope>/reports/*.md` — per-scope Markdown summaries;
- `source-artifacts/mutation-evidence-all-38123145052-1.zip` — unchanged original GitHub Actions artifact;
- `MANIFEST.md` — SHA-256 evidence-integrity manifest.

## Regression policy note

The successful Actions run reports `Regression policy: built-in final hardened fallback`. The repository policy file was not present in that checked-out workflow run, so the hardened fallback floors embedded in the final summary tooling were used. This is visible in the run annotations and is not hidden. The important result is that the same final service floors and the **65% overall floor** were enforced, and every gate passed.

## Evidence provenance

The original GitHub Actions artifact is preserved unchanged under `source-artifacts/`. Its SHA-256 is:

`151f61ef8a86d3161e7ef6b016f0fb554f8c38a9683bb823a6efa36eebe3308b`

The extracted artifact contains **85 files**, including the project-wide summary and per-scope HTML/JSON/Markdown reports.
