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

## Runs 22–143 — Evidence, boundaries, sequencing, repair grammar, and branch authority

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–87:** Consolidated and ordered six audit operations, then removed duplicate framing.
- **Runs 88–111:** Tightened field repair, explicit-label grammar, ambiguity handling, duplicate refusal, and multiline preservation.
- **Runs 112–126:** Established gate-to-branch accounting, branch-local blocking, nested and non-nested branch authority, conditional precedence, and scope-aware applicability.
- **Runs 127–140:** Established fallback triggers and gates, explicit evidence reuse, duration scope composition, conflict preservation, and the distinction between unavailable and unresolved fallback branches.
- **Run 141:** Kept fallback failure branch-local so a failed emergency-transfer branch could not suppress an independently satisfied salvage-shipment branch.
- **Run 142:** Verified that two fully satisfied non-nested fallback branches remain unresolved when no precedence or tie-breaker is supplied.
- **Run 143:** Required an applied unconditional precedence rule to remain visible in the governing recommendation.

## Run 144 — Preserve conflicting explicit precedence authorities

**What changed:** Added `SCENARIOS/142-conflicting-explicit-fallback-precedence.md` and strengthened the final recommendation obligation. When supplied precedence authorities conflict, the compiler must now preserve every conflicting rule and leave branch authority unresolved unless supplied applicability or governance evidence establishes which precedence source governs. It may not choose by field order, policy name, or convenience.

**Scenario tested:** Specimen batch B-248 violated its release-temperature gate. Local reprocessing and salvage shipment were independently fully satisfied. Laboratory disposition policy DP-9 gave local reprocessing precedence, while network transport policy NT-3 gave salvage shipment precedence. No supplied rule established which policy controlled.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/142-conflicting-explicit-fallback-precedence.md` reaches complete-contract output. Under the strengthened recommendation obligation, both precedence policies remain visible, both fallback branches remain satisfied candidates, branch authority remains unresolved, and the supplied hold action governs until a governance rule establishes which policy controls.

**What was removed or rejected:** Rejected automatic policy ranking, policy-name heuristics, a precedence parser, and laboratory-specific disposition logic. Historical H2 evidence in `HYPOTHESES.md` was compacted into run ranges so the new authority boundary remains inspectable without extending a near-line-by-line chronology.

**What was learned:** Citation alone does not make precedence auditable. A downstream analyst can still cite one supplied policy and omit an equally explicit opposing policy. Authority is established only when the supplied record resolves which precedence source governs.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test supplies an explicit governance rule selecting one of the conflicting precedence policies, testing whether the compiler applies it while preserving the displaced policy as conflicting but non-governing.