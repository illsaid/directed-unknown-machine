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

## Runs 22–69 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

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

## Run 70 — Make the two boundary stages visibly sequential

**What changed:** Added `SCENARIOS/069-boundary-reconcile-then-apply.md`. Renamed only the executable headings `Boundary reconciliation` and `Boundary evaluation` to `Boundary: reconcile` and `Boundary: apply`. Requirement text, group order, parser behavior, fields, and decision rules are unchanged.

**Scenario tested:** Paid conversion is 21% against two conflicting inclusive minimums, 20% and 22%, with explicit charter precedence for 22%. P95 latency is 480 milliseconds against a strict maximum below 500 milliseconds. The first boundary stage must preserve both conversion rules and reconcile the governing boundary to 22%; the second must apply the supplied evidence, producing violated conversion and satisfied latency gates; the governed recommendation must be delay because every gate must clear.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/069-boundary-reconcile-then-apply.md` was mentally simulated: all four labels parse unchanged; the six groups retain their dependency order; the two boundary headings print as `Boundary: reconcile` followed by `Boundary: apply`; their unchanged requirements preserve the supplied precedence, displaced threshold, and separate gate results; the supported recommendation remains delay.

**What was removed or rejected:** Rejected merging the two boundary stages and rejected broad operation-first renaming across all six groups. The scenario demonstrated one local sequencing ambiguity, so only the two implicated headings changed. Added no parser, classifier, calculator, unit converter, mode, configuration, or dashboard. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** A shared noun prefix plus distinct imperative verbs makes the dependency visible without collapsing the operations. `Boundary: reconcile` establishes which supplied rule governs; `Boundary: apply` evaluates evidence against that rule. The shorter vocabulary improves scanability while preserving the refusal to infer either reconciliation support or comparison semantics.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether any remaining audit heading creates a concrete sequencing ambiguity; no further renaming is justified without a named scenario.
