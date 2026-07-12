# 040 — Threshold number supplied without comparison wording

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply a conversion threshold number but do not state whether equality satisfies or violates the rollout gate.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: An auditable estimate produces a supported paid-conversion range of 20% to 24%. The supported p95 latency range is 460 to 490 milliseconds.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion meets the 20% threshold and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 20%–24% conversion range and the exact phrase “meets the 20% threshold.” Because the contract does not say whether equality at 20% is acceptable, do not invent strict or inclusive semantics. Mark the conversion gate unresolved, note that the latency gate is satisfied, and recommend delay because rollout requires both gates to be satisfied.

## Actual outcome

Run 41 requires a numeric threshold without explicit comparison wording to remain unresolved when supplied evidence touches equality. The conversion range includes exactly 20%, but “meets” does not establish whether that boundary counts as success. The latency gate is satisfied; rollout remains unsupported because the conversion gate is unresolved.

## Whether the system helped

yes

## What broke

Before Run 41, the assignment said to use supplied comparison wording but did not explicitly state what to do when no strict or inclusive comparison operator is supplied. That left room to inherit an unstated convention for equality.

## What would make the result more useful

Next, test a contract that uses conflicting comparison wording for the same threshold, verifying that the conflict remains explicit rather than selecting one rule.