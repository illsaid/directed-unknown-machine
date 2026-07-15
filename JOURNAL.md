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

## Runs 22–107 — Evidence, boundaries, sequencing, and repair grammar

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

## Run 108 — Preserve multiline Evidence structure

**What changed:** Added `SCENARIOS/106-multiline-evidence-preservation.md`. Changed `labeled_value()` from collapsing all whitespace with `" ".join(match.group(1).split())` to stripping only surrounding whitespace with `match.group(1).strip()`.

**Scenario tested:** A complete checkout rollout contract contains two ordinary Evidence lines: one measured conversion statement and one interview note. Neither continuation line begins with a colon or resembles a field label. The tool must accept the contract while retaining the line boundary supplied by the operator.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the scenario's recorded comparative-test gap.

**Observable output:** The new scenario reaches `Contract: complete — 4/4 fields explicit; nothing inferred.` Its Evidence output is `Paid conversion is 23 percent across 4,200 sessions.\nInterview notes say accountability remains unclear after launch.` A local simulation of the updated extraction returned that exact two-line value, with no unsupported or ambiguous-label findings.

**What was removed or rejected:** Removed destructive internal whitespace normalization. Rejected paragraph classification, a new multiline mode, and any change to the allowed field grammar. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Structural preservation includes meaningful line and paragraph boundaries, not only words. The parser can preserve those boundaries without semantic classification because the existing explicit-label lookahead already defines where a field ends.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is a valid Evidence value with a blank-line paragraph break; it should remain intact without creating a false field boundary.