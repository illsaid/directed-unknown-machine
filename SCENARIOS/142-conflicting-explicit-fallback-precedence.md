# 142 — Preserve conflicting explicit fallback precedence

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A specimen batch fails its release-temperature gate. Two separate fallback branches are fully satisfied, but two supplied policies give opposite precedence and no supplied authority establishes which policy governs.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-248.
Evidence: Freezer F-12 recorded minus 61 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-4 is validated for batch B-248, technician Inez Park is available now, and quality officer Mara Chen signed local-reprocessing authorization. Validated dry-ice overpack kit D-11 is reserved, quality officer Mara Chen also signed salvage-shipment authorization, and courier Northline confirmed collection within four hours. Laboratory disposition policy DP-9 states that local reprocessing takes precedence over salvage shipment when both branches qualify. Network transport policy NT-3 states that salvage shipment takes precedence over local reprocessing when both branches qualify. No supplied governance rule states whether DP-9 or NT-3 controls this disposition.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated storage-temperature gate, an intact seal, a validated reprocessing suite, an available qualified technician, and signed quality authorization. Salvage shipment requires a violated storage-temperature gate, an intact seal, a reserved validated dry-ice overpack, signed quality authorization, and confirmed courier collection within four hours. Neither fallback depends on the other.
Success: Release the batch if both release gates are satisfied. Otherwise local-reprocess it when every local-reprocessing condition is satisfied, or salvage-ship it when every salvage-shipment condition is satisfied. Apply supplied precedence only when the governing precedence authority is established. If precedence authority is unresolved, hold the batch, preserve both fallback branches as satisfied candidates, and report the missing governance rule.

## Expected useful outcome

The compiled contract must mark the storage-temperature gate violated and the seal gate satisfied. It must independently establish every local-reprocessing and salvage-shipment gate. Because both fallback branches are fully satisfied but DP-9 and NT-3 supply opposite precedence with no rule establishing which controls, it must preserve both policies, leave branch authority unresolved, recommend hold, and identify the missing governance rule. It must not choose by field order, policy name, or convenience.

## Actual outcome

Run 144 exposed a distinct authority gap. The recommendation obligation required an applied precedence rule to be cited, but did not explicitly forbid selecting one of two conflicting unconditional precedence sources when no supplied applicability or governance rule established which source controlled.

## Whether the system helped

partial

## What broke

Conflicting unconditional precedence policies could each appear sufficient in isolation, allowing a downstream analyst to select one and cite it while omitting the opposing supplied authority.

## What would make the result more useful

Require conflicting supplied precedence authorities to remain visible and leave branch authority unresolved unless supplied applicability or governance evidence establishes which precedence source governs.