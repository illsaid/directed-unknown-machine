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

## Runs 22–36 — Evidence provenance, applicability, assumptions, and sensitivity

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.

## Run 37 — Honor an explicitly inclusive threshold

**What changed:** Added `SCENARIOS/036-inclusive-threshold-touch.md` and added one requirement to `decision_brief.py`: when a supported range touches a threshold exactly, equality must be judged from the comparison wording supplied in the contract rather than from an assumed strict or inclusive boundary.

**Scenario tested:** An auditable adjustment produced a supported p95 latency range of 480–500 milliseconds. The constraint required performance “at or below 500 milliseconds,” and paid conversion was 23% against a 20% minimum.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario still maps `partial` to `hold-but-improve` and recommends fixing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/036-inclusive-threshold-touch.md` preserves all four fields and now requires the explicit inclusive wording to govern equality. Because the full range is at or below 500 milliseconds and conversion is 23%, rollout is supported.

**What was removed or rejected:** No threshold parser, comparator, calculator, fifth field, configuration, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Boundary equality is not intrinsically passing or failing. The operator’s supplied comparison rule is part of the decision contract and must remain authoritative.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The next test is the strict counterpart: a range ending exactly at 500 milliseconds under a requirement strictly below 500.