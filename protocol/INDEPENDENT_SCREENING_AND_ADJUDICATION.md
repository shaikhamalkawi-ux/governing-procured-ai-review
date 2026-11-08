# Independent title/abstract and full-text screening — R42 quality gate

This public protocol documents **future** independent human screening; it does not claim that it has happened.

- Freeze the licensed bibliographic source universe and stable BIB identifiers before assigning records.
- Give two human reviewers identical, privately accessible record batches without disclosing each other's decisions or AI-first-pass labels.
- Each reviewer fills a separate private CSV with these columns: record_id, reviewer_id, reviewer_kind, decision, reason_code, evidence_level.
- Valid decisions are INCLUDE_CANDIDATE, EXCLUDE_CANDIDATE, or HOLD. At title/abstract stage these are not full-text inclusion decisions.
- Valid reason codes: PCC_IN_SCOPE, NOT_PUBLIC_SECTOR, NOT_PROCURED_AI, AI_USED_IN_PROCUREMENT_ONLY, NO_ACCOUNTABILITY_EVIDENCE, WRONG_PUBLICATION_UNIT, INSUFFICIENT_METADATA, OTHER_DOCUMENTED.
- Concatenate the completed independent forms only after both submissions are frozen.
- Run: python scripts/validate_independent_screening.py --votes PRIVATE.csv --universe AUTHORIZED_IDS.csv --report PRIVATE_QA.json
- A failure means the review votes require source-data repair; a disagreement or differing evidence levels must be adjudicated by a documented human reviewer. The script never adjudicates, never excludes a record on its own, never turns AI labels into human votes and never generates final PRISMA counts.
- Full-text eligibility requires an additional study-family check and evidence-based human decision after the title/abstract stage; proceed to PRISMA only once all participating records are adjudicated and stage counts reconcile.
- Store reviewer identities, raw export metadata, texts and exclusion reasons privately where required by licensing and privacy obligations. Public summary outputs may report aggregate counts only after verification.

Scientific guardrail: study-level units, conference proceedings containers, preprint-to-publication versions and overlapping empirical cohorts must be resolved separately; do not treat a distinct bibliographic record as an independent study.
