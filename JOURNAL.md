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

## Runs 22–144 — Evidence, boundaries, sequencing, repair grammar, and branch authority

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–87:** Consolidated and ordered six audit operations, then removed duplicate framing.
- **Runs 88–111:** Tightened field repair, explicit-label grammar, ambiguity handling, duplicate refusal, and multiline preservation.
- **Runs 112–126:** Established gate-to-branch accounting, branch-local blocking, nested and non-nested branch authority, conditional precedence, and scope-aware applicability.
- **Runs 127–140:** Established fallback triggers and gates, explicit evidence reuse, duration scope composition, conflict preservation, and the distinction between unavailable and unresolved fallback branches.
- **Runs 141–143:** Kept fallback failures local, refused arbitrary selection between satisfied non-nested branches, and required applied precedence authority to remain visible.
- **Run 144:** Preserved opposing precedence policies and withheld branch authority when no supplied governance rule established which policy controlled.

## Run 145 — Preserve the full governed-precedence authority trace

**What changed:** Added `SCENARIOS/143-governed-conflicting-fallback-precedence.md` and strengthened the final recommendation obligation. When supplied governance resolves conflicting precedence authorities, the compiler must cite both the governance rule and selected precedence policy, preserve displaced policies as conflicting but non-governing, and preserve displaced fully satisfied branches as satisfied but non-governing.

**Scenario tested:** Specimen batch B-251 violated its release-temperature gate. Local reprocessing and salvage shipment were independently fully satisfied. DP-9 gave local reprocessing precedence; NT-3 gave salvage shipment precedence. Governance rule QG-2 explicitly established that DP-9 controls NT-3 for this on-site disposition.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/143-governed-conflicting-fallback-precedence.md` reaches complete-contract output. Under the strengthened obligation, local reprocessing governs; QG-2 and DP-9 remain visible as the authority chain; NT-3 remains conflicting but non-governing; and salvage shipment remains satisfied but non-governing.

**What was removed or rejected:** No dead H2 mechanism remained to remove. Rejected automatic policy ranking, policy-name heuristics, a governance parser, and laboratory-specific disposition logic.

**What was learned:** Correct branch selection is not enough. A governance-resolved decision is auditable only when the output preserves the full chain from governance rule to selected precedence policy and retains the displaced conflicting authority rather than silently erasing it.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test supplies a governance rule whose scope does not cover the target disposition, testing whether the compiler refuses to borrow authority across scope.