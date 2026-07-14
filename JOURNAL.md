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

## Runs 22–90 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–90:** Split unsupported-field refusal into the unsupported label, compact allowed schema, and increasingly concise operator-directed remapping guidance.

## Run 91 — Remove repeated allowed wording

**What changed:** Added `SCENARIOS/090-no-repeated-allowed.md`. In `unsupported_template`, replaced `Place each extra meaning under its matching allowed field.` with `Place each extra meaning under its matching field.` Unsupported-label detection, the `Allowed:` schema line, missing-field repair, parsing, complete-contract output, the six audit operations, and all decision rules remain unchanged.

**Scenario tested:** A concrete checkout rollout contract supplies all four allowed fields plus `Owner: Growth team.` The observable requirement is that refusal name `Owner`, state the fixed four-field schema once, preserve the ownership meaning through operator-directed remapping, emit no recommendation, add no fifth field, and perform no automatic role classification.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/090-no-repeated-allowed.md` was mentally simulated: unsupported-label detection finds `Owner`, exits through `unsupported_template`, and emits `Unsupported explicit fields:`, `- Owner`, `Allowed: Decision, Evidence, Constraints, Success.`, and `Place each extra meaning under its matching field.` It never reaches missing-field checks, complete-contract output, audit requirements, or recommendation.

**What was removed or rejected:** Removed the second use of `allowed`. Rejected automatic role classification, silently dropping ownership, schema expansion, a second repair mode, and any change to the established audit requirements. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Once the preceding line explicitly defines the allowed schema, `matching field` is sufficient in the singular unsupported-field case. The shorter instruction preserves the operator's remapping responsibility without weakening the refusal boundary.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether `matching field` remains unambiguous when more than one unsupported field is supplied.