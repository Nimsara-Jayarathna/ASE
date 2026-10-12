# Evidence Repository Structure

The SE3112 submission evidence is separated by assessment contribution rather than mixing unrelated reports into one directory.

```text
evidence/
├── unit/
│   ├── README.md
│   ├── EVIDENCE_INDEX.md
│   ├── MANIFEST.md
│   ├── coverage/
│   │   ├── coverage-summary.md
│   │   ├── coverage-metrics.env
│   │   ├── business/
│   │   └── all-source/
│   └── source-artifacts/
├── load/
│   ├── README.md
│   ├── EVIDENCE_INDEX.md
│   ├── docs/
│   ├── final-runs/
│   └── source-artifacts/
├── mutation/
│   ├── README.md
│   ├── EVIDENCE_INDEX.md
│   ├── MANIFEST.md
│   ├── reports/
│   └── source-artifacts/
└── code-quality/
    ├── README.md
    ├── EVIDENCE_INDEX.md
    ├── MANIFEST.md
    ├── docs/
    ├── reports/                  # offline dashboard + comparison tables
    ├── history/                  # genuine previous-run API evidence
    ├── final-run/                # completed cloud run and 7 OpenCover XMLs
    ├── source-artifacts/         # 4 original, unmodified Actions ZIPs
    └── scripts/                  # offline integrity verification
```

## Convention

Each completed contribution should contain:

1. a concise `README.md` explaining what the evidence proves;
2. an `EVIDENCE_INDEX.md` mapping claims to concrete files;
3. extracted reports that can be opened directly during the viva;
4. the original GitHub Actions artifact ZIP under `source-artifacts/`;
5. a checksum manifest for final evidence integrity where practical.

Unit, Load, Mutation, and Code Quality all now follow this convention. Code Quality includes four unchanged source artifacts and the authentic final cloud quality-gate decision.
