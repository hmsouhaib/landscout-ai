# `tests/unit/test_index_planning_regulation.py`

## File identity

- Repository path: `tests/unit/test_index_planning_regulation.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `ccf022c4ba939e973768b63120307ae83ff402b41bc6091a013a2c0b7fe0012d`

## 1. Purpose

Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError, replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from re import fullmatch` — required by the implementation paths and symbols documented below.

### Third-party

- `from importlib import import_module` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_text import ( normalize_planning_search_text as _normalize_search_text, )` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( GpuArchiveDownload, GpuDocumentMetadata, GpuExtractedFile, GpuExtraction, GpuInspectedLayer, GpuLayerSummary, GpuPlanningDocument, GpuSpatialLayerReference, GpuWrittenFile, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.index_planning_regulation import ( PAGE_COLUMNS, SEARCH_HIT_COLUMNS, SEARCH_NORMALIZATION_PROFILE, PlanningRegulationIndexError, index_planning_regulation, search_planning_regulation, validate_planning_regulation_index, validate_planning_regulation_search_result, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `DOCUMENT_ID` | `"doc-1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_SHA` | `"a" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DEFAULT_PDF` | `"31395_reglement_20240215.pdf"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PDF_BYTES` | `b"synthetic-pdf-bytes"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `_FakePage`

**Purpose:** Groups the `FakePage` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `result` | `not explicitly annotated` | `assigned in `__init__` from `result`` | `not explicitly annotated` state used by `tests/unit/test_index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(self, result: object) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `extract_text` — `def extract_text(self) -> object:`; decorators `none`. The complete method algorithm appears in the function/method section.

### `_FakeReader`

**Purpose:** Groups the `FakeReader` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `pages` | `not explicitly annotated` | `assigned in `__init__` from `[_FakePage(page) for page in pages]`` | `not explicitly annotated` state used by `tests/unit/test_index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `is_encrypted` | `not explicitly annotated` | `assigned in `__init__` from `encrypted`` | `not explicitly annotated` state used by `tests/unit/test_index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

## 6. Functions and methods

### `_FakePage.__init__`

**Signature**

```python
def __init__(self, result: object) -> None:
```

**Purpose**

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.result` from `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakePage.extract_text`

**Signature**

```python
def extract_text(self) -> object:
```

**Purpose**

Extracts and validates text according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `self.result`.

**Algorithm**

1. Checks `isinstance(self.result, Exception)`. When true: Raises `self.result`.
2. Returns `self.result`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(self.result, Exception)` is true.

**Exceptions**

- Explicitly raises: `self.result`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `isinstance`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeReader.__init__`

**Signature**

```python
def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
```

**Purpose**

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `pages` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `encrypted` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.pages` from `[_FakePage(page) for page in pages]`.
2. Computes `self.is_encrypted` from `encrypted`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_FakePage`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_patch_reader`

**Signature**

```python
def _patch_reader(
    monkeypatch: pytest.MonkeyPatch,
    pages: list[object],
    *,
    encrypted: bool = False,
) -> None:
```

**Purpose**

Implements patch reader according to the exact implementation and guards in this file.

**Inputs**

- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `pages` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `encrypted` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `monkeypatch.setattr(regulation_module, 'PdfReader', lambda *args, **kwargs: _FakeReader(pages, encrypted=encrypted))` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_FakeReader`, `monkeypatch.setattr`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_one_page_index`
- `tests/unit/test_index_planning_regulation.py` — `test_explicit_source_validated_selection_succeeds`
- `tests/unit/test_index_planning_regulation.py` — `test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py` — `test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py` — `test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py` — `test_source_nomfic_resolves_generic_filename`
- `tests/unit/test_index_planning_regulation.py` — `test_unchanged_zoning_source_is_revalidated_before_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_unrelated_non_pdf_written_file_does_not_block_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_version_discovery_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py` — `test_zero_page_pdf_is_rejected`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_explicit_source_validated_selection_succeeds`
- `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py::test_source_nomfic_resolves_generic_filename`
- `tests/unit/test_index_planning_regulation.py::test_unchanged_zoning_source_is_revalidated_before_selection`
- `tests/unit/test_index_planning_regulation.py::test_unrelated_non_pdf_written_file_does_not_block_selection`
- `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py::test_zero_page_pdf_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_summary`

**Signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    source_layer: str = "ZONE",
) -> GpuLayerSummary:
```

**Purpose**

Implements summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; optional/default `'ZONE'`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuLayerSummary`. Observed return expression(s): `GpuLayerSummary(source_document_id=DOCUMENT_ID, source_archive_sha256=ARCHIVE_SHA, source_layer=source_layer, crs='EPSG:2154', feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna().sum())) for column in frame.columns)), geomet…`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `non_null` from `geometry.notna()`.
3. Computes `non_empty` from `non_null & ~geometry.is_empty`.
4. Returns `GpuLayerSummary(source_document_id=DOCUMENT_ID, source_archive_sha256=ARCHIVE_SHA, source_layer=source_layer, crs='EPSG:2154', feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna().sum()…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `(~non_null).sum`, `GpuLayerSummary`, `frame.dtypes.items`, `frame[column].isna`, `frame[column].isna().sum`, `geometry.geom_type.value_counts`, `geometry.geom_type.value_counts().sort_index`, `geometry.geom_type.value_counts().sort_index().items`, `geometry.notna`, `int`, `len`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_write_zoning_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zone_frame`

**Signature**

```python
def _zone_frame(
    nomfic: list[object] | None = None,
    *,
    include_nomfic: bool = True,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements zone frame according to the exact implementation and guards in this file.

**Inputs**

- `nomfic` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_nomfic` (`bool`; optional/default `True`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame(attributes, geometry=[Polygon([(index, 0), (index, 1), (index + 1, 1), (index + 1, 0), (index, 0)]) for index in range(count)], crs='EPSG:2154')`.

**Algorithm**

1. Computes `filenames` from `[DEFAULT_PDF] if nomfic is None else nomfic`.
2. Computes `count` from `len(filenames)`.
3. Defines `attributes` with annotation `dict[str, list[object]]` from `{'LIB_IDZONE': [f'ZONE-{index + 1}' for index in range(count)]}`.
4. Checks `include_nomfic`. When true: Computes `attributes['NOMFIC']` from `filenames`.
5. Returns `gpd.GeoDataFrame(attributes, geometry=[Polygon([(index, 0), (index, 1), (index + 1, 1), (index + 1, 0), (index, 0)]) for index in range(count)], crs='EPSG:2154')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `len`, `range`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_fixture_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_inventory_item`

**Signature**

```python
def _inventory_item(relative_path: str, data: bytes = PDF_BYTES) -> GpuExtractedFile:
```

**Purpose**

Implements inventory item according to the exact implementation and guards in this file.

**Inputs**

- `relative_path` (`str`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `data` (`bytes`; optional/default `PDF_BYTES`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuExtractedFile`. Observed return expression(s): `GpuExtractedFile(relative_path=relative_path, file_type='pdf', size_bytes=len(data), sha256=sha256(data).hexdigest(), category='WRITTEN_REGULATION')`.

**Algorithm**

1. Returns `GpuExtractedFile(relative_path=relative_path, file_type='pdf', size_bytes=len(data), sha256=sha256(data).hexdigest(), category='WRITTEN_REGULATION')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuExtractedFile`, `len`, `sha256`, `sha256(data).hexdigest`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_fixture_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_spatial_inventory_item`

**Signature**

```python
def _spatial_inventory_item(root: Path, path: Path) -> GpuExtractedFile:
```

**Purpose**

Implements spatial inventory item according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuExtractedFile`. Observed return expression(s): `GpuExtractedFile(relative_path=path.relative_to(root).as_posix(), file_type=path.suffix.lower().lstrip('.') or 'binary', size_bytes=len(data), sha256=sha256(data).hexdigest(), category='SPATIAL_DATA')`.

**Algorithm**

1. Computes `data` from `path.read_bytes()`.
2. Returns `GpuExtractedFile(relative_path=path.relative_to(root).as_posix(), file_type=path.suffix.lower().lstrip('.') or 'binary', size_bytes=len(data), sha256=sha256(data).hexdigest(), category='SPATIAL_DATA')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuExtractedFile`, `len`, `path.read_bytes`, `path.relative_to`, `path.relative_to(root).as_posix`, `path.suffix.lower`, `path.suffix.lower().lstrip`, `sha256`, `sha256(data).hexdigest`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_write_zoning_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_zoning_source`

**Signature**

```python
def _write_zoning_source(
    root: Path,
    frame: gpd.GeoDataFrame,
    *,
    source_format: str,
) -> tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]:
```

**Purpose**

Writes zoning source according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_format` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]`. Observed return expression(s): `(layer, inventory)`.

**Algorithm**

1. Computes `spatial_root` from `root / 'spatial'`.
2. Calls `spatial_root.mkdir(parents=True, exist_ok=True)` for its validation or side effect.
3. Checks `source_format == 'GPKG'`. When true: Computes `path` from `spatial_root / 'zone.gpkg'`. Computes `source_layer` from `'ZONE'`. Calls `frame.to_file(path, layer=source_layer, driver='GPKG', engine='pyogrio')` for its validation or side effect. Executes 3 additional source-ordered statement(s). Otherwise: Checks `source_format == 'ESRI Shapefile'`. When true: Computes `path` from `spatial_root / 'ZONE.shp'`. Computes `source_layer` from `path.stem`. Calls `frame.to_file(path, driver='ESRI Shapefile', engine='pyogrio')` for its validation or side effect. Executes 3 additional source-ordered statement(s). Otherwise: Raises `AssertionError(f'Unsupported test source format: {source_format}')`.
4. Computes `reference` from `GpuSpatialLayerReference(path, source_layer, driver)`.
5. Computes `layer` from `GpuInspectedLayer('zoning', reference, loaded, _summary(loaded, source_layer=source_layer))`.
6. Computes `inventory` from `tuple((_spatial_inventory_item(root, item) for item in source_paths))`.
7. Returns `(layer, inventory)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_file`, `spatial_root.mkdir`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `AssertionError`, `GpuInspectedLayer`, `GpuSpatialLayerReference`, `_spatial_inventory_item`, `_summary`, `candidate.is_file`, `frame.to_file`, `gpd.read_file`, `path.parent.glob`, `sorted`, `spatial_root.mkdir`, `tuple`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_fixture_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_document`

**Signature**

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

Implements document according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `inventory` (`tuple[GpuExtractedFile, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_filenames` (`list[object] | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `written_filenames` (`tuple[str, ...]`; optional/default `(DEFAULT_PDF,)`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `GpuPlanningDocument(extraction=extraction, all_spatial_layers=(zoning.reference,), zoning=zoning, related_layers=())`.

**Algorithm**

1. Computes `inventory` from `tuple(sorted(inventory, key=lambda item: item.relative_path))`.
2. Computes `written` from `tuple((GpuWrittenFile(filename=value, title=None, document_path=None, source_url=None) for value in written_filenames))`.
3. Computes `metadata` from `GpuDocumentMetadata(provider="Géoportail de l'Urbanisme", portal='GPU', commune_code='31395', partition='DU_31395', document_id=DOCUMENT_ID, document_family='DU', document_type='PLU', document_title='Planning document', status='document.production', legal_status='APPROVED', effective_status='EN_VIGUEUR', version='10',…`.
4. Computes `archive` from `GpuArchiveDownload(document=metadata, download_timestamp='2026-08-12T12:00:00+00:00', filename='31395_PLU_20240215.zip', archive_format='zip', file_size=100, sha256=ARCHIVE_SHA, path=root.parent / 'source.zip', cache_hit=True)`.
5. Computes `marker` from `root / '.landscout-gpu-extraction.json'`.
6. Calls `marker.write_text(json.dumps({'schema_version': 2, 'archive_sha256': archive.sha256, 'files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in inventory]}, sort_keys=True), encoding='utf-8')` for its validation or side effect.
7. Computes `extraction` from `GpuExtraction(archive=archive, extraction_root=root, files=inventory, standard_models=('CNIG PLU v2017',), cache_hit=True)`.
8. Returns `GpuPlanningDocument(extraction=extraction, all_spatial_layers=(zoning.reference,), zoning=zoning, related_layers=())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuArchiveDownload`, `marker.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuArchiveDownload`, `GpuDocumentMetadata`, `GpuExtraction`, `GpuPlanningDocument`, `GpuWrittenFile`, `json.dumps`, `marker.write_text`, `sorted`, `tuple`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_fixture_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_fixture_document`

**Signature**

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

Implements fixture document according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `filename` (`str`; optional/default `DEFAULT_PDF`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_filenames` (`list[object] | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `written_filenames` (`tuple[str, ...] | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `inventory_filenames` (`tuple[str, ...] | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_format` (`str`; optional/default `'GPKG'`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_nomfic` (`bool`; optional/default `True`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `_document(root, tuple(inventory), zoning, zoning_filenames=zoning_filenames or [filename], written_filenames=(filename,) if written_filenames is None else written_filenames)`.

**Algorithm**

1. Computes `root` from `tmp_path / 'extraction'`.
2. Computes `inventory_names` from `(filename,) if inventory_filenames is None else inventory_filenames`.
3. Defines `inventory` with annotation `list[GpuExtractedFile]` from `[]`.
4. Iterates `(index, name)` over `enumerate(inventory_names)`. For each value: Computes `relative` from `f'written-{index}/{name}'`. Computes `path` from `root.joinpath(*relative.split('/'))`. Calls `path.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Executes 2 additional source-ordered statement(s).
5. Computes `(zoning, spatial_inventory)` from `_write_zoning_source(root, _zone_frame([filename] if zoning_filenames is None else zoning_filenames, include_nomfic=include_nomfic), source_format=source_format)`.
6. Calls `inventory.extend(spatial_inventory)` for its validation or side effect.
7. Returns `_document(root, tuple(inventory), zoning, zoning_filenames=zoning_filenames or [filename], written_filenames=(filename,) if written_filenames is None else written_filenames)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_write_zoning_source`, `path.parent.mkdir`, `path.write_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_document`, `_inventory_item`, `_write_zoning_source`, `_zone_frame`, `enumerate`, `inventory.append`, `inventory.extend`, `path.parent.mkdir`, `path.write_bytes`, `relative.split`, `root.joinpath`, `tuple`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_one_page_index`
- `tests/unit/test_index_planning_regulation.py` — `test_duplicate_inventory_basename_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_explicit_filename_not_referenced_by_zoning_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_explicit_source_validated_selection_succeeds`
- `tests/unit/test_index_planning_regulation.py` — `test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py` — `test_filename_absent_from_inventory_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_filename_absent_from_written_files_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py` — `test_malformed_source_metadata_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py` — `test_missing_nomfic_field_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_multiple_nomfic_values_are_ambiguous`
- `tests/unit/test_index_planning_regulation.py` — `test_mutated_loaded_nomfic_is_rejected_before_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_mutated_loaded_zoning_geometry_or_order_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_null_nomfic_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py` — `test_path_outside_root_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_pdf_inventory_integrity_mismatch_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_pdf_reader_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py` — `test_source_nomfic_resolves_generic_filename`
- `tests/unit/test_index_planning_regulation.py` — `test_unchanged_zoning_source_is_revalidated_before_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_unrelated_non_pdf_written_file_does_not_block_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_unsafe_explicit_filename_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_version_discovery_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py` — `test_zero_page_pdf_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_zoning_source_bytes_changed_after_ingestion_are_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_zoning_source_inventory_integrity_mismatch_is_rejected`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_duplicate_inventory_basename_fails`
- `tests/unit/test_index_planning_regulation.py::test_explicit_filename_not_referenced_by_zoning_fails`
- `tests/unit/test_index_planning_regulation.py::test_explicit_source_validated_selection_succeeds`
- `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_inventory_fails`
- `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_written_files_fails`
- `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py::test_malformed_source_metadata_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py::test_missing_nomfic_field_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_multiple_nomfic_values_are_ambiguous`
- `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_nomfic_is_rejected_before_selection`
- `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_zoning_geometry_or_order_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_null_nomfic_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py::test_path_outside_root_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_pdf_inventory_integrity_mismatch_fails`
- `tests/unit/test_index_planning_regulation.py::test_pdf_reader_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py::test_source_nomfic_resolves_generic_filename`
- `tests/unit/test_index_planning_regulation.py::test_unchanged_zoning_source_is_revalidated_before_selection`
- `tests/unit/test_index_planning_regulation.py::test_unrelated_non_pdf_written_file_does_not_block_selection`
- `tests/unit/test_index_planning_regulation.py::test_unsafe_explicit_filename_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py::test_zero_page_pdf_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_zoning_source_bytes_changed_after_ingestion_are_rejected`
- `tests/unit/test_index_planning_regulation.py::test_zoning_source_inventory_integrity_mismatch_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_one_page_index`

**Signature**

```python
def _one_page_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str = "Énergie",
):
```

**Purpose**

Implements one page index according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `text` (`str`; optional/default `'Énergie'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `index_planning_regulation(document)`.

**Algorithm**

1. Computes `document` from `_fixture_document(tmp_path)`.
2. Calls `_patch_reader(monkeypatch, [text])` for its validation or side effect.
3. Returns `index_planning_regulation(document)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_fixture_document`, `_patch_reader`, `index_planning_regulation`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_valid_search_result`
- `tests/unit/test_index_planning_regulation.py` — `test_complete_index_envelope_mutation_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_coordinated_page_mutation_fails_envelope_hash`
- `tests/unit/test_index_planning_regulation.py` — `test_duplicate_normalized_search_terms_are_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_empty_search_result_has_stable_schema_and_lineage`
- `tests/unit/test_index_planning_regulation.py` — `test_invalid_search_term_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_literal_search_does_not_add_semantic_synonyms`
- `tests/unit/test_index_planning_regulation.py` — `test_malformed_page_hash_schema_is_rejected_as_controlled_error`
- `tests/unit/test_index_planning_regulation.py` — `test_malformed_page_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py` — `test_raw_context_preserves_source_typography`
- `tests/unit/test_index_planning_regulation.py` — `test_unsupported_or_malformed_index_hash_schema_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_zero_context_preserves_complete_raw_unicode_span`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_complete_index_envelope_mutation_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_coordinated_page_mutation_fails_envelope_hash`
- `tests/unit/test_index_planning_regulation.py::test_duplicate_normalized_search_terms_are_rejected`
- `tests/unit/test_index_planning_regulation.py::test_empty_search_result_has_stable_schema_and_lineage`
- `tests/unit/test_index_planning_regulation.py::test_invalid_search_term_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_literal_search_does_not_add_semantic_synonyms`
- `tests/unit/test_index_planning_regulation.py::test_malformed_page_hash_schema_is_rejected_as_controlled_error`
- `tests/unit/test_index_planning_regulation.py::test_malformed_page_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py::test_raw_context_preserves_source_typography`
- `tests/unit/test_index_planning_regulation.py::test_unsupported_or_malformed_index_hash_schema_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_zero_context_preserves_complete_raw_unicode_span`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_pdf_reader_failure_is_controlled_and_chained.fail_reader`

**Signature**

```python
def fail_reader(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements fail reader according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `RuntimeError('broken xref')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `RuntimeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RuntimeError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_version_discovery_failure_is_controlled_and_chained.fail_version`

**Signature**

```python
def fail_version(name: str) -> str:
```

**Purpose**

Implements fail version according to the exact implementation and guards in this file.

**Inputs**

- `name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `RuntimeError(name)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `RuntimeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RuntimeError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_valid_search_result`

**Signature**

```python
def _valid_search_result(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
```

**Purpose**

Implements valid search result according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `(index, result)`.

**Algorithm**

1. Computes `index` from `_one_page_index(tmp_path, monkeypatch, 'Énergie énergie et Équipement d’intérêt collectif')`.
2. Computes `result` from `search_planning_regulation(index, ['energie', "equipement d'interet collectif"])`.
3. Returns `(index, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_one_page_index`, `search_planning_regulation`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `test_malformed_hit_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py` — `test_search_hit_lineage_mutation_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_search_index_identity_schema_and_terms_are_sealed`
- `tests/unit/test_index_planning_regulation.py` — `test_search_requested_terms_must_be_an_immutable_exact_tuple`
- `tests/unit/test_index_planning_regulation.py` — `test_search_result_envelope_is_valid_and_deterministic`
- `tests/unit/test_index_planning_regulation.py` — `test_search_result_integrity_mutations_fail`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_malformed_hit_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py::test_search_hit_lineage_mutation_fails`
- `tests/unit/test_index_planning_regulation.py::test_search_index_identity_schema_and_terms_are_sealed`
- `tests/unit/test_index_planning_regulation.py::test_search_requested_terms_must_be_an_immutable_exact_tuple`
- `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic`
- `tests/unit/test_index_planning_regulation.py::test_search_result_integrity_mutations_fail`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_immutable_models_and_validators`

**Signature**

```python
def test_public_api_exports_immutable_models_and_validators() -> None:
```

**Purpose**

Protects the `public api exports immutable models and validators` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `hasattr`.

**Expected result**

- Direct assertions: `assert name in stages.__all__`; `assert hasattr(stages, name)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public api exports immutable models and validators` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `hasattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_nomfic_resolves_generic_filename`

**Signature**

```python
def test_source_nomfic_resolves_generic_filename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    filename: str,
) -> None:
```

**Purpose**

Protects the `source nomfic resolves generic filename` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `filename`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, filename=filename)`.
- Computes `result` from `index_planning_regulation(document)`.

**Action**

- Calls `Path`, `_fixture_document`, `_patch_reader`, `index_planning_regulation`.

**Expected result**

- Direct assertions: `assert Path(result.pdf_relative_path).name == filename`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source nomfic resolves generic filename` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `_fixture_document`, `_patch_reader`, `index_planning_regulation`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_explicit_source_validated_selection_succeeds`

**Signature**

```python
def test_explicit_source_validated_selection_succeeds(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `explicit source validated selection succeeds` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `filenames` from `('a.pdf', 'b.pdf')`.
- Computes `document` from `_fixture_document(tmp_path, filename='a.pdf', zoning_filenames=list(filenames), written_filenames=filenames, inventory_filenames=filenames)`.
- Computes `result` from `index_planning_regulation(document, regulation_filename='b.pdf')`.

**Action**

- Calls `Path`, `_fixture_document`, `_patch_reader`, `index_planning_regulation`.

**Expected result**

- Direct assertions: `assert Path(result.pdf_relative_path).name == 'b.pdf'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `explicit source validated selection succeeds` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `_fixture_document`, `_patch_reader`, `index_planning_regulation`, `list`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unchanged_zoning_source_is_revalidated_before_selection`

**Signature**

```python
def test_unchanged_zoning_source_is_revalidated_before_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    source_format: str,
) -> None:
```

**Purpose**

Protects the `unchanged zoning source is revalidated before selection` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `source_format`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, source_format=source_format)`.
- Computes `result` from `index_planning_regulation(document)`.

**Action**

- Calls `_fixture_document`, `_patch_reader`, `fullmatch`, `index_planning_regulation`.

**Expected result**

- Direct assertions: `assert result.regulation_filename == DEFAULT_PDF`; `assert result.source_selection_method == 'ZONING_NOMFIC'`; `assert fullmatch('[0-9a-f]{64}', result.source_selection_sha256)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unchanged zoning source is revalidated before selection` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `_patch_reader`, `fullmatch`, `index_planning_regulation`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutated_loaded_nomfic_is_rejected_before_selection`

**Signature**

```python
def test_mutated_loaded_nomfic_is_rejected_before_selection(tmp_path: Path) -> None:
```

**Purpose**

Protects the `mutated loaded nomfic is rejected before selection` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `mutated` from `document.zoning.data.copy(deep=True)`.
- Computes `mutated.loc[0, 'NOMFIC']` from `'other_reglement.pdf'`.
- Computes `corrupted` from `replace(document, zoning=replace(document.zoning, data=mutated))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='zoning|source')` and executes: Calls `index_planning_regulation(corrupted)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `document.zoning.data.copy`, `index_planning_regulation`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='zoning|source'): index_planning_regulation(corrupted)`.

**Regression protected**

- Protects the exact `mutated loaded nomfic is rejected before selection` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `document.zoning.data.copy`, `index_planning_regulation`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutated_loaded_zoning_geometry_or_order_is_rejected`

**Signature**

```python
def test_mutated_loaded_zoning_geometry_or_order_is_rejected(
    tmp_path: Path,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `mutated loaded zoning geometry or order is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 4 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, zoning_filenames=[DEFAULT_PDF, DEFAULT_PDF])`.
- Computes `mutated` from `document.zoning.data.copy(deep=True)`.
- Computes `corrupted` from `replace(document, zoning=replace(document.zoning, data=mutated))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='zoning|source')` and executes: Calls `index_planning_regulation(corrupted)` for its validation or side effect.

**Action**

- Calls `Polygon`, `_fixture_document`, `document.zoning.data.copy`, `index_planning_regulation`, `mutated.geometry.copy`, `mutated.iloc[::-1].reset_index`, `mutated.set_geometry`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='zoning|source'): index_planning_regulation(corrupted)`.

**Regression protected**

- Protects the exact `mutated loaded zoning geometry or order is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_fixture_document`, `document.zoning.data.copy`, `index_planning_regulation`, `mutated.geometry.copy`, `mutated.iloc[::-1].reset_index`, `mutated.set_geometry`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zoning_source_bytes_changed_after_ingestion_are_rejected`

**Signature**

```python
def test_zoning_source_bytes_changed_after_ingestion_are_rejected(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `zoning source bytes changed after ingestion are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Enters managed context(s) `document.zoning.reference.dataset_path.open('ab')` and executes: Calls `stream.write(b'tamper')` for its validation or side effect.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='size|SHA256|integrity')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `document.zoning.reference.dataset_path.open`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='size|SHA256|integrity'): index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `zoning source bytes changed after ingestion are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `document.zoning.reference.dataset_path.open`, `index_planning_regulation`, `pytest.raises`, `stream.write`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zoning_source_inventory_integrity_mismatch_is_rejected`

**Signature**

```python
def test_zoning_source_inventory_integrity_mismatch_is_rejected(
    tmp_path: Path,
    field: str,
) -> None:
```

**Purpose**

Protects the `zoning source inventory integrity mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`.
- Contains 8 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `items` from `list(document.extraction.files)`.
- Computes `position` from `next((index for index, item in enumerate(items) if item.category == 'SPATIAL_DATA'))`.
- Computes `current` from `items[position]`.
- Defines `replacement` with annotation `object` from `current.size_bytes + 1 if field == 'size_bytes' else 'b' * 64`.
- Computes `items[position]` from `replace(current, **{field: replacement})`.
- Computes `corrupted` from `replace(document, extraction=replace(document.extraction, files=tuple(items)))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='size|SHA256|integrity')` and executes: Calls `index_planning_regulation(corrupted)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `enumerate`, `index_planning_regulation`, `next`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='size|SHA256|integrity'): index_planning_regulation(corrupted)`.

**Regression protected**

- Protects the exact `zoning source inventory integrity mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `enumerate`, `index_planning_regulation`, `list`, `next`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_nomfic_field_is_rejected`

**Signature**

```python
def test_missing_nomfic_field_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `missing nomfic field is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, include_nomfic=False)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='missing NOMFIC')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='missing NOMFIC'): index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `missing nomfic field is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_nomfic_is_rejected`

**Signature**

```python
def test_null_nomfic_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `null nomfic is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, zoning_filenames=[None])`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='no regulation filename')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='no regulation filename'): index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `null nomfic is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_multiple_nomfic_values_are_ambiguous`

**Signature**

```python
def test_multiple_nomfic_values_are_ambiguous(tmp_path: Path) -> None:
```

**Purpose**

Protects the `multiple nomfic values are ambiguous` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, filename='a.pdf', zoning_filenames=['a.pdf', 'b.pdf'], written_filenames=('a.pdf', 'b.pdf'), inventory_filenames=('a.pdf', 'b.pdf'))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='ambiguous')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='ambiguous'): index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `multiple nomfic values are ambiguous` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_explicit_filename_is_rejected`

**Signature**

```python
def test_unsafe_explicit_filename_is_rejected(tmp_path: Path, filename: str) -> None:
```

**Purpose**

Protects the `unsafe explicit filename is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `filename`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='filename')` and executes: Calls `index_planning_regulation(document, regulation_filename=filename)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='filename'): index_planning_regulation(document, regulation_filename=filename)`.

**Regression protected**

- Protects the exact `unsafe explicit filename is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_explicit_filename_not_referenced_by_zoning_fails`

**Signature**

```python
def test_explicit_filename_not_referenced_by_zoning_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `explicit filename not referenced by zoning fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='not referenced')` and executes: Calls `index_planning_regulation(document, regulation_filename='other.pdf')` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='not referenced'): index_planning_regulation(document, regulation_filename='other.pdf')`.

**Regression protected**

- Protects the exact `explicit filename not referenced by zoning fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_filename_absent_from_written_files_fails`

**Signature**

```python
def test_filename_absent_from_written_files_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `filename absent from written files fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, written_filenames=('other.pdf',))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='written_files')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='written_files'): index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `filename absent from written files fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unrelated_non_pdf_written_file_does_not_block_selection`

**Signature**

```python
def test_unrelated_non_pdf_written_file_does_not_block_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `unrelated non pdf written file does not block selection` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, written_filenames=(DEFAULT_PDF, 'technical-note.txt'))`.

**Action**

- Calls `_fixture_document`, `_patch_reader`, `index_planning_regulation`.

**Expected result**

- Direct assertions: `assert index_planning_regulation(document).total_page_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unrelated non pdf written file does not block selection` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `_patch_reader`, `index_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_filename_absent_from_inventory_fails`

**Signature**

```python
def test_filename_absent_from_inventory_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `filename absent from inventory fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `item_position` from `next((index for index, item in enumerate(document.extraction.files) if item.category == 'WRITTEN_REGULATION'))`.
- Computes `items` from `list(document.extraction.files)`.
- Computes `items[item_position]` from `replace(items[item_position], relative_path='written/other.pdf')`.
- Computes `corrupted` from `replace(document, extraction=replace(document.extraction, files=tuple(items)))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='missing from GPU inventory|verified manifest')` and executes: Calls `index_planning_regulation(corrupted)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `enumerate`, `index_planning_regulation`, `next`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='missing from GPU inventory|verified manifest'): index_planning_regulation(corrupted)`.

**Regression protected**

- Protects the exact `filename absent from inventory fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `enumerate`, `index_planning_regulation`, `list`, `next`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_inventory_basename_fails`

**Signature**

```python
def test_duplicate_inventory_basename_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate inventory basename fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path, inventory_filenames=(DEFAULT_PDF, DEFAULT_PDF))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='ambiguous')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='ambiguous'): index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `duplicate inventory basename fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_path_outside_root_is_rejected`

**Signature**

```python
def test_path_outside_root_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `path outside root is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `item` from `replace(document.extraction.files[0], relative_path=f'../{DEFAULT_PDF}')`.
- Computes `corrupted` from `replace(document, extraction=replace(document.extraction, files=(item,)))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='unsafe|verified manifest')` and executes: Calls `index_planning_regulation(corrupted)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='unsafe|verified manifest'): index_planning_regulation(corrupted)`.

**Regression protected**

- Protects the exact `path outside root is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_pdf_inventory_integrity_mismatch_fails`

**Signature**

```python
def test_pdf_inventory_integrity_mismatch_fails(tmp_path: Path, field: str) -> None:
```

**Purpose**

Protects the `pdf inventory integrity mismatch fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`.
- Contains 7 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Defines `value` with annotation `object` from `len(PDF_BYTES) + 1 if field == 'size_bytes' else 'b' * 64`.
- Computes `item_position` from `next((index for index, item in enumerate(document.extraction.files) if item.category == 'WRITTEN_REGULATION'))`.
- Computes `items` from `list(document.extraction.files)`.
- Computes `items[item_position]` from `replace(items[item_position], **{field: value})`.
- Computes `corrupted` from `replace(document, extraction=replace(document.extraction, files=tuple(items)))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='differs')` and executes: Calls `index_planning_regulation(corrupted)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `enumerate`, `index_planning_regulation`, `next`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='differs'): index_planning_regulation(corrupted)`.

**Regression protected**

- Protects the exact `pdf inventory integrity mismatch fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `enumerate`, `index_planning_regulation`, `len`, `list`, `next`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_page_states_numbering_and_hashes`

**Signature**

```python
def test_page_states_numbering_and_hashes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `page states numbering and hashes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `raw` from `'ÉNERGIE\n Batterie '`.
- Computes `result` from `index_planning_regulation(document)`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `result.total_page_count` from `9`.

**Action**

- Calls `RuntimeError`, `_fixture_document`, `_patch_reader`, `fullmatch`, `index_planning_regulation`, `result.pages.extraction_status.tolist`, `result.pages.page_content_sha256.str.fullmatch`, `result.pages.page_content_sha256.str.fullmatch('[0-9a-f]{64}').all`, `result.pages.page_number.tolist`, `validate_planning_regulation_index`.

**Expected result**

- Direct assertions: `assert tuple(result.pages.columns) == PAGE_COLUMNS`; `assert result.pages.page_number.tolist() == [1, 2, 3]`; `assert result.pages.extraction_status.tolist() == ['TEXT', 'EMPTY', 'ERROR']`; `assert result.pages.loc[0, 'raw_text'] == raw`; `assert result.pages.loc[0, 'normalized_search_text'] == 'energie batterie'`; `assert result.pages.page_content_sha256.str.fullmatch('[0-9a-f]{64}').all()`; `assert fullmatch('[0-9a-f]{64}', result.pages_content_sha256)`.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): result.total_page_count = 9`.

**Regression protected**

- Protects the exact `page states numbering and hashes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RuntimeError`, `_fixture_document`, `_patch_reader`, `fullmatch`, `index_planning_regulation`, `pytest.raises`, `result.pages.extraction_status.tolist`, `result.pages.page_content_sha256.str.fullmatch`, `result.pages.page_content_sha256.str.fullmatch('[0-9a-f]{64}').all`, `result.pages.page_number.tolist`, `tuple`, `validate_planning_regulation_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zero_page_pdf_is_rejected`

**Signature**

```python
def test_zero_page_pdf_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `zero page pdf is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='at least one page')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `_patch_reader`, `index_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='at least one page'): index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `zero page pdf is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `_patch_reader`, `index_planning_regulation`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_pdf_reader_failure_is_controlled_and_chained`

**Signature**

```python
def test_pdf_reader_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `pdf reader failure is controlled and chained` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='opened or parsed')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `RuntimeError`, `_fixture_document`, `index_planning_regulation`, `isinstance`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert isinstance(caught.value.__cause__, RuntimeError)`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='opened or parsed') as caught: index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `pdf reader failure is controlled and chained` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RuntimeError`, `_fixture_document`, `index_planning_regulation`, `isinstance`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_french_literal_normalization`

**Signature**

```python
def test_french_literal_normalization(source: str, term: str) -> None:
```

**Purpose**

Protects the `french literal normalization` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `source`, `term`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_normalize_search_text`.

**Expected result**

- Direct assertions: `assert _normalize_search_text(source) == term`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `french literal normalization` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_normalize_search_text`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_raw_context_preserves_source_typography`

**Signature**

```python
def test_raw_context_preserves_source_typography(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `raw context preserves source typography` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `raw` from `'Le projet vise un Équipement d’intérêt collectif dans la zone.'`.
- Computes `index` from `_one_page_index(tmp_path, monkeypatch, raw)`.
- Computes `result` from `search_planning_regulation(index, ["equipement d'interet collectif"], context_characters=4)`.
- Computes `hit` from `result.hits.iloc[0]`.

**Action**

- Calls `_one_page_index`, `search_planning_regulation`.

**Expected result**

- Direct assertions: `assert hit['page_number'] == 1`; `assert hit['occurrence_count'] == 1`; `assert 'Équipement d’intérêt collectif' in hit['raw_context']`; `assert "equipement d'interet collectif" in hit['normalized_context']`; `assert index.pages.iloc[0]['raw_text'] == raw`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `raw context preserves source typography` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `search_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zero_context_preserves_complete_raw_unicode_span`

**Signature**

```python
def test_zero_context_preserves_complete_raw_unicode_span(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    raw: str,
    term: str,
    expected_raw: str,
    expected_normalized: str,
) -> None:
```

**Purpose**

Protects the `zero context preserves complete raw unicode span` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `raw`, `term`, `expected_raw`, `expected_normalized`.
- Contains 3 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch, raw)`.
- Computes `result` from `search_planning_regulation(index, [term], context_characters=0)`.
- Computes `hit` from `result.hits.iloc[0]`.

**Action**

- Calls `_one_page_index`, `search_planning_regulation`.

**Expected result**

- Direct assertions: `assert hit['raw_context'] == expected_raw`; `assert hit['normalized_context'] == expected_normalized`; `assert hit['raw_context'] in raw`; `assert index.pages.iloc[0]['raw_text'] == raw`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `zero context preserves complete raw unicode span` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `pytest.mark.parametrize`, `search_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_literal_search_does_not_add_semantic_synonyms`

**Signature**

```python
def test_literal_search_does_not_add_semantic_synonyms(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `literal search does not add semantic synonyms` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch, 'Une batterie est mentionnée.')`.
- Computes `result` from `search_planning_regulation(index, ['accumulateur'])`.

**Action**

- Calls `_one_page_index`, `search_planning_regulation`.

**Expected result**

- Direct assertions: `assert result.hits.empty`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `literal search does not add semantic synonyms` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `search_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_version_discovery_failure_is_controlled_and_chained`

**Signature**

```python
def test_version_discovery_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `version discovery failure is controlled and chained` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='version')` and executes: Calls `index_planning_regulation(document)` for its validation or side effect.

**Action**

- Calls `RuntimeError`, `_fixture_document`, `_patch_reader`, `index_planning_regulation`, `isinstance`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert isinstance(caught.value.__cause__, RuntimeError)`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='version') as caught: index_planning_regulation(document)`.

**Regression protected**

- Protects the exact `version discovery failure is controlled and chained` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `RuntimeError`, `_fixture_document`, `_patch_reader`, `index_planning_regulation`, `isinstance`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_page_mutation_fails_envelope_hash`

**Signature**

```python
def test_coordinated_page_mutation_fails_envelope_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `coordinated page mutation fails envelope hash` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 8 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch)`.
- Computes `pages` from `index.pages.copy(deep=True)`.
- Computes `pages.loc[0, 'raw_text']` from `'Nouveau'`.
- Computes `pages.loc[0, 'normalized_search_text']` from `'nouveau'`.
- Computes `pages.loc[0, 'character_count']` from `7`.
- Computes `row` from `pages.iloc[0].to_dict()`.
- Computes `pages.loc[0, 'page_content_sha256']` from `regulation_module._page_content_sha256(row)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='envelope')` and executes: Calls `validate_planning_regulation_index(replace(index, pages=pages))` for its validation or side effect.

**Action**

- Calls `_one_page_index`, `index.pages.copy`, `pages.iloc[0].to_dict`, `regulation_module._page_content_sha256`, `replace`, `validate_planning_regulation_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='envelope'): validate_planning_regulation_index(replace(index, pages=pages))`.

**Regression protected**

- Protects the exact `coordinated page mutation fails envelope hash` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `index.pages.copy`, `pages.iloc[0].to_dict`, `pytest.raises`, `regulation_module._page_content_sha256`, `replace`, `validate_planning_regulation_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_index_integrity_mutations_fail`

**Signature**

```python
def test_index_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `index integrity mutations fail` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `target`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `index` from `index_planning_regulation(document)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_index(corrupted)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `_patch_reader`, `index.pages.copy`, `index.pages.iloc[::-1].reset_index`, `index_planning_regulation`, `replace`, `validate_planning_regulation_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_index(corrupted)`.

**Regression protected**

- Protects the exact `index integrity mutations fail` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `_patch_reader`, `index.pages.copy`, `index.pages.iloc[::-1].reset_index`, `index_planning_regulation`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `validate_planning_regulation_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_index_envelope_mutation_is_rejected`

**Signature**

```python
def test_complete_index_envelope_mutation_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
```

**Purpose**

Protects the `complete index envelope mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `field`, `replacement`.
- Contains 2 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_index(replace(index, **{field: replacement}))` for its validation or side effect.

**Action**

- Calls `_one_page_index`, `replace`, `validate_planning_regulation_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_index(replace(index, **{field: replacement}))`.

**Regression protected**

- Protects the exact `complete index envelope mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `len`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `validate_planning_regulation_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsupported_or_malformed_index_hash_schema_is_rejected`

**Signature**

```python
def test_unsupported_or_malformed_index_hash_schema_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
```

**Purpose**

Protects the `unsupported or malformed index hash schema is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `replacement`.
- Contains 2 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_index(replace(index, index_hash_schema_version=replacement))` for its validation or side effect.

**Action**

- Calls `_one_page_index`, `replace`, `validate_planning_regulation_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_index(replace(index, index_hash_schema_version=replacement))`.

**Regression protected**

- Protects the exact `unsupported or malformed index hash schema is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `validate_planning_regulation_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_page_hash_schema_is_rejected_as_controlled_error`

**Signature**

```python
def test_malformed_page_hash_schema_is_rejected_as_controlled_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
```

**Purpose**

Protects the `malformed page hash schema is rejected as controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `replacement`.
- Contains 2 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_index(replace(index, page_hash_schema_version=replacement))` for its validation or side effect.

**Action**

- Calls `_one_page_index`, `replace`, `validate_planning_regulation_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_index(replace(index, page_hash_schema_version=replacement))`.

**Regression protected**

- Protects the exact `malformed page hash schema is rejected as controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `validate_planning_regulation_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_search_result_envelope_is_valid_and_deterministic`

**Signature**

```python
def test_search_result_envelope_is_valid_and_deterministic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `search result envelope is valid and deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, first)` from `_valid_search_result(tmp_path, monkeypatch)`.
- Computes `second` from `search_planning_regulation(index, first.requested_terms)`.

**Action**

- Calls `_valid_search_result`, `search_planning_regulation`, `validate_planning_regulation_search_result`.

**Expected result**

- Direct assertions: `assert tuple(first.hits.columns) == SEARCH_HIT_COLUMNS`; `assert first.search_normalization_profile == SEARCH_NORMALIZATION_PROFILE`; `assert first.index_content_sha256 == index.index_content_sha256`; `assert first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION`; `assert first.hit_count == 2`; `assert first.hits_content_sha256 == second.hits_content_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `search result envelope is valid and deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_valid_search_result`, `assert_frame_equal`, `search_planning_regulation`, `tuple`, `validate_planning_regulation_search_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_search_index_identity_schema_and_terms_are_sealed`

**Signature**

```python
def test_search_index_identity_schema_and_terms_are_sealed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
```

**Purpose**

Protects the `search index identity schema and terms are sealed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `field`, `replacement`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, result)` from `_valid_search_result(tmp_path, monkeypatch)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_search_result(index, replace(result, **{field: replacement}))` for its validation or side effect.

**Action**

- Calls `_valid_search_result`, `replace`, `validate_planning_regulation_search_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_search_result(index, replace(result, **{field: replacement}))`.

**Regression protected**

- Protects the exact `search index identity schema and terms are sealed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_valid_search_result`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `validate_planning_regulation_search_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_search_requested_terms_must_be_an_immutable_exact_tuple`

**Signature**

```python
def test_search_requested_terms_must_be_an_immutable_exact_tuple(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `search requested terms must be an immutable exact tuple` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `(index, result)` from `_valid_search_result(tmp_path, monkeypatch)`.
- Computes `corrupted` from `replace(result, requested_terms=list(result.requested_terms))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='tuple')` and executes: Calls `validate_planning_regulation_search_result(index, corrupted)` for its validation or side effect.

**Action**

- Calls `_valid_search_result`, `replace`, `validate_planning_regulation_search_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='tuple'): validate_planning_regulation_search_result(index, corrupted)`.

**Regression protected**

- Protects the exact `search requested terms must be an immutable exact tuple` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_valid_search_result`, `list`, `pytest.raises`, `replace`, `validate_planning_regulation_search_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_search_result_integrity_mutations_fail`

**Signature**

```python
def test_search_result_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `search result integrity mutations fail` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `target`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, result)` from `_valid_search_result(tmp_path, monkeypatch)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_search_result(index, corrupted)` for its validation or side effect.

**Action**

- Calls `_valid_search_result`, `hits[target].astype`, `pd.concat`, `replace`, `result.hits.copy`, `validate_planning_regulation_search_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_search_result(index, corrupted)`.

**Regression protected**

- Protects the exact `search result integrity mutations fail` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_valid_search_result`, `hits[target].astype`, `len`, `pd.concat`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.hits.copy`, `validate_planning_regulation_search_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_search_hit_lineage_mutation_fails`

**Signature**

```python
def test_search_hit_lineage_mutation_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    column: str,
) -> None:
```

**Purpose**

Protects the `search hit lineage mutation fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `column`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, result)` from `_valid_search_result(tmp_path, monkeypatch)`.
- Computes `hits` from `result.hits.copy(deep=True)`.
- Computes `hits.loc[0, column]` from `'b' * 64 if column == 'pdf_sha256' else 'wrong'`.
- Computes `corrupted` from `replace(result, hits=hits)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='lineage')` and executes: Calls `validate_planning_regulation_search_result(index, corrupted)` for its validation or side effect.

**Action**

- Calls `_valid_search_result`, `replace`, `result.hits.copy`, `validate_planning_regulation_search_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='lineage'): validate_planning_regulation_search_result(index, corrupted)`.

**Regression protected**

- Protects the exact `search hit lineage mutation fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_valid_search_result`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.hits.copy`, `validate_planning_regulation_search_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_search_term_is_rejected`

**Signature**

```python
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
```

**Purpose**

Protects the `invalid search term is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `term`.
- Contains 2 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='search term')` and executes: Calls `search_planning_regulation(index, [term])` for its validation or side effect.

**Action**

- Calls `_one_page_index`, `search_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='search term'): search_planning_regulation(index, [term])`.

**Regression protected**

- Protects the exact `invalid search term is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `pytest.mark.parametrize`, `pytest.raises`, `search_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_normalized_search_terms_are_rejected`

**Signature**

```python
def test_duplicate_normalized_search_terms_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `duplicate normalized search terms are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='unique')` and executes: Calls `search_planning_regulation(index, ['énergie', 'ENERGIE'])` for its validation or side effect.

**Action**

- Calls `_one_page_index`, `search_planning_regulation`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='unique'): search_planning_regulation(index, ['énergie', 'ENERGIE'])`.

**Regression protected**

- Protects the exact `duplicate normalized search terms are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `pytest.raises`, `search_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_empty_search_result_has_stable_schema_and_lineage`

**Signature**

```python
def test_empty_search_result_has_stable_schema_and_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `empty search result has stable schema and lineage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch, 'Aucun terme')`.
- Computes `result` from `search_planning_regulation(index, ['batterie'])`.

**Action**

- Calls `_one_page_index`, `search_planning_regulation`, `validate_planning_regulation_search_result`.

**Expected result**

- Direct assertions: `assert result.hit_count == 0`; `assert result.hits.empty`; `assert tuple(result.hits.columns) == SEARCH_HIT_COLUMNS`; `assert result.document_id == index.document_id`; `assert result.pdf_sha256 == index.pdf_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `empty search result has stable schema and lineage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `search_planning_regulation`, `tuple`, `validate_planning_regulation_search_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_page_value_raises_controlled_index_error`

**Signature**

```python
def test_malformed_page_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `malformed page value raises controlled index error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_one_page_index(tmp_path, monkeypatch)`.
- Computes `pages` from `index.pages.copy(deep=True)`.
- Computes `pages.at[0, 'extraction_error']` from `['ambiguous', 'value']`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_index(replace(index, pages=pages))` for its validation or side effect.

**Action**

- Calls `_one_page_index`, `index.pages.copy`, `replace`, `validate_planning_regulation_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_index(replace(index, pages=pages))`.

**Regression protected**

- Protects the exact `malformed page value raises controlled index error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_one_page_index`, `index.pages.copy`, `pytest.raises`, `replace`, `validate_planning_regulation_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_hit_value_raises_controlled_index_error`

**Signature**

```python
def test_malformed_hit_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `malformed hit value raises controlled index error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, result)` from `_valid_search_result(tmp_path, monkeypatch)`.
- Computes `hits` from `result.hits.copy(deep=True)`.
- Computes `hits['raw_context']` from `hits['raw_context'].astype(object)`.
- Computes `hits.at[0, 'raw_context']` from `['not', 'text']`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `validate_planning_regulation_search_result(index, replace(result, hits=hits))` for its validation or side effect.

**Action**

- Calls `_valid_search_result`, `hits['raw_context'].astype`, `replace`, `result.hits.copy`, `validate_planning_regulation_search_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): validate_planning_regulation_search_result(index, replace(result, hits=hits))`.

**Regression protected**

- Protects the exact `malformed hit value raises controlled index error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_valid_search_result`, `hits['raw_context'].astype`, `pytest.raises`, `replace`, `result.hits.copy`, `validate_planning_regulation_search_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_canonical_hash_serialization_failure_is_controlled_and_chained`

**Signature**

```python
def test_canonical_hash_serialization_failure_is_controlled_and_chained() -> None:
```

**Purpose**

Protects the `canonical hash serialization failure is controlled and chained` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `invalid_payload` from `{'not_json': object()}`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError, match='serialized')` and executes: Calls `regulation_module._canonical_sha256(invalid_payload)` for its validation or side effect.

**Action**

- Calls `isinstance`, `object`, `regulation_module._canonical_sha256`.

**Expected result**

- Direct assertions: `assert isinstance(caught.value.__cause__, TypeError)`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError, match='serialized') as caught: regulation_module._canonical_sha256(invalid_payload)`.

**Regression protected**

- Protects the exact `canonical hash serialization failure is controlled and chained` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `isinstance`, `object`, `pytest.raises`, `regulation_module._canonical_sha256`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_source_metadata_raises_controlled_index_error`

**Signature**

```python
def test_malformed_source_metadata_raises_controlled_index_error(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `malformed source metadata raises controlled index error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `metadata` from `replace(document.extraction.archive.document, written_files=(object(),))`.
- Computes `archive` from `replace(document.extraction.archive, document=metadata)`.
- Computes `corrupted` from `replace(document, extraction=replace(document.extraction, archive=archive))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationIndexError)` and executes: Calls `index_planning_regulation(corrupted)` for its validation or side effect.

**Action**

- Calls `_fixture_document`, `index_planning_regulation`, `object`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationIndexError): index_planning_regulation(corrupted)`.

**Regression protected**

- Protects the exact `malformed source metadata raises controlled index error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `index_planning_regulation`, `object`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_and_search_do_not_mutate_inputs`

**Signature**

```python
def test_extraction_and_search_do_not_mutate_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `extraction and search do not mutate inputs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `document` from `_fixture_document(tmp_path)`.
- Computes `extraction_before` from `deepcopy(document.extraction)`.
- Computes `zoning_before` from `document.zoning.data.copy(deep=True)`.
- Computes `index` from `index_planning_regulation(document)`.
- Computes `pages_before` from `index.pages.copy(deep=True)`.

**Action**

- Calls `_fixture_document`, `_patch_reader`, `deepcopy`, `document.zoning.data.copy`, `index.pages.copy`, `index_planning_regulation`, `search_planning_regulation`.

**Expected result**

- Direct assertions: `assert document.extraction == extraction_before`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `extraction and search do not mutate inputs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_fixture_document`, `_patch_reader`, `assert_frame_equal`, `assert_geodataframe_equal`, `deepcopy`, `document.zoning.data.copy`, `index.pages.copy`, `index_planning_regulation`, `search_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `NOMFIC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `character_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `extraction_error` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_context` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_search_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `occurrence_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `page_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `page_number` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `raw_context` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `raw_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
