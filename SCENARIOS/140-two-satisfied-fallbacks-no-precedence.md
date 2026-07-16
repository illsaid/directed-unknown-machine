# 140 — Refuse to choose between satisfied fallbacks without precedence

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A specimen batch fails its release-temperature gate. Two separate fallback branches are fully satisfied, but Success supplies no precedence or tie-breaker between them.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-233.
Evidence: Freezer F-12 recorded minus 61 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-4 is validated for batch B-233, technician Inez Park is available now, and quality officer Mara Chen signed local-reprocessing authorization. Validated dry-ice overpack kit D-11 is reserved, quality officer Mara Chen also signed salvage-shipment authorization, and courier Northline confirmed collection within four hours.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated storage-temperature gate, an intact seal, a validated reprocessing suite, an available qualified technician, and signed quality authorization. Salvage shipment requires a violated storage-temperature gate, an intact seal, a reserved validated dry-ice overpack, signed quality authorization, and confirmed courier collection within four hours. Neither fallback depends on the other.
Success: Release the batch if both release gates are satisfied. Otherwise local-reprocess it when every local-reprocessing condition is satisfied, or salvage-ship it when every salvage-shipment condition is satisfied. If neither fallback is authorized, hold the batch and report why. No precedence or tie-breaker is supplied when both fallback branches qualify. Preserve the status of each branch separately.

## Expected useful outcome

The compiled contract must mark the storage-temperature gate violated and the seal gate satisfied. It must independently establish every local-reprocessing and salvage-shipment gate. Because both non-nested fallback branches are fully satisfied and Success supplies no precedence or tie-breaker, it must preserve both as authorized candidates but report governing branch authority unresolved rather than choosing one. It must identify the missing precedence or tie-breaker and must not collapse either branch into failure.

## Actual outcome

Run 142 verified that the existing non-nested branch obligation already covers competing fallback branches. Both fallback branches remain fully satisfied, but governing authority remains unresolved because the supplied Success rule gives no precedence or tie-breaker. No executable change was justified.

## Whether the system helped

yes

## What broke

Nothing. The existing rule correctly prevents an analyst from selecting between two independently satisfied, non-nested fallback branches without supplied authority.

## What would make the result more useful

Test the same two satisfied fallback branches with an explicit supplied precedence rule, verifying that the governing branch is selected while the displaced branch remains satisfied but non-governing.
