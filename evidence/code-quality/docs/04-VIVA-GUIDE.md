# 04 — Nimthara: 2-Minute VIVA Demonstration

## Demonstration plan (~120 seconds)

**0:00–0:20 — Problem and objective.** ResearchTrack has eight .NET 10 production projects. The individual SE3112 task was to automate **Static Code Analysis** and expose genuine quality metrics, not merely compile code.

**0:20–0:45 — Two complementary workflows.** In the backend GitHub repository show **Backend Code Quality** (CSharpier 1.3.0 formatting, Roslyn imports/style checks, eight builds) and **Backend SonarQube Cloud Analysis** (build-aware scanner, seven existing unit suites, OpenCover imports).

**0:45–1:15 — Final dashboard.** Show the online SonarQube Quality Gate **OK**: 6/6 conditions pass, 96.7% new-code coverage versus 80% required, 0.0% new-code duplication, three A ratings, 100% hotspots reviewed.

**1:15–1:40 — Actual evidence.** In the ASE repo open `final-run/quality-gate.json` and `final-run/measures.json` or the offline `reports/quality-evolution.html`. Explain why the gate failed at 73.3% and passed after focused AuthService cookie-configuration tests at 96.7%.

**1:40–2:00 — Limitations and proof.** Cite 60.2% overall coverage, 86 code smells, 2.4% overall duplication and the remaining review warnings. Mention that the gate is on **new code**, and that `SONAR_ENFORCE_GATE` must be `true` for CI to reject any future failing cloud gate.

## Likely questions and accurate answers

**Q: What is the difference between CSharpier and SonarQube?**  
A: CSharpier enforces consistent formatting. Roslyn validates selected import/style and compile-time checks. SonarQube Cloud supplies broader static-analysis ratings, complexity/duplication/debt and an independently evaluated quality gate.

**Q: Why use SonarScanner for .NET instead of scanning a ZIP?**  
A: It hooks into the real .NET builds for eight projects and uses the compiled C# analysis context; it imports real test coverage from OpenCover reports.

**Q: Why did the gate fail even when the scanner uploaded successfully?**  
A: The cloud analysis had `new_coverage=0.0%` when no reports were imported; after integration it was `73.3%`, below the 80% new-code threshold. Seven real reports plus targeted AuthService configuration tests raised it to `96.7%`.

**Q: Is 60.2% enough?**  
A: That is the overall source coverage, not the 80% new-code gate. The passing condition is 96.7% **on new code**, while improving overall coverage remains future work.

**Q: Did you fix all code smells?**  
A: No. The final result has 86 overall code smells and 95 minutes of estimated debt; the gate verifies quality of new code. Prioritised existing findings remain visible, which is the honest purpose of continuous quality metrics.

**Q: Is the quality gate enforced in GitHub Actions?**  
A: The script supports `SONAR_ENFORCE_GATE=true`; confirm the actual `production` environment variable before asserting future-failure enforcement. The final cloud `Quality Gate: OK` is directly evidenced in `quality-gate.json`.

## Show these files without network access

1. [`../reports/quality-evolution.html`](../reports/quality-evolution.html)
2. [`../final-run/sonarqube-summary.md`](../final-run/sonarqube-summary.md)
3. [`../final-run/quality-gate.json`](../final-run/quality-gate.json)
4. [`../final-run/coverage-collection-summary.md`](../final-run/coverage-collection-summary.md)
5. [`../MANIFEST.md`](../MANIFEST.md)
