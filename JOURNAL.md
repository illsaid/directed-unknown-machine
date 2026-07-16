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

## Runs 22–151 — Evidence, boundaries, sequencing, repair grammar, and branch authority

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
- **Run 151:** Confirmed that supplied governance can select one applicability authority while retaining the complete selected and displaced authority chain.

## Run 152 — Confine governance to the named status dimension

**What changed:** Added and completed `SCENARIOS/150-governed-one-status-unresolved-other-status.md`. Tightened `decision_brief.py` so governance selecting an applicability authority governs only the exact status, metric, period, population, or other dimension it explicitly names. Separate conflicts outside that dimension must remain unresolved.

**Scenario tested:** Specimen batch B-286 violated its release-temperature gate. Local reprocessing and salvage shipment otherwise qualified. DP-9 and NT-3 supplied opposite fallback precedence. QG-4 made DP-9 controlling only when neither contamination hold nor release hold applied. CH-28 and CR-20 conflicted on contamination status; AR-6 and AR-9 selected opposite records; AG-2 made AR-6 controlling for contamination-hold status only. RH-7 and RR-4 separately conflicted on release-hold status, with no supplied applicability authority.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/150-governed-one-status-unresolved-other-status.md` reaches complete-contract output. Applying the tightened obligation, AG-2 selects AR-6 and CR-20 for contamination-hold status only; AR-9 and CH-28 remain conflicting but non-governing on that dimension. RH-7 and RR-4 remain independently conflicting; QG-4 exception applicability remains unresolved; DP-9 and NT-3 remain conflicting; neither fallback receives authority; and hold is authorized pending release-status applicability authority.

**What was removed or rejected:** No dead H2 mechanism remained to remove. Rejected a general authority graph, automatic status taxonomy, laboratory-specific hold logic, and cross-status inheritance. One scope sentence is sufficient for the named scenario.

**What was learned:** Authority scope is dimensional, not merely source-specific. Resolving who governs one status does not authorize that source or governance rule to settle another status concerning the same target. The compiler is becoming specifically useful at preventing authority-chain results from leaking sideways into adjacent unresolved questions.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test supplies governance naming two status dimensions while omitting a third, testing whether enumerated scope remains closed.