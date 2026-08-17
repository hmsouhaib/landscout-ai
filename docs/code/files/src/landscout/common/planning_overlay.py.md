# `src/landscout/common/planning_overlay.py`

## File identity

- Repository path: `src/landscout/common/planning_overlay.py`
- File type: Python source
- Primary responsibility: Defines the technical floating-point tolerance used by factual planning overlay checks.
- Layer / domain: `internal common contract/utility` / `planning`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `f28349ab5f3f8223b537184ac28a98d6d6e328a724957dabb7089c3809351086`

## 1. Purpose

Defines the technical floating-point tolerance used by factual planning overlay checks.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.

### Third-party

- None.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `ABSOLUTE_OVERLAY_TOLERANCE` | `1e-6` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATIVE_OVERLAY_TOLERANCE` | `1e-12` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `technical_overlay_tolerance`

**Signature**

```python
def technical_overlay_tolerance(reference_value: float) -> float:
```

**Purpose**

Return the shared floating-point overlay tolerance for a metric value.

**Inputs**

- `reference_value` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `max(ABSOLUTE_OVERLAY_TOLERANCE, reference_value * RELATIVE_OVERLAY_TOLERANCE)`.

**Algorithm**

1. Checks `not isfinite(reference_value) or reference_value < 0`. When true: Raises `ValueError('Overlay tolerance reference must be finite and non-negative')`.
2. Returns `max(ABSOLUTE_OVERLAY_TOLERANCE, reference_value * RELATIVE_OVERLAY_TOLERANCE)`.

**Validation and invariants**

- Rejects or diverts the path when `not isfinite(reference_value) or reference_value < 0` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `isfinite`, `max`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `_feature_metric`
- `src/landscout/common/planning_feature_contract.py` — `validate_intrinsic_planning_feature_relations`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_relation_parcel_areas`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`
- `src/landscout/stages/enrich_planning_features.py` — `_require_close`
- `src/landscout/stages/enrich_planning_features.py` — `_technical_tolerance`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcel_summaries`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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
