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

## Runs 22–37 — Evidence provenance, applicability, assumptions, sensitivity, and threshold boundaries

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Run 37:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording.

## Run 38 — Treat equality as failure under a strict maximum

**What changed:** Added `SCENARIOS/037-strict-threshold-touch.md` and added one executable brief requirement: under a strict maximum such as “below” or “strictly below,” equality violates the gate rather than leaving it unresolved.

**Scenario tested:** An auditable adjustment produced a supported p95 latency range of 480–500 milliseconds. The constraint required performance strictly below 500 milliseconds, and paid conversion was 23% against a 20% minimum.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario still maps `partial` to `hold-but-improve` and recommends fixing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/037-strict-threshold-touch.md` preserves all four fields and now explicitly requires equality under the strict maximum to count as a violation. Because the supported range includes 500 milliseconds, the performance gate fails and delay is supported despite conversion clearing its gate.

**What was removed or rejected:** No threshold parser, comparator, calculator, fifth field, configuration, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The contract's comparison operator determines the boundary result. A value equal to a strict maximum is decisive contrary evidence, not an unresolved edge case.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The next test is the mirrored minimum boundary: a supported range whose lower bound equals a threshold stated as “at least.”