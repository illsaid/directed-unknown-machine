# 078 — Tighten governed recommendation without blending rule branches

## Type

structural-regression

## User

A product lead delegating a rollout decision whose supplied rule has explicit precedence among rollout, delay, and diagnostic actions.

## Situation

The `Decision: recommend` requirement must remain compact while forcing one action that is authorized by the supplied rule and explicitly tied to the branch that governs the observed gate pattern.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 540 milliseconds. Retention is 70%, but the contract supplies no comparator for the retention threshold.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds. Retention has a threshold of 70%, with no comparator supplied.
Success: If any gate is violated, delay rollout. Otherwise, if any gate is unresolved, run a diagnostic. Roll out only if every gate is satisfied.

## Expected useful outcome

The executable prints a compact `Decision: recommend` invariant requiring exactly one action authorized by the supplied rule and identification of the governing rule branch. The recommendation is delay because the violated latency gate triggers the first branch; it must not blend delay with the lower-priority diagnostic action triggered by the unresolved retention gate.

## Actual outcome

Run 79 changes only the `Decision: recommend` requirement. Conversion is satisfied, latency is violated, and retention is unresolved. The supplied precedence rule makes delay the single authorized recommendation because the violated-gate branch governs before the unresolved-gate branch. The output must name that branch rather than recommending both delay and diagnostic work as coequal actions.

## Whether the system helped

yes

## What broke

Before Run 79, the requirement asked for one action and traceability to the supplied rule, but did not explicitly forbid blending multiple rule branches or require naming the branch that authorizes the selected action.

## What would make the result more useful

Next, test whether the six-stage sequence can lose any remaining duplicated wording without weakening a tested refusal boundary.