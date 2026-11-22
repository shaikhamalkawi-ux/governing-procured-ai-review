# Paper A — Source-to-role crosswalk (13 local + 20 ministerial)

This document explains the separately published `data/source_to_role_crosswalk_33.csv`. The source is the **author-written R76 cumulative supplement** `Paper_A_R76_NewCumulativeSupplement_S13_to_S28.pdf` (22 pages, SHA-256 `7988989995f2f43a82b60c1d5ddd314dcf3c1cecc53ad3a2539292103e5c90d2`) and the previously released `data/local_authority_13_derived_R76.csv` and `data/ministerial_20_derived_R76.csv`.

The review used two separate paths: (A) the frozen public CSV records, and (B) source-authored PDF narratives (local S13-B, ministerial supplier S15 and complete technology status roster S27). It checked that the documentary role, third-party field and (for ministerial records) technology-source state agree. Every record has an original PDF page number, an official government URL and a short *source-authored* phrasing/locator. The two paths match 33/33. This proves **internal consistency**, not independent reproduction of the original official web-page interpretation or access to the original R65/R66/R75 machine ledgers. Ten selected official pages were reviewed again during this work; the other 23 cannot be labelled freshly live-verified. There was no human double coding and no inter-rater statistic.

Crucially, **13 local entries and 20 ministerial entries are different, nonprobability directory selections**, while the historical 28 descriptions are nested within nine programme families. The 3 broad local references to a contract/paid relationship in the R76 source include a parent contact-centre award; the narrower *AI-specific direct commercial use* test retains 2 entries (Newcastle Magic Notes and Dorset Formulate). This difference reflects different source questions and is **not** a new reclassification.

Run from the repository root:

```
python paper-a-procurement-oversight-audit/scripts/check_source_crosswalk.py
```

The raw source supplement remains in the manuscript's author/review package and should be made available with the journal supplement, subject to author rights. This crosswalk does **not** replace signed purchase orders, official original pages, or independent human validation. It does not attest to legal compliance, contract-cure effectiveness or model performance.
