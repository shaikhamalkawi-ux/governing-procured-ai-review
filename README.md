# Governing Procured AI — Public Reproducibility Repository (99aI)

**Research subject:** *Governing Procured AI: Vendor Accountability and Post-Deployment Oversight in the Public Sector*.

This public research checkpoint contains source-auditable, **non-proprietary** decision metadata and code. The study is currently in the **systematic scoping review execution phase**; it is not yet a completed PRISMA-ScR review or a final journal submission. The separate R38 documentary manuscript is a purposive critical review, not a systematic review.

## Latest verified checkpoint: R41, 8 November 2026

- 2,556 provisional bibliographic identities after conservative reconciliation.
- 220 titles and abstracts inspected at an **AI-assisted, single-pass, provisional** level; **2,336 remain unread**.
- A 14-source crosswalk records evidence-stage limits and original source links. These 14 entries **are not** a final included-study set.
- No final include/exclude decisions, independent human double-screening, inter-rater statistic, prevalence estimate, causal contract-remedy effect or completed PRISMA flow is claimed.
- Original Scopus/Web of Science raw files: **22 verified batches; 9 format-pair groups concordant** in private source custody. These licensed files are **not distributed** here.

## Structure

- `data/R41_220_provisional_decisions_PUBLICSAFE.csv`: stable study IDs, first-pass routing categories, and explicit non-final status (no licensed abstracts).
- `data/R41_progress_summary.json`: authoritative audited counts and gates.
- `data/R40_14_sources_evidence_chart_PUBLICSAFE.csv`: source-level evidence limitations and public locators.
- `data/documentary/`: five original R29 public-safe documentary registers plus frozen `replay_public_safe.py` reproducing the 28 descriptions and 140 proposition checks (these are NOT independent empirical observations or causal effects).
- `scripts/audit_release.py`: no-dependency public check of IDs, label totals, non-final states and crosswalk.
- `tests/test_audit_release.py`: reproducibility checks including intentional corrupt-data rejection.
- `protocol/PCC2_Boundaries_2026-11-08.md`: population/concept/context and stage/claim guardrails.
- `docs/SCIENTIFIC_LIMITS.md`: strict source, licensing and inference boundaries.
- `manuscript/`: author-preparation PDF copies (once deposited); these are **not peer-reviewed or submitted**.

## Run (Python 3.10+, standard library only)

```sh
python scripts/audit_release.py
python -m unittest discover -s tests -v
python data/documentary/replay_public_safe.py
```

Passing these tests verifies file consistency; it **cannot validate source semantics or decide eligibility**.

## Citation and data availability

Public repository: https://github.com/shaikhamalkawi-ux/governing-procured-ai-review

A permanent archival DOI and author-approved citation are pending. Please do **not** cite this repository as a peer-reviewed or completed scoping review. The repository URL will appear in *Data and Code Availability* for the documentary manuscript and in later scoping-review versions when scientifically justified.

## Copyright / access policy

Code in `scripts/` and `tests/` is made available under the MIT license specified in `LICENSE-CODE`. Content in `manuscript/` is a public author working draft, with publication/reuse rights reserved pending an author-approved policy. Source bibliographic exports, copyrighted published PDFs and privately held full texts are **not uploaded**. See `docs/SCIENTIFIC_LIMITS.md`.
