# 99aI R44 — Frozen two-stratum screening safety audit (8 Nov 2026)

The original 2,556 bibliographic identity groups were conserved. R43 had 404 AI-assisted single-pass, non-final title/abstract readings; R44 adds 64 frozen independent safety records (32 LOW and 32 MID heuristic-score strata), now 468 provisionally read and 2,088 unread. Neither stratum is population-representative; **do not calculate or claim recall/sensitivity/false-negative rates**, PRISMA-ScR inclusion, or independent human screening.

New provisional R44 labels: 50 out-of-scope, 8 contextual, **5 unresolved source-role holds**, 1 AI used around government school purchasing, **0 direct**. All are preliminary and may be revised after original-source eligibility adjudication.

## Source-specific distinctions

- **BIB00433, original 2026 article on commercial spyware markets:** Government entities are described as customers of commercial spyware. This **does not establish that the spyware product was AI**, nor a contract audit or supplier correction. Although indexed with 'Artificial intelligence' in the provider metadata, source-specific AI capability is **HOLD**, not direct eligibility. DOI: https://doi.org/10.1016/j.clsr.2026.106322
- **BIB01683, FoodSIS (Singapore NEA and IBM research authors):** An operational government AI pilot is documented, but procurement terms and supplier obligations are not. Original author-institution record: https://research.ibm.com/publications/foodsis-a-text-mining-system-to-improve-the-state-of-food-safety-in-singapore
- **BIB01917, SIADEX (Andalusian Regional Government):** The authors state they developed an AI planning system under a public research contract, not proof of a commercially procured production AI service or an exercised postdeployment contract remedy. Author PDF text consulted, independent visual PDF screenshot retrieval unavailable: https://citeseerx.ist.psu.edu/document?doi=20a963c1112dc40cec3b442c3876eb5571f9c93f&repid=rep1&type=pdf
- **BIB02145, Singapore care robotics:** Supplier and public-buyer identity unresolved; HOLD.
- **BIB00233, proceedings container:** 25 children, not one eligible study or 25 automatically eligible independent reports; HOLD.

The central research design must separate actual public authority BUYING AI from research or public-sector AI USE, R&D support from signed service procurement, contract language from dated oversight, and observed vendor response from downstream causal outcomes. The remaining 2,088 must be individually assessed, and original contracts/source full texts verified before adjudicated eligibility. No manuscript claims were changed.

## Reproducibility and rights
Execute `python scripts/audit_r44_public.py` and `python -m unittest discover -s tests -v`. Public artifact includes derived IDs and stage labels only; private licensed Scopus/WoS titles, abstracts, full-text PDFs, individual reason notes and original source files remain outside GitHub.

GitHub QA checks file integrity and label conservation but **cannot establish semantic validity of original source claims or study eligibility**.
