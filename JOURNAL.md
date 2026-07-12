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

## Runs 22–40 — Evidence provenance, applicability, assumptions, sensitivity, and threshold boundaries

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.

## Run 41 — Leave equality unresolved when comparison semantics are missing

**What changed:** Added `SCENARIOS/040-threshold-without-comparator.md` and added one executable brief requirement: when a numeric threshold is supplied without explicit strict or inclusive comparison wording, equality cannot resolve the gate and must remain unresolved rather than inheriting an unstated convention.

**Scenario tested:** An auditable estimate produced a supported paid-conversion range of 20%–24%, whose lower bound exactly equals a stated “20% threshold.” The notes say conversion must “meet” that threshold but do not say whether equality is accepted. The supported p95 latency range was 460–490 milliseconds against an inclusive maximum of 500 milliseconds.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario still maps `partial` to `hold-but-improve` and recommends fixing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/040-threshold-without-comparator.md` preserves all four fields and now explicitly requires the equality case to remain unresolved when comparison semantics are absent. The latency gate is satisfied, but the conversion gate is unresolved, so rollout is not supported and delay follows from the supplied success rule.

**What was removed or rejected:** No threshold parser, comparator, semantic classifier, calculator, fifth field, configuration, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** A number is not a complete decision boundary. When evidence touches equality, the operator must supply the comparison semantics; otherwise the system should expose the missing rule rather than manufacture one.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The next test is conflicting strict and inclusive comparison wording for the same threshold, verifying that the conflict remains explicit rather than selecting one rule.
