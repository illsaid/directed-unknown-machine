# 071 — Judge the gates, then recommend

## Type

structural-regression

## User

A product lead delegating a rollout decision whose evidence produces different results across independent gates.

## Situation

The executable keeps per-gate judgments and the final recommendation separate, but the headings `Gate judgments` and `Governed recommendation` read like neighboring result categories rather than an ordered pair. The recommendation must visibly follow from the independent gate results and the supplied success rule.

## Input

Decision: Roll out the checkout change or delay it.
Evidence: Paid conversion is 23%. P95 latency is 540 milliseconds.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds. Keep the two gate results separate.
Success: First judge conversion satisfied and latency violated from the supplied evidence. Then apply the rule that rollout requires every gate to clear, and recommend delay.

## Expected useful outcome

The executable prints `Decision: judge gates` before `Decision: recommend`. The first stage reports conversion satisfied and latency violated independently and states that the violated latency gate blocks rollout. The second stage applies the supplied all-gates rule and selects delay. Evidence and boundary stages remain unchanged.

## Actual outcome

Run 72 renames only the two final audit headings to `Decision: judge gates` and `Decision: recommend`. Their requirements, order, parser behavior, and decision rules remain unchanged. The output now exposes the final dependency as two imperative operations: establish each gate result, then select the action governed by the supplied success rule.

## Whether the system helped

yes

## What broke

Before Run 72, the noun phrases `Gate judgments` and `Governed recommendation` preserved the conceptual distinction but did not make the dependency as scannable as the evidence and boundary pairs. A reader could treat the recommendation as a parallel summary rather than an action derived from the gate results under the supplied rule.

## What would make the result more useful

Stop renaming headings unless a new scenario exposes a different concrete ambiguity. The six-stage reasoning sequence is now visibly preserve, transform, reconcile, apply, judge, recommend.