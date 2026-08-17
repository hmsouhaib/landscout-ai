# `src/landscout/stages/planning_overlay.py`

## File identity

- Repository path: `src/landscout/stages/planning_overlay.py`
- File type: Python source
- Primary responsibility: Provides the repository artifact `src/landscout/stages/planning_overlay.py` for the role described by its exact content below.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `7ba1e577956408550871aa0e817472e9b9443f900b48ed0fa28f09351951cf0b`

## 1. Purpose

Provides the repository artifact `src/landscout/stages/planning_overlay.py` for the role described by its exact content below.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.

### Third-party

- None.

### Internal LandScout

- `from landscout.common.planning_overlay import ( ABSOLUTE_OVERLAY_TOLERANCE, RELATIVE_OVERLAY_TOLERANCE, technical_overlay_tolerance, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

No function or method is declared in this file.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `planning` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
