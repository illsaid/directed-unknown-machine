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

## Runs 22–91 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–91:** Split unsupported-field refusal into the unsupported label, compact allowed schema, and increasingly concise operator-directed remapping guidance.

## Run 92 — Clarify multiple-field remapping

**What changed:** Added `SCENARIOS/091-multiple-unsupported-fields.md`. In `unsupported_template`, replaced `Place each extra meaning under its matching field.` with `Remap each extra meaning to one of those fields.` Unsupported-label detection, source-order listing, the `Allowed:` schema line, missing-field repair, parsing, complete-contract output, the six audit operations, and all decision rules remain unchanged.

**Scenario tested:** A concrete checkout rollout contract supplies all four allowed fields plus `Owner: Growth team.` and `Deadline: Decide by Friday.` The observable requirement is that refusal name both unsupported fields separately, state the fixed schema once, preserve both meanings for manual remapping, emit no recommendation, add no new fields, and perform no automatic field assignment.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/091-multiple-unsupported-fields.md` was mentally simulated: unsupported-label detection finds `Owner` and `Deadline` in source order, exits through `unsupported_template`, and emits `Unsupported explicit fields:`, both labels, `Allowed: Decision, Evidence, Constraints, Success.`, and `Remap each extra meaning to one of those fields.` It never reaches missing-field checks, complete-contract output, audit requirements, or recommendation.

**What was removed or rejected:** Removed the implication that every extra meaning already has a uniquely determined `matching field`. Rejected automatic role classification, silently dropping either extra meaning, schema expansion, a second repair mode, and any change to the established audit requirements. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The prior singular wording was adequate for one unsupported field but became overconfident with two. Pointing back to `those fields` preserves the fixed destination set while making operator choice explicit and avoiding a false claim that the executable knows the correct mapping.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether repeated unsupported labels should remain repeated to preserve distinct meanings or be collapsed for concision.