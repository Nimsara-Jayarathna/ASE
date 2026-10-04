# SE3112 ResearchTrack Microservice Testing Pipeline

## Team Implementation Plan

**Module:** SE3112 - Advanced Software Engineering  
**Assessment:** Take-Home Assessment - Microservice Testing Pipeline  
**Base project:** ResearchTrack (SE3022 CSP Microservice Project)  
**Group size:** 4 students  
**Due date:** 18 October 2026  
**Presentation:** 12 minutes  

### Final individual ownership

| Member | Individual testing area |
|---|---|
| **Sachith** | **Unit Testing & Mocking** |
| **Pamudi** | **Mutation Testing** |
| **Nimsara** | **Load & Performance Testing** |
| **Nimthara** | **Code Quality & Metrics** |

---

# 1. Purpose of This Plan

ResearchTrack already has a strong automated-testing and CI foundation. The goal of the SE3112 assessment is therefore **not to replace the existing frontend/backend test suites or pretend they do not exist**.

The group will use the existing implementation as part of the final testing solution and extend it with the four required individual testing paradigms. The final outcome must look like **one complete testing system**, not four unrelated demonstrations.

The intended assessment story is:

> ResearchTrack already used automated backend and frontend tests as part of normal development. For SE3112, the team strengthened that foundation with deeper unit-test isolation and failure testing, mutation-based test-quality evaluation, controlled load/performance engineering, measurable code-quality metrics, and a unified CI pipeline that runs and reports the complete testing system.

The assessor should therefore see three things clearly:

1. **The existing ResearchTrack testing foundation remains part of the solution.**
2. **Each member has a clear individual contribution that extends that foundation.**
3. **All individual work is finally integrated into one automated CI/testing pipeline with passing evidence.**

---

# 2. Current ResearchTrack Testing Foundation

The supplied backend and frontend already contain substantial automated testing. This is an advantage: the team can spend the assessment effort on **depth, measurement, fault detection, performance behaviour, and quality gates** instead of rebuilding basic testing infrastructure.

## 2.1 Backend foundation already available

The backend currently includes:

- xUnit v3 test projects;
- service-specific backend tests;
- `Microsoft.AspNetCore.Mvc.Testing` / `WebApplicationFactory` usage;
- Coverlet coverage collection;
- real MySQL database-integration testing for tests categorized as `DatabaseIntegration`;
- a shared `ResearchTrack.Testing` support project;
- parameterized xUnit tests using `[Theory]` and `[InlineData]`;
- manually implemented test doubles/stub HTTP handlers in existing areas such as GitHub testing;
- automated backend GitHub Actions CI;
- repository scripts for build/test execution.

The supplied backend contains dedicated test projects for:

- Auth Service;
- API Gateway;
- GitHub Service;
- Jira Service;
- Meeting Service;
- Project Service;
- Submission Service.

The current source inventory contains approximately:

- **55 backend test source files**;
- **255 `[Fact]` / `[Theory]` declarations**;
- **23 `[Theory]` declarations**;
- **83 `[InlineData]` cases**.

These figures are an inventory of the supplied source tree, not a replacement for the final xUnit runtime test count.

## 2.2 Frontend foundation already available

The frontend currently includes:

- Vitest;
- jsdom;
- React Testing Library;
- `@testing-library/jest-dom`;
- `@testing-library/user-event`;
- ESLint;
- Prettier;
- TypeScript type checking;
- Vite production build;
- GitHub Actions CI.

The supplied frontend contains approximately:

- **113 `*.test.*` / `*.spec.*` files**;
- around **460 static `it(...)` / `test(...)` declarations**.

The existing frontend CI command already performs a strong verification sequence similar to:

```text
format check
    -> ESLint
    -> TypeScript typecheck
    -> Vitest
    -> production build
```

This existing suite stays in the final assessment pipeline.

## 2.3 Existing operational visibility

ResearchTrack also already contains Prometheus/Grafana monitoring and metrics around multiple backend behaviours, including areas such as:

- service availability;
- HTTP error behaviour;
- GitHub synchronization/reconciliation;
- Jira webhook outcomes;
- Jira synchronization and queue behaviour;
- API latency/outcomes;
- background-worker/recovery behaviour.

This monitoring is **not itself the Load Testing contribution**. It becomes valuable supporting evidence when Nimsara generates controlled load with k6 and correlates client-side results with server-side behaviour.

---

# 3. What the Team Should Keep Versus Extend

The project already does many things well. The plan is therefore to **keep strong existing work, strengthen meaningful gaps, add missing testing paradigms, and integrate everything**.

| Capability | Existing ResearchTrack state | SE3112 action |
|---|---|---|
| Backend unit tests | Strong existing xUnit suite | Keep all; Sachith strengthens selected high-risk logic |
| Parameterized tests | Already present | Use existing tests and add deeper boundary/business-rule matrices where useful |
| Test doubles | Manual stubs/fakes already exist | Standardize and deepen dependency isolation/failure verification |
| Database integration tests | Real MySQL strategy already present | Keep as part of final backend suite |
| Frontend tests | Large Vitest/RTL suite | Keep in final pipeline |
| Backend coverage | Coverlet collection already present | Convert into visible aggregated metrics/thresholds |
| Frontend coverage | Tests exist but reporting is not standardized | Add measurable coverage reporting |
| Mutation testing | Not currently part of project | Pamudi adds Stryker.NET and test-quality evaluation |
| Performance testing | Not currently standardized | Nimsara adds k6 smoke/load/stress/specialized workloads |
| Code quality dashboard/gate | Existing lint/build checks, no unified metrics layer | Nimthara adds quality metrics and formal quality gate |
| CI | Strong FE/BE CI already exists | Extend into one assessment-level testing pipeline |

The important rule is:

> **Do not rewrite a good existing test merely so that it can be claimed as new work. Extend the existing suite only where the additional test creates assessment value.**

---

# 4. Testing Strategy for ResearchTrack

ResearchTrack should not be presented as a simple CRUD application. Its testing plan should reflect the behaviours that make the system technically interesting:

- multiple backend services;
- API Gateway and service boundaries;
- role-based access control;
- GitHub integration;
- Jira integration;
- external HTTP dependencies;
- webhook/event handling;
- synchronization/reconciliation behaviour;
- background work;
- document submission/versioning flows;
- persistent MySQL data;
- operational metrics;
- concurrent requests.

The four individual testing roles should therefore answer four different engineering questions:

```text
Sachith - Unit Testing & Mocking
"Does important service logic behave correctly in isolation, including boundaries and dependency failures?"

Pamudi - Mutation Testing
"Are those tests strong enough to detect realistic faults when production logic changes incorrectly?"

Nimsara - Load & Performance Testing
"How does the running ResearchTrack system behave as concurrency and event pressure increase?"

Nimthara - Code Quality & Metrics
"Can the team measure and automatically prevent code/test quality from falling below agreed standards?"
```

Together, these become one testing pipeline.

---

# 5. Sachith - Unit Testing & Mocking

## 5.1 Existing implementation Sachith inherits

Sachith does **not** start from an empty test project. The backend already contains:

- xUnit test projects;
- many `[Fact]` tests;
- existing `[Theory]` / `[InlineData]` parameterized tests;
- WebApplicationFactory-based tests;
- real MySQL integration testing;
- manual stubs/fakes/HTTP handlers in some services;
- Coverlet test coverage collection.

Sachith's job is to make the **Unit Testing & Mocking paradigm deeper and more explicit**, especially around high-risk logic that benefits from isolation.

## 5.2 Recommended primary scope

Use **Jira Service** as the main assessment target, because it contains meaningful orchestration and external-dependency behaviour rather than simple CRUD.

Good target behaviours include, where supported by the implementation:

- issue/sprint/workload calculation rules;
- synchronization decisions;
- webhook classification/handling;
- state transitions;
- dependency-failure handling;
- duplicate/ignored event behaviour;
- empty or unusual provider responses;
- authorization/business-rule boundaries.

A secondary scope can include a small number of Submission/Meeting business rules if the Jira test suite already covers a particular area sufficiently.

## 5.3 Required work

### A. Audit existing relevant tests before adding new ones

Create a small test-risk matrix:

| Behaviour | Existing coverage | Missing risk | Action |
|---|---|---|---|
| Example: Jira status mapping | Existing normal cases | Unknown/custom/null state | Add parameterized boundary cases |
| Example: Provider failure | Partial | Timeout / upstream error | Add dependency-failure test double |
| Example: Duplicate webhook | Existing or absent | Duplicate scheduling | Add/strengthen behaviour verification if needed |

The goal is to **extend**, not duplicate.

### B. Add meaningful parameterized tests

Existing `[Theory]` usage already proves the project understands parameterization. Sachith should add parameterized cases only where they improve readability and boundary coverage.

Good patterns:

```text
Input state       Expected mapped state
---------------------------------------
To Do             Planned
In Progress       Active
Done              Completed
Unknown/custom    Safe fallback
Empty/null        Safe failure/fallback
```

or a permission/business-rule matrix:

```text
Role          State            Action          Expected
-------------------------------------------------------
Student       Open             Allowed         true
Student       Closed           Allowed         false
Supervisor    Student-only     Allowed         false
...
```

### C. Strengthen test doubles/mocking

The project already contains manual stubs in places. Sachith should provide a clearer and more deliberate test-double strategy for the selected service.

Use either:

- a dedicated mocking library such as NSubstitute where it improves readability/interaction verification; and/or
- existing manual HTTP handlers/fakes where HTTP behaviour is more naturally simulated that way.

Demonstrate at least:

- successful dependency result;
- empty dependency result;
- dependency exception/timeout/server failure;
- verification that an expected dependency is called;
- verification that an unsafe/unnecessary dependency or persistence operation is **not** called after validation/failure.

### D. Add failure and boundary cases

Prioritize technically meaningful failures, for example:

- upstream Jira failure;
- timeout;
- malformed/unusable data;
- duplicate webhook/event;
- disconnected integration;
- no active sprint/empty dataset;
- synchronization state edge case;
- permission/authorization rejection;
- persistence must not occur after an invalid result.

Do not add artificial cases that the production code cannot actually encounter.

## 5.4 Suggested file ownership

Keep changes mostly in the Jira test project, for example:

```text
tests/ResearchTrack.JiraService.Tests/
  Assessment/
    Synchronization/
    Webhooks/
    Workload/
    Doubles/
```

Do not reorganize the entire existing test project unless necessary.

## 5.5 Sachith deliverables

- strengthened Jira unit-test suite;
- explicit parameterized business/boundary cases;
- clear test-double strategy;
- dependency-failure tests;
- behaviour verification tests;
- short documentation page for Unit Testing & Mocking;
- targeted command that runs the demo tests;
- passing integration with the normal backend test suite.

## 5.6 Definition of done

Sachith's work is complete when:

- all original backend tests still pass;
- new tests are deterministic;
- no live Jira/Atlassian API is required for unit tests;
- at least one meaningful parameterized matrix is demonstrated;
- at least one external/dependency failure is simulated using a test double;
- at least one dependency interaction or non-interaction is verified;
- the tests run automatically in CI;
- the member can clearly explain mock vs stub/fake and unit vs integration testing.

---

# 6. Pamudi - Mutation Testing

## 6.1 Existing implementation Pamudi inherits

Pamudi benefits from the already substantial backend unit-test suite. Mutation testing should **evaluate that existing test investment rather than create a disconnected demonstration**.

The ideal relationship is:

```text
Existing + strengthened unit tests
        |
        v
Stryker mutates production logic
        |
        +--> mutant killed -> test successfully detects the fault
        |
        +--> mutant survives -> test weakness discovered
                                |
                                v
                           improve test
                                |
                                v
                         mutant becomes killed
```

## 6.2 Primary tool

Use **Stryker.NET**.

## 6.3 Recommended primary mutation scope

Use a **focused, high-value part of GitHub Service** or another business-logic area that already has strong tests and does not overlap heavily with Sachith's Jira files.

Potential targets, depending on actual Stryker runtime/results:

- repository URL parsing/validation;
- synchronization decisions;
- webhook signature/ingress logic;
- queue/rule logic;
- installation/repository selection logic;
- option/boundary validation;
- other compact business logic with meaningful branches.

Do **not** mutate the whole backend blindly.

Exclude low-value areas when justified:

- migrations;
- generated code;
- `Program.cs` wiring;
- simple DTO properties;
- pure configuration boilerplate;
- code where mutation results would add no useful assessment insight.

## 6.4 Required work

### A. Configure Stryker reproducibly

Add configuration so the mutation run can be started with one documented command.

Configuration should control:

- production mutation target;
- test project;
- ignored/low-value files if needed;
- report output;
- final threshold after the baseline is known.

### B. Run the first mutation analysis

Record real values for:

- total mutants;
- killed mutants;
- survived mutants;
- no-coverage mutants;
- timeout mutants if any;
- mutation score.

### C. Investigate meaningful survivors

Select at least 2-3 meaningful survivors and explain what they reveal about the tests.

Typical mutation examples include:

```text
>  -> >=
== -> !=
true -> false
+ -> -
&& -> ||
condition removed
return value changed
```

### D. Improve tests rather than gaming the score

For each selected survivor:

1. explain why the existing tests allowed it to survive;
2. add/strengthen a meaningful assertion/case;
3. rerun the relevant mutation scope;
4. show that the mutant is now killed where practical.

The strongest evidence is a **before/after mutation report**.

### E. Add a mutation quality threshold

Do not choose a threshold before seeing the real baseline.

Process:

1. run baseline;
2. refine meaningful scope;
3. improve tests;
4. observe stable final score;
5. choose a defensible threshold slightly below the stable achieved score so future regression fails.

## 6.5 Pamudi deliverables

- Stryker.NET configuration;
- focused mutation scope;
- baseline mutation report;
- analysis of meaningful surviving mutants;
- strengthened tests based on survivor findings;
- final mutation report;
- mutation threshold/gate;
- short Mutation Testing documentation;
- CI artifact/report output.

## 6.6 Definition of done

Pamudi's work is complete when:

- Stryker runs through one documented command;
- the mutation scope is technically justified;
- at least one meaningful surviving mutant is explained;
- at least one real test is improved because of a surviving mutant;
- before/after mutation evidence is retained;
- final mutation score is reported;
- threshold failure is automated;
- existing backend tests remain passing.

---

# 7. Nimsara - Load & Performance Testing

## 7.1 Existing implementation Nimsara inherits

ResearchTrack already has:

- running microservices;
- gateway-accessed APIs;
- Jira/GitHub integration behaviour;
- webhook-related processing;
- Prometheus/Grafana monitoring;
- operational metrics that can help explain server-side behaviour.

What is missing is a **controlled, repeatable load/performance test suite with measurable thresholds and CI evidence**.

Nimsara's work should therefore test the **real ResearchTrack architecture**, not a toy endpoint.

## 7.2 Primary tool

Use **k6**.

## 7.3 Recommended structure

```text
tests/performance/
  README.md
  config/
    environment.example.json
  lib/
    auth.js
    checks.js
    endpoints.js
  scenarios/
    smoke.js
    normal-load.js
    stress.js
    jira-webhook-burst.js
  results/        # generated/ignored locally; CI artifacts preferred
```

## 7.4 Environment rules

- Never run destructive stress tests against production.
- Use a controlled test/local/deployed assessment environment.
- Do not commit secrets or access tokens.
- Performance scripts should target ResearchTrack, not intentionally overload GitHub/Atlassian infrastructure.
- Where a ResearchTrack endpoint would indirectly hit an external provider, prefer cached/stored/local-snapshot paths or a controlled test setup so results primarily measure ResearchTrack.

## 7.5 Required scenario 1 - Smoke performance test

Purpose: verify environment, authentication, script correctness and essential checks.

Starting shape:

```text
1-2 virtual users
10-20 seconds
```

Candidate checks:

- expected HTTP status;
- response contains expected structure/state;
- no unexpected errors;
- latency threshold.

This is the safest performance stage to integrate into frequent CI if the environment is stable.

## 7.6 Required scenario 2 - Normal load

Model realistic concurrent ResearchTrack use.

Candidate targets:

- project overview/dashboard reads;
- stored Jira issue/sprint/workload reads;
- stored GitHub activity reads;
- submission-history reads;
- other stable gateway endpoints representative of normal users.

Suggested first calibration profile:

```text
5 -> 15 -> 30 VUs
```

Do not treat this profile as final until real measurements are collected.

## 7.7 Required scenario 3 - Stress test

Purpose: discover the point at which quality begins to degrade, not merely prove an arbitrary user count.

Suggested progressive calibration:

```text
10 -> 25 -> 50 -> 75 -> 100 VUs
```

Observe:

- p95/p99 latency growth;
- error-rate change;
- throughput plateau;
- gateway/service pressure;
- database/service bottlenecks;
- recovery after load drops.

A stress-test result can be successful even if the system eventually degrades, because discovering the degradation boundary is the purpose of the test.

## 7.8 Required scenario 4 - ResearchTrack-specific Jira webhook burst

This should be Nimsara's distinctive scenario.

Generate a controlled burst of Jira webhook requests against the ResearchTrack test environment.

Measure, where observable:

- accepted requests;
- failed requests;
- ingress latency;
- duplicate/coalesced behaviour;
- queue/synchronization pressure;
- recovery after the burst;
- server-side error behaviour.

The purpose is to test a characteristic of ResearchTrack that a simple CRUD application would not have.

## 7.9 Required metrics

At minimum report:

- VUs/concurrency;
- total requests;
- requests/second;
- check success rate;
- failed request rate;
- p50;
- p90;
- p95;
- p99.

Nimsara must be able to explain why tail latency (p95/p99) is usually more useful than only showing an average.

## 7.10 Threshold strategy

Do not invent a visually attractive SLA before measurement.

Use this process:

1. run smoke and normal-load baselines;
2. record stable values;
3. define realistic assessment-environment thresholds;
4. configure k6 to fail automatically when those thresholds are violated.

Conceptual example only:

```javascript
thresholds: {
  http_req_failed: ['rate<0.01'],
  http_req_duration: ['p(95)<500'],
}
```

Final numbers must come from actual project measurements.

## 7.11 Prometheus/Grafana correlation

Where reliable, correlate k6 output with the monitoring ResearchTrack already has.

Example:

```text
k6 observation              Server-side observation
----------------------------------------------------
p95 rises                    service latency rises
error rate increases         HTTP 5xx metrics increase
webhook burst grows          queue depth / webhook metrics change
throughput plateaus          resource/service bottleneck appears
```

Grafana is supporting evidence, not a substitute for the k6 test itself.

## 7.12 Nimsara deliverables

- reusable k6 test structure;
- smoke test;
- normal-load test;
- stress test;
- Jira webhook-burst test;
- documented environment/configuration approach;
- calibrated thresholds;
- machine-readable results for CI;
- human-readable result summary;
- optional Grafana screenshots/panels showing meaningful correlation;
- Performance Testing documentation.

## 7.13 Definition of done

Nimsara's work is complete when:

- scripts run through documented commands;
- no secrets are committed;
- tests use a controlled non-production environment;
- checks verify functional correctness as well as status codes;
- smoke testing is stable and repeatable;
- normal/stress runs report p95 and failure rate;
- at least one performance threshold can fail automatically;
- webhook-burst testing demonstrates a ResearchTrack-specific workload;
- final evidence is retained for CI/demo;
- the system returns to normal after the test workload.

---

# 8. Nimthara - Code Quality & Metrics

## 8.1 Existing implementation Nimthara inherits

ResearchTrack already has useful quality checks:

- backend build/test automation;
- frontend Vitest tests;
- ESLint;
- Prettier;
- TypeScript type checking;
- production frontend build;
- Coverlet backend coverage collection;
- GitHub Actions CI.

Nimthara's task is **not to claim these existing checks as new**. The contribution is to convert them into a **measurable quality system with coverage reporting, static-analysis metrics, explicit thresholds and a visible quality gate**.

## 8.2 Primary tools

Recommended combination:

- SonarQube or SonarCloud for the quality dashboard/gate;
- existing Coverlet for backend coverage;
- Vitest coverage provider/reporting for frontend coverage;
- existing ESLint;
- existing Prettier;
- existing TypeScript checking;
- existing .NET build/format/analyzer checks.

Choose SonarQube vs SonarCloud based on whichever can be made most reliable for the assessment environment.

## 8.3 Required work

### A. Standardize backend coverage

The backend already collects coverage. Convert it into useful evidence:

- stable output directory;
- merged/aggregated report if required;
- machine-readable Cobertura/XML;
- human-readable HTML/summary;
- documented coverage command;
- final threshold policy.

### B. Add frontend coverage reporting

The frontend has many tests but coverage reporting is not currently standardized.

Add a command conceptually similar to:

```bash
npm run test:coverage
```

Produce:

- line coverage;
- branch coverage;
- function coverage where supported;
- human-readable report;
- machine-readable output for the quality platform/CI.

### C. Add static-analysis metrics

Use Sonar or the selected analysis platform to expose meaningful metrics such as:

- bugs;
- vulnerabilities/security findings supported by the tool;
- code smells;
- duplication;
- maintainability/technical-debt indicators;
- coverage;
- quality-gate state.

### D. Define a defensible quality gate

The final gate can combine:

```text
Build succeeds
Backend tests pass
Frontend tests pass
No ESLint errors
No TypeScript errors
Formatting checks pass
Coverage >= agreed threshold
No new blocker/critical quality issues
Duplication <= agreed threshold
Sonar quality gate = PASS
```

Do not set arbitrary numbers before collecting the baseline.

### E. Use metrics to improve real code

Select 2-3 genuine findings from the first analysis and improve them.

Good examples:

- duplicated logic;
- unnecessarily complex method;
- dead/unreachable code;
- null-safety problem;
- maintainability smell;
- important branch with weak coverage.

Then show the before/after quality change.

## 8.4 Nimthara deliverables

- SonarQube/SonarCloud configuration;
- backend coverage reporting;
- frontend coverage reporting;
- documented quality metrics;
- agreed quality thresholds;
- quality-gate configuration;
- 2-3 genuine improvements based on measured findings;
- before/after evidence;
- CI integration;
- Code Quality & Metrics documentation.

## 8.5 Definition of done

Nimthara's work is complete when:

- backend and frontend metrics are visible;
- coverage is shown as understandable percentages rather than only raw files;
- the quality gate has explicit pass/fail criteria;
- at least two real findings are explained;
- quality metrics are not fabricated/manually edited;
- CI publishes or links the result;
- existing FE/BE checks remain passing;
- the member can clearly explain coverage vs test quality, static analysis, code smells and technical debt.

---

# 9. Individual Work Separation

The work should be divided so members can work in parallel with minimal conflicts.

| Member | Primary ownership | Main files/areas |
|---|---|---|
| **Sachith** | Unit Testing & Mocking | Jira test project and related test helpers/docs |
| **Pamudi** | Mutation Testing | Stryker config, focused GitHub mutation target, selected test improvements/docs |
| **Nimsara** | Load & Performance Testing | New performance-test tree, k6 scripts/config/docs |
| **Nimthara** | Code Quality & Metrics | coverage configs, Sonar config, quality scripts/docs |

Recommended branches:

```text
feature/SE3112-unit-mocking-sachith
feature/SE3112-mutation-testing-pamudi
feature/SE3112-performance-testing-nimsara
feature/SE3112-code-quality-nimthara
```

A final shared integration branch can be used if it fits the team's normal workflow:

```text
feature/SE3112-testing-pipeline
```

## Shared-file rule

Do **not** have all four members edit the same GitHub Actions workflow simultaneously.

Each member should first make their tool work with one local/documented command. After the four individual work packages are stable, perform one planned group CI-integration session.

---

# 10. Shared Group Work - Final CI/Test Automation Pipeline

This is the most important shared part of the assessment.

The group requirement is not met merely because four tools exist. The final system must show that the testing layers can be **executed systematically** and their results are visible together.

## 10.1 Preserve existing CI

Do not replace the mature backend/frontend CI. Extend it.

The existing checks continue to run as part of the final system.

## 10.2 Fast pull-request pipeline

Every PR should run the fast and deterministic checks.

### Backend fast gates

```text
restore
build
existing infrastructure/config validations
existing backend unit/integration-safe tests
Sachith's strengthened unit/mocking tests
coverage collection
fast quality/static-analysis checks
```

### Frontend fast gates

```text
npm ci
Prettier check
ESLint
TypeScript typecheck
existing Vitest suite
frontend coverage
production build
```

### Optional fast performance gate

If the CI/test environment is sufficiently stable, run Nimsara's short **k6 smoke profile** as a fast performance gate.

If CI networking/environment makes it unreliable, keep the smoke run in the assessment/release workflow rather than creating flaky PR CI.

## 10.3 Heavy assurance pipeline

Run expensive checks through `workflow_dispatch`, scheduled CI, and/or the release-preparation workflow.

Heavy assurance includes:

- Pamudi's mutation suite;
- Nimsara's normal-load suite;
- Nimsara's stress suite;
- Nimsara's webhook-burst suite;
- optional deeper quality analysis.

Why this matters:

> Mutation testing repeatedly modifies production code and reruns tests. Stress testing intentionally consumes system resources. Running these at full intensity on every small commit would slow feedback and reduce CI reliability. They remain fully automated but run at an appropriate stage.

This is a strong VIVA/architecture decision.

---

# 11. Final Pipeline Architecture

```text
                           CODE CHANGE / PR
                                  |
                                  v
                  +-------------------------------+
                  | EXISTING + FAST QUALITY GATES |
                  |-------------------------------|
                  | Backend restore/build         |
                  | Frontend build                |
                  | Prettier                      |
                  | ESLint                        |
                  | TypeScript                    |
                  | Existing FE tests             |
                  | Existing BE tests             |
                  +---------------+---------------+
                                  |
                                  v
                  +-------------------------------+
                  | SACHITH                       |
                  | Unit Testing & Mocking        |
                  | parameterized + failure tests |
                  +---------------+---------------+
                                  |
                                  v
                  +-------------------------------+
                  | NIMTHARA                      |
                  | Coverage + Quality Metrics    |
                  | Static analysis + quality gate|
                  +---------------+---------------+
                                  |
                       FAST PIPELINE RESULT
                                  |
                +-----------------+-----------------+
                |                                   |
                v                                   v
    +---------------------------+       +---------------------------+
    | PAMUDI                    |       | NIMSARA                   |
    | Mutation Testing          |       | Load & Performance        |
    | scheduled/manual/release  |       | scheduled/manual/release  |
    +-------------+-------------+       +-------------+-------------+
                  |                                   |
                  +-----------------+-----------------+
                                    |
                                    v
                     +-----------------------------+
                     | UNIFIED TESTING EVIDENCE    |
                     |-----------------------------|
                     | Test results                |
                     | Coverage                    |
                     | Mutation score/report       |
                     | Quality metrics/gate        |
                     | k6 results/thresholds       |
                     | Final CI status             |
                     +-----------------------------+
```

---

# 12. Standard Commands

The final solution should make each testing paradigm easy to execute.

Suggested command contract (final names can follow the repository's existing script style):

## Backend

```bash
./scripts/test.sh all
./scripts/test.sh integration
./scripts/se3112-unit.sh
./scripts/se3112-mutation.sh
./scripts/se3112-quality.sh
```

## Frontend

```bash
npm run ci
npm run test:coverage
npm run quality
```

## Performance

```bash
./scripts/se3112-performance-smoke.sh
./scripts/se3112-performance-load.sh
./scripts/se3112-performance-stress.sh
./scripts/se3112-performance-webhook.sh
```

The wrapper scripts should call the real underlying tools rather than duplicating logic.

---

# 13. Unified CI Evidence

The final GitHub Actions execution should make the result understandable without opening dozens of logs.

Create a job summary similar to:

```text
RESEARCHTRACK - SE3112 AUTOMATED TESTING SUMMARY

Build & Baseline
Backend build                     PASS
Frontend format/lint/typecheck    PASS
Frontend build                    PASS

Automated Tests
Backend existing tests            PASS
Frontend existing tests           PASS
Sachith unit/mocking suite         PASS

Coverage & Quality
Backend coverage                  XX.X%
Frontend coverage                 XX.X%
Static quality gate               PASS

Mutation - Pamudi
Mutation score                    XX.X%
Mutation threshold                PASS

Performance - Nimsara
Smoke p95                         XXX ms
Smoke failure rate                X.XX%
Smoke thresholds                  PASS
Latest load/stress workflow       PASS

OVERALL SE3112 TESTING STATUS      PASS
```

All percentages and latency values must come from the actual run.

## Recommended CI artifacts

```text
backend-test-results
frontend-test-results
backend-coverage-report
frontend-coverage-report
mutation-report
quality-report
k6-smoke-results
k6-load-results
k6-stress-results
k6-webhook-results
```

Generated reports should normally be uploaded as CI artifacts rather than committed permanently to source control.

---

# 14. Evidence Matrix

Create a final `docs/testing/TEST-EVIDENCE-MATRIX.md` that connects system risk to the responsible test type.

| ResearchTrack risk / behaviour | Testing approach | Owner | Evidence |
|---|---|---|---|
| Jira dependency fails | Unit test + test double | Sachith | xUnit result |
| Jira state/business boundaries | Parameterized unit tests | Sachith | xUnit result |
| Duplicate/invalid event must not cause incorrect work | Unit/mock behaviour test | Sachith | xUnit result |
| Unit tests might execute code but miss faults | Mutation testing | Pamudi | Stryker report |
| Important business-rule mutant survives | Mutation-guided test improvement | Pamudi | before/after Stryker result |
| Normal concurrent reads become slow | Load testing | Nimsara | k6 normal-load report |
| System degrades under increasing pressure | Stress testing | Nimsara | k6 stress report |
| Jira webhook ingress receives a burst | Specialized performance test | Nimsara | k6 + optional Grafana evidence |
| Backend/frontend coverage regresses | Coverage gate | Nimthara | coverage report + CI |
| Static quality problems increase | Static analysis/quality gate | Nimthara | Sonar/quality report |
| Existing FE quality regresses | Existing Vitest/ESLint/TypeScript | Group + Nimthara | CI output |
| Existing BE regression occurs | Existing xUnit/integration suite | Group + Sachith | CI output |

---

# 15. Recommended Implementation Order

## Stage 1 - Individual foundations

### Sachith

1. Audit Jira tests.
2. Identify high-value missing failure/boundary cases.
3. Select mocking/test-double approach.
4. Add parameterized matrices.
5. Add dependency failure/interaction tests.
6. Ensure existing backend tests remain passing.

### Pamudi

1. Add Stryker.NET configuration.
2. Select focused mutation scope.
3. Run first baseline mutation report.
4. Identify meaningful survivors.
5. Add/strengthen tests to kill selected survivors.
6. Establish final mutation threshold.

### Nimsara

1. Add k6 structure/config.
2. Implement smoke test.
3. Establish safe test environment.
4. Add normal-load profile.
5. Add stress profile.
6. Add Jira webhook-burst profile.
7. Calibrate thresholds from real measurements.
8. Collect optional server-side monitoring evidence.

### Nimthara

1. Standardize backend coverage output.
2. Add frontend coverage output.
3. Configure Sonar/selected quality platform.
4. Capture first metrics.
5. Define quality gate after baseline measurement.
6. Fix 2-3 real quality findings.
7. Capture final before/after metrics.

## Stage 2 - Individual review

Before integration, every member must provide:

- one documented command;
- passing local result;
- expected inputs/environment variables;
- generated report location;
- CI requirements;
- demo evidence;
- short explanation of what was already present and what they added/strengthened.

## Stage 3 - Shared integration

1. Merge stable individual branches.
2. Run all existing backend tests.
3. Run all existing frontend tests.
4. Resolve test/config conflicts.
5. Extend GitHub Actions.
6. Add fast vs heavy workflows.
7. Upload reports as artifacts.
8. Add unified GitHub Actions summary.
9. Run the full testing system several times.
10. Fix any flaky or environment-dependent behaviour.

## Stage 4 - Final assessment evidence

1. Save a final successful CI run.
2. Save final mutation report.
3. Save final quality report/dashboard.
4. Save final load/stress results.
5. Save targeted unit/mocking result.
6. Produce final testing README/evidence matrix.
7. Prepare five slides/one-page architecture PDF.
8. Rehearse four 2-minute individual demos.
9. Prepare VIVA questions for each member.

---

# 16. Suggested Timeline

## 04-07 October - Individual setup and first measurements

- Sachith: test-gap audit + first strengthened unit/mocking tests.
- Pamudi: Stryker configuration + first mutation baseline.
- Nimsara: k6 smoke + first normal-load baseline.
- Nimthara: coverage configuration + first quality analysis.

## 08-11 October - Implementation depth

- Sachith: complete boundary/failure/interaction suite.
- Pamudi: investigate survivors + improve tests + rerun mutation.
- Nimsara: load/stress/webhook-burst + threshold calibration.
- Nimthara: quality improvements + final gate definition.

## 12-14 October - CI integration

- merge stable work;
- extend workflows;
- create artifacts and summaries;
- run complete pipeline repeatedly;
- eliminate flaky tests.

## 15-16 October - Documentation and presentation

- final README/testing guide;
- evidence matrix;
- screenshots/reports;
- maximum five slides or architecture PDF;
- VIVA preparation.

## 17 October - Submission freeze

- no unnecessary new features;
- only critical testing/demo fixes;
- execute final clean CI;
- retain all reports;
- validate each demo command from a clean environment.

## 18 October - Submission

Submit the project, tests, configurations and documentation before the deadline.

---

# 17. 12-Minute Demo Plan

## 0:00-2:00 - Group introduction and automation

Show:

- concise ResearchTrack microservice architecture;
- existing FE/BE automated testing foundation;
- final unified GitHub Actions pipeline;
- explanation of fast PR checks vs heavy assurance workflows.

Key message:

> All four individual testing contributions extend the existing ResearchTrack test foundation and are integrated into a common automated CI/testing process.

## 2:00-4:00 - Sachith: Unit Testing & Mocking

Show:

1. one meaningful parameterized test matrix;
2. one mocked/stubbed dependency failure;
3. one interaction/non-interaction verification;
4. targeted xUnit run passing.

Explain isolation, determinism and why a live Jira API is not needed.

## 4:00-6:00 - Pamudi: Mutation Testing

Show:

1. Stryker report;
2. one meaningful surviving mutant from the first run;
3. strengthened test;
4. mutant killed/final score;
5. mutation threshold result.

Explain why coverage alone cannot prove test effectiveness.

## 6:00-8:00 - Nimsara: Load & Performance Testing

Show:

1. short k6 smoke/normal run;
2. p95;
3. request throughput;
4. failure rate;
5. threshold result;
6. previously captured stress/webhook-burst evidence;
7. optional Grafana correlation if reliable.

Explain the difference between normal load and stress testing.

## 8:00-10:00 - Nimthara: Code Quality & Metrics

Show:

1. backend/frontend coverage;
2. quality dashboard;
3. selected metrics such as smells/duplication/technical debt;
4. quality-gate status;
5. one real before/after improvement.

Explain why the gate protects against regression.

## 10:00-12:00 - VIVA

Stop introducing new features and answer directly from the implementation.

---

# 18. Five-Slide Structure

## Slide 1 - ResearchTrack and testing risks

Show architecture and emphasize:

- microservices;
- external GitHub/Jira dependencies;
- webhooks/synchronization;
- database;
- concurrent use;
- role boundaries.

## Slide 2 - Complete automated testing architecture

Show:

```text
Existing FE/BE tests
       +
Unit/Mocking
       +
Mutation
       +
Performance
       +
Quality Metrics
       -> CI quality pipeline
```

## Slide 3 - Sachith + Pamudi

Show concise evidence:

- parameterized/mocked test;
- mutation survivor -> improved test -> killed mutant;
- actual final test/mutation metrics.

## Slide 4 - Nimsara + Nimthara

Show:

- k6 p95/failure/throughput result;
- webhook-burst/stress result;
- coverage;
- code-quality dashboard/gate.

## Slide 5 - Final integrated result

Show actual values from final CI:

```text
Backend tests       PASS
Frontend tests      PASS
Coverage            XX%
Mutation score      XX%
Performance gate    PASS
Quality gate        PASS
Overall pipeline    PASS
```

Also show the four member names and ownership.

---

# 19. Member-Specific VIVA Preparation

## Sachith - Unit Testing & Mocking

Must be ready for:

- mock vs stub vs fake;
- why parameterized testing is useful;
- behaviour verification vs state verification;
- why external APIs should be isolated in unit tests;
- what should not be mocked;
- unit vs integration test;
- deterministic testing;
- boundary and negative testing.

## Pamudi - Mutation Testing

Must be ready for:

- what a mutant is;
- killed vs survived mutant;
- no-coverage mutant;
- equivalent mutant;
- mutation score;
- why high coverage can still have weak assertions;
- why mutation testing is expensive;
- why scope is limited;
- why mutation does not run fully on every PR.

## Nimsara - Load & Performance Testing

Must be ready for:

- load vs stress vs spike testing;
- VUs/concurrency vs requests per second;
- p95/p99 vs average;
- throughput;
- failure rate;
- saturation/bottleneck;
- threshold design;
- why the team should not stress GitHub/Jira provider APIs directly;
- how monitoring correlates with generated load.

## Nimthara - Code Quality & Metrics

Must be ready for:

- line vs branch coverage;
- coverage vs test effectiveness;
- static vs dynamic analysis;
- code smell vs bug;
- duplication;
- maintainability/technical debt;
- false positive;
- quality gate;
- why arbitrary high coverage goals can be misleading.

---

# 20. Final Definition of Done for the Group

The assessment implementation is considered complete only when all of the following are true.

## Existing system remains healthy

- existing backend tests pass;
- existing frontend tests pass;
- backend build passes;
- frontend build passes;
- ESLint/Prettier/TypeScript checks pass;
- existing integration testing remains functional.

## Sachith

- strengthened unit/mocking tests pass;
- meaningful parameterization is visible;
- dependency-failure simulation is visible;
- interaction/non-interaction verification is visible.

## Pamudi

- Stryker report exists;
- meaningful survivor analysis exists;
- tests were strengthened from mutation feedback;
- final mutation threshold passes.

## Nimsara

- smoke profile passes;
- normal-load result exists;
- stress result exists;
- Jira webhook-burst result exists;
- p95/failure/throughput metrics exist;
- performance threshold result is automated.

## Nimthara

- backend coverage is visible;
- frontend coverage is visible;
- static-analysis metrics are visible;
- quality gate is automated;
- before/after quality improvement evidence exists.

## Group automation

- fast CI is stable;
- heavy assurance workflow is automated;
- important reports are uploaded/preserved;
- GitHub Actions contains a readable summary;
- all member work is documented;
- final CI/testing result is **PASS**;
- no demo depends on undocumented manual steps.

---

# 21. Final Team Message for the Assessment

The group should consistently explain the solution using this idea:

> ResearchTrack already had a strong automated backend/frontend test foundation. We retained that engineering work and extended it into a complete SE3112 microservice testing pipeline. Sachith strengthened isolated unit testing with parameterized cases, test doubles and failure-path verification. Pamudi evaluated and improved test effectiveness using mutation testing. Nimsara measured system behaviour under realistic concurrency, stress and webhook bursts using k6 with thresholds and operational evidence. Nimthara converted existing checks and coverage into measurable code-quality indicators and enforceable quality gates. All of these layers are integrated through CI so the final project can be evaluated as one repeatable automated testing system.

That is the implementation direction the team should follow.
