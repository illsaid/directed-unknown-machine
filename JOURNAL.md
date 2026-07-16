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

## Runs 22–150 — Evidence, boundaries, sequencing, repair grammar, and branch authority

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
- **Run 148:** Required positive supplied evidence that a target is outside every explicit exception before governance may resolve precedence.
- **Run 149:** Confirmed that supplied applicability authority can resolve conflicting exception-status evidence without an exception-specific mechanism.
- **Run 150:** Preserved conflicting applicability authorities and withheld every downstream authority when no supplied rule established which applicability authority controlled.

## Run 151 — Govern conflicting applicability authorities

**What changed:** Added and completed `SCENARIOS/149-governed-conflicting-applicability-authorities.md`. No executable change was made because the existing governance, applicability, evidence-preservation, and precedence obligations already compose to preserve the complete authority chain and displaced sources.

**Scenario tested:** Specimen batch B-281 violated its release-temperature gate. Local reprocessing and salvage shipment were independently fully satisfied. DP-9 and NT-3 supplied opposite fallback precedence. QG-4 made DP-9 controlling unless the batch was under contamination hold. CH-23 said B-281 remained under hold; CR-15 said it was cleared. AR-6 selected CR-15, AR-9 selected CH-23, and governance rule AG-2 explicitly made AR-6 controlling over AR-9 for current specimen contamination-hold status.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/149-governed-conflicting-applicability-authorities.md` reaches complete-contract output. Applying the existing obligations, AG-2 selects AR-6; AR-6 selects CR-15; AR-9 and CH-23 remain conflicting but non-governing; CR-15 establishes that B-281 is outside QG-4's exception; QG-4 selects DP-9; DP-9 authorizes local reprocessing; and NT-3 plus salvage shipment remain satisfied but non-governing.

**What was removed or rejected:** No dead H2 mechanism remained to remove. Rejected another executable sentence dedicated to governance over applicability authorities, an authority graph, source-rank machinery, and a laboratory-specific mode. The current obligations already produce the required authority trace.

**What was learned:** Governance over applicability authorities is not a new reasoning category. It is the existing governance pattern applied one level earlier in the same supplied authority chain. The useful specificity comes from preserving each selected and displaced authority and evidence source, not from adding a new abstraction for every level of authority.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test limits governance to contamination-hold status while introducing a separate release-status conflict, testing whether authority remains confined to the exact dimension it governs.