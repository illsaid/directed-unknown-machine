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

## Runs 22–85 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

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
- **Run 77:** Shortened the Boundary: apply invariant while retaining whole-range handling, explicit equality semantics, and the no-comparator refusal boundary.
- **Run 78:** Shortened Decision: judge gates while preserving independent statuses, supplied evidence, and blocking effects.
- **Run 79:** Shortened Decision: recommend while preserving one authorized action and explicit identification of the governing rule branch.
- **Run 80:** Named the `Success` field directly in the recommendation invariant while preserving one-action and branch-traceability boundaries.
- **Run 81:** Removed the standalone reasoning-sequence line after the six ordered headings proved sufficient to carry the audit path.
- **Run 82:** Removed the generic `Brief requirements` wrapper after the six audit headings proved sufficient to identify the requirement sequence.
- **Run 83:** Removed the generic opening title after the contract check and explicit fields proved sufficient to identify the artifact.
- **Run 84:** Tightened the complete-contract postcondition after missing-field validation proved to carry the refusal boundary.
- **Run 85:** Corrected partial-contract repair wording so it names only the validated missing-field defect.

## Run 86 — Make one repair path exact for zero or partial labels

**What changed:** Added `SCENARIOS/085-unlabeled-contract-repair.md`. Replaced the repair preamble `cannot preserve the decision contract; add these missing explicit fields without rewriting the notes:` with `contract incomplete; add the missing explicit fields without rewriting the notes:`. Updated the prior partial-contract scenario so it remains an active regression. Missing-field detection, label order, the four-field schema, complete-contract output, six audit operations, and all decision rules remain unchanged.

**Scenario tested:** A concrete rollout decision is supplied entirely as ordinary prose with no explicit contract labels. The observable requirement is one repair path that requests `Decision:`, `Evidence:`, `Constraints:`, and `Success:` in schema order without classifying the prose, inferring field contents, recommending an action, or adding a separate unlabeled-input mode.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/085-unlabeled-contract-repair.md` was mentally simulated: unsupported-label detection returns none, all four values remain absent, and the existing missing-field path exits with the direct incomplete-contract line followed by all four labels. The updated partial-contract regression still requests only `Success:`.

**What was removed or rejected:** Removed the indirect consequence phrase `cannot preserve the decision contract` and the demonstrative `these`. Rejected separate repair modes, automatic sentence classification, field inference, schema expansion, and changes to the six audit requirements. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The parser establishes one fact for both zero-label and partial-label inputs: the contract is incomplete. Naming that state is more exact than describing a downstream preservation failure, and one missing-field path remains sufficient across both cases.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether repair output can lead directly with the missing labels and remove the remaining generic diagnosis without making refusal less clear. `WHAT_THIS_IS_FOR.md` was not rewritten because its July 13 rewrite remains within 24 hours.