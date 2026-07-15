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

## Runs 22–109 — Evidence, boundaries, sequencing, and repair grammar

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

## Run 110 — Refuse duplicate allowed labels

**What changed:** Added `SCENARIOS/108-duplicate-allowed-label.md`. Added `duplicate_allowed_labels()` and a narrow pre-extraction refusal that reports all Input-relative locations for any allowed field appearing more than once.

**Scenario tested:** Intended Evidence contains the sentence `Success: depends on support coverage after launch.`, followed later by the actual `Success: Roll out only if every gate is satisfied; otherwise delay.` Both are structurally explicit allowed labels, so semantic intent cannot be determined safely.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap.

**Observable output:** The new preflight returns `Duplicate explicit fields:` followed by `- Success (input lines 3, 5)` and exits before `labeled_value()` can select the first occurrence. A direct Python simulation of the duplicate scan produced exactly `Success` at lines 3 and 5.

**What was removed or rejected:** Rejected first-wins, last-wins, field merging, and semantic classification of the interview sentence. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Exact field uniqueness is part of preserving delegated authority. A duplicate allowed label is not harmless formatting: it can replace the actual success rule while still producing apparently complete output. Refusal is safer and more specific than guessing intent.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test verifies that continuation prose beginning with an allowed-label word but lacking a colon remains inside Evidence and does not trigger the duplicate refusal.