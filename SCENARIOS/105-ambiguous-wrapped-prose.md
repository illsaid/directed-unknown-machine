# 105 — Refuse ambiguous wrapped prose without claiming certainty

## Type

hostile-transfer

## User

An operator whose evidence contains a line break that resembles a malformed extra field, and who needs a safe repair without the tool pretending it knows whether the text is prose or schema.

## Situation

A complete rollout contract contains ordinary interview prose wrapped so that `Owner` appears alone and the next line begins with a colon. Structurally, this is indistinguishable from the malformed unsupported field tested in Runs 100–106. The test is whether the tool refuses safely while describing the ambiguity accurately.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent. The interview transcript describes post-launch accountability as
Owner
: unclear after launch.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable exits before extraction and reports `Ambiguous field-like breaks:` followed by `- Owner (input line 3)`. It tells the operator either to keep prose continuous or keep each field label and colon on the same line. It does not assert that `Owner` is definitely an explicit field, absorb the text into Evidence, infer a destination, or emit complete-contract output.

## Actual outcome

Run 107 changes the refusal from the categorical `Malformed explicit fields:` to `Ambiguous field-like breaks:` and gives a two-branch repair. The tool still refuses before extraction, but no longer claims semantic certainty that the structure cannot support.

## Whether the system helped

yes

## What broke

The existing refusal protected field preservation but mislabeled an ambiguous wrapped-prose structure as definitely malformed schema.

## What would make the result more useful

Test a real multiline Evidence handoff with ordinary paragraph wrapping that does not create a colon-start line; it should remain preserved without triggering structural repair.
