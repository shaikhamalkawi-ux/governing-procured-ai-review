# Governing Procured AI — Public Reproducibility Repository (99aI)

**Research subject:** *Governing Procured AI: Vendor Accountability and Post-Deployment Oversight in the Public Sector*.

This public research checkpoint contains source-auditable, **non-proprietary** decision metadata and code. The study is currently in the **systematic scoping review execution phase**; it is not yet a completed PRISMA-ScR review or a final journal submission. The separate R38 documentary manuscript is a purposive critical review, not a systematic review.

## Latest verified source-screening checkpoint: R43 B05, 8 November 2026

- 2,556 provisional bibliographic identities after conservative reconciliation.
- **404** titles and abstracts inspected at an **AI-assisted, single-pass, provisional** level (**220 R41 + 64 R42 + 120 new R43**); **2,152 remain unread**. These bibliographic identity groups are not an adjudicated eligible-study set.
- A 14-source crosswalk records evidence-stage limits and original source links. These 14 entries **are not** a final included-study set.
- No final include/exclude decisions, independent human double-screening, inter-rater statistic, prevalence estimate, causal contract-remedy effect or completed PRISMA flow is claimed.
- Original Scopus/Web of Science raw files: **22 verified batches; 9 format-pair groups concordant** in private source custody. These licensed files are **not distributed** here.

## Structure

- `data/R41_220_provisional_decisions_PUBLICSAFE.csv`: stable study IDs, first-pass routing categories, and explicit non-final status (no licensed abstracts).
- `data/R41_progress_summary.json`: historical R41 audited counts and gates (unchanged). 
- `data/R42_B04_64_provisional_decisions_PUBLICSAFE.csv` and `data/R42_progress_summary.json`: historical 64-record R42 public-safe delta (unchanged).
- `data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv` and `data/R43_progress_summary.json`: current additional 120 and authoritative R43 first-pass totals.
- `data/R43_Original_Source_Verification_PublicSafe.csv` and `docs/R43_GOVERNANCE_SOURCE_GATES.md`: seven linked primary-source examples, acquisition-role distinctions, and contract/oversight evidence-stage limits.
- `scripts/audit_r43_public.py` and `tests/test_audit_r43_public.py`: public-data-only reproducibility checks including duplicate and false-finality rejection.
- `scripts/audit_r42_direction.py` and `tests/test_audit_r42_direction.py`: no-dependency R42 integrity tests, including a deliberately falsified-inclusion test.
- `docs/R42_SOURCE_DIRECTION_AND_FAMILY_GATES.md`: separate government buying AI from AI helping governments or researchers analyze purchasing.
- `data/R40_14_sources_evidence_chart_PUBLICSAFE.csv`: source-level evidence limitations and public locators.
- `data/documentary/`: five original R29 public-safe documentary registers plus frozen `replay_public_safe.py` reproducing the 28 descriptions and 140 proposition checks (these are NOT independent empirical observations or causal effects).
- `scripts/audit_release.py`: no-dependency public check of IDs, label totals, non-final states and crosswalk.
- `scripts/build_fulltext_queue.py`: portable private-input utility to create a full-text **retrieval** queue without publishing licensed source metadata or deciding eligibility.
- `docs/SCREENING_AND_FAMILY_HOLDS.md`: 34 high-priority records and study-family verification risks.
- `tests/test_audit_release.py`: reproducibility checks including intentional corrupt-data rejection.
- `protocol/PCC2_Boundaries_2026-11-08.md`: population/concept/context and stage/claim guardrails.
- `docs/SCIENTIFIC_LIMITS.md`: strict source, licensing and inference boundaries.
- `manuscript/`: **R41 MDPI documentary main PDF and supplementary PDF**, author-preparation working versions; these are **not peer-reviewed, published or submitted**.

## Run (Python 3.10+, standard library only)

```sh
python scripts/audit_release.py
python scripts/audit_r42_direction.py
python scripts/audit_r43_public.py
python -m unittest discover -s tests -v
python data/documentary/replay_public_safe.py
# Optional, requires your authorized private R41 status CSV:
python scripts/build_fulltext_queue.py --input-private PATH/PRIVATE_STATUS.csv --output-private PATH/FULLTEXT_QUEUE_PRIVATE.csv
```

Passing these tests verifies file consistency; it **cannot validate source semantics or decide eligibility**.

## Citation and data availability

Public repository: https://github.com/shaikhamalkawi-ux/governing-procured-ai-review

A permanent archival DOI and author-approved citation are pending. Please do **not** cite this repository as a peer-reviewed or completed scoping review. The repository URL will appear in *Data and Code Availability* for the documentary manuscript and in later scoping-review versions when scientifically justified.

## Copyright / access policy

Code in `scripts/` and `tests/` is made available under the MIT license specified in `LICENSE-CODE`. Content in `manuscript/` is a public author working draft, with publication/reuse rights reserved pending an author-approved policy. Source bibliographic exports, copyrighted published PDFs and privately held full texts are **not uploaded**. See `docs/SCIENTIFIC_LIMITS.md`.

## R42 reproducible screening safeguard (8 November 2026)

The repository now includes `scripts/validate_independent_screening.py`, `tests/test_validate_independent_screening.py`, and `protocol/INDEPENDENT_SCREENING_AND_ADJUDICATION.md`. The additional checks detect artificial-as-human labels, duplicated reviewers, mismatched evidence stages, disagreement and incomplete record coverage. Execute all tests with `python -m unittest discover -s tests -v`. This is **workflow QA, not human screening**. It was added before the R42 B04 64-record scientific increment; all 404 first-pass judgments remain provisional, and 2,152 records are still unread. No final included-study count or PRISMA chart is asserted.

## R43 scientific interpretation: government buying AI vs AI used in procurement

The new 120-record source-read tranche is deliberately high-priority, not probability-sampled. Its tentative routes are: 5 direct, 17 vendor/identity holds, 28 AI-used-in-procurement, 36 contextual, and 34 out-of-scope. They are **not counts of confirmed eligible/excluded studies**. Original Brazilian CGU evidence describes the Alice tender-monitoring tool as government-developed; vendor procurement must not be inferred simply from public-sector deployment. Case-level procurement contracts, executed oversight clauses, and observed vendor remediation are different evidence types. See `docs/R43_GOVERNANCE_SOURCE_GATES.md` for seven public linked source checks and study-family holds.
