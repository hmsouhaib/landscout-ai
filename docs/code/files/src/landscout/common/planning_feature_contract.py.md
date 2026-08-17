# `src/landscout/common/planning_feature_contract.py`

## File identity

- Repository path: `src/landscout/common/planning_feature_contract.py`
- File type: Python source
- Layer: internal common contract
- Domain: planning
- Responsibility: Validates stored factual planning relation semantics without rereading GPU geometry.
- Source SHA256: `b70e9bd8a63dedae29603d3cae1ef7d81ee776c25c7b53389fcc7a0736a73f36`

## 1. Purpose

Validates stored factual planning relation semantics without rereading GPU geometry.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import math`
- `from numbers import Integral, Real`

### Third-party packages

- `import numpy as np`
- `import pandas as pd`

### Internal LandScout imports

- `from landscout.common.planning_overlay import technical_overlay_tolerance`

## 4. Contract taxonomy

### A. Python constants

#### `RELATION_FLOAT_COLUMNS`

```python
RELATION_FLOAT_COLUMNS = frozenset(
    {
        "parcel_metric_area_m2",
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_contract.py::<module>` (value reference), `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` (value reference).

#### `RELATION_COUNT_COLUMNS`

```python
RELATION_COUNT_COLUMNS = frozenset(
    {
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_contract.py::<module>` (value reference), `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` (value reference).

#### `REQUIRED_RELATION_COLUMNS`

```python
REQUIRED_RELATION_COLUMNS = frozenset(
    {"geometry_kind", "relation_type"} | RELATION_FLOAT_COLUMNS | RELATION_COUNT_COLUMNS
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` (value reference).

#### `RELATION_TYPES_BY_GEOMETRY_KIND`

```python
RELATION_TYPES_BY_GEOMETRY_KIND = {
    "SURFACE": frozenset({"AREA_OVERLAP", "TOUCH_ONLY"}),
    "LINE": frozenset({"LENGTH_OVERLAP", "TOUCH_ONLY"}),
    "POINT": frozenset({"INSIDE", "BOUNDARY_TOUCH"}),
}
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_missing`

**Exact signature**

```python
def _missing(value: object) -> bool:
```

**Purpose**

Private `planning` helper for missing; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
isinstance(missing, (bool, np.bool_)) and bool(missing)

False
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/common/planning_feature_contract.py::_number` via `_missing`.
- direct call: `src/landscout/common/planning_feature_contract.py::_count` via `_missing`.
- direct call: `src/landscout/common/planning_feature_contract.py::_require_null` via `_missing`.

**Complete source-ordered implementation**

```python
def _missing(value: object) -> bool:
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return isinstance(missing, (bool, np.bool_)) and bool(missing)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_number`

**Exact signature**

```python
def _number(value: object, label: str, *, required: bool) -> float | None:
```

**Purpose**

Private `planning` helper for number; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float | None`.
- Every observed return expression is reproduced without truncation:
```python
number

None
```

**Validation and exceptions**

- Guard with a raise path: `_missing(value)`.
- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not math.isfinite(number) or number < 0`.
- Guard with a raise path: `required`.
- Explicit raise expressions: `TypeError(f'{label} must be numeric')`, `ValueError(f'{label} must be finite and non-negative')`, `ValueError(f'{label} must not be null')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` via `_number`.

**Complete source-ordered implementation**

```python
def _number(value: object, label: str, *, required: bool) -> float | None:
    if _missing(value):
        if required:
            raise ValueError(f"{label} must not be null")
        return None
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{label} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{label} must be finite and non-negative")
    return number
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_count`

**Exact signature**

```python
def _count(value: object, label: str, *, required: bool) -> int | None:
```

**Purpose**

Private `planning` helper for count; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int | None`.
- Every observed return expression is reproduced without truncation:
```python
int(value)

None
```

**Validation and exceptions**

- Guard with a raise path: `_missing(value)`.
- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0`.
- Guard with a raise path: `required`.
- Explicit raise expressions: `ValueError(f'{label} must be a strict non-negative integer')`, `ValueError(f'{label} must not be null')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` via `_count`.

**Complete source-ordered implementation**

```python
def _count(value: object, label: str, *, required: bool) -> int | None:
    if _missing(value):
        if required:
            raise ValueError(f"{label} must not be null")
        return None
    if isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0:
        raise ValueError(f"{label} must be a strict non-negative integer")
    return int(value)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_require_null`

**Exact signature**

```python
def _require_null(row: dict[str, object], columns: tuple[str, ...], kind: str) -> None:
```

**Purpose**

Private `planning` helper for require null; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((not _missing(row[column]) for column in columns))`.
- Explicit raise expressions: `ValueError(f'{kind} relation populated an unrelated metric')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` via `_require_null`.

**Complete source-ordered implementation**

```python
def _require_null(row: dict[str, object], columns: tuple[str, ...], kind: str) -> None:
    if any(not _missing(row[column]) for column in columns):
        raise ValueError(f"{kind} relation populated an unrelated metric")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_intrinsic_planning_feature_relations`

**Exact signature**

```python
def validate_intrinsic_planning_feature_relations(frame: pd.DataFrame) -> None:
```

**Purpose**

Validate stored relation types, metrics, nulls, and count semantics locally.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `not REQUIRED_RELATION_COLUMNS.issubset(frame.columns)`.
- Guard with a raise path: `allowed is None`.
- Guard with a raise path: `not isinstance(relation_type, str) or relation_type not in allowed`.
- Guard with a raise path: `parcel_area <= 0`.
- Guard with a raise path: `kind == 'SURFACE'`.
- Guard with a raise path: `feature_area <= 0`.
- Guard with a raise path: `relation_type != expected_type`.
- Guard with a raise path: `area - parcel_area > technical_overlay_tolerance(parcel_area)`.
- Guard with a raise path: `area - feature_area > technical_overlay_tolerance(feature_area)`.
- Guard with a raise path: `abs(parcel_pct - expected_parcel_pct) > pct_tolerance or abs(feature_pct - expected_feature_pct) > pct_tolerance`.
- Guard with a raise path: `kind == 'LINE'`.
- Guard with a raise path: `source_length <= 0`.
- Guard with a raise path: `relation_type != expected_type`.
- Guard with a raise path: `length - source_length > technical_overlay_tolerance(source_length)`.
- Guard with a raise path: `member_count <= 0`.
- Guard with a raise path: `inside + boundary > member_count`.
- Guard with a raise path: `relation_type == 'INSIDE' and inside < 1`.
- Guard with a raise path: `relation_type == 'BOUNDARY_TOUCH' and (inside != 0 or boundary < 1)`.
- Explicit raise expressions: `TypeError('planning relations must be a DataFrame')`, `ValueError('BOUNDARY_TOUCH relation type requires only boundary point members')`, `ValueError('INSIDE relation type requires an inside point member')`, `ValueError('line intersection exceeds source line length')`, `ValueError('line relation type is inconsistent with its length')`, `ValueError('planning relation factual metric schema is incomplete')`, `ValueError('planning relation geometry kind is invalid')`, `ValueError('planning relations contain duplicate columns')`, `ValueError('point covered members exceed source members')`, `ValueError('point member count must be positive')`, `ValueError('relation parcel metric area must be positive')`, `ValueError('source line length must be positive')`, `ValueError('surface feature area must be positive')`, `ValueError('surface intersection exceeds feature area')`, `ValueError('surface intersection exceeds parcel area')`, `ValueError('surface relation percentages are inconsistent')`, `ValueError('surface relation type is inconsistent with its area')`, `ValueError(f'{kind} relation type is incompatible with its geometry kind')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `RELATION_TYPES_BY_GEOMETRY_KIND.get`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `src/landscout/common/bess_application_contract.py::<module>` via `from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)`.
- import: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)`.
- import: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `validate_intrinsic_planning_feature_relations`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_relation_semantics` via `validate_intrinsic_planning_feature_relations`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_shared_intrinsic_relation_semantics_reject_every_invalid_case` via `validate_intrinsic_planning_feature_relations`.

**Complete source-ordered implementation**

```python
def validate_intrinsic_planning_feature_relations(frame: pd.DataFrame) -> None:
    """Validate stored relation types, metrics, nulls, and count semantics locally."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError("planning relations must be a DataFrame")
    if frame.columns.duplicated().any():
        raise ValueError("planning relations contain duplicate columns")
    if not REQUIRED_RELATION_COLUMNS.issubset(frame.columns):
        raise ValueError("planning relation factual metric schema is incomplete")
    for column in RELATION_FLOAT_COLUMNS:
        for value in frame[column].tolist():
            _number(value, f"relation {column}", required=False)
    for column in RELATION_COUNT_COLUMNS:
        for value in frame[column].tolist():
            _count(value, f"relation {column}", required=False)

    for row in frame.to_dict("records"):
        kind = row["geometry_kind"]
        relation_type = row["relation_type"]
        allowed = RELATION_TYPES_BY_GEOMETRY_KIND.get(kind)
        if allowed is None:
            raise ValueError("planning relation geometry kind is invalid")
        if not isinstance(relation_type, str) or relation_type not in allowed:
            raise ValueError(
                f"{kind} relation type is incompatible with its geometry kind"
            )
        parcel_area = _number(
            row["parcel_metric_area_m2"],
            "relation parcel metric area",
            required=True,
        )
        assert parcel_area is not None
        if parcel_area <= 0:
            raise ValueError("relation parcel metric area must be positive")

        if kind == "SURFACE":
            feature_area = _number(
                row["feature_area_m2"], "surface feature area", required=True
            )
            area = _number(
                row["intersection_area_m2"],
                "surface intersection area",
                required=True,
            )
            parcel_pct = _number(
                row["parcel_share_pct"], "surface parcel share", required=True
            )
            feature_pct = _number(
                row["feature_share_pct"], "surface feature share", required=True
            )
            assert None not in (feature_area, area, parcel_pct, feature_pct)
            assert feature_area is not None and area is not None
            assert parcel_pct is not None and feature_pct is not None
            if feature_area <= 0:
                raise ValueError("surface feature area must be positive")
            expected_type = "AREA_OVERLAP" if area > 0 else "TOUCH_ONLY"
            if relation_type != expected_type:
                raise ValueError("surface relation type is inconsistent with its area")
            if area - parcel_area > technical_overlay_tolerance(parcel_area):
                raise ValueError("surface intersection exceeds parcel area")
            if area - feature_area > technical_overlay_tolerance(feature_area):
                raise ValueError("surface intersection exceeds feature area")
            expected_parcel_pct = 100.0 * area / parcel_area
            expected_feature_pct = 100.0 * area / feature_area
            pct_tolerance = max(
                100.0 * technical_overlay_tolerance(parcel_area) / parcel_area,
                100.0 * technical_overlay_tolerance(feature_area) / feature_area,
            )
            if (
                abs(parcel_pct - expected_parcel_pct) > pct_tolerance
                or abs(feature_pct - expected_feature_pct) > pct_tolerance
            ):
                raise ValueError("surface relation percentages are inconsistent")
            _require_null(
                row,
                (
                    "source_line_length_m",
                    "intersection_length_m",
                    *RELATION_COUNT_COLUMNS,
                ),
                kind,
            )
        elif kind == "LINE":
            source_length = _number(
                row["source_line_length_m"], "source line length", required=True
            )
            length = _number(
                row["intersection_length_m"],
                "line intersection length",
                required=True,
            )
            assert source_length is not None and length is not None
            if source_length <= 0:
                raise ValueError("source line length must be positive")
            expected_type = "LENGTH_OVERLAP" if length > 0 else "TOUCH_ONLY"
            if relation_type != expected_type:
                raise ValueError("line relation type is inconsistent with its length")
            if length - source_length > technical_overlay_tolerance(source_length):
                raise ValueError("line intersection exceeds source line length")
            _require_null(
                row,
                (
                    "feature_area_m2",
                    "intersection_area_m2",
                    "parcel_share_pct",
                    "feature_share_pct",
                    *RELATION_COUNT_COLUMNS,
                ),
                kind,
            )
        else:
            member_count = _count(
                row["point_member_count"], "point member count", required=True
            )
            inside = _count(
                row["point_members_inside_count"],
                "point inside member count",
                required=True,
            )
            boundary = _count(
                row["point_members_boundary_count"],
                "point boundary member count",
                required=True,
            )
            assert (
                member_count is not None and inside is not None and boundary is not None
            )
            if member_count <= 0:
                raise ValueError("point member count must be positive")
            if inside + boundary > member_count:
                raise ValueError("point covered members exceed source members")
            if relation_type == "INSIDE" and inside < 1:
                raise ValueError("INSIDE relation type requires an inside point member")
            if relation_type == "BOUNDARY_TOUCH" and (inside != 0 or boundary < 1):
                raise ValueError(
                    "BOUNDARY_TOUCH relation type requires only boundary point members"
                )
            _require_null(
                row,
                (
                    "feature_area_m2",
                    "source_line_length_m",
                    "intersection_area_m2",
                    "intersection_length_m",
                    "parcel_share_pct",
                    "feature_share_pct",
                ),
                kind,
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `RELATION_FLOAT_COLUMNS` — canonical or derived frame-column schema

```python
RELATION_FLOAT_COLUMNS = frozenset(
    {
        "parcel_metric_area_m2",
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `feature_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 2 | `feature_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 3 | `intersection_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 4 | `intersection_length_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 5 | `parcel_metric_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 6 | `parcel_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 7 | `source_line_length_m` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `RELATION_COUNT_COLUMNS` — canonical or derived frame-column schema

```python
RELATION_COUNT_COLUMNS = frozenset(
    {
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `point_member_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 2 | `point_members_boundary_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 3 | `point_members_inside_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |

### `REQUIRED_RELATION_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
REQUIRED_RELATION_COLUMNS = frozenset(
    {"geometry_kind", "relation_type"} | RELATION_FLOAT_COLUMNS | RELATION_COUNT_COLUMNS
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `feature_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 2 | `feature_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 3 | `geometry_kind` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `intersection_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 5 | `intersection_length_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 6 | `parcel_metric_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 7 | `parcel_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 8 | `point_member_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 9 | `point_members_boundary_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 10 | `point_members_inside_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 11 | `relation_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `source_line_length_m` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the planning flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
