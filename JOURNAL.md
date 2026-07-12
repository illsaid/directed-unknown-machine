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

## Runs 22–44 — Evidence provenance, applicability, assumptions, sensitivity, and threshold boundaries

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.
- **Run 41:** Left equality unresolved when a numeric threshold lacked explicit strict or inclusive comparison semantics.
- **Run 42:** Preserved conflicting strict and inclusive comparison rules for the same threshold without manufacturing precedence.
- **Run 43:** Preserved conflicting numeric thresholds for the same metric without choosing the stricter, looser, or later value.
- **Run 44:** Preserved cross-unit threshold statements as unresolved when the contract supplied no conversion or equivalence.

## Run 45 — Accept explicit cross-unit equivalence

**What changed:** Added `SCENARIOS/044-explicit-cross-unit-equivalence.md` and tightened the cross-unit brief requirement into one two-sided rule: preserve both representations, reconcile them only when the contract explicitly supplies the conversion or equivalence, and otherwise leave the gate unresolved.

**Scenario tested:** `Constraints` requires p95 latency at or below 500 milliseconds. `Success` requires p95 latency at or below 0.5 seconds. Evidence supplies a 460–490 millisecond range, paid conversion of 23%, and an explicit statement that 500 milliseconds and 0.5 seconds are equivalent representations of the same threshold.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario still maps `partial` to `hold-but-improve` and recommends fixing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/044-explicit-cross-unit-equivalence.md` preserves all four fields and now explicitly permits reconciliation from the supplied equivalence statement. The conversion and latency gates are satisfied, so rollout follows from the supplied success rule.

**What was removed or rejected:** The prior cross-unit requirement was replaced rather than supplemented, avoiding another accumulated prose rule. No unit converter, numeric normalizer, threshold parser, semantic equivalence detector, calculator, fifth field, configuration, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The trust boundary is not “never reconcile.” It is “never reconcile invisibly.” Operator-supplied equivalence is sufficient because it makes the transformation inspectable while leaving the executable free of domain conversion logic.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The hypothesis survived. The next test is an explicit precedence rule between genuinely different numeric thresholds.