# 085 — Repair a wholly unlabeled contract without a new mode

## Type

hostile-regression

## User

An operator with bounded decision notes written as ordinary prose who needs the tool to request the four contract fields without interpreting or rewriting the notes.

## Situation

The input contains a concrete decision, evidence, boundaries, and a fallback rule, but none is labeled. The test is whether the same repair path used for a partially labeled contract accurately reports incompleteness and requests all four explicit fields without adding an unlabeled-input mode.

## Input

We need to decide whether to roll out the new checkout. Paid conversion is 23 percent and p95 latency is 480 milliseconds. Rollout requires conversion of at least 20 percent and latency below 500 milliseconds. Roll out only if both conditions pass; otherwise delay.

## Expected useful outcome

The executable exits with `contract incomplete; add the missing explicit fields without rewriting the notes:` followed by `Decision:`, `Evidence:`, `Constraints:`, and `Success:` in schema order. It does not classify the prose, infer field contents, emit a recommendation, or introduce a second repair mode.

## Actual outcome

Run 86 mentally simulates `python decision_brief.py SCENARIOS/085-unlabeled-contract-repair.md`. No supported or unsupported labels are detected. All four values remain absent, so the existing missing-field path exits with `contract incomplete; add the missing explicit fields without rewriting the notes:` followed by the four labels in schema order. No complete-contract output, inferred field content, or recommendation appears.

## Whether the system helped

yes

## What broke

The prior neutral phrase was accurate but indirect: `cannot preserve the decision contract` described a consequence rather than the exact validated state. The zero-label case showed that one direct incomplete-contract diagnosis works for both partial and wholly unlabeled inputs.

## What would make the result more useful

Next, test whether the repair output can lead directly with the missing labels and remove the remaining generic diagnosis without making the refusal less clear.