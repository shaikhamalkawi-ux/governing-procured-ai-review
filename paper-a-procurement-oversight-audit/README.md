# Paper A — Government AI procurement oversight: source-to-claim audit

**Linked manuscript:** *When AI Supplier Disclosures and Contracts Tell Different Stories: A Documentary Audit for Public Procurement Oversight* (99aiA, scientific baseline R76S3, editorial author-review G8-EP1 as of 22 November 2026). This is a **public-safe data and reproducibility release**, not a published or peer-reviewed article, validated classification model or DOI-tagged archive.

This subdirectory is **Paper A only**; it does not represent the earlier, separate 99aiA scoping-review workflow or any 99aiB project.

## What can be reproduced

| Evidence set | Exact analysis unit | Source-based descriptive numbers |
|---|---|---|
| Local-authority UK ATRS | 13 disclosed entries | 12 outside involvement; 7 procurement-connected; 2 expressly direct commercial AI-use descriptions |
| Ministerial UK ATRS | 20 separately selected entries | 14 declared outside parties; 13 AI/ML, 3 explicitly non-AI, 4 unresolved |
| Historical ledger | 28 evidence descriptions in 9 programmes, **NOT 28 independent contracts** | 2 documented **non-contractual** oversight-to-supplier responses; 0 complete contract-remedy-to-causally-attributable benefit chains in these inspected descriptions |
| Expenditure examples | 6 selected DWP Omilia entries | Listed payments, not a continuous spending series or specific remedy proof |
| Ontario comparison | 2 site reports | Reported mean documentation-time differences -12.9 and +10.3 minutes; no pooled denominator |

The three documentary populations have different selection rules and **must not be added into 61 purchased AI contracts**. `PROVENANCE_AND_LIMITATIONS.md` gives source availability and limits. All references to source records identify *published reports or classifications*, not independent raw-outcome measurements.

## Files

- `data/local_authority_13_derived_R76.csv` and `data/ministerial_20_derived_R76.csv`: official source URLs, original published roles and source-code flags; **derived from indexed R76 supplement** rather than restored original R65/R66 CSVs.
- `data/omilia_selected_six_payments.csv` and `data/ontario_reported_two_site_differences.csv`: **source-reported plotted inputs** (not independent sensor/causal datasets).
- `data/claim_check_blank.csv` and `data/three_worked_examples.csv`: reusable claim-to-source worksheet and three documentary illustrations.
- `data/SHA256SUMS.txt`: source files' SHA-256 checksums.
- `scripts/replay_paper_a_public.py`: deterministic standard-library count and structural checks.
- Existing frozen `../data/documentary/` at the repository root contains the historical source ledger, 140 proposition-support register and `replay_public_safe.py`; this historical directory is **not rewritten** by this release.

## Reproduce the checks

From the root of this GitHub repository:

```sh
python paper-a-procurement-oversight-audit/scripts/replay_paper_a_public.py
python data/documentary/replay_public_safe.py
```

The first command checks the separate 13-, 20- and 28-description datasets, expected descriptive categories, selected plot-point inputs, source locators and SHA-256 integrity; it does not perform fresh coding or legal/source validation. The second replays the already-published historical public-safe audit. Only Python 3.10+ standard-library modules are needed.

## Citing and reusing

When citing the current paper, distinguish this public-safe repo data release from the scientific manuscript, which has not yet received a permanent DOI. The current repository homepage is [Governing Procured AI](https://github.com/shaikhamalkawi-ux/governing-procured-ai-review), and this folder tracks the present documentary paper. An author-controlled archive/DOI, if approved and deposited, will be added separately. Publicly visible GitHub ownership does not mean the manuscript is approved for submission or that an independent human audit was conducted.

**No licence for third-party government PDFs, licensed bibliographic exports or source documents is granted by this release.** The existing `LICENSE-CODE` covers repository code on its own terms; no unverified data-reuse licence is asserted here.

## R76 source-to-classification provenance check (22 November 2026)

The additional [33-row crosswalk](data/source_to_role_crosswalk_33.csv) traces all 13 local and 20 ministerial retained entries to the author-written original R76 supplementary PDF pages, the exact official registry URLs, the frozen role/technology classifications and a separate source-narrative reading. All 33 match the frozen published derived CSVs. The check documents **internal consistency of the R76 source-authored addendum**, not an independent 33-page original government re-adjudication; 10 selected official records were consulted separately. The original R65/R66/R75 machine ledgers were not recovered, and there was no independent human coding. See [the provenance methodology](SOURCE_TO_ROLE_CROSSWALK_README.md) and run `python paper-a-procurement-oversight-audit/scripts/check_source_crosswalk.py` after cloning the full repo. No scientific result or denominator has changed.
