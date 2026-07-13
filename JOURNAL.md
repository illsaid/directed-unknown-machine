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

## Runs 22–76 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

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
- **Run 75:** Shortened the Evidence: transform invariant while retaining operation-specific support and non-substitution.
- **Run 76:** Shortened the Boundary: reconcile invariant while retaining precedence, equivalence, preservation, and non-substitution boundaries.

## Run 77 — Tighten boundary application without weakening range or equality semantics

**What changed:** Added `SCENARIOS/076-tightened-boundary-application.md`. Shortened only the `Boundary: apply` requirement in `decision_brief.py`. The replacement states one application rule—use the complete preserved evidence and only the supplied boundary semantics—then keeps separate compact handling for ranges and equality.

**Scenario tested:** Conversion sensitivity is 19% to 21% against an inclusive 20% minimum; latency sensitivity is 480 to 490 milliseconds against a strict 500 millisecond maximum; error rate equals an inclusive 2% maximum; churn equals a strict 5% maximum; retention equals a bare 70% threshold with no comparator. Every range must be evaluated in full, and equality must follow only explicit comparison wording.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/076-tightened-boundary-application.md` was mentally simulated: all four labels parse unchanged; the contract and six-stage sequence print intact; conversion is conditional, latency and error rate are satisfied, churn is violated, retention is unresolved, and the supplied all-gates success rule supports delay.

**What was removed or rejected:** Removed repeated application phrasing only. Rejected midpoint selection, best-case selection, treating every range as unresolved, inferring equality semantics from a bare threshold, adding a threshold parser, or adding a calculator. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Boundary application stays safe when compressed into two non-transferable instructions: evaluate the whole supplied range, and resolve equality only from supplied comparison wording. The refusal boundary is not the length of the requirement; it is refusing to select a convenient point or invent comparator semantics.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is `Decision: judge gates`, specifically whether it can be shortened without allowing an overall verdict to erase independent gate statuses, their supplied evidence, or their blocking effects.