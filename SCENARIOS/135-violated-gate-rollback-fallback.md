# 135 — Honor an explicit rollback fallback after a violated release gate

## Type

real decision handoff

## User

A release manager delegating a production deployment decision.

## Situation

A canary release has a measured error rate above the supplied release boundary. The same Success rule explicitly authorizes rollback when that gate is violated, but only if a verified recovery snapshot and an available rollback operator are both established.

## Input

Decision: Decide whether to continue, pause, or roll back production release R-47.
Evidence: The canary error rate is 3.2 percent. The release boundary is at or below 1.0 percent. The recovery service reports that snapshot S-884 passed its checksum verification after the canary began. The on-call SRE acknowledged the incident channel and confirmed availability to execute rollback within 30 minutes. No Severity 1 incident is open.
Constraints: Continuing the release requires an error rate at or below 1.0 percent and no open Severity 1 incident. Rollback is operationally permitted only when the release error-rate gate is violated, a post-canary recovery snapshot is verified, and an SRE is available to execute rollback within 30 minutes.
Success: Continue the release if both continuation gates are satisfied. If the error-rate gate is violated, roll back to the verified post-canary snapshot only if the snapshot and operator-availability gates are satisfied. Otherwise report that no supplied release branch is yet authorized.

## Expected useful outcome

The compiled contract must mark the error-rate gate violated and the no-Severity-1 gate satisfied. It must recognize the violated error-rate gate as the supplied rollback trigger, separately establish the verified-snapshot and operator-availability gates, and recommend rollback to snapshot S-884 as the authorized branch rather than treating the violated primary gate as leaving all branch authority unresolved.

## Actual outcome

Run 137 extended the explicit-fallback obligation from unresolved or conflicting conditions to supplied violated conditions. The rollback trigger and both fallback-specific gates now form one inspectable authority chain.

## Whether the system helped

yes

## What broke

The prior recommendation obligation explicitly recognized fallbacks triggered by unresolved or conflicting conditions, but not fallbacks triggered by a violated gate. A downstream analyst could therefore correctly mark the release gate violated yet fail to recommend the rollback branch that Success expressly authorized for that result.

## What would make the result more useful

Test a violated primary gate with one unresolved fallback-specific gate, confirming that recognizing the trigger does not bypass the remaining fallback conditions.
