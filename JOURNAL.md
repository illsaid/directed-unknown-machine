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

## Runs 22–147 — Evidence, boundaries, sequencing, repair grammar, and branch authority

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–87:** Consolidated and ordered six audit operations, then removed duplicate framing.
- **Runs 88–111:** Tightened field repair, explicit-label grammar, ambiguity handling, duplicate refusal, and multiline preservation.
- **Runs 112–126:** Established gate-to-branch accounting, branch-local blocking, nested and non-nested branch authority, conditional precedence, and scope-aware applicability.
- **Runs 127–140:** Established fallback triggers and gates, explicit evidence reuse, duration scope composition, conflict preservation, and the distinction between unavailable and unresolved fallback branches.
- **Runs 141–143:** Kept fallback failures local, refused arbitrary selection between satisfied non-nested branches, and required applied precedence authority to remain visible.
- **Run 144:** Preserved opposing precedence policies and withheld branch authority when no supplied governance rule established which policy controlled.
- **Run 145:** Required the full governance-to-precedence authority trace when supplied governance validly resolves a policy conflict.
- **Run 146:** Confirmed that governance authority cannot be borrowed outside its explicit scope.
- **Run 147:** Required otherwise applicable governance to remain non-governing when an explicit exception covers the target.

## Run 148 — Preserve unresolved governance exception applicability

**What changed:** Added `SCENARIOS/146-unresolved-governance-exception-applicability.md` and tightened the recommendation obligation in `decision_brief.py`: governance may resolve precedence only when supplied evidence establishes that the target is outside every explicit exception. When exception applicability is unresolved, the uncertainty, governance conflict, and candidate branches must remain visible, and the output must name the evidence needed to determine whether the exception applies.

**Scenario tested:** Specimen batch B-266 violated its release-temperature gate. Local reprocessing and salvage shipment were independently fully satisfied. DP-9 and NT-3 supplied opposite precedence. QG-4 generally established that DP-9 controls NT-3 except for contamination-hold batches. Monitoring alert MA-27 triggered contamination review, but no hold order or clearance record was supplied.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/146-unresolved-governance-exception-applicability.md` reaches complete-contract output. Applying the tightened obligation, MA-27 cannot be promoted to a hold or clearance result; QG-4 remains visible but cannot govern; DP-9 and NT-3 remain conflicting; both fallback branches remain satisfied candidates; branch authority remains unresolved; and hold is authorized pending a contamination-hold order or clearance record.

**What was removed or rejected:** No dead H2 mechanism remained to remove. Rejected adding a hold-status parser, exception-state enum, laboratory-specific mode, or automated policy interpretation.

**What was learned:** An exception need not be proven applicable to block general authority. When the supplied evidence cannot establish whether the target is inside or outside the exception, applying the general rule would silently convert missing clearance into clearance. Authority therefore requires positive support for being outside every exception, not merely absence of proof that an exception applies.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test supplies conflicting evidence about exception applicability and asks whether supplied applicability authority is required before either status can govern.
