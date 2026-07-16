# 141 — Apply explicit precedence between satisfied fallbacks

## Type

contrasting real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A specimen batch fails its release-temperature gate. Two separate fallback branches are fully satisfied, and Success explicitly gives local reprocessing precedence over salvage shipment when both qualify.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-241.
Evidence: Freezer F-12 recorded minus 61 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-4 is validated for batch B-241, technician Inez Park is available now, and quality officer Mara Chen signed local-reprocessing authorization. Validated dry-ice overpack kit D-11 is reserved, quality officer Mara Chen also signed salvage-shipment authorization, and courier Northline confirmed collection within four hours. Disposition policy DP-9 states that local reprocessing takes precedence over salvage shipment when both branches qualify.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated storage-temperature gate, an intact seal, a validated reprocessing suite, an available qualified technician, and signed quality authorization. Salvage shipment requires a violated storage-temperature gate, an intact seal, a reserved validated dry-ice overpack, signed quality authorization, and confirmed courier collection within four hours. Neither fallback depends on the other.
Success: Release the batch if both release gates are satisfied. Otherwise local-reprocess it when every local-reprocessing condition is satisfied, or salvage-ship it when every salvage-shipment condition is satisfied. When both fallback branches qualify, disposition policy DP-9 gives local reprocessing precedence. If neither fallback is authorized, hold the batch and report why. Preserve the status of each branch separately.

## Expected useful outcome

The compiled contract must mark the storage-temperature gate violated and the seal gate satisfied. It must independently establish every local-reprocessing and salvage-shipment gate. Because both non-nested fallback branches are fully satisfied and DP-9 explicitly gives local reprocessing precedence, it must recommend local reprocessing, cite DP-9 as the authority selecting that branch, and preserve salvage shipment as satisfied but non-governing rather than failed or omitted.

## Actual outcome

Run 143 exposed a small auditability gap. The existing recommendation obligation selected the supplied precedence correctly and preserved the displaced branch, but it required citation only for conditional precedence. The obligation was strengthened so unconditional supplied precedence must also remain visible in the authority trace.

## Whether the system helped

yes

## What broke

The governing branch could be selected under explicit unconditional precedence without requiring the output to cite the supplied policy that authorized the selection.

## What would make the result more useful

Require every applied supplied precedence rule, conditional or unconditional, to be cited in the governing recommendation.