# 102 — Collapse repeated malformed unsupported labels

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract repeats the same malformed unsupported field and who needs one repair item pointing to the first occurrence rather than duplicate schema errors.

## Situation

The input is a concrete rollout decision with two `Owner` label-only lines, each followed by a colon-start value line. The test is whether the tool refuses before field extraction, collapses both malformed occurrences case-insensitively, and retains the first occurrence line number.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Owner
: Growth team owns implementation.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
owner
: Finance owns final approval.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable exits with `Malformed explicit fields:` followed by exactly one `- Owner (line 2)` item and the existing same-line repair instruction. It does not report the second case variant separately, replace the first spelling or line number, absorb either ownership meaning into an allowed field, normalize either split label, or emit complete-contract output.

## Actual outcome

Run 104 confirms the existing malformed-label preflight already satisfies this boundary. It deduplicates case-insensitively, preserves the first supplied spelling, retains the first occurrence line number, and exits before field extraction with `Malformed explicit fields:`, exactly one `- Owner (line 2)` item, and `Keep each field label and colon on the same line.`

## Whether the system helped

yes

## What broke

Nothing. The Run 103 implementation already combines first-occurrence location with case-insensitive malformed-label deduplication.

## What would make the result more useful

Test whether two different malformed unsupported labels remain separately visible with their own first occurrence line numbers.