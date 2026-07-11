# 024 — Overlapping evidence sources do not create duplicate corroboration

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two evidence sources overlap on one measurement, while only one source supplies a second measurement needed for another rollout gate.

## Input

Decision: Roll out the checkout change to all users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured median response time at 140 milliseconds and p95 response time at 430 milliseconds. A separate 2,000-request canary test measured median response time at 150 milliseconds but did not report p95 response time. Paid conversion in the matched cohort was 23%.
Constraints: Do not recommend rollout if median response time exceeds 200 milliseconds. Do not recommend rollout unless p95 response time is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and both supplied performance constraints are satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve that median latency has two overlapping sources while p95 latency has only one, avoid treating the repeated median measurement as independent corroboration for p95, and keep both gate judgments separately auditable.

## Actual outcome

Run 25 preserves the complete four-field contract and requires overlap to be disclosed at the measurement level: the two sources corroborate median latency, while only the production-shadow test supports the p95 judgment.

## Whether the system helped

yes

## What broke

Before Run 25, the assignment required shared-source disclosure and measurement coverage, but did not explicitly require overlapping measurements across different sources to be separated from genuinely distinct evidence.

## What would make the result more useful

Next, test two sources that disagree on the same measurement, verifying that disagreement remains explicit instead of being averaged or collapsed.