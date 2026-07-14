# 094 — Normalize spacing before an unsupported-label colon

## Type

hostile-regression

## User

An operator whose notes contain harmless spacing variation before a colon and who needs one concise schema repair rather than duplicate unsupported-field items.

## Situation

The input is a concrete rollout decision with all four allowed fields plus `Owner:` and `Owner :` lines containing distinct meanings. The test is whether repair treats whitespace before the colon as presentation variation, reports the schema defect once using the first supplied spelling, and leaves both meanings untouched for manual remapping.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team owns implementation.
Owner : Finance owns final approval.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by one `- Owner`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Remap each extra meaning to one of those fields.` It does not emit a second whitespace-variant item, alter or discard either ownership note, infer where either meaning belongs, emit complete-contract output, or add an ownership field to the schema.

## Actual outcome

Run 95 verifies that `unsupported_labels` trims the captured label before case-insensitive deduplication. `Owner:` and `Owner :` therefore share the same key, the first supplied spelling `Owner` is retained, and `unsupported_template` emits one repair item. Both source lines remain untouched; missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

Before Run 95, the regex capture for `Owner :` retained trailing whitespace, so it could survive deduplication as a second unsupported label even though the difference was purely typographic.

## What would make the result more useful

Test whether the same harmless pre-colon spacing should also be accepted for one of the four allowed labels without weakening explicit-field detection.