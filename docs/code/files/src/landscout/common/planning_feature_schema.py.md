# `src/landscout/common/planning_feature_schema.py`

## File identity

- Repository path: `src/landscout/common/planning_feature_schema.py`
- File type: Python source
- Layer: internal common contract
- Domain: planning
- Responsibility: Centralizes ordered normalized, CNIG-coded, and BESS-application feature/relation schemas and dtypes.
- Source SHA256: `7f1921b20cceb88c35232a99677fdcc3b5c247f67f380eae73e1d79e59bb0d18`

## 1. Purpose

Centralizes ordered normalized, CNIG-coded, and BESS-application feature/relation schemas and dtypes.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from typing import Literal`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pyproj import CRS`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `COMMON_FEATURE_COLUMNS`

```python
COMMON_FEATURE_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "regulation_filename_raw",
    "regulation_url_raw",
    "source_document_reference_raw",
    "source_validity_date_raw",
    "source_provider",
    "source_portal",
    "source_commune_code",
    "source_document_id",
    "source_document_type",
    "source_archive_name",
    "source_archive_sha256",
    "source_layer",
    "source_standard_model",
    "source_crs",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_schema.py::<module>` (value reference).

#### `SURFACE_FEATURE_COLUMNS`

```python
SURFACE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_area_m2")
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_schema.py::<module>` (value reference).

#### `LINE_FEATURE_COLUMNS`

```python
LINE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_length_m")
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_schema.py::<module>` (value reference).

#### `POINT_FEATURE_COLUMNS`

```python
POINT_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "point_member_count")
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_schema.py::<module>` (value reference).

#### `NORMALIZED_FEATURE_COLUMNS`

```python
NORMALIZED_FEATURE_COLUMNS = {
    "SURFACE": SURFACE_FEATURE_COLUMNS,
    "LINE": LINE_FEATURE_COLUMNS,
    "POINT": POINT_FEATURE_COLUMNS,
}
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import), `src/landscout/common/planning_feature_schema.py::normalized_feature_dtypes` (value reference), `src/landscout/common/planning_feature_schema.py::feature_columns` (value reference), `src/landscout/stages/enrich_planning_features.py::_canonical_catalog_dtypes` (value reference), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` (value reference).

#### `RELATION_COLUMNS`

```python
RELATION_COLUMNS = (
    "parcel_id",
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "relation_type",
    "parcel_metric_area_m2",
    "feature_area_m2",
    "source_line_length_m",
    "intersection_area_m2",
    "intersection_length_m",
    "parcel_share_pct",
    "feature_share_pct",
    "point_member_count",
    "point_members_inside_count",
    "point_members_boundary_count",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_validity_date_raw",
    "regulation_filename_raw",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import), `src/landscout/common/planning_feature_schema.py::<module>` (value reference), `src/landscout/common/planning_feature_schema.py::relation_columns` (value reference), `src/landscout/stages/enrich_planning_features.py::_empty_relations` (value reference), `src/landscout/stages/enrich_planning_features.py::_build_relation_tables` (value reference), `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_relations` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` (value reference).

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import), `src/landscout/common/planning_feature_schema.py::<module>` (value reference), `src/landscout/stages/enrich_planning_features.py::_point_relations` (value reference), `src/landscout/stages/enrich_planning_features.py::_empty_relations` (value reference), `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_relations` (value reference).

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import), `src/landscout/common/planning_feature_schema.py::<module>` (value reference), `src/landscout/stages/enrich_planning_features.py::_surface_relations` (value reference), `src/landscout/stages/enrich_planning_features.py::_line_relations` (value reference), `src/landscout/stages/enrich_planning_features.py::_empty_relations` (value reference), `src/landscout/stages/enrich_planning_features.py::_build_relation_tables` (value reference).

#### `RELATION_STRING_COLUMNS`

```python
RELATION_STRING_COLUMNS = (
    frozenset(RELATION_COLUMNS) - RELATION_FLOAT_COLUMNS - (RELATION_COUNT_COLUMNS)
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import), `src/landscout/stages/enrich_planning_features.py::_build_relation_tables` (value reference).

#### `OFFICIAL_CODE_COLUMNS`

```python
OFFICIAL_CODE_COLUMNS = (
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::<module>` (import), `src/landscout/common/planning_feature_schema.py::<module>` (value reference), `src/landscout/common/planning_feature_schema.py::feature_columns` (value reference), `src/landscout/common/planning_feature_schema.py::relation_columns` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_coded_catalog` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_coded_relations` (value reference).

#### `_COMMON_STR_DTYPES`

```python
_COMMON_STR_DTYPES = {
    column: "str"
    for column in COMMON_FEATURE_COLUMNS
    if column not in {"text_raw", "regulation_filename_raw", "regulation_url_raw"}
}
```

Canonical Pandas/GeoPandas dtype contract aligned with the named schema. Consumers include `src/landscout/common/planning_feature_schema.py::<module>` (value reference).

#### `NORMALIZED_FEATURE_DTYPES`

```python
NORMALIZED_FEATURE_DTYPES: dict[GeometryKind, tuple[str, ...]] = {
    "SURFACE": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "str",
            "regulation_filename_raw": "str",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "feature_area_m2": "float64",
        }[column]
        for column in SURFACE_FEATURE_COLUMNS
    ),
    "LINE": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "object",
            "regulation_filename_raw": "object",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "feature_length_m": "float64",
        }[column]
        for column in LINE_FEATURE_COLUMNS
    ),
    "POINT": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "object",
            "regulation_filename_raw": "object",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "point_member_count": "int64",
        }[column]
        for column in POINT_FEATURE_COLUMNS
    ),
}
```

Canonical Pandas/GeoPandas dtype contract aligned with the named schema. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import), `src/landscout/common/planning_feature_schema.py::normalized_feature_dtypes` (value reference), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (value reference).

#### `NORMALIZED_RELATION_DTYPES`

```python
NORMALIZED_RELATION_DTYPES = tuple(
    "float64"
    if column in RELATION_FLOAT_COLUMNS
    else "Int64"
    if column in RELATION_COUNT_COLUMNS
    else "str"
    for column in RELATION_COLUMNS
)
```

Canonical Pandas/GeoPandas dtype contract aligned with the named schema. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import), `tests/unit/test_resolve_planning_feature_codes.py::<module>` (import), `src/landscout/common/planning_feature_schema.py::relation_dtypes` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` (value reference), `tests/unit/test_resolve_planning_feature_codes.py::_canonical_relation_schema` (value reference).

#### `OFFICIAL_CODE_DTYPES`

```python
OFFICIAL_CODE_DTYPES = tuple("str" for _ in OFFICIAL_CODE_COLUMNS)
```

Canonical Pandas/GeoPandas dtype contract aligned with the named schema. Consumers include `src/landscout/common/planning_feature_schema.py::feature_dtypes` (value reference), `src/landscout/common/planning_feature_schema.py::relation_dtypes` (value reference).


### B. Type aliases and closed domains

#### `GeometryKind`

```python
GeometryKind = Literal["SURFACE", "LINE", "POINT"]
```

Closed planning-feature geometry-family domain: SURFACE, LINE, or POINT. Enforced/consumed by `src/landscout/common/bess_application_contract.py::<module>` (import), `src/landscout/stages/resolve_planning_feature_codes.py::<module>` (import), `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` (value reference), `src/landscout/common/planning_feature_schema.py::<module>` (type annotation), `src/landscout/common/planning_feature_schema.py::normalized_feature_dtypes` (type annotation), `src/landscout/common/planning_feature_schema.py::feature_columns` (type annotation), `src/landscout/common/planning_feature_schema.py::feature_dtypes` (type annotation), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` (value reference).

#### `IndexClass`

```python
IndexClass = Literal["Index", "RangeIndex"]
```

Portable frame-signature index-class domain: Index or RangeIndex. Enforced/consumed by `src/landscout/common/planning_feature_schema.py::validate_canonical_frame_schema` (type annotation).


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `normalized_feature_dtypes`

**Exact signature**

```python
def normalized_feature_dtypes(
    geometry_kind: GeometryKind,
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
```

**Purpose**

Return exact factual dtypes, including deterministic all-null raw fields.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(dtypes)

tuple(dtypes)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `NORMALIZED_FEATURE_COLUMNS[geometry_kind].index`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `dtypes[position]`.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`.
- direct call: `src/landscout/common/planning_feature_schema.py::feature_dtypes` via `normalized_feature_dtypes`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_canonical_catalog_dtypes` via `normalized_feature_dtypes`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `normalized_feature_dtypes`.

**Complete source-ordered implementation**

```python
def normalized_feature_dtypes(
    geometry_kind: GeometryKind,
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
    """Return exact factual dtypes, including deterministic all-null raw fields."""

    dtypes = list(NORMALIZED_FEATURE_DTYPES[geometry_kind])
    if frame is None or frame.empty:
        return tuple(dtypes)
    # Pandas/Parquet preserve an all-null optional raw source field as object. The
    # null pattern is factual input, so it is the sole deterministic variant.
    for column in ("text_raw", "regulation_filename_raw", "regulation_url_raw"):
        if column not in frame.columns:
            continue
        position = NORMALIZED_FEATURE_COLUMNS[geometry_kind].index(column)
        dtypes[position] = "object" if frame[column].isna().all() else "str"
    return tuple(dtypes)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `feature_columns`

**Exact signature**

```python
def feature_columns(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
) -> tuple[str, ...]:
```

**Purpose**

Return one exact ordered feature schema with deterministic suffixes.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
(*NORMALIZED_FEATURE_COLUMNS[geometry_kind], *OFFICIAL_CODE_COLUMNS, *suffix)
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

- import: `src/landscout/common/bess_application_contract.py::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `feature_columns`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `feature_columns`.

**Complete source-ordered implementation**

```python
def feature_columns(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
) -> tuple[str, ...]:
    """Return one exact ordered feature schema with deterministic suffixes."""

    return (*NORMALIZED_FEATURE_COLUMNS[geometry_kind], *OFFICIAL_CODE_COLUMNS, *suffix)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `feature_dtypes`

**Exact signature**

```python
def feature_dtypes(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
```

**Purpose**

Return matching exact feature dtypes with deterministic suffixes.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
(*normalized_feature_dtypes(geometry_kind, frame), *OFFICIAL_CODE_DTYPES, *suffix)
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

- import: `src/landscout/common/bess_application_contract.py::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `feature_dtypes`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `feature_dtypes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_canonical_empty_coded_result` via `feature_dtypes`.

**Complete source-ordered implementation**

```python
def feature_dtypes(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
    """Return matching exact feature dtypes with deterministic suffixes."""

    return (
        *normalized_feature_dtypes(geometry_kind, frame),
        *OFFICIAL_CODE_DTYPES,
        *suffix,
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `relation_columns`

**Exact signature**

```python
def relation_columns(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
```

**Purpose**

Return one exact ordered relation schema with deterministic suffixes.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
(*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)
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

- import: `src/landscout/common/bess_application_contract.py::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.common.planning_feature_schema import relation_columns, relation_dtypes`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `relation_columns`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `relation_columns`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `relation_columns`.

**Complete source-ordered implementation**

```python
def relation_columns(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return one exact ordered relation schema with deterministic suffixes."""

    return (*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `relation_dtypes`

**Exact signature**

```python
def relation_dtypes(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
```

**Purpose**

Return matching exact relation dtypes with deterministic suffixes.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
(*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)
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

- import: `src/landscout/common/bess_application_contract.py::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.common.planning_feature_schema import relation_columns, relation_dtypes`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `relation_dtypes`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `relation_dtypes`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `relation_dtypes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_canonical_empty_coded_result` via `relation_dtypes`.

**Complete source-ordered implementation**

```python
def relation_dtypes(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return matching exact relation dtypes with deterministic suffixes."""

    return (*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_canonical_frame_schema`

**Exact signature**

```python
def validate_canonical_frame_schema(
    frame: pd.DataFrame,
    *,
    columns: tuple[str, ...],
    dtypes: tuple[str, ...],
    label: str,
    geospatial: bool,
    index_class: IndexClass = "Index",
) -> None:
```

**Purpose**

Reject any deviation from one complete persisted frame-schema contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `tuple(frame.columns) != columns or tuple((str(dtype) for dtype in frame.dtypes)) != dtypes`.
- Guard with a raise path: `type(index) is not expected_index_type or list(index.names) != [None] or str(index.dtype) != 'int64'`.
- Guard with a raise path: `index_class == 'RangeIndex' and (index.start != 0 or index.stop != len(frame) or index.step != 1)`.
- Guard with a raise path: `geospatial`.
- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `frame.geometry.name != 'geometry' or frame.crs is None`.
- Guard with a raise path: `not canonical_crs`.
- Guard with a raise path: `isinstance(frame, gpd.GeoDataFrame)`.
- Explicit raise expressions: `TypeError(f'{label} must be a DataFrame')`, `TypeError(f'{label} must be a GeoDataFrame')`, `TypeError(f'{label} must not be a GeoDataFrame')`, `ValueError(f'{label} canonical CRS differs from EPSG:2154')`, `ValueError(f'{label} canonical CRS is invalid')`, `ValueError(f'{label} canonical column, geometry, or dtype schema differs')`, `ValueError(f'{label} canonical geometry or CRS metadata differs')`, `ValueError(f'{label} canonical index schema differs')`, `ValueError(f'{label} canonical range index differs')`, `ValueError(f'{label} contains duplicate columns')`.

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

- import: `src/landscout/common/bess_application_contract.py::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`.
- import: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `validate_canonical_frame_schema`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `validate_canonical_frame_schema`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `validate_canonical_frame_schema`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `validate_canonical_frame_schema`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `validate_canonical_frame_schema`.

**Complete source-ordered implementation**

```python
def validate_canonical_frame_schema(
    frame: pd.DataFrame,
    *,
    columns: tuple[str, ...],
    dtypes: tuple[str, ...],
    label: str,
    geospatial: bool,
    index_class: IndexClass = "Index",
) -> None:
    """Reject any deviation from one complete persisted frame-schema contract."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError(f"{label} must be a DataFrame")
    if frame.columns.duplicated().any():
        raise ValueError(f"{label} contains duplicate columns")
    if (
        tuple(frame.columns) != columns
        or tuple(str(dtype) for dtype in frame.dtypes) != dtypes
    ):
        raise ValueError(
            f"{label} canonical column, geometry, or dtype schema differs"
        )
    index = frame.index
    expected_index_type = pd.Index if index_class == "Index" else pd.RangeIndex
    if type(index) is not expected_index_type or list(index.names) != [None] or str(
        index.dtype
    ) != "int64":
        raise ValueError(f"{label} canonical index schema differs")
    if index_class == "RangeIndex" and (
        index.start != 0 or index.stop != len(frame) or index.step != 1
    ):
        raise ValueError(f"{label} canonical range index differs")
    if geospatial:
        if not isinstance(frame, gpd.GeoDataFrame):
            raise TypeError(f"{label} must be a GeoDataFrame")
        if frame.geometry.name != "geometry" or frame.crs is None:
            raise ValueError(f"{label} canonical geometry or CRS metadata differs")
        try:
            canonical_crs = CRS.from_user_input(frame.crs).equals(CRS.from_epsg(2154))
        except Exception as error:
            raise ValueError(f"{label} canonical CRS is invalid") from error
        if not canonical_crs:
            raise ValueError(f"{label} canonical CRS differs from EPSG:2154")
    elif isinstance(frame, gpd.GeoDataFrame):
        raise TypeError(f"{label} must not be a GeoDataFrame")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `COMMON_FEATURE_COLUMNS` — canonical or derived frame-column schema

```python
COMMON_FEATURE_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "regulation_filename_raw",
    "regulation_url_raw",
    "source_document_reference_raw",
    "source_validity_date_raw",
    "source_provider",
    "source_portal",
    "source_commune_code",
    "source_document_id",
    "source_document_type",
    "source_archive_name",
    "source_archive_sha256",
    "source_layer",
    "source_standard_model",
    "source_crs",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `planning_feature_id` | Pandas nullable string dtype | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_identity_kind` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_identity_field` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `logical_layer` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `geometry_kind` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `type_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `subtype_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `label_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `text_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `regulation_filename_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `regulation_url_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_document_reference_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `source_validity_date_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_provider` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_portal` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `source_commune_code` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `source_document_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `source_document_type` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 21 | `source_archive_name` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 22 | `source_archive_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `source_layer` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 24 | `source_standard_model` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `source_crs` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `SURFACE_FEATURE_COLUMNS` — canonical or derived frame-column schema

```python
SURFACE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_area_m2")
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `planning_feature_id` | Pandas nullable string dtype | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_identity_kind` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_identity_field` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `logical_layer` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `geometry_kind` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `type_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `subtype_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `label_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `text_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `regulation_filename_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `regulation_url_raw` | Pandas object dtype retained for heterogeneous/nullable source values | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_document_reference_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `source_validity_date_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_provider` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_portal` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `source_commune_code` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `source_document_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `source_document_type` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 21 | `source_archive_name` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 22 | `source_archive_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `source_layer` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 24 | `source_standard_model` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `source_crs` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 26 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 27 | `feature_area_m2` | NumPy float64 | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |

### `LINE_FEATURE_COLUMNS` — canonical or derived frame-column schema

```python
LINE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_length_m")
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `planning_feature_id` | Pandas nullable string dtype | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_identity_kind` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_identity_field` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `logical_layer` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `geometry_kind` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `type_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `subtype_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `label_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `text_raw` | Pandas object dtype retained for heterogeneous/nullable source values | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `regulation_filename_raw` | Pandas object dtype retained for heterogeneous/nullable source values | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `regulation_url_raw` | Pandas object dtype retained for heterogeneous/nullable source values | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_document_reference_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `source_validity_date_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_provider` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_portal` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `source_commune_code` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `source_document_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `source_document_type` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 21 | `source_archive_name` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 22 | `source_archive_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `source_layer` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 24 | `source_standard_model` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `source_crs` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 26 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 27 | `feature_length_m` | NumPy float64 | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |

### `POINT_FEATURE_COLUMNS` — canonical or derived frame-column schema

```python
POINT_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "point_member_count")
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `planning_feature_id` | Pandas nullable string dtype | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_identity_kind` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_identity_field` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `logical_layer` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `geometry_kind` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `type_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `subtype_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `label_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `text_raw` | Pandas object dtype retained for heterogeneous/nullable source values | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `regulation_filename_raw` | Pandas object dtype retained for heterogeneous/nullable source values | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `regulation_url_raw` | Pandas object dtype retained for heterogeneous/nullable source values | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_document_reference_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `source_validity_date_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_provider` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_portal` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `source_commune_code` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `source_document_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `source_document_type` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 21 | `source_archive_name` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 22 | `source_archive_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `source_layer` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 24 | `source_standard_model` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `source_crs` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 26 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 27 | `point_member_count` | NumPy int64 | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |

### `NORMALIZED_FEATURE_COLUMNS` — canonical or derived frame-column schema

```python
NORMALIZED_FEATURE_COLUMNS = {
    "SURFACE": SURFACE_FEATURE_COLUMNS,
    "LINE": LINE_FEATURE_COLUMNS,
    "POINT": POINT_FEATURE_COLUMNS,
}
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `SURFACE` | ('str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'object', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'geometry', 'float64') | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `LINE` | ('str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'object', 'object', 'object', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'geometry', 'float64') | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `POINT` | ('str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'object', 'object', 'object', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'geometry', 'int64') | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `RELATION_COLUMNS` — canonical or derived frame-column schema

```python
RELATION_COLUMNS = (
    "parcel_id",
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "relation_type",
    "parcel_metric_area_m2",
    "feature_area_m2",
    "source_line_length_m",
    "intersection_area_m2",
    "intersection_length_m",
    "parcel_share_pct",
    "feature_share_pct",
    "point_member_count",
    "point_members_inside_count",
    "point_members_boundary_count",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_validity_date_raw",
    "regulation_filename_raw",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_id` | Pandas nullable string dtype | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `planning_feature_id` | Pandas nullable string dtype | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `source_feature_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_identity_kind` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_identity_field` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `logical_layer` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `geometry_kind` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `type_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `subtype_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `label_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `text_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `relation_type` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `parcel_metric_area_m2` | NumPy float64 | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 15 | `feature_area_m2` | NumPy float64 | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 16 | `source_line_length_m` | NumPy float64 | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `intersection_area_m2` | NumPy float64 | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 18 | `intersection_length_m` | NumPy float64 | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 19 | `parcel_share_pct` | NumPy float64 | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 20 | `feature_share_pct` | NumPy float64 | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 21 | `point_member_count` | Pandas nullable Int64 | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 22 | `point_members_inside_count` | Pandas nullable Int64 | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 23 | `point_members_boundary_count` | Pandas nullable Int64 | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 24 | `source_document_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `source_archive_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 26 | `source_layer` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 27 | `source_validity_date_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 28 | `regulation_filename_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

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

### `RELATION_STRING_COLUMNS` — canonical or derived frame-column schema

```python
RELATION_STRING_COLUMNS = (
    frozenset(RELATION_COLUMNS) - RELATION_FLOAT_COLUMNS - (RELATION_COUNT_COLUMNS)
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `geometry_kind` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `label_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `logical_layer` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 6 | `planning_feature_id` | Pandas nullable string dtype | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 7 | `regulation_filename_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `relation_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `source_archive_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 10 | `source_document_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_feature_id` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `source_identity_field` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `source_identity_kind` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_layer` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `source_validity_date_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `subtype_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `text_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `type_code_raw` | Pandas nullable string dtype | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `OFFICIAL_CODE_COLUMNS` — canonical or derived frame-column schema

```python
OFFICIAL_CODE_COLUMNS = (
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `official_code_status` | Pandas nullable string dtype | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 2 | `official_code_label` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `official_legal_reference` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `official_regulation_reference` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `official_code_source_url` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `official_code_profile` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `official_code_profile_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `_COMMON_STR_DTYPES` — dtype contract aligned with a canonical schema

```python
_COMMON_STR_DTYPES = {
    column: "str"
    for column in COMMON_FEATURE_COLUMNS
    if column not in {"text_raw", "regulation_filename_raw", "regulation_url_raw"}
}
```

### `NORMALIZED_FEATURE_DTYPES` — dtype contract aligned with a canonical schema

```python
NORMALIZED_FEATURE_DTYPES: dict[GeometryKind, tuple[str, ...]] = {
    "SURFACE": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "str",
            "regulation_filename_raw": "str",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "feature_area_m2": "float64",
        }[column]
        for column in SURFACE_FEATURE_COLUMNS
    ),
    "LINE": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "object",
            "regulation_filename_raw": "object",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "feature_length_m": "float64",
        }[column]
        for column in LINE_FEATURE_COLUMNS
    ),
    "POINT": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "object",
            "regulation_filename_raw": "object",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "point_member_count": "int64",
        }[column]
        for column in POINT_FEATURE_COLUMNS
    ),
}
```

### `NORMALIZED_RELATION_DTYPES` — dtype contract aligned with a canonical schema

```python
NORMALIZED_RELATION_DTYPES = tuple(
    "float64"
    if column in RELATION_FLOAT_COLUMNS
    else "Int64"
    if column in RELATION_COUNT_COLUMNS
    else "str"
    for column in RELATION_COLUMNS
)
```

### `OFFICIAL_CODE_DTYPES` — dtype contract aligned with a canonical schema

```python
OFFICIAL_CODE_DTYPES = tuple("str" for _ in OFFICIAL_CODE_COLUMNS)
```


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
