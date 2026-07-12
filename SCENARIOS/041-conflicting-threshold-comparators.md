# 041 — Same threshold supplied with conflicting comparison wording

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes define the same paid-conversion threshold once as inclusive and once as strict, while the supported evidence touches equality.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: An auditable estimate produces a supported paid-conversion range of 20% to 24%. The supported p95 latency range is 460 to 490 milliseconds.
Constraints: Do not recommend rollout unless paid conversion is at least 20% and p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is above 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve both comparison rules and the full 20%–24% conversion range. Do not silently choose “at least 20%” or “above 20%,” merge them into one rule, or infer precedence from field order. Mark the conversion gate unresolved because equality satisfies the inclusive wording but violates the strict wording. Note that latency is satisfied and recommend delay because rollout requires a resolved satisfied conversion gate.

## Actual outcome

Run 42 requires conflicting comparison wording for the same threshold to remain explicit and unresolved unless the contract supplies a precedence or reconciliation rule. The conversion range includes exactly 20%, so the inclusive and strict rules produce opposite boundary judgments. The latency gate is satisfied, but rollout remains unsupported and delay follows from the supplied fallback.

## Whether the system helped

yes

## What broke

Before Run 42, the assignment handled explicit, missing, strict, and inclusive comparators independently but did not say what to do when the same contract supplied contradictory comparison semantics for one threshold. That left room to choose one wording silently.

## What would make the result more useful

Next, test contradictory threshold values for the same metric, verifying that the system preserves both numbers and leaves the gate unresolved rather than selecting one threshold.