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

## Runs 22–74 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

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
- **Run 71:** Renamed the two evidence stages to `Evidence: preserve` and `Evidence: transform` so preservation visibly precedes any supported transformation.
- **Run 72:** Renamed the two final stages to `Decision: judge gates` and `Decision: recommend`, completing three visibly ordered pairs.
- **Run 73:** Printed the complete six-stage reasoning sequence once before the detailed requirements.
- **Run 74:** Shortened the Evidence: preserve invariant while retaining all tested source-record refusal boundaries.

## Run 75 — Tighten evidence transformation without cross-authorizing operations

**What changed:** Added `SCENARIOS/074-tightened-evidence-transformation.md`. Shortened only the `Evidence: transform` requirement in `decision_brief.py`. The replacement states the shared rule once—support must match the exact transformation—then keeps separate minimum evidence for source exclusion and value adjustment, preservation of originals, the non-substitution rule, and conditional treatment of unsupported assumptions.

**Scenario tested:** Production report A supplies 23% conversion and 540 millisecond latency for the target customer population. Canary B supplies 410 milliseconds for employees, with supplied environment evidence showing that an employee-only authentication cache makes it non-applicable to customers. A browser table supports the arithmetic behind a proposed 480 millisecond adjustment, but no supplied source supports the governing 60/40 desktop-mobile traffic mix. The valid exclusion evidence must not authorize the adjustment.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/074-tightened-evidence-transformation.md` was mentally simulated: all four labels parse unchanged; the contract and six-stage sequence print intact; Canary B has operation-specific support for exclusion; the 480 millisecond adjustment remains conditional because its traffic-share assumption is unsupported; the latency gate therefore does not clear; and the supplied success rule supports delay plus collection of production traffic-share evidence.

**What was removed or rejected:** Removed repeated transformation phrasing only. Rejected combining exclusion and adjustment into one generic applicability test, allowing one operation's support to authorize the other, adding a weighting calculator, inferring production mix, changing parser behavior, or adding another mode. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The transformation boundary remains intact when expressed as one exact-operation support rule followed by two compact operation-specific tests. The key refusal is not verbosity; it is preventing applicability evidence from laundering an unsupported adjusted value, and preventing adjustment arithmetic from erasing a source without applicability evidence.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is `Boundary: reconcile`, specifically whether it can be shortened without allowing precedence support to substitute for equivalence support or vice versa.
