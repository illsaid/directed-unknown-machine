# 051 — Consolidated source exclusion preserves observation and relevance boundaries

## Type

structural-regression

## User

A product lead reviewing a delegated rollout assignment before it leaves the team.

## Situation

The source-exclusion requirement repeats several conditions for rejecting a measurement as non-comparable. The rule should be shorter while still distinguishing a supplied scope mismatch that clearly excludes a source from an observed difference whose relevance is not established.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test using the current US web traffic mix measured p95 response time at 430 milliseconds. Canary A measured 560 milliseconds, but 78% of its requests came from an internal mobile-client build that is explicitly outside Monday's US web rollout. Canary B measured 540 milliseconds and directly recorded 38% Safari traffic versus 24% in the current US web mix, but no browser-segment latency results, weighting analysis, or other supplied evidence establishes that this difference changes applicability to Monday's rollout population. Paid conversion in the matched US web cohort was 23%.
Constraints: Do not recommend rollout unless paid conversion is at least 20% and p95 response time for Monday's US web rollout population is below 500 milliseconds.
Success: Preserve all three latency values. Exclude Canary A only with its supplied out-of-scope observation and relevance to the target population. Do not exclude Canary B because the supplied Safari-mix difference lacks evidence establishing relevance. Recommend rollout only if every remaining applicable measurement satisfies the gates; otherwise recommend delay.

## Expected useful outcome

Emit one concise source-exclusion rule requiring the excluded value plus supplied evidence of both the observed mismatch and why it changes applicability to the target population. Under that rule, Canary A may be excluded, Canary B may not, the remaining latency evidence conflicts across 430 and 540 milliseconds, the latency gate is unresolved, and delay is recommended.

## Actual outcome

Run 52 replaces the duplicated source-exclusion wording with one two-part evidence rule. The output still permits Canary A's exclusion because the mobile-client traffic is directly observed and explicitly outside the target population, while Canary B remains applicable because the Safari-mix difference has no supplied relevance evidence. The latency gate remains unresolved and delay is supported.

## Whether the system helped

yes

## What broke

Before Run 52, the source-exclusion requirement expressed the same trust boundary through a long sequence of named clauses and two separate negative formulations, making the invariant harder to inspect than necessary.

## What would make the result more useful

Next, inspect the sensitivity requirements for duplicated positive and negative wording that can be consolidated without losing the threshold-crossing boundary.