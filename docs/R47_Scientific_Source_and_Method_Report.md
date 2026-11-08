# Project 99aI — R47 continuation from R46

**Research question:** Governing Procured AI: Vendor Accountability and Post-Deployment Oversight in the Public Sector.

## Reproducible bounded continuation

The R46 sealed 2,556-identity source corpus and previous 648 case-specific AI-assisted title/abstract assessments are unchanged. R46 had frozen a 192-identity research plan; 68 records had already been examined in R46. R47 processes its **124 previously unread records**, rather than resampling or double counting. Its records now carry an ID, original source-scoped title/abstract or missing-abstract state, one preliminary direction, and an explicit rationale in the PRIVATE table. The public counterpart strips title, abstract, DOI and publisher metadata. **Total provisional case-text assessments: 772/2,556; remaining 1,784.** These are neither independently adjudicated studies nor final PRISMA decisions. The R46 machine-only routes for the remaining records remain machine-only.

The new 124 directions are 3 cases where AI was used to analyze a policy or procurement task rather than bought by government, 70 contextual, 10 ambiguity or source-unit holds, and 41 preliminary out-of-scope routes. These categories have no screening-sensitivity, prevalence or final-exclusion interpretation.

## Priority source interpretation: independently checked publisher pages

- **BIB01273 — Dekker et al. (2022), *Co-designing algorithms for governance*.** The publisher describes a humanitarian collaboration between IOM, NGO Elva, and analysis company Notilyze, with funding through a humanitarian innovation challenge. The documentary evidence supports collaborative algorithm design but does not by itself prove that a public authority purchased a third-party AI product under an executed service contract. Source: https://journals.sagepub.com/doi/full/10.1177/20539517221087855 . Route: **contextual / distinct public-international organization partnership**.
- **BIB01506 — Survey of US health system leaders (2024).** The publisher reports 32/65 institutional responses and that 11/27 AI-using respondent institutions primarily purchased AI predictive models from vendors. These are **not 11 verified government procurements**, because public legal status of each health system is not established by the survey. Source: https://link.springer.com/article/10.1186/s44247-024-00135-3 . Route: **contextual procurement evidence with population caveat**.
- **BIB02546 — Andersen et al. (2026), Norwegian emergency primary care.** Original open-access paper describes 12 personnel interviews and a theme on staff roles in *prospective* AI procurement and development. This does not demonstrate a dated purchase, contract or supplier enforcement event. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC13168706/ . Route: **hold for acquisition evidence**.
- **BIB00263 — AWS government lobbying in Canada.** The retained indexed abstract describes lobbying for procurement of AWS services and AI-related cloud capabilities. A specific contracted AI system and postdeployment audit event are not documented by that abstract, so the source is **HOLD**, not proof of government procurement of an AI model.

## Decision evidence ladder retained

The final paper must distinguish source-defined: (i) proposed legal clauses, (ii) executed buyer/supplier instrument, (iii) dated monitoring/audit action, (iv) observed supplier response/remedy, and (v) downstream outcomes with attribution limits. Source documents supporting a lower stage must not be silently recoded as higher-stage evidence. Purchasing cloud compute is not automatically purchasing an AI system, receiving funding for development is not a public-service purchase, and mentioning 'AI' in a copyright notice is not an AI study.

## Files and guards

- `R47_124_CaseText_Triage_PRIVATE.csv` — all source text and individual reasons (restricted; NEVER publish).
- `R47_124_CaseText_Triage_PUBLICSAFE.csv` — original ID and original derived preliminary label/reason code only.
- `R47_ProgressSummary.json` — exact progression and source hash.
- `audit_r47.py`, `build_r47.py` — private reproducibility; source archive required. No attempt to reproduce licensed Scopus/WoS exports publicly.
- `99aI_Documentary_Main_with_Appendix_R46.pdf` — unchanged presentation format: 15-page main paper followed by 11-page Appendix, 26 pages total. Scientific manuscript and scoping review remain separate.

**Next source task:** review the remaining 1,784 records at the same case-text level, prioritizing vendor/client contracts and ambiguous public/legal identities, then retrieve/verify primary full texts of the evidence-bearing queue; deduplicate reports at study-family level before any final synthesis. Preserve non-final states until source and study evidence are resolved.
