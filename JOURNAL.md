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

## Runs 22–135 — Evidence, boundaries, sequencing, repair grammar, and branch authority

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
- **Run 118:** Required every activating condition of conditional precedence to be established before precedence can govern.
- **Run 119:** Required activated conditional precedence to cite the supplied evidence establishing its trigger.
- **Run 120:** Kept conditional precedence unresolved when supplied trigger evidence conflicts and no applicability rule establishes which source governs.
- **Run 121:** Applied supplied source governance while preserving displaced conflicting trigger evidence as non-governing rather than false or omitted.
- **Run 122:** Limited applicability authority to its explicit period or population scope.
- **Run 123:** Prevented a supplied majority population from standing in for an uncovered remainder.
- **Run 124:** Evaluated universal triggers across complementary governed populations without averaging their results.
- **Run 125:** Resolved overlapping governed populations with supplied overlap authority before evaluating a universal trigger.
- **Run 126:** Preserved conflicting authority inside an overlap when no supplied rule governed the shared scope.
- **Run 127:** Honored an explicit unresolved-condition fallback instead of confusing unresolved evidence with unresolved branch authority.
- **Run 128:** Required the fallback trigger and every additional fallback-specific gate to be established before the fallback can govern.
- **Run 129:** Required an activated fallback recommendation to cite the evidence establishing its trigger and every additional fallback-specific gate.
- **Run 130:** Kept distinct fallback-specific gates independently evidenced and allowed shared support only when the supplied record explicitly supported both.
- **Run 131:** Verified that one record may support two fallback gates when it explicitly states support for each.
- **Run 132:** Rejected implied support for a second fallback gate; explicit support for assay-start capacity did not establish storage availability.
- **Run 133:** Limited duration-bound fallback evidence to its stated period and preserved the uncovered remainder.
- **Run 134:** Allowed complementary duration evidence to compose only when explicit scopes cover the full required period without gaps or conflicting overlap.
- **Run 135:** Verified that a one-day gap keeps the full-duration gate unresolved and blocks the fallback.

## Run 136 — Preserve a conflicting duration overlap

**What changed:** Added `SCENARIOS/134-conflicting-overlap-duration-evidence.md` and strengthened the `Decision: recommend` obligation. When explicit duration scopes overlap and conflict, the compiler must preserve both results for the shared period, mark that period unresolved, and keep the full-duration gate unresolved even when every required day is nominally mentioned.

**Scenario tested:** Refrigerated shipment L-213 has conflicting maximum-temperature records at 7.8°C and 8.3°C and an intact seal. One signed record establishes assay start within 48 hours and qualified storage for days one through four. A second record nominally covers days four through seven but states that its storage unit was outside its qualified calibration interval on day four.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/134-conflicting-overlap-duration-evidence.md` reaches complete-contract output. Under the strengthened obligation, both day-four claims remain visible, day four is unresolved, the seven-day storage gate remains unresolved despite nominal day-one-through-seven coverage, and quarantine is not authorized.

**What was removed or rejected:** Rejected source-ranking, date arithmetic, a temporal evidence engine, and further duration permutations. No dead H1 code was removed because `machine.py` remains required for the historical demo command.

**What was learned:** A no-conflicting-overlap rule is not fully auditable unless it also identifies the exact shared period whose authority failed. Nominal coverage is not established coverage when one required period has contradictory support.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. Duration-scope permutations are now closed; the next test transfers the fallback-authority obligations to a fresh operational domain with a different bounded decision and evidence shape.