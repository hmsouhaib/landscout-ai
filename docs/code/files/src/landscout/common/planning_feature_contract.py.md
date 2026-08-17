# `src/landscout/common/planning_feature_contract.py`

## File identity

- Repository path: `src/landscout/common/planning_feature_contract.py`
- File type: Python source
- Primary responsibility: Validates stored factual planning relation semantics without rereading GPU geometry.
- Layer / domain: `internal common contract/utility` / `planning`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `b70e9bd8a63dedae29603d3cae1ef7d81ee776c25c7b53389fcc7a0736a73f36`

## 1. Purpose

Validates stored factual planning relation semantics without rereading GPU geometry.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.

### Third-party

- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `RELATION_FLOAT_COLUMNS` | `frozenset( { "parcel_metric_area_m2", "feature_area_m2", "source_line_length_m", "intersection_area_m2", "intersection_length_m", "parcel_share_pct", "feature_share_pct", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_COUNT_COLUMNS` | `frozenset( { "point_member_count", "point_members_inside_count", "point_members_boundary_count", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `REQUIRED_RELATION_COLUMNS` | `frozenset( {"geometry_kind", "relation_type"} &#124; RELATION_FLOAT_COLUMNS &#124; RELATION_COUNT_COLUMNS )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_TYPES_BY_GEOMETRY_KIND` | `{ "SURFACE": frozenset({"AREA_OVERLAP", "TOUCH_ONLY"}), "LINE": frozenset({"LENGTH_OVERLAP", "TOUCH_ONLY"}), "POINT": frozenset({"INSIDE", "BOUNDARY_TOUCH"}), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_missing`

**Signature**

```python
def _missing(value: object) -> bool:
```

**Purpose**

Implements missing according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `isinstance(missing, (bool, np.bool_)) and bool(missing)`; `False`.

**Algorithm**

1. Runs guarded operation: Computes `missing` from `pd.isna(value)`. Handles `(TypeError, ValueError)`.
2. Returns `isinstance(missing, (bool, np.bool_)) and bool(missing)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/common/planning_feature_contract.py` — `_count`
- `src/landscout/common/planning_feature_contract.py` — `_number`
- `src/landscout/common/planning_feature_contract.py` — `_require_null`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_number`

**Signature**

```python
def _number(value: object, label: str, *, required: bool) -> float | None:
```

**Purpose**

Implements number according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `required` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float | None`. Observed return expression(s): `number`; `None`.

**Algorithm**

1. Checks `_missing(value)`. When true: Checks `required`. When true: Raises `ValueError(f'{label} must not be null')`. Returns `None`.
2. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `TypeError(f'{label} must be numeric')`.
3. Computes `number` from `float(value)`.
4. Checks `not math.isfinite(number) or number < 0`. When true: Raises `ValueError(f'{label} must be finite and non-negative')`.
5. Returns `number`.

**Validation and invariants**

- Rejects or diverts the path when `_missing(value)` is true.
- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(number) or number < 0` is true.
- Rejects or diverts the path when `required` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `TypeError`, `ValueError`, `_missing`, `float`, `isinstance`, `math.isfinite`.

**Known repository callers**

- `src/landscout/common/planning_feature_contract.py` — `validate_intrinsic_planning_feature_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_count`

**Signature**

```python
def _count(value: object, label: str, *, required: bool) -> int | None:
```

**Purpose**

Implements count according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `required` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int | None`. Observed return expression(s): `int(value)`; `None`.

**Algorithm**

1. Checks `_missing(value)`. When true: Checks `required`. When true: Raises `ValueError(f'{label} must not be null')`. Returns `None`.
2. Checks `isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0`. When true: Raises `ValueError(f'{label} must be a strict non-negative integer')`.
3. Returns `int(value)`.

**Validation and invariants**

- Rejects or diverts the path when `_missing(value)` is true.
- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0` is true.
- Rejects or diverts the path when `required` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_missing`, `int`, `isinstance`.

**Known repository callers**

- `src/landscout/common/planning_feature_contract.py` — `validate_intrinsic_planning_feature_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_require_null`

**Signature**

```python
def _require_null(row: dict[str, object], columns: tuple[str, ...], kind: str) -> None:
```

**Purpose**

Implements require null according to the exact implementation and guards in this file.

**Inputs**

- `row` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `kind` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `any((not _missing(row[column]) for column in columns))`. When true: Raises `ValueError(f'{kind} relation populated an unrelated metric')`.

**Validation and invariants**

- Rejects or diverts the path when `any((not _missing(row[column]) for column in columns))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_missing`, `any`.

**Known repository callers**

- `src/landscout/common/planning_feature_contract.py` — `validate_intrinsic_planning_feature_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_intrinsic_planning_feature_relations`

**Signature**

```python
def validate_intrinsic_planning_feature_relations(frame: pd.DataFrame) -> None:
```

**Purpose**

Validate stored relation types, metrics, nulls, and count semantics locally.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(frame, pd.DataFrame)`. When true: Raises `TypeError('planning relations must be a DataFrame')`.
2. Checks `frame.columns.duplicated().any()`. When true: Raises `ValueError('planning relations contain duplicate columns')`.
3. Checks `not REQUIRED_RELATION_COLUMNS.issubset(frame.columns)`. When true: Raises `ValueError('planning relation factual metric schema is incomplete')`.
4. Iterates `column` over `RELATION_FLOAT_COLUMNS`. For each value: Iterates `value` over `frame[column].tolist()`. For each value: Calls `_number(value, f'relation {column}', required=False)` for its validation or side effect.
5. Iterates `column` over `RELATION_COUNT_COLUMNS`. For each value: Iterates `value` over `frame[column].tolist()`. For each value: Calls `_count(value, f'relation {column}', required=False)` for its validation or side effect.
6. Iterates `row` over `frame.to_dict('records')`. For each value: Computes `kind` from `row['geometry_kind']`. Computes `relation_type` from `row['relation_type']`. Computes `allowed` from `RELATION_TYPES_BY_GEOMETRY_KIND.get(kind)`. Executes 6 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `not REQUIRED_RELATION_COLUMNS.issubset(frame.columns)` is true.
- Rejects or diverts the path when `allowed is None` is true.
- Rejects or diverts the path when `not isinstance(relation_type, str) or relation_type not in allowed` is true.
- Rejects or diverts the path when `parcel_area <= 0` is true.
- Rejects or diverts the path when `kind == 'SURFACE'` is true.
- Rejects or diverts the path when `feature_area <= 0` is true.
- Rejects or diverts the path when `relation_type != expected_type` is true.
- Rejects or diverts the path when `area - parcel_area > technical_overlay_tolerance(parcel_area)` is true.
- Rejects or diverts the path when `area - feature_area > technical_overlay_tolerance(feature_area)` is true.
- Rejects or diverts the path when `abs(parcel_pct - expected_parcel_pct) > pct_tolerance or abs(feature_pct - expected_feature_pct) > pct_tolerance` is true.
- Rejects or diverts the path when `kind == 'LINE'` is true.
- Rejects or diverts the path when `source_length <= 0` is true.
- Rejects or diverts the path when `length - source_length > technical_overlay_tolerance(source_length)` is true.
- Rejects or diverts the path when `member_count <= 0` is true.
- Rejects or diverts the path when `inside + boundary > member_count` is true.
- Rejects or diverts the path when `relation_type == 'INSIDE' and inside < 1` is true.
- Rejects or diverts the path when `relation_type == 'BOUNDARY_TOUCH' and (inside != 0 or boundary < 1)` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RELATION_TYPES_BY_GEOMETRY_KIND.get`, `REQUIRED_RELATION_COLUMNS.issubset`, `TypeError`, `ValueError`, `_count`, `_number`, `_require_null`, `abs`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `frame.to_dict`, `frame[column].tolist`, `isinstance`, `max`, `technical_overlay_tolerance`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_relation_semantics`
- `tests/unit/test_enrich_planning_features.py` — `test_shared_intrinsic_relation_semantics_reject_every_invalid_case`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_shared_intrinsic_relation_semantics_reject_every_invalid_case`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `feature_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `feature_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `point_member_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_boundary_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_inside_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_line_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |

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
