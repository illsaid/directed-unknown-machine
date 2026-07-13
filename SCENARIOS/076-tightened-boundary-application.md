# 076 — Tighten boundary application without weakening range or equality semantics

## Type

structural-regression

## User

A product lead delegating a rollout decision whose gates include sensitivity ranges and several forms of equality at a threshold.

## Situation

The `Boundary: apply` requirement protects two distinct application cases: evaluating a complete supplied range and resolving equality only from explicit comparison wording. The operator needs a shorter invariant that retains both refusal boundaries.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion sensitivity is 19% to 21%. P95 latency sensitivity is 480 to 490 milliseconds. Error rate is exactly 2%. Churn is exactly 5%. Retention is exactly 70%.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds. Error rate must be at or below 2%. Churn must be below 5%. The retention threshold is 70%, with no strict or inclusive comparator supplied. Evaluate every sensitivity range in full and do not select a midpoint or convenient point.
Success: Roll out only if every governing gate is supported as satisfied. Otherwise delay and identify each conditional, violated, or unresolved gate.

## Expected useful outcome

The executable prints a shorter `Boundary: apply` invariant that still evaluates complete ranges, marks threshold-crossing ranges conditional, resolves same-side ranges from the whole range, honors inclusive and strict equality wording, and leaves equality unresolved when no comparator is supplied.

## Actual outcome

Run 77 shortens only the `Boundary: apply` requirement. Conversion is conditional because its 19% to 21% range crosses the 20% minimum. Latency is satisfied because the complete 480 to 490 millisecond range is below 500 milliseconds. Error rate at 2% satisfies the inclusive maximum. Churn at 5% violates the strict maximum. Retention at 70% remains unresolved because the threshold supplies no comparator. The governed recommendation is delay.

## Whether the system helped

yes

## What broke

Before Run 77, the boundary-application invariant repeated the same refusal logic across long range and equality clauses. The behavior was correct, but the wording obscured the simpler rule: apply the complete supplied evidence using only the supplied boundary semantics.

## What would make the result more useful

Next, test whether `Decision: judge gates` can be shortened without allowing an overall verdict to erase independent gate statuses or their evidence.