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

## Runs 22–146 — Evidence, boundaries, sequencing, repair grammar, and branch authority

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–87:** Consolidated and ordered six audit operations, then removed duplicate framing.
- **Runs 88–111:** Tightened field repair, explicit-label grammar, ambiguity handling, duplicate refusal, and multiline preservation.
- **Runs 112–126:** Established gate-to-branch accounting, branch-local blocking, nested and non-nested branch authority, conditional precedence, and scope-aware applicability.
- **Runs 127–140:** Established fallback triggers and gates, explicit evidence reuse, duration scope composition, conflict preservation, and the distinction between unavailable and unresolved fallback branches.
- **Runs 141–143:** Kept fallback failures local, refused arbitrary selection between satisfied non-nested branches, and required applied precedence authority to remain visible.
- **Run 144:** Preserved opposing precedence policies and withheld branch authority when no supplied governance rule established which policy controlled.
- **Run 145:** Required the full governance-to-precedence authority trace when supplied governance validly resolves a policy conflict.
- **Run 146:** Confirmed that governance authority cannot be borrowed outside its explicit scope.

## Run 147 — Honor an explicit exception inside otherwise applicable governance

**What changed:** Added `SCENARIOS/145-governance-exception-blocks-precedence.md` and tightened the recommendation obligation in `decision_brief.py`: a governance rule governs only when the target is inside its stated scope and outside every explicit exception. An applicable exception must remain visible and leaves the underlying precedence conflict unresolved.

**Scenario tested:** Specimen batch B-261 violated its release-temperature gate. Local reprocessing and salvage shipment were independently fully satisfied. DP-9 and NT-3 supplied opposite precedence. QG-4 generally established that DP-9 controls NT-3 for specimen disposition but explicitly exempted contamination-hold batches; B-261 was under contamination hold CH-11.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/145-governance-exception-blocks-precedence.md` reaches complete-contract output. Applying the tightened obligation, QG-4 remains visible but cannot govern B-261; DP-9 and NT-3 remain conflicting; both fallback branches remain satisfied candidates; branch authority remains unresolved; and hold is authorized pending governance authority covering contamination-hold batches.

**What was removed or rejected:** No dead H2 mechanism remained to remove. Rejected adding a policy parser, exception taxonomy, contamination-hold mode, or automated rule interpretation.

**What was learned:** Scope alone is insufficient when the same authority supplies explicit carve-outs. A rule can cover the general decision class yet still lack authority over the target. Exceptions must constrain authority before precedence is applied, not be treated as commentary after a branch is selected.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test supplies an exception whose applicability to the target is unresolved.