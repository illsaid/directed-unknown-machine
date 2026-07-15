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

## Runs 22–111 — Evidence, boundaries, sequencing, and repair grammar

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

## Run 112 — Trace every gate into the authorized branch

**What changed:** Added `SCENARIOS/110-vendor-renewal-authority.md`. Strengthened the `Decision: recommend` obligation so the downstream analyst must connect every gate result to the named Success branch and cannot recommend an action until every branch condition is accounted for.

**Scenario tested:** A quarterly vendor-renewal handoff supplies conflicting four-hour response figures and an incomplete avoided-cost estimate. Renewal is authorized only if independent compliance is at least 90 percent and evidenced avoided backlog cost is at least the $24,000 fee. Selecting the vendor's favorable 92 percent figure or inventing an avoided-ticket count would produce a plausible but unauthorized renewal.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** `python decision_brief.py SCENARIOS/110-vendor-renewal-authority.md` reaches complete-contract output and now emits: `Recommend one authorized action and name the governing Success branch. Connect every gate result to that branch, and do not recommend an action until every branch condition is accounted for.` The service conflict and missing avoided-ticket count therefore remain blocking rather than disappearing behind the favorable values.

**What was removed or rejected:** Rejected vendor-specific calculations, automatic conflict resolution, and a domain mode. No dead H1 code was removed because `machine.py` remains required for the historical demo command.

**What was learned:** Naming the governing branch is not enough to preserve delegated authority. A recommendation can cite the correct branch while silently omitting an unresolved condition. The narrow useful requirement is a complete gate-to-branch trace, not more domain analysis.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is a contrasting real handoff with all gates satisfied, checking that the stronger traceability rule permits the authorized positive branch without expanding the compiler's role.