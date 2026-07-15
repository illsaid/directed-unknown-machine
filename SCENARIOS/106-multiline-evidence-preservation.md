# 106 — Preserve ordinary multiline Evidence structure

## Type

transfer

## User

An operator handing an analyst a bounded rollout decision whose evidence includes a deliberately wrapped interview note.

## Situation

A complete four-field contract contains ordinary multiline Evidence prose. No line resembles an explicit or malformed field. The test is whether the handoff reaches complete-contract output without flattening the supplied evidence structure.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent across 4,200 sessions.
Interview notes say accountability remains unclear after launch.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable reaches `Contract: complete` and prints the Evidence value on two lines exactly as supplied. It does not trigger structural repair, merge the interview note into a single normalized sentence, infer a new field, or alter the four-field schema.

## Actual outcome

Run 108 changes field extraction to remove only surrounding whitespace. The two supplied Evidence lines remain separately visible in complete-contract output.

## Whether the system helped

yes

## What broke

The parser previously collapsed all internal whitespace with `" ".join(...split())`, turning deliberately multiline Evidence into one sentence and weakening the claim that the handoff preserves supplied notes.

## What would make the result more useful

Test whether blank-line paragraph separation inside Evidence should also remain intact without being mistaken for a field boundary.