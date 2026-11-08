# R43: Government as the AI buyer — source- and inference-stage controls

**Research:** Governing Procured AI: Vendor Accountability and Post-Deployment Oversight in the Public Sector. **Checkpoint:** R43 B05, 8 November 2026.

## Cumulative status
R41 screened 220 original bibliographic IDs provisionally; R42 added 64; R43 adds 120 individually reasoned original title/abstract reads. Total **404 / 2,556** first-pass, **2,152 unread**. These are stable *bibliographic identity groups*, NOT 2,556 verified unique studies, and NOT a sample of 404 eligible studies. No independent second human, adjudicated exclusion, full-text eligibility set, final study count or PRISMA-ScR flow exists.

New R43 label counts: 5 direct leads, 17 held for vendor/contract/study identity, 28 AI used within or to study procurement, 36 contextual and 34 outside. All five categories are **non-final triage routes**.

## Critical role separation
**Government buying AI from an external supplier** is distinct from (a) government developing AI in-house, (b) government using AI to purchase unrelated products, (c) researchers using AI to analyze public contracts, and (d) private companies/consumers buying AI or other products.

- **BIB01334, Brazil's Alice:** The primary public CGU office source describes the Alice procurement-monitoring tool as CGU-developed. Government use in procurement is not proof of external purchase of Alice. Original source: https://www.gov.br/cgu/pt-br/assuntos/auditoria-e-fiscalizacao/alice/alice/
- **BIB00150, migration AI secrecy:** The publisher article examines algorithmic opacity and legal access where vendor-provided technologies intersect migration administration. It does not establish a dated exercise of a supplier audit/remedy. https://www.cambridge.org/core/journals/european-law-open/article/cracking-ai-secrecy-beyond-eu-migration-law-and-governance/0BDF7E96162E239A31321A000DD486F4
- **BIB00917, Chinese police facial recognition:** Original publisher reports government AI procurement evidence. It is not direct evidence of contract remedies being triggered; track potential empirical family relationships to BIB00667 before counting studies. https://academic.oup.com/restud/article-abstract/90/4/1701/6665906
- **BIB00776, access to algorithms:** A legal argument about proprietary algorithmic tools and public law, not an observed enforcement event. https://ir.lawnet.fordham.edu/flr/vol88/iss4/2/
- **BIB00542:** Analysis of human-oversight policies is distinct from supplier compliance measurement. https://www.sciencedirect.com/science/article/pii/S0267364922000292

**Source version hold:** BIB00421 has a 2027 issue volume but may have appeared online during 2026. Verify publication-event date and citation metadata rather than auto-exclude by future issue year.

**Record identity holds:** BIB00627/BIB00767 and BIB00809/BIB00866 have matching title/abstract conference-container signals. Neither is proof of two distinct studies, and neither pair may be silently collapsed without publisher-level child-record audit.

## Proposed evidence-stage vocabulary for eventual data charting
1. **Normative design:** what oversight/contract provisions ought to exist
2. **Contract formation:** actual buyer, vendor, signed terms, contract scope and version
3. **Operational oversight:** dated audit, access request, incident, monitoring event
4. **Vendor response:** documented remediation, sanctions, amendment or contestation
5. **Outcome attribution:** traceable consequences plus an appropriate design for causal claims

These stages are distinct evidence capabilities, not automatically sequential outcomes. Do not infer that a signed audit clause was exercised, that a system withdrawal resulted from supplier default, or that later accuracy/cost metrics demonstrate causally effective procurement oversight.

## Reproducibility and release limits
Public paths: `data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv`, `data/R43_progress_summary.json`, `data/R43_Original_Source_Verification_PublicSafe.csv`, `scripts/audit_r43_public.py`, `tests/test_audit_r43_public.py`.

Execute `python scripts/audit_r43_public.py` and `python -m unittest discover -s tests -v`. These check integrity, duplication, stages and known failure modes. **Test success does not mean semantic source accuracy or completed study selection.**

Licensed original Scopus/WoS titles, abstracts, exports and related private methodological notes remain in controlled Drive/private archive, not GitHub. Permanent DOI, author-approved licensing and full review admissibility remain pending. The R38 documentary manuscript is a separate purposive analysis and its earlier results have not been rewritten as scoping-review conclusions.
