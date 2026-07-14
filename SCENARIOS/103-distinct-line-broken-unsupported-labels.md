# 103 — Locate distinct malformed unsupported labels

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract contains two different malformed unsupported fields and who needs each distinct repair point identified without confusing Input-block locations with whole-file line numbers.

## Situation

The input is a concrete rollout decision with malformed `Owner` and `Deadline` fields at separate points. The test is whether the tool refuses before extraction, reports both distinct labels in source order with their own Input-relative line numbers, and makes the location scope explicit.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Owner
: Growth team owns implementation.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Deadline
: Decide by Friday.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable exits with `Malformed explicit fields:` followed by `- Owner (input line 2)` and `- Deadline (input line 5)` in source order, then the existing same-line repair instruction. It does not imply whole-file line numbers, merge the two distinct schema defects, absorb either extra meaning into an allowed field, normalize either split label, or emit complete-contract output.

## Actual outcome

Run 105 changes the repair wording from ambiguous `(line N)` to `(input line N)`. The executable reports both distinct malformed fields in source order as `- Owner (input line 2)` and `- Deadline (input line 5)`, then exits before unsupported-label detection or field extraction.

## Whether the system helped

yes

## What broke

The preflight already retained separate first-occurrence locations, but the output called them only `line N` even though numbering begins at the extracted `## Input` block rather than at the top of the scenario file.

## What would make the result more useful

Verify that a malformed distinct label repeated later still retains only its first Input-relative location while another distinct label remains separately visible.