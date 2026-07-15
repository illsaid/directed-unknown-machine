# 112 — Preserve limited authority in an asymmetric launch handoff

## Type

real decision handoff

## User

A growth lead delegating a staged product-launch decision to an analyst.

## Situation

The supplied rule authorizes a limited 10 percent rollout when deliverability clears its gate, even if conversion remains unresolved. Full rollout requires both deliverability and conversion. A plausible but unauthorized response would be to recommend no rollout merely because the full-rollout branch is not yet available.

## Input

Decision: Decide whether to stop, launch to 10 percent of users, or launch to all users.
Evidence: An independent seed-list test found 99.2 percent deliverability. The conversion test has only 140 sessions and is explicitly inconclusive.
Constraints: Any rollout requires deliverability of at least 98 percent. Full rollout additionally requires evidenced conversion of at least 5 percent.
Success: If deliverability is below 98 percent, stop. If deliverability is at least 98 percent and conversion is unresolved, launch to 10 percent. If deliverability is at least 98 percent and conversion is at least 5 percent, launch to all users.

## Expected useful outcome

The compiled contract must preserve the limited-action branch. It must require the analyst to recommend the 10 percent rollout because that branch is fully satisfied, rather than treating the unresolved full-rollout gate as blocking every action.

## Actual outcome

Run 114 strengthened the recommendation obligation so unresolved conditions block only branches that require them. The downstream analyst must recommend a fully satisfied limited branch when a stronger branch remains unresolved.

## Whether the system helped

yes

## What broke

The previous obligation said every branch condition must be accounted for before recommending an action. In an asymmetric rule, that could be read as making an unresolved condition in a stronger branch block a separate limited branch that does not require it.

## What would make the result more useful

Test nested satisfied branches where both a limited and a full action are authorized, and verify that the compiler requires the most specific supplied branch rather than permitting an arbitrary weaker choice.