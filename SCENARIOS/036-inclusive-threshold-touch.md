# 036 — Supported range touches an inclusive threshold

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply a supported latency range whose upper bound equals an explicitly inclusive rollout threshold.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: An auditable target-population adjustment produces a supported p95 latency range of 480 to 500 milliseconds. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 480–500 millisecond range and the supplied inclusive wording. Because every supported value is at or below 500 milliseconds and paid conversion is 23%, judge both gates satisfied and recommend rollout. Do not silently reinterpret “at or below” as “below.”

## Actual outcome

Run 37 requires equality at a threshold to follow the comparison rule supplied in the contract. The range touches 500 milliseconds but satisfies the explicitly inclusive maximum, so rollout is supported.

## Whether the system helped

yes

## What broke

Before Run 37, the assignment resolved same-side ranges but did not explicitly state that a boundary-touching value must follow the supplied inclusive or strict comparison rule.

## What would make the result more useful

Next, test the strict counterpart: a supported range whose upper bound equals a threshold stated as strictly below 500 milliseconds.