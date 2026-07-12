# 043 — Thresholds that appear equivalent only after unit conversion

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes state two latency thresholds for the same rollout decision in different units, but do not supply a conversion rule or explicitly say that the thresholds are equivalent.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: The supported p95 latency range is 460 to 490 milliseconds. Paid conversion is 23%.
Constraints: Do not recommend rollout unless paid conversion is at least 20% and p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and p95 response time is at or below 0.5 seconds; otherwise recommend delay.

## Expected useful outcome

Preserve both supplied latency thresholds, 500 milliseconds and 0.5 seconds. Do not silently declare them equivalent or convert between them because the contract supplies neither a conversion rule nor an explicit equivalence statement. Mark the latency gate unresolved despite the supplied 460–490 millisecond range, note that conversion is satisfied, and recommend delay because rollout requires a resolved satisfied latency gate.

## Actual outcome

Run 44 requires threshold statements in different units or representations to remain separately visible and unresolved unless the contract supplies the conversion or explicitly states their equivalence. The conversion gate is satisfied, but the latency gate remains unresolved and delay follows from the supplied fallback.

## Whether the system helped

yes

## What broke

Before Run 44, the assignment preserved conflicting numeric thresholds but did not state what to do when two thresholds appear numerically equivalent only after an unstated unit conversion. That left room for the analyst to introduce a hidden normalization step.

## What would make the result more useful

Next, test a contract that explicitly supplies the unit conversion or equivalence statement, verifying that the two representations can then be reconciled without adding an automatic conversion engine.