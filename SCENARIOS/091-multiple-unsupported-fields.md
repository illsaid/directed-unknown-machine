# 091 — Remap multiple unsupported fields

## Type

hostile-regression

## User

An operator who supplied a complete four-field decision contract plus separate ownership and timing fields and needs a repair that preserves both extra meanings without expanding the schema or assigning them automatically.

## Situation

The input is a concrete rollout decision with all four allowed fields plus `Owner` and `Deadline`. The test is whether the repair remains clear when more than one unsupported field must be preserved and manually remapped.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team.
Deadline: Decide by Friday.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by `- Owner` and `- Deadline`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Remap each extra meaning to one of those fields.` It emits no complete-contract output or recommendation, preserves both extra meanings for operator-directed remapping, does not assign either meaning automatically, and does not add `Owner` or `Deadline` to the schema.

## Actual outcome

Run 92 mentally simulates `python decision_brief.py SCENARIOS/091-multiple-unsupported-fields.md`. Unsupported-label detection finds `Owner` and `Deadline` in source order; the executable exits through `unsupported_template` with both labels, the unchanged allowed-field list, and an instruction that points unambiguously back to that list. Missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

The prior instruction, `Place each extra meaning under its matching field.`, was proven only for one unsupported field. With two extras, `matching field` could sound as though the executable had already determined a unique destination for each meaning.

## What would make the result more useful

Test whether the unsupported-field list should preserve duplicate labels or collapse them without losing distinct meanings.