# 088 — Shorten the allowed-schema reminder

## Type

hostile-regression

## User

An operator who supplied a complete four-field decision contract plus one unsupported ownership field and needs a compact repair that still preserves both the schema and the ownership meaning.

## Situation

The input is a concrete rollout decision with all four supported fields and an extra `Owner` field. The test is whether the unsupported-field refusal can replace the longer supported-schema sentence with a compact allowed-field line while retaining explicit remapping guidance.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by `- Owner`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Move each extra meaning under the allowed field matching its role.` It emits no complete-contract output or recommendation and does not add `Owner` to the schema.

## Actual outcome

Run 89 mentally simulates `python decision_brief.py SCENARIOS/088-allowed-schema-shorthand.md`. Unsupported-label detection finds `Owner`; the executable exits through `unsupported_template` with the unsupported label first, the compact allowed-field list, and explicit remapping guidance. Missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

The prior refusal used `Supported fields:` and a longer preservation sentence. Both were accurate, but the repeated word `supported` made the repair denser than necessary after the unsupported label had already been named.

## What would make the result more useful

Test whether `Move each extra meaning` can be shortened further without implying that the unsupported value may be dropped or automatically classified.