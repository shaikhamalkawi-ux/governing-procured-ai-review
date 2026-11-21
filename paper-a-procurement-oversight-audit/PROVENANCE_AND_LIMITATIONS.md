# Data provenance, scope and limitations — Paper A

**Release:** 2026-11-22, public-safe author dataset for **99aiA Paper A**, source-derived from the R76 cumulative evidence addendum and frozen R29 documentary ledger. This release is **not** a verified executed-contract dataset and **not** a nationally representative AI procurement sample.

## What is present

- `data/local_authority_13_derived_R76.csv`: 13 UK ATRS local-authority disclosure entries, selected in the retained 15 November 2026 directory snapshot. Derived/transcribed from the original R76 indexed addendum, **not** byte-for-byte original R65 machine data. Source URLs and evidence limits preserved. Counts: 12 third-party yes, 7 broad procurement-connected, 2 explicitly direct commercial AI use/AI-specific term descriptions. The last categories are source questions, not an inferred general contract-prevalence hierarchy.
- `data/ministerial_20_derived_R76.csv`: a separate first-20 ministerial ATRS directory cohort; 14 outside-party declared yes, 6 no; technology source codes 13 AI/ML, 3 explicit no AI/ML, 4 unresolved. 10 commissioned development, 3 direct tool/component-access descriptions, 1 in-house model with external components among the 14 yes. The preserved **original access flag** marks one DfE entry as indexed official excerpt at the historical source-read stage, despite later official-page rechecks.
- Existing frozen `../data/documentary/R29_28Event_CXSM_A_SourceLedger.csv`: 28 **descriptions nested in nine programmes**, not 28 independent contracts, 140 linked propositions in the established historical source. The two oversight-to-supplier-action links were **non-contractual**, not established as a remedy-to-causal-benefit chain.
- `data/omilia_selected_six_payments.csv`: six selected *source-reported* spending observations as in the R76 addendum S17, **not an exhaustive monthly series**, causal effect, supplier-release chronology or confirmed contract allocation. Three entries depend on official indexed excerpts rather than full HTML reading.
- `data/ontario_reported_two_site_differences.csv`: two reported site-level mean documentation-time differences (-12.9 and +10.3 minutes). The original Ontario report contains unresolved **44 versus 42 interactions** wording, so no reconstructed denominator, pooled estimate or contract-remedy attribution is warranted.
- Blank worksheet and three illustrative, source-linked examples designed for human use; neither are independently human-coded evaluations nor validated algorithmic predictions.

## Integrity and release boundaries

The local/ministerial CSVs are publicly distributable **author-derived classifications of public government records**. The original R65/R66/R75 structured source ledgers were not available as immutable raw datasets; reconstructed values are labeled accordingly. The original R76 addendum PDF/Word was later recovered in the private project archive, but is not uploaded here. A machine replay validates recorded counts and file schema, **not the truth of each classification, legal contract enforceability, accuracy, causal benefits or real-time source availability**. No independent human coding, human adjudication, preregistered national sampling, complete PRISMA evidence or generalizable population estimate is represented. Separate cohorts MUST NOT be summed as independent contracts.

Author-generated descriptions are linked to URLs of official government sources; official page content remains authoritative. The release excludes full third-party PDFs, licensed bibliographic exports, restricted records, unpublished contracts, identifiable participant information, manuscript author approval claims and unapproved publication/license declarations.

The repository account name identifies its owner and may be unsuitable for an anonymized peer-review submission; this is an **author-facing public repository**, not a blinded deposit. A permanent repository DOI has not been assigned.
