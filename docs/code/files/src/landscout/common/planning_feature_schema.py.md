# `src/landscout/common/planning_feature_schema.py`

## File identity

- Repository path: `src/landscout/common/planning_feature_schema.py`
- File type: Python source
- Layer: internal common contract
- Domain: shared validation and schema contracts
- Responsibility: Centralizes ordered normalized, CNIG-coded, and BESS-application feature/relation schemas and dtypes.
- Source SHA256: `c8b96c834d46cf9bcdddb0a4200e7a3520b94b70ed32122b591b810dce39ac1f`

## 1. STEP 7F.1A.4 contract delta

- Ruff formatting only in STEP 7F.1A.4; executable contract, values, schemas, and test intent are unchanged. The companion is refreshed because its raw bytes and SHA changed.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Centralizes ordered normalized, CNIG-coded, and BESS-application feature/relation schemas and dtypes.

The file belongs to the **internal common contract** layer and **shared validation and schema contracts** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from typing import Literal`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pyproj import CRS`

### Internal LandScout imports

- None.

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `GeometryKind`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
GeometryKind = Literal["SURFACE", "LINE", "POINT"]
```

- Qualified consumers:
  - import: `landscout.common.bess_application_contract::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.common.bess_application_contract::validate_bess_application_feature_catalogs` via `GeometryKind`
  - import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `GeometryKind`

### `IndexClass`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
IndexClass = Literal["Index", "RangeIndex"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `COMMON_FEATURE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `planning_feature_id`
  - `source_feature_id`
  - `source_identity_kind`
  - `source_identity_field`
  - `logical_layer`
  - `feature_family`
  - `geometry_kind`
  - `type_code_raw`
  - `subtype_code_raw`
  - `label_raw`
  - `text_raw`
  - `regulation_filename_raw`
  - `regulation_url_raw`
  - `source_document_reference_raw`
  - `source_validity_date_raw`
  - `source_provider`
  - `source_portal`
  - `source_commune_code`
  - `source_document_id`
  - `source_document_type`
  - `source_archive_name`
  - `source_archive_sha256`
  - `source_layer`
  - `source_standard_model`
  - `source_crs`

### `SURFACE_FEATURE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
SURFACE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_area_m2")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LINE_FEATURE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
LINE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_length_m")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POINT_FEATURE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POINT_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "point_member_count")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `NORMALIZED_FEATURE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
NORMALIZED_FEATURE_COLUMNS = {
    "SURFACE": SURFACE_FEATURE_COLUMNS,
    "LINE": LINE_FEATURE_COLUMNS,
    "POINT": POINT_FEATURE_COLUMNS,
}
```

- Qualified consumers:
  - import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.enrich_planning_features::_canonical_catalog_dtypes` via `NORMALIZED_FEATURE_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_empty_catalog` via `NORMALIZED_FEATURE_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_validate_catalog_contract` via `NORMALIZED_FEATURE_COLUMNS`

### `RELATION_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.enrich_planning_features::_empty_relations` via `RELATION_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_build_relation_tables` via `RELATION_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_compare_rebuilt_relations` via `RELATION_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_validate_normalized_planning_feature_inputs` via `RELATION_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `planning_feature_id`
  - `source_feature_id`
  - `source_identity_kind`
  - `source_identity_field`
  - `logical_layer`
  - `feature_family`
  - `geometry_kind`
  - `type_code_raw`
  - `subtype_code_raw`
  - `label_raw`
  - `text_raw`
  - `relation_type`
  - `parcel_metric_area_m2`
  - `feature_area_m2`
  - `source_line_length_m`
  - `intersection_area_m2`
  - `intersection_length_m`
  - `parcel_share_pct`
  - `feature_share_pct`
  - `point_member_count`
  - `point_members_inside_count`
  - `point_members_boundary_count`
  - `source_document_id`
  - `source_archive_sha256`
  - `source_layer`
  - `source_validity_date_raw`
  - `regulation_filename_raw`

### `RELATION_FLOAT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.enrich_planning_features::_point_relations` via `RELATION_FLOAT_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_empty_relations` via `RELATION_FLOAT_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_compare_rebuilt_relations` via `RELATION_FLOAT_COLUMNS`

### `RELATION_COUNT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RELATION_COUNT_COLUMNS = frozenset(
    {
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    }
)
```

- Qualified consumers:
  - import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.enrich_planning_features::_surface_relations` via `RELATION_COUNT_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_line_relations` via `RELATION_COUNT_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_empty_relations` via `RELATION_COUNT_COLUMNS`
  - value/type reference: `landscout.stages.enrich_planning_features::_build_relation_tables` via `RELATION_COUNT_COLUMNS`

### `RELATION_STRING_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RELATION_STRING_COLUMNS = (
    frozenset(RELATION_COLUMNS) - RELATION_FLOAT_COLUMNS - (RELATION_COUNT_COLUMNS)
)
```

- Qualified consumers:
  - import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.enrich_planning_features::_build_relation_tables` via `RELATION_STRING_COLUMNS`

### `OFFICIAL_CODE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `OFFICIAL_CODE_COLUMNS`
  - value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_catalog` via `OFFICIAL_CODE_COLUMNS`
  - value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_relations` via `OFFICIAL_CODE_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `official_code_status`
  - `official_code_label`
  - `official_legal_reference`
  - `official_regulation_reference`
  - `official_code_source_url`
  - `official_code_profile`
  - `official_code_profile_sha256`

### `_COMMON_STR_DTYPES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_COMMON_STR_DTYPES = {
    column: "str"
    for column in COMMON_FEATURE_COLUMNS
    if column not in {"text_raw", "regulation_filename_raw", "regulation_url_raw"}
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `NORMALIZED_FEATURE_DTYPES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.enrich_planning_features::_empty_catalog` via `NORMALIZED_FEATURE_DTYPES`

### `NORMALIZED_RELATION_DTYPES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
  - value/type reference: `landscout.stages.enrich_planning_features::_validate_normalized_planning_feature_inputs` via `NORMALIZED_RELATION_DTYPES`
  - import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)`
  - value/type reference: `tests.unit.test_resolve_planning_feature_codes::_canonical_relation_schema` via `NORMALIZED_RELATION_DTYPES`

### `OFFICIAL_CODE_DTYPES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
OFFICIAL_CODE_DTYPES = tuple("str" for _ in OFFICIAL_CODE_COLUMNS)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `normalized_feature_dtypes`

**Purpose:** Return exact factual dtypes, including deterministic all-null raw fields.

**Exact signature**

```python
def normalized_feature_dtypes(
    geometry_kind: GeometryKind,
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry_kind` | positional-or-keyword | `GeometryKind` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(dtypes)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.planning_feature_schema::feature_dtypes` via `normalized_feature_dtypes`
- value/type reference: `landscout.common.planning_feature_schema::feature_dtypes` via `normalized_feature_dtypes`
- import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.stages.enrich_planning_features::_canonical_catalog_dtypes` via `normalized_feature_dtypes`
- value/type reference: `landscout.stages.enrich_planning_features::_canonical_catalog_dtypes` via `normalized_feature_dtypes`
- direct call: `landscout.stages.enrich_planning_features::_validate_catalog_contract` via `normalized_feature_dtypes`
- value/type reference: `landscout.stages.enrich_planning_features::_validate_catalog_contract` via `normalized_feature_dtypes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `NORMALIZED_FEATURE_COLUMNS[geometry_kind].index` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `NORMALIZED_FEATURE_COLUMNS[geometry_kind].index` |
| External process/environment | None directly present. |
| In-memory mutation | `dtypes[position] = "object" if frame[column].isna().all() else "str"` |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `feature_columns`

**Purpose:** Return one exact ordered feature schema with deterministic suffixes.

**Exact signature**

```python
def feature_columns(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry_kind` | positional-or-keyword | `GeometryKind` | `required` |
| `suffix` | positional-or-keyword | `tuple[str, ...]` | `()` |

**Return and exception contract**

- Exact observed return expressions:
  - `(*NORMALIZED_FEATURE_COLUMNS[geometry_kind], *OFFICIAL_CODE_COLUMNS, *suffix)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.common.bess_application_contract::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.common.bess_application_contract::validate_bess_application_feature_catalogs` via `feature_columns`
- value/type reference: `landscout.common.bess_application_contract::validate_bess_application_feature_catalogs` via `feature_columns`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `feature_columns`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `feature_columns`

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `feature_dtypes`

**Purpose:** Return matching exact feature dtypes with deterministic suffixes.

**Exact signature**

```python
def feature_dtypes(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry_kind` | positional-or-keyword | `GeometryKind` | `required` |
| `suffix` | positional-or-keyword | `tuple[str, ...]` | `()` |
| `frame` | positional-or-keyword | `pd.DataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        *normalized_feature_dtypes(geometry_kind, frame),<br>        *OFFICIAL_CODE_DTYPES,<br>        *suffix,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.common.bess_application_contract::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.common.bess_application_contract::validate_bess_application_feature_catalogs` via `feature_dtypes`
- value/type reference: `landscout.common.bess_application_contract::validate_bess_application_feature_catalogs` via `feature_dtypes`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `feature_dtypes`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `feature_dtypes`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_canonical_empty_coded_result` via `feature_dtypes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_canonical_empty_coded_result` via `feature_dtypes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalized_feature_dtypes` | `landscout.common.planning_feature_schema.normalized_feature_dtypes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `relation_columns`

**Purpose:** Return one exact ordered relation schema with deterministic suffixes.

**Exact signature**

```python
def relation_columns(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `suffix` | positional-or-keyword | `tuple[str, ...]` | `()` |

**Return and exception contract**

- Exact observed return expressions:
  - `(*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.common.bess_application_contract::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.common.bess_application_contract::validate_bess_application_relation_frame` via `relation_columns`
- value/type reference: `landscout.common.bess_application_contract::validate_bess_application_relation_frame` via `relation_columns`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `relation_columns`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `relation_columns`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.common.planning_feature_schema import relation_columns, relation_dtypes`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_build_from_relations` via `relation_columns`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_build_from_relations` via `relation_columns`

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def relation_columns(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return one exact ordered relation schema with deterministic suffixes."""

    return (*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `relation_dtypes`

**Purpose:** Return matching exact relation dtypes with deterministic suffixes.

**Exact signature**

```python
def relation_dtypes(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `suffix` | positional-or-keyword | `tuple[str, ...]` | `()` |

**Return and exception contract**

- Exact observed return expressions:
  - `(*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.common.bess_application_contract::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.common.bess_application_contract::validate_bess_application_relation_frame` via `relation_dtypes`
- value/type reference: `landscout.common.bess_application_contract::validate_bess_application_relation_frame` via `relation_dtypes`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `relation_dtypes`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `relation_dtypes`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.common.planning_feature_schema import relation_columns, relation_dtypes`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_build_from_relations` via `relation_dtypes`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_build_from_relations` via `relation_dtypes`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_canonical_empty_coded_result` via `relation_dtypes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_canonical_empty_coded_result` via `relation_dtypes`

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def relation_dtypes(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return matching exact relation dtypes with deterministic suffixes."""

    return (*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `validate_canonical_frame_schema`

**Purpose:** Reject any deviation from one complete persisted frame-schema contract.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | keyword-only | `tuple[str, ...]` | `required` |
| `dtypes` | keyword-only | `tuple[str, ...]` | `required` |
| `label` | keyword-only | `str` | `required` |
| `geospatial` | keyword-only | `bool` | `required` |
| `index_class` | keyword-only | `IndexClass` | `'Index'` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `TypeError(f"{label} must be a DataFrame")` under lexical guard `not isinstance(frame, pd.DataFrame)`.
  - `ValueError(f"{label} contains duplicate columns")` under lexical guard `frame.columns.duplicated().any()`.
  - `ValueError(f"{label} canonical column, geometry, or dtype schema differs")` under lexical guard `tuple(frame.columns) != columns<br>        or tuple(str(dtype) for dtype in frame.dtypes) != dtypes`.
  - `ValueError(f"{label} canonical index schema differs")` under lexical guard `type(index) is not expected_index_type<br>        or list(index.names) != [None]<br>        or str(index.dtype) != "int64"`.
  - `ValueError(f"{label} canonical range index differs")` under lexical guard `index_class == "RangeIndex" and (<br>        index.start != 0 or index.stop != len(frame) or index.step != 1<br>    )`.
  - `TypeError(f"{label} must be a GeoDataFrame")` under lexical guard `geospatial`.
  - `ValueError(f"{label} canonical geometry or CRS metadata differs")` under lexical guard `geospatial`.
  - `ValueError(f"{label} canonical CRS is invalid")` under lexical guard `geospatial`.
  - `ValueError(f"{label} canonical CRS differs from EPSG:2154")` under lexical guard `geospatial`.
  - `TypeError(f"{label} must not be a GeoDataFrame")` under lexical guard `geospatial`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.common.bess_application_contract::<module>` via `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.common.bess_application_contract::validate_bess_application_feature_catalogs` via `validate_canonical_frame_schema`
- value/type reference: `landscout.common.bess_application_contract::validate_bess_application_feature_catalogs` via `validate_canonical_frame_schema`
- direct call: `landscout.common.bess_application_contract::validate_bess_application_relation_frame` via `validate_canonical_frame_schema`
- value/type reference: `landscout.common.bess_application_contract::validate_bess_application_relation_frame` via `validate_canonical_frame_schema`
- import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.stages.enrich_planning_features::_validate_catalog_contract` via `validate_canonical_frame_schema`
- value/type reference: `landscout.stages.enrich_planning_features::_validate_catalog_contract` via `validate_canonical_frame_schema`
- direct call: `landscout.stages.enrich_planning_features::_validate_normalized_planning_feature_inputs` via `validate_canonical_frame_schema`
- value/type reference: `landscout.stages.enrich_planning_features::_validate_normalized_planning_feature_inputs` via `validate_canonical_frame_schema`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `validate_canonical_frame_schema`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `validate_canonical_frame_schema`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input(frame.crs).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        raise ValueError(f"{label} canonical column, geometry, or dtype schema differs")
    index = frame.index
    expected_index_type = pd.Index if index_class == "Index" else pd.RangeIndex
    if (
        type(index) is not expected_index_type
        or list(index.names) != [None]
        or str(index.dtype) != "int64"
    ):
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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `COMMON_FEATURE_COLUMNS`, `SURFACE_FEATURE_COLUMNS`, `LINE_FEATURE_COLUMNS`, `POINT_FEATURE_COLUMNS`, `NORMALIZED_FEATURE_COLUMNS`, `RELATION_COLUMNS`, `RELATION_FLOAT_COLUMNS`, `RELATION_COUNT_COLUMNS`, `RELATION_STRING_COLUMNS`, `OFFICIAL_CODE_COLUMNS`, `_COMMON_STR_DTYPES`, `NORMALIZED_FEATURE_DTYPES`, `NORMALIZED_RELATION_DTYPES`, `OFFICIAL_CODE_DTYPES`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Internal canonical schemas for normalized, coded, and applied planning facts."""

from __future__ import annotations

from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS

GeometryKind = Literal["SURFACE", "LINE", "POINT"]
IndexClass = Literal["Index", "RangeIndex"]

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
SURFACE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_area_m2")
LINE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_length_m")
POINT_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "point_member_count")
NORMALIZED_FEATURE_COLUMNS = {
    "SURFACE": SURFACE_FEATURE_COLUMNS,
    "LINE": LINE_FEATURE_COLUMNS,
    "POINT": POINT_FEATURE_COLUMNS,
}

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
RELATION_COUNT_COLUMNS = frozenset(
    {
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    }
)
RELATION_STRING_COLUMNS = (
    frozenset(RELATION_COLUMNS) - RELATION_FLOAT_COLUMNS - (RELATION_COUNT_COLUMNS)
)

OFFICIAL_CODE_COLUMNS = (
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)

_COMMON_STR_DTYPES = {
    column: "str"
    for column in COMMON_FEATURE_COLUMNS
    if column not in {"text_raw", "regulation_filename_raw", "regulation_url_raw"}
}
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
NORMALIZED_RELATION_DTYPES = tuple(
    "float64"
    if column in RELATION_FLOAT_COLUMNS
    else "Int64"
    if column in RELATION_COUNT_COLUMNS
    else "str"
    for column in RELATION_COLUMNS
)
OFFICIAL_CODE_DTYPES = tuple("str" for _ in OFFICIAL_CODE_COLUMNS)


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


def feature_columns(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
) -> tuple[str, ...]:
    """Return one exact ordered feature schema with deterministic suffixes."""

    return (*NORMALIZED_FEATURE_COLUMNS[geometry_kind], *OFFICIAL_CODE_COLUMNS, *suffix)


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


def relation_columns(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return one exact ordered relation schema with deterministic suffixes."""

    return (*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)


def relation_dtypes(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return matching exact relation dtypes with deterministic suffixes."""

    return (*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)


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
        raise ValueError(f"{label} canonical column, geometry, or dtype schema differs")
    index = frame.index
    expected_index_type = pd.Index if index_class == "Index" else pd.RangeIndex
    if (
        type(index) is not expected_index_type
        or list(index.names) != [None]
        or str(index.dtype) != "int64"
    ):
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
