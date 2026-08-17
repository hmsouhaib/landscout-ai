# `tests/unit/test_index_planning_regulation.py`

## File identity

- Repository path: `tests/unit/test_index_planning_regulation.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.
- Source SHA256: `ccf022c4ba939e973768b63120307ae83ff402b41bc6091a013a2c0b7fe0012d`

## 1. Purpose

Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError, replace`
- `from hashlib import sha256`
- `from importlib import import_module`
- `from pathlib import Path`
- `from re import fullmatch`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.common.planning_text import (
    normalize_planning_search_text as _normalize_search_text,
)`
- `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`
- `from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`

## 4. Contract taxonomy

### A. Python constants

#### `DOCUMENT_ID`

```python
DOCUMENT_ID = "doc-1"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_index_planning_regulation.py::_summary` (value reference), `tests/unit/test_index_planning_regulation.py::_document` (value reference).

#### `ARCHIVE_SHA`

```python
ARCHIVE_SHA = "a" * 64
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract. Consumers include `tests/unit/test_index_planning_regulation.py::_summary` (value reference), `tests/unit/test_index_planning_regulation.py::_document` (value reference).

#### `DEFAULT_PDF`

```python
DEFAULT_PDF = "31395_reglement_20240215.pdf"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_index_planning_regulation.py::_zone_frame` (value reference), `tests/unit/test_index_planning_regulation.py::test_unchanged_zoning_source_is_revalidated_before_selection` (value reference), `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_zoning_geometry_or_order_is_rejected` (value reference), `tests/unit/test_index_planning_regulation.py::test_unrelated_non_pdf_written_file_does_not_block_selection` (value reference), `tests/unit/test_index_planning_regulation.py::test_duplicate_inventory_basename_fails` (value reference), `tests/unit/test_index_planning_regulation.py::test_path_outside_root_is_rejected` (value reference).

#### `PDF_BYTES`

```python
PDF_BYTES = b"synthetic-pdf-bytes"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_index_planning_regulation.py::_fixture_document` (value reference), `tests/unit/test_index_planning_regulation.py::test_pdf_inventory_integrity_mismatch_fails` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `_FakePage`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `result` | `self.result = result  # assigned in __init__` | Deterministic test-double state `result` used by the reproduced network/source regression harness. |

**Interface consumers**

- constructor call: `tests/unit/test_index_planning_regulation.py::_FakeReader.__init__` via `_FakePage`.

**Exact class source**

```python
class _FakePage:
    def __init__(self, result: object) -> None:
        self.result = result

    def extract_text(self) -> object:
        if isinstance(self.result, Exception):
            raise self.result
        return self.result
```

### `_FakeReader`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `pages` | `self.pages = [_FakePage(page) for page in pages]  # assigned in __init__` | Deterministically ordered regulation PDF page records. |
| `is_encrypted` | `self.is_encrypted = encrypted  # assigned in __init__` | Deterministic test-double state `is_encrypted` used by the reproduced network/source regression harness. |

**Interface consumers**

- constructor call: `tests/unit/test_index_planning_regulation.py::_patch_reader` via `_FakeReader`.

**Exact class source**

```python
class _FakeReader:
    def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
        self.pages = [_FakePage(page) for page in pages]
        self.is_encrypted = encrypted
```


## 6. Functions and methods

### `_FakePage.__init__`

**Exact signature**

```python
def __init__(self, result: object) -> None:
```

**Purpose**

Private `test` helper for init; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self.result`.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __init__(self, result: object) -> None:
        self.result = result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakePage.extract_text`

**Exact signature**

```python
def extract_text(self) -> object:
```

**Purpose**

Validates and extracts text; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
self.result
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(self.result, Exception)`.
- Explicit raise expressions: `self.result`.

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
def extract_text(self) -> object:
        if isinstance(self.result, Exception):
            raise self.result
        return self.result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeReader.__init__`

**Exact signature**

```python
def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
```

**Purpose**

Private `test` helper for init; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self.is_encrypted`, `self.pages`.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
        self.pages = [_FakePage(page) for page in pages]
        self.is_encrypted = encrypted
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_patch_reader`

**Exact signature**

```python
def _patch_reader(
    monkeypatch: pytest.MonkeyPatch,
    pages: list[object],
    *,
    encrypted: bool = False,
) -> None:
```

**Purpose**

Private `test` helper for patch reader; its complete implementation below is the authoritative behavioral contract.

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

- direct call: `tests/unit/test_index_planning_regulation.py::_one_page_index` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_source_nomfic_resolves_generic_filename` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_explicit_source_validated_selection_succeeds` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unchanged_zoning_source_is_revalidated_before_selection` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unrelated_non_pdf_written_file_does_not_block_selection` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zero_page_pdf_is_rejected` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail` via `_patch_reader`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs` via `_patch_reader`.

**Complete source-ordered implementation**

```python
def _patch_reader(
    monkeypatch: pytest.MonkeyPatch,
    pages: list[object],
    *,
    encrypted: bool = False,
) -> None:
    monkeypatch.setattr(
        regulation_module,
        "PdfReader",
        lambda *args, **kwargs: _FakeReader(pages, encrypted=encrypted),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_summary`

**Exact signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    source_layer: str = "ZONE",
) -> GpuLayerSummary:
```

**Purpose**

Private `test` helper for summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
GpuLayerSummary(source_document_id=DOCUMENT_ID, source_archive_sha256=ARCHIVE_SHA, source_layer=source_layer, crs='EPSG:2154', feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna().sum())) for column in frame.columns)), geometry_types=tuple(((str(key), int(value)) for key, value in geometry.geom_type.value_counts().sort_index().items())), null_geometry_count=int((~non_null).sum()), empty_geometry_count=int((non_null & geometry.is_empty).sum()), invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `geometry.geom_type.value_counts`, `geometry.geom_type.value_counts().sort_index`, `geometry.geom_type.value_counts().sort_index().items`, `geometry.notna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_index_planning_regulation.py::_write_zoning_source` via `_summary`.

**Complete source-ordered implementation**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    source_layer: str = "ZONE",
) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = geometry.notna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id=DOCUMENT_ID,
        source_archive_sha256=ARCHIVE_SHA,
        source_layer=source_layer,
        crs="EPSG:2154",
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in frame.dtypes.items()),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(key), int(value))
            for key, value in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zone_frame`

**Exact signature**

```python
def _zone_frame(
    nomfic: list[object] | None = None,
    *,
    include_nomfic: bool = True,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for zone frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame(attributes, geometry=[Polygon([(index, 0), (index, 1), (index + 1, 1), (index + 1, 0), (index, 0)]) for index in range(count)], crs='EPSG:2154')
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
- In-memory mutation: `attributes['NOMFIC']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_index_planning_regulation.py::_fixture_document` via `_zone_frame`.

**Complete source-ordered implementation**

```python
def _zone_frame(
    nomfic: list[object] | None = None,
    *,
    include_nomfic: bool = True,
) -> gpd.GeoDataFrame:
    filenames = [DEFAULT_PDF] if nomfic is None else nomfic
    count = len(filenames)
    attributes: dict[str, list[object]] = {
        "LIB_IDZONE": [f"ZONE-{index + 1}" for index in range(count)]
    }
    if include_nomfic:
        attributes["NOMFIC"] = filenames
    return gpd.GeoDataFrame(
        attributes,
        geometry=[
            Polygon(
                [
                    (index, 0),
                    (index, 1),
                    (index + 1, 1),
                    (index + 1, 0),
                    (index, 0),
                ]
            )
            for index in range(count)
        ],
        crs="EPSG:2154",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_inventory_item`

**Exact signature**

```python
def _inventory_item(relative_path: str, data: bytes = PDF_BYTES) -> GpuExtractedFile:
```

**Purpose**

Private `test` helper for inventory item; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuExtractedFile`.
- Every observed return expression is reproduced without truncation:
```python
GpuExtractedFile(relative_path=relative_path, file_type='pdf', size_bytes=len(data), sha256=sha256(data).hexdigest(), category='WRITTEN_REGULATION')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(data).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_index_planning_regulation.py::_fixture_document` via `_inventory_item`.

**Complete source-ordered implementation**

```python
def _inventory_item(relative_path: str, data: bytes = PDF_BYTES) -> GpuExtractedFile:
    return GpuExtractedFile(
        relative_path=relative_path,
        file_type="pdf",
        size_bytes=len(data),
        sha256=sha256(data).hexdigest(),
        category="WRITTEN_REGULATION",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_spatial_inventory_item`

**Exact signature**

```python
def _spatial_inventory_item(root: Path, path: Path) -> GpuExtractedFile:
```

**Purpose**

Private `test` helper for spatial inventory item; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuExtractedFile`.
- Every observed return expression is reproduced without truncation:
```python
GpuExtractedFile(relative_path=path.relative_to(root).as_posix(), file_type=path.suffix.lower().lstrip('.') or 'binary', size_bytes=len(data), sha256=sha256(data).hexdigest(), category='SPATIAL_DATA')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.read_bytes`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(data).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_index_planning_regulation.py::_write_zoning_source` via `_spatial_inventory_item`.

**Complete source-ordered implementation**

```python
def _spatial_inventory_item(root: Path, path: Path) -> GpuExtractedFile:
    data = path.read_bytes()
    return GpuExtractedFile(
        relative_path=path.relative_to(root).as_posix(),
        file_type=path.suffix.lower().lstrip(".") or "binary",
        size_bytes=len(data),
        sha256=sha256(data).hexdigest(),
        category="SPATIAL_DATA",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_zoning_source`

**Exact signature**

```python
def _write_zoning_source(
    root: Path,
    frame: gpd.GeoDataFrame,
    *,
    source_format: str,
) -> tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]:
```

**Purpose**

Serializes zoning source; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(layer, inventory)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError(f'Unsupported test source format: {source_format}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `candidate.is_file`, `gpd.read_file`.
- Filesystem write: `frame.to_file`, `spatial_root.mkdir`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_index_planning_regulation.py::_fixture_document` via `_write_zoning_source`.

**Complete source-ordered implementation**

```python
def _write_zoning_source(
    root: Path,
    frame: gpd.GeoDataFrame,
    *,
    source_format: str,
) -> tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]:
    spatial_root = root / "spatial"
    spatial_root.mkdir(parents=True, exist_ok=True)
    if source_format == "GPKG":
        path = spatial_root / "zone.gpkg"
        source_layer = "ZONE"
        frame.to_file(path, layer=source_layer, driver="GPKG", engine="pyogrio")
        source_paths = (path,)
        loaded = gpd.read_file(path, layer=source_layer, engine="pyogrio")
        driver = "GPKG"
    elif source_format == "ESRI Shapefile":
        path = spatial_root / "ZONE.shp"
        source_layer = path.stem
        frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio")
        source_paths = tuple(
            candidate
            for candidate in sorted(path.parent.glob(f"{path.stem}.*"))
            if candidate.is_file()
        )
        loaded = gpd.read_file(path, engine="pyogrio")
        driver = "ESRI Shapefile"
    else:  # pragma: no cover - fixture misuse
        raise AssertionError(f"Unsupported test source format: {source_format}")
    reference = GpuSpatialLayerReference(path, source_layer, driver)
    layer = GpuInspectedLayer(
        "zoning",
        reference,
        loaded,
        _summary(loaded, source_layer=source_layer),
    )
    inventory = tuple(_spatial_inventory_item(root, item) for item in source_paths)
    return layer, inventory
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_document`

**Exact signature**

```python
def _document(
    root: Path,
    inventory: tuple[GpuExtractedFile, ...],
    zoning: GpuInspectedLayer,
    *,
    zoning_filenames: list[object] | None = None,
    written_filenames: tuple[str, ...] = (DEFAULT_PDF,),
) -> GpuPlanningDocument:
```

**Purpose**

Private `test` helper for document; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuPlanningDocument`.
- Every observed return expression is reproduced without truncation:
```python
GpuPlanningDocument(extraction=extraction, all_spatial_layers=(zoning.reference,), zoning=zoning, related_layers=())
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `marker.write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_index_planning_regulation.py::_fixture_document` via `_document`.

**Complete source-ordered implementation**

```python
def _document(
    root: Path,
    inventory: tuple[GpuExtractedFile, ...],
    zoning: GpuInspectedLayer,
    *,
    zoning_filenames: list[object] | None = None,
    written_filenames: tuple[str, ...] = (DEFAULT_PDF,),
) -> GpuPlanningDocument:
    inventory = tuple(sorted(inventory, key=lambda item: item.relative_path))
    written = tuple(
        GpuWrittenFile(filename=value, title=None, document_path=None, source_url=None)
        for value in written_filenames
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="GPU",
        commune_code="31395",
        partition="DU_31395",
        document_id=DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Planning document",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name="31395_PLU_20240215",
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model="CNIG PLU v2017",
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=written,
    )
    archive = GpuArchiveDownload(
        document=metadata,
        download_timestamp="2026-08-12T12:00:00+00:00",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=100,
        sha256=ARCHIVE_SHA,
        path=root.parent / "source.zip",
        cache_hit=True,
    )
    marker = root / ".landscout-gpu-extraction.json"
    marker.write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": archive.sha256,
                "files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in inventory
                ],
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=root,
        files=inventory,
        standard_models=("CNIG PLU v2017",),
        cache_hit=True,
    )
    return GpuPlanningDocument(
        extraction=extraction,
        all_spatial_layers=(zoning.reference,),
        zoning=zoning,
        related_layers=(),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_fixture_document`

**Exact signature**

```python
def _fixture_document(
    tmp_path: Path,
    *,
    filename: str = DEFAULT_PDF,
    zoning_filenames: list[object] | None = None,
    written_filenames: tuple[str, ...] | None = None,
    inventory_filenames: tuple[str, ...] | None = None,
    source_format: str = "GPKG",
    include_nomfic: bool = True,
) -> GpuPlanningDocument:
```

**Purpose**

Private `test` helper for fixture document; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuPlanningDocument`.
- Every observed return expression is reproduced without truncation:
```python
_document(root, tuple(inventory), zoning, zoning_filenames=zoning_filenames or [filename], written_filenames=(filename,) if written_filenames is None else written_filenames)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.parent.mkdir`, `path.write_bytes`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `inventory`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_index_planning_regulation.py::_one_page_index` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_source_nomfic_resolves_generic_filename` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_explicit_source_validated_selection_succeeds` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unchanged_zoning_source_is_revalidated_before_selection` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_nomfic_is_rejected_before_selection` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_missing_nomfic_field_is_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_null_nomfic_is_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_multiple_nomfic_values_are_ambiguous` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unsafe_explicit_filename_is_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_explicit_filename_not_referenced_by_zoning_fails` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_written_files_fails` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unrelated_non_pdf_written_file_does_not_block_selection` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_inventory_fails` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_duplicate_inventory_basename_fails` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_path_outside_root_is_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_pdf_inventory_integrity_mismatch_fails` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zero_page_pdf_is_rejected` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_pdf_reader_failure_is_controlled_and_chained` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_source_metadata_raises_controlled_index_error` via `_fixture_document`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs` via `_fixture_document`.

**Complete source-ordered implementation**

```python
def _fixture_document(
    tmp_path: Path,
    *,
    filename: str = DEFAULT_PDF,
    zoning_filenames: list[object] | None = None,
    written_filenames: tuple[str, ...] | None = None,
    inventory_filenames: tuple[str, ...] | None = None,
    source_format: str = "GPKG",
    include_nomfic: bool = True,
) -> GpuPlanningDocument:
    root = tmp_path / "extraction"
    inventory_names = (filename,) if inventory_filenames is None else inventory_filenames
    inventory: list[GpuExtractedFile] = []
    for index, name in enumerate(inventory_names):
        relative = f"written-{index}/{name}"
        path = root.joinpath(*relative.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(PDF_BYTES)
        inventory.append(_inventory_item(relative))
    zoning, spatial_inventory = _write_zoning_source(
        root,
        _zone_frame(
            [filename] if zoning_filenames is None else zoning_filenames,
            include_nomfic=include_nomfic,
        ),
        source_format=source_format,
    )
    inventory.extend(spatial_inventory)
    return _document(
        root,
        tuple(inventory),
        zoning,
        zoning_filenames=zoning_filenames or [filename],
        written_filenames=(filename,) if written_filenames is None else written_filenames,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_one_page_index`

**Exact signature**

```python
def _one_page_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str = "Énergie",
):
```

**Purpose**

Private `test` helper for one page index; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
index_planning_regulation(document)
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

- direct call: `tests/unit/test_index_planning_regulation.py::test_raw_context_preserves_source_typography` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_zero_context_preserves_complete_raw_unicode_span` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_literal_search_does_not_add_semantic_synonyms` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_coordinated_page_mutation_fails_envelope_hash` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_complete_index_envelope_mutation_is_rejected` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::_valid_search_result` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_invalid_search_term_is_rejected` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_duplicate_normalized_search_terms_are_rejected` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_empty_search_result_has_stable_schema_and_lineage` via `_one_page_index`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_page_value_raises_controlled_index_error` via `_one_page_index`.

**Complete source-ordered implementation**

```python
def _one_page_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str = "Énergie",
):
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [text])
    return index_planning_regulation(document)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_immutable_models_and_validators`

**Purpose**

Exercises `public api exports immutable models and validators`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
for name in (
        "PlanningRegulationIndex",
        "PlanningRegulationIndexError",
        "PlanningRegulationSearchResult",
        "index_planning_regulation",
        "search_planning_regulation",
        "validate_planning_regulation_index",
        "validate_planning_regulation_search_result",
    ):
        assert name in stages.__all__
        assert hasattr(stages, name)
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

Locks `public api exports immutable models and validators` through the exact asserted conditions: `name in stages.__all__`; `hasattr(stages, name)`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_api_exports_immutable_models_and_validators() -> None:
    for name in (
        "PlanningRegulationIndex",
        "PlanningRegulationIndexError",
        "PlanningRegulationSearchResult",
        "index_planning_regulation",
        "search_planning_regulation",
        "validate_planning_regulation_index",
        "validate_planning_regulation_search_result",
    ):
        assert name in stages.__all__
        assert hasattr(stages, name)
```

### `test_source_nomfic_resolves_generic_filename`

**Purpose**

Exercises `source nomfic resolves generic filename`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `filename`.

**Setup**

```python
document = _fixture_document(tmp_path, filename=filename)
_patch_reader(monkeypatch, ["Texte"])
```

**Action**

```python
result = index_planning_regulation(document)
```

**Expected result**

```python
assert Path(result.pdf_relative_path).name == filename
```

**Regression protected**

Locks `source nomfic resolves generic filename` through the exact asserted conditions: `Path(result.pdf_relative_path).name == filename`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_nomfic_resolves_generic_filename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    filename: str,
) -> None:
    document = _fixture_document(tmp_path, filename=filename)
    _patch_reader(monkeypatch, ["Texte"])
    result = index_planning_regulation(document)
    assert Path(result.pdf_relative_path).name == filename
```

### `test_explicit_source_validated_selection_succeeds`

**Purpose**

Exercises `explicit source validated selection succeeds`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
filenames = ("a.pdf", "b.pdf")
document = _fixture_document(
        tmp_path,
        filename="a.pdf",
        zoning_filenames=list(filenames),
        written_filenames=filenames,
        inventory_filenames=filenames,
    )
_patch_reader(monkeypatch, ["Texte"])
```

**Action**

```python
result = index_planning_regulation(document, regulation_filename="b.pdf")
```

**Expected result**

```python
assert Path(result.pdf_relative_path).name == "b.pdf"
```

**Regression protected**

Locks `explicit source validated selection succeeds` through the exact asserted conditions: `Path(result.pdf_relative_path).name == 'b.pdf'`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_explicit_source_validated_selection_succeeds(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    filenames = ("a.pdf", "b.pdf")
    document = _fixture_document(
        tmp_path,
        filename="a.pdf",
        zoning_filenames=list(filenames),
        written_filenames=filenames,
        inventory_filenames=filenames,
    )
    _patch_reader(monkeypatch, ["Texte"])
    result = index_planning_regulation(document, regulation_filename="b.pdf")
    assert Path(result.pdf_relative_path).name == "b.pdf"
```

### `test_unchanged_zoning_source_is_revalidated_before_selection`

**Purpose**

Exercises `unchanged zoning source is revalidated before selection`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `source_format`.

**Setup**

```python
document = _fixture_document(tmp_path, source_format=source_format)
_patch_reader(monkeypatch, ["Texte"])
```

**Action**

```python
result = index_planning_regulation(document)
```

**Expected result**

```python
assert result.regulation_filename == DEFAULT_PDF
assert result.source_selection_method == "ZONING_NOMFIC"
assert fullmatch(r"[0-9a-f]{64}", result.source_selection_sha256)
```

**Regression protected**

Locks `unchanged zoning source is revalidated before selection` through the exact asserted conditions: `result.regulation_filename == DEFAULT_PDF`; `result.source_selection_method == 'ZONING_NOMFIC'`; `fullmatch('[0-9a-f]{64}', result.source_selection_sha256)`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unchanged_zoning_source_is_revalidated_before_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    source_format: str,
) -> None:
    document = _fixture_document(tmp_path, source_format=source_format)
    _patch_reader(monkeypatch, ["Texte"])
    result = index_planning_regulation(document)
    assert result.regulation_filename == DEFAULT_PDF
    assert result.source_selection_method == "ZONING_NOMFIC"
    assert fullmatch(r"[0-9a-f]{64}", result.source_selection_sha256)
```

### `test_mutated_loaded_nomfic_is_rejected_before_selection`

**Purpose**

Exercises `mutated loaded nomfic is rejected before selection`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
mutated = document.zoning.data.copy(deep=True)
mutated.loc[0, "NOMFIC"] = "other_reglement.pdf"
corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)
```

**Regression protected**

Locks `mutated loaded nomfic is rejected before selection`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_mutated_loaded_nomfic_is_rejected_before_selection(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    mutated = document.zoning.data.copy(deep=True)
    mutated.loc[0, "NOMFIC"] = "other_reglement.pdf"
    corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
    with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)
```

### `test_mutated_loaded_zoning_geometry_or_order_is_rejected`

**Purpose**

Exercises `mutated loaded zoning geometry or order is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
document = _fixture_document(
        tmp_path,
        zoning_filenames=[DEFAULT_PDF, DEFAULT_PDF],
    )
mutated = document.zoning.data.copy(deep=True)
if mutation == "reorder":
        mutated = mutated.iloc[::-1].reset_index(drop=True)
    else:
        geometry = mutated.geometry.copy()
        geometry.iloc[0] = Polygon([(20, 0), (20, 1), (21, 1), (21, 0), (20, 0)])
        mutated = mutated.set_geometry(geometry)
corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_mutated_loaded_zoning_geometry_or_order_is_rejected(
    tmp_path: Path,
    mutation: str,
) -> None:
    document = _fixture_document(
        tmp_path,
        zoning_filenames=[DEFAULT_PDF, DEFAULT_PDF],
    )
    mutated = document.zoning.data.copy(deep=True)
    if mutation == "reorder":
        mutated = mutated.iloc[::-1].reset_index(drop=True)
    else:
        geometry = mutated.geometry.copy()
        geometry.iloc[0] = Polygon([(20, 0), (20, 1), (21, 1), (21, 0), (20, 0)])
        mutated = mutated.set_geometry(geometry)
    corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
    with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)
```

### `test_zoning_source_bytes_changed_after_ingestion_are_rejected`

**Purpose**

Exercises `zoning source bytes changed after ingestion are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
with document.zoning.reference.dataset_path.open("ab") as stream:
        stream.write(b"tamper")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(document)
```

**Regression protected**

Locks `zoning source bytes changed after ingestion are rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_zoning_source_bytes_changed_after_ingestion_are_rejected(
    tmp_path: Path,
) -> None:
    document = _fixture_document(tmp_path)
    with document.zoning.reference.dataset_path.open("ab") as stream:
        stream.write(b"tamper")
    with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(document)
```

### `test_zoning_source_inventory_integrity_mismatch_is_rejected`

**Purpose**

Exercises `zoning source inventory integrity mismatch is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
document = _fixture_document(tmp_path)
items = list(document.extraction.files)
position = next(
        index for index, item in enumerate(items) if item.category == "SPATIAL_DATA"
    )
current = items[position]
replacement: object = (
        current.size_bytes + 1 if field == "size_bytes" else "b" * 64
    )
items[position] = replace(current, **{field: replacement})
corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(corrupted)
```

**Regression protected**

Locks `zoning source inventory integrity mismatch is rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_zoning_source_inventory_integrity_mismatch_is_rejected(
    tmp_path: Path,
    field: str,
) -> None:
    document = _fixture_document(tmp_path)
    items = list(document.extraction.files)
    position = next(
        index for index, item in enumerate(items) if item.category == "SPATIAL_DATA"
    )
    current = items[position]
    replacement: object = (
        current.size_bytes + 1 if field == "size_bytes" else "b" * 64
    )
    items[position] = replace(current, **{field: replacement})
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(corrupted)
```

### `test_missing_nomfic_field_is_rejected`

**Purpose**

Exercises `missing nomfic field is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path, include_nomfic=False)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC"):
        index_planning_regulation(document)
```

**Regression protected**

Locks `missing nomfic field is rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_missing_nomfic_field_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, include_nomfic=False)
    with pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC"):
        index_planning_regulation(document)
```

### `test_null_nomfic_is_rejected`

**Purpose**

Exercises `null nomfic is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path, zoning_filenames=[None])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="no regulation filename"):
        index_planning_regulation(document)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_null_nomfic_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, zoning_filenames=[None])
    with pytest.raises(PlanningRegulationIndexError, match="no regulation filename"):
        index_planning_regulation(document)
```

### `test_multiple_nomfic_values_are_ambiguous`

**Purpose**

Exercises `multiple nomfic values are ambiguous`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(
        tmp_path,
        filename="a.pdf",
        zoning_filenames=["a.pdf", "b.pdf"],
        written_filenames=("a.pdf", "b.pdf"),
        inventory_filenames=("a.pdf", "b.pdf"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)
```

**Regression protected**

Locks `multiple nomfic values are ambiguous`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_multiple_nomfic_values_are_ambiguous(tmp_path: Path) -> None:
    document = _fixture_document(
        tmp_path,
        filename="a.pdf",
        zoning_filenames=["a.pdf", "b.pdf"],
        written_filenames=("a.pdf", "b.pdf"),
        inventory_filenames=("a.pdf", "b.pdf"),
    )
    with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)
```

### `test_unsafe_explicit_filename_is_rejected`

**Purpose**

Exercises `unsafe explicit filename is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `filename`.

**Setup**

```python
document = _fixture_document(tmp_path)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="filename"):
        index_planning_regulation(document, regulation_filename=filename)
```

**Regression protected**

Locks `unsafe explicit filename is rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unsafe_explicit_filename_is_rejected(tmp_path: Path, filename: str) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="filename"):
        index_planning_regulation(document, regulation_filename=filename)
```

### `test_explicit_filename_not_referenced_by_zoning_fails`

**Purpose**

Exercises `explicit filename not referenced by zoning fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="not referenced"):
        index_planning_regulation(document, regulation_filename="other.pdf")
```

**Regression protected**

Locks `explicit filename not referenced by zoning fails`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_explicit_filename_not_referenced_by_zoning_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="not referenced"):
        index_planning_regulation(document, regulation_filename="other.pdf")
```

### `test_filename_absent_from_written_files_fails`

**Purpose**

Exercises `filename absent from written files fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path, written_filenames=("other.pdf",))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="written_files"):
        index_planning_regulation(document)
```

**Regression protected**

Locks `filename absent from written files fails`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_filename_absent_from_written_files_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, written_filenames=("other.pdf",))
    with pytest.raises(PlanningRegulationIndexError, match="written_files"):
        index_planning_regulation(document)
```

### `test_unrelated_non_pdf_written_file_does_not_block_selection`

**Purpose**

Exercises `unrelated non pdf written file does not block selection`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(
        tmp_path, written_filenames=(DEFAULT_PDF, "technical-note.txt")
    )
_patch_reader(monkeypatch, ["Texte"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert index_planning_regulation(document).total_page_count == 1
```

**Regression protected**

Locks `unrelated non pdf written file does not block selection` through the exact asserted conditions: `index_planning_regulation(document).total_page_count == 1`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unrelated_non_pdf_written_file_does_not_block_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(
        tmp_path, written_filenames=(DEFAULT_PDF, "technical-note.txt")
    )
    _patch_reader(monkeypatch, ["Texte"])
    assert index_planning_regulation(document).total_page_count == 1
```

### `test_filename_absent_from_inventory_fails`

**Purpose**

Exercises `filename absent from inventory fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
item_position = next(
        index
        for index, item in enumerate(document.extraction.files)
        if item.category == "WRITTEN_REGULATION"
    )
items = list(document.extraction.files)
items[item_position] = replace(
        items[item_position], relative_path="written/other.pdf"
    )
corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningRegulationIndexError,
        match="missing from GPU inventory|verified manifest",
    ):
        index_planning_regulation(corrupted)
```

**Regression protected**

Locks `filename absent from inventory fails`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_filename_absent_from_inventory_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item_position = next(
        index
        for index, item in enumerate(document.extraction.files)
        if item.category == "WRITTEN_REGULATION"
    )
    items = list(document.extraction.files)
    items[item_position] = replace(
        items[item_position], relative_path="written/other.pdf"
    )
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(
        PlanningRegulationIndexError,
        match="missing from GPU inventory|verified manifest",
    ):
        index_planning_regulation(corrupted)
```

### `test_duplicate_inventory_basename_fails`

**Purpose**

Exercises `duplicate inventory basename fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(
        tmp_path, inventory_filenames=(DEFAULT_PDF, DEFAULT_PDF)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)
```

**Regression protected**

Locks `duplicate inventory basename fails`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_inventory_basename_fails(tmp_path: Path) -> None:
    document = _fixture_document(
        tmp_path, inventory_filenames=(DEFAULT_PDF, DEFAULT_PDF)
    )
    with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)
```

### `test_path_outside_root_is_rejected`

**Purpose**

Exercises `path outside root is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
item = replace(
        document.extraction.files[0], relative_path=f"../{DEFAULT_PDF}"
    )
corrupted = replace(
        document,
        extraction=replace(document.extraction, files=(item,)),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningRegulationIndexError,
        match="unsafe|verified manifest",
    ):
        index_planning_regulation(corrupted)
```

**Regression protected**

Locks `path outside root is rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_path_outside_root_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item = replace(
        document.extraction.files[0], relative_path=f"../{DEFAULT_PDF}"
    )
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=(item,)),
    )
    with pytest.raises(
        PlanningRegulationIndexError,
        match="unsafe|verified manifest",
    ):
        index_planning_regulation(corrupted)
```

### `test_pdf_inventory_integrity_mismatch_fails`

**Purpose**

Exercises `pdf inventory integrity mismatch fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
document = _fixture_document(tmp_path)
value: object = len(PDF_BYTES) + 1 if field == "size_bytes" else "b" * 64
item_position = next(
        index
        for index, item in enumerate(document.extraction.files)
        if item.category == "WRITTEN_REGULATION"
    )
items = list(document.extraction.files)
items[item_position] = replace(items[item_position], **{field: value})
corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="differs"):
        index_planning_regulation(corrupted)
```

**Regression protected**

Locks `pdf inventory integrity mismatch fails`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_pdf_inventory_integrity_mismatch_fails(tmp_path: Path, field: str) -> None:
    document = _fixture_document(tmp_path)
    value: object = len(PDF_BYTES) + 1 if field == "size_bytes" else "b" * 64
    item_position = next(
        index
        for index, item in enumerate(document.extraction.files)
        if item.category == "WRITTEN_REGULATION"
    )
    items = list(document.extraction.files)
    items[item_position] = replace(items[item_position], **{field: value})
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="differs"):
        index_planning_regulation(corrupted)
```

### `test_page_states_numbering_and_hashes`

**Purpose**

Exercises `page states numbering and hashes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
raw = "ÉNERGIE\n Batterie  "
_patch_reader(monkeypatch, [raw, " \n", RuntimeError("page failed")])
```

**Action**

```python
result = index_planning_regulation(document)
validate_planning_regulation_index(result)
```

**Expected result**

```python
assert tuple(result.pages.columns) == PAGE_COLUMNS
assert result.pages.page_number.tolist() == [1, 2, 3]
assert result.pages.extraction_status.tolist() == ["TEXT", "EMPTY", "ERROR"]
assert result.pages.loc[0, "raw_text"] == raw
assert result.pages.loc[0, "normalized_search_text"] == "energie batterie"
assert result.pages.page_content_sha256.str.fullmatch(r"[0-9a-f]{64}").all()
assert fullmatch(r"[0-9a-f]{64}", result.pages_content_sha256)
with pytest.raises(FrozenInstanceError):
        result.total_page_count = 9
```

**Regression protected**

Locks `page states numbering and hashes`: the reproduced adversarial input must raise `FrozenInstanceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_page_states_numbering_and_hashes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    raw = "ÉNERGIE\n Batterie  "
    _patch_reader(monkeypatch, [raw, " \n", RuntimeError("page failed")])
    result = index_planning_regulation(document)
    assert tuple(result.pages.columns) == PAGE_COLUMNS
    assert result.pages.page_number.tolist() == [1, 2, 3]
    assert result.pages.extraction_status.tolist() == ["TEXT", "EMPTY", "ERROR"]
    assert result.pages.loc[0, "raw_text"] == raw
    assert result.pages.loc[0, "normalized_search_text"] == "energie batterie"
    assert result.pages.page_content_sha256.str.fullmatch(r"[0-9a-f]{64}").all()
    assert fullmatch(r"[0-9a-f]{64}", result.pages_content_sha256)
    validate_planning_regulation_index(result)
    with pytest.raises(FrozenInstanceError):
        result.total_page_count = 9
```

### `test_zero_page_pdf_is_rejected`

**Purpose**

Exercises `zero page pdf is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
_patch_reader(monkeypatch, [])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="at least one page"):
        index_planning_regulation(document)
```

**Regression protected**

Locks `zero page pdf is rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_zero_page_pdf_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [])
    with pytest.raises(PlanningRegulationIndexError, match="at least one page"):
        index_planning_regulation(document)
```

### `test_pdf_reader_failure_is_controlled_and_chained`

**Purpose**

Exercises `pdf reader failure is controlled and chained`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
def fail_reader(*args: object, **kwargs: object) -> object:
        raise RuntimeError("broken xref")
monkeypatch.setattr(regulation_module, "PdfReader", fail_reader)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningRegulationIndexError, match="opened or parsed"
    ) as caught:
        index_planning_regulation(document)
assert isinstance(caught.value.__cause__, RuntimeError)
```

**Regression protected**

Locks `pdf reader failure is controlled and chained`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_pdf_reader_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)

    def fail_reader(*args: object, **kwargs: object) -> object:
        raise RuntimeError("broken xref")

    monkeypatch.setattr(regulation_module, "PdfReader", fail_reader)
    with pytest.raises(
        PlanningRegulationIndexError, match="opened or parsed"
    ) as caught:
        index_planning_regulation(document)
    assert isinstance(caught.value.__cause__, RuntimeError)
```

### `test_pdf_reader_failure_is_controlled_and_chained.fail_reader`

**Exact signature**

```python
def fail_reader(*args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for fail reader; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `RuntimeError('broken xref')`.

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

- function object argument: `tests/unit/test_index_planning_regulation.py::test_pdf_reader_failure_is_controlled_and_chained` via `monkeypatch.setattr(regulation_module, 'PdfReader', fail_reader)`.

**Complete source-ordered implementation**

```python
def fail_reader(*args: object, **kwargs: object) -> object:
        raise RuntimeError("broken xref")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_french_literal_normalization`

**Purpose**

Exercises `french literal normalization`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `source`, `term`.

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
assert _normalize_search_text(source) == term
```

**Regression protected**

Locks `french literal normalization` through the exact asserted conditions: `_normalize_search_text(source) == term`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_french_literal_normalization(source: str, term: str) -> None:
    assert _normalize_search_text(source) == term
```

### `test_raw_context_preserves_source_typography`

**Purpose**

Exercises `raw context preserves source typography`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
raw = "Le projet vise un Équipement d’intérêt collectif dans la zone."
index = _one_page_index(tmp_path, monkeypatch, raw)
hit = result.hits.iloc[0]
```

**Action**

```python
result = search_planning_regulation(
        index, ["equipement d'interet collectif"], context_characters=4
    )
```

**Expected result**

```python
assert hit["page_number"] == 1
assert hit["occurrence_count"] == 1
assert "Équipement d’intérêt collectif" in hit["raw_context"]
assert "equipement d'interet collectif" in hit["normalized_context"]
assert index.pages.iloc[0]["raw_text"] == raw
```

**Regression protected**

Locks `raw context preserves source typography` through the exact asserted conditions: `hit['page_number'] == 1`; `hit['occurrence_count'] == 1`; `'Équipement d’intérêt collectif' in hit['raw_context']`; `"equipement d'interet collectif" in hit['normalized_context']`; plus 1 additional reproduced assertion(s).

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_raw_context_preserves_source_typography(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    raw = "Le projet vise un Équipement d’intérêt collectif dans la zone."
    index = _one_page_index(tmp_path, monkeypatch, raw)
    result = search_planning_regulation(
        index, ["equipement d'interet collectif"], context_characters=4
    )
    hit = result.hits.iloc[0]
    assert hit["page_number"] == 1
    assert hit["occurrence_count"] == 1
    assert "Équipement d’intérêt collectif" in hit["raw_context"]
    assert "equipement d'interet collectif" in hit["normalized_context"]
    assert index.pages.iloc[0]["raw_text"] == raw
```

### `test_zero_context_preserves_complete_raw_unicode_span`

**Purpose**

Exercises `zero context preserves complete raw unicode span`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `expected_normalized`, `expected_raw`, `raw`, `term`.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch, raw)
hit = result.hits.iloc[0]
```

**Action**

```python
result = search_planning_regulation(index, [term], context_characters=0)
```

**Expected result**

```python
assert hit["raw_context"] == expected_raw
assert hit["normalized_context"] == expected_normalized
assert hit["raw_context"] in raw
assert index.pages.iloc[0]["raw_text"] == raw
```

**Regression protected**

Locks `zero context preserves complete raw unicode span` through the exact asserted conditions: `hit['raw_context'] == expected_raw`; `hit['normalized_context'] == expected_normalized`; `hit['raw_context'] in raw`; `index.pages.iloc[0]['raw_text'] == raw`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_zero_context_preserves_complete_raw_unicode_span(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    raw: str,
    term: str,
    expected_raw: str,
    expected_normalized: str,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, raw)
    result = search_planning_regulation(index, [term], context_characters=0)
    hit = result.hits.iloc[0]
    assert hit["raw_context"] == expected_raw
    assert hit["normalized_context"] == expected_normalized
    assert hit["raw_context"] in raw
    assert index.pages.iloc[0]["raw_text"] == raw
```

### `test_literal_search_does_not_add_semantic_synonyms`

**Purpose**

Exercises `literal search does not add semantic synonyms`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch, "Une batterie est mentionnée.")
```

**Action**

```python
result = search_planning_regulation(index, ["accumulateur"])
```

**Expected result**

```python
assert result.hits.empty
```

**Regression protected**

Locks `literal search does not add semantic synonyms` through the exact asserted conditions: `result.hits.empty`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_literal_search_does_not_add_semantic_synonyms(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, "Une batterie est mentionnée.")
    result = search_planning_regulation(index, ["accumulateur"])
    assert result.hits.empty
```

### `test_version_discovery_failure_is_controlled_and_chained`

**Purpose**

Exercises `version discovery failure is controlled and chained`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
_patch_reader(monkeypatch, ["Texte"])
def fail_version(name: str) -> str:
        raise RuntimeError(name)
monkeypatch.setattr(regulation_module, "version", fail_version)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="version") as caught:
        index_planning_regulation(document)
assert isinstance(caught.value.__cause__, RuntimeError)
```

**Regression protected**

Locks `version discovery failure is controlled and chained`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_version_discovery_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["Texte"])

    def fail_version(name: str) -> str:
        raise RuntimeError(name)

    monkeypatch.setattr(regulation_module, "version", fail_version)
    with pytest.raises(PlanningRegulationIndexError, match="version") as caught:
        index_planning_regulation(document)
    assert isinstance(caught.value.__cause__, RuntimeError)
```

### `test_version_discovery_failure_is_controlled_and_chained.fail_version`

**Exact signature**

```python
def fail_version(name: str) -> str:
```

**Purpose**

Private `test` helper for fail version; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `RuntimeError(name)`.

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

- function object argument: `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained` via `monkeypatch.setattr(regulation_module, 'version', fail_version)`.

**Complete source-ordered implementation**

```python
def fail_version(name: str) -> str:
        raise RuntimeError(name)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_page_mutation_fails_envelope_hash`

**Purpose**

Exercises `coordinated page mutation fails envelope hash`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch)
pages = index.pages.copy(deep=True)
pages.loc[0, "raw_text"] = "Nouveau"
pages.loc[0, "normalized_search_text"] = "nouveau"
pages.loc[0, "character_count"] = 7
row = pages.iloc[0].to_dict()
pages.loc[0, "page_content_sha256"] = regulation_module._page_content_sha256(row)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="envelope"):
        validate_planning_regulation_index(replace(index, pages=pages))
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_coordinated_page_mutation_fails_envelope_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    pages = index.pages.copy(deep=True)
    pages.loc[0, "raw_text"] = "Nouveau"
    pages.loc[0, "normalized_search_text"] = "nouveau"
    pages.loc[0, "character_count"] = 7
    row = pages.iloc[0].to_dict()
    pages.loc[0, "page_content_sha256"] = regulation_module._page_content_sha256(row)
    with pytest.raises(PlanningRegulationIndexError, match="envelope"):
        validate_planning_regulation_index(replace(index, pages=pages))
```

### `test_index_integrity_mutations_fail`

**Purpose**

Exercises `index integrity mutations fail`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `target`, `value`.

**Setup**

```python
document = _fixture_document(tmp_path)
_patch_reader(monkeypatch, ["One", "Two"])
if target == "page_hash":
        pages = index.pages.copy(deep=True)
        pages.loc[0, "page_content_sha256"] = value
        corrupted = replace(index, pages=pages)
    elif target == "envelope_hash":
        corrupted = replace(index, pages_content_sha256=value)
    elif target == "profile":
        corrupted = replace(index, search_normalization_profile=value)
    else:
        corrupted = replace(index, pages=index.pages.iloc[::-1].reset_index(drop=True))
```

**Action**

```python
index = index_planning_regulation(document)
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(corrupted)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_index_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["One", "Two"])
    index = index_planning_regulation(document)
    if target == "page_hash":
        pages = index.pages.copy(deep=True)
        pages.loc[0, "page_content_sha256"] = value
        corrupted = replace(index, pages=pages)
    elif target == "envelope_hash":
        corrupted = replace(index, pages_content_sha256=value)
    elif target == "profile":
        corrupted = replace(index, search_normalization_profile=value)
    else:
        corrupted = replace(index, pages=index.pages.iloc[::-1].reset_index(drop=True))
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(corrupted)
```

### `test_complete_index_envelope_mutation_is_rejected`

**Purpose**

Exercises `complete index envelope mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `replacement`.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, **{field: replacement}))
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_complete_index_envelope_mutation_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, **{field: replacement}))
```

### `test_unsupported_or_malformed_index_hash_schema_is_rejected`

**Purpose**

Exercises `unsupported or malformed index hash schema is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `replacement`.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(
            replace(index, index_hash_schema_version=replacement)
        )
```

**Regression protected**

Locks `unsupported or malformed index hash schema is rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unsupported_or_malformed_index_hash_schema_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(
            replace(index, index_hash_schema_version=replacement)
        )
```

### `test_malformed_page_hash_schema_is_rejected_as_controlled_error`

**Purpose**

Exercises `malformed page hash schema is rejected as controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `replacement`.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(
            replace(index, page_hash_schema_version=replacement)
        )
```

**Regression protected**

Locks `malformed page hash schema is rejected as controlled error`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_page_hash_schema_is_rejected_as_controlled_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(
            replace(index, page_hash_schema_version=replacement)
        )
```

### `_valid_search_result`

**Exact signature**

```python
def _valid_search_result(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
```

**Purpose**

Private `test` helper for valid search result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
(index, result)
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

- direct call: `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic` via `_valid_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_index_identity_schema_and_terms_are_sealed` via `_valid_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `_valid_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_result_integrity_mutations_fail` via `_valid_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_search_hit_lineage_mutation_fails` via `_valid_search_result`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_malformed_hit_value_raises_controlled_index_error` via `_valid_search_result`.

**Complete source-ordered implementation**

```python
def _valid_search_result(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    index = _one_page_index(
        tmp_path,
        monkeypatch,
        "Énergie énergie et Équipement d’intérêt collectif",
    )
    result = search_planning_regulation(
        index, ["energie", "equipement d'interet collectif"]
    )
    return index, result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_search_result_envelope_is_valid_and_deterministic`

**Purpose**

Exercises `search result envelope is valid and deterministic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, first = _valid_search_result(tmp_path, monkeypatch)
assert_frame_equal(first.hits, second.hits)
```

**Action**

```python
second = search_planning_regulation(index, first.requested_terms)
validate_planning_regulation_search_result(index, first)
```

**Expected result**

```python
assert tuple(first.hits.columns) == SEARCH_HIT_COLUMNS
assert first.search_normalization_profile == SEARCH_NORMALIZATION_PROFILE
assert first.index_content_sha256 == index.index_content_sha256
assert first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION
assert first.hit_count == 2
assert first.hits_content_sha256 == second.hits_content_sha256
```

**Regression protected**

Locks `search result envelope is valid and deterministic` through the exact asserted conditions: `tuple(first.hits.columns) == SEARCH_HIT_COLUMNS`; `first.search_normalization_profile == SEARCH_NORMALIZATION_PROFILE`; `first.index_content_sha256 == index.index_content_sha256`; `first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION`; plus 2 additional reproduced assertion(s).

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_search_result_envelope_is_valid_and_deterministic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index, first = _valid_search_result(tmp_path, monkeypatch)
    second = search_planning_regulation(index, first.requested_terms)
    assert tuple(first.hits.columns) == SEARCH_HIT_COLUMNS
    assert first.search_normalization_profile == SEARCH_NORMALIZATION_PROFILE
    assert first.index_content_sha256 == index.index_content_sha256
    assert first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION
    assert first.hit_count == 2
    assert_frame_equal(first.hits, second.hits)
    assert first.hits_content_sha256 == second.hits_content_sha256
    validate_planning_regulation_search_result(index, first)
```

### `test_search_index_identity_schema_and_terms_are_sealed`

**Purpose**

Exercises `search index identity schema and terms are sealed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `replacement`.

**Setup**

```python
index, result = _valid_search_result(tmp_path, monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(
            index,
            replace(result, **{field: replacement}),
        )
```

**Regression protected**

Locks `search index identity schema and terms are sealed`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_search_index_identity_schema_and_terms_are_sealed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(
            index,
            replace(result, **{field: replacement}),
        )
```

### `test_search_requested_terms_must_be_an_immutable_exact_tuple`

**Purpose**

Exercises `search requested terms must be an immutable exact tuple`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = _valid_search_result(tmp_path, monkeypatch)
corrupted = replace(
        result,
        requested_terms=list(result.requested_terms),  # type: ignore[arg-type]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="tuple"):
        validate_planning_regulation_search_result(index, corrupted)
```

**Regression protected**

Locks `search requested terms must be an immutable exact tuple`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_search_requested_terms_must_be_an_immutable_exact_tuple(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    corrupted = replace(
        result,
        requested_terms=list(result.requested_terms),  # type: ignore[arg-type]
    )
    with pytest.raises(PlanningRegulationIndexError, match="tuple"):
        validate_planning_regulation_search_result(index, corrupted)
```

### `test_search_result_integrity_mutations_fail`

**Purpose**

Exercises `search result integrity mutations fail`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `target`, `value`.

**Setup**

```python
index, result = _valid_search_result(tmp_path, monkeypatch)
if target in {"document_id", "pdf_sha256", "hits_content_sha256"}:
        corrupted = replace(result, **{target: value})
    else:
        hits = result.hits.copy(deep=True)
        if target == "duplicate":
            hits = pd.concat([hits, hits.iloc[[0]]], ignore_index=True)
            corrupted = replace(result, hit_count=len(hits), hits=hits)
        else:
            hits[target] = hits[target].astype(object)
            hits.loc[0, target] = value
            corrupted = replace(result, hits=hits)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(index, corrupted)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_search_result_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    if target in {"document_id", "pdf_sha256", "hits_content_sha256"}:
        corrupted = replace(result, **{target: value})
    else:
        hits = result.hits.copy(deep=True)
        if target == "duplicate":
            hits = pd.concat([hits, hits.iloc[[0]]], ignore_index=True)
            corrupted = replace(result, hit_count=len(hits), hits=hits)
        else:
            hits[target] = hits[target].astype(object)
            hits.loc[0, target] = value
            corrupted = replace(result, hits=hits)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(index, corrupted)
```

### `test_search_hit_lineage_mutation_fails`

**Purpose**

Exercises `search hit lineage mutation fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
index, result = _valid_search_result(tmp_path, monkeypatch)
hits = result.hits.copy(deep=True)
hits.loc[0, column] = "b" * 64 if column == "pdf_sha256" else "wrong"
corrupted = replace(result, hits=hits)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="lineage"):
        validate_planning_regulation_search_result(index, corrupted)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_search_hit_lineage_mutation_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    column: str,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    hits = result.hits.copy(deep=True)
    hits.loc[0, column] = "b" * 64 if column == "pdf_sha256" else "wrong"
    corrupted = replace(result, hits=hits)
    with pytest.raises(PlanningRegulationIndexError, match="lineage"):
        validate_planning_regulation_search_result(index, corrupted)
```

### `test_invalid_search_term_is_rejected`

**Purpose**

Exercises `invalid search term is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `term`.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="search term"):
        search_planning_regulation(index, [term])
```

**Regression protected**

Locks `invalid search term is rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="search term"):
        search_planning_regulation(index, [term])
```

### `test_duplicate_normalized_search_terms_are_rejected`

**Purpose**

Exercises `duplicate normalized search terms are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError, match="unique"):
        search_planning_regulation(index, ["énergie", "ENERGIE"])
```

**Regression protected**

Locks `duplicate normalized search terms are rejected`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_normalized_search_terms_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="unique"):
        search_planning_regulation(index, ["énergie", "ENERGIE"])
```

### `test_empty_search_result_has_stable_schema_and_lineage`

**Purpose**

Exercises `empty search result has stable schema and lineage`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch, "Aucun terme")
```

**Action**

```python
result = search_planning_regulation(index, ["batterie"])
validate_planning_regulation_search_result(index, result)
```

**Expected result**

```python
assert result.hit_count == 0
assert result.hits.empty
assert tuple(result.hits.columns) == SEARCH_HIT_COLUMNS
assert result.document_id == index.document_id
assert result.pdf_sha256 == index.pdf_sha256
```

**Regression protected**

Locks `empty search result has stable schema and lineage` through the exact asserted conditions: `result.hit_count == 0`; `result.hits.empty`; `tuple(result.hits.columns) == SEARCH_HIT_COLUMNS`; `result.document_id == index.document_id`; plus 1 additional reproduced assertion(s).

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_empty_search_result_has_stable_schema_and_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, "Aucun terme")
    result = search_planning_regulation(index, ["batterie"])
    assert result.hit_count == 0
    assert result.hits.empty
    assert tuple(result.hits.columns) == SEARCH_HIT_COLUMNS
    assert result.document_id == index.document_id
    assert result.pdf_sha256 == index.pdf_sha256
    validate_planning_regulation_search_result(index, result)
```

### `test_malformed_page_value_raises_controlled_index_error`

**Purpose**

Exercises `malformed page value raises controlled index error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _one_page_index(tmp_path, monkeypatch)
pages = index.pages.copy(deep=True)
pages.at[0, "extraction_error"] = ["ambiguous", "value"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, pages=pages))
```

**Regression protected**

Locks `malformed page value raises controlled index error`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_page_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    pages = index.pages.copy(deep=True)
    pages.at[0, "extraction_error"] = ["ambiguous", "value"]
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, pages=pages))
```

### `test_malformed_hit_value_raises_controlled_index_error`

**Purpose**

Exercises `malformed hit value raises controlled index error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = _valid_search_result(tmp_path, monkeypatch)
hits = result.hits.copy(deep=True)
hits["raw_context"] = hits["raw_context"].astype(object)
hits.at[0, "raw_context"] = ["not", "text"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(
            index,
            replace(result, hits=hits),
        )
```

**Regression protected**

Locks `malformed hit value raises controlled index error`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_hit_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    hits = result.hits.copy(deep=True)
    hits["raw_context"] = hits["raw_context"].astype(object)
    hits.at[0, "raw_context"] = ["not", "text"]
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(
            index,
            replace(result, hits=hits),
        )
```

### `test_canonical_hash_serialization_failure_is_controlled_and_chained`

**Purpose**

Exercises `canonical hash serialization failure is controlled and chained`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid_payload = {"not_json": object()}
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningRegulationIndexError,
        match="serialized",
    ) as caught:
        regulation_module._canonical_sha256(invalid_payload)
assert isinstance(caught.value.__cause__, TypeError)
```

**Regression protected**

Locks `canonical hash serialization failure is controlled and chained`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_canonical_hash_serialization_failure_is_controlled_and_chained() -> None:
    invalid_payload = {"not_json": object()}
    with pytest.raises(
        PlanningRegulationIndexError,
        match="serialized",
    ) as caught:
        regulation_module._canonical_sha256(invalid_payload)
    assert isinstance(caught.value.__cause__, TypeError)
```

### `test_malformed_source_metadata_raises_controlled_index_error`

**Purpose**

Exercises `malformed source metadata raises controlled index error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
metadata = replace(
        document.extraction.archive.document,
        written_files=(object(),),  # type: ignore[arg-type]
    )
archive = replace(document.extraction.archive, document=metadata)
corrupted = replace(
        document,
        extraction=replace(document.extraction, archive=archive),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationIndexError):
        index_planning_regulation(corrupted)
```

**Regression protected**

Locks `malformed source metadata raises controlled index error`: the reproduced adversarial input must raise `PlanningRegulationIndexError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_source_metadata_raises_controlled_index_error(
    tmp_path: Path,
) -> None:
    document = _fixture_document(tmp_path)
    metadata = replace(
        document.extraction.archive.document,
        written_files=(object(),),  # type: ignore[arg-type]
    )
    archive = replace(document.extraction.archive, document=metadata)
    corrupted = replace(
        document,
        extraction=replace(document.extraction, archive=archive),
    )
    with pytest.raises(PlanningRegulationIndexError):
        index_planning_regulation(corrupted)
```

### `test_extraction_and_search_do_not_mutate_inputs`

**Purpose**

Exercises `extraction and search do not mutate inputs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
document = _fixture_document(tmp_path)
extraction_before = deepcopy(document.extraction)
zoning_before = document.zoning.data.copy(deep=True)
_patch_reader(monkeypatch, ["Énergie"])
pages_before = index.pages.copy(deep=True)
assert_geodataframe_equal(document.zoning.data, zoning_before)
assert_frame_equal(index.pages, pages_before)
```

**Action**

```python
index = index_planning_regulation(document)
search_planning_regulation(index, ["energie"])
```

**Expected result**

```python
assert document.extraction == extraction_before
```

**Regression protected**

Locks `extraction and search do not mutate inputs` through the exact asserted conditions: `document.extraction == extraction_before`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_extraction_and_search_do_not_mutate_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    extraction_before = deepcopy(document.extraction)
    zoning_before = document.zoning.data.copy(deep=True)
    _patch_reader(monkeypatch, ["Énergie"])
    index = index_planning_regulation(document)
    pages_before = index.pages.copy(deep=True)
    search_planning_regulation(index, ["energie"])
    assert document.extraction == extraction_before
    assert_geodataframe_equal(document.zoning.data, zoning_before)
    assert_frame_equal(index.pages, pages_before)
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
