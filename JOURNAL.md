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

## Runs 22–45 — Evidence provenance, applicability, assumptions, sensitivity, and threshold boundaries

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.
- **Run 41:** Left equality unresolved when a numeric threshold lacked explicit strict or inclusive comparison semantics.
- **Run 42:** Preserved conflicting strict and inclusive comparison rules for the same threshold without manufacturing precedence.
- **Run 43:** Preserved conflicting numeric thresholds for the same metric without choosing the stricter, looser, or later value.
- **Runs 44–45:** Preserved cross-unit statements when equivalence was absent and accepted reconciliation only when the contract explicitly supplied equivalence.

## Run 46 — Preserve displaced thresholds under explicit precedence

**What changed:** Added `SCENARIOS/045-explicit-threshold-precedence.md` and tightened the conflicting-threshold requirement. When the contract supplies precedence, the brief must identify the governing threshold while preserving every displaced threshold and reporting the result under each.

**Scenario tested:** `Constraints` requires paid conversion of at least 20%. `Success` requires at least 22%. Evidence reports 21% and explicitly states that the Success threshold governs a conflict while the Constraints threshold remains contextual. The same evidence reports a supported 460–490 millisecond latency range against an inclusive 500 millisecond maximum.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario still maps `partial` to `hold-but-improve` and recommends fixing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/045-explicit-threshold-precedence.md` preserves all four fields and emits the strengthened precedence obligation. Under the supplied contract, 21% satisfies the contextual 20% threshold but violates the governing 22% threshold; latency is satisfied and the Success fallback requires delay.

**What was removed or rejected:** The prior conflicting-numeric-threshold clause was replaced rather than supplemented. No threshold parser, precedence detector, calculator, fifth field, configuration, domain mode, or dashboard was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Explicit precedence can resolve a conflict without erasing it. The useful boundary is not merely choosing the governing rule; it is keeping the displaced rule inspectable so the analyst cannot make reconciliation look like the original contract was internally consistent.

**Hypothesis movement:** H2 remains primary at 0.99. Confidence stayed unchanged near saturation. The hypothesis survived. The next test is structural simplification of the accumulated gate requirements without losing a previously established boundary.