# Governing Procured AI — Public Reproducibility Repository (99aI)

**Research subject:** *Governing Procured AI: Vendor Accountability and Post-Deployment Oversight in the Public Sector*.

This public research checkpoint contains source-auditable, **non-proprietary** decision metadata and code. The study is currently in the **systematic scoping review execution phase**; it is not yet a completed PRISMA-ScR review or a final journal submission. The separate R38 documentary manuscript is a purposive critical review, not a systematic review.

## Latest verified source-screening checkpoint: R46 — 8 November 2026

- 2,556 provisional bibliographic identities after conservative reconciliation.
- **648** source identities have individually reasoned, non-final title/abstract first-pass assessments (**580 inherited R45 + 68 new R46**); **1,908 still await individual source reading**. All the previous 1,976 unread source abstracts were also parsed using deterministic machine routing, which does NOT mean 1,976 additional individually screened studies. These bibliographic identity groups are not an adjudicated eligible-study set.
- A 14-source crosswalk records evidence-stage limits and original source links. These 14 entries **are not** a final included-study set.
- No final include/exclude decisions, independent human double-screening, inter-rater statistic, prevalence estimate, causal contract-remedy effect or completed PRISMA flow is claimed.
- Original Scopus/Web of Science raw files: **22 verified batches; 9 format-pair groups concordant** in private source custody. These licensed files are **not distributed** here.

## Structure

- `data/R41_220_provisional_decisions_PUBLICSAFE.csv`: stable study IDs, first-pass routing categories, and explicit non-final status (no licensed abstracts).
- `data/R41_progress_summary.json`: historical R41 audited counts and gates (unchanged). 
- `data/R42_B04_64_provisional_decisions_PUBLICSAFE.csv` and `data/R42_progress_summary.json`: historical 64-record R42 public-safe delta (unchanged).
- `data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv` and `data/R43_progress_summary.json`: historical R43 +120 checkpoint (unchanged).
- `data/R44_64_Provisional_RecallStress_PUBLICSAFE.csv`, `data/R44_progress_summary.json` and `data/R44_Three_PublicSource_Gates_PUBLICSAFE.csv`: historical R44 +64 source-safety checkpoint (unchanged).
- `data/R45_112_Provisional_Routes_PUBLICSAFE.csv` and `data/R45_Public_ProgressSummary.json`: historical R45 +112 source-scoped checkpoint; retained unchanged.
- `data/R46_All1976_IDOnly_MachineRoutes_PUBLICSAFE.csv`: diagnostic text-signal routing only, not individual source readings.
- `data/R46_68_SourceReasons_PUBLICSAFE.csv`, `data/R46_ProgressSummary_PublicSafe.json`: 68 new first-pass case-level reasons, current 648/1,908 status.
- `data/R46_100_RetrievalPriority_IDonly_PUBLICSAFE.csv`: retrieval-priority identities, NOT 100 full texts assessed or included studies.
- `data/R46_4_OriginalSource_Verification_PUBLICSAFE.csv` and `data/R46_8_FurtherPublisherBoundaries_PUBLICSAFE.csv`: 12 traceable source-to-claim cards, including original full text vs publisher abstract vs secondary abstract distinctions.
- `data/R46_Seven_Exact_TextIdentity_IDonly_PUBLICSAFE.csv`: hold 7 exact title-and-abstract collision sets (17 original source IDs).
- `scripts/audit_r46_public.py`, `tests/test_audit_r46_public.py`, `docs/R46_METHODS_SOURCE_GATES_AND_APPENDIX.md`: source-count, stage, ID and rights QA.
- `data/R45_13_PublicSource_ClaimBoundaries.csv`: 13 author-summarized source propositions across seven source families, not 13 included independent studies.
- `data/R45_Identity_Holds_IDonly_PUBLICSAFE.csv`: seven exact title/abstract identity groups with 17 distinct bibliographic IDs held rather than auto-merged.
- `scripts/audit_r45_public.py`, `tests/test_audit_r45_public.py`, `docs/R45_SOURCE_EVIDENCE_AND_PRISMA_GATES.md`: public-only integrity tests, deliberate falsification tests and source/claim gates.
- `scripts/audit_r44_public.py`, `tests/test_audit_r44_public.py`, `docs/R44_HEURISTIC_SAFETY_TEST.md`: positive and negative checks of R44 labels, provenance and source uncertainty, with licensed data excluded.
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
python scripts/audit_r44_public.py
python scripts/audit_r45_public.py
python scripts/audit_r46_public.py
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

The repository now includes `scripts/validate_independent_screening.py`, `tests/test_validate_independent_screening.py`, and `protocol/INDEPENDENT_SCREENING_AND_ADJUDICATION.md`. The additional checks detect artificial-as-human labels, duplicated reviewers, mismatched evidence stages, disagreement and incomplete record coverage. Execute all tests with `python -m unittest discover -s tests -v`. This is **workflow QA, not human screening**. It was added before the R42 B04 64-record scientific increment; all 648 case-by-case first-pass judgments remain provisional, and 1,908 records still need individual source reading. No final included-study count or PRISMA chart is asserted.

## R43 scientific interpretation: government buying AI vs AI used in procurement

The new 120-record source-read tranche is deliberately high-priority, not probability-sampled. Its tentative routes are: 5 direct, 17 vendor/identity holds, 28 AI-used-in-procurement, 36 contextual, and 34 out-of-scope. They are **not counts of confirmed eligible/excluded studies**. Original Brazilian CGU evidence describes the Alice tender-monitoring tool as government-developed; vendor procurement must not be inferred simply from public-sector deployment. Case-level procurement contracts, executed oversight clauses, and observed vendor remediation are different evidence types. See `docs/R43_GOVERNANCE_SOURCE_GATES.md` for seven public linked source checks and study-family holds.

## R44 caution about low-signal sources

The prespecified R44 test sampled **32 low- and 32 mid-signal** bibliographic identities before individual AI-assisted title/abstract review. It detected a low-score commercial **spyware** vendor-government-client discussion, but **spyware is not necessarily AI**. The study remains on **HOLD** until evidence establishes AI capability and a specific public buyer/vendor instrument. This test is neither an estimated recall/sensitivity statistic nor a verified missed eligible study. Source-level uncertainty is an essential finding; do not auto-exclude solely because a lexical score is low. See `docs/R44_HEURISTIC_SAFETY_TEST.md`.

## R45 evidence-ladder and screening checkpoint

A new pre-frozen 112-record AI-assisted title/abstract batch used 32 high-ranked, 32 medium hash-selected, 32 low hash-selected and 16 vendor-word enriched identities. All are non-final, and the strata cannot estimate population-level screening sensitivity. The current private fulltext **retrieval** queue has 89 leads (26 direct candidates, 63 evidence-unit/vendor holds); none is a final included study. Source-specific verification now identifies the FAccT 2025 seven-city interview study (19 respondents) as reported qualitative post-award oversight evidence, **not** independent contract-breach or vendor-sanction proof. Normative proposals for supplier accountability remain distinct from signed government contracts and exercised oversight. Seven exact-title-and-abstract identity groups (17 source IDs) are unresolved HOLD cases. See `docs/R45_SOURCE_EVIDENCE_AND_PRISMA_GATES.md`. A private audit workbook and original licensed-index reasons are kept outside this public repository.

## R46 manuscript reading copy and scientific boundary

The original R41 **15-page documentary paper** and **11-page supplementary material** have been assembled without rewriting either source into a **26-page Main with Appendix** PDF: the appendix directly follows the paper with a labelled appendix bookmark. This delivery is separate from the unfinished scoping review and is available alongside the full confidential research package in the project's connected Google Drive. R46 has 12 bounded source cards, including original published evidence on the NHS contracting timeline and U.S. municipal interviews, with full-text/abstract provenance levels kept distinct. The 100-ID retrieval queue does not constitute a full-text eligibility list; no final study count or PRISMA diagram is claimed. See `README_R46.md` and `docs/R46_METHODS_SOURCE_GATES_AND_APPENDIX.md`.
