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

## Runs 22–48 — Evidence provenance, applicability, assumptions, sensitivity, threshold boundaries, and requirement simplification

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.
- **Run 41:** Left equality unresolved when a numeric threshold lacked explicit strict or inclusive comparison semantics.
- **Run 42:** Preserved conflicting strict and inclusive comparison rules for the same threshold without manufacturing precedence.
- **Run 43:** Preserved conflicting numeric thresholds for the same metric without choosing the stricter, looser, or later value.
- **Runs 44–45:** Preserved cross-unit statements when equivalence was absent and accepted reconciliation only when the contract explicitly supplied equivalence.
- **Run 46:** Accepted explicit threshold precedence while preserving the displaced threshold and its separate result.
- **Run 47:** Grouped the accumulated obligations under seven inspectable requirement labels without weakening the precedence boundary.
- **Run 48:** Consolidated four equality clauses into one supplied-strictness rule without weakening inclusive or strict minimum and maximum boundaries.

## Run 49 — Consolidate threshold-conflict semantics without weakening boundaries

**What changed:** Added `SCENARIOS/048-consolidated-threshold-conflicts.md`. In `decision_brief.py`, replaced separate conflicting-comparator, conflicting-value, and silent-choice requirements with one rule covering any conflicting threshold statements for the same metric. Explicit precedence and cross-unit handling remain separate requirements.

**Scenario tested:** One rollout contract supplies two kinds of threshold conflict. Paid conversion is 21%; `Constraints` requires at least 20%, while `Success` requires above 20%, creating conflicting equality semantics. Seven-day retention is 71%; `Constraints` requires at least 70%, while `Success` requires at least 72%, creating conflicting numeric values. Latency is 480 milliseconds against the same inclusive 500-millisecond maximum in both fields. No precedence or reconciliation rule is supplied.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes from the current parser and scenario. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. `python decision_brief.py SCENARIOS/048-consolidated-threshold-conflicts.md` was mentally simulated after the change: all four labels parse unchanged, the Threshold conflict group prints three bullets instead of five, the conversion and retention conflicts remain explicit and unresolved, latency remains satisfied, and the supplied fallback remains delay.

**What was removed or rejected:** Removed two duplicated conflict bullets and folded the no-silent-choice obligation into the consolidated rule. No conflict detector, threshold parser, comparator, calculator, schema field, configuration, domain mode, or dashboard was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Comparator disagreement and numeric-threshold disagreement share one useful invariant: preserve every supplied rule and refuse to manufacture precedence. Keeping explicit precedence and cross-unit equivalence separate preserves their distinct positive and representation boundaries while reducing audit cost.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The hypothesis survived. The next test is to inspect another requirement group for one duplicated obligation that can be removed while preserving its named scenario boundary.
