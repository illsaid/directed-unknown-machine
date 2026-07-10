# 002 — Hostile: vague input tries to force generic output

## Type

hostile

## User

A busy operator who wants the system to be useful but gives it vague, contradictory, or overbroad input.

## Situation

The system is asked to evaluate an idea without a clear user, task, or success condition. This tests whether it can resist false generality instead of producing generic advice.

## Input

"Build something that helps me organize messy information and make better decisions. It should be flexible, smart, and useful for many things."

## Expected useful outcome

The system should refuse to inflate the vague request into a generic platform. It should identify the missing concrete task, propose the smallest testable version, and mark confidence low until a specific scenario exists.

## Actual outcome

Run 3 showed that the previous report could identify vagueness but could not recover from it. `machine.py` now detects broad capability language and emits one bounded task: use one real messy note set to support one named decision, produce a one-page brief with three evidence-backed options and one recommendation, and judge success by whether the user can choose without requesting a platform.

This is more useful than asking the human for clarification, but the generated task is still a fixed default rather than evidence that the system understands multiple domains.

## Whether the system helped

partial

## What broke

The old report diagnosed vague input but only repeated that more specificity was needed. The new bounded task recovers one executable test, but it may be too opinionated outside decision-brief situations.

## What would make the result more useful

Test the bounded-task output on a transfer scenario from a different domain. If it still produces a useful test without becoming generic, strengthen H2; otherwise narrow H2 specifically to decision-brief shaping.
