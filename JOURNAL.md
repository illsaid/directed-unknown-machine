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

## Runs 22–86 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–86:** Made complete and incomplete contract states exact across partial and wholly unlabeled inputs.

## Run 87 — Let the missing schema labels carry the repair

**What changed:** Added `SCENARIOS/086-missing-fields-first.md`. Replaced `contract incomplete; add the missing explicit fields without rewriting the notes:` with `Missing explicit fields:`. Missing-field detection, schema order, unsupported-field handling, complete-contract output, the six audit operations, and all decision rules remain unchanged.

**Scenario tested:** A concrete rollout decision supplies `Decision`, `Evidence`, and `Constraints` but omits `Success`. The observable requirement is that repair identify the absent field immediately, preserve the supplied fields, infer no success rule, emit no recommendation, and add no repair mode.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/086-missing-fields-first.md` was mentally simulated: unsupported-label detection returns none, `Success` alone is missing, and the existing repair path exits with `Missing explicit fields:` followed by `Success:`.

**What was removed or rejected:** Removed the generic incomplete-contract diagnosis and instruction sentence. Rejected field inference, prose classification, a second repair mode, schema expansion, and changes to any audit requirement. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The absent schema labels are already a complete repair instruction. A generic diagnosis adds presentation density but no enforceable information.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether the unsupported-field error can be made equally direct without weakening its guidance to preserve meaning inside the four-field schema.