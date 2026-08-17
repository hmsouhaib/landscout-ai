# `src/landscout/common/planning_feature_schema.py`

## File identity

- Repository path: `src/landscout/common/planning_feature_schema.py`
- File type: Python source
- Primary responsibility: Centralizes ordered normalized, CNIG-coded, and BESS-application feature/relation schemas and dtypes.
- Layer / domain: `internal common contract/utility` / `planning`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `7f1921b20cceb88c35232a99677fdcc3b5c247f67f380eae73e1d79e59bb0d18`

## 1. Purpose

Centralizes ordered normalized, CNIG-coded, and BESS-application feature/relation schemas and dtypes.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `COMMON_FEATURE_COLUMNS` | `( "planning_feature_id", "source_feature_id", "source_identity_kind", "source_identity_field", "logical_layer", "feature_family", "geometry_kind", "type_code_raw", "subtype_code_raw", "label_raw", "text_raw", "regulation_filename_raw", "regulation_url_raw", "source_document_reference_raw", "source_validity_date_raw", "source_provider", "source_portal", "source_commune_code", "source_document_id", "source_document_type", "source_archive_name", "source_archive_sha256", "source_layer", "source_standard_model", "source_crs", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SURFACE_FEATURE_COLUMNS` | `(*COMMON_FEATURE_COLUMNS, "geometry", "feature_area_m2")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_FEATURE_COLUMNS` | `(*COMMON_FEATURE_COLUMNS, "geometry", "feature_length_m")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POINT_FEATURE_COLUMNS` | `(*COMMON_FEATURE_COLUMNS, "geometry", "point_member_count")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `NORMALIZED_FEATURE_COLUMNS` | `{ "SURFACE": SURFACE_FEATURE_COLUMNS, "LINE": LINE_FEATURE_COLUMNS, "POINT": POINT_FEATURE_COLUMNS, }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_COLUMNS` | `( "parcel_id", "planning_feature_id", "source_feature_id", "source_identity_kind", "source_identity_field", "logical_layer", "feature_family", "geometry_kind", "type_code_raw", "subtype_code_raw", "label_raw", "text_raw", "relation_type", "parcel_metric_area_m2", "feature_area_m2", "source_line_length_m", "intersection_area_m2", "intersection_length_m", "parcel_share_pct", "feature_share_pct", "point_member_count", "point_members_inside_count", "point_members_boundary_count", "source_document_id", "source_archive_sha256", "source_layer", "source_validity_date_raw", "regulation_filename_raw", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_FLOAT_COLUMNS` | `frozenset( { "parcel_metric_area_m2", "feature_area_m2", "source_line_length_m", "intersection_area_m2", "intersection_length_m", "parcel_share_pct", "feature_share_pct", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_COUNT_COLUMNS` | `frozenset( { "point_member_count", "point_members_inside_count", "point_members_boundary_count", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_STRING_COLUMNS` | `frozenset(RELATION_COLUMNS) - RELATION_FLOAT_COLUMNS - (RELATION_COUNT_COLUMNS)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OFFICIAL_CODE_COLUMNS` | `( "official_code_status", "official_code_label", "official_legal_reference", "official_regulation_reference", "official_code_source_url", "official_code_profile", "official_code_profile_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_COMMON_STR_DTYPES` | `{ column: "str" for column in COMMON_FEATURE_COLUMNS if column not in {"text_raw", "regulation_filename_raw", "regulation_url_raw"} }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `NORMALIZED_FEATURE_DTYPES` | `{ "SURFACE": tuple( { **_COMMON_STR_DTYPES, "text_raw": "str", "regulation_filename_raw": "str", "regulation_url_raw": "object", "geometry": "geometry", "feature_area_m2": "float64", }[column] for column in SURFACE_FEATURE_COLUMNS ), "LINE": tuple( { **_COMMON_STR_DTYPES, "text_raw": "object", "regulation_filename_raw": "object", "regulation_url_raw": "object", "geometry": "geometry", "feature_length_m": "float64", }[column] for column in LINE_FEATURE_COLUMNS ), "POINT": tuple( { **_COMMON_STR_DTYPES, "text_raw": "object", "regulation_filename_raw": "object", "regulation_url_raw": "object", "geometry": "geometry", "point_member_count": "int64", }[column] for column in POINT_FEATURE_COLUMNS ), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `NORMALIZED_RELATION_DTYPES` | `tuple( "float64" if column in RELATION_FLOAT_COLUMNS else "Int64" if column in RELATION_COUNT_COLUMNS else "str" for column in RELATION_COLUMNS )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OFFICIAL_CODE_DTYPES` | `tuple("str" for _ in OFFICIAL_CODE_COLUMNS)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `normalized_feature_dtypes`

**Signature**

```python
def normalized_feature_dtypes(
    geometry_kind: GeometryKind,
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
```

**Purpose**

Return exact factual dtypes, including deterministic all-null raw fields.

**Inputs**

- `geometry_kind` (`GeometryKind`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `tuple(dtypes)`.

**Algorithm**

1. Computes `dtypes` from `list(NORMALIZED_FEATURE_DTYPES[geometry_kind])`.
2. Checks `frame is None or frame.empty`. When true: Returns `tuple(dtypes)`.
3. Iterates `column` over `('text_raw', 'regulation_filename_raw', 'regulation_url_raw')`. For each value: Checks `column not in frame.columns`. When true: Executes `continue` control flow. Computes `position` from `NORMALIZED_FEATURE_COLUMNS[geometry_kind].index(column)`. Computes `dtypes[position]` from `'object' if frame[column].isna().all() else 'str'`.
4. Returns `tuple(dtypes)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `NORMALIZED_FEATURE_COLUMNS[geometry_kind].index`, `frame[column].isna`, `frame[column].isna().all`, `list`, `tuple`.

**Known repository callers**

- `src/landscout/common/planning_feature_schema.py` — `feature_dtypes`
- `src/landscout/stages/enrich_planning_features.py` — `_canonical_catalog_dtypes`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `feature_columns`

**Signature**

```python
def feature_columns(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
) -> tuple[str, ...]:
```

**Purpose**

Return one exact ordered feature schema with deterministic suffixes.

**Inputs**

- `geometry_kind` (`GeometryKind`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `suffix` (`tuple[str, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `(*NORMALIZED_FEATURE_COLUMNS[geometry_kind], *OFFICIAL_CODE_COLUMNS, *suffix)`.

**Algorithm**

1. Returns `(*NORMALIZED_FEATURE_COLUMNS[geometry_kind], *OFFICIAL_CODE_COLUMNS, *suffix)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `feature_dtypes`

**Signature**

```python
def feature_dtypes(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
```

**Purpose**

Return matching exact feature dtypes with deterministic suffixes.

**Inputs**

- `geometry_kind` (`GeometryKind`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `suffix` (`tuple[str, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `(*normalized_feature_dtypes(geometry_kind, frame), *OFFICIAL_CODE_DTYPES, *suffix)`.

**Algorithm**

1. Returns `(*normalized_feature_dtypes(geometry_kind, frame), *OFFICIAL_CODE_DTYPES, *suffix)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `normalized_feature_dtypes`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_canonical_empty_coded_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `relation_columns`

**Signature**

```python
def relation_columns(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
```

**Purpose**

Return one exact ordered relation schema with deterministic suffixes.

**Inputs**

- `suffix` (`tuple[str, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `(*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)`.

**Algorithm**

1. Returns `(*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_build_from_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `relation_dtypes`

**Signature**

```python
def relation_dtypes(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
```

**Purpose**

Return matching exact relation dtypes with deterministic suffixes.

**Inputs**

- `suffix` (`tuple[str, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `(*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)`.

**Algorithm**

1. Returns `(*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_build_from_relations`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_canonical_empty_coded_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_canonical_frame_schema`

**Signature**

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

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `dtypes` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geospatial` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `index_class` (`IndexClass`; optional/default `'Index'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(frame, pd.DataFrame)`. When true: Raises `TypeError(f'{label} must be a DataFrame')`.
2. Checks `frame.columns.duplicated().any()`. When true: Raises `ValueError(f'{label} contains duplicate columns')`.
3. Checks `tuple(frame.columns) != columns or tuple((str(dtype) for dtype in frame.dtypes)) != dtypes`. When true: Raises `ValueError(f'{label} canonical column, geometry, or dtype schema differs')`.
4. Computes `index` from `frame.index`.
5. Computes `expected_index_type` from `pd.Index if index_class == 'Index' else pd.RangeIndex`.
6. Checks `type(index) is not expected_index_type or list(index.names) != [None] or str(index.dtype) != 'int64'`. When true: Raises `ValueError(f'{label} canonical index schema differs')`.
7. Checks `index_class == 'RangeIndex' and (index.start != 0 or index.stop != len(frame) or index.step != 1)`. When true: Raises `ValueError(f'{label} canonical range index differs')`.
8. Checks `geospatial`. When true: Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `TypeError(f'{label} must be a GeoDataFrame')`. Checks `frame.geometry.name != 'geometry' or frame.crs is None`. When true: Raises `ValueError(f'{label} canonical geometry or CRS metadata differs')`. Runs guarded operation: Computes `canonical_crs` from `CRS.from_user_input(frame.crs).equals(CRS.from_epsg(2154))`. Handles `Exception`. Executes 1 additional source-ordered statement(s). Otherwise: Checks `isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `TypeError(f'{label} must not be a GeoDataFrame')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `tuple(frame.columns) != columns or tuple((str(dtype) for dtype in frame.dtypes)) != dtypes` is true.
- Rejects or diverts the path when `type(index) is not expected_index_type or list(index.names) != [None] or str(index.dtype) != 'int64'` is true.
- Rejects or diverts the path when `index_class == 'RangeIndex' and (index.start != 0 or index.stop != len(frame) or index.step != 1)` is true.
- Rejects or diverts the path when `geospatial` is true.
- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `frame.geometry.name != 'geometry' or frame.crs is None` is true.
- Rejects or diverts the path when `not canonical_crs` is true.
- Rejects or diverts the path when `isinstance(frame, gpd.GeoDataFrame)` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `CRS.from_user_input(frame.crs).equals`, `TypeError`, `ValueError`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `isinstance`, `len`, `list`, `str`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `Index` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LINE` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `POINT` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `RangeIndex` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SURFACE` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `feature_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `feature_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `logical_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `official_legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_regulation_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `point_member_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_boundary_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_inside_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_filename_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_url_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_commune_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_crs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_reference_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_field` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_line_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `source_portal` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_standard_model` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_validity_date_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `text_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `type_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |

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
