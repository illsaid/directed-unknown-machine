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

## Runs 22–117 — Evidence, boundaries, sequencing, repair grammar, and branch authority

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–87:** Removed duplicate framing and made contract states direct and exact.
- **Runs 88–99:** Simplified unsupported-field repair, deduplicated label variants, and aligned label grammar around same-line horizontal colon spacing.
- **Run 100:** Exposed malformed-label contamination and weakened H2.
- **Run 101:** Added a narrow malformed unsupported-label refusal and restored H2.
- **Runs 102–104:** Verified allowed-label exclusion, first-location reporting, and repeated-label collapse.
- **Run 105:** Verified distinct malformed labels and clarified that reported locations are Input-relative.
- **Run 106:** Verified that repeated and distinct malformed-label handling composes correctly, then stopped extending deduplication permutations.
- **Run 107:** Reframed an indistinguishable prose/schema break as ambiguous rather than definitely malformed.
- **Run 108:** Preserved ordinary multiline Evidence by removing destructive internal whitespace normalization.
- **Run 109:** Verified preservation of a blank-line paragraph break inside Evidence.
- **Run 110:** Refused duplicate allowed labels before extraction rather than silently selecting one occurrence.
- **Run 111:** Verified that an allowed-label word without a colon remains ordinary field prose, then ended label-format permutations.
- **Run 112:** Required every gate result to be connected to the governing Success branch before an action can be recommended.
- **Run 113:** Required a fully satisfied supplied branch to be recommended without invented caution gates.
- **Run 114:** Made gate blocking branch-local so an unresolved stronger branch cannot erase a separately authorized limited action.
- **Run 115:** Required the more conditional supplied branch when satisfied branches are nested by condition inclusion.
- **Run 116:** Required independent satisfied branches with no supplied precedence to remain unresolved rather than authorizing an analyst-selected choice.
- **Run 117:** Applied supplied precedence between independent satisfied branches while preserving displaced branches as satisfied but non-governing.

## Run 118 — Require evidence for conditional precedence

**What changed:** Added `SCENARIOS/116-conditional-precedence-unresolved.md`. Strengthened the `Decision: recommend` obligation so a conditional precedence rule governs only when every supplied condition activating it is established. If an activating condition is violated or unresolved, candidate branch satisfaction is preserved but precedence and branch authority remain unresolved.

**Scenario tested:** Paid acquisition qualifies at 34 percent contribution margin and referral qualifies at 68 percent retained-user conversion. Only one may be funded. Referral takes precedence only if a partner-exclusivity clause applies, but supplied legal evidence says applicability has not been established.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/116-conditional-precedence-unresolved.md` reaches complete-contract output and now emits: `A conditional precedence rule governs only when every supplied condition activating it is established; if any activating condition is violated or unresolved, preserve the candidate branches and report precedence unresolved.`

**What was removed or rejected:** Rejected automatic branch parsing, legal-domain logic, treating the unresolved precedence trigger as false, and selecting either satisfied program by analyst preference. No dead H1 code was removed because `machine.py` remains required for the historical demo command.

**What was learned:** A precedence statement is itself a gated authority rule. Evidence can satisfy every candidate action branch while still failing to authorize a choice between them.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is the same conditional precedence with its triggering fact established; referral should govern while paid acquisition remains satisfied but non-governing.