# 047 — Consolidated equality semantics preserve four boundaries

## Type

structural-regression

## User

A product lead reviewing a delegated rollout assignment before it leaves the team.

## Situation

The executable repeats separate equality clauses for strict maximum, inclusive minimum, and strict minimum gates even though one comparison rule can preserve all established outcomes.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Supported ranges are p95 latency 480 to 500 milliseconds, paid conversion 20% to 24%, completion rate 80% to 84%, and refund rate 2% to 3%.
Constraints: Latency must be at or below 500 milliseconds; paid conversion must be at least 20%; completion rate must be above 80%; refund rate must be strictly below 3%.
Success: Recommend rollout only if every supplied gate is satisfied; otherwise recommend delay.

## Expected useful outcome

Emit one inspectable equality rule rather than separate clauses. It must preserve all four observable judgments: the inclusive latency maximum is satisfied at 500 milliseconds; the inclusive conversion minimum is satisfied at 20%; the strict completion minimum is violated at 80%; and the strict refund maximum is violated at 3%. Because two gates are violated, the supported recommendation remains delay.

## Actual outcome

Run 48 replaces four overlapping equality clauses with one rule that maps supplied inclusive wording to satisfied equality and supplied strict wording to violated equality. The four established boundary outcomes remain explicit, and the no-comparator rule remains separate.

## Whether the system helped

yes

## What broke

Before Run 48, the Threshold semantics group repeated the same equality principle across multiple bullets, increasing audit cost without adding a distinct boundary.

## What would make the result more useful

Next, test whether another requirement group contains duplication that can be removed without weakening a named scenario boundary.