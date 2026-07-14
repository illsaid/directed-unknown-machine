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

## Runs 22–96 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–92:** Split unsupported-field refusal into unsupported labels, a compact allowed schema, and concise operator-directed remapping guidance; then clarified multiple distinct unsupported labels.
- **Run 93:** Added order-preserving, case-insensitive deduplication so repeated occurrences of one unsupported label produce one repair item while all source meanings remain untouched.
- **Run 94:** Verified case variants collapse under that same boundary without an executable change.
- **Run 95:** Normalized harmless pre-colon spacing during unsupported-label identity checks, so `Owner:` and `Owner :` produce one repair item without changing the schema or either source meaning.
- **Run 96:** Accepted horizontal spacing before an allowed-label colon and kept next-field boundaries consistent, so `Decision :` reaches complete-contract output rather than a false missing-field refusal.

## Run 97 — Keep allowed-label spacing horizontal

**What changed:** Added `SCENARIOS/096-line-broken-allowed-label.md` and replaced `\s*` around allowed-field colons in `labeled_value()` with `[ \t]*`. Same-line spaces and tabs remain accepted, but newline characters can no longer join a label to a detached colon or blur the next-field lookahead.

**Scenario tested:** A concrete checkout rollout contract supplies `Decision` on one line and `: Decide whether...` on the next, followed by canonical `Evidence:`, `Constraints:`, and `Success:` fields. The observable requirement is a `Missing explicit fields:` refusal containing `Decision:`, with no complete-contract output or inferred multiline label.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The decision-contract executable was then mentally simulated before and after the change. Under the old `Decision\s*:` pattern, the newline matched `\s*` and the broken label was accepted. Under `Decision[ \t]*:`, it does not match, while the three canonical fields remain readable, so the executable requests only `Decision:`.

**What was removed or rejected:** Removed newline tolerance from the allowed-label grammar. Rejected multiline labels, fuzzy repair, semantic inference, a parser mode, schema expansion, and changes to the six audit operations. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Presentation tolerance must not include structural whitespace. Restricting colon padding to horizontal whitespace preserves the convenience established in Run 96 while restoring the explicit same-line field boundary that makes the contract inspectable.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether a tab before the colon is accepted as intended without weakening the multiline refusal boundary.