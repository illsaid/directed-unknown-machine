# 042 — Same metric supplied with conflicting numeric thresholds

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes define two different minimum paid-conversion thresholds for the same rollout decision, with no rule saying which threshold governs.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: The supported paid-conversion result is 21%. The supported p95 latency range is 460 to 490 milliseconds.
Constraints: Do not recommend rollout unless paid conversion is at least 20% and p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 22% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve both paid-conversion thresholds, 20% and 22%, and the supplied 21% result. Do not silently select the stricter threshold, the looser threshold, or the value appearing later in the contract. Mark the conversion gate unresolved because 21% satisfies one supplied rule and violates the other, while no precedence or reconciliation rule is supplied. Note that latency is satisfied and recommend delay because rollout requires a resolved satisfied conversion gate.

## Actual outcome

Run 43 requires contradictory numeric thresholds for the same metric to remain explicit and unresolved unless the contract supplies a precedence or reconciliation rule. The supported 21% conversion result satisfies the 20% minimum and violates the 22% minimum. The latency gate is satisfied, but rollout remains unsupported and delay follows from the supplied fallback.

## Whether the system helped

yes

## What broke

Before Run 43, the assignment preserved contradictory comparison wording for one threshold but did not state what to do when the contract supplied two different numeric thresholds for the same metric. That left room to choose the stricter, looser, or later value silently.

## What would make the result more useful

Next, test two threshold statements that may be numerically equivalent but use different units or representations, verifying that the system does not declare equivalence without a supplied conversion rule.
