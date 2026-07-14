# 087 — Lead unsupported repair with the unsupported fields

## Type

hostile-regression

## User

An operator who supplied a complete four-field decision contract plus one unsupported ownership field and needs a repair that preserves the ownership meaning without expanding the schema.

## Situation

The input is a concrete rollout decision with all four supported fields and an extra `Owner` field. The test is whether refusal names the unsupported field first, restates the supported schema, and preserves the extra meaning inside the matching supported field rather than dropping it or adding a fifth field.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by `- Owner`, then lists the four supported fields and instructs the operator to preserve the ownership meaning under the supported field that matches its role. It emits no complete-contract output or recommendation and does not add `Owner` to the schema.

## Actual outcome

Run 88 mentally simulates `python decision_brief.py SCENARIOS/087-unsupported-fields-first.md`. Unsupported-label detection finds `Owner`; the executable exits through `unsupported_template` with the unsupported label first, the unchanged four-field schema, and one preservation instruction. Missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

The prior unsupported-field refusal compressed the unsupported label, supported schema, and preservation guidance into one sentence. It was accurate but slower to inspect than the missing-field repair.

## What would make the result more useful

Test whether the supported-schema line can be shortened without making schema preservation or remapping guidance ambiguous.