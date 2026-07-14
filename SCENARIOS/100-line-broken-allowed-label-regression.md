# 100 — Preserve the missing-field refusal for a line-broken allowed label

## Type

hostile-regression

## User

An operator whose decision contract splits one of the four allowed field labels from its colon and who needs a precise repair request rather than a misleading malformed-extra-field error.

## Situation

The input is a concrete rollout decision whose `Decision` label appears on one line and its colon begins the next. Run 101 introduced a preflight refusal for the same structure on unsupported labels. This test verifies that the new preflight does not capture allowed labels or change the established missing-field boundary.

## Input

Decision
: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable exits with `Missing explicit fields:` followed by `Decision:`. It does not emit `Malformed explicit fields:`, normalize `Decision\n:` into a valid label, emit complete-contract output, or change the four-field grammar.

## Actual outcome

Run 102 verifies that `malformed_unsupported_labels()` explicitly excludes the four allowed labels. `Decision\n:` therefore reaches normal field extraction, where `Decision` is absent under the same-line grammar, and the executable exits with `Missing explicit fields:` followed by `Decision:`. The Run 101 malformed unsupported-label refusal remains intact without changing executable code.

## Whether the system helped

yes

## What broke

Nothing in the current implementation. The regression test confirms that the Run 101 preflight remains limited to unsupported labels and does not replace the more specific repair for a broken allowed field.

## What would make the result more useful

Test whether a malformed unsupported label appearing between two allowed fields is refused before it can contaminate either neighboring value.
