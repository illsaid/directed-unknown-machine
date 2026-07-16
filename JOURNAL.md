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

## Runs 22–149 — Evidence, boundaries, sequencing, repair grammar, and branch authority

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

## Run 150 — Preserve conflicting applicability authorities

**What changed:** Added and completed `SCENARIOS/148-conflicting-applicability-authorities.md`. Tightened the recommendation obligation in `decision_brief.py`: when supplied applicability authorities select opposite evidence sources, preserve every authority and affected source, leave the applicability result and every downstream authority unresolved, and identify the governance evidence required to select among those authorities.

**Scenario tested:** Specimen batch B-276 violated its release-temperature gate. Local reprocessing and salvage shipment were independently fully satisfied. DP-9 and NT-3 supplied opposite fallback precedence. QG-4 made DP-9 controlling unless the batch was under contamination hold. CH-19 said B-276 remained under hold; CR-11 said it was cleared. AR-6 selected CR-11, while AR-9 selected CH-19, and no supplied rule established which applicability authority controlled.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/148-conflicting-applicability-authorities.md` reaches complete-contract output. Applying the tightened obligation, AR-6, AR-9, CH-19, and CR-11 remain visible; current hold status remains unresolved; QG-4 cannot govern; DP-9 and NT-3 remain conflicting; both fallback branches remain satisfied candidates; branch authority remains unresolved; and hold is authorized pending governance evidence selecting the governing applicability rule.

**What was removed or rejected:** No dead H2 mechanism remained to remove. Rejected a source-rank table, automatic recency comparison, laboratory-specific applicability mode, and semantic policy parser. None is needed to preserve the authority boundary.

**What was learned:** Applicability authority is itself subject to the same non-borrowing rule as evidence, precedence, and governance. A rule that selects evidence cannot silently outrank an opposing rule that selects different evidence. Without supplied authority over the authority conflict, every downstream conclusion depending on the selected evidence must remain unresolved.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test supplies governance that explicitly selects one of the conflicting applicability authorities and checks whether the complete authority chain and displaced sources remain visible.