# R42 — Procurement direction and evidence-stage safeguards

**Project:** 99aI; **date:** 2026-11-08; **stage:** R42 B04. Not a completed scoping review.

A new deterministic, purposive prioritization of the **2,336 records still unread at R41** chose 64 original titles and abstracts for individual AI-assisted reading. The cumulative first-pass is **284/2,556** and **2,272 remain unread**. R41's 220 existing provisional labels have not been revised. The heuristic ranks records; it does **not** decide eligibility.

A lexical hit for "procurement", "AI", or "supplier" may indicate at least four different phenomena:

1. A government **purchasing AI** from an external provider (central research question);
2. AI **used in procurement** to buy unrelated products;
3. AI used by a **researcher analyzing procurement data** without government deploying that model;
4. **Private consumers or firms** buying products or choosing suppliers.

The extra `r42_direction` field prevents the coarse triage label from hiding these different meanings. Study units and source evidence must still be verified at full text.

**Evidence ladder:** proposed contract clauses are not executed contracts; purchasing an AI system is not proof of dated monitoring; a deployment withdrawal after funding ends is not independently verified contract enforcement; subsequent outcomes are not evidence of causal contractual effectiveness without a separate attribution design.

Targeted publisher cross-checks: Trevor Taylor's 2019 defence AI acquisition argument (https://doi.org/10.1080/03071847.2019.1694229), Beraja et al.'s 2023 empirical facial-recognition government contracts (https://doi.org/10.1093/qje/qjad012), and Packer et al.'s 2026 NHS AI tool decommissioning survey (https://doi.org/10.1016/j.jacr.2026.06.004). These **do not establish** whether a specific vendor answered a contractual remediation notice.

**Identity hold:** BIB00057 and BIB00202 are distinct provider keys whose frozen conference-container titles and abstracts match exactly. They have not been merged or counted as independent studies pending publisher-level adjudication.

**Never infer from R42:** final inclusion/exclusion, PRISMA-ScR flow counts, human dual screening, screen sensitivity, cross-record prevalence, universal accountability rates, or causal supplier-remedy effects.

**Release boundary:** this GitHub repository contains ONLY original stable record IDs and nonlicensed first-pass labels; original Scopus/WoS abstracts, titles, publisher PDFs and fulltext audit notes remain PRIVATE in the controlled research archive.

Run `python scripts/audit_r42_direction.py` and `python -m unittest discover -s tests -v` to check public-file integrity. Test PASS is **not** human source validation.
