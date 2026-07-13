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

## Runs 22–65 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.
- **Run 41:** Left equality unresolved when a numeric threshold lacked explicit strict or inclusive comparison semantics.
- **Runs 42–46:** Preserved conflicting comparators, numeric thresholds, and cross-unit statements; accepted reconciliation only when explicit equivalence or precedence was supplied.
- **Runs 47–58:** Grouped and consolidated accumulated decision, gate, provenance, applicability, sensitivity, equality, and interpretation obligations without weakening established boundaries.
- **Run 59:** Consolidated source exclusion and value adjustment into one applicability-transformation invariant while preserving distinct support requirements.
- **Run 60:** Consolidated explicit threshold semantics and the no-comparator refusal boundary into one supplied-wording invariant.
- **Run 61:** Consolidated unresolved threshold conflicts, explicit precedence, and cross-unit equivalence into one exact-reconciliation-support invariant.
- **Run 62:** Merged sensitivity and threshold semantics into one Boundary evaluation group while retaining full-range and equality rules.
- **Run 63:** Kept Boundary evaluation and Boundary reconciliation separate and renamed the latter to identify the audit operation rather than the input condition.
- **Run 64:** Kept Governed recommendation and Gate judgments separate and renamed the former to identify action selection under the supplied success rule.
- **Run 65:** Kept Evidence provenance and Evidence transformation separate and renamed the latter to identify the operation that changes how preserved evidence applies.

## Run 66 — Order the six audit operations as a visible reasoning sequence

**What changed:** Added `SCENARIOS/065-visible-reasoning-sequence.md`. Reordered the unchanged `REQUIREMENT_GROUPS` in `decision_brief.py` to print Evidence provenance, Evidence transformation, Boundary reconciliation, Boundary evaluation, Gate judgments, and Governed recommendation. No requirement text, parser behavior, field, or decision rule changed.

**Scenario tested:** Production report A supplies conversion at 23% and latency at 540 milliseconds. A browser-segment table preserves the original latency and supplies the target mix plus arithmetic yielding an adjusted 480 millisecond estimate. The success contract explicitly requires source recording, transformation audit, boundary handling, gate judgments, and only then the final recommendation. The supported adjustment leaves conversion and latency satisfied, so the governed recommendation is rollout.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes from the unchanged historical harness: `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. `python decision_brief.py SCENARIOS/065-visible-reasoning-sequence.md` was mentally simulated after the change: all four labels parse unchanged and the six existing groups print in the scenario's required dependency order.

**What was removed or rejected:** Removed no obligation and added no feature. Rejected merging any groups because Runs 63–65 established that boundary application versus reconciliation, gate judgment versus recommendation, and source record versus transformation are distinct operations. No classifier, decision engine, converter, mode, configuration, or dashboard was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Ordering alone materially improves specificity. The output now reads as an audit trail: preserve the record, authorize transformations, determine the governing boundary, apply evidence to it, judge each gate, and select the governed action. The remaining structural defect is that evidence-status handling still sits inside the final recommendation group even though it may belong nearer the source record.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether observation, interpretation, assumption, and unresolved-gap statuses should move from Governed recommendation to Evidence provenance without broadening provenance beyond the supplied record.
