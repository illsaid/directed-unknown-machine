# 048 — Consolidated threshold-conflict semantics preserve two boundaries

## Type

structural-regression

## User

A product lead reviewing a delegated rollout assignment before it leaves the team.

## Situation

The executable uses separate requirements for conflicting comparison wording and conflicting numeric values even though both are instances of the same unresolved threshold-conflict rule.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion is 21%, seven-day retention is 71%, and p95 latency is 480 milliseconds.
Constraints: Paid conversion must be at least 20%; seven-day retention must be at least 70%; latency must be at or below 500 milliseconds.
Success: Recommend rollout only if paid conversion is above 20%, seven-day retention is at least 72%, and latency is at or below 500 milliseconds; otherwise recommend delay. No precedence or reconciliation rule is supplied.

## Expected useful outcome

Emit one inspectable conflict rule rather than separate comparator-conflict and numeric-conflict clauses. It must preserve both observable boundaries: paid conversion remains unresolved because 21% passes both supplied rules but the rules still conflict on equality semantics; retention remains unresolved because 71% passes the supplied 70% threshold and fails the supplied 72% threshold. Latency is satisfied. Because two gates remain unresolved, the supported recommendation is delay.

## Actual outcome

Run 49 replaces the separate conflicting-comparator, conflicting-value, and silent-choice clauses with one rule covering any conflicting threshold statements for the same metric. Explicit precedence and cross-unit handling remain separate.

## Whether the system helped

yes

## What broke

Before Run 49, the Threshold conflict group repeated the same preservation-and-no-inference principle across three bullets, increasing audit cost without establishing a distinct additional boundary.

## What would make the result more useful

Next, inspect the remaining requirement groups for a duplicated obligation that can be removed without weakening a named scenario boundary.
