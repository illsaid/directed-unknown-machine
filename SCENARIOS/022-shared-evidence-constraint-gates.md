# 022 — Two constraint gates share one evidence source

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two performance constraints use different measurements from the same production-shadow test, so separate gate judgments must not imply independent corroboration.

## Input

Decision: Roll out the checkout change to all users on Monday or delay it.
Evidence: In one production-shadow test covering 10,000 checkout requests, median response time was 140 milliseconds and p95 response time was 480 milliseconds. Paid conversion in the matched test cohort was 23%.
Constraints: Do not recommend rollout if median response time exceeds 200 milliseconds. Do not recommend rollout if p95 response time exceeds 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and both supplied performance constraints are satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve both separately satisfied performance gates, identify that their measurements come from the same production-shadow test, and prevent the repeated source from being presented as two independent bodies of evidence.

## Actual outcome

Run 23 preserves the complete four-field contract and requires separate gate judgments while explicitly identifying shared evidence sources rather than treating repeated citation as independent corroboration.

## Whether the system helped

yes

## What broke

Before Run 23, the assignment required evidence for every constraint but did not require the analyst to disclose when multiple judgments relied on the same evidence source. Repeating the same test under two gate judgments could look like independent support.

## What would make the result more useful

Next, test two constraints that share one evidence source where one measurement passes and the other is unresolved, verifying that shared provenance does not collapse distinct gate states.