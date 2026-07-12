# 049 — Consolidated evidence provenance preserves overlap and coverage boundaries

## Type

structural-regression

## User

A product lead reviewing a delegated rollout assignment before it leaves the team.

## Situation

The executable separately requires identifying shared sources and disclosing overlapping measurements, even though both obligations can be expressed as one source-to-measurement provenance rule.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Experiment report A and analytics export B both report paid conversion at 23%. Report A also reports p95 latency at 480 milliseconds. Export B contains no latency measurement.
Constraints: Paid conversion must be at least 20% and p95 latency must be at or below 500 milliseconds.
Success: Recommend rollout only if both gates are satisfied from supplied evidence; otherwise recommend delay.

## Expected useful outcome

Emit one inspectable provenance rule that maps every source to the measurements it actually supplies and discloses overlap without treating duplicate conversion reporting as independent support or as latency evidence. Conversion is satisfied from the shared 23% measurement, latency is satisfied from report A alone, and rollout is supported.

## Actual outcome

Run 50 consolidates the shared-source and overlapping-measurement clauses into one provenance rule. The output still requires source-to-measurement mapping, identifies duplicate conversion coverage, prevents that overlap from becoming extra independent corroboration, and keeps latency tied only to report A.

## Whether the system helped

yes

## What broke

Before Run 50, the Evidence provenance group split one provenance invariant across two bullets: identify which measurements each source supplies, then separately disclose overlap and prohibit spillover.

## What would make the result more useful

Next, inspect the Applicability and adjustment group for one duplicated obligation that can be removed without weakening its named scenario boundary.
