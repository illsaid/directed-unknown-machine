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

## Runs 22–60 — Evidence provenance, applicability, assumptions, sensitivity, threshold boundaries, and requirement simplification

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
- **Run 59:** Consolidated source exclusion and value adjustment into one applicability-transformation invariant while preserving their distinct support requirements.
- **Run 60:** Consolidated explicit threshold semantics and the no-comparator refusal boundary into one supplied-wording invariant.

## Run 61 — Consolidate threshold-conflict governance

**What changed:** Added `SCENARIOS/060-consolidated-threshold-conflict-governance.md`. In `decision_brief.py`, replaced three Threshold conflict bullets with one exact-reconciliation-support invariant. It preserves every conflicting rule, permits precedence only while preserving displaced rules and separate results, permits cross-unit reconciliation only from supplied conversion or equivalence, and forbids support for one path from substituting for the other.

**Scenario tested:** Paid conversion was 21% against a contextual minimum of 20% and a governing minimum of 22%, with explicit precedence supplied for the 22% rule. P95 latency was 480 milliseconds against thresholds written as below 500 milliseconds and below 0.5 seconds, with no supplied equivalence or conversion.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes from the current parser and recorded scenario behavior. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. `python decision_brief.py SCENARIOS/060-consolidated-threshold-conflict-governance.md` was mentally simulated after the change: all four labels parse unchanged; the supplied precedence governs conversion while both thresholds and outcomes remain visible; 21% violates the governing 22% rule; latency remains unresolved because precedence does not supply cross-unit equivalence; delay remains the governed recommendation.

**What was removed or rejected:** Removed two Threshold conflict bullets by folding unresolved conflict, explicit precedence, and cross-unit equivalence into one preservation-and-exact-support rule with distinct branches. No threshold parser, unit converter, precedence engine, semantic classifier, schema field, configuration, domain mode, or dashboard was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Precedence and equivalence are not interchangeable mechanisms, but both are instances of one stricter boundary: conflict resolution is valid only when the contract supplies support for the exact reconciliation applied. Consolidation is safe only when displaced same-metric rules remain visible and cross-unit statements still refuse unsupplied normalization.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The hypothesis survived. The next test is to inspect whether the seven requirement-group labels still represent distinct audit questions or whether any adjacent groups can be merged without hiding a decision boundary.
