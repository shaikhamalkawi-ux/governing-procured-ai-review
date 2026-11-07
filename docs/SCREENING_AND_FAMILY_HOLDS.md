# R41 Scoping Evidence Gates: Priorities and Publication Families

This note is a public method record, not a statement that a study is eligible.

## Full-text priorities

From the **220 non-final AI-assisted first-pass reads**, **15** were routed `DIRECT_TA_POSSIBLE` and **19** were routed `HOLD_DIRECTION_OR_UNIT`. These **34** records are a **retrieval priority queue, not the final sample**. The remaining **2,336** provisional identities still require title/abstract review; a record is not excluded merely because it is not in this queue.

The portable `scripts/build_fulltext_queue.py` regenerates the **private** 34-record priority sheet from an authorized private `R41_All2556_Progress_Conserved_PRIVATE.csv`. The private output includes source titles and DOI identifiers for internal retrieval, and must not be committed to this repository. The public 220-row status file deliberately omits licensed source-title and abstract fields.

## Possible multiple reports from one research family (verify, do not collapse)

- `BIB00001` and `BIB01360`: likely overlapping Italian-public-administration subject and title variants. Verify original work, DOI and publication version before treating them as one work or two.
- `BIB02557` and `BIB02573`: both report NHS AI chest-diagnostic implementation. Determine whether one is a project report and another a journal article drawn from shared work; count source documents and underlying studies separately.
- `BIB02562` is related to NHS image-screening implementation but must not be assumed identical to the above without a cohort/project match.
- `BIB00458` discusses procurement of AI *and* AI deployed within procurement operations; source passages must be linked to the right direction of acquisition rather than classifying the entire work at a uniform level.
- `BIB01410` is a review of AI impacts in procurement. Clarify whether it addresses AI purchased by the state or AI used to manage procurement records.
- Culot et al. (2026), DOI `10.1111/jbl.70088`, is an **external near-prior-art lead**, not silently inserted into the original 2,556 identity baseline. A dated refresh is required before counting it in the systematic source universe.

## Evidence chart to be constructed after full-text checks

Record for each unique study: public buyer jurisdiction; acquired AI system/service vs AI as an internal procurement tool; exact supplier and buyer identities; statutory or contractual oversight design; **dated actual** exercise; supplier response; independently measured outcome; causal identification basis; direct original-source locator; and missingness/qualifications.

No thematic frequency, multi-study effect, risk ratio, publication-bias statistic, prevalence or external validation is claimed from this priority queue. Independent human screening is **NOT PERFORMED** and cannot be inferred from a test passing.
