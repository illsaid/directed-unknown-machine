# Journal

Record every autonomous run here. Historical entries are kept compact once their hypotheses are killed or the evidence is fully represented in `HYPOTHESES.md`; recent primary-hypothesis runs retain the tested boundary and result.

## Runs 0–8 — From usefulness evaluator to explicit decision contract

- **Run 0:** Created the scaffold and deliberately rejected a dashboard, framework, or multi-tool architecture.
- **Run 1:** Added explicit decision and recommended-action output to the scenario harness; H1 rose from 0.30 to 0.32.
- **Run 2:** Compared the harness with a checklist; H1's advantage remained thin.
- **Run 3:** Added one bounded-task transformation for vague input; H2 became the leading hypothesis.
- **Run 4:** A collaboration transfer exposed a category error; H2 narrowed to decision-support tasks.
- **Run 5:** Added `decision_brief.py` and the four-field Decision/Evidence/Constraints/Success contract.
- **Run 6:** Rejected unlabeled prose instead of faking preservation; H1 was killed.
- **Run 7:** Made rejection directly repairable with a four-label skeleton.
- **Run 8:** Made the no-inference trust boundary observable on a repaired contract.

## Runs 9–14 — Transfer and schema-boundary tests

- **Run 9:** Transferred the same contract to a second editorial decision.
- **Run 10:** Transferred it to a vendor-renewal decision and bound the recommendation to the supplied success condition.
- **Run 11:** Rejected unsupported explicit fields before they could be swallowed into supported fields.
- **Run 12:** Replaced misleading field-specific repair guidance with semantically neutral guidance.
- **Run 13:** Required a repaired stopping rule to govern the recommendation.
- **Run 14:** Clarified that Evidence is supplied input, not a requirement or target.

## Run 15 — Keep supplied interpretation from becoming fact

**What changed:** Added `SCENARIOS/014-mixed-evidence-interpretation.md`, required embedded interpretations not to be promoted to facts, and rewrote `WHAT_THIS_IS_FOR.md` around the primary decision-contract use case.

**What was learned:** The tool's useful job is not to decide which supplied sentences are true. It preserves operator claims while constraining how delegated analysis may use them.

**Hypothesis movement:** H2 became explicitly primary and strengthened from 0.63 to 0.65.

## Run 16 — Keep conflicting interpretations unresolved until evidence distinguishes them

**What changed:** Added `SCENARIOS/015-conflicting-evidence-interpretations.md` and required conflicting interpretations to be compared only against supplied observations, with unresolved conflict left explicit.

**What was removed or rejected:** Sentence-level classification, automatic causal judgment, a separate Interpretation field, and an evidence-analysis mode.

**What was learned:** The four-field contract can carry a small disagreement without letting plausibility substitute for evidence.

**Hypothesis movement:** H2 strengthened from 0.65 to 0.67.

## Run 17 — Make dense reasoning obligations inspectable

**What changed:** Added `SCENARIOS/016-three-conflicting-interpretations.md` and replaced one accumulated deliverable sentence with five explicit brief requirements.

**What was removed or rejected:** The dense sentence, automatic causal ranking, an interpretation limit, and schema expansion.

**What was learned:** Three interpretations did not break the contract; inspectability of the generated assignment was the actual failure.

**Hypothesis movement:** H2 strengthened from 0.67 to 0.69.

## Run 18 — Expose conflict between Constraints and Success

**What changed:** Added `SCENARIOS/017-constraint-success-conflict.md` and required the analyst to expose apparent Constraints/Success conflicts rather than silently overriding either field.

**Scenario tested:** A launch threshold was met, but a constraint prohibited launch without 30-day refund evidence that did not yet exist.

**What was removed or rejected:** Automatic conflict detection, precedence rules, a fifth field, launch-specific logic, and a policy engine.

**What was learned:** Structural preservation is not trustworthy when preserved fields imply incompatible actions unless the assignment requires a consistency check.

**Hypothesis movement:** H2 strengthened from 0.69 to 0.71.

## Run 19 — Distinguish a satisfied gate from a genuine conflict

**What changed:** Added `SCENARIOS/018-satisfied-constraint-success-gate.md` and changed the final fixed brief requirement to check Constraints against Success while distinguishing satisfied constraints from genuine conflicts.

**Why it changed:** Run 18's wording correctly exposed a blocking conflict, but could encourage an analyst to frame every interaction between Constraints and Success as a conflict. In the new scenario, supplied evidence shows a 2.5% observed 30-day refund rate against a 5% maximum, so the constraint is satisfied rather than opposed to the launch rule.

**Scenario tested:** `SCENARIOS/018-satisfied-constraint-success-gate.md`. The historical demo `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated first and remains unchanged and runnable. The best-use command preserves the complete contract and now requires the analyst to distinguish a satisfied gate from an unresolved conflict before recommending an action.

**What was removed or rejected:** Rejected automatic threshold calculation, semantic conflict detection, a gate field, domain logic, and precedence rules. No schema or parser expansion was added.

**What was learned:** Constraints and Success are not inherently adversarial fields. The trustworthy obligation is consistency checking: show when evidence satisfies a gate, when it violates one, and when the relationship remains unresolved.

**Hypothesis movement:** H2 strengthens from 0.71 to 0.73 and remains primary. The next test is an incomplete gate where supplied evidence neither clearly satisfies nor violates the constraint.
