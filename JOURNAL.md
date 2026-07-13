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

## Runs 22–57 — Evidence provenance, applicability, assumptions, sensitivity, threshold boundaries, and requirement simplification

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

## Run 58 — Consolidate evidence status and interpretation conflict

**What changed:** Added `SCENARIOS/057-consolidated-evidence-interpretation.md`. In `decision_brief.py`, replaced the separate evidence-status and conflicting-interpretation bullets with one requirement that preserves observations, interpretations, assumptions, and gaps as distinct statuses; compares rival interpretations only against supplied observations; leaves unsupported conflict explicit; and names the evidence that would distinguish it.

**Scenario tested:** Checkout abandonment was observed at 12%. The growth lead interpreted confusing copy as the cause; the engineering lead interpreted latency as the cause; the operator assumed returning users would adapt. No step-level abandonment breakdown or response-time correlation was supplied. The decision was whether to rewrite copy, prioritize latency work, or run another diagnostic.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes from the current parser and recorded scenario behavior. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. `python decision_brief.py SCENARIOS/057-consolidated-evidence-interpretation.md` was mentally simulated after the change: all four labels parse unchanged; the 12% abandonment remains an observation; confusing copy and latency remain rival interpretations; adaptation remains an assumption; the causal gap remains unresolved; the requirement names step-level abandonment and response-time correlation as distinguishing evidence; and another diagnostic remains the supported recommendation.

**What was removed or rejected:** Removed one duplicated Decision bullet by folding statement-status preservation and conflicting-interpretation handling into one observation-governed invariant. No classifier, causal model, recommender, schema field, configuration, domain mode, or dashboard was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Evidence status and interpretation conflict are not separate concerns. Both enforce the same trust boundary: a supplied claim may gain decision weight only through supplied observations, while unsupported interpretations and assumptions remain visible but unresolved.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The hypothesis survived. The next test is to inspect whether the two Applicability and adjustment requirements are genuinely separate invariants or can be consolidated without allowing source exclusion and value adjustment to blur together.
