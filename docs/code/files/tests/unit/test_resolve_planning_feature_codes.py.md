# `tests/unit/test_resolve_planning_feature_codes.py`

## File identity

- Repository path: `tests/unit/test_resolve_planning_feature_codes.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.
- Source SHA256: `e27391c2e81b7e8d74d2d34da0df1590f4b1003ed0281dd99899c59cc2004e43`

## 1. Purpose

Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import importlib`
- `import inspect`
- `import json`
- `import shutil`
- `import tempfile`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `import yaml`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)`
- `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`
- `from landscout.stages.enrich_planning_features import (
    RELATION_COLUMNS,
    intersect_parcels_with_gpu_planning_features,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    resolve_planning_feature_codes as _public_resolve_planning_feature_codes,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    validate_planning_feature_code_result as _public_validate_planning_feature_code_result,
)`

## 4. Contract taxonomy

### A. Python constants

#### `P_URL`

```python
P_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `tests/unit/test_resolve_planning_feature_codes.py::_record` (value reference), `tests/unit/test_resolve_planning_feature_codes.py::_profile_payload` (value reference), `tests/unit/test_resolve_planning_feature_codes.py::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` (value reference).

#### `I_URL`

```python
I_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `tests/unit/test_resolve_planning_feature_codes.py::_record` (value reference), `tests/unit/test_resolve_planning_feature_codes.py::_profile_payload` (value reference), `tests/unit/test_resolve_planning_feature_codes.py::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` (value reference).

#### `TEXT_NORMALIZATION`

```python
TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_resolve_planning_feature_codes.py::_profile_payload` (value reference), `tests/unit/test_resolve_planning_feature_codes.py::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result.DerivedPlanningFeatureCodeResult`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** `PlanningFeatureCodeResult`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- constructor call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result` via `DerivedPlanningFeatureCodeResult`.

**Exact class source**

```python
class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
        pass
```


## 6. Functions and methods

### `_canonical_relation_schema`

**Exact signature**

```python
def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for canonical relation schema; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
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
- In-memory mutation: `output.index`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_parcel_feature_relation_is_rejected` via `_canonical_relation_schema`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_type_must_match_catalog_geometry_kind` via `_canonical_relation_schema`.

**Complete source-ordered implementation**

```python
def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
    output = frame.copy(deep=True)
    for column, dtype in zip(RELATION_COLUMNS, NORMALIZED_RELATION_DTYPES, strict=True):
        output[column] = pd.Series(
            output[column].tolist(), index=output.index, dtype=dtype
        )
    output.index = pd.RangeIndex(len(output))
    return output
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_records_hash`

**Exact signature**

```python
def _records_hash(records: list[dict[str, object]]) -> str:
```

**Purpose**

Private `test` helper for records hash; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(payload).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_profile_payload` via `_records_hash`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_records_hash`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_official_family_endpoints_require_exact_identity` via `_records_hash`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_official_text_must_already_be_canonical` via `_records_hash`.

**Complete source-ordered implementation**

```python
def _records_hash(records: list[dict[str, object]]) -> str:
    ordered = sorted(
        records,
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"]),
    )
    payload = json.dumps(
        ordered,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_payload_hash`

**Exact signature**

```python
def _payload_hash(payload: object) -> str:
```

**Purpose**

Private `test` helper for payload hash; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(encoded).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(encoded).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` via `_payload_hash`.

**Complete source-ordered implementation**

```python
def _payload_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_record`

**Exact signature**

```python
def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
```

**Purpose**

Private `test` helper for record; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'feature_family': family, 'type_code': type_code, 'subtype_code': subtype_code, 'official_label': label, 'legal_reference': None, 'regulation_or_annex_reference': None, 'official_source_url': P_URL if family == 'PRESCRIPTION' else I_URL}
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_profile_payload` via `_record`.

**Complete source-ordered implementation**

```python
def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
    return {
        "feature_family": family,
        "type_code": type_code,
        "subtype_code": subtype_code,
        "official_label": label,
        "legal_reference": None,
        "regulation_or_annex_reference": None,
        "official_source_url": P_URL if family == "PRESCRIPTION" else I_URL,
    }
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_profile_payload`

**Exact signature**

```python
def _profile_payload() -> dict[str, object]:
```

**Purpose**

Computes non-decisional summary statistics for payload; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'schema_version': 2, 'profile': 'synthetic_cnig_plu_2017', 'standard_model': 'CNIG PLU v2017', 'official_text_normalization': TEXT_NORMALIZATION, 'official_sources': {'prescription': P_URL, 'information': I_URL}, 'retrieval_date': '2026-08-12', 'canonical_records_sha256': _records_hash(records), 'records': records}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_records_hash`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_profile` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_official_family_endpoints_require_exact_identity` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_official_text_must_already_be_canonical` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_malformed_code_is_rejected` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_pair_and_profile_hash_mutation_are_rejected` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_official_host_and_unknown_field_are_rejected` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_record_order_must_be_deterministic` via `_profile_payload`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_yaml_snapshot_loads_strictly` via `_profile_payload`.

**Complete source-ordered implementation**

```python
def _profile_payload() -> dict[str, object]:
    records = [
        _record("INFORMATION", "02", "00", "Information two"),
        _record("INFORMATION", "99", "00", "Other information"),
        _record("PRESCRIPTION", "07", "00", "Prescription seven"),
        _record("PRESCRIPTION", "07", "04", "Prescription seven subtype four"),
    ]
    return {
        "schema_version": 2,
        "profile": "synthetic_cnig_plu_2017",
        "standard_model": "CNIG PLU v2017",
        "official_text_normalization": TEXT_NORMALIZATION,
        "official_sources": {
            "prescription": P_URL,
            "information": I_URL,
        },
        "retrieval_date": "2026-08-12",
        "canonical_records_sha256": _records_hash(records),
        "records": records,
    }
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_profile`

**Exact signature**

```python
def _profile() -> CnigFeatureCodeProfile:
```

**Purpose**

Computes non-decisional summary statistics for profile; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CnigFeatureCodeProfile`.
- Every observed return expression is reproduced without truncation:
```python
CnigFeatureCodeProfile.model_validate(_profile_payload())
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_legacy_inputs` via `_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_mutated_profile` via `_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_yaml_snapshot_loads_strictly` via `_profile`.

**Complete source-ordered implementation**

```python
def _profile() -> CnigFeatureCodeProfile:
    return CnigFeatureCodeProfile.model_validate(_profile_payload())
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_physical_inventory`

**Exact signature**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

**Purpose**

Private `test` helper for physical inventory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[GpuExtractedFile, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple((GpuExtractedFile(relative_path=path.relative_to(root).as_posix(), file_type=path.suffix.casefold().lstrip('.') or 'none', size_bytes=path.stat().st_size, sha256=sha256(path.read_bytes()).hexdigest(), category='SPATIAL_DATA') for path in sorted((item for item in root.rglob('*') if item.is_file()), key=str) if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `item.is_file`, `path.read_bytes`, `path.stat`, `root.rglob`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(path.read_bytes()).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `_physical_inventory`.

**Complete source-ordered implementation**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    return tuple(
        GpuExtractedFile(
            relative_path=path.relative_to(root).as_posix(),
            file_type=path.suffix.casefold().lstrip(".") or "none",
            size_bytes=path.stat().st_size,
            sha256=sha256(path.read_bytes()).hexdigest(),
            category="SPATIAL_DATA",
        )
        for path in sorted(
            (item for item in root.rglob("*") if item.is_file()), key=str
        )
        if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_extraction_manifest`

**Exact signature**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
```

**Purpose**

Serializes extraction manifest; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `(root / EXTRACTION_MANIFEST_NAME).write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `_write_extraction_manifest`.

**Complete source-ordered implementation**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": archive_sha256,
                "files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in files
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_layer_summary`

**Exact signature**

```python
def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
```

**Purpose**

Private `test` helper for layer summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
GpuLayerSummary(source_document_id='doc-1', source_archive_sha256='a' * 64, source_layer=source_layer, crs=frame.crs.to_string(), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna().sum())) for column in frame.columns)), geometry_types=tuple(((str(name), int(count)) for name, count in geometry.geom_type.value_counts().sort_index().items())), null_geometry_count=int((~non_null).sum()), empty_geometry_count=int((non_null & geometry.is_empty).sum()), invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `geometry.geom_type.value_counts`, `geometry.geom_type.value_counts().sort_index`, `geometry.geom_type.value_counts().sort_index().items`, `geometry.isna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `_layer_summary`.

**Complete source-ordered implementation**

```python
def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_planning_document`

**Exact signature**

```python
def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
```

**Purpose**

Private `test` helper for planning document; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuPlanningDocument`.
- Every observed return expression is reproduced without truncation:
```python
GpuPlanningDocument(extraction, (reference, *(layer.reference for layer in related_layers)), zoning, related_layers)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `gpd.read_file`.
- Filesystem write: `layer.data.to_file`, `zoning_data.to_file`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `physical_layers`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_legacy_inputs` via `_planning_document`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `_planning_document`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected` via `_planning_document`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted` via `_planning_document`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `_planning_document`.

**Complete source-ordered implementation**

```python
def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
    extraction_root = Path(tempfile.mkdtemp(prefix="landscout-code-source-"))
    physical_layers: list[GpuInspectedLayer] = []
    for layer in related_layers:
        path = extraction_root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=layer.reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reread = gpd.read_file(
            path, layer=layer.reference.source_layer, engine="pyogrio"
        )
        reference = replace(
            layer.reference,
            dataset_path=path,
            driver="GPKG",
        )
        physical_layers.append(
            replace(
                layer,
                reference=reference,
                data=reread,
                summary=_layer_summary(reread, reference.source_layer),
            )
        )
    related_layers = tuple(physical_layers)
    document = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="https://www.geoportail-urbanisme.gouv.fr",
        commune_code="31395",
        partition="DU_31395",
        document_id="doc-1",
        document_family="DU",
        document_type="PLU",
        document_title=None,
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name="31395_PLU_20240215",
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-08-12T00:00:00Z",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=1,
        sha256="a" * 64,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_data = gpd.GeoDataFrame(
        {"LIB_IDZONE": ["Z1"]},
        geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        crs="EPSG:2154",
    )
    zoning_path = extraction_root / "zones.gpkg"
    zoning_data.to_file(
        zoning_path,
        layer="ZONE",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_data = gpd.read_file(zoning_path, layer="ZONE", engine="pyogrio")
    reference = GpuSpatialLayerReference(zoning_path, "ZONE", "GPKG")
    summary = _layer_summary(zoning_data, "ZONE")
    zoning = GpuInspectedLayer("zoning", reference, zoning_data, summary)
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, archive.sha256, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(standard,),
        cache_hit=True,
    )
    return GpuPlanningDocument(
        extraction,
        (reference, *(layer.reference for layer in related_layers)),
        zoning,
        related_layers,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_base_row`

**Exact signature**

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

Private `test` helper for base row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'planning_feature_id': feature_id, 'source_feature_id': source_id, 'source_identity_kind': 'CNIG_ATTRIBUTE', 'source_identity_field': 'LIB_IDPSC' if family == 'PRESCRIPTION' else 'LIB_IDINFO', 'logical_layer': layer, 'feature_family': family, 'geometry_kind': kind, 'type_code_raw': type_code, 'subtype_code_raw': subtype_code, 'label_raw': None, 'text_raw': None, 'regulation_filename_raw': None, 'regulation_url_raw': None, 'source_document_reference_raw': '31395_PLU_20240215', 'source_validity_date_raw': '20240215', 'source_provider': "Géoportail de l'Urbanisme", 'source_portal': 'https://www.geoportail-urbanisme.gouv.fr', 'source_commune_code': '31395', 'source_document_id': 'doc-1', 'source_document_type': 'PLU', 'source_archive_name': '31395_PLU_20240215', 'source_archive_sha256': 'a' * 64, 'source_layer': layer.upper(), 'source_standard_model': 'CNIG PLU v2017', 'source_crs': 'EPSG:2154'}
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_legacy_inputs` via `_base_row`.

**Complete source-ordered implementation**

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
    return {
        "planning_feature_id": feature_id,
        "source_feature_id": source_id,
        "source_identity_kind": "CNIG_ATTRIBUTE",
        "source_identity_field": "LIB_IDPSC"
        if family == "PRESCRIPTION"
        else "LIB_IDINFO",
        "logical_layer": layer,
        "feature_family": family,
        "geometry_kind": kind,
        "type_code_raw": type_code,
        "subtype_code_raw": subtype_code,
        "label_raw": None,
        "text_raw": None,
        "regulation_filename_raw": None,
        "regulation_url_raw": None,
        "source_document_reference_raw": "31395_PLU_20240215",
        "source_validity_date_raw": "20240215",
        "source_provider": "Géoportail de l'Urbanisme",
        "source_portal": "https://www.geoportail-urbanisme.gouv.fr",
        "source_commune_code": "31395",
        "source_document_id": "doc-1",
        "source_document_type": "PLU",
        "source_archive_name": "31395_PLU_20240215",
        "source_archive_sha256": "a" * 64,
        "source_layer": layer.upper(),
        "source_standard_model": "CNIG PLU v2017",
        "source_crs": "EPSG:2154",
    }
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_legacy_inputs`

**Exact signature**

```python
def _legacy_inputs():
```

**Purpose**

Private `test` helper for legacy inputs; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
(_planning_document(), surface, line, point, relations, _profile())
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
- In-memory mutation: `line['feature_length_m']`, `point['point_member_count']`, `surface['feature_area_m2']`.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _legacy_inputs():
    surface_rows = [
        _base_row(
            "F-P-0700",
            "P-1",
            "PRESCRIPTION",
            "prescription_surface",
            "SURFACE",
            "07",
            "00",
        ),
        _base_row(
            "F-I-0200",
            "I-1",
            "INFORMATION",
            "information_surface",
            "SURFACE",
            "02",
            "00",
        ),
    ]
    surface = gpd.GeoDataFrame(
        surface_rows,
        geometry=[
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
            Polygon([(3, 0), (5, 0), (5, 2), (3, 2)]),
        ],
        crs="EPSG:2154",
        index=pd.Index([11, 22], name="source_row"),
    )
    surface["feature_area_m2"] = [4.0, 4.0]
    line = gpd.GeoDataFrame(
        [
            _base_row(
                "F-P-0704",
                "P-2",
                "PRESCRIPTION",
                "prescription_line",
                "LINE",
                "07",
                "04",
            )
        ],
        geometry=[LineString([(0, 0), (2, 0)])],
        crs="EPSG:2154",
        index=pd.Index([33], name="source_row"),
    )
    line["feature_length_m"] = [2.0]
    point = gpd.GeoDataFrame(
        [
            _base_row(
                "F-I-9900",
                "I-2",
                "INFORMATION",
                "information_point",
                "POINT",
                "99",
                "00",
            )
        ],
        geometry=[Point(1, 1)],
        crs="EPSG:2154",
        index=pd.Index([44], name="source_row"),
    )
    point["point_member_count"] = [1]
    relations = pd.DataFrame(
        [
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: surface.iloc[0][key]
                    for key in (
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
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "AREA_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": 4.0,
                "source_line_length_m": None,
                "intersection_area_m2": 4.0,
                "intersection_length_m": None,
                "parcel_share_pct": 100.0,
                "feature_share_pct": 100.0,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: line.iloc[0][key]
                    for key in (
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
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "LENGTH_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": None,
                "source_line_length_m": 2.0,
                "intersection_area_m2": None,
                "intersection_length_m": 2.0,
                "parcel_share_pct": None,
                "feature_share_pct": None,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
        ],
        index=pd.Index([101, 102], name="relation_row"),
    )
    relations = relations.loc[:, list(RELATION_COLUMNS)]
    return _planning_document(), surface, line, point, relations, _profile()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_mutated_profile`

**Exact signature**

```python
def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
```

**Purpose**

Build a deliberately unvalidated frozen profile for boundary tests.

**Return contract**

- Declared return annotation: `CnigFeatureCodeProfile`.
- Every observed return expression is reproduced without truncation:
```python
profile.model_copy(update=updates)
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `_mutated_profile`.

**Complete source-ordered implementation**

```python
def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
    """Build a deliberately unvalidated frozen profile for boundary tests."""

    profile = _profile()
    return profile.model_copy(update=updates)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_empty_catalog`

**Exact signature**

```python
def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
```

**Purpose**

Return an optional empty catalog with the deterministic source schema.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
template.iloc[0:0].copy()
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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
    """Return an optional empty catalog with the deterministic source schema."""

    _, surface, line, point, _, _ = _inputs()
    template = {"SURFACE": surface, "LINE": line, "POINT": point}[kind]
    return template.iloc[0:0].copy()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_source_frame`

**Exact signature**

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

Private `test` helper for integration source frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'LIBELLE': [f'Label {identifier}' for identifier in source_ids], 'TXT': [None] * len(source_ids), 'TYPEPSC' if prescription else 'TYPEINF': type_codes, 'STYPEPSC' if prescription else 'STYPEINF': subtype_codes, 'NOMFIC': [None] * len(source_ids), 'URLFIC': [None] * len(source_ids), 'IDURBA': ['31395_PLU_20240215'] * len(source_ids), 'DATVALID': ['20240215'] * len(source_ids), 'LIB_IDPSC' if prescription else 'LIB_IDINFO': source_ids}, geometry=geometries, crs='EPSG:2154')
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `_integration_source_frame`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `_integration_source_frame`.

**Complete source-ordered implementation**

```python
def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
    prescription = logical_layer.startswith("prescription")
    return gpd.GeoDataFrame(
        {
            "LIBELLE": [f"Label {identifier}" for identifier in source_ids],
            "TXT": [None] * len(source_ids),
            ("TYPEPSC" if prescription else "TYPEINF"): type_codes,
            ("STYPEPSC" if prescription else "STYPEINF"): subtype_codes,
            "NOMFIC": [None] * len(source_ids),
            "URLFIC": [None] * len(source_ids),
            "IDURBA": ["31395_PLU_20240215"] * len(source_ids),
            "DATVALID": ["20240215"] * len(source_ids),
            ("LIB_IDPSC" if prescription else "LIB_IDINFO"): source_ids,
        },
        geometry=geometries,
        crs="EPSG:2154",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_layer`

**Exact signature**

```python
def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
```

**Purpose**

Private `test` helper for integration layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuInspectedLayer`.
- Every observed return expression is reproduced without truncation:
```python
GpuInspectedLayer(logical_layer, reference, frame, summary)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `geometry.geom_type.value_counts`, `geometry.geom_type.value_counts().sort_index`, `geometry.geom_type.value_counts().sort_index().items`, `geometry.isna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `_integration_layer`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted` via `_integration_layer`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `_integration_layer`.

**Complete source-ordered implementation**

```python
def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
    source_layer = logical_layer.upper()
    reference = GpuSpatialLayerReference(
        Path(f"{logical_layer}.gpkg"), source_layer, "GPKG"
    )
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
    return GpuInspectedLayer(logical_layer, reference, frame, summary)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_inputs`

**Exact signature**

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

Private `test` helper for integration inputs; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, pd.DataFrame, CnigFeatureCodeProfile]`.
- Every observed return expression is reproduced without truncation:
```python
(planning_document, parcels, normalized.surface_features, normalized.line_features, normalized.point_features, normalized.relations, _profile())
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_inputs` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coded_result_persists_all_source_input_hashes` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_input_hash_mutation_is_rejected` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_related_source_hash_is_deterministic_across_cache_roots` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_binding_hashes_bind_every_component_hash` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_parcel_source_change_invalidates_coded_result` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_document_context_change_invalidates_coded_result` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_relation_change_invalidates_coded_result` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `_integration_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_integration_inputs`.

**Complete source-ordered implementation**

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
    layers = (
        _integration_layer(
            "prescription_surface",
            _integration_source_frame(
                "prescription_surface",
                [Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
                ["P-1"],
                ["07"],
                ["00"],
            ),
        ),
        _integration_layer(
            "information_surface",
            _integration_source_frame(
                "information_surface",
                [Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])],
                ["I-1"],
                ["02"],
                ["00"],
            ),
        ),
        _integration_layer(
            "prescription_line",
            _integration_source_frame(
                "prescription_line",
                [LineString([(0, 1), (2, 1)])],
                ["P-2"],
                ["07"],
                ["04"],
            ),
        ),
        _integration_layer(
            "information_point",
            _integration_source_frame(
                "information_point",
                [Point(10, 10)],
                ["I-2"],
                ["99"],
                ["00"],
            ),
        ),
    )
    planning_document = _planning_document(related_layers=layers)
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(
        parcels, planning_document
    )
    return (
        planning_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_integration_parcels`

**Exact signature**

```python
def _integration_parcels() -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for integration parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'parcel_id': ['PARCEL-1'], 'existing_fact': [7]}, geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])], crs='EPSG:2154', index=pd.Index([91], name='parcel_row'))
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `_integration_parcels`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_integration_parcels`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_integration_parcels`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `_integration_parcels`.

**Complete source-ordered implementation**

```python
def _integration_parcels() -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "existing_fact": [7]},
        geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
        crs="EPSG:2154",
        index=pd.Index([91], name="parcel_row"),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_inputs`

**Exact signature**

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

Private `test` helper for inputs; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, pd.DataFrame, CnigFeatureCodeProfile]`.
- Every observed return expression is reproduced without truncation:
```python
(document, surface, line, point, relations, profile)
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_empty_catalog` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_exact_family_pair_resolution_and_leading_zeros` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalogs_and_relations_are_preserved_and_inputs_immutable` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_normalized_catalog_schema_is_required` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_catalog_column_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_identity_provenance_is_exact` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_ogr_fid_provenance_is_restricted` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_feature_id_is_unique_inside_logical_layer` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_crs_must_be_canonical_epsg_2154` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_geometry_metrics_are_revalidated` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_schema_is_required` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_relation_column_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_resolver_invokes_shared_factual_contract` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_catalog_agreement_is_required` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_surface_relation_metrics_are_revalidated` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_line_relation_metrics_are_revalidated` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_catalog_columns_are_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_missing_catalog_crs_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unparseable_catalog_crs_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_inactive_or_wrong_geometry_column_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_surface_geometry_contract_is_enforced` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_semantic_and_string_contracts_are_enforced` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_every_required_catalog_identity_is_an_exact_non_null_string` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_line_and_point_geometry_types_are_enforced` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_planning_feature_ids_are_globally_unique_across_catalogs` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_catalog_code_mismatch_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_relation_columns_are_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_identity_must_be_an_exact_non_null_string` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_parcel_feature_relation_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unknown_relation_feature_id_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_type_must_match_catalog_geometry_kind` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_parquet_readback_passes_source_complete_validation` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_result_schema_versions_are_strict` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `_inputs`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_schema_v5_envelope_result` via `_inputs`.

**Complete source-ordered implementation**

```python
def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    document, _, surface, line, point, relations, profile = _integration_inputs()
    return document, surface, line, point, relations, profile
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `resolve_planning_feature_codes`

**Exact signature**

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

**Return contract**

- Declared return annotation: `PlanningFeatureCodeResult`.
- Every observed return expression is reproduced without truncation:
```python
_public_resolve_planning_feature_codes(planning_document, _integration_parcels(), surface_features, line_features, point_features, relations, code_profile)
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_exact_family_pair_resolution_and_leading_zeros` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalogs_and_relations_are_preserved_and_inputs_immutable` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_normalized_catalog_schema_is_required` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_catalog_column_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_identity_provenance_is_exact` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_ogr_fid_provenance_is_restricted` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_feature_id_is_unique_inside_logical_layer` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_crs_must_be_canonical_epsg_2154` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_geometry_metrics_are_revalidated` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_schema_is_required` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_relation_column_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_resolver_invokes_shared_factual_contract` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_catalog_agreement_is_required` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_surface_relation_metrics_are_revalidated` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_line_relation_metrics_are_revalidated` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_catalog_columns_are_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_missing_catalog_crs_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unparseable_catalog_crs_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_inactive_or_wrong_geometry_column_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_surface_geometry_contract_is_enforced` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_semantic_and_string_contracts_are_enforced` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_every_required_catalog_identity_is_an_exact_non_null_string` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_line_and_point_geometry_types_are_enforced` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_planning_feature_ids_are_globally_unique_across_catalogs` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_catalog_code_mismatch_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_relation_columns_are_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_identity_must_be_an_exact_non_null_string` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_parcel_feature_relation_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_unknown_relation_feature_id_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_type_must_match_catalog_geometry_kind` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_parquet_readback_passes_source_complete_validation` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_result_schema_versions_are_strict` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_schema_v5_envelope_result` via `resolve_planning_feature_codes`.

**Complete source-ordered implementation**

```python
def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Exercise the new bound API while keeping legacy unit call sites compact."""

    return _public_resolve_planning_feature_codes(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `validate_planning_feature_code_result`

**Exact signature**

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

Rejects malformed or inconsistent planning feature code result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected` via `validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_parquet_readback_passes_source_complete_validation` via `validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_result_schema_versions_are_strict` via `validate_planning_feature_code_result`.

**Complete source-ordered implementation**

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
    _public_validate_planning_feature_code_result(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
        result,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_family_pair_resolution_and_leading_zeros`

**Purpose**

Exercises `exact family pair resolution and leading zeros`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = resolve_planning_feature_codes(*_inputs())
surface = result.surface_features.set_index("planning_feature_id")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert (
        surface.loc["GPU:doc-1:prescription_surface:P-1", "official_code_label"]
        == "Prescription seven"
    )
assert (
        surface.loc["GPU:doc-1:information_surface:I-1", "official_code_label"]
        == "Information two"
    )
assert (
        result.line_features.iloc[0]["official_code_label"]
        == "Prescription seven subtype four"
    )
assert result.line_features.iloc[0]["type_code_raw"] == "07"
assert result.line_features.iloc[0]["subtype_code_raw"] == "04"
assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}
```

**Regression protected**

Locks `exact family pair resolution and leading zeros` through the exact asserted conditions: `surface.loc['GPU:doc-1:prescription_surface:P-1', 'official_code_label'] == 'Prescription seven'`; `surface.loc['GPU:doc-1:information_surface:I-1', 'official_code_label'] == 'Information two'`; `result.line_features.iloc[0]['official_code_label'] == 'Prescription seven subtype four'`; `result.line_features.iloc[0]['type_code_raw'] == '07'`; plus 2 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_family_pair_resolution_and_leading_zeros() -> None:
    result = resolve_planning_feature_codes(*_inputs())
    surface = result.surface_features.set_index("planning_feature_id")
    assert (
        surface.loc["GPU:doc-1:prescription_surface:P-1", "official_code_label"]
        == "Prescription seven"
    )
    assert (
        surface.loc["GPU:doc-1:information_surface:I-1", "official_code_label"]
        == "Information two"
    )
    assert (
        result.line_features.iloc[0]["official_code_label"]
        == "Prescription seven subtype four"
    )
    assert result.line_features.iloc[0]["type_code_raw"] == "07"
    assert result.line_features.iloc[0]["subtype_code_raw"] == "04"
    assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}
```

### `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`

**Purpose**

Exercises `no type only or cross family fallback and unknown is retained`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
payload = _profile_payload()
payload["records"] = [
        record
        for record in payload["records"]
        if not (
            (record["feature_family"], record["type_code"], record["subtype_code"])
            in {("PRESCRIPTION", "07", "04"), ("INFORMATION", "99", "00")}
        )
    ]
payload["canonical_records_sha256"] = _records_hash(payload["records"])
profile = CnigFeatureCodeProfile.model_validate(payload)
result = resolve_planning_feature_codes(
        document, surface, line, point, relations, profile
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.line_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
assert pd.isna(result.line_features.iloc[0]["official_code_label"])
assert result.point_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
assert len(result.line_features) == 1
assert len(result.point_features) == 1
```

**Regression protected**

Locks `no type only or cross family fallback and unknown is retained` through the exact asserted conditions: `result.line_features.iloc[0]['official_code_status'] == 'UNKNOWN_CODE_PAIR'`; `pd.isna(result.line_features.iloc[0]['official_code_label'])`; `result.point_features.iloc[0]['official_code_status'] == 'UNKNOWN_CODE_PAIR'`; `len(result.line_features) == 1`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
    document, surface, line, point, relations, profile = _inputs()
    payload = _profile_payload()
    payload["records"] = [
        record
        for record in payload["records"]
        if not (
            (record["feature_family"], record["type_code"], record["subtype_code"])
            in {("PRESCRIPTION", "07", "04"), ("INFORMATION", "99", "00")}
        )
    ]
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    profile = CnigFeatureCodeProfile.model_validate(payload)
    result = resolve_planning_feature_codes(
        document, surface, line, point, relations, profile
    )
    assert result.line_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert pd.isna(result.line_features.iloc[0]["official_code_label"])
    assert result.point_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1
```

### `test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`

**Purpose**

Exercises `in memory profile model copy with wrong hash is revalidated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_inputs())
inputs[-1] = _mutated_profile(canonical_records_sha256="f" * 64)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="profile|canonical"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `in memory profile model copy with wrong hash is revalidated`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
    inputs = list(_inputs())
    inputs[-1] = _mutated_profile(canonical_records_sha256="f" * 64)
    with pytest.raises(PlanningFeatureCodeError, match="profile|canonical"):
        resolve_planning_feature_codes(*inputs)
```

### `test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`

**Purpose**

Exercises `in memory profile model construct with invalid schema is revalidated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
profile = _profile()
invalid = CnigFeatureCodeProfile.model_construct(
        **{**profile.model_dump(mode="python"), "schema_version": 1}
    )
inputs = list(_inputs())
inputs[-1] = invalid
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="schema|profile"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `in memory profile model construct with invalid schema is revalidated`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{**profile.model_dump(mode="python"), "schema_version": 1}
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="schema|profile"):
        resolve_planning_feature_codes(*inputs)
```

### `test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`

**Purpose**

Exercises `in memory profile model construct with duplicate pair is revalidated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
profile = _profile()
invalid = CnigFeatureCodeProfile.model_construct(
        **{
            **profile.model_dump(mode="python"),
            "records": (*profile.records, profile.records[0]),
        }
    )
inputs = list(_inputs())
inputs[-1] = invalid
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="duplicate|profile"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `in memory profile model construct with duplicate pair is revalidated`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{
            **profile.model_dump(mode="python"),
            "records": (*profile.records, profile.records[0]),
        }
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|profile"):
        resolve_planning_feature_codes(*inputs)
```

### `test_official_family_endpoints_require_exact_identity`

**Purpose**

Exercises `official family endpoints require exact identity`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `family`, `url`.

**Setup**

```python
payload = _profile_payload()
payload["official_sources"][family] = url
family_name = family.upper()
for record in payload["records"]:
        if record["feature_family"] == family_name:
            record["official_source_url"] = url
payload["canonical_records_sha256"] = _records_hash(payload["records"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="official|source|URL"):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Regression protected**

Locks `official family endpoints require exact identity`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
    payload = _profile_payload()
    payload["official_sources"][family] = url
    family_name = family.upper()
    for record in payload["records"]:
        if record["feature_family"] == family_name:
            record["official_source_url"] = url
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(ValueError, match="official|source|URL"):
        CnigFeatureCodeProfile.model_validate(payload)
```

### `test_official_text_must_already_be_canonical`

**Purpose**

Exercises `official text must already be canonical`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
payload = _profile_payload()
payload["records"][0][field] = value
payload["canonical_records_sha256"] = _records_hash(payload["records"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        ValueError,
        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact",
    ):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Regression protected**

Locks `official text must already be canonical`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
    payload = _profile_payload()
    payload["records"][0][field] = value
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(
        ValueError,
        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact",
    ):
        CnigFeatureCodeProfile.model_validate(payload)
```

### `test_malformed_code_is_rejected`

**Purpose**

Exercises `malformed code is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `code`.

**Setup**

```python
payload = _profile_payload()
payload["records"][0]["type_code"] = code
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Regression protected**

Locks `malformed code is rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_code_is_rejected(code: object) -> None:
    payload = _profile_payload()
    payload["records"][0]["type_code"] = code
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)
```

### `test_duplicate_pair_and_profile_hash_mutation_are_rejected`

**Purpose**

Exercises `duplicate pair and profile hash mutation are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _profile_payload()
payload["records"].append(dict(payload["records"][0]))
payload = _profile_payload()
payload["canonical_records_sha256"] = "f" * 64
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="duplicate"):
        CnigFeatureCodeProfile.model_validate(payload)
with pytest.raises(ValueError, match="canonical"):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
    payload = _profile_payload()
    payload["records"].append(dict(payload["records"][0]))
    with pytest.raises(ValueError, match="duplicate"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["canonical_records_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="canonical"):
        CnigFeatureCodeProfile.model_validate(payload)
```

### `test_wrong_official_host_and_unknown_field_are_rejected`

**Purpose**

Exercises `wrong official host and unknown field are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _profile_payload()
payload["official_sources"]["prescription"] = "https://example.com/codes"
payload = _profile_payload()
payload["semantic_policy"] = "BLOCK"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="official|exact"):
        CnigFeatureCodeProfile.model_validate(payload)
with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Regression protected**

Locks `wrong official host and unknown field are rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
    payload = _profile_payload()
    payload["official_sources"]["prescription"] = "https://example.com/codes"
    with pytest.raises(ValueError, match="official|exact"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["semantic_policy"] = "BLOCK"
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)
```

### `test_duplicate_yaml_key_is_rejected`

**Purpose**

Exercises `duplicate yaml key is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "codes.yaml"
path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML"):
        load_cnig_feature_code_profile(path)
```

**Regression protected**

Locks `duplicate yaml key is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "codes.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML"):
        load_cnig_feature_code_profile(path)
```

### `test_wrong_planning_standard_is_rejected`

**Purpose**

Exercises `wrong planning standard is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_inputs())
inputs[0] = _planning_document("CNIG PLU v2022")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="standard"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `wrong planning standard is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_planning_standard_is_rejected() -> None:
    inputs = list(_inputs())
    inputs[0] = _planning_document("CNIG PLU v2022")
    with pytest.raises(PlanningFeatureCodeError, match="standard"):
        resolve_planning_feature_codes(*inputs)
```

### `test_catalogs_and_relations_are_preserved_and_inputs_immutable`

**Purpose**

Exercises `catalogs and relations are preserved and inputs immutable`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _inputs()
snapshots = [frame.copy(deep=True) for frame in inputs[1:5]]
result = resolve_planning_feature_codes(*inputs)
for original, snapshot, coded in zip(
        inputs[1:4],
        snapshots[:3],
        (result.surface_features, result.line_features, result.point_features),
        strict=True,
    ):
        assert_geodataframe_equal(original, snapshot)
        assert_geodataframe_equal(coded.loc[:, original.columns], original)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
pd.testing.assert_frame_equal(inputs[4], snapshots[3])
pd.testing.assert_frame_equal(result.relations.loc[:, inputs[4].columns], inputs[4])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS
assert result.relations.index.equals(inputs[4].index)
```

**Regression protected**

Locks `catalogs and relations are preserved and inputs immutable` through the exact asserted conditions: `tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS`; `result.relations.index.equals(inputs[4].index)`; `tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS):]) == OFFICIAL_CODE_COLUMNS`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
    inputs = _inputs()
    snapshots = [frame.copy(deep=True) for frame in inputs[1:5]]
    result = resolve_planning_feature_codes(*inputs)
    for original, snapshot, coded in zip(
        inputs[1:4],
        snapshots[:3],
        (result.surface_features, result.line_features, result.point_features),
        strict=True,
    ):
        assert_geodataframe_equal(original, snapshot)
        assert_geodataframe_equal(coded.loc[:, original.columns], original)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
    pd.testing.assert_frame_equal(inputs[4], snapshots[3])
    pd.testing.assert_frame_equal(result.relations.loc[:, inputs[4].columns], inputs[4])
    assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS
    assert result.relations.index.equals(inputs[4].index)
```

### `test_complete_normalized_catalog_schema_is_required`

**Purpose**

Exercises `complete normalized catalog schema is required`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `catalog_position`, `column`.

**Setup**

```python
inputs = list(_inputs())
inputs[catalog_position] = inputs[catalog_position].drop(columns=column)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
    inputs = list(_inputs())
    inputs[catalog_position] = inputs[catalog_position].drop(columns=column)
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

### `test_unexpected_factual_catalog_column_is_rejected`

**Purpose**

Exercises `unexpected factual catalog column is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_inputs())
surface = inputs[1].copy(deep=True)
surface["unexpected_fact"] = "not-produced-by-step-7d-3-1"
inputs[1] = surface
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `unexpected factual catalog column is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unexpected_factual_catalog_column_is_rejected() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface["unexpected_fact"] = "not-produced-by-step-7d-3-1"
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

### `test_cnig_identity_provenance_is_exact`

**Purpose**

Exercises `cnig identity provenance is exact`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
inputs = list(_inputs())
surface = inputs[1].copy(deep=True)
surface.loc[surface.index[0], column] = value
inputs[1] = surface
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningFeatureCodeError, match="identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `cnig identity provenance is exact`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[0], column] = value
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)
```

### `test_ogr_fid_provenance_is_restricted`

**Purpose**

Exercises `ogr fid provenance is restricted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `feature_family`, `logical_layer`, `source_feature_id`.

**Setup**

```python
inputs = list(_inputs())
surface = inputs[1].copy(deep=True)
row_index = surface.index[0]
surface.loc[row_index, "logical_layer"] = logical_layer
surface.loc[row_index, "feature_family"] = feature_family
surface.loc[row_index, "source_identity_kind"] = "ARCHIVE_SCOPED_OGR_FID"
surface.loc[row_index, "source_identity_field"] = "OGR_FID"
surface.loc[row_index, "source_feature_id"] = source_feature_id
inputs[1] = surface
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningFeatureCodeError, match="OGR|identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `ogr fid provenance is restricted`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    row_index = surface.index[0]
    surface.loc[row_index, "logical_layer"] = logical_layer
    surface.loc[row_index, "feature_family"] = feature_family
    surface.loc[row_index, "source_identity_kind"] = "ARCHIVE_SCOPED_OGR_FID"
    surface.loc[row_index, "source_identity_field"] = "OGR_FID"
    surface.loc[row_index, "source_feature_id"] = source_feature_id
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="OGR|identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)
```

### `test_source_feature_id_is_unique_inside_logical_layer`

**Purpose**

Exercises `source feature id is unique inside logical layer`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_inputs())
surface = inputs[1].copy(deep=True)
surface.loc[surface.index[1], "logical_layer"] = surface.iloc[0]["logical_layer"]
surface.loc[surface.index[1], "feature_family"] = surface.iloc[0]["feature_family"]
surface.loc[surface.index[1], "source_identity_field"] = surface.iloc[0][
        "source_identity_field"
    ]
surface.loc[surface.index[1], "source_feature_id"] = surface.iloc[0][
        "source_feature_id"
    ]
inputs[1] = surface
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="source_feature_id|unique"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `source feature id is unique inside logical layer`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_feature_id_is_unique_inside_logical_layer() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[1], "logical_layer"] = surface.iloc[0]["logical_layer"]
    surface.loc[surface.index[1], "feature_family"] = surface.iloc[0]["feature_family"]
    surface.loc[surface.index[1], "source_identity_field"] = surface.iloc[0][
        "source_identity_field"
    ]
    surface.loc[surface.index[1], "source_feature_id"] = surface.iloc[0][
        "source_feature_id"
    ]
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="source_feature_id|unique"):
        resolve_planning_feature_codes(*inputs)
```

### `test_catalog_crs_must_be_canonical_epsg_2154`

**Purpose**

Exercises `catalog crs must be canonical epsg 2154`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_inputs())
inputs[1] = inputs[1].to_crs("EPSG:4326")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="EPSG:2154|CRS"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
    inputs = list(_inputs())
    inputs[1] = inputs[1].to_crs("EPSG:4326")
    with pytest.raises(PlanningFeatureCodeError, match="EPSG:2154|CRS"):
        resolve_planning_feature_codes(*inputs)
```

### `test_catalog_geometry_metrics_are_revalidated`

**Purpose**

Exercises `catalog geometry metrics are revalidated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `catalog_position`, `column`, `value`.

**Setup**

```python
inputs = list(_inputs())
catalog = inputs[catalog_position].copy(deep=True)
catalog.loc[catalog.index[0], column] = value
inputs[catalog_position] = catalog
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="metric|area|length|member"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `catalog geometry metrics are revalidated`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    catalog = inputs[catalog_position].copy(deep=True)
    catalog.loc[catalog.index[0], column] = value
    inputs[catalog_position] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="metric|area|length|member"):
        resolve_planning_feature_codes(*inputs)
```

### `test_complete_relation_schema_is_required`

**Purpose**

Exercises `complete relation schema is required`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_inputs())
inputs[4] = inputs[4].drop(columns="intersection_length_m")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="relation|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `complete relation schema is required`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_complete_relation_schema_is_required() -> None:
    inputs = list(_inputs())
    inputs[4] = inputs[4].drop(columns="intersection_length_m")
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

### `test_unexpected_factual_relation_column_is_rejected`

**Purpose**

Exercises `unexpected factual relation column is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_inputs())
relations = inputs[4].copy(deep=True)
relations["unexpected_metric"] = 0.0
inputs[4] = relations
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="relation|schema"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `unexpected factual relation column is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unexpected_factual_relation_column_is_rejected() -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations["unexpected_metric"] = 0.0
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema"):
        resolve_planning_feature_codes(*inputs)
```

### `test_cnig_resolver_invokes_shared_factual_contract`

**Purpose**

Exercises `cnig resolver invokes shared factual contract`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
calls = 0
def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")
monkeypatch.setattr(
        coding_module,
        "validate_normalized_planning_feature_inputs",
        reject_shared_contract,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningFeatureCodeError, match="shared factual contract marker"
    ):
        resolve_planning_feature_codes(*_inputs())
assert calls == 1
```

**Regression protected**

Locks `cnig resolver invokes shared factual contract`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    calls = 0

    def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")

    monkeypatch.setattr(
        coding_module,
        "validate_normalized_planning_feature_inputs",
        reject_shared_contract,
    )
    with pytest.raises(
        PlanningFeatureCodeError, match="shared factual contract marker"
    ):
        resolve_planning_feature_codes(*_inputs())
    assert calls == 1
```

### `test_cnig_resolver_invokes_shared_factual_contract.reject_shared_contract`

**Exact signature**

```python
def reject_shared_contract(*args: object) -> None:
```

**Purpose**

Private `test` helper for reject shared contract; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `ValueError('shared factual contract marker')`.

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

- function object argument: `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_resolver_invokes_shared_factual_contract` via `monkeypatch.setattr(coding_module, 'validate_normalized_planning_feature_inputs', reject_shared_contract)`.

**Complete source-ordered implementation**

```python
def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_relation_catalog_agreement_is_required`

**Purpose**

Exercises `complete relation catalog agreement is required`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
inputs = list(_inputs())
relations = inputs[4].copy(deep=True)
relations.loc[relations.index[0], column] = value
inputs[4] = relations
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningFeatureCodeError, match="catalog|metric|normalized|feature share"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `complete relation catalog agreement is required`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="catalog|metric|normalized|feature share"
    ):
        resolve_planning_feature_codes(*inputs)
```

### `test_surface_relation_metrics_are_revalidated`

**Purpose**

Exercises `surface relation metrics are revalidated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
inputs = list(_inputs())
relations = inputs[4].copy(deep=True)
relations.loc[relations.index[0], column] = value
inputs[4] = relations
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningFeatureCodeError, match="relation|metric|finite|percentage"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `surface relation metrics are revalidated`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="relation|metric|finite|percentage"
    ):
        resolve_planning_feature_codes(*inputs)
```

### `test_line_relation_metrics_are_revalidated`

**Purpose**

Exercises `line relation metrics are revalidated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
inputs = list(_inputs())
relations = inputs[4].copy(deep=True)
line_index = relations.index[relations["geometry_kind"].eq("LINE")][0]
relations.loc[line_index, column] = value
inputs[4] = relations
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="relation|length|catalog"):
        resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Locks `line relation metrics are revalidated`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    line_index = relations.index[relations["geometry_kind"].eq("LINE")][0]
    relations.loc[line_index, column] = value
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|length|catalog"):
        resolve_planning_feature_codes(*inputs)
```

### `test_duplicate_catalog_columns_are_rejected`

**Purpose**

Exercises `duplicate catalog columns are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
duplicate = pd.concat([surface, surface[["planning_feature_id"]]], axis=1)
duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=surface.crs)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, duplicate, line, point, relations, profile
        )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_catalog_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([surface, surface[["planning_feature_id"]]], axis=1)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=surface.crs)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, duplicate, line, point, relations, profile
        )
```

### `test_missing_catalog_crs_is_rejected`

**Purpose**

Exercises `missing catalog crs is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
surface = surface.set_crs(None, allow_override=True)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.set_crs(None, allow_override=True)
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_unparseable_catalog_crs_is_rejected`

**Purpose**

Exercises `unparseable catalog crs is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
surface = surface.copy(deep=True)
surface.geometry.array._crs = "definitely-not-a-crs"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unparseable_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.geometry.array._crs = "definitely-not-a-crs"  # type: ignore[attr-defined]
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_inactive_or_wrong_geometry_column_is_rejected`

**Purpose**

Exercises `inactive or wrong geometry column is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
surface = surface.copy(deep=True)
surface["alternate_geometry"] = surface.geometry.copy()
surface = surface.set_geometry("alternate_geometry")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Locks `inactive or wrong geometry column is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface["alternate_geometry"] = surface.geometry.copy()
    surface = surface.set_geometry("alternate_geometry")
    with pytest.raises(PlanningFeatureCodeError, match="geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_surface_geometry_contract_is_enforced`

**Purpose**

Exercises `surface geometry contract is enforced`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`, `message`.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
surface = surface.copy(deep=True)
surface.at[surface.index[0], "geometry"] = geometry
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.at[surface.index[0], "geometry"] = geometry
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_valid_multi_geometries_are_accepted`

**Purpose**

Exercises `valid multi geometries are accepted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `catalog_name`, `geometry`.

**Setup**

```python
document, parcels, _, _, _, _, profile = _integration_inputs()
target_logical = {
        "surface": "prescription_surface",
        "line": "prescription_line",
        "point": "information_point",
    }[catalog_name]
changed_layers: list[GpuInspectedLayer] = []
for layer in document.related_layers:
        if layer.logical_name != target_logical:
            changed_layers.append(layer)
            continue
        source = layer.data.copy(deep=True)
        source.at[source.index[0], "geometry"] = geometry
        changed_layers.append(_integration_layer(target_logical, source))
changed_document = _planning_document(related_layers=tuple(changed_layers))
```

**Action**

```python
normalized = intersect_parcels_with_gpu_planning_features(parcels, changed_document)
result = _public_resolve_planning_feature_codes(
        changed_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
```

**Expected result**

```python
assert getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals(geometry)
```

**Regression protected**

Locks `valid multi geometries are accepted` through the exact asserted conditions: `getattr(result, f'{catalog_name}_features').geometry.iloc[0].equals(geometry)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    target_logical = {
        "surface": "prescription_surface",
        "line": "prescription_line",
        "point": "information_point",
    }[catalog_name]
    changed_layers: list[GpuInspectedLayer] = []
    for layer in document.related_layers:
        if layer.logical_name != target_logical:
            changed_layers.append(layer)
            continue
        source = layer.data.copy(deep=True)
        source.at[source.index[0], "geometry"] = geometry
        changed_layers.append(_integration_layer(target_logical, source))
    changed_document = _planning_document(related_layers=tuple(changed_layers))
    normalized = intersect_parcels_with_gpu_planning_features(parcels, changed_document)
    result = _public_resolve_planning_feature_codes(
        changed_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    assert getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals(geometry)
```

### `test_catalog_semantic_and_string_contracts_are_enforced`

**Purpose**

Exercises `catalog semantic and string contracts are enforced`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `message`, `value`.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
surface = surface.copy(deep=True)
surface.loc[surface.index[0], column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Locks `catalog semantic and string contracts are enforced`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_every_required_catalog_identity_is_an_exact_non_null_string`

**Purpose**

Exercises `every required catalog identity is an exact non null string`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
surface = surface.copy(deep=True)
relations = relations.copy(deep=True)
feature_id = surface.iloc[0]["planning_feature_id"]
surface.loc[surface.index[0], column] = " invalid "
if column in relations.columns:
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = (
            " invalid "
        )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="exact string|non-empty"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    relations = relations.copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], column] = " invalid "
    if column in relations.columns:
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = (
            " invalid "
        )
    with pytest.raises(PlanningFeatureCodeError, match="exact string|non-empty"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_line_and_point_geometry_types_are_enforced`

**Purpose**

Exercises `line and point geometry types are enforced`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `catalog_name`, `geometry`.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
catalogs = {"line": line.copy(deep=True), "point": point.copy(deep=True)}
catalog = catalogs[catalog_name]
catalog.at[catalog.index[0], "geometry"] = geometry
catalogs[catalog_name] = catalog
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="geometry|type"):
        resolve_planning_feature_codes(
            document,
            surface,
            catalogs["line"],
            catalogs["point"],
            relations,
            profile,
        )
```

**Regression protected**

Locks `line and point geometry types are enforced`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"line": line.copy(deep=True), "point": point.copy(deep=True)}
    catalog = catalogs[catalog_name]
    catalog.at[catalog.index[0], "geometry"] = geometry
    catalogs[catalog_name] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="geometry|type"):
        resolve_planning_feature_codes(
            document,
            surface,
            catalogs["line"],
            catalogs["point"],
            relations,
            profile,
        )
```

### `test_planning_feature_ids_are_globally_unique_across_catalogs`

**Purpose**

Exercises `planning feature ids are globally unique across catalogs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
line = line.copy(deep=True)
line.loc[line.index[0], "planning_feature_id"] = surface.iloc[0][
        "planning_feature_id"
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="unique|catalog|deterministic"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Locks `planning feature ids are globally unique across catalogs`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
    document, surface, line, point, relations, profile = _inputs()
    line = line.copy(deep=True)
    line.loc[line.index[0], "planning_feature_id"] = surface.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(PlanningFeatureCodeError, match="unique|catalog|deterministic"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_valid_empty_optional_catalogs_preserve_schema_and_crs`

**Purpose**

Exercises `valid empty optional catalogs preserve schema and crs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, parcels, _, _, _, _, profile = _integration_inputs()
surface_layers = tuple(
        layer
        for layer in document.related_layers
        if layer.logical_name in {"prescription_surface", "information_surface"}
    )
document = replace(document, related_layers=surface_layers)
for original, coded in (
        (normalized.line_features, result.line_features),
        (normalized.point_features, result.point_features),
    ):
        assert coded.empty
        assert coded.crs == original.crs
        assert tuple(coded.columns[: len(original.columns)]) == tuple(original.columns)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
```

**Action**

```python
normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    surface_layers = tuple(
        layer
        for layer in document.related_layers
        if layer.logical_name in {"prescription_surface", "information_surface"}
    )
    document = replace(document, related_layers=surface_layers)
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    for original, coded in (
        (normalized.line_features, result.line_features),
        (normalized.point_features, result.point_features),
    ):
        assert coded.empty
        assert coded.crs == original.crs
        assert tuple(coded.columns[: len(original.columns)]) == tuple(original.columns)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
```

### `test_relation_catalog_code_mismatch_is_rejected`

**Purpose**

Exercises `relation catalog code mismatch is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
relations = relations.copy(deep=True)
relation_index = relations.index[0]
original = relations.loc[relation_index, "subtype_code_raw"]
relations.loc[relation_index, "subtype_code_raw"] = (
        "04" if original != "04" else "00"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="catalog"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Locks `relation catalog code mismatch is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_relation_catalog_code_mismatch_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relation_index = relations.index[0]
    original = relations.loc[relation_index, "subtype_code_raw"]
    relations.loc[relation_index, "subtype_code_raw"] = (
        "04" if original != "04" else "00"
    )
    with pytest.raises(PlanningFeatureCodeError, match="catalog"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_duplicate_relation_columns_are_rejected`

**Purpose**

Exercises `duplicate relation columns are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
duplicate = pd.concat([relations, relations[["parcel_id"]]], axis=1)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, surface, line, point, duplicate, profile
        )
```

**Regression protected**

Locks `duplicate relation columns are rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_relation_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([relations, relations[["parcel_id"]]], axis=1)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, surface, line, point, duplicate, profile
        )
```

### `test_relation_identity_must_be_an_exact_non_null_string`

**Purpose**

Exercises `relation identity must be an exact non null string`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
relations = relations.copy(deep=True)
relations.loc[relations.index[0], column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="relation|exact string"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match="relation|exact string"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_duplicate_parcel_feature_relation_is_rejected`

**Purpose**

Exercises `duplicate parcel feature relation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
relations = _canonical_relation_schema(relations)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="unique|duplicate"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Locks `duplicate parcel feature relation is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_parcel_feature_relation_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
    relations = _canonical_relation_schema(relations)
    with pytest.raises(PlanningFeatureCodeError, match="unique|duplicate"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_unknown_relation_feature_id_is_rejected`

**Purpose**

Exercises `unknown relation feature id is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
relations = relations.copy(deep=True)
relations.loc[relations.index[0], "planning_feature_id"] = "UNKNOWN"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="unknown"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Regression protected**

Locks `unknown relation feature id is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "UNKNOWN"
    with pytest.raises(PlanningFeatureCodeError, match="unknown"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

### `test_relation_type_must_match_catalog_geometry_kind`

**Purpose**

Exercises `relation type must match catalog geometry kind`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry_kind`, `relation_type`.

**Setup**

```python
document, surface, line, point, relations, profile = _inputs()
catalogs = {"SURFACE": surface, "LINE": line, "POINT": point}
feature = catalogs[geometry_kind].iloc[0]
row = relations.iloc[0].copy()
for column in (
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "type_code_raw",
        "subtype_code_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "label_raw",
        "text_raw",
        "source_validity_date_raw",
        "regulation_filename_raw",
    ):
        row[column] = feature[column]
row["relation_type"] = relation_type
metric_columns = (
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    )
for column in metric_columns:
        row[column] = None
if geometry_kind == "SURFACE":
        area = 4.0 if relation_type == "AREA_OVERLAP" else 0.0
        row["feature_area_m2"] = 4.0
        row["intersection_area_m2"] = area
        row["parcel_share_pct"] = 100.0 if area else 0.0
        row["feature_share_pct"] = 100.0 if area else 0.0
    elif geometry_kind == "LINE":
        row["source_line_length_m"] = 2.0
        row["intersection_length_m"] = 2.0 if relation_type == "LENGTH_OVERLAP" else 0.0
    else:
        row["point_member_count"] = 1
        row["point_members_inside_count"] = 1 if relation_type == "INSIDE" else 0
        row["point_members_boundary_count"] = (
            1 if relation_type == "BOUNDARY_TOUCH" else 0
        )
candidate = pd.DataFrame([row], columns=relations.columns)
candidate = _canonical_relation_schema(candidate)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type|geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, candidate, profile
        )
```

**Regression protected**

Locks `relation type must match catalog geometry kind`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"SURFACE": surface, "LINE": line, "POINT": point}
    feature = catalogs[geometry_kind].iloc[0]
    row = relations.iloc[0].copy()
    for column in (
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "type_code_raw",
        "subtype_code_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "label_raw",
        "text_raw",
        "source_validity_date_raw",
        "regulation_filename_raw",
    ):
        row[column] = feature[column]
    row["relation_type"] = relation_type
    metric_columns = (
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    )
    for column in metric_columns:
        row[column] = None
    if geometry_kind == "SURFACE":
        area = 4.0 if relation_type == "AREA_OVERLAP" else 0.0
        row["feature_area_m2"] = 4.0
        row["intersection_area_m2"] = area
        row["parcel_share_pct"] = 100.0 if area else 0.0
        row["feature_share_pct"] = 100.0 if area else 0.0
    elif geometry_kind == "LINE":
        row["source_line_length_m"] = 2.0
        row["intersection_length_m"] = 2.0 if relation_type == "LENGTH_OVERLAP" else 0.0
    else:
        row["point_member_count"] = 1
        row["point_members_inside_count"] = 1 if relation_type == "INSIDE" else 0
        row["point_members_boundary_count"] = (
            1 if relation_type == "BOUNDARY_TOUCH" else 0
        )
    candidate = pd.DataFrame([row], columns=relations.columns)
    candidate = _canonical_relation_schema(candidate)
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type|geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, candidate, profile
        )
```

### `test_valid_relation_types_are_retained`

**Purpose**

Exercises `valid relation types are retained`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry_kind`, `relation_type`.

**Setup**

```python
geometry: object
if geometry_kind == "SURFACE":
        logical = "prescription_surface"
        geometry = (
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
            if relation_type == "AREA_OVERLAP"
            else Polygon([(2, 0), (4, 0), (4, 2), (2, 2)])
        )
    elif geometry_kind == "LINE":
        logical = "prescription_line"
        geometry = (
            LineString([(0, 1), (2, 1)])
            if relation_type == "LENGTH_OVERLAP"
            else LineString([(-1, 0), (0, 0)])
        )
    else:
        logical = "information_point"
        geometry = Point(1, 1) if relation_type == "INSIDE" else Point(0, 1)
source = _integration_source_frame(
        logical,
        [geometry],
        ["FEATURE-1"],
        ["07" if logical.startswith("prescription") else "99"],
        ["00"],
    )
document = _planning_document(related_layers=(_integration_layer(logical, source),))
parcels = _integration_parcels()
```

**Action**

```python
normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )
```

**Expected result**

```python
assert result.relations["relation_type"].tolist() == [relation_type]
```

**Regression protected**

Locks `valid relation types are retained` through the exact asserted conditions: `result.relations['relation_type'].tolist() == [relation_type]`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
    geometry: object
    if geometry_kind == "SURFACE":
        logical = "prescription_surface"
        geometry = (
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
            if relation_type == "AREA_OVERLAP"
            else Polygon([(2, 0), (4, 0), (4, 2), (2, 2)])
        )
    elif geometry_kind == "LINE":
        logical = "prescription_line"
        geometry = (
            LineString([(0, 1), (2, 1)])
            if relation_type == "LENGTH_OVERLAP"
            else LineString([(-1, 0), (0, 0)])
        )
    else:
        logical = "information_point"
        geometry = Point(1, 1) if relation_type == "INSIDE" else Point(0, 1)
    source = _integration_source_frame(
        logical,
        [geometry],
        ["FEATURE-1"],
        ["07" if logical.startswith("prescription") else "99"],
        ["00"],
    )
    document = _planning_document(related_layers=(_integration_layer(logical, source),))
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )
    assert result.relations["relation_type"].tolist() == [relation_type]
```

### `test_coordinated_output_hash_mutation_is_rejected`

**Purpose**

Exercises `coordinated output hash mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _inputs()
result = resolve_planning_feature_codes(*inputs)
surface = result.surface_features.copy(deep=True)
surface.loc[surface.index[0], "official_code_label"] = "Mutated"
```

**Action**

```python
mutated = _result_with_hashes(replace(result, surface_features=surface))
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="rebuilt|meaning|dictionary"):
        validate_planning_feature_code_result(*inputs, mutated)
```

**Regression protected**

Locks `coordinated output hash mutation is rejected`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_output_hash_mutation_is_rejected() -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = "Mutated"
    mutated = _result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(PlanningFeatureCodeError, match="rebuilt|meaning|dictionary"):
        validate_planning_feature_code_result(*inputs, mutated)
```

### `test_parquet_readback_passes_source_complete_validation`

**Purpose**

Exercises `parquet readback passes source complete validation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _inputs()
result = resolve_planning_feature_codes(*inputs)
paths = {
        name: tmp_path / f"{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
validate_planning_feature_code_result(*inputs, persisted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    validate_planning_feature_code_result(*inputs, persisted)
```

### `test_record_order_must_be_deterministic`

**Purpose**

Exercises `record order must be deterministic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _profile_payload()
payload["records"] = list(reversed(payload["records"]))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="deterministic order"):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Regression protected**

Locks `record order must be deterministic`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_record_order_must_be_deterministic() -> None:
    payload = _profile_payload()
    payload["records"] = list(reversed(payload["records"]))
    with pytest.raises(ValueError, match="deterministic order"):
        CnigFeatureCodeProfile.model_validate(payload)
```

### `test_yaml_snapshot_loads_strictly`

**Purpose**

Exercises `yaml snapshot loads strictly`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _profile_payload()
path = tmp_path / "profile.yaml"
path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert load_cnig_feature_code_profile(path) == _profile()
```

**Regression protected**

Locks `yaml snapshot loads strictly` through the exact asserted conditions: `load_cnig_feature_code_profile(path) == _profile()`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
    payload = _profile_payload()
    path = tmp_path / "profile.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    assert load_cnig_feature_code_profile(path) == _profile()
```

### `test_stable_public_api_is_exported_from_module_and_stage_package`

**Purpose**

Exercises `stable public api is exported from module and stage package`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
from landscout import stages
coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
required = {
        "CnigFeatureCodeProfile",
        "PlanningFeatureCodeError",
        "PlanningFeatureCodeResult",
        "load_cnig_feature_code_profile",
        "resolve_planning_feature_codes",
        "validate_planning_feature_code_result",
        "validate_planning_feature_code_result_envelope",
    }
low_level = {
        "_canonical_json_sha256",
        "_coded_catalog",
        "_lookup",
        "_profile_sha256",
        "_result_with_hashes",
    }
for name in required:
        assert getattr(stages, name) is getattr(coding_module, name)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert required.issubset(set(coding_module.__all__))
assert required.issubset(set(stages.__all__))
assert low_level.isdisjoint(coding_module.__all__)
assert low_level.isdisjoint(stages.__all__)
```

**Regression protected**

Locks `stable public api is exported from module and stage package` through the exact asserted conditions: `required.issubset(set(coding_module.__all__))`; `required.issubset(set(stages.__all__))`; `low_level.isdisjoint(coding_module.__all__)`; `low_level.isdisjoint(stages.__all__)`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
    from landscout import stages

    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )

    required = {
        "CnigFeatureCodeProfile",
        "PlanningFeatureCodeError",
        "PlanningFeatureCodeResult",
        "load_cnig_feature_code_profile",
        "resolve_planning_feature_codes",
        "validate_planning_feature_code_result",
        "validate_planning_feature_code_result_envelope",
    }
    low_level = {
        "_canonical_json_sha256",
        "_coded_catalog",
        "_lookup",
        "_profile_sha256",
        "_result_with_hashes",
    }
    assert required.issubset(set(coding_module.__all__))
    assert required.issubset(set(stages.__all__))
    for name in required:
        assert getattr(stages, name) is getattr(coding_module, name)
    assert low_level.isdisjoint(coding_module.__all__)
    assert low_level.isdisjoint(stages.__all__)
```

### `test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`

**Purpose**

Exercises `checked in official snapshot is complete for observed muret pairs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
expected_records = (
        (
            "INFORMATION",
            "02",
            "00",
            "Zone d'aménagement concerté",
            "L311-1 code de l’urbanisme",
            "R151-52 8°",
            I_URL,
        ),
        (
            "INFORMATION",
            "14",
            "00",
            "Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)",
            "L571-10 code de l’environnement",
            "R151-53 5°",
            I_URL,
        ),
        (
            "INFORMATION",
            "27",
            "00",
            "Plan d'exposition au bruit des aérodromes",
            "L112-6 code de l’urbanisme",
            "R151-52 2°",
            I_URL,
        ),
        (
            "INFORMATION",
            "99",
            "00",
            "Autre périmètre, secteur, plan, document, site, projet, espace.",
            None,
            None,
            I_URL,
        ),
        (
            "PRESCRIPTION",
            "01",
            "00",
            "Espace boisé classé",
            "L113-1",
            "R151-31 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "05",
            "00",
            "Emplacement réservé",
            "L151-41 1° à 3°",
            "R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "00",
            "Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique",
            "L151-19 et L151-23",
            "R151-41 3° Et R151-43",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "04",
            "Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique",
            "L151-23",
            "R151-43 5°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "00",
            "Règles d’implantation des constructions",
            "L151-17 et L151-18",
            "R151-39 dernier al.",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "01",
            "Implantation des constructions par rapport aux voies et aux emprises publiques",
            "L151-17 et L151-18",
            "R151-39",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "17",
            "00",
            "Secteur à programme de logements mixité sociale en zone U et AU",
            "L151-15",
            "R151-38 3°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "18",
            "00",
            "Périmètre comportant des orientations d’aménagement et de programmation (OAP)",
            "L151-6 et L151-7",
            "R151-6 à R151-8-1",
            P_URL,
        ),
    )
actual_records = tuple(
        (
            record.feature_family,
            record.type_code,
            record.subtype_code,
            record.official_label,
            record.legal_reference,
            record.regulation_or_annex_reference,
            record.official_source_url,
        )
        for record in profile.records
    )
```

**Action**

```python
profile = load_cnig_feature_code_profile(path)
```

**Expected result**

```python
assert profile.schema_version == 2
assert profile.profile == "cnig_plu_2017_muret_observed_pairs_v2"
assert profile.standard_model == "CNIG PLU v2017"
assert profile.official_text_normalization == TEXT_NORMALIZATION
assert profile.retrieval_date.isoformat() == "2026-08-12"
assert profile.official_sources.prescription == P_URL
assert profile.official_sources.information == I_URL
assert (
        profile.canonical_records_sha256
        == "5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"
    )
assert (
        _payload_hash(profile.model_dump(mode="json"))
        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    )
assert actual_records == expected_records
```

**Regression protected**

Locks `checked in official snapshot is complete for observed muret pairs` through the exact asserted conditions: `profile.schema_version == 2`; `profile.profile == 'cnig_plu_2017_muret_observed_pairs_v2'`; `profile.standard_model == 'CNIG PLU v2017'`; `profile.official_text_normalization == TEXT_NORMALIZATION`; plus 6 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
    path = Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    profile = load_cnig_feature_code_profile(path)
    expected_records = (
        (
            "INFORMATION",
            "02",
            "00",
            "Zone d'aménagement concerté",
            "L311-1 code de l’urbanisme",
            "R151-52 8°",
            I_URL,
        ),
        (
            "INFORMATION",
            "14",
            "00",
            "Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)",
            "L571-10 code de l’environnement",
            "R151-53 5°",
            I_URL,
        ),
        (
            "INFORMATION",
            "27",
            "00",
            "Plan d'exposition au bruit des aérodromes",
            "L112-6 code de l’urbanisme",
            "R151-52 2°",
            I_URL,
        ),
        (
            "INFORMATION",
            "99",
            "00",
            "Autre périmètre, secteur, plan, document, site, projet, espace.",
            None,
            None,
            I_URL,
        ),
        (
            "PRESCRIPTION",
            "01",
            "00",
            "Espace boisé classé",
            "L113-1",
            "R151-31 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "05",
            "00",
            "Emplacement réservé",
            "L151-41 1° à 3°",
            "R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "00",
            "Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique",
            "L151-19 et L151-23",
            "R151-41 3° Et R151-43",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "04",
            "Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique",
            "L151-23",
            "R151-43 5°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "00",
            "Règles d’implantation des constructions",
            "L151-17 et L151-18",
            "R151-39 dernier al.",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "01",
            "Implantation des constructions par rapport aux voies et aux emprises publiques",
            "L151-17 et L151-18",
            "R151-39",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "17",
            "00",
            "Secteur à programme de logements mixité sociale en zone U et AU",
            "L151-15",
            "R151-38 3°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "18",
            "00",
            "Périmètre comportant des orientations d’aménagement et de programmation (OAP)",
            "L151-6 et L151-7",
            "R151-6 à R151-8-1",
            P_URL,
        ),
    )
    actual_records = tuple(
        (
            record.feature_family,
            record.type_code,
            record.subtype_code,
            record.official_label,
            record.legal_reference,
            record.regulation_or_annex_reference,
            record.official_source_url,
        )
        for record in profile.records
    )
    assert profile.schema_version == 2
    assert profile.profile == "cnig_plu_2017_muret_observed_pairs_v2"
    assert profile.standard_model == "CNIG PLU v2017"
    assert profile.official_text_normalization == TEXT_NORMALIZATION
    assert profile.retrieval_date.isoformat() == "2026-08-12"
    assert profile.official_sources.prescription == P_URL
    assert profile.official_sources.information == I_URL
    assert (
        profile.canonical_records_sha256
        == "5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"
    )
    assert (
        _payload_hash(profile.model_dump(mode="json"))
        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    )
    assert actual_records == expected_records
```

### `test_result_schema_versions_are_strict`

**Purpose**

Exercises `result schema versions are strict`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
inputs = _inputs()
result = resolve_planning_feature_codes(*inputs)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="schema version"):
        validate_planning_feature_code_result(
            *inputs, replace(result, **{field: value})
        )
```

**Regression protected**

Locks `result schema versions are strict`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="schema version"):
        validate_planning_feature_code_result(
            *inputs, replace(result, **{field: value})
        )
```

### `test_step_7d_3_1_output_integrates_with_public_coding_api`

**Purpose**

Exercises `step 7d 3 1 output integrates with public coding api`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*inputs)
_public_validate_planning_feature_code_result(*inputs, result)
```

**Expected result**

```python
assert result.result_hash_schema_version == 5
assert result.profile_schema_version == 2
assert len(result.surface_features) == 2
assert len(result.line_features) == 1
assert len(result.point_features) == 1
assert len(result.relations) == 2
assert set(result.surface_features["official_code_status"]) == {"RESOLVED_OFFICIAL"}
```

**Regression protected**

Locks `step 7d 3 1 output integrates with public coding api` through the exact asserted conditions: `result.result_hash_schema_version == 5`; `result.profile_schema_version == 2`; `len(result.surface_features) == 2`; `len(result.line_features) == 1`; plus 3 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    assert result.result_hash_schema_version == 5
    assert result.profile_schema_version == 2
    assert len(result.surface_features) == 2
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1
    assert len(result.relations) == 2
    assert set(result.surface_features["official_code_status"]) == {"RESOLVED_OFFICIAL"}
    _public_validate_planning_feature_code_result(*inputs, result)
```

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats`

**Purpose**

Exercises `resolver runs heavy factual validation once and public validator repeats`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
enrich_module = importlib.import_module("landscout.stages.enrich_planning_features")
actual_physical = enrich_module.revalidate_gpu_spatial_layer_sources
actual_relations = enrich_module._build_relation_tables
calls = {"physical": 0, "relations": 0}
def counted_physical(*args: object, **kwargs: object) -> object:
        calls["physical"] += 1
        return actual_physical(*args, **kwargs)
def counted_relations(*args: object, **kwargs: object) -> object:
        calls["relations"] += 1
        return actual_relations(*args, **kwargs)
monkeypatch.setattr(
        enrich_module, "revalidate_gpu_spatial_layer_sources", counted_physical
    )
monkeypatch.setattr(enrich_module, "_build_relation_tables", counted_relations)
result = coding_module.resolve_planning_feature_codes(*inputs)
coding_module.validate_planning_feature_code_result(*inputs, result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert calls == {"physical": 1, "relations": 1}
assert calls == {"physical": 2, "relations": 2}
```

**Regression protected**

Locks `resolver runs heavy factual validation once and public validator repeats` through the exact asserted conditions: `calls == {'physical': 1, 'relations': 1}`; `calls == {'physical': 2, 'relations': 2}`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    enrich_module = importlib.import_module("landscout.stages.enrich_planning_features")
    actual_physical = enrich_module.revalidate_gpu_spatial_layer_sources
    actual_relations = enrich_module._build_relation_tables
    calls = {"physical": 0, "relations": 0}

    def counted_physical(*args: object, **kwargs: object) -> object:
        calls["physical"] += 1
        return actual_physical(*args, **kwargs)

    def counted_relations(*args: object, **kwargs: object) -> object:
        calls["relations"] += 1
        return actual_relations(*args, **kwargs)

    monkeypatch.setattr(
        enrich_module, "revalidate_gpu_spatial_layer_sources", counted_physical
    )
    monkeypatch.setattr(enrich_module, "_build_relation_tables", counted_relations)

    result = coding_module.resolve_planning_feature_codes(*inputs)
    assert calls == {"physical": 1, "relations": 1}

    coding_module.validate_planning_feature_code_result(*inputs, result)
    assert calls == {"physical": 2, "relations": 2}
```

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_physical`

**Exact signature**

```python
def counted_physical(*args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for counted physical; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
actual_physical(*args, **kwargs)
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

- function object argument: `tests/unit/test_resolve_planning_feature_codes.py::test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats` via `monkeypatch.setattr(enrich_module, 'revalidate_gpu_spatial_layer_sources', counted_physical)`.

**Complete source-ordered implementation**

```python
def counted_physical(*args: object, **kwargs: object) -> object:
        calls["physical"] += 1
        return actual_physical(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_relations`

**Exact signature**

```python
def counted_relations(*args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for counted relations; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
actual_relations(*args, **kwargs)
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

- function object argument: `tests/unit/test_resolve_planning_feature_codes.py::test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats` via `monkeypatch.setattr(enrich_module, '_build_relation_tables', counted_relations)`.

**Complete source-ordered implementation**

```python
def counted_relations(*args: object, **kwargs: object) -> object:
        calls["relations"] += 1
        return actual_relations(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coded_result_persists_all_source_input_hashes`

**Purpose**

Exercises `coded result persists all source input hashes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
for hash_field in (
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ):
        value = getattr(result, hash_field)
        assert isinstance(value, str)
        assert len(value) == 64
        int(value, 16)
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*_integration_inputs())
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `coded result persists all source input hashes` through the exact asserted conditions: `isinstance(value, str)`; `len(value) == 64`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coded_result_persists_all_source_input_hashes() -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    for hash_field in (
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ):
        value = getattr(result, hash_field)
        assert isinstance(value, str)
        assert len(value) == 64
        int(value, 16)
```

### `test_source_input_hash_mutation_is_rejected`

**Purpose**

Exercises `source input hash mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
inputs = _integration_inputs()
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="hash|rebuilt|source"):
        _public_validate_planning_feature_code_result(
            *inputs, replace(result, **{field: "f" * 64})
        )
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="hash|rebuilt|source"):
        _public_validate_planning_feature_code_result(
            *inputs, replace(result, **{field: "f" * 64})
        )
```

### `test_gpu_related_source_hash_is_deterministic_across_cache_roots`

**Purpose**

Exercises `gpu related source hash is deterministic across cache roots`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first_inputs = _integration_inputs()
first_document = first_inputs[0]
source_root = first_document.extraction.extraction_root
relocated_root = tmp_path / "relocated-extraction"
shutil.copytree(source_root, relocated_root)
def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)
reference_map = {
        reference: relocated_reference(reference)
        for reference in first_document.all_spatial_layers
    }
relocated_document = replace(
        first_document,
        extraction=replace(
            first_document.extraction,
            extraction_root=relocated_root,
        ),
        all_spatial_layers=tuple(
            reference_map[reference] for reference in first_document.all_spatial_layers
        ),
        zoning=replace(
            first_document.zoning,
            reference=reference_map[first_document.zoning.reference],
        ),
        related_layers=tuple(
            replace(layer, reference=reference_map[layer.reference])
            for layer in first_document.related_layers
        ),
    )
second_inputs = (relocated_document, *first_inputs[1:])
```

**Action**

```python
first = _public_resolve_planning_feature_codes(*first_inputs)
second = _public_resolve_planning_feature_codes(*second_inputs)
```

**Expected result**

```python
assert (
        first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256
    )
```

**Regression protected**

Locks `gpu related source hash is deterministic across cache roots` through the exact asserted conditions: `first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
    first_inputs = _integration_inputs()
    first_document = first_inputs[0]
    source_root = first_document.extraction.extraction_root
    relocated_root = tmp_path / "relocated-extraction"
    shutil.copytree(source_root, relocated_root)

    def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)

    reference_map = {
        reference: relocated_reference(reference)
        for reference in first_document.all_spatial_layers
    }
    relocated_document = replace(
        first_document,
        extraction=replace(
            first_document.extraction,
            extraction_root=relocated_root,
        ),
        all_spatial_layers=tuple(
            reference_map[reference] for reference in first_document.all_spatial_layers
        ),
        zoning=replace(
            first_document.zoning,
            reference=reference_map[first_document.zoning.reference],
        ),
        related_layers=tuple(
            replace(layer, reference=reference_map[layer.reference])
            for layer in first_document.related_layers
        ),
    )
    second_inputs = (relocated_document, *first_inputs[1:])
    first = _public_resolve_planning_feature_codes(*first_inputs)
    second = _public_resolve_planning_feature_codes(*second_inputs)
    assert (
        first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256
    )
```

### `test_gpu_related_source_hash_is_deterministic_across_cache_roots.relocated_reference`

**Exact signature**

```python
def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
```

**Purpose**

Private `test` helper for relocated reference; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuSpatialLayerReference`.
- Every observed return expression is reproduced without truncation:
```python
replace(reference, dataset_path=relocated_root / relative)
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_related_source_hash_is_deterministic_across_cache_roots` via `relocated_reference`.

**Complete source-ordered implementation**

```python
def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_binding_hashes_bind_every_component_hash`

**Purpose**

Exercises `source binding hashes bind every component hash`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
for hash_field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        assert getattr(changed, hash_field) != getattr(result, hash_field)
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*_integration_inputs())
changed = _result_with_hashes(replace(result, **{field: "f" * 64}))
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `source binding hashes bind every component hash` through the exact asserted conditions: `getattr(changed, hash_field) != getattr(result, hash_field)`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    changed = _result_with_hashes(replace(result, **{field: "f" * 64}))
    for hash_field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        assert getattr(changed, hash_field) != getattr(result, hash_field)
```

### `test_parcel_source_change_invalidates_coded_result`

**Purpose**

Exercises `parcel source change invalidates coded result`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_integration_inputs())
parcels = inputs[1].copy(deep=True)
parcels.loc[parcels.index[0], "parcel_id"] = "CHANGED-PARCEL"
inputs[1] = parcels
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="parcel|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Regression protected**

Locks `parcel source change invalidates coded result`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_parcel_source_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    parcels = inputs[1].copy(deep=True)
    parcels.loc[parcels.index[0], "parcel_id"] = "CHANGED-PARCEL"
    inputs[1] = parcels
    with pytest.raises(PlanningFeatureCodeError, match="parcel|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

### `test_gpu_document_context_change_invalidates_coded_result`

**Purpose**

Exercises `gpu document context change invalidates coded result`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_integration_inputs())
planning_document = inputs[0]
archive = planning_document.extraction.archive
changed_document = replace(archive.document, provider="Changed provider")
inputs[0] = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=changed_document),
        ),
    )
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="document|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Regression protected**

Locks `gpu document context change invalidates coded result`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_gpu_document_context_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    planning_document = inputs[0]
    archive = planning_document.extraction.archive
    changed_document = replace(archive.document, provider="Changed provider")
    inputs[0] = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=changed_document),
        ),
    )
    with pytest.raises(PlanningFeatureCodeError, match="document|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

### `test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`

**Purpose**

Exercises `normalized catalog change invalidates coded result even when coherent`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_integration_inputs())
surface = inputs[2].copy(deep=True)
relations = inputs[5].copy(deep=True)
feature_id = surface.iloc[0]["planning_feature_id"]
surface.loc[surface.index[0], "label_raw"] = "Coherently changed"
relations.loc[relations["planning_feature_id"].eq(feature_id), "label_raw"] = (
        "Coherently changed"
    )
inputs[2] = surface
inputs[5] = relations
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="normalized|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Regression protected**

Locks `normalized catalog change invalidates coded result even when coherent`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    surface = inputs[2].copy(deep=True)
    relations = inputs[5].copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], "label_raw"] = "Coherently changed"
    relations.loc[relations["planning_feature_id"].eq(feature_id), "label_raw"] = (
        "Coherently changed"
    )
    inputs[2] = surface
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="normalized|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

### `test_normalized_relation_change_invalidates_coded_result`

**Purpose**

Exercises `normalized relation change invalidates coded result`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = list(_integration_inputs())
relations = inputs[5].copy(deep=True)
line_mask = relations["geometry_kind"].eq("LINE")
relations.loc[line_mask, "parcel_metric_area_m2"] = 8.0
inputs[5] = relations
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Regression protected**

Locks `normalized relation change invalidates coded result`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_normalized_relation_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    relations = inputs[5].copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "parcel_metric_area_m2"] = 8.0
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

### `test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`

**Purpose**

Exercises `coding api rejects relation set not rebuilt from geometry`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
inputs = list(_integration_inputs())
relations = inputs[5].copy(deep=True)
if mutation == "missing":
        relations = relations.iloc[1:].copy()
    elif mutation == "extra":
        extra = relations.iloc[[0]].copy(deep=True)
        extra.loc[extra.index[0], "parcel_id"] = "PARCEL-OTHER"
        relations = pd.concat([relations, extra], ignore_index=True)
    elif mutation == "reordered":
        relations = relations.iloc[::-1].reset_index(drop=True)
    else:
        line_mask = relations["geometry_kind"].eq("LINE")
        relations.loc[line_mask, "intersection_length_m"] = 1.0
inputs[5] = relations
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningFeatureCodeError,
        match="relation|parcel|source|rebuilt|normalized",
    ):
        _public_resolve_planning_feature_codes(*inputs)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
    inputs = list(_integration_inputs())
    relations = inputs[5].copy(deep=True)
    if mutation == "missing":
        relations = relations.iloc[1:].copy()
    elif mutation == "extra":
        extra = relations.iloc[[0]].copy(deep=True)
        extra.loc[extra.index[0], "parcel_id"] = "PARCEL-OTHER"
        relations = pd.concat([relations, extra], ignore_index=True)
    elif mutation == "reordered":
        relations = relations.iloc[::-1].reset_index(drop=True)
    else:
        line_mask = relations["geometry_kind"].eq("LINE")
        relations.loc[line_mask, "intersection_length_m"] = 1.0
    inputs[5] = relations
    with pytest.raises(
        PlanningFeatureCodeError,
        match="relation|parcel|source|rebuilt|normalized",
    ):
        _public_resolve_planning_feature_codes(*inputs)
```

### `test_schema_v5_parquet_readback_preserves_source_hash_envelope`

**Purpose**

Exercises `schema v5 parquet readback preserves source hash envelope`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
paths = {
        name: tmp_path / f"integrated-{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
```

**Action**

```python
result = _public_resolve_planning_feature_codes(*inputs)
_public_validate_planning_feature_code_result(*inputs, persisted)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `schema v5 parquet readback preserves source hash envelope` by requiring the reproduced call path `_integration_inputs`, `_public_resolve_planning_feature_codes`, `paths.items`, `replace` without an unasserted exception.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_schema_v5_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"integrated-{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    _public_validate_planning_feature_code_result(*inputs, persisted)
```

### `test_schema_v5_public_api_signatures_remain_source_complete`

**Purpose**

Exercises `schema v5 public api signatures remain source complete`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(
        inspect.signature(_public_resolve_planning_feature_codes).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
    )
assert tuple(
        inspect.signature(_public_validate_planning_feature_code_result).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
        "result",
    )
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_public_api_signatures_remain_source_complete() -> None:
    assert tuple(
        inspect.signature(_public_resolve_planning_feature_codes).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
    )
    assert tuple(
        inspect.signature(_public_validate_planning_feature_code_result).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
        "result",
    )
```

### `test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`

**Purpose**

Exercises `step 7d 5b 2b 5 exposes lightweight coded result validator`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
inputs = _inputs()
result = resolve_planning_feature_codes(*inputs)
module.validate_planning_feature_code_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert hasattr(module, "validate_planning_feature_code_result_envelope")
with pytest.raises(PlanningFeatureCodeError, match="hash|invalid"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )
```

**Regression protected**

Locks `step 7d 5b 2b 5 exposes lightweight coded result validator`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    assert hasattr(module, "validate_planning_feature_code_result_envelope")
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    module.validate_planning_feature_code_result_envelope(result)
    with pytest.raises(PlanningFeatureCodeError, match="hash|invalid"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )
```

### `_schema_v5_envelope_result`

**Exact signature**

```python
def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
```

**Purpose**

Private `test` helper for schema v5 envelope result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningFeatureCodeResult`.
- Every observed return expression is reproduced without truncation:
```python
resolve_planning_feature_codes(*_inputs())
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

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_controls_malformed_dictionary_type` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_geospatial_code_dictionary` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_schema_is_explicit` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `_schema_v5_envelope_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result` via `_schema_v5_envelope_result`.

**Complete source-ordered implementation**

```python
def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
    return resolve_planning_feature_codes(*_inputs())
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_canonical_empty_coded_result`

**Exact signature**

```python
def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
```

**Purpose**

Private `test` helper for canonical empty coded result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningFeatureCodeResult`.
- Every observed return expression is reproduced without truncation:
```python
_result_with_hashes(replace(result, code_dictionary=dictionary, relations=relations, **catalogs))
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
- In-memory mutation: `catalogs[field]`, `dictionary.index`, `output.index`, `output[column]`, `relations.index`, `relations[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `_canonical_empty_coded_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs` via `_canonical_empty_coded_result`.

**Complete source-ordered implementation**

```python
def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
    catalogs: dict[str, gpd.GeoDataFrame] = {}
    for field, kind in (
        ("surface_features", "SURFACE"),
        ("line_features", "LINE"),
        ("point_features", "POINT"),
    ):
        output = getattr(result, field).iloc[0:0].copy(deep=True)
        for column, dtype in zip(output.columns, feature_dtypes(kind), strict=True):
            if dtype != "geometry":
                output[column] = pd.Series(index=output.index, dtype=dtype)
        output.index = pd.Index([], dtype="int64")
        catalogs[field] = output
    relations = result.relations.iloc[0:0].copy(deep=True)
    for column, dtype in zip(relations.columns, relation_dtypes(), strict=True):
        relations[column] = pd.Series(index=relations.index, dtype=dtype)
    relations.index = pd.Index([], dtype="int64")
    dictionary = result.code_dictionary.copy(deep=True)
    if empty_dictionary:
        dictionary = dictionary.iloc[0:0].copy(deep=True)
        dictionary.index = pd.Index([], dtype="int64")
    return _result_with_hashes(
        replace(
            result,
            code_dictionary=dictionary,
            relations=relations,
            **catalogs,
        )
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`

**Purpose**

Exercises `schema v5 envelope rejects canonical empty code dictionary`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=True
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="dictionary|empty|record"):
        module.validate_planning_feature_code_result_envelope(result)
```

**Regression protected**

Locks `schema v5 envelope rejects canonical empty code dictionary`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_envelope_rejects_canonical_empty_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=True
    )
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|empty|record"):
        module.validate_planning_feature_code_result_envelope(result)
```

### `test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`

**Purpose**

Exercises `schema v5 envelope accepts nonempty dictionary with empty outputs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=False
    )
module.validate_planning_feature_code_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.code_dictionary) >= 1
assert (
        sum(
            len(frame)
            for frame in (
                result.surface_features,
                result.line_features,
                result.point_features,
                result.relations,
            )
        )
        == 0
    )
```

**Regression protected**

Locks `schema v5 envelope accepts nonempty dictionary with empty outputs` through the exact asserted conditions: `len(result.code_dictionary) >= 1`; `sum((len(frame) for frame in (result.surface_features, result.line_features, result.point_features, result.relations))) == 0`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=False
    )
    assert len(result.code_dictionary) >= 1
    assert (
        sum(
            len(frame)
            for frame in (
                result.surface_features,
                result.line_features,
                result.point_features,
                result.relations,
            )
        )
        == 0
    )
    module.validate_planning_feature_code_result_envelope(result)
```

### `test_schema_v5_envelope_controls_malformed_dictionary_type`

**Purpose**

Exercises `schema v5 envelope controls malformed dictionary type`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `dictionary`.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _schema_v5_envelope_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )
```

**Regression protected**

Locks `schema v5 envelope controls malformed dictionary type`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_envelope_controls_malformed_dictionary_type(
    dictionary: object,
) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    with pytest.raises(PlanningFeatureCodeError):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )
```

### `test_schema_v5_envelope_rejects_geospatial_code_dictionary`

**Purpose**

Exercises `schema v5 envelope rejects geospatial code dictionary`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _schema_v5_envelope_result()
dictionary = gpd.GeoDataFrame(result.code_dictionary.copy(deep=True))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="dictionary|DataFrame"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )
```

**Regression protected**

Locks `schema v5 envelope rejects geospatial code dictionary`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_schema_v5_envelope_rejects_geospatial_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = gpd.GeoDataFrame(result.code_dictionary.copy(deep=True))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|DataFrame"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )
```

### `test_schema_v5_dictionary_schema_is_explicit`

**Purpose**

Exercises `schema v5 dictionary schema is explicit`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _schema_v5_envelope_result()
dictionary = result.code_dictionary.copy(deep=True)
if mutation == "dtype":
        dictionary["official_label"] = dictionary["official_label"].astype("category")
    elif mutation == "range-index":
        dictionary.index = pd.RangeIndex(len(dictionary))
    elif mutation == "index-name":
        dictionary.index = dictionary.index.rename("changed")
    else:
        dictionary.index = pd.Index(dictionary.index.to_numpy(), dtype="uint64")
```

**Action**

```python
changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="dictionary|schema|dtype|index"):
        module.validate_planning_feature_code_result_envelope(changed)
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_dictionary_schema_is_explicit(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "dtype":
        dictionary["official_label"] = dictionary["official_label"].astype("category")
    elif mutation == "range-index":
        dictionary.index = pd.RangeIndex(len(dictionary))
    elif mutation == "index-name":
        dictionary.index = dictionary.index.rename("changed")
    else:
        dictionary.index = pd.Index(dictionary.index.to_numpy(), dtype="uint64")
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|schema|dtype|index"):
        module.validate_planning_feature_code_result_envelope(changed)
```

### `test_schema_v5_dictionary_rows_are_intrinsically_validated`

**Purpose**

Exercises `schema v5 dictionary rows are intrinsically validated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _schema_v5_envelope_result()
dictionary = result.code_dictionary.copy(deep=True)
if mutation == "duplicate-pair":
        dictionary.loc[
            dictionary.index[1], ["feature_family", "type_code", "subtype_code"]
        ] = dictionary.loc[
            dictionary.index[0], ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "unsorted-pairs":
        dictionary = dictionary.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-type":
        dictionary.loc[dictionary.index[0], "type_code"] = "1"
    elif mutation == "malformed-subtype":
        dictionary.loc[dictionary.index[0], "subtype_code"] = "000"
    elif mutation == "wrong-family":
        dictionary.loc[dictionary.index[0], "feature_family"] = "ZONING"
    elif mutation == "wrong-url":
        dictionary.loc[dictionary.index[0], "official_source_url"] = (
            "https://example.com/codes"
        )
    elif mutation == "wrong-profile":
        dictionary.loc[dictionary.index[0], "profile"] = "other-profile"
    elif mutation == "wrong-profile-sha":
        dictionary.loc[dictionary.index[0], "profile_sha256"] = "a" * 64
    else:
        dictionary.loc[dictionary.index[0], "legal_reference"] = "None"
```

**Action**

```python
changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
```

**Expected result**

```python
with pytest.raises(
        PlanningFeatureCodeError, match="dictionary|pair|code|family|URL|profile|order"
    ):
        module.validate_planning_feature_code_result_envelope(changed)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_dictionary_rows_are_intrinsically_validated(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "duplicate-pair":
        dictionary.loc[
            dictionary.index[1], ["feature_family", "type_code", "subtype_code"]
        ] = dictionary.loc[
            dictionary.index[0], ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "unsorted-pairs":
        dictionary = dictionary.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-type":
        dictionary.loc[dictionary.index[0], "type_code"] = "1"
    elif mutation == "malformed-subtype":
        dictionary.loc[dictionary.index[0], "subtype_code"] = "000"
    elif mutation == "wrong-family":
        dictionary.loc[dictionary.index[0], "feature_family"] = "ZONING"
    elif mutation == "wrong-url":
        dictionary.loc[dictionary.index[0], "official_source_url"] = (
            "https://example.com/codes"
        )
    elif mutation == "wrong-profile":
        dictionary.loc[dictionary.index[0], "profile"] = "other-profile"
    elif mutation == "wrong-profile-sha":
        dictionary.loc[dictionary.index[0], "profile_sha256"] = "a" * 64
    else:
        dictionary.loc[dictionary.index[0], "legal_reference"] = "None"
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(
        PlanningFeatureCodeError, match="dictionary|pair|code|family|URL|profile|order"
    ):
        module.validate_planning_feature_code_result_envelope(changed)
```

### `test_schema_v5_scalar_lineage_contracts_are_intrinsic`

**Purpose**

Exercises `schema v5 scalar lineage contracts are intrinsic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _schema_v5_envelope_result()
```

**Action**

```python
changed_standard = _result_with_hashes(
        replace(result, standard_model="CNIG PLU v2099")
    )
malformed_sha = _result_with_hashes(
        replace(result, planning_document_context_sha256="not-a-sha")
    )
```

**Expected result**

```python
for changed in (changed_standard, malformed_sha):
        with pytest.raises(PlanningFeatureCodeError, match="standard|SHA|sha|lineage"):
            module.validate_planning_feature_code_result_envelope(changed)
```

**Regression protected**

Locks `schema v5 scalar lineage contracts are intrinsic`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_scalar_lineage_contracts_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    changed_standard = _result_with_hashes(
        replace(result, standard_model="CNIG PLU v2099")
    )
    malformed_sha = _result_with_hashes(
        replace(result, planning_document_context_sha256="not-a-sha")
    )
    for changed in (changed_standard, malformed_sha):
        with pytest.raises(PlanningFeatureCodeError, match="standard|SHA|sha|lineage"):
            module.validate_planning_feature_code_result_envelope(changed)
```

### `test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`

**Purpose**

Exercises `schema v5 official rows and relation feature agreement are intrinsic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _schema_v5_envelope_result()
surface = result.surface_features.copy(deep=True)
surface.loc[surface.index[0], "official_code_label"] = pd.NA
surface = result.surface_features.copy(deep=True)
surface.loc[surface.index[0], "official_code_status"] = "UNKNOWN_CODE_PAIR"
relations = result.relations.copy(deep=True)
relations.loc[relations.index[0], "official_code_label"] = "Other official meaning"
```

**Action**

```python
missing_meaning = _result_with_hashes(replace(result, surface_features=surface))
invented_unknown = _result_with_hashes(replace(result, surface_features=surface))
mismatched_relation = _result_with_hashes(replace(result, relations=relations))
```

**Expected result**

```python
for changed in (missing_meaning, invented_unknown, mismatched_relation):
        with pytest.raises(
            PlanningFeatureCodeError,
            match="official|meaning|UNKNOWN|relation|feature",
        ):
            module.validate_planning_feature_code_result_envelope(changed)
```

**Regression protected**

Locks `schema v5 official rows and relation feature agreement are intrinsic`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = pd.NA
    missing_meaning = _result_with_hashes(replace(result, surface_features=surface))

    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_status"] = "UNKNOWN_CODE_PAIR"
    invented_unknown = _result_with_hashes(replace(result, surface_features=surface))

    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "official_code_label"] = "Other official meaning"
    mismatched_relation = _result_with_hashes(replace(result, relations=relations))

    for changed in (missing_meaning, invented_unknown, mismatched_relation):
        with pytest.raises(
            PlanningFeatureCodeError,
            match="official|meaning|UNKNOWN|relation|feature",
        ):
            module.validate_planning_feature_code_result_envelope(changed)
```

### `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result`

**Purpose**

Exercises `schema v5 envelope requires exact result type and accepts valid result`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
result = _schema_v5_envelope_result()
class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
        pass
derived = DerivedPlanningFeatureCodeResult(**result.__dict__)
module.validate_planning_feature_code_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningFeatureCodeError, match="type|result"):
        module.validate_planning_feature_code_result_envelope(derived)
```

**Regression protected**

Locks `schema v5 envelope requires exact result type and accepts valid result`: the reproduced adversarial input must raise `PlanningFeatureCodeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result() -> (
    None
):
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()

    class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
        pass

    derived = DerivedPlanningFeatureCodeResult(**result.__dict__)
    with pytest.raises(PlanningFeatureCodeError, match="type|result"):
        module.validate_planning_feature_code_result_envelope(derived)
    module.validate_planning_feature_code_result_envelope(result)
```


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

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

The module contributes to the test flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
