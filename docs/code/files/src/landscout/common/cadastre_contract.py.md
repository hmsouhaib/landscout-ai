# `src/landscout/common/cadastre_contract.py`

## File identity

- Repository path: `src/landscout/common/cadastre_contract.py`
- File type: Python source
- Primary responsibility: Provides the internal exact geometry-status vocabulary guard shared by cadastral filtering stages.
- Layer / domain: `internal common contract/utility` / `cadastre`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `d7dc15892f65fbf8935051af26e519b82c98b74defa2e1b2f09c298427903971`

## 1. Purpose

Provides the internal exact geometry-status vocabulary guard shared by cadastral filtering stages.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `cadastre` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from collections.abc import Iterable` — required by the implementation paths and symbols documented below.

### Third-party

- None.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `CADASTRE_GEOMETRY_STATUSES` | `frozenset({"VALID", "INVALID"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `validate_cadastre_geometry_statuses`

**Signature**

```python
def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
```

**Purpose**

Require the exact geometry-status vocabulary emitted by normalization.

**Inputs**

- `values` (`Iterable[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `any((type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES for value in values))`. When true: Raises `ValueError('geometry_status must contain only exact VALID or INVALID strings')`.

**Validation and invariants**

- Rejects or diverts the path when `any((type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES for value in values))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `any`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_shape.py` — `enrich_parcel_shapes`
- `src/landscout/stages/filter_parcels.py` — `filter_parcels_by_area`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

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

This file contributes to LandScout's `cadastre` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
