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

## Runs 22–58 — Evidence provenance, applicability, assumptions, sensitivity, threshold boundaries, and requirement simplification

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.
- **Run 41:** Left equality unresolved when a numeric threshold lacked explicit strict or inclusive comparison semantics.
- **Run 42:** Preserved conflicting strict and inclusive comparison rules for the same threshold without manufacturing precedence.
- **Run 43:** Preserved conflicting numeric thresholds for the same metric without choosing the stricter, looser, or later value.
- **Runs 44–45:** Preserved cross-unit statements when equivalence was absent and accepted reconciliation only when the contract explicitly supplied equivalence.
- **Run 46:** Accepted explicit threshold precedence while preserving the displaced threshold and its separate result.
- **Run 47:** Grouped the accumulated obligations under seven inspectable requirement labels without weakening the precedence boundary.
- **Run 48:** Consolidated four equality clauses into one supplied-strictness rule without weakening inclusive or strict minimum and maximum boundaries.
- **Run 49:** Consolidated comparator and numeric threshold conflicts into one preservation-and-no-inference rule.
- **Run 50:** Consolidated source identification and overlapping coverage into one source-to-measurement provenance rule.
- **Run 51:** Consolidated adjustment context, method auditability, and assumption support into one adjustment-auditability rule.
- **Run 52:** Consolidated source exclusion into one observed-mismatch-plus-relevance rule.
- **Run 53:** Consolidated sensitivity handling into one full-range rule covering crossing and same-side ranges.
- **Run 54:** Consolidated evidence status and interpretation conflict handling without weakening the no-promotion boundary.
- **Run 55:** Consolidated gate judgments without weakening independent-gate visibility or recommendation blocking.
- **Run 56:** Consolidated evidence provenance without weakening overlap handling or disagreement visibility.
- **Run 57:** Consolidated recommendation selection and supplied fallback governance into one Decision invariant.
- **Run 58:** Consolidated evidence-status preservation and observation-only interpretation handling into one Decision invariant.

## Run 59 — Consolidate applicability transformations

**What changed:** Added `SCENARIOS/058-consolidated-applicability-transforms.md`. In `decision_brief.py`, replaced the separate source-exclusion and value-adjustment bullets with one applicability-transformation requirement. It preserves every original value, requires supplied support specific to the transformation used, and explicitly prevents evidence sufficient for exclusion from substituting for adjustment support or vice versa.

**Scenario tested:** Paid conversion was 23%. Mobile Canary A reported 560 milliseconds from traffic that was 95% native-app, and the contract explicitly placed native-app telemetry outside the target US web population. Web Canary B reported 540 milliseconds from a 70% Safari and 30% Chrome sample, supplied 600/400-millisecond segment values, and supplied a production target mix of 40% Safari and 60% Chrome, producing an auditable 480-millisecond reweighted estimate.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes from the current parser and recorded scenario behavior. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. `python decision_brief.py SCENARIOS/058-consolidated-applicability-transforms.md` was mentally simulated after the change: all four labels parse unchanged; Canary A's original value remains visible and exclusion is supported by both mismatch and relevance; Canary B's original and adjusted values remain visible and the supplied segment arithmetic resolves the target-population estimate; conversion and latency gates are satisfied; rollout remains the governed recommendation.

**What was removed or rejected:** Removed one duplicated Applicability and adjustment bullet by folding exclusion and adjustment into one preservation-and-transformation-support invariant with distinct branches. No source classifier, reweighting engine, applicability model, schema field, configuration, domain mode, or dashboard was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Source exclusion and value adjustment are not interchangeable, but they do share one governing boundary: preserve the original evidence and require supplied support for the exact transformation applied. A single invariant can express that boundary only when it keeps the two support tests explicit.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The hypothesis survived. The next test is to inspect whether the two Threshold semantics requirements can be consolidated without letting a numeric threshold with no comparator inherit strict or inclusive meaning.