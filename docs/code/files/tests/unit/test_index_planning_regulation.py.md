# `tests/unit/test_index_planning_regulation.py`

## File identity

- Repository path: `tests/unit/test_index_planning_regulation.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Exercises source-referenced PDF selection with physical synthetic zoning files, mocked page extraction, canonical index/search tampering, Unicode contexts, controlled failures, and successful-path input preservation.
- Source SHA256: `e36baad245c33bef983f78bb49fc8060bc4e45152c420c5d658f2853d742df8b`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for index planning regulation; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Exercises source-referenced PDF selection with physical synthetic zoning files, mocked page extraction, canonical index/search tampering, Unicode contexts, controlled failures, and successful-path input preservation.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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
- `from urllib.parse import quote`

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
- `from landscout.sources import gpu_fr as gpu_source_module`
- `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `regulation_module`

- Category: module-level alias/value.
- Exact declaration:

```python
regulation_module = import_module("landscout.stages.index_planning_regulation")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DOCUMENT_ID`

- Category: module constant or closed domain.
- Exact declaration:

```python
DOCUMENT_ID = "doc-1"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARCHIVE_SHA`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_SHA = "a" * 64
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEFAULT_PDF`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_PDF = "31395_reglement_20240215.pdf"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PDF_BYTES`

- Category: module constant or closed domain.
- Exact declaration:

```python
PDF_BYTES = b"synthetic-pdf-bytes"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.



### Verified fixture and assertion scope

This file declares 45 test functions representing 114 parametrized cases (16 parametrized definitions), plus 15 helpers/methods/callbacks, two mutable fake classes, and three instance fields. These are static declaration counts, not a report of test execution.

The fixture writes genuine temporary GPKG or Shapefile zoning datasets, rereads them through Pyogrio, and computes physical file inventories. PDF filenames refer to the fixed non-PDF bytes `b"synthetic-pdf-bytes"`; successful extraction is supplied by `_FakeReader`. A schema-2 extraction marker is written, but source.zip is only a fabricated download descriptor (size 100, a*64) and is never created. Thus this file is not full archive-acquisition, real pypdf parsing, or network-safety evidence. The separate integration test provides a different real-PDF chain.

Every `pytest.raises` expectation, parametrized value, and direct/assertion-helper check is described under its callable. Broad expected-message alternatives are not attributed to a later guard when an earlier manifest check can satisfy them. Mutation tests usually retain a stale enclosing hash; they do not claim resistance to coordinated replacement of every hash without an external source lock. The page-state test checks frozen attribute assignment, not deep immutability of pandas tables.

| Declaration | Actual role and consumers |
|---|---|
| `regulation_module` | Literal `import_module("landscout.stages.index_planning_regulation")` owner for PdfReader/version monkeypatches and private hash helper/schema references. |
| `DOCUMENT_ID` | Synthetic doc-1 identity used by metadata and geometry summaries. |
| `ARCHIVE_SHA` | Fabricated a*64 archive identity in metadata/manifest, not the computed hash of an existing ZIP. |
| `DEFAULT_PDF` | Default source-referenced fixture basename; the generic-name test also uses an unrelated name. |
| `PDF_BYTES` | Synthetic byte payload written as .pdf fixture files and hashed by inventory helpers; not parsed as a real PDF. |

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_FakePage`

**Source purpose:** Mutable page test double that returns a stored object or raises a stored exception. It does not read PDF bytes.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration | Meaning |
|---|---|---|---|---|
| `result` | `assigned instance field` | `result` | `self.result = result` | Stored caller-supplied return object or exception, retained by reference. |

These fields belong to mutable test doubles, not production integrity evidence.

**Qualified consumers**

- constructor call: `tests.unit.test_index_planning_regulation::_FakeReader.__init__` via `_FakePage`
- value/type reference: `tests.unit.test_index_planning_regulation::_FakeReader.__init__` via `_FakePage`

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

**Source purpose:** Mutable reader test double exposing a newly built list of `_FakePage` objects and an encryption flag. Used by `_patch_reader` through its captured lambda; no actual PDF parser is invoked.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration | Meaning |
|---|---|---|---|---|
| `pages` | `assigned instance field` | `[_FakePage(page) for page in pages]` | `self.pages = [_FakePage(page) for page in pages]` | Newly allocated mutable page-double list; each page stores its supplied result object. |
| `is_encrypted` | `assigned instance field` | `encrypted` | `self.is_encrypted = encrypted` | Supplied fake-reader flag; default false. No test in this file passes true. |

These fields belong to mutable test doubles, not production integrity evidence.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _FakeReader:
    def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
        self.pages = [_FakePage(page) for page in pages]
        self.is_encrypted = encrypted
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_FakePage.__init__`

**Purpose:** Store the supplied object as mutable `self.result` without copying or validation; the fake reader creates these page doubles. This fixture state is not an immutable production model.

**Exact signature**

```python
def __init__(self, result: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | no annotation | `required` |
| `result` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

**Effects and limits**

Store the supplied object as mutable `self.result` without copying or validation; the fake reader creates these page doubles. This fixture state is not an immutable production model.

**Complete source-ordered implementation**

```python
def __init__(self, result: object) -> None:
        self.result = result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakePage.extract_text`

**Purpose:** Raise the stored object when it is an Exception, otherwise return it unchanged. This simulates page text/None/nontext or extraction failure; it does not parse a PDF or write anything.

**Exact signature**

```python
def extract_text(self) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | no annotation | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self.result`
- Explicit raise paths:
  - `self.result` under lexical guard `isinstance(self.result, Exception)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Raise the stored object when it is an Exception, otherwise return it unchanged. This simulates page text/None/nontext or extraction failure; it does not parse a PDF or write anything.

**Complete source-ordered implementation**

```python
def extract_text(self) -> object:
        if isinstance(self.result, Exception):
            raise self.result
        return self.result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeReader.__init__`

**Purpose:** Create a new mutable list of `_FakePage` wrappers for the supplied page-result objects and retain the encryption flag. It exposes the two properties used by indexing; no PDF bytes are interpreted.

**Exact signature**

```python
def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | no annotation | `required` |
| `pages` | positional-or-keyword | `list[object]` | `required` |
| `encrypted` | keyword-only | `bool` | `False` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_FakePage` | `tests.unit.test_index_planning_regulation._FakePage` |

**Effects and limits**

Create a new mutable list of `_FakePage` wrappers for the supplied page-result objects and retain the encryption flag. It exposes the two properties used by indexing; no PDF bytes are interpreted.

**Complete source-ordered implementation**

```python
def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
        self.pages = [_FakePage(page) for page in pages]
        self.is_encrypted = encrypted
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_patch_reader`

**Purpose:** Monkeypatch the stage module's `PdfReader` name to a lambda that ignores reader arguments and returns `_FakeReader` with captured pages/encryption. The fixture reads physical synthetic file bytes for integrity but bypasses pypdf parsing; monkeypatch restores the binding after the test.

**Exact signature**

```python
def _patch_reader(
    monkeypatch: pytest.MonkeyPatch,
    pages: list[object],
    *,
    encrypted: bool = False,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `pages` | positional-or-keyword | `list[object]` | `required` |
| `encrypted` | keyword-only | `bool` | `False` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_one_page_index` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::_one_page_index` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_source_nomfic_resolves_generic_filename` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_source_nomfic_resolves_generic_filename` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_explicit_source_validated_selection_succeeds` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_explicit_source_validated_selection_succeeds` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_unchanged_zoning_source_is_revalidated_before_selection` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unchanged_zoning_source_is_revalidated_before_selection` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_unrelated_non_pdf_written_file_does_not_block_selection` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unrelated_non_pdf_written_file_does_not_block_selection` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_zero_page_pdf_is_rejected` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zero_page_pdf_is_rejected` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_version_discovery_failure_is_controlled_and_chained` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_version_discovery_failure_is_controlled_and_chained` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `_patch_reader`
- direct call: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `_patch_reader`
- value/type reference: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `_patch_reader`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Monkeypatch the stage module's `PdfReader` name to a lambda that ignores reader arguments and returns `_FakeReader` with captured pages/encryption. The fixture reads physical synthetic file bytes for integrity but bypasses pypdf parsing; monkeypatch restores the binding after the test.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_summary`

**Purpose:** Construct a GPU summary from the supplied synthetic frame: ordered columns/dtypes/null counts, geometry type counts, null/empty/nonempty-invalid counts, row count, and fixed document/archive/EPSG:2154 lineage. It measures in-memory fixture geometry, not physical archive authenticity.

**Exact signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    source_layer: str = "ZONE",
) -> GpuLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `GpuLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `source_layer` | keyword-only | `str` | `'ZONE'` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuLayerSummary(<br>        source_document_id=DOCUMENT_ID,<br>        source_archive_sha256=ARCHIVE_SHA,<br>        source_layer=source_layer,<br>        crs="EPSG:2154",<br>        feature_count=len(frame),<br>        columns=tuple(str(column) for column in frame.columns),<br>        dtypes=tuple(<br>            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()<br>        ),<br>        null_counts=tuple(<br>            (str(column), int(frame[column].isna().sum())) for column in frame.columns<br>        ),<br>        geometry_types=tuple(<br>            (str(key), int(value))<br>            for key, value in geometry.geom_type.value_counts().sort_index().items()<br>        ),<br>        null_geometry_count=int((~non_null).sum()),<br>        empty_geometry_count=int((non_null & geometry.is_empty).sum()),<br>        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `_summary`
- value/type reference: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuLayerSummary` | `landscout.sources.gpu_fr.GpuLayerSummary` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index().items` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~non_null).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null & geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_empty & ~geometry.is_valid).sum` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Construct a GPU summary from the supplied synthetic frame: ordered columns/dtypes/null counts, geometry type counts, null/empty/nonempty-invalid counts, row count, and fixed document/archive/EPSG:2154 lineage. It measures in-memory fixture geometry, not physical archive authenticity.

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
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_zone_frame`

**Purpose:** Build adjacent unit-square Polygons in EPSG:2154, one per requested filename, with sequential LIB_IDZONE identifiers and optionally NOMFIC. Default None creates one default filename; an explicitly empty filename list creates no rows. Only temporary attributes/geometries are allocated.

**Exact signature**

```python
def _zone_frame(
    nomfic: list[object] | None = None,
    *,
    include_nomfic: bool = True,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `nomfic` | positional-or-keyword | `list[object] \| None` | `None` |
| `include_nomfic` | keyword-only | `bool` | `True` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        attributes,<br>        geometry=[<br>            Polygon(<br>                [<br>                    (index, 0),<br>                    (index, 1),<br>                    (index + 1, 1),<br>                    (index + 1, 0),<br>                    (index, 0),<br>                ]<br>            )<br>            for index in range(count)<br>        ],<br>        crs="EPSG:2154",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_fixture_document` via `_zone_frame`
- value/type reference: `tests.unit.test_index_planning_regulation::_fixture_document` via `_zone_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |

**Effects and limits**

Build adjacent unit-square Polygons in EPSG:2154, one per requested filename, with sequential LIB_IDZONE identifiers and optionally NOMFIC. Default None creates one default filename; an explicitly empty filename list creates no rows. Only temporary attributes/geometries are allocated.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_inventory_item`

**Purpose:** Compute size and SHA256 of supplied fixture bytes and return a PDF/WRITTEN_REGULATION inventory record for the requested relative path. It hashes memory and does not create the file.

**Exact signature**

```python
def _inventory_item(relative_path: str, data: bytes = PDF_BYTES) -> GpuExtractedFile:
```

- Exact decorators: none.
- Declared return annotation: `GpuExtractedFile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relative_path` | positional-or-keyword | `str` | `required` |
| `data` | positional-or-keyword | `bytes` | `PDF_BYTES` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuExtractedFile(<br>        relative_path=relative_path,<br>        file_type="pdf",<br>        size_bytes=len(data),<br>        sha256=sha256(data).hexdigest(),<br>        category="WRITTEN_REGULATION",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_fixture_document` via `_inventory_item`
- value/type reference: `tests.unit.test_index_planning_regulation::_fixture_document` via `_inventory_item`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `GpuExtractedFile` | `landscout.sources.gpu_fr.GpuExtractedFile` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(data).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Effects and limits**

Compute size and SHA256 of supplied fixture bytes and return a PDF/WRITTEN_REGULATION inventory record for the requested relative path. It hashes memory and does not create the file.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_spatial_inventory_item`

**Purpose:** Read an existing temporary spatial file's bytes, hash them, and record its root-relative POSIX path, lowercase suffix or binary fallback, size, and SPATIAL_DATA category. This is a local file read, not remote acquisition.

**Exact signature**

```python
def _spatial_inventory_item(root: Path, path: Path) -> GpuExtractedFile:
```

- Exact decorators: none.
- Declared return annotation: `GpuExtractedFile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuExtractedFile(<br>        relative_path=path.relative_to(root).as_posix(),<br>        file_type=path.suffix.lower().lstrip(".") or "binary",<br>        size_bytes=len(data),<br>        sha256=sha256(data).hexdigest(),<br>        category="SPATIAL_DATA",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `_spatial_inventory_item`
- value/type reference: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `_spatial_inventory_item`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuExtractedFile` | `landscout.sources.gpu_fr.GpuExtractedFile` |
| `path.relative_to(root).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.lower().lstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.lower` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(data).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Effects and limits**

Read an existing temporary spatial file's bytes, hash them, and record its root-relative POSIX path, lowercase suffix or binary fallback, size, and SPATIAL_DATA category. This is a local file read, not remote acquisition.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_zoning_source`

**Purpose:** Create temporary spatial directories, write the provided frame as real GPKG ZONE or ESRI Shapefile ZONE, then reread it through Pyogrio. For Shapefile, inventory all existing same-stem files in sorted path order. Return a retained inspected layer with fresh summary plus byte-hashed inventory; unsupported fixture formats raise AssertionError. The to_file calls are actual filesystem writes.

**Exact signature**

```python
def _write_zoning_source(
    root: Path,
    frame: gpd.GeoDataFrame,
    *,
    source_format: str,
) -> tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `source_format` | keyword-only | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `layer, inventory`
- Explicit raise paths:
  - `AssertionError(f"Unsupported test source format: {source_format}")` in the final else branch, when the format is neither GPKG nor ESRI Shapefile.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_fixture_document` via `_write_zoning_source`
- value/type reference: `tests.unit.test_index_planning_regulation::_fixture_document` via `_write_zoning_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `spatial_root.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.parent.glob` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidate.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |
| `_summary` | `tests.unit.test_index_planning_regulation._summary` |
| `_spatial_inventory_item` | `tests.unit.test_index_planning_regulation._spatial_inventory_item` |

**Effects and limits**

Create temporary spatial directories, write the provided frame as real GPKG ZONE or ESRI Shapefile ZONE, then reread it through Pyogrio. For Shapefile, inventory all existing same-stem files in sorted path order. Return a retained inspected layer with fresh summary plus byte-hashed inventory; unsupported fixture formats raise AssertionError. The to_file calls are actual filesystem writes.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_document`

**Purpose:** Sort the inventory, load the checked-in GPU YAML, construct synthetic DU/PLU metadata and config-derived quoted written-file URLs, and write a schema-2 extraction manifest. Revalidate a dumped config with zoning match_tokens set to ZONE, hash that config, and assemble a retained source-bound document. The archive descriptor is fabricated with a*64, size 100, and source.zip path; no ZIP is written. The `zoning_filenames` parameter is accepted but unused in this helper.

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

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `inventory` | positional-or-keyword | `tuple[GpuExtractedFile, ...]` | `required` |
| `zoning` | positional-or-keyword | `GpuInspectedLayer` | `required` |
| `zoning_filenames` | keyword-only | `list[object] \| None` | `None` |
| `written_filenames` | keyword-only | `tuple[str, ...]` | `(DEFAULT_PDF,)` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuPlanningDocument(<br>        source_config=source_config,<br>        source_config_sha256=gpu_source_module._source_config_sha256(source_config),<br>        extraction=extraction,<br>        all_spatial_layers=(zoning.reference,),<br>        zoning=zoning,<br>        related_layers=(),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_fixture_document` via `_document`
- value/type reference: `tests.unit.test_index_planning_regulation::_fixture_document` via `_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `Path` | `pathlib.Path` |
| `GpuWrittenFile` | `landscout.sources.gpu_fr.GpuWrittenFile` |
| `str(base_config.api.base_url).rstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `quote` | `urllib.parse.quote` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `marker.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `GpuExtraction` | `landscout.sources.gpu_fr.GpuExtraction` |
| `base_config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `GpuPlanningDocument` | `landscout.sources.gpu_fr.GpuPlanningDocument` |
| `gpu_source_module._source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |

**Effects and limits**

Sort the inventory, load the checked-in GPU YAML, construct synthetic DU/PLU metadata and config-derived quoted written-file URLs, and write a schema-2 extraction manifest. Revalidate a dumped config with zoning match_tokens set to ZONE, hash that config, and assemble a retained source-bound document. The archive descriptor is fabricated with a*64, size 100, and source.zip path; no ZIP is written. The `zoning_filenames` parameter is accepted but unused in this helper.

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
    base_config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    written = tuple(
        GpuWrittenFile(
            filename=value,
            title=None,
            document_path=None,
            source_url=(
                f"{str(base_config.api.base_url).rstrip('/')}/document/"
                f"{quote(DOCUMENT_ID, safe='')}/files/{quote(value, safe='')}"
            ),
        )
        for value in written_filenames
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
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
    config_payload = base_config.model_dump(mode="python")
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]
    source_config = GpuSourceConfig.model_validate(config_payload)
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=(zoning.reference,),
        zoning=zoning,
        related_layers=(),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_fixture_document`

**Purpose:** Create synthetic PDF byte files under numbered written directories, build a real zoning source in the requested format, combine inventories, and delegate metadata/manifest/config assembly to `_document`. Optional filename inventories deliberately support missing/duplicate selection regressions. No archive download or real PDF text parsing occurs.

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

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `filename` | keyword-only | `str` | `DEFAULT_PDF` |
| `zoning_filenames` | keyword-only | `list[object] \| None` | `None` |
| `written_filenames` | keyword-only | `tuple[str, ...] \| None` | `None` |
| `inventory_filenames` | keyword-only | `tuple[str, ...] \| None` | `None` |
| `source_format` | keyword-only | `str` | `'GPKG'` |
| `include_nomfic` | keyword-only | `bool` | `True` |

**Return and exception contract**

- Exact observed return expressions:
  - `_document(<br>        root,<br>        tuple(inventory),<br>        zoning,<br>        zoning_filenames=zoning_filenames or [filename],<br>        written_filenames=(filename,)<br>        if written_filenames is None<br>        else written_filenames,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::_one_page_index` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::_one_page_index` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_source_nomfic_resolves_generic_filename` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_source_nomfic_resolves_generic_filename` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_explicit_source_validated_selection_succeeds` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_explicit_source_validated_selection_succeeds` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_unchanged_zoning_source_is_revalidated_before_selection` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unchanged_zoning_source_is_revalidated_before_selection` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_mutated_loaded_nomfic_is_rejected_before_selection` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_mutated_loaded_nomfic_is_rejected_before_selection` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_mutated_loaded_zoning_geometry_or_order_is_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zoning_source_bytes_changed_after_ingestion_are_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zoning_source_inventory_integrity_mismatch_is_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_missing_nomfic_field_is_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_missing_nomfic_field_is_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_null_nomfic_is_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_null_nomfic_is_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_multiple_nomfic_values_are_ambiguous` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_multiple_nomfic_values_are_ambiguous` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_unsafe_explicit_filename_is_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unsafe_explicit_filename_is_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_explicit_filename_not_referenced_by_zoning_fails` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_explicit_filename_not_referenced_by_zoning_fails` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_filename_absent_from_written_files_fails` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_filename_absent_from_written_files_fails` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_unrelated_non_pdf_written_file_does_not_block_selection` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unrelated_non_pdf_written_file_does_not_block_selection` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_filename_absent_from_inventory_fails` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_filename_absent_from_inventory_fails` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_duplicate_inventory_basename_fails` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_duplicate_inventory_basename_fails` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_path_outside_root_is_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_path_outside_root_is_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_pdf_inventory_integrity_mismatch_fails` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_pdf_inventory_integrity_mismatch_fails` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_page_states_numbering_and_hashes` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_zero_page_pdf_is_rejected` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zero_page_pdf_is_rejected` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_pdf_reader_failure_is_controlled_and_chained` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_pdf_reader_failure_is_controlled_and_chained` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_version_discovery_failure_is_controlled_and_chained` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_version_discovery_failure_is_controlled_and_chained` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_index_integrity_mutations_fail` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_source_metadata_raises_controlled_index_error` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_source_metadata_raises_controlled_index_error` via `_fixture_document`
- direct call: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `_fixture_document`
- value/type reference: `tests.unit.test_index_planning_regulation::test_extraction_and_search_do_not_mutate_inputs` via `_fixture_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `relative.split` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `inventory.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inventory_item` | `tests.unit.test_index_planning_regulation._inventory_item` |
| `_write_zoning_source` | `tests.unit.test_index_planning_regulation._write_zoning_source` |
| `_zone_frame` | `tests.unit.test_index_planning_regulation._zone_frame` |
| `inventory.extend` | `unresolved local/third-party receiver; no ownership inferred` |
| `_document` | `tests.unit.test_index_planning_regulation._document` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Create synthetic PDF byte files under numbered written directories, build a real zoning source in the requested format, combine inventories, and delegate metadata/manifest/config assembly to `_document`. Optional filename inventories deliberately support missing/duplicate selection regressions. No archive download or real PDF text parsing occurs.

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
    inventory_names = (
        (filename,) if inventory_filenames is None else inventory_filenames
    )
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
        written_filenames=(filename,)
        if written_filenames is None
        else written_filenames,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_one_page_index`

**Purpose:** Create the physical synthetic document, replace PDF parsing with one chosen text result (default Énergie), and run the real public indexing stage. Return its PlanningRegulationIndex; the function has no declared return annotation, not a None return contract.

**Exact signature**

```python
def _one_page_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str = "Énergie",
):
```

- Exact decorators: none.
- No return annotation is declared; the actual returned object is described above.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `text` | positional-or-keyword | `str` | `'Énergie'` |

**Return and exception contract**

- Exact observed return expressions:
  - `index_planning_regulation(document)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::test_raw_context_preserves_source_typography` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_raw_context_preserves_source_typography` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_zero_context_preserves_complete_raw_unicode_span` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_zero_context_preserves_complete_raw_unicode_span` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_literal_search_does_not_add_semantic_synonyms` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_literal_search_does_not_add_semantic_synonyms` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_coordinated_page_mutation_fails_envelope_hash` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_coordinated_page_mutation_fails_envelope_hash` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_complete_index_envelope_mutation_is_rejected` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_complete_index_envelope_mutation_is_rejected` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_unsupported_or_malformed_index_hash_schema_is_rejected` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_page_hash_schema_is_rejected_as_controlled_error` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::_valid_search_result` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::_valid_search_result` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_invalid_search_term_is_rejected` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_invalid_search_term_is_rejected` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_duplicate_normalized_search_terms_are_rejected` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_duplicate_normalized_search_terms_are_rejected` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_empty_search_result_has_stable_schema_and_lineage` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_empty_search_result_has_stable_schema_and_lineage` via `_one_page_index`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_page_value_raises_controlled_index_error` via `_one_page_index`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_page_value_raises_controlled_index_error` via `_one_page_index`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Create the physical synthetic document, replace PDF parsing with one chosen text result (default Énergie), and run the real public indexing stage. Return its PlanningRegulationIndex; the function has no declared return annotation, not a None return contract.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_api_exports_immutable_models_and_validators`

**Purpose:** Loop over seven expected stage export names and assert both __all__ membership and attribute presence. Despite the test name, these assertions do not construct models or attempt immutability mutations.

**Exact signature**

```python
def test_public_api_exports_immutable_models_and_validators() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert name in stages.__all__`
  - `assert hasattr(stages, name)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Loop over seven expected stage export names and assert both __all__ membership and attribute presence. Despite the test name, these assertions do not construct models or attempt immutability mutations.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_nomfic_resolves_generic_filename`

**Purpose:** For the default basename and an unrelated commune/date-like basename, create matching zoning/written/inventory evidence and a one-page reader double; assert the selected PDF relative path ends in exactly that basename. This checks source-driven selection rather than hardcoded filename identity.

**Exact signature**

```python
def test_source_nomfic_resolves_generic_filename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    filename: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "filename",
    [DEFAULT_PDF, "98765_reglement_20300102.pdf"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `filename` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert Path(result.pdf_relative_path).name == filename`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `Path` | `pathlib.Path` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_explicit_source_validated_selection_succeeds`

**Purpose:** Build a.pdf and b.pdf in all source inventories, provide an explicit b.pdf request, and assert its selected basename. The reader is mocked; ambiguity is resolved only among source-referenced candidates.

**Exact signature**

```python
def test_explicit_source_validated_selection_succeeds(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert Path(result.pdf_relative_path).name == "b.pdf"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `Path` | `pathlib.Path` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unchanged_zoning_source_is_revalidated_before_selection`

**Purpose:** For real temporary GPKG and Shapefile zoning sources, run indexing with a reader double and assert default filename, ZONING_NOMFIC method, and lowercase 64-hex selection digest. The real source validator is not monkeypatched; this test does not instrument its call count.

**Exact signature**

```python
def test_unchanged_zoning_source_is_revalidated_before_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    source_format: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("source_format", ["GPKG", "ESRI Shapefile"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `source_format` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.regulation_filename == DEFAULT_PDF`
  - `assert result.source_selection_method == "ZONING_NOMFIC"`
  - `assert fullmatch(r"[0-9a-f]{64}", result.source_selection_sha256)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `fullmatch` | `re.fullmatch` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutated_loaded_nomfic_is_rejected_before_selection`

**Purpose:** Copy the loaded zoning frame, replace NOMFIC without changing physical bytes, and expect a stage error matching zoning/source from public indexing. The inconsistent retained frame cannot select another PDF.

**Exact signature**

```python
def test_mutated_loaded_nomfic_is_rejected_before_selection(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="zoning\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `document.zoning.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_mutated_loaded_nomfic_is_rejected_before_selection(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    mutated = document.zoning.data.copy(deep=True)
    mutated.loc[0, "NOMFIC"] = "other_reglement.pdf"
    corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
    with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutated_loaded_zoning_geometry_or_order_is_rejected`

**Purpose:** Use two source rows, then either reverse their retained order or replace one retained Polygon far from the original. Public indexing must fail with zoning/source text in both cases; physical source bytes remain unchanged.

**Exact signature**

```python
def test_mutated_loaded_zoning_geometry_or_order_is_rejected(
    tmp_path: Path,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["reorder", "geometry"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="zoning\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `document.zoning.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `mutated.iloc[::-1].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `mutated.geometry.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `Polygon` | `shapely.geometry.Polygon` |
| `mutated.set_geometry` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zoning_source_bytes_changed_after_ingestion_are_rejected`

**Purpose:** Append b'tamper' to the actual temporary zoning dataset file after fixture ingestion, then expect indexing to fail with size/SHA256/integrity text. This is an intentional local append write, not a read-only operation.

**Exact signature**

```python
def test_zoning_source_bytes_changed_after_ingestion_are_rejected(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="size\|SHA256\|integrity")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `document.zoning.reference.dataset_path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zoning_source_inventory_integrity_mismatch_is_rejected`

**Purpose:** Replace the first SPATIAL_DATA inventory record's size with size+1 or SHA with b*64 while keeping the manifest/bytes unchanged. Expect a controlled size/SHA256/integrity failure from indexing; the test does not isolate the later file-byte gate from manifest validation.

**Exact signature**

```python
def test_zoning_source_inventory_integrity_mismatch_is_rejected(
    tmp_path: Path,
    field: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["size_bytes", "sha256"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="size\|SHA256\|integrity")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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
    replacement: object = current.size_bytes + 1 if field == "size_bytes" else "b" * 64
    items[position] = replace(current, **{field: replacement})
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_nomfic_field_is_rejected`

**Purpose:** Write and load a physical zoning source without NOMFIC; public indexing must fail with missing NOMFIC. This differs from mutating only the retained frame.

**Exact signature**

```python
def test_missing_nomfic_field_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_missing_nomfic_field_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, include_nomfic=False)
    with pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC"):
        index_planning_regulation(document)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_nomfic_is_rejected`

**Purpose:** Write a physical source whose sole NOMFIC is null, then expect no regulation filename from indexing. No PDF reader double is needed because source selection fails first.

**Exact signature**

```python
def test_null_nomfic_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="no regulation filename")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_null_nomfic_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, zoning_filenames=[None])
    with pytest.raises(PlanningRegulationIndexError, match="no regulation filename"):
        index_planning_regulation(document)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_multiple_nomfic_values_are_ambiguous`

**Purpose:** Provide two fully inventoried/source-referenced PDF names and omit an explicit choice. Require an ambiguity error; no automatic filename/title preference is asserted.

**Exact signature**

```python
def test_multiple_nomfic_values_are_ambiguous(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="ambiguous")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsafe_explicit_filename_is_rejected`

**Purpose:** Exercise eight explicit strings: empty, leading/trailing whitespace, traversal, POSIX separator, Windows drive/backslash spelling, NUL, and non-PDF suffix. Every public call must fail with filename text; this is a bounded lexical test set, not exhaustive filesystem path coverage.

**Exact signature**

```python
def test_unsafe_explicit_filename_is_rejected(tmp_path: Path, filename: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "filename",
    [
        "",
        " file.pdf",
        "file.pdf ",
        "../file.pdf",
        "a/b.pdf",
        "C:\\a.pdf",
        "bad\x00.pdf",
        "file.txt",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `filename` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="filename")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_unsafe_explicit_filename_is_rejected(tmp_path: Path, filename: str) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="filename"):
        index_planning_regulation(document, regulation_filename=filename)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_explicit_filename_not_referenced_by_zoning_fails`

**Purpose:** Request other.pdf against a default-only physical zoning source and require a not referenced error. A syntactically valid PDF name alone does not authorize selection.

**Exact signature**

```python
def test_explicit_filename_not_referenced_by_zoning_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="not referenced")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_explicit_filename_not_referenced_by_zoning_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="not referenced"):
        index_planning_regulation(document, regulation_filename="other.pdf")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_filename_absent_from_written_files_fails`

**Purpose:** Keep default NOMFIC/inventory but provide only other.pdf in written_files; expect the written_files error. The exact cross-inventory basename match is tested.

**Exact signature**

```python
def test_filename_absent_from_written_files_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="written_files")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_filename_absent_from_written_files_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, written_filenames=("other.pdf",))
    with pytest.raises(PlanningRegulationIndexError, match="written_files"):
        index_planning_regulation(document)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unrelated_non_pdf_written_file_does_not_block_selection`

**Purpose:** Add technical-note.txt beside the valid default PDF in written metadata, use a one-page reader double, and assert a one-page index. Unrelated non-PDF metadata must not block the selected source-referenced regulation.

**Exact signature**

```python
def test_unrelated_non_pdf_written_file_does_not_block_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert index_planning_regulation(document).total_page_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_filename_absent_from_inventory_fails`

**Purpose:** Change the retained regulation inventory path to other.pdf while leaving physical files and marker unchanged. Require either missing from GPU inventory or verified manifest text; this test permits rejection at the earlier manifest boundary.

**Exact signature**

```python
def test_filename_absent_from_inventory_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="missing from GPU inventory\|verified manifest",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_inventory_basename_fails`

**Purpose:** Create two physical files with the same selected basename in distinct numbered directories and a matching inventory. Public indexing must reject the ambiguous basename even though the relative paths differ.

**Exact signature**

```python
def test_duplicate_inventory_basename_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="ambiguous")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_duplicate_inventory_basename_fails(tmp_path: Path) -> None:
    document = _fixture_document(
        tmp_path, inventory_filenames=(DEFAULT_PDF, DEFAULT_PDF)
    )
    with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_path_outside_root_is_rejected`

**Purpose:** Replace the first sorted retained inventory item with a ../ PDF spelling and discard the other retained entries. Expect unsafe or verified manifest text. No outside-root file is read or created; the broad expected alternative does not prove a specific path-resolution branch was reached.

**Exact signature**

```python
def test_path_outside_root_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="unsafe\|verified manifest",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_path_outside_root_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item = replace(document.extraction.files[0], relative_path=f"../{DEFAULT_PDF}")
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_pdf_inventory_integrity_mismatch_fails`

**Purpose:** Replace the WRITTEN_REGULATION inventory size or SHA without rewriting the manifest or PDF bytes, then require a controlled error containing differs. This protects consistency but does not isolate manifest mismatch from the later physical PDF comparison.

**Exact signature**

```python
def test_pdf_inventory_integrity_mismatch_fails(tmp_path: Path, field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["size_bytes", "sha256"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="differs")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_page_states_numbering_and_hashes`

**Purpose:** Mock three pages: accented/multiline text, whitespace-only text, and RuntimeError. Assert exact seven-column schema, ordered page numbers, TEXT/EMPTY/ERROR states, retained raw text, expected normalization, and digest spelling; run intrinsic validation. An attempted total_page_count reassignment must immediately raise FrozenInstanceError; mutable page-cell changes are not prohibited by this test.

**Exact signature**

```python
def test_page_states_numbering_and_hashes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(FrozenInstanceError)`
- Exact assertions:
  - `assert tuple(result.pages.columns) == PAGE_COLUMNS`
  - `assert result.pages.page_number.tolist() == [1, 2, 3]`
  - `assert result.pages.extraction_status.tolist() == ["TEXT", "EMPTY", "ERROR"]`
  - `assert result.pages.loc[0, "raw_text"] == raw`
  - `assert result.pages.loc[0, "normalized_search_text"] == "energie batterie"`
  - `assert result.pages.page_content_sha256.str.fullmatch(r"[0-9a-f]{64}").all()`
  - `assert fullmatch(r"[0-9a-f]{64}", result.pages_content_sha256)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `RuntimeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.pages.page_number.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.pages.extraction_status.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.pages.page_content_sha256.str.fullmatch(r"[0-9a-f]{64}").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.pages.page_content_sha256.str.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `fullmatch` | `re.fullmatch` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `pytest.raises` | `pytest.raises` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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
        result.total_page_count = 9  # type: ignore[misc]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zero_page_pdf_is_rejected`

**Purpose:** Return an empty fake reader page list and require the at least one page stage error. This tests zero pages, not encryption rejection or a real malformed PDF.

**Exact signature**

```python
def test_zero_page_pdf_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="at least one page")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_pdf_reader_failure_is_controlled_and_chained`

**Purpose:** Replace PdfReader with the nested callback that raises RuntimeError. Public indexing must raise the opened or parsed stage error and retain RuntimeError as __cause__; fixture bytes are not actually parsed.

**Exact signature**

```python
def test_pdf_reader_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningRegulationIndexError, match="opened or parsed"<br>    )`
- Exact assertions:
  - `assert isinstance(caught.value.__cause__, RuntimeError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_pdf_reader_failure_is_controlled_and_chained.fail_reader`

**Purpose:** Ignore all reader arguments and raise RuntimeError('broken xref'). Installed as the stage's PdfReader binding by the enclosing test; never returns normally.

**Exact signature**

```python
def fail_reader(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- This callback always raises; it has no successful normal return.
- Explicit raise paths:
  - `RuntimeError("broken xref")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RuntimeError` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Ignore all reader arguments and raise RuntimeError('broken xref'). Installed as the stage's PdfReader binding by the enclosing test; never returns normally.

**Complete source-ordered implementation**

```python
def fail_reader(*args: object, **kwargs: object) -> object:
        raise RuntimeError("broken xref")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_french_literal_normalization`

**Purpose:** Assert eight exact source-to-normalized strings for case/accent folding, curly apostrophe, œ/Æ expansion, long dash, soft hyphen, and whitespace collapse. This directly calls the common planning-text owner; no index or files are constructed.

**Exact signature**

```python
def test_french_literal_normalization(source: str, term: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("source", "term"),
    [
        ("ÉNERGIE", "energie"),
        ("intérêt", "interet"),
        ("d’intérêt", "d'interet"),
        ("œuvre", "oeuvre"),
        ("ÆTHER", "aether"),
        ("poste—source", "poste-source"),
        ("inter\u00adruption", "interruption"),
        ("ligne\n   électrique", "ligne electrique"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `str` | `required` |
| `term` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _normalize_search_text(source) == term`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_normalize_search_text` | `landscout.common.planning_text.normalize_planning_search_text` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Assert eight exact source-to-normalized strings for case/accent folding, curly apostrophe, œ/Æ expansion, long dash, soft hyphen, and whitespace collapse. This directly calls the common planning-text owner; no index or files are constructed.

**Complete source-ordered implementation**

```python
def test_french_literal_normalization(source: str, term: str) -> None:
    assert _normalize_search_text(source) == term
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_raw_context_preserves_source_typography`

**Purpose:** Index an accented French phrase through the reader double, search its normalized literal with a four-character context margin, and assert page 1, one occurrence, raw/normalized phrase presence, and unchanged raw indexed text.

**Exact signature**

```python
def test_raw_context_preserves_source_typography(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert hit["page_number"] == 1`
  - `assert hit["occurrence_count"] == 1`
  - `assert "Équipement d’intérêt collectif" in hit["raw_context"]`
  - `assert "equipement d'interet collectif" in hit["normalized_context"]`
  - `assert index.pages.iloc[0]["raw_text"] == raw`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zero_context_preserves_complete_raw_unicode_span`

**Purpose:** For eight precomposed/decomposed accent, ligature, curly-apostrophe, and leading/internal/trailing soft-hyphen examples, search with zero margin and assert exact raw and normalized contexts plus substring membership and unchanged indexed raw text. The regression verifies Unicode span mapping, not UTF-8 byte offsets.

**Exact signature**

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

- Exact decorators: `pytest.mark.parametrize(
    ("raw", "term", "expected_raw", "expected_normalized"),
    [
        ("café", "cafe", "café", "cafe"),
        ("cafe\u0301", "cafe", "cafe\u0301", "cafe"),
        ("œuvre", "oeuvre", "œuvre", "oeuvre"),
        ("æther", "aether", "æther", "aether"),
        ("d’intérêt", "d'interet", "d’intérêt", "d'interet"),
        ("inter\u00adruption", "interruption", "inter\u00adruption", "interruption"),
        ("\u00adcafe", "cafe", "\u00adcafe", "cafe"),
        ("cafe\u00ad", "cafe", "cafe\u00ad", "cafe"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `raw` | positional-or-keyword | `str` | `required` |
| `term` | positional-or-keyword | `str` | `required` |
| `expected_raw` | positional-or-keyword | `str` | `required` |
| `expected_normalized` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert hit["raw_context"] == expected_raw`
  - `assert hit["normalized_context"] == expected_normalized`
  - `assert hit["raw_context"] in raw`
  - `assert index.pages.iloc[0]["raw_text"] == raw`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_literal_search_does_not_add_semantic_synonyms`

**Purpose:** Index text mentioning batterie and search accumulateur; assert an empty hit table. This checks one absent synonym pair, not any policy conclusion about batteries.

**Exact signature**

```python
def test_literal_search_does_not_add_semantic_synonyms(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.hits.empty`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_literal_search_does_not_add_semantic_synonyms(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, "Une batterie est mentionnée.")
    result = search_planning_regulation(index, ["accumulateur"])
    assert result.hits.empty
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_version_discovery_failure_is_controlled_and_chained`

**Purpose:** Use a successful reader double but replace the stage's imported distribution-version function with a failing callback. Require a version error whose __cause__ is RuntimeError; no environment package is changed.

**Exact signature**

```python
def test_version_discovery_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="version")`
- Exact assertions:
  - `assert isinstance(caught.value.__cause__, RuntimeError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_version_discovery_failure_is_controlled_and_chained.fail_version`

**Purpose:** Raise RuntimeError carrying the supplied distribution name. The enclosing test monkeypatches the stage's `version` binding to this callback; it never returns a version.

**Exact signature**

```python
def fail_version(name: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- This callback always raises; it has no successful normal return.
- Explicit raise paths:
  - `RuntimeError(name)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RuntimeError` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Raise RuntimeError carrying the supplied distribution name. The enclosing test monkeypatches the stage's `version` binding to this callback; it never returns a version.

**Complete source-ordered implementation**

```python
def fail_version(name: str) -> str:
        raise RuntimeError(name)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_page_mutation_fails_envelope_hash`

**Purpose:** Copy the page table, change raw/normalized text and character count coherently, and recompute only that page's hash. Intrinsic validation must fail with envelope text because the retained pages/outer envelopes remain unchanged. It does not test a coordinated rehash of every envelope.

**Exact signature**

```python
def test_coordinated_page_mutation_fails_envelope_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="envelope")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `index.pages.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pages.iloc[0].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `regulation_module._page_content_sha256` | `landscout.stages.index_planning_regulation._page_content_sha256`, through the literal import_module binding |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `replace` | `dataclasses.replace` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_index_integrity_mutations_fail`

**Purpose:** Against a two-page index, corrupt one page hash, the pages envelope digest, the normalization profile, or page order. Each bounded mutation must cause the public intrinsic validator to raise a stage error; no physical files are changed.

**Exact signature**

```python
def test_index_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("target", "value"),
    [
        ("page_hash", "b" * 64),
        ("envelope_hash", "b" * 64),
        ("profile", "other_v1"),
        ("order", None),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `target` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `index.pages.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `index.pages.iloc[::-1].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_index_envelope_mutation_is_rejected`

**Purpose:** Individually replace fifteen retained metadata/envelope fields, including the extractor version, without recomputing all hashes. Expect a stage error for every replacement. The version case proves the old outer hash binds its value, not a requirement to match the installed package version.

**Exact signature**

```python
def test_complete_index_envelope_mutation_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("document_id", "other-document"),
        ("archive_sha256", "b" * 64),
        ("regulation_filename", "other_reglement.pdf"),
        ("source_selection_method", "EXPLICIT_FILENAME"),
        ("source_selection_sha256", "b" * 64),
        ("pdf_relative_path", "written-0/other_reglement.pdf"),
        ("pdf_size_bytes", len(PDF_BYTES) + 1),
        ("pdf_sha256", "b" * 64),
        ("extraction_library", "other-reader"),
        ("extraction_library_version", "0.0.0"),
        ("search_normalization_profile", "other-profile"),
        ("page_hash_schema_version", 2),
        ("total_page_count", 2),
        ("pages_content_sha256", "b" * 64),
        ("index_content_sha256", "b" * 64),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `replacement` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsupported_or_malformed_index_hash_schema_is_rejected`

**Purpose:** Replace the index schema with 0, -1, 1.5, string '1', or unsupported 2; require a controlled intrinsic error. These five cases do not include a boolean.

**Exact signature**

```python
def test_unsupported_or_malformed_index_hash_schema_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("replacement", [0, -1, 1.5, "1", 2])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `replacement` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_page_hash_schema_is_rejected_as_controlled_error`

**Purpose:** Replace the page schema with 0, -1, 1.5, or string '1' and require a controlled intrinsic error. Unsupported integer 2 is separately represented in the metadata mutation matrix.

**Exact signature**

```python
def test_malformed_page_hash_schema_is_rejected_as_controlled_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("replacement", [0, -1, 1.5, "1"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `replacement` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_valid_search_result`

**Purpose:** Build a one-page index whose reader text contains two energy occurrences and one collective-equipment phrase, then search the two requested literals. Return the index and search result; no return annotation is declared.

**Exact signature**

```python
def _valid_search_result(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
```

- Exact decorators: none.
- No return annotation is declared; the actual returned object is described above.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `index, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `_valid_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_envelope_is_valid_and_deterministic` via `_valid_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_index_identity_schema_and_terms_are_sealed` via `_valid_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_index_identity_schema_and_terms_are_sealed` via `_valid_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `_valid_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_requested_terms_must_be_an_immutable_exact_tuple` via `_valid_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_result_integrity_mutations_fail` via `_valid_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_result_integrity_mutations_fail` via `_valid_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_search_hit_lineage_mutation_fails` via `_valid_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_search_hit_lineage_mutation_fails` via `_valid_search_result`
- direct call: `tests.unit.test_index_planning_regulation::test_malformed_hit_value_raises_controlled_index_error` via `_valid_search_result`
- value/type reference: `tests.unit.test_index_planning_regulation::test_malformed_hit_value_raises_controlled_index_error` via `_valid_search_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |

**Effects and limits**

Build a one-page index whose reader text contains two energy occurrences and one collective-equipment phrase, then search the two requested literals. Return the index and search result; no return annotation is declared.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_search_result_envelope_is_valid_and_deterministic`

**Purpose:** Repeat the same two-term search and assert hit-column order, normalization profile, index digest, search schema, two term/page rows, exact pandas frame equality, equal hits digest, and successful result validation. The helper text has two energy occurrences, but this test does not directly assert that occurrence_count equals two.

**Exact signature**

```python
def test_search_result_envelope_is_valid_and_deterministic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(first.hits.columns) == SEARCH_HIT_COLUMNS`
  - `assert first.search_normalization_profile == SEARCH_NORMALIZATION_PROFILE`
  - `assert first.index_content_sha256 == index.index_content_sha256`
  - `assert (<br>        first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION<br>    )`
  - `assert first.hit_count == 2`
  - `assert first.hits_content_sha256 == second.hits_content_sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_valid_search_result` | `tests.unit.test_index_planning_regulation._valid_search_result` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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
    assert (
        first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION
    )
    assert first.hit_count == 2
    assert_frame_equal(first.hits, second.hits)
    assert first.hits_content_sha256 == second.hits_content_sha256
    validate_planning_regulation_search_result(index, first)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_search_index_identity_schema_and_terms_are_sealed`

**Purpose:** Individually replace the referenced index digest, five unsupported/malformed search-schema values, or requested raw terms. Require a controlled search-result error in all seven cases; replacements retain the previous hits hash.

**Exact signature**

```python
def test_search_index_identity_schema_and_terms_are_sealed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("index_content_sha256", "b" * 64),
        ("search_hash_schema_version", 2),
        ("search_hash_schema_version", 0),
        ("search_hash_schema_version", -1),
        ("search_hash_schema_version", 1.5),
        ("search_hash_schema_version", "1"),
        ("requested_terms", ("other-term",)),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `replacement` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_valid_search_result` | `tests.unit.test_index_planning_regulation._valid_search_result` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_search_requested_terms_must_be_an_immutable_exact_tuple`

**Purpose:** Replace the tuple of requested terms with a list and require the validator's tuple error. This tests immediate boundary type rejection, not attempted in-place mutation of the valid tuple.

**Exact signature**

```python
def test_search_requested_terms_must_be_an_immutable_exact_tuple(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="tuple")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_valid_search_result` | `tests.unit.test_index_planning_regulation._valid_search_result` |
| `replace` | `dataclasses.replace` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_search_result_integrity_mutations_fail`

**Purpose:** Exercise nine retained result/hit mutations: wrong envelope document/PDF identity, unknown page, duplicated hit with updated row count, zero/fractional/string occurrence count, altered raw context, or wrong hits hash. Expect a controlled error in every case; copied frames isolate edits from the original result and hashes are not coordinated to the edits.

**Exact signature**

```python
def test_search_result_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("target", "value"),
    [
        ("document_id", "wrong"),
        ("pdf_sha256", "b" * 64),
        ("page_number", 99),
        ("duplicate", None),
        ("occurrence_count", 0),
        ("occurrence_count", 1.5),
        ("occurrence_count", "1"),
        ("raw_context", "corrupted"),
        ("hits_content_sha256", "b" * 64),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `target` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_valid_search_result` | `tests.unit.test_index_planning_regulation._valid_search_result` |
| `replace` | `dataclasses.replace` |
| `result.hits.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `hits[target].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_search_hit_lineage_mutation_fails`

**Purpose:** Change one hit's document_id or pdf_sha256 while retaining correct outer lineage and expect the specific lineage error. This independently targets row lineage rather than only the envelope.

**Exact signature**

```python
def test_search_hit_lineage_mutation_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["document_id", "pdf_sha256"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_valid_search_result` | `tests.unit.test_index_planning_regulation._valid_search_result` |
| `result.hits.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_search_term_is_rejected`

**Purpose:** Pass one empty, whitespace-only, edge-whitespace, or nonstring integer term in a list; require a search term error for all five cases. Input list typing is intentionally violated for the integer case.

**Exact signature**

```python
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("term", ["", "   ", " term", "term ", 7])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `term` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="search term")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `pytest.raises` | `pytest.raises` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="search term"):
        search_planning_regulation(index, [term])  # type: ignore[list-item]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_normalized_search_terms_are_rejected`

**Purpose:** Search both énergie and ENERGIE and require a unique error, showing duplicate detection occurs after normalization rather than on raw spelling.

**Exact signature**

```python
def test_duplicate_normalized_search_terms_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `pytest.raises` | `pytest.raises` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

```python
def test_duplicate_normalized_search_terms_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="unique"):
        search_planning_regulation(index, ["énergie", "ENERGIE"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_empty_search_result_has_stable_schema_and_lineage`

**Purpose:** Search batterie in a nonmatching page, then assert zero count, empty hits, exact column order, retained document/PDF identity, and successful validation. This is a no-match request, not an empty requested-term tuple test; it does not directly assert each dtype.

**Exact signature**

```python
def test_empty_search_result_has_stable_schema_and_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.hit_count == 0`
  - `assert result.hits.empty`
  - `assert tuple(result.hits.columns) == SEARCH_HIT_COLUMNS`
  - `assert result.document_id == index.document_id`
  - `assert result.pdf_sha256 == index.pdf_sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_page_value_raises_controlled_index_error`

**Purpose:** Put a list in the copied page extraction_error cell and require the public index validator to return a controlled stage error rather than leaking pandas ambiguous-null behavior. No exact message or cause is required.

**Exact signature**

```python
def test_malformed_page_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_one_page_index` | `tests.unit.test_index_planning_regulation._one_page_index` |
| `index.pages.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `replace` | `dataclasses.replace` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_hit_value_raises_controlled_index_error`

**Purpose:** Put a list into a copied hit raw_context cell and require a controlled result-validation error. No real PDF text or original hit table is modified.

**Exact signature**

```python
def test_malformed_hit_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_valid_search_result` | `tests.unit.test_index_planning_regulation._valid_search_result` |
| `result.hits.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `hits["raw_context"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |
| `replace` | `dataclasses.replace` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_canonical_hash_serialization_failure_is_controlled_and_chained`

**Purpose:** Pass a bare object leaf to the private canonical JSON hasher. Require a serialized stage error with a TypeError cause; no digest is successfully produced and no fallback repr is accepted.

**Exact signature**

```python
def test_canonical_hash_serialization_failure_is_controlled_and_chained() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="serialized",<br>    )`
- Exact assertions:
  - `assert isinstance(caught.value.__cause__, TypeError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `regulation_module._canonical_sha256` | `landscout.stages.index_planning_regulation._canonical_sha256`, through the literal import_module binding |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Effects and limits**

Pass a bare object leaf to the private canonical JSON hasher. Require a serialized stage error with a TypeError cause; no digest is successfully produced and no fallback repr is accepted.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_source_metadata_raises_controlled_index_error`

**Purpose:** Replace written_files with an exact tuple containing a bare object and expect controlled public indexing failure. The test deliberately constructs an invalid dataclass graph and does not assert a particular inner metadata gate.

**Exact signature**

```python
def test_malformed_source_metadata_raises_controlled_index_error(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationIndexError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `replace` | `dataclasses.replace` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_and_search_do_not_mutate_inputs`

**Purpose:** Deep-copy extraction metadata and zoning data, index through a reader double, snapshot the pages, then search. Assert extraction equality, exact GeoDataFrame equality for zoning, and pandas frame equality for pages. This is a bounded successful-path no-input-mutation regression, not deep immutability of the output tables.

**Exact signature**

```python
def test_extraction_and_search_do_not_mutate_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert document.extraction == extraction_before`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_fixture_document` | `tests.unit.test_index_planning_regulation._fixture_document` |
| `deepcopy` | `copy.deepcopy` |
| `document.zoning.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_patch_reader` | `tests.unit.test_index_planning_regulation._patch_reader` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `index.pages.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |

**Effects and limits**

Constructs temporary on-disk fixture files through the documented helpers and exercises the real indexing/validation functions. PDF parsing is mocked where execution reaches successful extraction; negative source-selection tests fail earlier. Deliberate copied-frame/envelope changes, scoped monkeypatches, or physical tampering are described above. No live GPU request, production cache modification, or parcel policy decision occurs.

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **45**, expanding to **114 declared cases**; no execution is reported here.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

The numeric column counts only direct Python `assert` syntax. It excludes `pytest.raises` contexts and assertion-helper calls such as `assert_frame_equal`; a zero is not absence of test evidence. Complete callable source is in section 6 and the full-file snapshot in section 11.

| Test | Parametrization | Expected exception contexts | Direct AST assert statements | Verified regression scope |
|---|---|---|---:|---|
| `test_public_api_exports_immutable_models_and_validators` | none | none | 2 | Loop over seven expected stage export names and assert both __all__ membership and attribute presence. Despite the test name, these assertions do not construct models or attempt immutability mutations. |
| `test_source_nomfic_resolves_generic_filename` | pytest.mark.parametrize(<br>    "filename",<br>    [DEFAULT_PDF, "98765_reglement_20300102.pdf"],<br>) | none | 1 | For the default basename and an unrelated commune/date-like basename, create matching zoning/written/inventory evidence and a one-page reader double; assert the selected PDF relative path ends in exactly that basename. This checks source-driven selection rather than hardcoded filename identity. |
| `test_explicit_source_validated_selection_succeeds` | none | none | 1 | Build a.pdf and b.pdf in all source inventories, provide an explicit b.pdf request, and assert its selected basename. The reader is mocked; ambiguity is resolved only among source-referenced candidates. |
| `test_unchanged_zoning_source_is_revalidated_before_selection` | pytest.mark.parametrize("source_format", ["GPKG", "ESRI Shapefile"]) | none | 3 | For real temporary GPKG and Shapefile zoning sources, run indexing with a reader double and assert default filename, ZONING_NOMFIC method, and lowercase 64-hex selection digest. The real source validator is not monkeypatched; this test does not instrument its call count. |
| `test_mutated_loaded_nomfic_is_rejected_before_selection` | none | pytest.raises(PlanningRegulationIndexError, match="zoning\|source") | 0 | Copy the loaded zoning frame, replace NOMFIC without changing physical bytes, and expect a stage error matching zoning/source from public indexing. The inconsistent retained frame cannot select another PDF. |
| `test_mutated_loaded_zoning_geometry_or_order_is_rejected` | pytest.mark.parametrize("mutation", ["reorder", "geometry"]) | pytest.raises(PlanningRegulationIndexError, match="zoning\|source") | 0 | Use two source rows, then either reverse their retained order or replace one retained Polygon far from the original. Public indexing must fail with zoning/source text in both cases; physical source bytes remain unchanged. |
| `test_zoning_source_bytes_changed_after_ingestion_are_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="size\|SHA256\|integrity") | 0 | Append b'tamper' to the actual temporary zoning dataset file after fixture ingestion, then expect indexing to fail with size/SHA256/integrity text. This is an intentional local append write, not a read-only operation. |
| `test_zoning_source_inventory_integrity_mismatch_is_rejected` | pytest.mark.parametrize("field", ["size_bytes", "sha256"]) | pytest.raises(PlanningRegulationIndexError, match="size\|SHA256\|integrity") | 0 | Replace the first SPATIAL_DATA inventory record's size with size+1 or SHA with b*64 while keeping the manifest/bytes unchanged. Expect a controlled size/SHA256/integrity failure from indexing; the test does not isolate the later file-byte gate from manifest validation. |
| `test_missing_nomfic_field_is_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC") | 0 | Write and load a physical zoning source without NOMFIC; public indexing must fail with missing NOMFIC. This differs from mutating only the retained frame. |
| `test_null_nomfic_is_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="no regulation filename") | 0 | Write a physical source whose sole NOMFIC is null, then expect no regulation filename from indexing. No PDF reader double is needed because source selection fails first. |
| `test_multiple_nomfic_values_are_ambiguous` | none | pytest.raises(PlanningRegulationIndexError, match="ambiguous") | 0 | Provide two fully inventoried/source-referenced PDF names and omit an explicit choice. Require an ambiguity error; no automatic filename/title preference is asserted. |
| `test_unsafe_explicit_filename_is_rejected` | pytest.mark.parametrize(<br>    "filename",<br>    [<br>        "",<br>        " file.pdf",<br>        "file.pdf ",<br>        "../file.pdf",<br>        "a/b.pdf",<br>        "C:\\a.pdf",<br>        "bad\x00.pdf",<br>        "file.txt",<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError, match="filename") | 0 | Exercise eight explicit strings: empty, leading/trailing whitespace, traversal, POSIX separator, Windows drive/backslash spelling, NUL, and non-PDF suffix. Every public call must fail with filename text; this is a bounded lexical test set, not exhaustive filesystem path coverage. |
| `test_explicit_filename_not_referenced_by_zoning_fails` | none | pytest.raises(PlanningRegulationIndexError, match="not referenced") | 0 | Request other.pdf against a default-only physical zoning source and require a not referenced error. A syntactically valid PDF name alone does not authorize selection. |
| `test_filename_absent_from_written_files_fails` | none | pytest.raises(PlanningRegulationIndexError, match="written_files") | 0 | Keep default NOMFIC/inventory but provide only other.pdf in written_files; expect the written_files error. The exact cross-inventory basename match is tested. |
| `test_unrelated_non_pdf_written_file_does_not_block_selection` | none | none | 1 | Add technical-note.txt beside the valid default PDF in written metadata, use a one-page reader double, and assert a one-page index. Unrelated non-PDF metadata must not block the selected source-referenced regulation. |
| `test_filename_absent_from_inventory_fails` | none | pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="missing from GPU inventory\|verified manifest",<br>    ) | 0 | Change the retained regulation inventory path to other.pdf while leaving physical files and marker unchanged. Require either missing from GPU inventory or verified manifest text; this test permits rejection at the earlier manifest boundary. |
| `test_duplicate_inventory_basename_fails` | none | pytest.raises(PlanningRegulationIndexError, match="ambiguous") | 0 | Create two physical files with the same selected basename in distinct numbered directories and a matching inventory. Public indexing must reject the ambiguous basename even though the relative paths differ. |
| `test_path_outside_root_is_rejected` | none | pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="unsafe\|verified manifest",<br>    ) | 0 | Replace the first sorted retained inventory item with a ../ PDF spelling and discard the other retained entries. Expect unsafe or verified manifest text. No outside-root file is read or created; the broad expected alternative does not prove a specific path-resolution branch was reached. |
| `test_pdf_inventory_integrity_mismatch_fails` | pytest.mark.parametrize("field", ["size_bytes", "sha256"]) | pytest.raises(PlanningRegulationIndexError, match="differs") | 0 | Replace the WRITTEN_REGULATION inventory size or SHA without rewriting the manifest or PDF bytes, then require a controlled error containing differs. This protects consistency but does not isolate manifest mismatch from the later physical PDF comparison. |
| `test_page_states_numbering_and_hashes` | none | pytest.raises(FrozenInstanceError) | 7 | Mock three pages: accented/multiline text, whitespace-only text, and RuntimeError. Assert exact seven-column schema, ordered page numbers, TEXT/EMPTY/ERROR states, retained raw text, expected normalization, and digest spelling; run intrinsic validation. An attempted total_page_count reassignment must immediately raise FrozenInstanceError; mutable page-cell changes are not prohibited by this test. |
| `test_zero_page_pdf_is_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="at least one page") | 0 | Return an empty fake reader page list and require the at least one page stage error. This tests zero pages, not encryption rejection or a real malformed PDF. |
| `test_pdf_reader_failure_is_controlled_and_chained` | none | pytest.raises(<br>        PlanningRegulationIndexError, match="opened or parsed"<br>    ) | 1 | Replace PdfReader with the nested callback that raises RuntimeError. Public indexing must raise the opened or parsed stage error and retain RuntimeError as __cause__; fixture bytes are not actually parsed. |
| `test_french_literal_normalization` | pytest.mark.parametrize(<br>    ("source", "term"),<br>    [<br>        ("ÉNERGIE", "energie"),<br>        ("intérêt", "interet"),<br>        ("d’intérêt", "d'interet"),<br>        ("œuvre", "oeuvre"),<br>        ("ÆTHER", "aether"),<br>        ("poste—source", "poste-source"),<br>        ("inter\u00adruption", "interruption"),<br>        ("ligne\n   électrique", "ligne electrique"),<br>    ],<br>) | none | 1 | Assert eight exact source-to-normalized strings for case/accent folding, curly apostrophe, œ/Æ expansion, long dash, soft hyphen, and whitespace collapse. This directly calls the common planning-text owner; no index or files are constructed. |
| `test_raw_context_preserves_source_typography` | none | none | 5 | Index an accented French phrase through the reader double, search its normalized literal with a four-character context margin, and assert page 1, one occurrence, raw/normalized phrase presence, and unchanged raw indexed text. |
| `test_zero_context_preserves_complete_raw_unicode_span` | pytest.mark.parametrize(<br>    ("raw", "term", "expected_raw", "expected_normalized"),<br>    [<br>        ("café", "cafe", "café", "cafe"),<br>        ("cafe\u0301", "cafe", "cafe\u0301", "cafe"),<br>        ("œuvre", "oeuvre", "œuvre", "oeuvre"),<br>        ("æther", "aether", "æther", "aether"),<br>        ("d’intérêt", "d'interet", "d’intérêt", "d'interet"),<br>        ("inter\u00adruption", "interruption", "inter\u00adruption", "interruption"),<br>        ("\u00adcafe", "cafe", "\u00adcafe", "cafe"),<br>        ("cafe\u00ad", "cafe", "cafe\u00ad", "cafe"),<br>    ],<br>) | none | 4 | For eight precomposed/decomposed accent, ligature, curly-apostrophe, and leading/internal/trailing soft-hyphen examples, search with zero margin and assert exact raw and normalized contexts plus substring membership and unchanged indexed raw text. The regression verifies Unicode span mapping, not UTF-8 byte offsets. |
| `test_literal_search_does_not_add_semantic_synonyms` | none | none | 1 | Index text mentioning batterie and search accumulateur; assert an empty hit table. This checks one absent synonym pair, not any policy conclusion about batteries. |
| `test_version_discovery_failure_is_controlled_and_chained` | none | pytest.raises(PlanningRegulationIndexError, match="version") | 1 | Use a successful reader double but replace the stage's imported distribution-version function with a failing callback. Require a version error whose __cause__ is RuntimeError; no environment package is changed. |
| `test_coordinated_page_mutation_fails_envelope_hash` | none | pytest.raises(PlanningRegulationIndexError, match="envelope") | 0 | Copy the page table, change raw/normalized text and character count coherently, and recompute only that page's hash. Intrinsic validation must fail with envelope text because the retained pages/outer envelopes remain unchanged. It does not test a coordinated rehash of every envelope. |
| `test_index_integrity_mutations_fail` | pytest.mark.parametrize(<br>    ("target", "value"),<br>    [<br>        ("page_hash", "b" * 64),<br>        ("envelope_hash", "b" * 64),<br>        ("profile", "other_v1"),<br>        ("order", None),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Against a two-page index, corrupt one page hash, the pages envelope digest, the normalization profile, or page order. Each bounded mutation must cause the public intrinsic validator to raise a stage error; no physical files are changed. |
| `test_complete_index_envelope_mutation_is_rejected` | pytest.mark.parametrize(<br>    ("field", "replacement"),<br>    [<br>        ("document_id", "other-document"),<br>        ("archive_sha256", "b" * 64),<br>        ("regulation_filename", "other_reglement.pdf"),<br>        ("source_selection_method", "EXPLICIT_FILENAME"),<br>        ("source_selection_sha256", "b" * 64),<br>        ("pdf_relative_path", "written-0/other_reglement.pdf"),<br>        ("pdf_size_bytes", len(PDF_BYTES) + 1),<br>        ("pdf_sha256", "b" * 64),<br>        ("extraction_library", "other-reader"),<br>        ("extraction_library_version", "0.0.0"),<br>        ("search_normalization_profile", "other-profile"),<br>        ("page_hash_schema_version", 2),<br>        ("total_page_count", 2),<br>        ("pages_content_sha256", "b" * 64),<br>        ("index_content_sha256", "b" * 64),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Individually replace fifteen retained metadata/envelope fields, including the extractor version, without recomputing all hashes. Expect a stage error for every replacement. The version case proves the old outer hash binds its value, not a requirement to match the installed package version. |
| `test_unsupported_or_malformed_index_hash_schema_is_rejected` | pytest.mark.parametrize("replacement", [0, -1, 1.5, "1", 2]) | pytest.raises(PlanningRegulationIndexError) | 0 | Replace the index schema with 0, -1, 1.5, string '1', or unsupported 2; require a controlled intrinsic error. These five cases do not include a boolean. |
| `test_malformed_page_hash_schema_is_rejected_as_controlled_error` | pytest.mark.parametrize("replacement", [0, -1, 1.5, "1"]) | pytest.raises(PlanningRegulationIndexError) | 0 | Replace the page schema with 0, -1, 1.5, or string '1' and require a controlled intrinsic error. Unsupported integer 2 is separately represented in the metadata mutation matrix. |
| `test_search_result_envelope_is_valid_and_deterministic` | none | none | 6 | Repeat the same two-term search and assert hit-column order, normalization profile, index digest, search schema, two term/page rows, exact pandas frame equality, equal hits digest, and successful result validation. The helper text has two energy occurrences, but this test does not directly assert that occurrence_count equals two. |
| `test_search_index_identity_schema_and_terms_are_sealed` | pytest.mark.parametrize(<br>    ("field", "replacement"),<br>    [<br>        ("index_content_sha256", "b" * 64),<br>        ("search_hash_schema_version", 2),<br>        ("search_hash_schema_version", 0),<br>        ("search_hash_schema_version", -1),<br>        ("search_hash_schema_version", 1.5),<br>        ("search_hash_schema_version", "1"),<br>        ("requested_terms", ("other-term",)),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Individually replace the referenced index digest, five unsupported/malformed search-schema values, or requested raw terms. Require a controlled search-result error in all seven cases; replacements retain the previous hits hash. |
| `test_search_requested_terms_must_be_an_immutable_exact_tuple` | none | pytest.raises(PlanningRegulationIndexError, match="tuple") | 0 | Replace the tuple of requested terms with a list and require the validator's tuple error. This tests immediate boundary type rejection, not attempted in-place mutation of the valid tuple. |
| `test_search_result_integrity_mutations_fail` | pytest.mark.parametrize(<br>    ("target", "value"),<br>    [<br>        ("document_id", "wrong"),<br>        ("pdf_sha256", "b" * 64),<br>        ("page_number", 99),<br>        ("duplicate", None),<br>        ("occurrence_count", 0),<br>        ("occurrence_count", 1.5),<br>        ("occurrence_count", "1"),<br>        ("raw_context", "corrupted"),<br>        ("hits_content_sha256", "b" * 64),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Exercise nine retained result/hit mutations: wrong envelope document/PDF identity, unknown page, duplicated hit with updated row count, zero/fractional/string occurrence count, altered raw context, or wrong hits hash. Expect a controlled error in every case; copied frames isolate edits from the original result and hashes are not coordinated to the edits. |
| `test_search_hit_lineage_mutation_fails` | pytest.mark.parametrize("column", ["document_id", "pdf_sha256"]) | pytest.raises(PlanningRegulationIndexError, match="lineage") | 0 | Change one hit's document_id or pdf_sha256 while retaining correct outer lineage and expect the specific lineage error. This independently targets row lineage rather than only the envelope. |
| `test_invalid_search_term_is_rejected` | pytest.mark.parametrize("term", ["", "   ", " term", "term ", 7]) | pytest.raises(PlanningRegulationIndexError, match="search term") | 0 | Pass one empty, whitespace-only, edge-whitespace, or nonstring integer term in a list; require a search term error for all five cases. Input list typing is intentionally violated for the integer case. |
| `test_duplicate_normalized_search_terms_are_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="unique") | 0 | Search both énergie and ENERGIE and require a unique error, showing duplicate detection occurs after normalization rather than on raw spelling. |
| `test_empty_search_result_has_stable_schema_and_lineage` | none | none | 5 | Search batterie in a nonmatching page, then assert zero count, empty hits, exact column order, retained document/PDF identity, and successful validation. This is a no-match request, not an empty requested-term tuple test; it does not directly assert each dtype. |
| `test_malformed_page_value_raises_controlled_index_error` | none | pytest.raises(PlanningRegulationIndexError) | 0 | Put a list in the copied page extraction_error cell and require the public index validator to return a controlled stage error rather than leaking pandas ambiguous-null behavior. No exact message or cause is required. |
| `test_malformed_hit_value_raises_controlled_index_error` | none | pytest.raises(PlanningRegulationIndexError) | 0 | Put a list into a copied hit raw_context cell and require a controlled result-validation error. No real PDF text or original hit table is modified. |
| `test_canonical_hash_serialization_failure_is_controlled_and_chained` | none | pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="serialized",<br>    ) | 1 | Pass a bare object leaf to the private canonical JSON hasher. Require a serialized stage error with a TypeError cause; no digest is successfully produced and no fallback repr is accepted. |
| `test_malformed_source_metadata_raises_controlled_index_error` | none | pytest.raises(PlanningRegulationIndexError) | 0 | Replace written_files with an exact tuple containing a bare object and expect controlled public indexing failure. The test deliberately constructs an invalid dataclass graph and does not assert a particular inner metadata gate. |
| `test_extraction_and_search_do_not_mutate_inputs` | none | none | 1 | Deep-copy extraction metadata and zoning data, index through a reader double, snapshot the pages, then search. Assert extraction equality, exact GeoDataFrame equality for zoning, and pandas frame equality for pages. This is a bounded successful-path no-input-mutation regression, not deep immutability of the output tables. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Temporary fixture writes, source-validator reads, hash calculations, copied-frame mutations, failed frozen assignment, and restored monkeypatches are distinguished in each callable's effects and limits.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from __future__ import annotations

import json
from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from importlib import import_module
from pathlib import Path
from re import fullmatch
from urllib.parse import quote

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import Polygon

from landscout import stages
from landscout.common.planning_text import (
    normalize_planning_search_text as _normalize_search_text,
)
from landscout.sources import gpu_fr as gpu_source_module
from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)
from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)

regulation_module = import_module("landscout.stages.index_planning_regulation")

DOCUMENT_ID = "doc-1"
ARCHIVE_SHA = "a" * 64
DEFAULT_PDF = "31395_reglement_20240215.pdf"
PDF_BYTES = b"synthetic-pdf-bytes"


class _FakePage:
    def __init__(self, result: object) -> None:
        self.result = result

    def extract_text(self) -> object:
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


class _FakeReader:
    def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
        self.pages = [_FakePage(page) for page in pages]
        self.is_encrypted = encrypted


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
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
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


def _inventory_item(relative_path: str, data: bytes = PDF_BYTES) -> GpuExtractedFile:
    return GpuExtractedFile(
        relative_path=relative_path,
        file_type="pdf",
        size_bytes=len(data),
        sha256=sha256(data).hexdigest(),
        category="WRITTEN_REGULATION",
    )


def _spatial_inventory_item(root: Path, path: Path) -> GpuExtractedFile:
    data = path.read_bytes()
    return GpuExtractedFile(
        relative_path=path.relative_to(root).as_posix(),
        file_type=path.suffix.lower().lstrip(".") or "binary",
        size_bytes=len(data),
        sha256=sha256(data).hexdigest(),
        category="SPATIAL_DATA",
    )


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


def _document(
    root: Path,
    inventory: tuple[GpuExtractedFile, ...],
    zoning: GpuInspectedLayer,
    *,
    zoning_filenames: list[object] | None = None,
    written_filenames: tuple[str, ...] = (DEFAULT_PDF,),
) -> GpuPlanningDocument:
    inventory = tuple(sorted(inventory, key=lambda item: item.relative_path))
    base_config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    written = tuple(
        GpuWrittenFile(
            filename=value,
            title=None,
            document_path=None,
            source_url=(
                f"{str(base_config.api.base_url).rstrip('/')}/document/"
                f"{quote(DOCUMENT_ID, safe='')}/files/{quote(value, safe='')}"
            ),
        )
        for value in written_filenames
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
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
    config_payload = base_config.model_dump(mode="python")
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]
    source_config = GpuSourceConfig.model_validate(config_payload)
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=(zoning.reference,),
        zoning=zoning,
        related_layers=(),
    )


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
    inventory_names = (
        (filename,) if inventory_filenames is None else inventory_filenames
    )
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
        written_filenames=(filename,)
        if written_filenames is None
        else written_filenames,
    )


def _one_page_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str = "Énergie",
):
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [text])
    return index_planning_regulation(document)


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


@pytest.mark.parametrize(
    "filename",
    [DEFAULT_PDF, "98765_reglement_20300102.pdf"],
)
def test_source_nomfic_resolves_generic_filename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    filename: str,
) -> None:
    document = _fixture_document(tmp_path, filename=filename)
    _patch_reader(monkeypatch, ["Texte"])
    result = index_planning_regulation(document)
    assert Path(result.pdf_relative_path).name == filename


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


@pytest.mark.parametrize("source_format", ["GPKG", "ESRI Shapefile"])
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


def test_mutated_loaded_nomfic_is_rejected_before_selection(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    mutated = document.zoning.data.copy(deep=True)
    mutated.loc[0, "NOMFIC"] = "other_reglement.pdf"
    corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
    with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)


@pytest.mark.parametrize("mutation", ["reorder", "geometry"])
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


def test_zoning_source_bytes_changed_after_ingestion_are_rejected(
    tmp_path: Path,
) -> None:
    document = _fixture_document(tmp_path)
    with document.zoning.reference.dataset_path.open("ab") as stream:
        stream.write(b"tamper")
    with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(document)


@pytest.mark.parametrize("field", ["size_bytes", "sha256"])
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
    replacement: object = current.size_bytes + 1 if field == "size_bytes" else "b" * 64
    items[position] = replace(current, **{field: replacement})
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(corrupted)


def test_missing_nomfic_field_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, include_nomfic=False)
    with pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC"):
        index_planning_regulation(document)


def test_null_nomfic_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, zoning_filenames=[None])
    with pytest.raises(PlanningRegulationIndexError, match="no regulation filename"):
        index_planning_regulation(document)


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


@pytest.mark.parametrize(
    "filename",
    [
        "",
        " file.pdf",
        "file.pdf ",
        "../file.pdf",
        "a/b.pdf",
        "C:\\a.pdf",
        "bad\x00.pdf",
        "file.txt",
    ],
)
def test_unsafe_explicit_filename_is_rejected(tmp_path: Path, filename: str) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="filename"):
        index_planning_regulation(document, regulation_filename=filename)


def test_explicit_filename_not_referenced_by_zoning_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="not referenced"):
        index_planning_regulation(document, regulation_filename="other.pdf")


def test_filename_absent_from_written_files_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, written_filenames=("other.pdf",))
    with pytest.raises(PlanningRegulationIndexError, match="written_files"):
        index_planning_regulation(document)


def test_unrelated_non_pdf_written_file_does_not_block_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(
        tmp_path, written_filenames=(DEFAULT_PDF, "technical-note.txt")
    )
    _patch_reader(monkeypatch, ["Texte"])
    assert index_planning_regulation(document).total_page_count == 1


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


def test_duplicate_inventory_basename_fails(tmp_path: Path) -> None:
    document = _fixture_document(
        tmp_path, inventory_filenames=(DEFAULT_PDF, DEFAULT_PDF)
    )
    with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)


def test_path_outside_root_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item = replace(document.extraction.files[0], relative_path=f"../{DEFAULT_PDF}")
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=(item,)),
    )
    with pytest.raises(
        PlanningRegulationIndexError,
        match="unsafe|verified manifest",
    ):
        index_planning_regulation(corrupted)


@pytest.mark.parametrize("field", ["size_bytes", "sha256"])
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
        result.total_page_count = 9  # type: ignore[misc]


def test_zero_page_pdf_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [])
    with pytest.raises(PlanningRegulationIndexError, match="at least one page"):
        index_planning_regulation(document)


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


@pytest.mark.parametrize(
    ("source", "term"),
    [
        ("ÉNERGIE", "energie"),
        ("intérêt", "interet"),
        ("d’intérêt", "d'interet"),
        ("œuvre", "oeuvre"),
        ("ÆTHER", "aether"),
        ("poste—source", "poste-source"),
        ("inter\u00adruption", "interruption"),
        ("ligne\n   électrique", "ligne electrique"),
    ],
)
def test_french_literal_normalization(source: str, term: str) -> None:
    assert _normalize_search_text(source) == term


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


@pytest.mark.parametrize(
    ("raw", "term", "expected_raw", "expected_normalized"),
    [
        ("café", "cafe", "café", "cafe"),
        ("cafe\u0301", "cafe", "cafe\u0301", "cafe"),
        ("œuvre", "oeuvre", "œuvre", "oeuvre"),
        ("æther", "aether", "æther", "aether"),
        ("d’intérêt", "d'interet", "d’intérêt", "d'interet"),
        ("inter\u00adruption", "interruption", "inter\u00adruption", "interruption"),
        ("\u00adcafe", "cafe", "\u00adcafe", "cafe"),
        ("cafe\u00ad", "cafe", "cafe\u00ad", "cafe"),
    ],
)
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


def test_literal_search_does_not_add_semantic_synonyms(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, "Une batterie est mentionnée.")
    result = search_planning_regulation(index, ["accumulateur"])
    assert result.hits.empty


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


@pytest.mark.parametrize(
    ("target", "value"),
    [
        ("page_hash", "b" * 64),
        ("envelope_hash", "b" * 64),
        ("profile", "other_v1"),
        ("order", None),
    ],
)
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


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("document_id", "other-document"),
        ("archive_sha256", "b" * 64),
        ("regulation_filename", "other_reglement.pdf"),
        ("source_selection_method", "EXPLICIT_FILENAME"),
        ("source_selection_sha256", "b" * 64),
        ("pdf_relative_path", "written-0/other_reglement.pdf"),
        ("pdf_size_bytes", len(PDF_BYTES) + 1),
        ("pdf_sha256", "b" * 64),
        ("extraction_library", "other-reader"),
        ("extraction_library_version", "0.0.0"),
        ("search_normalization_profile", "other-profile"),
        ("page_hash_schema_version", 2),
        ("total_page_count", 2),
        ("pages_content_sha256", "b" * 64),
        ("index_content_sha256", "b" * 64),
    ],
)
def test_complete_index_envelope_mutation_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, **{field: replacement}))


@pytest.mark.parametrize("replacement", [0, -1, 1.5, "1", 2])
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


@pytest.mark.parametrize("replacement", [0, -1, 1.5, "1"])
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


def test_search_result_envelope_is_valid_and_deterministic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index, first = _valid_search_result(tmp_path, monkeypatch)
    second = search_planning_regulation(index, first.requested_terms)
    assert tuple(first.hits.columns) == SEARCH_HIT_COLUMNS
    assert first.search_normalization_profile == SEARCH_NORMALIZATION_PROFILE
    assert first.index_content_sha256 == index.index_content_sha256
    assert (
        first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION
    )
    assert first.hit_count == 2
    assert_frame_equal(first.hits, second.hits)
    assert first.hits_content_sha256 == second.hits_content_sha256
    validate_planning_regulation_search_result(index, first)


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("index_content_sha256", "b" * 64),
        ("search_hash_schema_version", 2),
        ("search_hash_schema_version", 0),
        ("search_hash_schema_version", -1),
        ("search_hash_schema_version", 1.5),
        ("search_hash_schema_version", "1"),
        ("requested_terms", ("other-term",)),
    ],
)
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


@pytest.mark.parametrize(
    ("target", "value"),
    [
        ("document_id", "wrong"),
        ("pdf_sha256", "b" * 64),
        ("page_number", 99),
        ("duplicate", None),
        ("occurrence_count", 0),
        ("occurrence_count", 1.5),
        ("occurrence_count", "1"),
        ("raw_context", "corrupted"),
        ("hits_content_sha256", "b" * 64),
    ],
)
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


@pytest.mark.parametrize("column", ["document_id", "pdf_sha256"])
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


@pytest.mark.parametrize("term", ["", "   ", " term", "term ", 7])
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="search term"):
        search_planning_regulation(index, [term])  # type: ignore[list-item]


def test_duplicate_normalized_search_terms_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="unique"):
        search_planning_regulation(index, ["énergie", "ENERGIE"])


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


def test_malformed_page_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    pages = index.pages.copy(deep=True)
    pages.at[0, "extraction_error"] = ["ambiguous", "value"]
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, pages=pages))


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


def test_canonical_hash_serialization_failure_is_controlled_and_chained() -> None:
    invalid_payload = {"not_json": object()}
    with pytest.raises(
        PlanningRegulationIndexError,
        match="serialized",
    ) as caught:
        regulation_module._canonical_sha256(invalid_payload)
    assert isinstance(caught.value.__cause__, TypeError)


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
