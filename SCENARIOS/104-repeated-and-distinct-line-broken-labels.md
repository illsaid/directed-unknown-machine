# 104 — Preserve first locations across repeated and distinct malformed labels

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract contains one malformed extra field twice and another malformed extra field once, and who needs a concise repair list that preserves only actionable first locations.

## Situation

The input is a concrete rollout decision with malformed `Owner`, `Deadline`, and later `owner` fields. The test is whether the tool collapses the repeated case variant to the first Input-relative location while retaining the distinct malformed label separately and in source order.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Owner
: Growth team owns implementation.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Deadline
: Decide by Friday.
owner
: Finance owns final approval.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable exits with `Malformed explicit fields:` followed by exactly `- Owner (input line 2)` and `- Deadline (input line 5)` in source order, then the existing same-line repair instruction. It does not report the later `owner` occurrence, replace the first spelling or location, merge the distinct defects, absorb any extra meaning into an allowed field, normalize a split label, or emit complete-contract output.

## Actual outcome

Run 106 confirms the existing malformed-label preflight already satisfies this combined boundary. It reports exactly `- Owner (input line 2)` and `- Deadline (input line 5)` in source order. The later `owner` occurrence is collapsed case-insensitively without replacing the first spelling or location, and the refusal occurs before field extraction.

## Whether the system helped

yes

## What broke

Nothing. The existing implementation correctly composes first-occurrence deduplication with preservation of distinct malformed schema defects.

## What would make the result more useful

Stop extending deduplication permutations. Test whether the malformed-label preflight can falsely classify ordinary wrapped field prose as a schema defect.