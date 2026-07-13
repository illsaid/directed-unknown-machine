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

## Runs 22–70 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

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
- **Run 69:** Consolidated full-range and equality handling into one Boundary evaluation invariant.
- **Run 70:** Renamed the two boundary stages to `Boundary: reconcile` and `Boundary: apply` so their dependency is visible without merging them.

## Run 71 — Make the two evidence stages visibly sequential

**What changed:** Added `SCENARIOS/070-evidence-preserve-then-transform.md`. Renamed only the executable headings `Evidence provenance` and `Evidence transformation` to `Evidence: preserve` and `Evidence: transform`. Requirement text, group order, parser behavior, fields, and decision rules are unchanged.

**Scenario tested:** Report A records paid conversion at 23% and p95 latency at 540 milliseconds. A supplied browser-segment table records 60% desktop traffic at 450 milliseconds and 40% mobile-web traffic at 525 milliseconds, with an explicitly matching production mix and auditable weighted estimate of 480 milliseconds. The first evidence stage must preserve every original source and value; the second may apply only the supported adjustment. Conversion and adjusted latency both satisfy their gates, so the governed recommendation is rollout.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/070-evidence-preserve-then-transform.md` was mentally simulated: all four labels parse unchanged; the six groups retain their dependency order; the evidence headings print as `Evidence: preserve` followed by `Evidence: transform`; their unchanged requirements retain every original value and authorize the 480 millisecond adjustment only from the supplied method, target population, weights, and assumption support; the supported recommendation is rollout.

**What was removed or rejected:** Rejected merging evidence preservation with transformation and rejected renaming the remaining recommendation stages without scenario evidence. Added no parser, classifier, calculator, adjustment engine, mode, configuration, or dashboard. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The same shared-prefix grammar that clarified boundary handling also clarifies evidence handling. `Evidence: preserve` fixes the immutable source record; `Evidence: transform` permits only supported changes in how that record applies. The sequence is easier to scan while the prohibition on unsupported exclusion or opaque adjustment remains intact.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether `Gate judgments` and `Governed recommendation` create a comparable sequencing ambiguity; no further heading change is justified without a named scenario.
