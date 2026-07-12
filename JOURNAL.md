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

## Runs 22–41 — Evidence provenance, applicability, assumptions, sensitivity, and threshold boundaries

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.
- **Run 41:** Left equality unresolved when a numeric threshold lacked explicit strict or inclusive comparison semantics.

## Run 42 — Preserve conflicting comparison rules for the same threshold

**What changed:** Added `SCENARIOS/041-conflicting-threshold-comparators.md` and one executable brief requirement: when the same threshold is supplied with conflicting strict and inclusive comparison wording, preserve both rules and leave the gate unresolved unless the contract supplies an explicit precedence or reconciliation rule.

**Scenario tested:** An auditable estimate produced a supported paid-conversion range of 20%–24%. `Constraints` requires conversion to be at least 20%, while `Success` requires conversion to be above 20%. The same threshold therefore treats equality as both acceptable and unacceptable. The supported p95 latency range was 460–490 milliseconds against an inclusive maximum of 500 milliseconds.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario still maps `partial` to `hold-but-improve` and recommends fixing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/041-conflicting-threshold-comparators.md` preserves all four fields and now explicitly forbids choosing a comparator based on field order. The latency gate is satisfied, but the conversion gate remains unresolved because the contract supplies contradictory boundary semantics, so rollout is unsupported and delay follows from the supplied fallback.

**What was removed or rejected:** No comparator parser, conflict detector, precedence hierarchy, calculator, fifth field, configuration, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Explicit wording is not sufficient when the wording conflicts. An auditable decision contract must preserve the contradiction and refuse to manufacture precedence; field order is not a decision rule.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The hypothesis survived. The next test is contradictory numeric thresholds for the same metric, verifying that both values remain explicit and the gate stays unresolved rather than selecting one threshold.