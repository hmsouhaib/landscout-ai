# `tests/unit/test_index_planning_regulation.py`

## File identity

- Repository path: `tests/unit/test_index_planning_regulation.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.
- Source SHA256: `e36baad245c33bef983f78bb49fc8060bc4e45152c420c5d658f2853d742df8b`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for index planning regulation; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_FakePage`

**Source purpose:** Defines `_FakePage`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `result` | `assigned instance field` | `result` | `self.result = result` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

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

**Source purpose:** Defines `_FakeReader`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `pages` | `assigned instance field` | `[_FakePage(page) for page in pages]` | `self.pages = [_FakePage(page) for page in pages]` |
| `is_encrypted` | `assigned instance field` | `encrypted` | `self.is_encrypted = encrypted` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

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

**Purpose:** Implements `init` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

**Exact signature**

```python
def __init__(self, result: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `result` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
| In-memory mutation | `self.result = result` |
| Direct parameter mutation | `self.result = result` |

**Complete source-ordered implementation**

```python
def __init__(self, result: object) -> None:
        self.result = result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakePage.extract_text`

**Purpose:** Implements `extract text` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

**Exact signature**

```python
def extract_text(self) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

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
def extract_text(self) -> object:
        if isinstance(self.result, Exception):
            raise self.result
        return self.result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeReader.__init__`

**Purpose:** Implements `init` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

**Exact signature**

```python
def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
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
| In-memory mutation | `self.pages = [_FakePage(page) for page in pages]`<br>`self.is_encrypted = encrypted` |
| Direct parameter mutation | `self.pages = [_FakePage(page) for page in pages]`<br>`self.is_encrypted = encrypted` |

**Complete source-ordered implementation**

```python
def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
        self.pages = [_FakePage(page) for page in pages]
        self.is_encrypted = encrypted
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_patch_reader`

**Purpose:** Implements `patch reader` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

**Purpose:** Implements `summary` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.notna`<br>`geometry.geom_type.value_counts().sort_index().items`<br>`geometry.geom_type.value_counts().sort_index`<br>`geometry.geom_type.value_counts`<br>`(non_null & geometry.is_empty).sum`<br>`(non_empty & ~geometry.is_valid).sum` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Implements `zone frame` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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
| In-memory mutation | `attributes["NOMFIC"] = filenames` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Implements `inventory item` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(data).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Implements `spatial inventory item` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(data).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Implements `write zoning source` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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
  - `AssertionError(f"Unsupported test source format: {source_format}")` under lexical guard `source_format == "GPKG"`.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file`<br>`path.parent.glob`<br>`candidate.is_file` |
| Filesystem/archive write or publication | `spatial_root.mkdir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Implements `document` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `marker.write_text` |
| Hashing/byte identity | `gpu_source_module._source_config_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Implements `fixture document` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.parent.mkdir`<br>`path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inventory.append(_inventory_item(relative))`<br>`inventory.extend(spatial_inventory)` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Implements `one page index` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

**Exact signature**

```python
def _one_page_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str = "Énergie",
):
```

- Exact decorators: none.
- Declared return annotation: `None`.

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

**Purpose:** Regression invariant: public api exports immutable models and validators. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: source nomfic resolves generic filename. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: explicit source validated selection succeeds. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: unchanged zoning source is revalidated before selection. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: mutated loaded nomfic is rejected before selection. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `mutated.loc[0, "NOMFIC"] = "other_reglement.pdf"` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: mutated loaded zoning geometry or order is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `mutated.geometry.copy`<br>`mutated.set_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | `geometry.iloc[0] = Polygon([(20, 0), (20, 1), (21, 1), (21, 0), (20, 0)])`<br>`mutated.set_geometry(geometry)` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: zoning source bytes changed after ingestion are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `document.zoning.reference.dataset_path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: zoning source inventory integrity mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `items[position] = replace(current, **{field: replacement})` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: missing nomfic field is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
def test_missing_nomfic_field_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, include_nomfic=False)
    with pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC"):
        index_planning_regulation(document)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_nomfic_is_rejected`

**Purpose:** Regression invariant: null nomfic is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
def test_null_nomfic_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, zoning_filenames=[None])
    with pytest.raises(PlanningRegulationIndexError, match="no regulation filename"):
        index_planning_regulation(document)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_multiple_nomfic_values_are_ambiguous`

**Purpose:** Regression invariant: multiple nomfic values are ambiguous. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: unsafe explicit filename is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
def test_unsafe_explicit_filename_is_rejected(tmp_path: Path, filename: str) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="filename"):
        index_planning_regulation(document, regulation_filename=filename)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_explicit_filename_not_referenced_by_zoning_fails`

**Purpose:** Regression invariant: explicit filename not referenced by zoning fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
def test_explicit_filename_not_referenced_by_zoning_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="not referenced"):
        index_planning_regulation(document, regulation_filename="other.pdf")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_filename_absent_from_written_files_fails`

**Purpose:** Regression invariant: filename absent from written files fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
def test_filename_absent_from_written_files_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, written_filenames=("other.pdf",))
    with pytest.raises(PlanningRegulationIndexError, match="written_files"):
        index_planning_regulation(document)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unrelated_non_pdf_written_file_does_not_block_selection`

**Purpose:** Regression invariant: unrelated non pdf written file does not block selection. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: filename absent from inventory fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `items[item_position] = replace(<br>        items[item_position], relative_path="written/other.pdf"<br>    )` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: duplicate inventory basename fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: path outside root is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: pdf inventory integrity mismatch fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `items[item_position] = replace(items[item_position], **{field: value})` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: page states numbering and hashes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `result.pages.extraction_status.tolist` |
| Hashing/byte identity | `result.pages.page_content_sha256.str.fullmatch(r"[0-9a-f]{64}").all`<br>`result.pages.page_content_sha256.str.fullmatch` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `result.total_page_count = 9` |
| Direct parameter mutation | None directly present. |

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
        result.total_page_count = 9
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zero_page_pdf_is_rejected`

**Purpose:** Regression invariant: zero page pdf is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: pdf reader failure is controlled and chained. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Implements `fail reader` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RuntimeError("broken xref")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RuntimeError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_reader(*args: object, **kwargs: object) -> object:
        raise RuntimeError("broken xref")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_french_literal_normalization`

**Purpose:** Regression invariant: french literal normalization. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
def test_french_literal_normalization(source: str, term: str) -> None:
    assert _normalize_search_text(source) == term
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_raw_context_preserves_source_typography`

**Purpose:** Regression invariant: raw context preserves source typography. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: zero context preserves complete raw unicode span. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: literal search does not add semantic synonyms. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: version discovery failure is controlled and chained. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Implements `fail version` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

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

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RuntimeError(name)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RuntimeError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_version(name: str) -> str:
        raise RuntimeError(name)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_page_mutation_fails_envelope_hash`

**Purpose:** Regression invariant: coordinated page mutation fails envelope hash. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| `regulation_module._page_content_sha256` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `regulation_module._page_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `pages.loc[0, "raw_text"] = "Nouveau"`<br>`pages.loc[0, "normalized_search_text"] = "nouveau"`<br>`pages.loc[0, "character_count"] = 7`<br>`pages.loc[0, "page_content_sha256"] = regulation_module._page_content_sha256(row)` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: index integrity mutations fail. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `pages.loc[0, "page_content_sha256"] = value` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: complete index envelope mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: unsupported or malformed index hash schema is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: malformed page hash schema is rejected as controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Implements `valid search result` within the file role: Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file.

**Exact signature**

```python
def _valid_search_result(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
```

- Exact decorators: none.
- Declared return annotation: `None`.

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

**Purpose:** Regression invariant: search result envelope is valid and deterministic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: search index identity schema and terms are sealed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: search requested terms must be an immutable exact tuple. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: search result integrity mutations fail. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `hits[target] = hits[target].astype(object)`<br>`hits.loc[0, target] = value` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: search hit lineage mutation fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `hits.loc[0, column] = "b" * 64 if column == "pdf_sha256" else "wrong"` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: invalid search term is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="search term"):
        search_planning_regulation(index, [term])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_normalized_search_terms_are_rejected`

**Purpose:** Regression invariant: duplicate normalized search terms are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: empty search result has stable schema and lineage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: malformed page value raises controlled index error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `pages.at[0, "extraction_error"] = ["ambiguous", "value"]` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: malformed hit value raises controlled index error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| In-memory mutation | `hits["raw_context"] = hits["raw_context"].astype(object)`<br>`hits.at[0, "raw_context"] = ["not", "text"]` |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: canonical hash serialization failure is controlled and chained. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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
| `regulation_module._canonical_sha256` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `regulation_module._canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

**Purpose:** Regression invariant: malformed source metadata raises controlled index error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

**Purpose:** Regression invariant: extraction and search do not mutate inputs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

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

- Test functions: **45**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_public_api_exports_immutable_models_and_validators` | none | none | 2 | Proves public api exports immutable models and validators using the exact source reproduced in section 7. |
| `test_source_nomfic_resolves_generic_filename` | pytest.mark.parametrize(<br>    "filename",<br>    [DEFAULT_PDF, "98765_reglement_20300102.pdf"],<br>) | none | 1 | Proves source nomfic resolves generic filename using the exact source reproduced in section 7. |
| `test_explicit_source_validated_selection_succeeds` | none | none | 1 | Proves explicit source validated selection succeeds using the exact source reproduced in section 7. |
| `test_unchanged_zoning_source_is_revalidated_before_selection` | pytest.mark.parametrize("source_format", ["GPKG", "ESRI Shapefile"]) | none | 3 | Proves unchanged zoning source is revalidated before selection using the exact source reproduced in section 7. |
| `test_mutated_loaded_nomfic_is_rejected_before_selection` | none | pytest.raises(PlanningRegulationIndexError, match="zoning\|source") | 0 | Proves mutated loaded nomfic is rejected before selection using the exact source reproduced in section 7. |
| `test_mutated_loaded_zoning_geometry_or_order_is_rejected` | pytest.mark.parametrize("mutation", ["reorder", "geometry"]) | pytest.raises(PlanningRegulationIndexError, match="zoning\|source") | 0 | Proves mutated loaded zoning geometry or order is rejected using the exact source reproduced in section 7. |
| `test_zoning_source_bytes_changed_after_ingestion_are_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="size\|SHA256\|integrity") | 0 | Proves zoning source bytes changed after ingestion are rejected using the exact source reproduced in section 7. |
| `test_zoning_source_inventory_integrity_mismatch_is_rejected` | pytest.mark.parametrize("field", ["size_bytes", "sha256"]) | pytest.raises(PlanningRegulationIndexError, match="size\|SHA256\|integrity") | 0 | Proves zoning source inventory integrity mismatch is rejected using the exact source reproduced in section 7. |
| `test_missing_nomfic_field_is_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC") | 0 | Proves missing nomfic field is rejected using the exact source reproduced in section 7. |
| `test_null_nomfic_is_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="no regulation filename") | 0 | Proves null nomfic is rejected using the exact source reproduced in section 7. |
| `test_multiple_nomfic_values_are_ambiguous` | none | pytest.raises(PlanningRegulationIndexError, match="ambiguous") | 0 | Proves multiple nomfic values are ambiguous using the exact source reproduced in section 7. |
| `test_unsafe_explicit_filename_is_rejected` | pytest.mark.parametrize(<br>    "filename",<br>    [<br>        "",<br>        " file.pdf",<br>        "file.pdf ",<br>        "../file.pdf",<br>        "a/b.pdf",<br>        "C:\\a.pdf",<br>        "bad\x00.pdf",<br>        "file.txt",<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError, match="filename") | 0 | Proves unsafe explicit filename is rejected using the exact source reproduced in section 7. |
| `test_explicit_filename_not_referenced_by_zoning_fails` | none | pytest.raises(PlanningRegulationIndexError, match="not referenced") | 0 | Proves explicit filename not referenced by zoning fails using the exact source reproduced in section 7. |
| `test_filename_absent_from_written_files_fails` | none | pytest.raises(PlanningRegulationIndexError, match="written_files") | 0 | Proves filename absent from written files fails using the exact source reproduced in section 7. |
| `test_unrelated_non_pdf_written_file_does_not_block_selection` | none | none | 1 | Proves unrelated non pdf written file does not block selection using the exact source reproduced in section 7. |
| `test_filename_absent_from_inventory_fails` | none | pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="missing from GPU inventory\|verified manifest",<br>    ) | 0 | Proves filename absent from inventory fails using the exact source reproduced in section 7. |
| `test_duplicate_inventory_basename_fails` | none | pytest.raises(PlanningRegulationIndexError, match="ambiguous") | 0 | Proves duplicate inventory basename fails using the exact source reproduced in section 7. |
| `test_path_outside_root_is_rejected` | none | pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="unsafe\|verified manifest",<br>    ) | 0 | Proves path outside root is rejected using the exact source reproduced in section 7. |
| `test_pdf_inventory_integrity_mismatch_fails` | pytest.mark.parametrize("field", ["size_bytes", "sha256"]) | pytest.raises(PlanningRegulationIndexError, match="differs") | 0 | Proves pdf inventory integrity mismatch fails using the exact source reproduced in section 7. |
| `test_page_states_numbering_and_hashes` | none | pytest.raises(FrozenInstanceError) | 7 | Proves page states numbering and hashes using the exact source reproduced in section 7. |
| `test_zero_page_pdf_is_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="at least one page") | 0 | Proves zero page pdf is rejected using the exact source reproduced in section 7. |
| `test_pdf_reader_failure_is_controlled_and_chained` | none | pytest.raises(<br>        PlanningRegulationIndexError, match="opened or parsed"<br>    ) | 1 | Proves pdf reader failure is controlled and chained using the exact source reproduced in section 7. |
| `test_french_literal_normalization` | pytest.mark.parametrize(<br>    ("source", "term"),<br>    [<br>        ("ÉNERGIE", "energie"),<br>        ("intérêt", "interet"),<br>        ("d’intérêt", "d'interet"),<br>        ("œuvre", "oeuvre"),<br>        ("ÆTHER", "aether"),<br>        ("poste—source", "poste-source"),<br>        ("inter\u00adruption", "interruption"),<br>        ("ligne\n   électrique", "ligne electrique"),<br>    ],<br>) | none | 1 | Proves french literal normalization using the exact source reproduced in section 7. |
| `test_raw_context_preserves_source_typography` | none | none | 5 | Proves raw context preserves source typography using the exact source reproduced in section 7. |
| `test_zero_context_preserves_complete_raw_unicode_span` | pytest.mark.parametrize(<br>    ("raw", "term", "expected_raw", "expected_normalized"),<br>    [<br>        ("café", "cafe", "café", "cafe"),<br>        ("cafe\u0301", "cafe", "cafe\u0301", "cafe"),<br>        ("œuvre", "oeuvre", "œuvre", "oeuvre"),<br>        ("æther", "aether", "æther", "aether"),<br>        ("d’intérêt", "d'interet", "d’intérêt", "d'interet"),<br>        ("inter\u00adruption", "interruption", "inter\u00adruption", "interruption"),<br>        ("\u00adcafe", "cafe", "\u00adcafe", "cafe"),<br>        ("cafe\u00ad", "cafe", "cafe\u00ad", "cafe"),<br>    ],<br>) | none | 4 | Proves zero context preserves complete raw unicode span using the exact source reproduced in section 7. |
| `test_literal_search_does_not_add_semantic_synonyms` | none | none | 1 | Proves literal search does not add semantic synonyms using the exact source reproduced in section 7. |
| `test_version_discovery_failure_is_controlled_and_chained` | none | pytest.raises(PlanningRegulationIndexError, match="version") | 1 | Proves version discovery failure is controlled and chained using the exact source reproduced in section 7. |
| `test_coordinated_page_mutation_fails_envelope_hash` | none | pytest.raises(PlanningRegulationIndexError, match="envelope") | 0 | Proves coordinated page mutation fails envelope hash using the exact source reproduced in section 7. |
| `test_index_integrity_mutations_fail` | pytest.mark.parametrize(<br>    ("target", "value"),<br>    [<br>        ("page_hash", "b" * 64),<br>        ("envelope_hash", "b" * 64),<br>        ("profile", "other_v1"),<br>        ("order", None),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Proves index integrity mutations fail using the exact source reproduced in section 7. |
| `test_complete_index_envelope_mutation_is_rejected` | pytest.mark.parametrize(<br>    ("field", "replacement"),<br>    [<br>        ("document_id", "other-document"),<br>        ("archive_sha256", "b" * 64),<br>        ("regulation_filename", "other_reglement.pdf"),<br>        ("source_selection_method", "EXPLICIT_FILENAME"),<br>        ("source_selection_sha256", "b" * 64),<br>        ("pdf_relative_path", "written-0/other_reglement.pdf"),<br>        ("pdf_size_bytes", len(PDF_BYTES) + 1),<br>        ("pdf_sha256", "b" * 64),<br>        ("extraction_library", "other-reader"),<br>        ("extraction_library_version", "0.0.0"),<br>        ("search_normalization_profile", "other-profile"),<br>        ("page_hash_schema_version", 2),<br>        ("total_page_count", 2),<br>        ("pages_content_sha256", "b" * 64),<br>        ("index_content_sha256", "b" * 64),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Proves complete index envelope mutation is rejected using the exact source reproduced in section 7. |
| `test_unsupported_or_malformed_index_hash_schema_is_rejected` | pytest.mark.parametrize("replacement", [0, -1, 1.5, "1", 2]) | pytest.raises(PlanningRegulationIndexError) | 0 | Proves unsupported or malformed index hash schema is rejected using the exact source reproduced in section 7. |
| `test_malformed_page_hash_schema_is_rejected_as_controlled_error` | pytest.mark.parametrize("replacement", [0, -1, 1.5, "1"]) | pytest.raises(PlanningRegulationIndexError) | 0 | Proves malformed page hash schema is rejected as controlled error using the exact source reproduced in section 7. |
| `test_search_result_envelope_is_valid_and_deterministic` | none | none | 6 | Proves search result envelope is valid and deterministic using the exact source reproduced in section 7. |
| `test_search_index_identity_schema_and_terms_are_sealed` | pytest.mark.parametrize(<br>    ("field", "replacement"),<br>    [<br>        ("index_content_sha256", "b" * 64),<br>        ("search_hash_schema_version", 2),<br>        ("search_hash_schema_version", 0),<br>        ("search_hash_schema_version", -1),<br>        ("search_hash_schema_version", 1.5),<br>        ("search_hash_schema_version", "1"),<br>        ("requested_terms", ("other-term",)),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Proves search index identity schema and terms are sealed using the exact source reproduced in section 7. |
| `test_search_requested_terms_must_be_an_immutable_exact_tuple` | none | pytest.raises(PlanningRegulationIndexError, match="tuple") | 0 | Proves search requested terms must be an immutable exact tuple using the exact source reproduced in section 7. |
| `test_search_result_integrity_mutations_fail` | pytest.mark.parametrize(<br>    ("target", "value"),<br>    [<br>        ("document_id", "wrong"),<br>        ("pdf_sha256", "b" * 64),<br>        ("page_number", 99),<br>        ("duplicate", None),<br>        ("occurrence_count", 0),<br>        ("occurrence_count", 1.5),<br>        ("occurrence_count", "1"),<br>        ("raw_context", "corrupted"),<br>        ("hits_content_sha256", "b" * 64),<br>    ],<br>) | pytest.raises(PlanningRegulationIndexError) | 0 | Proves search result integrity mutations fail using the exact source reproduced in section 7. |
| `test_search_hit_lineage_mutation_fails` | pytest.mark.parametrize("column", ["document_id", "pdf_sha256"]) | pytest.raises(PlanningRegulationIndexError, match="lineage") | 0 | Proves search hit lineage mutation fails using the exact source reproduced in section 7. |
| `test_invalid_search_term_is_rejected` | pytest.mark.parametrize("term", ["", "   ", " term", "term ", 7]) | pytest.raises(PlanningRegulationIndexError, match="search term") | 0 | Proves invalid search term is rejected using the exact source reproduced in section 7. |
| `test_duplicate_normalized_search_terms_are_rejected` | none | pytest.raises(PlanningRegulationIndexError, match="unique") | 0 | Proves duplicate normalized search terms are rejected using the exact source reproduced in section 7. |
| `test_empty_search_result_has_stable_schema_and_lineage` | none | none | 5 | Proves empty search result has stable schema and lineage using the exact source reproduced in section 7. |
| `test_malformed_page_value_raises_controlled_index_error` | none | pytest.raises(PlanningRegulationIndexError) | 0 | Proves malformed page value raises controlled index error using the exact source reproduced in section 7. |
| `test_malformed_hit_value_raises_controlled_index_error` | none | pytest.raises(PlanningRegulationIndexError) | 0 | Proves malformed hit value raises controlled index error using the exact source reproduced in section 7. |
| `test_canonical_hash_serialization_failure_is_controlled_and_chained` | none | pytest.raises(<br>        PlanningRegulationIndexError,<br>        match="serialized",<br>    ) | 1 | Proves canonical hash serialization failure is controlled and chained using the exact source reproduced in section 7. |
| `test_malformed_source_metadata_raises_controlled_index_error` | none | pytest.raises(PlanningRegulationIndexError) | 0 | Proves malformed source metadata raises controlled index error using the exact source reproduced in section 7. |
| `test_extraction_and_search_do_not_mutate_inputs` | none | none | 1 | Proves extraction and search do not mutate inputs using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

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
