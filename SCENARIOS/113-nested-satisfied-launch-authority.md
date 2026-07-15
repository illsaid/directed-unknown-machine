# 113 — Prefer the fully satisfied nested launch branch

## Type

real decision handoff

## User

A growth lead delegating a staged product-launch decision to an analyst.

## Situation

The supplied rule authorizes a 10 percent rollout when deliverability clears its gate and authorizes full rollout when deliverability and conversion both clear their gates. Both branches are technically satisfied because the full branch contains all conditions of the limited branch plus one additional satisfied condition. A plausible but unauthorized response would choose the weaker 10 percent rollout merely because it is also allowed.

## Input

Decision: Decide whether to stop, launch to 10 percent of users, or launch to all users.
Evidence: An independent seed-list test found 99.2 percent deliverability. A preregistered conversion test across 8,400 sessions found 6.1 percent conversion.
Constraints: Any rollout requires deliverability of at least 98 percent. Full rollout additionally requires evidenced conversion of at least 5 percent.
Success: If deliverability is below 98 percent, stop. If deliverability is at least 98 percent, launch to 10 percent. If deliverability is at least 98 percent and conversion is at least 5 percent, launch to all users.

## Expected useful outcome

The compiled contract must require the analyst to recommend full rollout. Because the full-rollout branch contains every condition of the limited branch plus an additional satisfied condition, the analyst must not arbitrarily select the weaker 10 percent branch.

## Actual outcome

Run 115 strengthened the recommendation obligation so, when one fully satisfied branch contains every condition of another plus additional satisfied conditions, the more conditional supplied branch governs.

## Whether the system helped

yes

## What broke

The previous obligation required recommending a fully satisfied supplied branch, but both the 10 percent and full-rollout branches were satisfied. It did not prevent arbitrary selection of the weaker branch.

## What would make the result more useful

Test two fully satisfied branches that are not nested and verify that the compiler reports unresolved branch authority unless the supplied Success rule states precedence.