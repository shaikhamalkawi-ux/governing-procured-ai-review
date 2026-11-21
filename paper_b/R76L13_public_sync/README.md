# Paper B — R76L13: public evidence and figure audit materials

**Article:** *After Government Buys AI: What Can Public-Sector Auditors Verify? A Critical Review of Supplier Accountability and Outcome Evidence*.

**Version:** R76L13 (22 November 2026). **Status:** author review / **Submission HOLD**. This folder is a public-safe supporting release, **not** a peer-reviewed publication, a final author-approved manuscript, an empirical supplier-remedy dataset, or a completed PRISMA-ScR review.

The main paper is a **critical narrative review** describing what procurement contracts, interviews, administrative notices, official audits, supplier records and outcome measurements can or cannot establish about accountability after a public body buys AI. Its current curated bibliography contains **93 cited source identities**, not 93 independent empirical studies.

## Contents and what they support

| Path | Contents | Evidence boundary |
|---|---|---|
| `data/source_identity_register_93.csv` | 93 cited bibliographic identities, source roles, public locators and inherited access labels | The access fields were not revalidated line by line for this deposit |
| `data/source_selection_ledger_93.csv` | Retrospective reasons for narrative retention | Not a PRISMA inclusion/exclusion log |
| `data/literature_update_2021_2026_9_sources.csv` | Bounded additions R85–R93, with source-access and claim limits | Different source types and access depths; not comparable estimates |
| `data/targeted_search_log_20261121.csv` | Ten logged search/discovery entries from 21 November 2026 | Not a reconstructed historical systematic search or hit count |
| `data/figure_data_manifest.json` | Exact chart quantities and cautionary notes | Source-reported and arithmetic values, not new measured effects |
| `figures/*.pdf` | Four main figures and Supplementary Figure S1 inherited byte-for-byte from the R76L13 manuscript source | Figures do not validate the underlying published studies |
| `scripts/build_figures.py` | Rebuild the five journal figure panels with ReportLab | Requires `reportlab` and optionally local DejaVu fonts; font binaries are not supplied |
| `scripts/verify_public_release.py` | Recompute internal counts, percentages, weights and SHA-256 checks | File/arithmetic QA only |
| `RELEASE_SHA256SUMS.txt` | Frozen SHA-256 digests of this public subset | Checks the committed public files, not restricted external sources |

## Main reproducible quantities

- Source roles among 93 **cited identities**: official/public evidence **34** (36.6%), empirical/observed research **25** (26.9%), legal/doctrinal **16** (17.2%), standards/methods **9** (9.7%), review/methodology **6** (6.5%), other scholarship/sector evidence **3** (3.2%). The displayed rounded percentages total **100.1%**.
- OECD 2026 **country-level** indicators for 36 participating countries: central AI-purchasing support **21/36 = 58.3%**, post-deployment audit **11/36 = 30.6%**, AI-use impact measurement **10/36 = 27.8%**. These are neither contract-level transitions nor mutually exclusive outcome groups.
- Kim and Kesari (2026) U.S. **state-government** contract-clause study: 215 selected contracts, 3,771 provisions, **77.0%** generic/boilerplate, and selected clause-category proportions **5.3%** transparency, **3.0%** cybersecurity and **2.4%** fairness/accountability. These are **not U.S. federal contract proportions** and **not measured effects of enforcement**. Refer to the cited source for its actual coding scope and overlap definitions.
- GOV Voice UK4 published tender criteria: **70%** quality + **30%** commercial. With announced quality subweights (60%, 30%, 10%), the *conditional arithmetic* is **42%** product, **21%** written, **7%** social and **30%** commercial. These are neither completed adjudication scores nor results achieved after deployment.
- GOV Voice UK7 published 100% / 90% operational **targets** are not observed performance rates; target graphics are not included as achieved outcomes.

## Verification

Requires Python 3.10+ (standard library) for the structural audit:

```bash
python paper_b/R76L13_public_sync/scripts/verify_public_release.py
python -m unittest discover -s paper_b/R76L13_public_sync/tests -v
```

Optional figure regeneration, from a clean checkout:

```bash
python -m pip install -r paper_b/R76L13_public_sync/requirements-figures.txt
python paper_b/R76L13_public_sync/scripts/build_figures.py
```

Newly rendered PDF bytes may differ across platforms or font installations; the source data/semantics are the reproducibility target. The checked-in `figures/*.pdf` are the exact author-review graphics, and their SHA-256 values are recorded in `RELEASE_SHA256SUMS.txt`.

## Access, copyright and citation

The public release contains authored data tables, original analysis scripts and figures. **It excludes** licensed Scopus/Web of Science exports, third-party article PDFs, unshared full-text documents, confidential government records, author declarations, and the complete internal manuscript delivery ZIP. Bibliographic source links refer to third-party works; users must respect original copyrights and access conditions. No new data- or figure-reuse license is implied here; code-license and final journal/repository citation terms require author approval.

**Canonical GitHub repository:** https://github.com/shaikhamalkawi-ux/governing-procured-ai-review

**Manuscript disclosure:** The R76L13 manuscript names this repository in its *Data and Source Availability* section. The manuscript is not certified as published, externally validated or author-final. The separate, historical provisional R51 screening corpus has a different sampling universe and cannot be combined with the paper's R53 checkpoint (800 of 920 provisional screen decisions; 120 then outstanding), or treated as a completed inclusion denominator.
