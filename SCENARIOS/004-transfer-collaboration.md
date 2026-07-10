# 004 — Transfer: vague collaboration request is not a decision brief

## Type

transfer

## User

A volunteer coordinator trying to improve communication and participation in a neighborhood mutual-aid group.

## Situation

The coordinator has scattered messages, inconsistent attendance, and unclear ownership. They ask for broad help, but the underlying problem is coordination rather than choosing among evidence-backed options.

## Input

"Build something flexible and smart that organizes our messy information, helps everyone communicate better, and is useful for many kinds of volunteer work."

## Expected useful outcome

The system should either shape one concrete coordination experiment with an observable result, or clearly state that its current decision-brief default does not fit. It should not disguise a coordination problem as a three-option decision brief.

## Actual outcome

Run 4 mentally simulated the current `machine.py`. Its vague-input detector activates and produces the same one-page decision brief used for the hostile decision-support scenario. That output is concrete, but it is not well matched to the user's coordination problem: the missing artifact is more likely an owner/action roster or one-event handoff test than three evidence-backed options and a recommendation.

## Whether the system helped

no

## What broke

The system treated all vague requests as decision-support requests. Its fixed bounded-task transformation supplied specificity by changing the problem rather than understanding it.

## What would make the result more useful

Do not generalize into multiple task templates. Narrow the live hypothesis to shaping messy decision-support inputs into one-page decision briefs, and treat other vague task classes as outside the current proven purpose until evidence supports a replacement.