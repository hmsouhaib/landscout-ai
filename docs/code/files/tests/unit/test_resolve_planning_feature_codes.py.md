# `tests/unit/test_resolve_planning_feature_codes.py`

## File identity

- Repository path: `tests/unit/test_resolve_planning_feature_codes.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `e27391c2e81b7e8d74d2d34da0df1590f4b1003ed0281dd99899c59cc2004e43`

## 1. Purpose

Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import shutil` — required by the implementation paths and symbols documented below.
- `import tempfile` — required by the implementation paths and symbols documented below.
- `from dataclasses import replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import importlib` — required by the implementation paths and symbols documented below.
- `import inspect` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.planning_feature_schema import ( NORMALIZED_RELATION_DTYPES, feature_dtypes, relation_dtypes, )` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( EXTRACTION_MANIFEST_NAME, GpuArchiveDownload, GpuDocumentMetadata, GpuExtractedFile, GpuExtraction, GpuInspectedLayer, GpuLayerSummary, GpuPlanningDocument, GpuSpatialLayerReference, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_planning_features import ( RELATION_COLUMNS, intersect_parcels_with_gpu_planning_features, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( CODE_DICTIONARY_COLUMNS, OFFICIAL_CODE_COLUMNS, CnigFeatureCodeProfile, PlanningFeatureCodeError, PlanningFeatureCodeResult, _result_with_hashes, load_cnig_feature_code_profile, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( resolve_planning_feature_codes as _public_resolve_planning_feature_codes, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( validate_planning_feature_code_result as _public_validate_planning_feature_code_result, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `P_URL` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `I_URL` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `TEXT_NORMALIZATION` | `"GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result.DerivedPlanningFeatureCodeResult`

**Purpose:** Carries an immutable stage/result envelope whose fields and hashes are consumed by downstream validation.

**Inheritance:** `PlanningFeatureCodeResult`.

**Model form and mutability:** class inheriting from `PlanningFeatureCodeResult`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `_canonical_relation_schema`

**Signature**

```python
def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
```

**Purpose**

Implements canonical relation schema according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `frame.copy(deep=True)`.
2. Iterates `(column, dtype)` over `zip(RELATION_COLUMNS, NORMALIZED_RELATION_DTYPES, strict=True)`. For each value: Computes `output[column]` from `pd.Series(output[column].tolist(), index=output.index, dtype=dtype)`.
3. Computes `output.index` from `pd.RangeIndex(len(output))`.
4. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `frame.copy`, `len`, `output[column].tolist`, `pd.RangeIndex`, `pd.Series`, `zip`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_parcel_feature_relation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_relation_type_must_match_catalog_geometry_kind`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_parcel_feature_relation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_relation_type_must_match_catalog_geometry_kind`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_records_hash`

**Signature**

```python
def _records_hash(records: list[dict[str, object]]) -> str:
```

**Purpose**

Implements records hash according to the exact implementation and guards in this file.

**Inputs**

- `records` (`list[dict[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(payload).hexdigest()`.

**Algorithm**

1. Computes `ordered` from `sorted(records, key=lambda row: (row['feature_family'], row['type_code'], row['subtype_code']))`.
2. Computes `payload` from `json.dumps(ordered, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode()`.
3. Returns `sha256(payload).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `json.dumps`, `json.dumps(ordered, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(payload).hexdigest`, `sorted`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_profile_payload`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_official_family_endpoints_require_exact_identity`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_official_text_must_already_be_canonical`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py::test_official_family_endpoints_require_exact_identity`
- `tests/unit/test_resolve_planning_feature_codes.py::test_official_text_must_already_be_canonical`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_payload_hash`

**Signature**

```python
def _payload_hash(payload: object) -> str:
```

**Purpose**

Implements payload hash according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(encoded).hexdigest()`.

**Algorithm**

1. Computes `encoded` from `json.dumps(payload, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':'), default=str).encode('utf-8')`.
2. Returns `sha256(encoded).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `json.dumps`, `json.dumps(payload, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':'), default=str).encode`, `sha256`, `sha256(encoded).hexdigest`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_record`

**Signature**

```python
def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
```

**Purpose**

Implements record according to the exact implementation and guards in this file.

**Inputs**

- `family` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `type_code` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `subtype_code` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'feature_family': family, 'type_code': type_code, 'subtype_code': subtype_code, 'official_label': label, 'legal_reference': None, 'regulation_or_annex_reference': None, 'official_source_url': P_URL if family == 'PRESCRIPTION' else I_URL}`.

**Algorithm**

1. Returns `{'feature_family': family, 'type_code': type_code, 'subtype_code': subtype_code, 'official_label': label, 'legal_reference': None, 'regulation_or_annex_reference': None, 'official_source_url': P_URL if family == 'PRESCRIPTION' else I_URL}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_profile_payload`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_profile_payload`

**Signature**

```python
def _profile_payload() -> dict[str, object]:
```

**Purpose**

Profiles payload according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'schema_version': 2, 'profile': 'synthetic_cnig_plu_2017', 'standard_model': 'CNIG PLU v2017', 'official_text_normalization': TEXT_NORMALIZATION, 'official_sources': {'prescription': P_URL, 'information': I_URL}, 'retrieval_date': '2026-08-12', 'canonical_records_sha256': _records_hash(records), 'records': records}`.

**Algorithm**

1. Computes `records` from `[_record('INFORMATION', '02', '00', 'Information two'), _record('INFORMATION', '99', '00', 'Other information'), _record('PRESCRIPTION', '07', '00', 'Prescription seven'), _record('PRESCRIPTION', '07', '04', 'Prescription seven subtype four')]`.
2. Returns `{'schema_version': 2, 'profile': 'synthetic_cnig_plu_2017', 'standard_model': 'CNIG PLU v2017', 'official_text_normalization': TEXT_NORMALIZATION, 'official_sources': {'prescription': P_URL, 'information': I_URL}, 'retrieval_date': '2026-08-12', 'canonical_records_sha256': _records_hash(records), 'records': records}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_record`, `_records_hash`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_profile`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_pair_and_profile_hash_mutation_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_malformed_code_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_official_family_endpoints_require_exact_identity`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_official_text_must_already_be_canonical`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_record_order_must_be_deterministic`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_wrong_official_host_and_unknown_field_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_yaml_snapshot_loads_strictly`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_pair_and_profile_hash_mutation_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_malformed_code_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py::test_official_family_endpoints_require_exact_identity`
- `tests/unit/test_resolve_planning_feature_codes.py::test_official_text_must_already_be_canonical`
- `tests/unit/test_resolve_planning_feature_codes.py::test_record_order_must_be_deterministic`
- `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_official_host_and_unknown_field_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_yaml_snapshot_loads_strictly`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_profile`

**Signature**

```python
def _profile() -> CnigFeatureCodeProfile:
```

**Purpose**

Profiles profile according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `CnigFeatureCodeProfile`. Observed return expression(s): `CnigFeatureCodeProfile.model_validate(_profile_payload())`.

**Algorithm**

1. Returns `CnigFeatureCodeProfile.model_validate(_profile_payload())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `_profile_payload`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_integration_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_legacy_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_mutated_profile`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_relation_types_are_retained`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_yaml_snapshot_loads_strictly`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained`
- `tests/unit/test_resolve_planning_feature_codes.py::test_yaml_snapshot_loads_strictly`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_inventory`

**Signature**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

**Purpose**

Implements physical inventory according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuExtractedFile, ...]`. Observed return expression(s): `tuple((GpuExtractedFile(relative_path=path.relative_to(root).as_posix(), file_type=path.suffix.casefold().lstrip('.') or 'none', size_bytes=path.stat().st_size, sha256=sha256(path.read_bytes()).hexdigest(), category='SPATIAL_DATA') for path in sorted((item for item in root.rglob('*') if item.is_file()), key=str) if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)))`.

**Algorithm**

1. Returns `tuple((GpuExtractedFile(relative_path=path.relative_to(root).as_posix(), file_type=path.suffix.casefold().lstrip('.') or 'none', size_bytes=path.stat().st_size, sha256=sha256(path.read_bytes()).hexdigest(), category='SPATIAL_DATA') for path in sorted((item for item in root.rglob('*') if item.is_file()), key=str) if not (path.parent == root and path.name == …`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_bytes`, `sha256(path.read_bytes()).hexdigest`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuExtractedFile`, `item.is_file`, `path.read_bytes`, `path.relative_to`, `path.relative_to(root).as_posix`, `path.stat`, `path.suffix.casefold`, `path.suffix.casefold().lstrip`, `root.rglob`, `sha256`, `sha256(path.read_bytes()).hexdigest`, `sorted`, `tuple`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_extraction_manifest`

**Signature**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
```

**Purpose**

Writes extraction manifest according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_sha256` (`str`; required) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.
- `files` (`tuple[GpuExtractedFile, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `(root / EXTRACTION_MANIFEST_NAME).write_text(json.dumps({'schema_version': 2, 'archive_sha256': archive_sha256, 'files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in files]}, sort_keys=True, separators=(',', ':')), encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(root / EXTRACTION_MANIFEST_NAME).write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(root / EXTRACTION_MANIFEST_NAME).write_text`, `json.dumps`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_layer_summary`

**Signature**

```python
def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
```

**Purpose**

Implements layer summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuLayerSummary`. Observed return expression(s): `GpuLayerSummary(source_document_id='doc-1', source_archive_sha256='a' * 64, source_layer=source_layer, crs=frame.crs.to_string(), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna().sum())) for column in frame.columns)), geo…`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `non_null` from `~geometry.isna()`.
3. Computes `non_empty` from `non_null & ~geometry.is_empty`.
4. Returns `GpuLayerSummary(source_document_id='doc-1', source_archive_sha256='a' * 64, source_layer=source_layer, crs=frame.crs.to_string(), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna().su…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `(~non_null).sum`, `GpuLayerSummary`, `frame.crs.to_string`, `frame.dtypes.items`, `frame[column].isna`, `frame[column].isna().sum`, `geometry.geom_type.value_counts`, `geometry.geom_type.value_counts().sort_index`, `geometry.geom_type.value_counts().sort_index().items`, `geometry.isna`, `int`, `len`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_planning_document`

**Signature**

```python
def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
```

**Purpose**

Implements planning document according to the exact implementation and guards in this file.

**Inputs**

- `standard` (`str`; optional/default `'CNIG PLU v2017'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `related_layers` (`tuple[GpuInspectedLayer, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `GpuPlanningDocument(extraction, (reference, *(layer.reference for layer in related_layers)), zoning, related_layers)`.

**Algorithm**

1. Computes `extraction_root` from `Path(tempfile.mkdtemp(prefix='landscout-code-source-'))`.
2. Defines `physical_layers` with annotation `list[GpuInspectedLayer]` from `[]`.
3. Iterates `layer` over `related_layers`. For each value: Computes `path` from `extraction_root / f'{layer.logical_name}.gpkg'`. Calls `layer.data.to_file(path, layer=layer.reference.source_layer, driver='GPKG', engine='pyogrio', index=False)` for its validation or side effect. Computes `reread` from `gpd.read_file(path, layer=layer.reference.source_layer, engine='pyogrio')`. Executes 2 additional source-ordered statement(s).
4. Computes `related_layers` from `tuple(physical_layers)`.
5. Computes `document` from `GpuDocumentMetadata(provider="Géoportail de l'Urbanisme", portal='https://www.geoportail-urbanisme.gouv.fr', commune_code='31395', partition='DU_31395', document_id='doc-1', document_family='DU', document_type='PLU', document_title=None, status='document.production', legal_status='APPROVED', effective_status='EN_VIGUE…`.
6. Computes `archive` from `GpuArchiveDownload(document=document, download_timestamp='2026-08-12T00:00:00Z', filename='31395_PLU_20240215.zip', archive_format='zip', file_size=1, sha256='a' * 64, path=Path('synthetic.zip'), cache_hit=True)`.
7. Computes `zoning_data` from `gpd.GeoDataFrame({'LIB_IDZONE': ['Z1']}, geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])], crs='EPSG:2154')`.
8. Computes `zoning_path` from `extraction_root / 'zones.gpkg'`.
9. Calls `zoning_data.to_file(zoning_path, layer='ZONE', driver='GPKG', engine='pyogrio', index=False)` for its validation or side effect.
10. Computes `zoning_data` from `gpd.read_file(zoning_path, layer='ZONE', engine='pyogrio')`.
11. Computes `reference` from `GpuSpatialLayerReference(zoning_path, 'ZONE', 'GPKG')`.
12. Computes `summary` from `_layer_summary(zoning_data, 'ZONE')`.
13. Computes `zoning` from `GpuInspectedLayer('zoning', reference, zoning_data, summary)`.
14. Computes `inventory` from `_physical_inventory(extraction_root)`.
15. Calls `_write_extraction_manifest(extraction_root, archive.sha256, inventory)` for its validation or side effect.
16. Computes `extraction` from `GpuExtraction(archive=archive, extraction_root=extraction_root, files=inventory, standard_models=(standard,), cache_hit=True)`.
17. Returns `GpuPlanningDocument(extraction, (reference, *(layer.reference for layer in related_layers)), zoning, related_layers)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuArchiveDownload`, `_write_extraction_manifest`, `gpd.read_file`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuArchiveDownload`, `GpuDocumentMetadata`, `GpuExtraction`, `GpuInspectedLayer`, `GpuPlanningDocument`, `GpuSpatialLayerReference`, `Path`, `Polygon`, `_layer_summary`, `_physical_inventory`, `_write_extraction_manifest`, `gpd.GeoDataFrame`, `gpd.read_file`, `layer.data.to_file`, `physical_layers.append`, `replace`, `tempfile.mkdtemp`, `tuple`, `zoning_data.to_file`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_integration_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_legacy_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_relation_types_are_retained`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_wrong_planning_standard_is_rejected`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained`
- `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_base_row`

**Signature**

```python
def _base_row(
    feature_id: str,
    source_id: str,
    family: str,
    layer: str,
    kind: str,
    type_code: str,
    subtype_code: str,
) -> dict[str, object]:
```

**Purpose**

Implements base row according to the exact implementation and guards in this file.

**Inputs**

- `feature_id` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `family` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `kind` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `type_code` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `subtype_code` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'planning_feature_id': feature_id, 'source_feature_id': source_id, 'source_identity_kind': 'CNIG_ATTRIBUTE', 'source_identity_field': 'LIB_IDPSC' if family == 'PRESCRIPTION' else 'LIB_IDINFO', 'logical_layer': layer, 'feature_family': family, 'geometry_kind': kind, 'type_code_raw': type_code, 'subtype_code_raw': subtype_code, 'label_raw': None, 'text_raw': None, 'regulation_filename_raw': None, …`.

**Algorithm**

1. Returns `{'planning_feature_id': feature_id, 'source_feature_id': source_id, 'source_identity_kind': 'CNIG_ATTRIBUTE', 'source_identity_field': 'LIB_IDPSC' if family == 'PRESCRIPTION' else 'LIB_IDINFO', 'logical_layer': layer, 'feature_family': family, 'geometry_kind': kind, 'type_code_raw': type_code, 'subtype_code_raw': subtype_code, 'label_raw': None, 'text_raw':…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `layer.upper`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_legacy_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_legacy_inputs`

**Signature**

```python
def _legacy_inputs():
```

**Purpose**

Implements legacy inputs according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `(_planning_document(), surface, line, point, relations, _profile())`.

**Algorithm**

1. Computes `surface_rows` from `[_base_row('F-P-0700', 'P-1', 'PRESCRIPTION', 'prescription_surface', 'SURFACE', '07', '00'), _base_row('F-I-0200', 'I-1', 'INFORMATION', 'information_surface', 'SURFACE', '02', '00')]`.
2. Computes `surface` from `gpd.GeoDataFrame(surface_rows, geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]), Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])], crs='EPSG:2154', index=pd.Index([11, 22], name='source_row'))`.
3. Computes `surface['feature_area_m2']` from `[4.0, 4.0]`.
4. Computes `line` from `gpd.GeoDataFrame([_base_row('F-P-0704', 'P-2', 'PRESCRIPTION', 'prescription_line', 'LINE', '07', '04')], geometry=[LineString([(0, 0), (2, 0)])], crs='EPSG:2154', index=pd.Index([33], name='source_row'))`.
5. Computes `line['feature_length_m']` from `[2.0]`.
6. Computes `point` from `gpd.GeoDataFrame([_base_row('F-I-9900', 'I-2', 'INFORMATION', 'information_point', 'POINT', '99', '00')], geometry=[Point(1, 1)], crs='EPSG:2154', index=pd.Index([44], name='source_row'))`.
7. Computes `point['point_member_count']` from `[1]`.
8. Computes `relations` from `pd.DataFrame([{'parcel_id': 'PARCEL-1', **{key: surface.iloc[0][key] for key in ('planning_feature_id', 'source_feature_id', 'source_identity_kind', 'source_identity_field', 'logical_layer', 'feature_family', 'geometry_kind', 'type_code_raw', 'subtype_code_raw', 'label_raw', 'text_raw', 'source_document_id', 'source_a…`.
9. Computes `relations` from `relations.loc[:, list(RELATION_COLUMNS)]`.
10. Returns `(_planning_document(), surface, line, point, relations, _profile())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `Point`, `Polygon`, `_base_row`, `_planning_document`, `_profile`, `gpd.GeoDataFrame`, `list`, `pd.DataFrame`, `pd.Index`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_mutated_profile`

**Signature**

```python
def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
```

**Purpose**

Build a deliberately unvalidated frozen profile for boundary tests.

**Inputs**

- `**updates` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CnigFeatureCodeProfile`. Observed return expression(s): `profile.model_copy(update=updates)`.

**Algorithm**

1. Computes `profile` from `_profile()`.
2. Returns `profile.model_copy(update=updates)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `profile.model_copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_profile`, `profile.model_copy`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_empty_catalog`

**Signature**

```python
def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
```

**Purpose**

Return an optional empty catalog with the deterministic source schema.

**Inputs**

- `kind` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `template.iloc[0:0].copy()`.

**Algorithm**

1. Computes `(_, surface, line, point, _, _)` from `_inputs()`.
2. Computes `template` from `{'SURFACE': surface, 'LINE': line, 'POINT': point}[kind]`.
3. Returns `template.iloc[0:0].copy()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `template.iloc[0:0].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_inputs`, `template.iloc[0:0].copy`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_source_frame`

**Signature**

```python
def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements integration source frame according to the exact implementation and guards in this file.

**Inputs**

- `logical_layer` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometries` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_ids` (`list[str]`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `type_codes` (`list[str]`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `subtype_codes` (`list[str]`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'LIBELLE': [f'Label {identifier}' for identifier in source_ids], 'TXT': [None] * len(source_ids), 'TYPEPSC' if prescription else 'TYPEINF': type_codes, 'STYPEPSC' if prescription else 'STYPEINF': subtype_codes, 'NOMFIC': [None] * len(source_ids), 'URLFIC': [None] * len(source_ids), 'IDURBA': ['31395_PLU_20240215'] * len(source_ids), 'DATVALID': ['20240215'] * len(source_ids), 'L…`.

**Algorithm**

1. Computes `prescription` from `logical_layer.startswith('prescription')`.
2. Returns `gpd.GeoDataFrame({'LIBELLE': [f'Label {identifier}' for identifier in source_ids], 'TXT': [None] * len(source_ids), 'TYPEPSC' if prescription else 'TYPEINF': type_codes, 'STYPEPSC' if prescription else 'STYPEINF': subtype_codes, 'NOMFIC': [None] * len(source_ids), 'URLFIC': [None] * len(source_ids), 'IDURBA': ['31395_PLU_20240215'] * len(source_ids), 'DATVA…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `gpd.GeoDataFrame`, `len`, `logical_layer.startswith`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_integration_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_relation_types_are_retained`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_layer`

**Signature**

```python
def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
```

**Purpose**

Implements integration layer according to the exact implementation and guards in this file.

**Inputs**

- `logical_layer` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuInspectedLayer`. Observed return expression(s): `GpuInspectedLayer(logical_layer, reference, frame, summary)`.

**Algorithm**

1. Computes `source_layer` from `logical_layer.upper()`.
2. Computes `reference` from `GpuSpatialLayerReference(Path(f'{logical_layer}.gpkg'), source_layer, 'GPKG')`.
3. Computes `geometry` from `frame.geometry`.
4. Computes `non_null` from `~geometry.isna()`.
5. Computes `non_empty` from `non_null & ~geometry.is_empty`.
6. Computes `summary` from `GpuLayerSummary(source_document_id='doc-1', source_archive_sha256='a' * 64, source_layer=source_layer, crs=frame.crs.to_string(), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((…`.
7. Returns `GpuInspectedLayer(logical_layer, reference, frame, summary)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `(~non_null).sum`, `GpuInspectedLayer`, `GpuLayerSummary`, `GpuSpatialLayerReference`, `Path`, `frame.crs.to_string`, `frame.dtypes.items`, `frame[column].isna`, `frame[column].isna().sum`, `geometry.geom_type.value_counts`, `geometry.geom_type.value_counts().sort_index`, `geometry.geom_type.value_counts().sort_index().items`, `geometry.isna`, `int`, `len`, `logical_layer.upper`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_integration_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_relation_types_are_retained`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_inputs`

**Signature**

```python
def _integration_inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
```

**Purpose**

Implements integration inputs according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, pd.DataFrame, CnigFeatureCodeProfile]`. Observed return expression(s): `(planning_document, parcels, normalized.surface_features, normalized.line_features, normalized.point_features, normalized.relations, _profile())`.

**Algorithm**

1. Computes `layers` from `(_integration_layer('prescription_surface', _integration_source_frame('prescription_surface', [Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])], ['P-1'], ['07'], ['00'])), _integration_layer('information_surface', _integration_source_frame('information_surface', [Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])], ['I-1'], ['02'], …`.
2. Computes `planning_document` from `_planning_document(related_layers=layers)`.
3. Computes `parcels` from `_integration_parcels()`.
4. Computes `normalized` from `intersect_parcels_with_gpu_planning_features(parcels, planning_document)`.
5. Returns `(planning_document, parcels, normalized.surface_features, normalized.line_features, normalized.point_features, normalized.relations, _profile())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `Point`, `Polygon`, `_integration_layer`, `_integration_parcels`, `_integration_source_frame`, `_planning_document`, `_profile`, `intersect_parcels_with_gpu_planning_features`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_checked_in_policy_result`
- `tests/unit/test_bess_planning_feature_policy.py` — `_compiled_fixture`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_compiler_and_public_validator_invoke_source_complete_coding_validation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_malformed_sha256_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_status_priority_contract_is_strict`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_unknown_yaml_field_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coded_result_persists_all_source_input_hashes`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_gpu_document_context_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_gpu_related_source_hash_is_deterministic_across_cache_roots`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_normalized_relation_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_parcel_source_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_parquet_readback_preserves_source_hash_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_binding_hashes_bind_every_component_hash`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_input_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_step_7d_3_1_output_integrates_with_public_coding_api`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_empty_optional_catalogs_preserve_schema_and_crs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_multi_geometries_are_accepted`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation`
- `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_malformed_sha256_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py::test_status_priority_contract_is_strict`
- `tests/unit/test_bess_planning_feature_policy.py::test_unknown_yaml_field_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_coded_result_persists_all_source_input_hashes`
- `tests/unit/test_resolve_planning_feature_codes.py::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`
- `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_document_context_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_related_source_hash_is_deterministic_across_cache_roots`
- `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`
- `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_relation_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_parcel_source_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_parquet_readback_preserves_source_hash_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_binding_hashes_bind_every_component_hash`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_input_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_3_1_output_integrates_with_public_coding_api`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_empty_optional_catalogs_preserve_schema_and_crs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_parcels`

**Signature**

```python
def _integration_parcels() -> gpd.GeoDataFrame:
```

**Purpose**

Implements integration parcels according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': ['PARCEL-1'], 'existing_fact': [7]}, geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])], crs='EPSG:2154', index=pd.Index([91], name='parcel_row'))`.

**Algorithm**

1. Returns `gpd.GeoDataFrame({'parcel_id': ['PARCEL-1'], 'existing_fact': [7]}, geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])], crs='EPSG:2154', index=pd.Index([91], name='parcel_row'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `pd.Index`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_integration_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `resolve_planning_feature_codes`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_relation_types_are_retained`
- `tests/unit/test_resolve_planning_feature_codes.py` — `validate_planning_feature_code_result`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_inputs`

**Signature**

```python
def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
```

**Purpose**

Implements inputs according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, pd.DataFrame, CnigFeatureCodeProfile]`. Observed return expression(s): `(document, surface, line, point, relations, profile)`.

**Algorithm**

1. Computes `(document, _, surface, line, point, relations, profile)` from `_integration_inputs()`.
2. Returns `(document, surface, line, point, relations, profile)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_integration_inputs`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_empty_catalog`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_schema_v5_envelope_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalog_crs_must_be_canonical_epsg_2154`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalog_geometry_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalog_semantic_and_string_contracts_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalogs_and_relations_are_preserved_and_inputs_immutable`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_cnig_identity_provenance_is_exact`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_cnig_resolver_invokes_shared_factual_contract`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_complete_normalized_catalog_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_complete_relation_catalog_agreement_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_complete_relation_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_catalog_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_parcel_feature_relation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_relation_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_every_required_catalog_identity_is_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_exact_family_pair_resolution_and_leading_zeros`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_inactive_or_wrong_geometry_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_line_and_point_geometry_types_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_line_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_missing_catalog_crs_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_ogr_fid_provenance_is_restricted`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_parquet_readback_passes_source_complete_validation`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_planning_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_relation_catalog_code_mismatch_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_relation_identity_must_be_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_relation_type_must_match_catalog_geometry_kind`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_result_schema_versions_are_strict`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_feature_id_is_unique_inside_logical_layer`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_surface_geometry_contract_is_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_surface_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unexpected_factual_catalog_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unexpected_factual_relation_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unknown_relation_feature_id_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unparseable_catalog_crs_is_rejected`
- 1 additional static callers are indexed by the completeness audit.

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_crs_must_be_canonical_epsg_2154`
- `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_geometry_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_semantic_and_string_contracts_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py::test_catalogs_and_relations_are_preserved_and_inputs_immutable`
- `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_identity_provenance_is_exact`
- `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_resolver_invokes_shared_factual_contract`
- `tests/unit/test_resolve_planning_feature_codes.py::test_complete_normalized_catalog_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_catalog_agreement_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_catalog_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_parcel_feature_relation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_relation_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_every_required_catalog_identity_is_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py::test_exact_family_pair_resolution_and_leading_zeros`
- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_inactive_or_wrong_geometry_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_line_and_point_geometry_types_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py::test_line_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_missing_catalog_crs_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py::test_ogr_fid_provenance_is_restricted`
- `tests/unit/test_resolve_planning_feature_codes.py::test_parquet_readback_passes_source_complete_validation`
- `tests/unit/test_resolve_planning_feature_codes.py::test_planning_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_relation_catalog_code_mismatch_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_relation_identity_must_be_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py::test_relation_type_must_match_catalog_geometry_kind`
- `tests/unit/test_resolve_planning_feature_codes.py::test_result_schema_versions_are_strict`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_feature_id_is_unique_inside_logical_layer`
- `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`
- `tests/unit/test_resolve_planning_feature_codes.py::test_surface_geometry_contract_is_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py::test_surface_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_catalog_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_relation_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unknown_relation_feature_id_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unparseable_catalog_crs_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `resolve_planning_feature_codes`

**Signature**

```python
def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
```

**Purpose**

Exercise the new bound API while keeping legacy unit call sites compact.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureCodeResult`. Observed return expression(s): `_public_resolve_planning_feature_codes(planning_document, _integration_parcels(), surface_features, line_features, point_features, relations, code_profile)`.

**Algorithm**

1. Returns `_public_resolve_planning_feature_codes(planning_document, _integration_parcels(), surface_features, line_features, point_features, relations, code_profile)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_integration_parcels`, `_public_resolve_planning_feature_codes`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `_schema_v5_envelope_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalog_crs_must_be_canonical_epsg_2154`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalog_geometry_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalog_semantic_and_string_contracts_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_catalogs_and_relations_are_preserved_and_inputs_immutable`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_cnig_identity_provenance_is_exact`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_cnig_resolver_invokes_shared_factual_contract`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_complete_normalized_catalog_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_complete_relation_catalog_agreement_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_complete_relation_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_catalog_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_parcel_feature_relation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_relation_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_every_required_catalog_identity_is_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_exact_family_pair_resolution_and_leading_zeros`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_inactive_or_wrong_geometry_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_line_and_point_geometry_types_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_line_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_missing_catalog_crs_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_ogr_fid_provenance_is_restricted`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_parquet_readback_passes_source_complete_validation`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_planning_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_relation_catalog_code_mismatch_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_relation_identity_must_be_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_relation_type_must_match_catalog_geometry_kind`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_result_schema_versions_are_strict`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_feature_id_is_unique_inside_logical_layer`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_surface_geometry_contract_is_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_surface_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unexpected_factual_catalog_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unexpected_factual_relation_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unknown_relation_feature_id_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_unparseable_catalog_crs_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_wrong_planning_standard_is_rejected`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_crs_must_be_canonical_epsg_2154`
- `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_geometry_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_semantic_and_string_contracts_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py::test_catalogs_and_relations_are_preserved_and_inputs_immutable`
- `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_identity_provenance_is_exact`
- `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_resolver_invokes_shared_factual_contract`
- `tests/unit/test_resolve_planning_feature_codes.py::test_complete_normalized_catalog_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_catalog_agreement_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_schema_is_required`
- `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_catalog_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_parcel_feature_relation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_relation_columns_are_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_every_required_catalog_identity_is_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py::test_exact_family_pair_resolution_and_leading_zeros`
- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_inactive_or_wrong_geometry_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_line_and_point_geometry_types_are_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py::test_line_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_missing_catalog_crs_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`
- `tests/unit/test_resolve_planning_feature_codes.py::test_ogr_fid_provenance_is_restricted`
- `tests/unit/test_resolve_planning_feature_codes.py::test_parquet_readback_passes_source_complete_validation`
- `tests/unit/test_resolve_planning_feature_codes.py::test_planning_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_relation_catalog_code_mismatch_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_relation_identity_must_be_an_exact_non_null_string`
- `tests/unit/test_resolve_planning_feature_codes.py::test_relation_type_must_match_catalog_geometry_kind`
- `tests/unit/test_resolve_planning_feature_codes.py::test_result_schema_versions_are_strict`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_feature_id_is_unique_inside_logical_layer`
- `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`
- `tests/unit/test_resolve_planning_feature_codes.py::test_surface_geometry_contract_is_enforced`
- `tests/unit/test_resolve_planning_feature_codes.py::test_surface_relation_metrics_are_revalidated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_catalog_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_relation_column_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unknown_relation_feature_id_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_unparseable_catalog_crs_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `validate_planning_feature_code_result`

**Signature**

```python
def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
```

**Purpose**

Validates and rejects malformed planning feature code result according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `_public_validate_planning_feature_code_result(planning_document, _integration_parcels(), surface_features, line_features, point_features, relations, code_profile, result)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_integration_parcels`, `_public_validate_planning_feature_code_result`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_parquet_readback_passes_source_complete_validation`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_result_schema_versions_are_strict`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_parquet_readback_passes_source_complete_validation`
- `tests/unit/test_resolve_planning_feature_codes.py::test_result_schema_versions_are_strict`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cnig_resolver_invokes_shared_factual_contract.reject_shared_contract`

**Signature**

```python
def reject_shared_contract(*args: object) -> None:
```

**Purpose**

Implements reject shared contract according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.
3. Raises `ValueError('shared factual contract marker')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_physical`

**Signature**

```python
def counted_physical(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements counted physical according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `actual_physical(*args, **kwargs)`.

**Algorithm**

1. Updates `calls['physical']` using `` and `1`.
2. Returns `actual_physical(*args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual_physical`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_relations`

**Signature**

```python
def counted_relations(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements counted relations according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `actual_relations(*args, **kwargs)`.

**Algorithm**

1. Updates `calls['relations']` using `` and `1`.
2. Returns `actual_relations(*args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual_relations`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_gpu_related_source_hash_is_deterministic_across_cache_roots.relocated_reference`

**Signature**

```python
def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
```

**Purpose**

Implements relocated reference according to the exact implementation and guards in this file.

**Inputs**

- `reference` (`GpuSpatialLayerReference`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuSpatialLayerReference`. Observed return expression(s): `replace(reference, dataset_path=relocated_root / relative)`.

**Algorithm**

1. Computes `relative` from `reference.dataset_path.relative_to(source_root)`.
2. Returns `replace(reference, dataset_path=relocated_root / relative)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `reference.dataset_path.relative_to`, `replace`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_schema_v5_envelope_result`

**Signature**

```python
def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
```

**Purpose**

Implements schema v5 envelope result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `PlanningFeatureCodeResult`. Observed return expression(s): `resolve_planning_feature_codes(*_inputs())`.

**Algorithm**

1. Returns `resolve_planning_feature_codes(*_inputs())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_inputs`, `resolve_planning_feature_codes`.

**Known repository callers**

- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_dictionary_rows_are_intrinsically_validated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_dictionary_schema_is_explicit`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_envelope_controls_malformed_dictionary_type`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_envelope_rejects_geospatial_code_dictionary`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_scalar_lineage_contracts_are_intrinsic`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_rows_are_intrinsically_validated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_schema_is_explicit`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_controls_malformed_dictionary_type`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_geospatial_code_dictionary`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_scalar_lineage_contracts_are_intrinsic`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_canonical_empty_coded_result`

**Signature**

```python
def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
```

**Purpose**

Implements canonical empty coded result according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `empty_dictionary` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureCodeResult`. Observed return expression(s): `_result_with_hashes(replace(result, code_dictionary=dictionary, relations=relations, **catalogs))`.

**Algorithm**

1. Defines `catalogs` with annotation `dict[str, gpd.GeoDataFrame]` from `{}`.
2. Iterates `(field, kind)` over `(('surface_features', 'SURFACE'), ('line_features', 'LINE'), ('point_features', 'POINT'))`. For each value: Computes `output` from `getattr(result, field).iloc[0:0].copy(deep=True)`. Iterates `(column, dtype)` over `zip(output.columns, feature_dtypes(kind), strict=True)`. For each value: Checks `dtype != 'geometry'`. When true: Computes `output[column]` from `pd.Series(index=output.index, dtype=dtype)`. Computes `output.index` from `pd.Index([], dtype='int64')`. Executes 1 additional source-ordered statement(s).
3. Computes `relations` from `result.relations.iloc[0:0].copy(deep=True)`.
4. Iterates `(column, dtype)` over `zip(relations.columns, relation_dtypes(), strict=True)`. For each value: Computes `relations[column]` from `pd.Series(index=relations.index, dtype=dtype)`.
5. Computes `relations.index` from `pd.Index([], dtype='int64')`.
6. Computes `dictionary` from `result.code_dictionary.copy(deep=True)`.
7. Checks `empty_dictionary`. When true: Computes `dictionary` from `dictionary.iloc[0:0].copy(deep=True)`. Computes `dictionary.index` from `pd.Index([], dtype='int64')`.
8. Returns `_result_with_hashes(replace(result, code_dictionary=dictionary, relations=relations, **catalogs))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `dictionary.iloc[0:0].copy`, `getattr(result, field).iloc[0:0].copy`, `replace`, `result.code_dictionary.copy`, `result.relations.iloc[0:0].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_result_with_hashes`, `dictionary.iloc[0:0].copy`, `feature_dtypes`, `getattr`, `getattr(result, field).iloc[0:0].copy`, `pd.Index`, `pd.Series`, `relation_dtypes`, `replace`, `result.code_dictionary.copy`, `result.relations.iloc[0:0].copy`, `zip`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_family_pair_resolution_and_leading_zeros`

**Signature**

```python
def test_exact_family_pair_resolution_and_leading_zeros() -> None:
```

**Purpose**

Protects the `exact family pair resolution and leading zeros` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `resolve_planning_feature_codes(*_inputs())`.
- Computes `surface` from `result.surface_features.set_index('planning_feature_id')`.

**Action**

- Calls `_inputs`, `resolve_planning_feature_codes`, `result.surface_features.set_index`.

**Expected result**

- Direct assertions: `assert surface.loc['GPU:doc-1:prescription_surface:P-1', 'official_code_label'] == 'Prescription seven'`; `assert surface.loc['GPU:doc-1:information_surface:I-1', 'official_code_label'] == 'Information two'`; `assert result.line_features.iloc[0]['official_code_label'] == 'Prescription seven subtype four'`; `assert result.line_features.iloc[0]['type_code_raw'] == '07'`; `assert result.line_features.iloc[0]['subtype_code_raw'] == '04'`; `assert set(surface['official_code_status']) == {'RESOLVED_OFFICIAL'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact family pair resolution and leading zeros` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `resolve_planning_feature_codes`, `result.surface_features.set_index`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`

**Signature**

```python
def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
```

**Purpose**

Protects the `no type only or cross family fallback and unknown is retained` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `payload` from `_profile_payload()`.
- Computes `payload['records']` from `[record for record in payload['records'] if not (record['feature_family'], record['type_code'], record['subtype_code']) in {('PRESCRIPTION', '07', '04'), ('INFORMATION', '99', '00')}]`.
- Computes `payload['canonical_records_sha256']` from `_records_hash(payload['records'])`.
- Computes `profile` from `CnigFeatureCodeProfile.model_validate(payload)`.
- Computes `result` from `resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Action**

- Calls `CnigFeatureCodeProfile.model_validate`, `_inputs`, `_profile_payload`, `_records_hash`, `pd.isna`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert result.line_features.iloc[0]['official_code_status'] == 'UNKNOWN_CODE_PAIR'`; `assert pd.isna(result.line_features.iloc[0]['official_code_label'])`; `assert result.point_features.iloc[0]['official_code_status'] == 'UNKNOWN_CODE_PAIR'`; `assert len(result.line_features) == 1`; `assert len(result.point_features) == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no type only or cross family fallback and unknown is retained` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `_inputs`, `_profile_payload`, `_records_hash`, `len`, `pd.isna`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`

**Signature**

```python
def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
```

**Purpose**

Protects the `in memory profile model copy with wrong hash is revalidated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `inputs[-1]` from `_mutated_profile(canonical_records_sha256='f' * 64)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='profile|canonical')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `_mutated_profile`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='profile|canonical'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `in memory profile model copy with wrong hash is revalidated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `_mutated_profile`, `list`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`

**Signature**

```python
def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
```

**Purpose**

Protects the `in memory profile model construct with invalid schema is revalidated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `profile` from `_profile()`.
- Computes `invalid` from `CnigFeatureCodeProfile.model_construct(**{**profile.model_dump(mode='python'), 'schema_version': 1})`.
- Computes `inputs` from `list(_inputs())`.
- Computes `inputs[-1]` from `invalid`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='schema|profile')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_construct`, `_inputs`, `_profile`, `profile.model_dump`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='schema|profile'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `in memory profile model construct with invalid schema is revalidated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_construct`, `_inputs`, `_profile`, `list`, `profile.model_dump`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`

**Signature**

```python
def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
```

**Purpose**

Protects the `in memory profile model construct with duplicate pair is revalidated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `profile` from `_profile()`.
- Computes `invalid` from `CnigFeatureCodeProfile.model_construct(**{**profile.model_dump(mode='python'), 'records': (*profile.records, profile.records[0])})`.
- Computes `inputs` from `list(_inputs())`.
- Computes `inputs[-1]` from `invalid`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='duplicate|profile')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_construct`, `_inputs`, `_profile`, `profile.model_dump`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='duplicate|profile'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `in memory profile model construct with duplicate pair is revalidated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_construct`, `_inputs`, `_profile`, `list`, `profile.model_dump`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_official_family_endpoints_require_exact_identity`

**Signature**

```python
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
```

**Purpose**

Protects the `official family endpoints require exact identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `family`, `url`.
- Contains 5 explicit setup/context statement(s).
- Computes `payload` from `_profile_payload()`.
- Computes `payload['official_sources'][family]` from `url`.
- Computes `family_name` from `family.upper()`.
- Computes `payload['canonical_records_sha256']` from `_records_hash(payload['records'])`.
- Enters managed context(s) `pytest.raises(ValueError, match='official|source|URL')` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_validate`, `I_URL.replace`, `_profile_payload`, `_records_hash`, `family.upper`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='official|source|URL'): CnigFeatureCodeProfile.model_validate(payload)`.

**Regression protected**

- Protects the exact `official family endpoints require exact identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `I_URL.replace`, `_profile_payload`, `_records_hash`, `family.upper`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_official_text_must_already_be_canonical`

**Signature**

```python
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
```

**Purpose**

Protects the `official text must already be canonical` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `payload` from `_profile_payload()`.
- Computes `payload['records'][0][field]` from `value`.
- Computes `payload['canonical_records_sha256']` from `_records_hash(payload['records'])`.
- Enters managed context(s) `pytest.raises(ValueError, match='GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact')` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `_records_hash`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact'): CnigFeatureCodeProfile.model_validate(payload)`.

**Regression protected**

- Protects the exact `official text must already be canonical` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `_records_hash`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_code_is_rejected`

**Signature**

```python
def test_malformed_code_is_rejected(code: object) -> None:
```

**Purpose**

Protects the `malformed code is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `code`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_profile_payload()`.
- Computes `payload['records'][0]['type_code']` from `code`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_validate`, `_profile_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError): CnigFeatureCodeProfile.model_validate(payload)`.

**Regression protected**

- Protects the exact `malformed code is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_pair_and_profile_hash_mutation_are_rejected`

**Signature**

```python
def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
```

**Purpose**

Protects the `duplicate pair and profile hash mutation are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `payload` from `_profile_payload()`.
- Enters managed context(s) `pytest.raises(ValueError, match='duplicate')` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.
- Computes `payload` from `_profile_payload()`.
- Computes `payload['canonical_records_sha256']` from `'f' * 64`.
- Enters managed context(s) `pytest.raises(ValueError, match='canonical')` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `payload['records'].append`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='duplicate'): CnigFeatureCodeProfile.model_validate(payload)`; `with pytest.raises(ValueError, match='canonical'): CnigFeatureCodeProfile.model_validate(payload)`.

**Regression protected**

- Protects the exact `duplicate pair and profile hash mutation are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `dict`, `payload['records'].append`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_official_host_and_unknown_field_are_rejected`

**Signature**

```python
def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
```

**Purpose**

Protects the `wrong official host and unknown field are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `payload` from `_profile_payload()`.
- Computes `payload['official_sources']['prescription']` from `'https://example.com/codes'`.
- Enters managed context(s) `pytest.raises(ValueError, match='official|exact')` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.
- Computes `payload` from `_profile_payload()`.
- Computes `payload['semantic_policy']` from `'BLOCK'`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_validate`, `_profile_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='official|exact'): CnigFeatureCodeProfile.model_validate(payload)`; `with pytest.raises(ValueError): CnigFeatureCodeProfile.model_validate(payload)`.

**Regression protected**

- Protects the exact `wrong official host and unknown field are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_yaml_key_is_rejected`

**Signature**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate yaml key is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'codes.yaml'`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='Duplicate YAML')` and executes: Calls `load_cnig_feature_code_profile(path)` for its validation or side effect.

**Action**

- Calls `load_cnig_feature_code_profile`, `path.write_text`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='Duplicate YAML'): load_cnig_feature_code_profile(path)`.

**Regression protected**

- Protects the exact `duplicate yaml key is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_cnig_feature_code_profile`, `path.write_text`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_planning_standard_is_rejected`

**Signature**

```python
def test_wrong_planning_standard_is_rejected() -> None:
```

**Purpose**

Protects the `wrong planning standard is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `inputs[0]` from `_planning_document('CNIG PLU v2022')`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='standard')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `_planning_document`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='standard'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `wrong planning standard is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `_planning_document`, `list`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_catalogs_and_relations_are_preserved_and_inputs_immutable`

**Signature**

```python
def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
```

**Purpose**

Protects the `catalogs and relations are preserved and inputs immutable` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `_inputs()`.
- Computes `snapshots` from `[frame.copy(deep=True) for frame in inputs[1:5]]`.
- Computes `result` from `resolve_planning_feature_codes(*inputs)`.

**Action**

- Calls `_inputs`, `frame.copy`, `pd.testing.assert_frame_equal`, `resolve_planning_feature_codes`, `result.relations.index.equals`, `zip`.

**Expected result**

- Direct assertions: `assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS`; `assert result.relations.index.equals(inputs[4].index)`; `assert tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS):]) == OFFICIAL_CODE_COLUMNS`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `catalogs and relations are preserved and inputs immutable` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `assert_geodataframe_equal`, `frame.copy`, `len`, `pd.testing.assert_frame_equal`, `resolve_planning_feature_codes`, `result.relations.index.equals`, `tuple`, `zip`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_normalized_catalog_schema_is_required`

**Signature**

```python
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
```

**Purpose**

Protects the `complete normalized catalog schema is required` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `catalog_position`, `column`.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `inputs[catalog_position]` from `inputs[catalog_position].drop(columns=column)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='normalized|schema|column')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[catalog_position].drop`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='normalized|schema|column'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `complete normalized catalog schema is required` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[catalog_position].drop`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unexpected_factual_catalog_column_is_rejected`

**Signature**

```python
def test_unexpected_factual_catalog_column_is_rejected() -> None:
```

**Purpose**

Protects the `unexpected factual catalog column is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `surface` from `inputs[1].copy(deep=True)`.
- Computes `surface['unexpected_fact']` from `'not-produced-by-step-7d-3-1'`.
- Computes `inputs[1]` from `surface`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='normalized|schema|column')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[1].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='normalized|schema|column'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `unexpected factual catalog column is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[1].copy`, `list`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cnig_identity_provenance_is_exact`

**Signature**

```python
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
```

**Purpose**

Protects the `cnig identity provenance is exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `surface` from `inputs[1].copy(deep=True)`.
- Computes `surface.loc[surface.index[0], column]` from `value`.
- Computes `inputs[1]` from `surface`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='identity|provenance|normalized')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[1].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='identity|provenance|normalized'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `cnig identity provenance is exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[1].copy`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ogr_fid_provenance_is_restricted`

**Signature**

```python
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
```

**Purpose**

Protects the `ogr fid provenance is restricted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `logical_layer`, `feature_family`, `source_feature_id`.
- Contains 10 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `surface` from `inputs[1].copy(deep=True)`.
- Computes `row_index` from `surface.index[0]`.
- Computes `surface.loc[row_index, 'logical_layer']` from `logical_layer`.
- Computes `surface.loc[row_index, 'feature_family']` from `feature_family`.
- Computes `surface.loc[row_index, 'source_identity_kind']` from `'ARCHIVE_SCOPED_OGR_FID'`.
- Computes `surface.loc[row_index, 'source_identity_field']` from `'OGR_FID'`.
- Computes `surface.loc[row_index, 'source_feature_id']` from `source_feature_id`.
- Computes `inputs[1]` from `surface`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='OGR|identity|provenance|normalized')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[1].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='OGR|identity|provenance|normalized'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `ogr fid provenance is restricted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[1].copy`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_feature_id_is_unique_inside_logical_layer`

**Signature**

```python
def test_source_feature_id_is_unique_inside_logical_layer() -> None:
```

**Purpose**

Protects the `source feature id is unique inside logical layer` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 8 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `surface` from `inputs[1].copy(deep=True)`.
- Computes `surface.loc[surface.index[1], 'logical_layer']` from `surface.iloc[0]['logical_layer']`.
- Computes `surface.loc[surface.index[1], 'feature_family']` from `surface.iloc[0]['feature_family']`.
- Computes `surface.loc[surface.index[1], 'source_identity_field']` from `surface.iloc[0]['source_identity_field']`.
- Computes `surface.loc[surface.index[1], 'source_feature_id']` from `surface.iloc[0]['source_feature_id']`.
- Computes `inputs[1]` from `surface`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='source_feature_id|unique')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[1].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='source_feature_id|unique'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `source feature id is unique inside logical layer` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[1].copy`, `list`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_catalog_crs_must_be_canonical_epsg_2154`

**Signature**

```python
def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
```

**Purpose**

Protects the `catalog crs must be canonical epsg 2154` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `inputs[1]` from `inputs[1].to_crs('EPSG:4326')`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='EPSG:2154|CRS')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[1].to_crs`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='EPSG:2154|CRS'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `catalog crs must be canonical epsg 2154` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[1].to_crs`, `list`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_catalog_geometry_metrics_are_revalidated`

**Signature**

```python
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `catalog geometry metrics are revalidated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `catalog_position`, `column`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `catalog` from `inputs[catalog_position].copy(deep=True)`.
- Computes `catalog.loc[catalog.index[0], column]` from `value`.
- Computes `inputs[catalog_position]` from `catalog`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='metric|area|length|member')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[catalog_position].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='metric|area|length|member'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `catalog geometry metrics are revalidated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[catalog_position].copy`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_relation_schema_is_required`

**Signature**

```python
def test_complete_relation_schema_is_required() -> None:
```

**Purpose**

Protects the `complete relation schema is required` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `inputs[4]` from `inputs[4].drop(columns='intersection_length_m')`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='relation|schema|column')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[4].drop`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='relation|schema|column'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `complete relation schema is required` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[4].drop`, `list`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unexpected_factual_relation_column_is_rejected`

**Signature**

```python
def test_unexpected_factual_relation_column_is_rejected() -> None:
```

**Purpose**

Protects the `unexpected factual relation column is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `relations` from `inputs[4].copy(deep=True)`.
- Computes `relations['unexpected_metric']` from `0.0`.
- Computes `inputs[4]` from `relations`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='relation|schema')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[4].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='relation|schema'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `unexpected factual relation column is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[4].copy`, `list`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cnig_resolver_invokes_shared_factual_contract`

**Signature**

```python
def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `cnig resolver invokes shared factual contract` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `coding_module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `calls` from `0`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='shared factual contract marker')` and executes: Calls `resolve_planning_feature_codes(*_inputs())` for its validation or side effect.

**Action**

- Calls `ValueError`, `_inputs`, `importlib.import_module`, `monkeypatch.setattr`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert calls == 1`.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='shared factual contract marker'): resolve_planning_feature_codes(*_inputs())`.

**Regression protected**

- Protects the exact `cnig resolver invokes shared factual contract` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ValueError`, `_inputs`, `importlib.import_module`, `monkeypatch.setattr`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_relation_catalog_agreement_is_required`

**Signature**

```python
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `complete relation catalog agreement is required` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `relations` from `inputs[4].copy(deep=True)`.
- Computes `relations.loc[relations.index[0], column]` from `value`.
- Computes `inputs[4]` from `relations`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='catalog|metric|normalized|feature share')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[4].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='catalog|metric|normalized|feature share'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `complete relation catalog agreement is required` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[4].copy`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_surface_relation_metrics_are_revalidated`

**Signature**

```python
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
```

**Purpose**

Protects the `surface relation metrics are revalidated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `relations` from `inputs[4].copy(deep=True)`.
- Computes `relations.loc[relations.index[0], column]` from `value`.
- Computes `inputs[4]` from `relations`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='relation|metric|finite|percentage')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `float`, `inputs[4].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='relation|metric|finite|percentage'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `surface relation metrics are revalidated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `float`, `inputs[4].copy`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_relation_metrics_are_revalidated`

**Signature**

```python
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
```

**Purpose**

Protects the `line relation metrics are revalidated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 6 explicit setup/context statement(s).
- Computes `inputs` from `list(_inputs())`.
- Computes `relations` from `inputs[4].copy(deep=True)`.
- Computes `line_index` from `relations.index[relations['geometry_kind'].eq('LINE')][0]`.
- Computes `relations.loc[line_index, column]` from `value`.
- Computes `inputs[4]` from `relations`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='relation|length|catalog')` and executes: Calls `resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_inputs`, `inputs[4].copy`, `relations['geometry_kind'].eq`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='relation|length|catalog'): resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `line relation metrics are revalidated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `inputs[4].copy`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `relations['geometry_kind'].eq`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_catalog_columns_are_rejected`

**Signature**

```python
def test_duplicate_catalog_columns_are_rejected() -> None:
```

**Purpose**

Protects the `duplicate catalog columns are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `duplicate` from `pd.concat([surface, surface[['planning_feature_id']]], axis=1)`.
- Computes `duplicate` from `gpd.GeoDataFrame(duplicate, geometry='geometry', crs=surface.crs)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='duplicate|columns')` and executes: Calls `resolve_planning_feature_codes(document, duplicate, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `gpd.GeoDataFrame`, `pd.concat`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='duplicate|columns'): resolve_planning_feature_codes(document, duplicate, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `duplicate catalog columns are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `gpd.GeoDataFrame`, `pd.concat`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_catalog_crs_is_rejected`

**Signature**

```python
def test_missing_catalog_crs_is_rejected() -> None:
```

**Purpose**

Protects the `missing catalog crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `surface` from `surface.set_crs(None, allow_override=True)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='CRS')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `resolve_planning_feature_codes`, `surface.set_crs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='CRS'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `missing catalog crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.raises`, `resolve_planning_feature_codes`, `surface.set_crs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unparseable_catalog_crs_is_rejected`

**Signature**

```python
def test_unparseable_catalog_crs_is_rejected() -> None:
```

**Purpose**

Protects the `unparseable catalog crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `surface` from `surface.copy(deep=True)`.
- Computes `surface.geometry.array._crs` from `'definitely-not-a-crs'`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='CRS')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `resolve_planning_feature_codes`, `surface.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='CRS'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `unparseable catalog crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.raises`, `resolve_planning_feature_codes`, `surface.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inactive_or_wrong_geometry_column_is_rejected`

**Signature**

```python
def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
```

**Purpose**

Protects the `inactive or wrong geometry column is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `surface` from `surface.copy(deep=True)`.
- Computes `surface['alternate_geometry']` from `surface.geometry.copy()`.
- Computes `surface` from `surface.set_geometry('alternate_geometry')`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='geometry')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `resolve_planning_feature_codes`, `surface.copy`, `surface.geometry.copy`, `surface.set_geometry`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='geometry'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `inactive or wrong geometry column is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.raises`, `resolve_planning_feature_codes`, `surface.copy`, `surface.geometry.copy`, `surface.set_geometry`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_surface_geometry_contract_is_enforced`

**Signature**

```python
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
```

**Purpose**

Protects the `surface geometry contract is enforced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`, `message`.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `surface` from `surface.copy(deep=True)`.
- Computes `surface.at[surface.index[0], 'geometry']` from `geometry`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match=message)` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `LineString`, `Polygon`, `_inputs`, `resolve_planning_feature_codes`, `surface.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match=message): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `surface geometry contract is enforced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Polygon`, `_inputs`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`, `surface.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_multi_geometries_are_accepted`

**Signature**

```python
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
```

**Purpose**

Protects the `valid multi geometries are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `catalog_name`, `geometry`.
- Contains 6 explicit setup/context statement(s).
- Computes `(document, parcels, _, _, _, _, profile)` from `_integration_inputs()`.
- Computes `target_logical` from `{'surface': 'prescription_surface', 'line': 'prescription_line', 'point': 'information_point'}[catalog_name]`.
- Defines `changed_layers` with annotation `list[GpuInspectedLayer]` from `[]`.
- Computes `changed_document` from `_planning_document(related_layers=tuple(changed_layers))`.
- Computes `normalized` from `intersect_parcels_with_gpu_planning_features(parcels, changed_document)`.
- Computes `result` from `_public_resolve_planning_feature_codes(changed_document, parcels, normalized.surface_features, normalized.line_features, normalized.point_features, normalized.relations, profile)`.

**Action**

- Calls `MultiLineString`, `MultiPoint`, `MultiPolygon`, `Polygon`, `_integration_inputs`, `_integration_layer`, `_planning_document`, `_public_resolve_planning_feature_codes`, `changed_layers.append`, `getattr`, `getattr(result, f'{catalog_name}_features').geometry.iloc[0].equals`, `intersect_parcels_with_gpu_planning_features`, `layer.data.copy`.

**Expected result**

- Direct assertions: `assert getattr(result, f'{catalog_name}_features').geometry.iloc[0].equals(geometry)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid multi geometries are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiLineString`, `MultiPoint`, `MultiPolygon`, `Polygon`, `_integration_inputs`, `_integration_layer`, `_planning_document`, `_public_resolve_planning_feature_codes`, `changed_layers.append`, `getattr`, `getattr(result, f'{catalog_name}_features').geometry.iloc[0].equals`, `intersect_parcels_with_gpu_planning_features`, `layer.data.copy`, `pytest.mark.parametrize`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_catalog_semantic_and_string_contracts_are_enforced`

**Signature**

```python
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
```

**Purpose**

Protects the `catalog semantic and string contracts are enforced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`, `message`.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `surface` from `surface.copy(deep=True)`.
- Computes `surface.loc[surface.index[0], column]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match=message)` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `resolve_planning_feature_codes`, `surface.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match=message): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `catalog semantic and string contracts are enforced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`, `surface.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_required_catalog_identity_is_an_exact_non_null_string`

**Signature**

```python
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
```

**Purpose**

Protects the `every required catalog identity is an exact non null string` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 6 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `surface` from `surface.copy(deep=True)`.
- Computes `relations` from `relations.copy(deep=True)`.
- Computes `feature_id` from `surface.iloc[0]['planning_feature_id']`.
- Computes `surface.loc[surface.index[0], column]` from `' invalid '`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='exact string|non-empty')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `relations.copy`, `relations['planning_feature_id'].eq`, `resolve_planning_feature_codes`, `surface.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='exact string|non-empty'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `every required catalog identity is an exact non null string` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.mark.parametrize`, `pytest.raises`, `relations.copy`, `relations['planning_feature_id'].eq`, `resolve_planning_feature_codes`, `surface.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_and_point_geometry_types_are_enforced`

**Signature**

```python
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
```

**Purpose**

Protects the `line and point geometry types are enforced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `catalog_name`, `geometry`.
- Contains 6 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `catalogs` from `{'line': line.copy(deep=True), 'point': point.copy(deep=True)}`.
- Computes `catalog` from `catalogs[catalog_name]`.
- Computes `catalog.at[catalog.index[0], 'geometry']` from `geometry`.
- Computes `catalogs[catalog_name]` from `catalog`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='geometry|type')` and executes: Calls `resolve_planning_feature_codes(document, surface, catalogs['line'], catalogs['point'], relations, profile)` for its validation or side effect.

**Action**

- Calls `LineString`, `Polygon`, `_inputs`, `line.copy`, `point.copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='geometry|type'): resolve_planning_feature_codes(document, surface, catalogs['line'], catalogs['point'], relations, profile)`.

**Regression protected**

- Protects the exact `line and point geometry types are enforced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Polygon`, `_inputs`, `line.copy`, `point.copy`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_planning_feature_ids_are_globally_unique_across_catalogs`

**Signature**

```python
def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
```

**Purpose**

Protects the `planning feature ids are globally unique across catalogs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `line` from `line.copy(deep=True)`.
- Computes `line.loc[line.index[0], 'planning_feature_id']` from `surface.iloc[0]['planning_feature_id']`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='unique|catalog|deterministic')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `line.copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='unique|catalog|deterministic'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `planning feature ids are globally unique across catalogs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `line.copy`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_empty_optional_catalogs_preserve_schema_and_crs`

**Signature**

```python
def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
```

**Purpose**

Protects the `valid empty optional catalogs preserve schema and crs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `(document, parcels, _, _, _, _, profile)` from `_integration_inputs()`.
- Computes `surface_layers` from `tuple((layer for layer in document.related_layers if layer.logical_name in {'prescription_surface', 'information_surface'}))`.
- Computes `document` from `replace(document, related_layers=surface_layers)`.
- Computes `normalized` from `intersect_parcels_with_gpu_planning_features(parcels, document)`.
- Computes `result` from `_public_resolve_planning_feature_codes(document, parcels, normalized.surface_features, normalized.line_features, normalized.point_features, normalized.relations, profile)`.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `intersect_parcels_with_gpu_planning_features`, `replace`.

**Expected result**

- Direct assertions: `assert coded.empty`; `assert coded.crs == original.crs`; `assert tuple(coded.columns[:len(original.columns)]) == tuple(original.columns)`; `assert tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS):]) == OFFICIAL_CODE_COLUMNS`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid empty optional catalogs preserve schema and crs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `intersect_parcels_with_gpu_planning_features`, `len`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_catalog_code_mismatch_is_rejected`

**Signature**

```python
def test_relation_catalog_code_mismatch_is_rejected() -> None:
```

**Purpose**

Protects the `relation catalog code mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `relations` from `relations.copy(deep=True)`.
- Computes `relation_index` from `relations.index[0]`.
- Computes `original` from `relations.loc[relation_index, 'subtype_code_raw']`.
- Computes `relations.loc[relation_index, 'subtype_code_raw']` from `'04' if original != '04' else '00'`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='catalog')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `relations.copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='catalog'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `relation catalog code mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.raises`, `relations.copy`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_relation_columns_are_rejected`

**Signature**

```python
def test_duplicate_relation_columns_are_rejected() -> None:
```

**Purpose**

Protects the `duplicate relation columns are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `duplicate` from `pd.concat([relations, relations[['parcel_id']]], axis=1)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='duplicate|columns')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, duplicate, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `pd.concat`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='duplicate|columns'): resolve_planning_feature_codes(document, surface, line, point, duplicate, profile)`.

**Regression protected**

- Protects the exact `duplicate relation columns are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pd.concat`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_identity_must_be_an_exact_non_null_string`

**Signature**

```python
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `relation identity must be an exact non null string` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `relations` from `relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], column]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='relation|exact string')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `relations.copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='relation|exact string'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `relation identity must be an exact non null string` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.mark.parametrize`, `pytest.raises`, `relations.copy`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_feature_relation_is_rejected`

**Signature**

```python
def test_duplicate_parcel_feature_relation_is_rejected() -> None:
```

**Purpose**

Protects the `duplicate parcel feature relation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `relations` from `pd.concat([relations, relations.iloc[[0]]], ignore_index=True)`.
- Computes `relations` from `_canonical_relation_schema(relations)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='unique|duplicate')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_canonical_relation_schema`, `_inputs`, `pd.concat`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='unique|duplicate'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `duplicate parcel feature relation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_canonical_relation_schema`, `_inputs`, `pd.concat`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_relation_feature_id_is_rejected`

**Signature**

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
```

**Purpose**

Protects the `unknown relation feature id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `relations` from `relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'planning_feature_id']` from `'UNKNOWN'`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='unknown')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, relations, profile)` for its validation or side effect.

**Action**

- Calls `_inputs`, `relations.copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='unknown'): resolve_planning_feature_codes(document, surface, line, point, relations, profile)`.

**Regression protected**

- Protects the exact `unknown relation feature id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.raises`, `relations.copy`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_type_must_match_catalog_geometry_kind`

**Signature**

```python
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

**Purpose**

Protects the `relation type must match catalog geometry kind` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry_kind`, `relation_type`.
- Contains 9 explicit setup/context statement(s).
- Computes `(document, surface, line, point, relations, profile)` from `_inputs()`.
- Computes `catalogs` from `{'SURFACE': surface, 'LINE': line, 'POINT': point}`.
- Computes `feature` from `catalogs[geometry_kind].iloc[0]`.
- Computes `row` from `relations.iloc[0].copy()`.
- Computes `row['relation_type']` from `relation_type`.
- Computes `metric_columns` from `('feature_area_m2', 'source_line_length_m', 'intersection_area_m2', 'intersection_length_m', 'parcel_share_pct', 'feature_share_pct', 'point_member_count', 'point_members_inside_count', 'point_members_boundary_count')`.
- Computes `candidate` from `pd.DataFrame([row], columns=relations.columns)`.
- Computes `candidate` from `_canonical_relation_schema(candidate)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='[Rr]elation type|geometry')` and executes: Calls `resolve_planning_feature_codes(document, surface, line, point, candidate, profile)` for its validation or side effect.

**Action**

- Calls `_canonical_relation_schema`, `_inputs`, `pd.DataFrame`, `relations.iloc[0].copy`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='[Rr]elation type|geometry'): resolve_planning_feature_codes(document, surface, line, point, candidate, profile)`.

**Regression protected**

- Protects the exact `relation type must match catalog geometry kind` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_canonical_relation_schema`, `_inputs`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`, `relations.iloc[0].copy`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_relation_types_are_retained`

**Signature**

```python
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

**Purpose**

Protects the `valid relation types are retained` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry_kind`, `relation_type`.
- Contains 6 explicit setup/context statement(s).
- Defines `geometry` with annotation `object` without an initial value.
- Computes `source` from `_integration_source_frame(logical, [geometry], ['FEATURE-1'], ['07' if logical.startswith('prescription') else '99'], ['00'])`.
- Computes `document` from `_planning_document(related_layers=(_integration_layer(logical, source),))`.
- Computes `parcels` from `_integration_parcels()`.
- Computes `normalized` from `intersect_parcels_with_gpu_planning_features(parcels, document)`.
- Computes `result` from `_public_resolve_planning_feature_codes(document, parcels, normalized.surface_features, normalized.line_features, normalized.point_features, normalized.relations, _profile())`.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_integration_layer`, `_integration_parcels`, `_integration_source_frame`, `_planning_document`, `_profile`, `_public_resolve_planning_feature_codes`, `intersect_parcels_with_gpu_planning_features`, `logical.startswith`, `result.relations['relation_type'].tolist`.

**Expected result**

- Direct assertions: `assert result.relations['relation_type'].tolist() == [relation_type]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid relation types are retained` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_integration_layer`, `_integration_parcels`, `_integration_source_frame`, `_planning_document`, `_profile`, `_public_resolve_planning_feature_codes`, `intersect_parcels_with_gpu_planning_features`, `logical.startswith`, `pytest.mark.parametrize`, `result.relations['relation_type'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_output_hash_mutation_is_rejected`

**Signature**

```python
def test_coordinated_output_hash_mutation_is_rejected() -> None:
```

**Purpose**

Protects the `coordinated output hash mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `inputs` from `_inputs()`.
- Computes `result` from `resolve_planning_feature_codes(*inputs)`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `surface.loc[surface.index[0], 'official_code_label']` from `'Mutated'`.
- Computes `mutated` from `_result_with_hashes(replace(result, surface_features=surface))`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='rebuilt|meaning|dictionary')` and executes: Calls `validate_planning_feature_code_result(*inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_inputs`, `_result_with_hashes`, `replace`, `resolve_planning_feature_codes`, `result.surface_features.copy`, `validate_planning_feature_code_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='rebuilt|meaning|dictionary'): validate_planning_feature_code_result(*inputs, mutated)`.

**Regression protected**

- Protects the exact `coordinated output hash mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `_result_with_hashes`, `pytest.raises`, `replace`, `resolve_planning_feature_codes`, `result.surface_features.copy`, `validate_planning_feature_code_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parquet_readback_passes_source_complete_validation`

**Signature**

```python
def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
```

**Purpose**

Protects the `parquet readback passes source complete validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `inputs` from `_inputs()`.
- Computes `result` from `resolve_planning_feature_codes(*inputs)`.
- Computes `paths` from `{name: tmp_path / f'{name}.parquet' for name in ('code_dictionary', 'surface_features', 'line_features', 'point_features', 'relations')}`.
- Computes `persisted` from `replace(result, code_dictionary=pd.read_parquet(paths['code_dictionary']), surface_features=gpd.read_parquet(paths['surface_features']), line_features=gpd.read_parquet(paths['line_features']), point_features=gpd.read_parquet(paths['point_features']), relations=pd.read_parquet(paths['relations']))`.

**Action**

- Calls `_inputs`, `getattr`, `getattr(result, name).to_parquet`, `gpd.read_parquet`, `paths.items`, `pd.read_parquet`, `replace`, `resolve_planning_feature_codes`, `validate_planning_feature_code_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parquet readback passes source complete validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `getattr`, `getattr(result, name).to_parquet`, `gpd.read_parquet`, `paths.items`, `pd.read_parquet`, `replace`, `resolve_planning_feature_codes`, `validate_planning_feature_code_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_record_order_must_be_deterministic`

**Signature**

```python
def test_record_order_must_be_deterministic() -> None:
```

**Purpose**

Protects the `record order must be deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_profile_payload()`.
- Computes `payload['records']` from `list(reversed(payload['records']))`.
- Enters managed context(s) `pytest.raises(ValueError, match='deterministic order')` and executes: Calls `CnigFeatureCodeProfile.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `reversed`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='deterministic order'): CnigFeatureCodeProfile.model_validate(payload)`.

**Regression protected**

- Protects the exact `record order must be deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `_profile_payload`, `list`, `pytest.raises`, `reversed`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_yaml_snapshot_loads_strictly`

**Signature**

```python
def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
```

**Purpose**

Protects the `yaml snapshot loads strictly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `payload` from `_profile_payload()`.
- Computes `path` from `tmp_path / 'profile.yaml'`.

**Action**

- Calls `_profile`, `_profile_payload`, `load_cnig_feature_code_profile`, `path.write_text`, `yaml.safe_dump`.

**Expected result**

- Direct assertions: `assert load_cnig_feature_code_profile(path) == _profile()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `yaml snapshot loads strictly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_profile`, `_profile_payload`, `load_cnig_feature_code_profile`, `path.write_text`, `yaml.safe_dump`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stable_public_api_is_exported_from_module_and_stage_package`

**Signature**

```python
def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
```

**Purpose**

Protects the `stable public api is exported from module and stage package` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coding_module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `required` from `{'CnigFeatureCodeProfile', 'PlanningFeatureCodeError', 'PlanningFeatureCodeResult', 'load_cnig_feature_code_profile', 'resolve_planning_feature_codes', 'validate_planning_feature_code_result', 'validate_planning_feature_code_result_envelope'}`.
- Computes `low_level` from `{'_canonical_json_sha256', '_coded_catalog', '_lookup', '_profile_sha256', '_result_with_hashes'}`.

**Action**

- Calls `getattr`, `importlib.import_module`, `low_level.isdisjoint`, `required.issubset`.

**Expected result**

- Direct assertions: `assert required.issubset(set(coding_module.__all__))`; `assert required.issubset(set(stages.__all__))`; `assert low_level.isdisjoint(coding_module.__all__)`; `assert low_level.isdisjoint(stages.__all__)`; `assert getattr(stages, name) is getattr(coding_module, name)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `stable public api is exported from module and stage package` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `getattr`, `importlib.import_module`, `low_level.isdisjoint`, `required.issubset`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`

**Signature**

```python
def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
```

**Purpose**

Protects the `checked in official snapshot is complete for observed muret pairs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `path` from `Path('configs/planning/cnig_plu_2017_feature_codes.yaml')`.
- Computes `profile` from `load_cnig_feature_code_profile(path)`.
- Computes `expected_records` from `(('INFORMATION', '02', '00', "Zone d'aménagement concerté", 'L311-1 code de l’urbanisme', 'R151-52 8°', I_URL), ('INFORMATION', '14', '00', "Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)", 'L571-10 code de l’environnement', 'R151-53 5°', I_URL), ('INFORMATION', '27', '00…`.
- Computes `actual_records` from `tuple(((record.feature_family, record.type_code, record.subtype_code, record.official_label, record.legal_reference, record.regulation_or_annex_reference, record.official_source_url) for record in profile.records))`.

**Action**

- Calls `Path`, `_payload_hash`, `load_cnig_feature_code_profile`, `profile.model_dump`, `profile.retrieval_date.isoformat`.

**Expected result**

- Direct assertions: `assert profile.schema_version == 2`; `assert profile.profile == 'cnig_plu_2017_muret_observed_pairs_v2'`; `assert profile.standard_model == 'CNIG PLU v2017'`; `assert profile.official_text_normalization == TEXT_NORMALIZATION`; `assert profile.retrieval_date.isoformat() == '2026-08-12'`; `assert profile.official_sources.prescription == P_URL`; `assert profile.official_sources.information == I_URL`; `assert profile.canonical_records_sha256 == '5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c'`; `assert _payload_hash(profile.model_dump(mode='json')) == '5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee'`; `assert actual_records == expected_records`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checked in official snapshot is complete for observed muret pairs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `_payload_hash`, `load_cnig_feature_code_profile`, `profile.model_dump`, `profile.retrieval_date.isoformat`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_schema_versions_are_strict`

**Signature**

```python
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
```

**Purpose**

Protects the `result schema versions are strict` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `_inputs()`.
- Computes `result` from `resolve_planning_feature_codes(*inputs)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='schema version')` and executes: Calls `validate_planning_feature_code_result(*inputs, replace(result, **{field: value}))` for its validation or side effect.

**Action**

- Calls `_inputs`, `replace`, `resolve_planning_feature_codes`, `validate_planning_feature_code_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='schema version'): validate_planning_feature_code_result(*inputs, replace(result, **{field: value}))`.

**Regression protected**

- Protects the exact `result schema versions are strict` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `resolve_planning_feature_codes`, `validate_planning_feature_code_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_step_7d_3_1_output_integrates_with_public_coding_api`

**Signature**

```python
def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
```

**Purpose**

Protects the `step 7d 3 1 output integrates with public coding api` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `result` from `_public_resolve_planning_feature_codes(*inputs)`.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`.

**Expected result**

- Direct assertions: `assert result.result_hash_schema_version == 5`; `assert result.profile_schema_version == 2`; `assert len(result.surface_features) == 2`; `assert len(result.line_features) == 1`; `assert len(result.point_features) == 1`; `assert len(result.relations) == 2`; `assert set(result.surface_features['official_code_status']) == {'RESOLVED_OFFICIAL'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `step 7d 3 1 output integrates with public coding api` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `len`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats`

**Signature**

```python
def test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `resolver runs heavy factual validation once and public validator repeats` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coding_module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `enrich_module` from `importlib.import_module('landscout.stages.enrich_planning_features')`.
- Computes `actual_physical` from `enrich_module.revalidate_gpu_spatial_layer_sources`.
- Computes `actual_relations` from `enrich_module._build_relation_tables`.
- Computes `calls` from `{'physical': 0, 'relations': 0}`.
- Computes `result` from `coding_module.resolve_planning_feature_codes(*inputs)`.

**Action**

- Calls `_integration_inputs`, `actual_physical`, `actual_relations`, `coding_module.resolve_planning_feature_codes`, `coding_module.validate_planning_feature_code_result`, `importlib.import_module`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert calls == {'physical': 1, 'relations': 1}`; `assert calls == {'physical': 2, 'relations': 2}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `resolver runs heavy factual validation once and public validator repeats` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `actual_physical`, `actual_relations`, `coding_module.resolve_planning_feature_codes`, `coding_module.validate_planning_feature_code_result`, `importlib.import_module`, `monkeypatch.setattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coded_result_persists_all_source_input_hashes`

**Signature**

```python
def test_coded_result_persists_all_source_input_hashes() -> None:
```

**Purpose**

Protects the `coded result persists all source input hashes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_public_resolve_planning_feature_codes(*_integration_inputs())`.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `getattr`, `int`, `isinstance`.

**Expected result**

- Direct assertions: `assert isinstance(value, str)`; `assert len(value) == 64`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `coded result persists all source input hashes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `getattr`, `int`, `isinstance`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_input_hash_mutation_is_rejected`

**Signature**

```python
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
```

**Purpose**

Protects the `source input hash mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`.
- Contains 3 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `result` from `_public_resolve_planning_feature_codes(*inputs)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='hash|rebuilt|source')` and executes: Calls `_public_validate_planning_feature_code_result(*inputs, replace(result, **{field: 'f' * 64}))` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='hash|rebuilt|source'): _public_validate_planning_feature_code_result(*inputs, replace(result, **{field: 'f' * 64}))`.

**Regression protected**

- Protects the exact `source input hash mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_gpu_related_source_hash_is_deterministic_across_cache_roots`

**Signature**

```python
def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `gpu related source hash is deterministic across cache roots` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 9 explicit setup/context statement(s).
- Computes `first_inputs` from `_integration_inputs()`.
- Computes `first_document` from `first_inputs[0]`.
- Computes `source_root` from `first_document.extraction.extraction_root`.
- Computes `relocated_root` from `tmp_path / 'relocated-extraction'`.
- Computes `reference_map` from `{reference: relocated_reference(reference) for reference in first_document.all_spatial_layers}`.
- Computes `relocated_document` from `replace(first_document, extraction=replace(first_document.extraction, extraction_root=relocated_root), all_spatial_layers=tuple((reference_map[reference] for reference in first_document.all_spatial_layers)), zoning=replace(first_document.zoning, reference=reference_map[first_document.zoning.reference]), related_layers…`.
- Computes `second_inputs` from `(relocated_document, *first_inputs[1:])`.
- Computes `first` from `_public_resolve_planning_feature_codes(*first_inputs)`.
- Computes `second` from `_public_resolve_planning_feature_codes(*second_inputs)`.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `reference.dataset_path.relative_to`, `relocated_reference`, `replace`, `shutil.copytree`.

**Expected result**

- Direct assertions: `assert first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `gpu related source hash is deterministic across cache roots` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `reference.dataset_path.relative_to`, `relocated_reference`, `replace`, `shutil.copytree`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_binding_hashes_bind_every_component_hash`

**Signature**

```python
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
```

**Purpose**

Protects the `source binding hashes bind every component hash` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_public_resolve_planning_feature_codes(*_integration_inputs())`.
- Computes `changed` from `_result_with_hashes(replace(result, **{field: 'f' * 64}))`.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_result_with_hashes`, `getattr`, `replace`.

**Expected result**

- Direct assertions: `assert getattr(changed, hash_field) != getattr(result, hash_field)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source binding hashes bind every component hash` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_result_with_hashes`, `getattr`, `pytest.mark.parametrize`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_source_change_invalidates_coded_result`

**Signature**

```python
def test_parcel_source_change_invalidates_coded_result() -> None:
```

**Purpose**

Protects the `parcel source change invalidates coded result` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `inputs` from `list(_integration_inputs())`.
- Computes `result` from `_public_resolve_planning_feature_codes(*inputs)`.
- Computes `parcels` from `inputs[1].copy(deep=True)`.
- Computes `parcels.loc[parcels.index[0], 'parcel_id']` from `'CHANGED-PARCEL'`.
- Computes `inputs[1]` from `parcels`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='parcel|source|rebuilt')` and executes: Calls `_public_validate_planning_feature_code_result(*inputs, result)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `inputs[1].copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='parcel|source|rebuilt'): _public_validate_planning_feature_code_result(*inputs, result)`.

**Regression protected**

- Protects the exact `parcel source change invalidates coded result` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `inputs[1].copy`, `list`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_gpu_document_context_change_invalidates_coded_result`

**Signature**

```python
def test_gpu_document_context_change_invalidates_coded_result() -> None:
```

**Purpose**

Protects the `gpu document context change invalidates coded result` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `list(_integration_inputs())`.
- Computes `result` from `_public_resolve_planning_feature_codes(*inputs)`.
- Computes `planning_document` from `inputs[0]`.
- Computes `archive` from `planning_document.extraction.archive`.
- Computes `changed_document` from `replace(archive.document, provider='Changed provider')`.
- Computes `inputs[0]` from `replace(planning_document, extraction=replace(planning_document.extraction, archive=replace(archive, document=changed_document)))`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='document|source|rebuilt')` and executes: Calls `_public_validate_planning_feature_code_result(*inputs, result)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='document|source|rebuilt'): _public_validate_planning_feature_code_result(*inputs, result)`.

**Regression protected**

- Protects the exact `gpu document context change invalidates coded result` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `list`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`

**Signature**

```python
def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
```

**Purpose**

Protects the `normalized catalog change invalidates coded result even when coherent` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 10 explicit setup/context statement(s).
- Computes `inputs` from `list(_integration_inputs())`.
- Computes `result` from `_public_resolve_planning_feature_codes(*inputs)`.
- Computes `surface` from `inputs[2].copy(deep=True)`.
- Computes `relations` from `inputs[5].copy(deep=True)`.
- Computes `feature_id` from `surface.iloc[0]['planning_feature_id']`.
- Computes `surface.loc[surface.index[0], 'label_raw']` from `'Coherently changed'`.
- Computes `relations.loc[relations['planning_feature_id'].eq(feature_id), 'label_raw']` from `'Coherently changed'`.
- Computes `inputs[2]` from `surface`.
- Computes `inputs[5]` from `relations`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='normalized|source|rebuilt')` and executes: Calls `_public_validate_planning_feature_code_result(*inputs, result)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `inputs[2].copy`, `inputs[5].copy`, `relations['planning_feature_id'].eq`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='normalized|source|rebuilt'): _public_validate_planning_feature_code_result(*inputs, result)`.

**Regression protected**

- Protects the exact `normalized catalog change invalidates coded result even when coherent` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `inputs[2].copy`, `inputs[5].copy`, `list`, `pytest.raises`, `relations['planning_feature_id'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normalized_relation_change_invalidates_coded_result`

**Signature**

```python
def test_normalized_relation_change_invalidates_coded_result() -> None:
```

**Purpose**

Protects the `normalized relation change invalidates coded result` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `list(_integration_inputs())`.
- Computes `result` from `_public_resolve_planning_feature_codes(*inputs)`.
- Computes `relations` from `inputs[5].copy(deep=True)`.
- Computes `line_mask` from `relations['geometry_kind'].eq('LINE')`.
- Computes `relations.loc[line_mask, 'parcel_metric_area_m2']` from `8.0`.
- Computes `inputs[5]` from `relations`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='[Rr]elation|source|rebuilt')` and executes: Calls `_public_validate_planning_feature_code_result(*inputs, result)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `inputs[5].copy`, `relations['geometry_kind'].eq`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='[Rr]elation|source|rebuilt'): _public_validate_planning_feature_code_result(*inputs, result)`.

**Regression protected**

- Protects the exact `normalized relation change invalidates coded result` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `inputs[5].copy`, `list`, `pytest.raises`, `relations['geometry_kind'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`

**Signature**

```python
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
```

**Purpose**

Protects the `coding api rejects relation set not rebuilt from geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 4 explicit setup/context statement(s).
- Computes `inputs` from `list(_integration_inputs())`.
- Computes `relations` from `inputs[5].copy(deep=True)`.
- Computes `inputs[5]` from `relations`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='relation|parcel|source|rebuilt|normalized')` and executes: Calls `_public_resolve_planning_feature_codes(*inputs)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `inputs[5].copy`, `pd.concat`, `relations.iloc[1:].copy`, `relations.iloc[::-1].reset_index`, `relations.iloc[[0]].copy`, `relations['geometry_kind'].eq`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='relation|parcel|source|rebuilt|normalized'): _public_resolve_planning_feature_codes(*inputs)`.

**Regression protected**

- Protects the exact `coding api rejects relation set not rebuilt from geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `inputs[5].copy`, `list`, `pd.concat`, `pytest.mark.parametrize`, `pytest.raises`, `relations.iloc[1:].copy`, `relations.iloc[::-1].reset_index`, `relations.iloc[[0]].copy`, `relations['geometry_kind'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_parquet_readback_preserves_source_hash_envelope`

**Signature**

```python
def test_schema_v5_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `schema v5 parquet readback preserves source hash envelope` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `result` from `_public_resolve_planning_feature_codes(*inputs)`.
- Computes `paths` from `{name: tmp_path / f'integrated-{name}.parquet' for name in ('code_dictionary', 'surface_features', 'line_features', 'point_features', 'relations')}`.
- Computes `persisted` from `replace(result, code_dictionary=pd.read_parquet(paths['code_dictionary']), surface_features=gpd.read_parquet(paths['surface_features']), line_features=gpd.read_parquet(paths['line_features']), point_features=gpd.read_parquet(paths['point_features']), relations=pd.read_parquet(paths['relations']))`.

**Action**

- Calls `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `getattr`, `getattr(result, name).to_parquet`, `gpd.read_parquet`, `paths.items`, `pd.read_parquet`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `schema v5 parquet readback preserves source hash envelope` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_public_resolve_planning_feature_codes`, `_public_validate_planning_feature_code_result`, `getattr`, `getattr(result, name).to_parquet`, `gpd.read_parquet`, `paths.items`, `pd.read_parquet`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_public_api_signatures_remain_source_complete`

**Signature**

```python
def test_schema_v5_public_api_signatures_remain_source_complete() -> None:
```

**Purpose**

Protects the `schema v5 public api signatures remain source complete` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `inspect.signature`.

**Expected result**

- Direct assertions: `assert tuple(inspect.signature(_public_resolve_planning_feature_codes).parameters) == ('planning_document', 'parcels', 'surface_features', 'line_features', 'point_features', 'relations', 'code_profile')`; `assert tuple(inspect.signature(_public_validate_planning_feature_code_result).parameters) == ('planning_document', 'parcels', 'surface_features', 'line_features', 'point_features', 'relations', 'code_profile', 'result')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `schema v5 public api signatures remain source complete` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `inspect.signature`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`

**Signature**

```python
def test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator() -> None:
```

**Purpose**

Protects the `step 7d 5b 2b 5 exposes lightweight coded result validator` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `inputs` from `_inputs()`.
- Computes `result` from `resolve_planning_feature_codes(*inputs)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='hash|invalid')` and executes: Calls `module.validate_planning_feature_code_result_envelope(replace(result, complete_result_content_sha256='0' * 64))` for its validation or side effect.

**Action**

- Calls `_inputs`, `hasattr`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `replace`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert hasattr(module, 'validate_planning_feature_code_result_envelope')`.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='hash|invalid'): module.validate_planning_feature_code_result_envelope(replace(result, complete_result_content_sha256='0' * 64))`.

**Regression protected**

- Protects the exact `step 7d 5b 2b 5 exposes lightweight coded result validator` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_inputs`, `hasattr`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.raises`, `replace`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`

**Signature**

```python
def test_schema_v5_envelope_rejects_canonical_empty_code_dictionary() -> None:
```

**Purpose**

Protects the `schema v5 envelope rejects canonical empty code dictionary` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_canonical_empty_coded_result(_schema_v5_envelope_result(), empty_dictionary=True)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='dictionary|empty|record')` and executes: Calls `module.validate_planning_feature_code_result_envelope(result)` for its validation or side effect.

**Action**

- Calls `_canonical_empty_coded_result`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='dictionary|empty|record'): module.validate_planning_feature_code_result_envelope(result)`.

**Regression protected**

- Protects the exact `schema v5 envelope rejects canonical empty code dictionary` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_canonical_empty_coded_result`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`

**Signature**

```python
def test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs() -> None:
```

**Purpose**

Protects the `schema v5 envelope accepts nonempty dictionary with empty outputs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_canonical_empty_coded_result(_schema_v5_envelope_result(), empty_dictionary=False)`.

**Action**

- Calls `_canonical_empty_coded_result`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `sum`.

**Expected result**

- Direct assertions: `assert len(result.code_dictionary) >= 1`; `assert sum((len(frame) for frame in (result.surface_features, result.line_features, result.point_features, result.relations))) == 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `schema v5 envelope accepts nonempty dictionary with empty outputs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_canonical_empty_coded_result`, `_schema_v5_envelope_result`, `importlib.import_module`, `len`, `module.validate_planning_feature_code_result_envelope`, `sum`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_envelope_controls_malformed_dictionary_type`

**Signature**

```python
def test_schema_v5_envelope_controls_malformed_dictionary_type(
    dictionary: object,
) -> None:
```

**Purpose**

Protects the `schema v5 envelope controls malformed dictionary type` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `dictionary`.
- Contains 3 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_schema_v5_envelope_result()`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError)` and executes: Calls `module.validate_planning_feature_code_result_envelope(replace(result, code_dictionary=dictionary))` for its validation or side effect.

**Action**

- Calls `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError): module.validate_planning_feature_code_result_envelope(replace(result, code_dictionary=dictionary))`.

**Regression protected**

- Protects the exact `schema v5 envelope controls malformed dictionary type` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_envelope_rejects_geospatial_code_dictionary`

**Signature**

```python
def test_schema_v5_envelope_rejects_geospatial_code_dictionary() -> None:
```

**Purpose**

Protects the `schema v5 envelope rejects geospatial code dictionary` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_schema_v5_envelope_result()`.
- Computes `dictionary` from `gpd.GeoDataFrame(result.code_dictionary.copy(deep=True))`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='dictionary|DataFrame')` and executes: Calls `module.validate_planning_feature_code_result_envelope(replace(result, code_dictionary=dictionary))` for its validation or side effect.

**Action**

- Calls `_schema_v5_envelope_result`, `gpd.GeoDataFrame`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `replace`, `result.code_dictionary.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='dictionary|DataFrame'): module.validate_planning_feature_code_result_envelope(replace(result, code_dictionary=dictionary))`.

**Regression protected**

- Protects the exact `schema v5 envelope rejects geospatial code dictionary` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_schema_v5_envelope_result`, `gpd.GeoDataFrame`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.raises`, `replace`, `result.code_dictionary.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_dictionary_schema_is_explicit`

**Signature**

```python
def test_schema_v5_dictionary_schema_is_explicit(mutation: str) -> None:
```

**Purpose**

Protects the `schema v5 dictionary schema is explicit` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_schema_v5_envelope_result()`.
- Computes `dictionary` from `result.code_dictionary.copy(deep=True)`.
- Computes `changed` from `_result_with_hashes(replace(result, code_dictionary=dictionary))`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='dictionary|schema|dtype|index')` and executes: Calls `module.validate_planning_feature_code_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pd.Index`, `pd.RangeIndex`, `replace`, `result.code_dictionary.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='dictionary|schema|dtype|index'): module.validate_planning_feature_code_result_envelope(changed)`.

**Regression protected**

- Protects the exact `schema v5 dictionary schema is explicit` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_schema_v5_envelope_result`, `dictionary.index.rename`, `dictionary.index.to_numpy`, `dictionary['official_label'].astype`, `importlib.import_module`, `len`, `module.validate_planning_feature_code_result_envelope`, `pd.Index`, `pd.RangeIndex`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.code_dictionary.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_dictionary_rows_are_intrinsically_validated`

**Signature**

```python
def test_schema_v5_dictionary_rows_are_intrinsically_validated(mutation: str) -> None:
```

**Purpose**

Protects the `schema v5 dictionary rows are intrinsically validated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_schema_v5_envelope_result()`.
- Computes `dictionary` from `result.code_dictionary.copy(deep=True)`.
- Computes `changed` from `_result_with_hashes(replace(result, code_dictionary=dictionary))`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='dictionary|pair|code|family|URL|profile|order')` and executes: Calls `module.validate_planning_feature_code_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `replace`, `result.code_dictionary.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='dictionary|pair|code|family|URL|profile|order'): module.validate_planning_feature_code_result_envelope(changed)`.

**Regression protected**

- Protects the exact `schema v5 dictionary rows are intrinsically validated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_schema_v5_envelope_result`, `dictionary.iloc[::-1].copy`, `dictionary.loc[dictionary.index[0], ['feature_family', 'type_code', 'subtype_code']].tolist`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.code_dictionary.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_scalar_lineage_contracts_are_intrinsic`

**Signature**

```python
def test_schema_v5_scalar_lineage_contracts_are_intrinsic() -> None:
```

**Purpose**

Protects the `schema v5 scalar lineage contracts are intrinsic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_schema_v5_envelope_result()`.
- Computes `changed_standard` from `_result_with_hashes(replace(result, standard_model='CNIG PLU v2099'))`.
- Computes `malformed_sha` from `_result_with_hashes(replace(result, planning_document_context_sha256='not-a-sha'))`.

**Action**

- Calls `_result_with_hashes`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='standard|SHA|sha|lineage'): module.validate_planning_feature_code_result_envelope(changed)`.

**Regression protected**

- Protects the exact `schema v5 scalar lineage contracts are intrinsic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`

**Signature**

```python
def test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic() -> None:
```

**Purpose**

Protects the `schema v5 official rows and relation feature agreement are intrinsic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 11 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_schema_v5_envelope_result()`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `surface.loc[surface.index[0], 'official_code_label']` from `pd.NA`.
- Computes `missing_meaning` from `_result_with_hashes(replace(result, surface_features=surface))`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `surface.loc[surface.index[0], 'official_code_status']` from `'UNKNOWN_CODE_PAIR'`.
- Computes `invented_unknown` from `_result_with_hashes(replace(result, surface_features=surface))`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'official_code_label']` from `'Other official meaning'`.
- Computes `mismatched_relation` from `_result_with_hashes(replace(result, relations=relations))`.

**Action**

- Calls `_result_with_hashes`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `replace`, `result.relations.copy`, `result.surface_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='official|meaning|UNKNOWN|relation|feature'): module.validate_planning_feature_code_result_envelope(changed)`.

**Regression protected**

- Protects the exact `schema v5 official rows and relation feature agreement are intrinsic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.raises`, `replace`, `result.relations.copy`, `result.surface_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result`

**Signature**

```python
def test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result() -> (
    None
):
```

**Purpose**

Protects the `schema v5 envelope requires exact result type and accepts valid result` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `result` from `_schema_v5_envelope_result()`.
- Computes `derived` from `DerivedPlanningFeatureCodeResult(**result.__dict__)`.
- Enters managed context(s) `pytest.raises(PlanningFeatureCodeError, match='type|result')` and executes: Calls `module.validate_planning_feature_code_result_envelope(derived)` for its validation or side effect.

**Action**

- Calls `DerivedPlanningFeatureCodeResult`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningFeatureCodeError, match='type|result'): module.validate_planning_feature_code_result_envelope(derived)`.

**Regression protected**

- Protects the exact `schema v5 envelope requires exact result type and accepts valid result` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `DerivedPlanningFeatureCodeResult`, `_schema_v5_envelope_result`, `importlib.import_module`, `module.validate_planning_feature_code_result_envelope`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `DATVALID` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GPU:doc-1:information_surface:I-1` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GPU:doc-1:prescription_surface:P-1` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `IDURBA` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIBELLE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIB_IDZONE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NOMFIC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TXT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `URLFIC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `alternate_geometry` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `canonical_records_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `code_dictionary` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `existing_fact` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `feature_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `line` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `line_features` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `logical_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `official_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_sources` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `physical` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `point` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `point_features` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `point_member_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_boundary_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_inside_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `prescription` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `records` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `relations` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `semantic_policy` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_field` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_line_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `surface_features` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `type_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `type_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `unexpected_fact` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `unexpected_metric` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
