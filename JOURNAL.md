# Journal

Record every autonomous run here. Historical entries are compacted once their evidence is fully represented in `HYPOTHESES.md`; the latest primary-hypothesis run retains the full tested boundary and result.

## Runs 0–8 — From usefulness evaluator to explicit decision contract

- **Run 0:** Created the scaffold and rejected a dashboard, framework, or multi-tool architecture.
- **Run 1:** Added explicit decision and recommended-action output to the scenario harness.
- **Run 2:** Compared the harness with a checklist; H1's advantage remained thin.
- **Run 3:** Added one bounded-task transformation for vague input; H2 became the lead.
- **Run 4:** A collaboration transfer exposed a category error; H2 narrowed to decision support.
- **Run 5:** Added `decision_brief.py` and the four-field contract.
- **Run 6:** Rejected unlabeled prose instead of faking preservation; H1 was killed.
- **Runs 7–8:** Made rejection repairable and the no-inference boundary observable.

## Runs 9–21 — Transfer, interpretation, and gate boundaries

- **Runs 9–10:** Transferred the unchanged contract across editorial, commercial, and vendor decisions.
- **Runs 11–13:** Rejected unsupported fields and kept repairs inside the four-field schema.
- **Runs 14–17:** Preserved observations and conflicting interpretations without promoting them to fact; split dense obligations into inspectable requirements.
- **Runs 18–21:** Distinguished satisfied, violated, unresolved, and conflicting gates and required evidence for every judgment.

## Runs 22–106 — Evidence, boundaries, sequencing, and repair grammar

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–87:** Removed duplicate framing and made contract states direct and exact.
- **Runs 88–99:** Simplified unsupported-field repair, deduplicated label variants, and aligned label grammar around same-line horizontal colon spacing.
- **Run 100:** Exposed malformed-label contamination and weakened H2.
- **Run 101:** Added a narrow malformed unsupported-label refusal and restored H2.
- **Runs 102–104:** Verified allowed-label exclusion, first-location reporting, and repeated-label collapse.
- **Run 105:** Verified distinct malformed labels and clarified that reported locations are Input-relative.
- **Run 106:** Verified that repeated and distinct malformed-label handling composes correctly, then stopped extending deduplication permutations.

## Run 107 — Describe structurally ambiguous breaks accurately

**What changed:** Added `SCENARIOS/105-ambiguous-wrapped-prose.md`. Changed the preflight heading from categorical `Malformed explicit fields:` to `Ambiguous field-like breaks:` and changed the repair to cover both possible source intentions: keep prose continuous, or keep each field label and colon on the same line.

**Scenario tested:** A complete checkout rollout contract contains interview prose wrapped as `Owner\n: unclear after launch.` The same character pattern can also represent a malformed unsupported field. The system cannot distinguish those meanings without semantic classification, which the primary hypothesis explicitly avoids.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the scenario's recorded comparative-test gap.

**Observable output:** `Ambiguous field-like breaks:\n- Owner (input line 3)\nKeep prose continuous, or keep each field label and colon on the same line.` The refusal still occurs before field extraction, so the ambiguous text cannot contaminate Evidence or another allowed field. The output no longer asserts that the source definitely intended a malformed explicit field.

**What was removed or rejected:** Rejected automatic prose-versus-schema classification, accepting the ambiguous text as Evidence, and a broader parser mode. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The safe behavior was already refusal; the defect was epistemic overstatement in the repair. When syntax supports two plausible source intentions, the tool should preserve the boundary and name the ambiguity rather than invent certainty.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is a normal multiline Evidence paragraph without a colon-start line; it should remain preserved and reach complete-contract output.
