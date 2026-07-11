# 023 — Shared evidence source does not cover every gate

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two performance constraints refer to one production-shadow test, but the test measured only one of the required metrics.

## Input

Decision: Roll out the checkout change to all users on Monday or delay it.
Evidence: In one production-shadow test covering 10,000 checkout requests, median response time was 140 milliseconds. The test did not report p95 response time. Paid conversion in the matched test cohort was 23%.
Constraints: Do not recommend rollout if median response time exceeds 200 milliseconds. Do not recommend rollout unless p95 response time is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and both supplied performance constraints are satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve that both gate judgments refer to the same production-shadow test, mark the median gate satisfied and the p95 gate unresolved, and prevent the shared source from implying that both metrics were measured.

## Actual outcome

Run 24 preserves the complete four-field contract and requires shared evidence provenance to be distinguished from actual coverage: the shared test supports the median judgment but leaves p95 unresolved.

## Whether the system helped

yes

## What broke

Before Run 24, the assignment required disclosure of shared provenance but did not explicitly prevent one shared source from being treated as if it supplied evidence for every gate associated with it.

## What would make the result more useful

Next, test whether two sources with overlapping measurements can be cited without double-counting the overlap as corroboration.