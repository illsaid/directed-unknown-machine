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

## Runs 22–68 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

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
- **Run 66:** Ordered the six unchanged audit groups into dependency order from source record through governed action.
- **Run 67:** Moved evidence-status preservation from Governed recommendation to Evidence provenance so supplied claim status is fixed before downstream reasoning.
- **Run 68:** Consolidated source mapping and claim-status preservation into one immutable Evidence provenance invariant.

## Run 69 — Consolidate boundary evaluation into one application invariant

**What changed:** Added `SCENARIOS/068-consolidated-boundary-evaluation.md`. Replaced the two adjacent Boundary evaluation requirements in `decision_brief.py` with one requirement covering complete-range application, threshold-crossing conditionality, same-side range resolution, explicit strict and inclusive equality semantics, and the no-comparator refusal boundary. No parser behavior, field, group, decision rule, classifier, transformation, or mode changed.

**Scenario tested:** Paid conversion is exactly 20% against an inclusive minimum of at least 20%; p95 latency is estimated at 480–520 milliseconds against a strict maximum below 500 milliseconds; retention is exactly 70% against a bare 70% threshold with no comparator. The combined invariant must satisfy conversion, preserve a conditional latency result across the range, leave retention unresolved, and support delay because not every gate clears.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/068-consolidated-boundary-evaluation.md` was mentally simulated: all four labels parse unchanged; Boundary evaluation prints one combined requirement; the other five groups retain their order and wording; conversion equality satisfies the inclusive boundary, the latency range remains conditional across the strict threshold, retention equality remains unresolved without comparator wording, and the governed recommendation remains delay.

**What was removed or rejected:** Removed one duplicate requirement boundary rather than adding a new audit operation. Added no threshold parser, range calculator, semantic classifier, unit converter, configuration, or dashboard. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Range position and equality are both cases of one operation: apply all supplied evidence to the governing boundary exactly as written. They can share one invariant as long as the wording preserves complete-range evaluation, conditional outcomes at crossings, explicit comparator semantics, and refusal to infer equality behavior from a bare number.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether Boundary reconciliation and Boundary evaluation can use a shorter shared vocabulary without merging their distinct operations or weakening either refusal boundary.