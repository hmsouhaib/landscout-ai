# `tests/integration/test_gpu_planning_end_to_end.py`

## File identity

- Repository path: `tests/integration/test_gpu_planning_end_to_end.py`
- File type: Python source
- Layer: integration regression
- Domain: physical end-to-end test evidence
- Responsibility: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.
- Source SHA256: `384fc848b7c1ddbedbc45fc20374546970381ab2549379e7b256a6ef1076247f`

## 1. STEP 7F.1A.4 contract delta

- Adds the physical GPU planning chain regression over real synthetic GPKG/PDF/ZIP bytes, including source mutation, config mismatch, and required-article omission failures.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

The file belongs to the **integration regression** layer and **physical end-to-end test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import dataclass, replace`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from urllib.parse import quote`
- `from zipfile import ZIP_DEFLATED, ZipFile`

### Third-party packages

- `import geopandas as gpd`
- `import pytest`
- `from pypdf import PdfWriter`
- `from pypdf.generic import (
    DecodedStreamObject,
    DictionaryObject,
    NameObject,
)`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    intersect_parcels_with_gpu_zoning,
)`
- `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    index_planning_regulation,
)`
- `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)`
- `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureResult,
    structure_planning_regulation,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `_ARCHIVE_NAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
_ARCHIVE_NAME = "synthetic_gpu_document"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_DOCUMENT_ID`

- Category: module constant or closed domain.
- Exact declaration:

```python
_DOCUMENT_ID = "synthetic-document"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_REGULATION_FILENAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
_REGULATION_FILENAME = "reglement.pdf"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_PhysicalPlanningChain`

**Source purpose:** Defines `_PhysicalPlanningChain`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `planning_document` | `GpuPlanningDocument` | `required` | `planning_document: GpuPlanningDocument` |
| `zoning` | `ParcelZoningResult` | `required` | `zoning: ParcelZoningResult` |
| `index` | `PlanningRegulationIndex` | `required` | `index: PlanningRegulationIndex` |
| `structure_config` | `PlanningRegulationStructureConfig` | `required` | `structure_config: PlanningRegulationStructureConfig` |
| `structure` | `PlanningRegulationStructureResult` | `required` | `structure: PlanningRegulationStructureResult` |
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |
| `policy` | `BessZoningPolicyConfig` | `required` | `policy: BessZoningPolicyConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_PhysicalPlanningChain`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_PhysicalPlanningChain`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_interpret` via `_PhysicalPlanningChain`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_validate` via `_PhysicalPlanningChain`

**Exact class source**

```python
class _PhysicalPlanningChain:
    planning_document: GpuPlanningDocument
    zoning: ParcelZoningResult
    index: PlanningRegulationIndex
    structure_config: PlanningRegulationStructureConfig
    structure: PlanningRegulationStructureResult
    parcels: gpd.GeoDataFrame
    policy: BessZoningPolicyConfig
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_sha256`

**Purpose:** Implements `sha256` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _sha256(path: Path) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(path.read_bytes()).hexdigest()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_sha256`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256(path.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sha256(path.read_bytes()).hexdigest`<br>`path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(path.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_text_pdf`

**Purpose:** Implements `write text pdf` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _write_text_pdf(path: Path, *, include_article_two: bool) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `include_article_two` | keyword-only | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::_write_gpu_archive` via `_write_text_pdf`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_write_gpu_archive` via `_write_text_pdf`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `lines.extend` | `unresolved local/third-party receiver; no ownership inferred` |
| `PdfWriter` | `pypdf.PdfWriter` |
| `writer.add_blank_page` | `unresolved local/third-party receiver; no ownership inferred` |
| `DictionaryObject` | `pypdf.generic.DictionaryObject` |
| `NameObject` | `pypdf.generic.NameObject` |
| `writer._add_object` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `operations.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `f"({line}) Tj".encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `DecodedStreamObject` | `pypdf.generic.DecodedStreamObject` |
| `stream.set_data` | `unresolved local/third-party receiver; no ownership inferred` |
| `b"\n".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `writer.write` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.open` |
| Filesystem/archive write or publication | `path.parent.mkdir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `lines.extend(<br>            (<br>                "ARTICLE U 2 - OTHER",<br>                "Second factual source sentence.",<br>            )<br>        )`<br>`page[NameObject("/Resources")] = DictionaryObject(<br>        {<br>            NameObject("/Font"): DictionaryObject(<br>                {NameObject("/F1"): writer._add_object(font)}<br>            )<br>        }<br>    )`<br>`operations.append(b"0 -18 Td")`<br>`operations.append(f"({line}) Tj".encode("ascii"))`<br>`operations.append(b"ET")`<br>`page[NameObject("/Contents")] = writer._add_object(stream)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_text_pdf(path: Path, *, include_article_two: bool) -> None:
    lines = [
        "ZONE U",
        "ARTICLE U 1 - USES",
        "First factual source sentence.",
    ]
    if include_article_two:
        lines.extend(
            (
                "ARTICLE U 2 - OTHER",
                "Second factual source sentence.",
            )
        )
    writer = PdfWriter()
    page = writer.add_blank_page(width=612, height=792)
    font = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject("/Helvetica"),
        }
    )
    page[NameObject("/Resources")] = DictionaryObject(
        {
            NameObject("/Font"): DictionaryObject(
                {NameObject("/F1"): writer._add_object(font)}
            )
        }
    )
    operations = [b"BT", b"/F1 12 Tf", b"72 720 Td"]
    for position, line in enumerate(lines):
        if position:
            operations.append(b"0 -18 Td")
        operations.append(f"({line}) Tj".encode("ascii"))
    operations.append(b"ET")
    stream = DecodedStreamObject()
    stream.set_data(b"\n".join(operations))
    page[NameObject("/Contents")] = writer._add_object(stream)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as output:
        writer.write(output)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_gpu_archive`

**Purpose:** Implements `write gpu archive` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _write_gpu_archive(
    tmp_path: Path,
    *,
    include_article_two: bool,
) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `include_article_two` | keyword-only | `bool` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `archive_path`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_write_gpu_archive`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_write_gpu_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `package.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `zones.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_text_pdf` | `tests.integration.test_gpu_planning_end_to_end._write_text_pdf` |
| `ZipFile` | `zipfile.ZipFile` |
| `archive.write` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `ZipFile` |
| Filesystem/archive write or publication | `package.mkdir`<br>`_write_text_pdf` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_gpu_archive(
    tmp_path: Path,
    *,
    include_article_two: bool,
) -> Path:
    package = tmp_path / "package-source"
    package.mkdir()
    zoning_path = package / "planning.gpkg"
    zones = gpd.GeoDataFrame(
        {
            "LIB_IDZONE": ["ZONE-U"],
            "LIBELLE": ["U"],
            "LIBELONG": ["Zone U"],
            "TYPEZONE": ["U"],
            "NOMFIC": [_REGULATION_FILENAME],
            "URLFIC": ["https://example.invalid/reglement.pdf"],
            "IDURBA": [_ARCHIVE_NAME],
            "DATVALID": ["2026-01-01"],
        },
        geometry=[Polygon([(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)])],
        crs="EPSG:2154",
    )
    zones.to_file(
        zoning_path,
        layer="zone_urba",
        driver="GPKG",
        engine="pyogrio",
    )
    pdf_path = package / _REGULATION_FILENAME
    _write_text_pdf(pdf_path, include_article_two=include_article_two)
    archive_path = tmp_path / f"{_ARCHIVE_NAME}.zip"
    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        archive.write(zoning_path, "package/planning.gpkg")
        archive.write(pdf_path, f"package/{_REGULATION_FILENAME}")
    return archive_path
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_gpu_document`

**Purpose:** Implements `gpu document` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _gpu_document(config: GpuSourceConfig) -> GpuDocumentMetadata:
```

- Exact decorators: none.
- Declared return annotation: `GpuDocumentMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuDocumentMetadata(<br>        provider=config.provider,<br>        portal=config.portal,<br>        commune_code=config.pilot.commune_code,<br>        partition=build_gpu_partition(config),<br>        document_id=_DOCUMENT_ID,<br>        document_family="DU",<br>        document_type="PLU",<br>        document_title="Synthetic planning document",<br>        status="document.production",<br>        legal_status="APPROVED",<br>        effective_status="EN_VIGUEUR",<br>        version="1",<br>        archive_name=_ARCHIVE_NAME,<br>        publication_timestamp=None,<br>        update_timestamp=None,<br>        revision_date=None,<br>        producer=None,<br>        standard_model=None,<br>        projection="EPSG:2154",<br>        metadata_identifier=None,<br>        source_url=build_gpu_partition_download_url(config),<br>        written_files=(<br>            GpuWrittenFile(<br>                filename=_REGULATION_FILENAME,<br>                title="Synthetic regulation",<br>                document_path=None,<br>                source_url=written_url,<br>            ),<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_gpu_document`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_gpu_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `str(config.api.base_url).rstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `quote` | `urllib.parse.quote` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `build_gpu_partition` | `landscout.sources.gpu_fr.build_gpu_partition` |
| `build_gpu_partition_download_url` | `landscout.sources.gpu_fr.build_gpu_partition_download_url` |
| `GpuWrittenFile` | `landscout.sources.gpu_fr.GpuWrittenFile` |

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
def _gpu_document(config: GpuSourceConfig) -> GpuDocumentMetadata:
    written_url = (
        f"{str(config.api.base_url).rstrip('/')}/document/"
        f"{quote(_DOCUMENT_ID, safe='')}/files/"
        f"{quote(_REGULATION_FILENAME, safe='')}"
    )
    return GpuDocumentMetadata(
        provider=config.provider,
        portal=config.portal,
        commune_code=config.pilot.commune_code,
        partition=build_gpu_partition(config),
        document_id=_DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Synthetic planning document",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="1",
        archive_name=_ARCHIVE_NAME,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url=build_gpu_partition_download_url(config),
        written_files=(
            GpuWrittenFile(
                filename=_REGULATION_FILENAME,
                title="Synthetic regulation",
                document_path=None,
                source_url=written_url,
            ),
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_structure_config`

**Purpose:** Implements `structure config` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _structure_config(
    index: PlanningRegulationIndex,
) -> PlanningRegulationStructureConfig:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationStructureConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `PlanningRegulationStructureConfig.model_validate(<br>        {<br>            "schema_version": 2,<br>            "structure_profile": "synthetic_physical_v1",<br>            "document_lock": {<br>                "document_id": index.document_id,<br>                "pdf_sha256": index.pdf_sha256,<br>                "pages_content_sha256": index.pages_content_sha256,<br>                "index_content_sha256": index.index_content_sha256,<br>                "normalization_profile": index.search_normalization_profile,<br>            },<br>            "document_layout": {<br>                "body_start_page": 1,<br>                "table_of_contents_pages": [],<br>                "max_heading_continuation_lines": 0,<br>                "include_table_of_contents_in_topic_evidence": False,<br>            },<br>            "heading_patterns": {<br>                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],<br>                "article": [<br>                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"<br>                ],<br>                "general_section": [r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"],<br>                "continuation": [],<br>            },<br>            "ignored_patterns": {"page_headers": [], "page_footers": []},<br>            "zone_aliases": {},<br>            "topics": {"factual": ["factual"]},<br>            "topic_match_policy": {<br>                "boundary_mode": "token",<br>                "overlap_resolution": "longest_match",<br>            },<br>            "topic_context_characters": 10,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_structure_config`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_structure_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PlanningRegulationStructureConfig.model_validate` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig.model_validate` |

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
def _structure_config(
    index: PlanningRegulationIndex,
) -> PlanningRegulationStructureConfig:
    return PlanningRegulationStructureConfig.model_validate(
        {
            "schema_version": 2,
            "structure_profile": "synthetic_physical_v1",
            "document_lock": {
                "document_id": index.document_id,
                "pdf_sha256": index.pdf_sha256,
                "pages_content_sha256": index.pages_content_sha256,
                "index_content_sha256": index.index_content_sha256,
                "normalization_profile": index.search_normalization_profile,
            },
            "document_layout": {
                "body_start_page": 1,
                "table_of_contents_pages": [],
                "max_heading_continuation_lines": 0,
                "include_table_of_contents_in_topic_evidence": False,
            },
            "heading_patterns": {
                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],
                "article": [
                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"
                ],
                "general_section": [r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"],
                "continuation": [],
            },
            "ignored_patterns": {"page_headers": [], "page_footers": []},
            "zone_aliases": {},
            "topics": {"factual": ["factual"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 10,
        }
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_policy`

**Purpose:** Implements `policy` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
) -> BessZoningPolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessZoningPolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BessZoningPolicyConfig.model_validate(<br>        {<br>            "schema_version": 5,<br>            "policy_profile": "synthetic_physical_policy_v5",<br>            "planning_precheck_scope": "WRITTEN_ZONING_REGULATION_ONLY",<br>            "review_scope": "CONFIGURED_USE_CONTROL_ARTICLES_ONLY",<br>            "source_lock": {<br>                "document_id": index.document_id,<br>                "archive_sha256": index.archive_sha256,<br>                "pdf_sha256": index.pdf_sha256,<br>                "index_content_sha256": index.index_content_sha256,<br>                "structure_result_content_sha256": (<br>                    structure.structure_result_content_sha256<br>                ),<br>                "structure_profile": structure.structure_profile,<br>            },<br>            "required_zone_article_numbers": ["1", "2"],<br>            "chapters": [<br>                {<br>                    "resolved_zone_chapter_label": "U",<br>                    "review_completeness": (<br>                        "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"<br>                    ),<br>                    "reviewed_section_ids": reviewed,<br>                    "review_note": "The configured source articles were reviewed.",<br>                    "zoning_precheck_status": "UNKNOWN",<br>                    "zoning_precheck_confidence": "LOW",<br>                    "rationale": "No decision evidence is configured in this fixture.",<br>                    "missing_information": "Formal planning review remains required.",<br>                    "evidence": [],<br>                    "route_assessments": [],<br>                }<br>            ],<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_policy`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections.loc[<br>            structure.sections["section_type"].eq("ARTICLE"), "section_id"<br>        ].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |

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
def _policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
) -> BessZoningPolicyConfig:
    reviewed = tuple(
        structure.sections.loc[
            structure.sections["section_type"].eq("ARTICLE"), "section_id"
        ].tolist()
    )
    return BessZoningPolicyConfig.model_validate(
        {
            "schema_version": 5,
            "policy_profile": "synthetic_physical_policy_v5",
            "planning_precheck_scope": "WRITTEN_ZONING_REGULATION_ONLY",
            "review_scope": "CONFIGURED_USE_CONTROL_ARTICLES_ONLY",
            "source_lock": {
                "document_id": index.document_id,
                "archive_sha256": index.archive_sha256,
                "pdf_sha256": index.pdf_sha256,
                "index_content_sha256": index.index_content_sha256,
                "structure_result_content_sha256": (
                    structure.structure_result_content_sha256
                ),
                "structure_profile": structure.structure_profile,
            },
            "required_zone_article_numbers": ["1", "2"],
            "chapters": [
                {
                    "resolved_zone_chapter_label": "U",
                    "review_completeness": (
                        "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"
                    ),
                    "reviewed_section_ids": reviewed,
                    "review_note": "The configured source articles were reviewed.",
                    "zoning_precheck_status": "UNKNOWN",
                    "zoning_precheck_confidence": "LOW",
                    "rationale": "No decision evidence is configured in this fixture.",
                    "missing_information": "Formal planning review remains required.",
                    "evidence": [],
                    "route_assessments": [],
                }
            ],
        }
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_build_physical_chain`

**Purpose:** Implements `build physical chain` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _build_physical_chain(
    tmp_path: Path,
    *,
    include_article_two: bool = True,
) -> _PhysicalPlanningChain:
```

- Exact decorators: none.
- Declared return annotation: `_PhysicalPlanningChain`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `include_article_two` | keyword-only | `bool` | `True` |

**Return and exception contract**

- Exact observed return expressions:
  - `_PhysicalPlanningChain(<br>        planning_document=planning_document,<br>        zoning=zoning,<br>        index=index,<br>        structure_config=structure_config,<br>        structure=structure,<br>        parcels=parcels,<br>        policy=_policy(index, structure),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_planning_chain_builds_and_revalidates` via `_build_physical_chain`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_planning_chain_builds_and_revalidates` via `_build_physical_chain`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_source_byte_mutation_is_rejected` via `_build_physical_chain`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_source_byte_mutation_is_rejected` via `_build_physical_chain`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_config_hash_mutation_is_rejected` via `_build_physical_chain`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_config_hash_mutation_is_rejected` via `_build_physical_chain`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_missing_required_article_is_rejected` via `_build_physical_chain`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_missing_required_article_is_rejected` via `_build_physical_chain`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `Path` | `pathlib.Path` |
| `_write_gpu_archive` | `tests.integration.test_gpu_planning_end_to_end._write_gpu_archive` |
| `_gpu_document` | `tests.integration.test_gpu_planning_end_to_end._gpu_document` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `archive_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `tests.integration.test_gpu_planning_end_to_end._sha256` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `_structure_config` | `tests.integration.test_gpu_planning_end_to_end._structure_config` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `zoning.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_PhysicalPlanningChain` | `tests.integration.test_gpu_planning_end_to_end._PhysicalPlanningChain` |
| `_policy` | `tests.integration.test_gpu_planning_end_to_end._policy` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `parcels[column] = 0`<br>`parcels["planning_feature_document_id"] = index.document_id`<br>`parcels["planning_feature_archive_sha256"] = index.archive_sha256` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _build_physical_chain(
    tmp_path: Path,
    *,
    include_article_two: bool = True,
) -> _PhysicalPlanningChain:
    config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    archive_path = _write_gpu_archive(
        tmp_path,
        include_article_two=include_article_two,
    )
    document = _gpu_document(config)
    download = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-09-01T00:00:00+00:00",
        filename=archive_path.name,
        archive_format="zip",
        file_size=archive_path.stat().st_size,
        sha256=_sha256(archive_path),
        path=archive_path,
        cache_hit=False,
    )
    extraction = extract_gpu_document(download, tmp_path / "cache")
    planning_document = inspect_gpu_planning_document(extraction, config)
    source_parcels = gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "prior_fact": ["unchanged"]},
        geometry=[Polygon([(10, 10), (60, 10), (60, 60), (10, 60), (10, 10)])],
        crs="EPSG:2154",
    )
    zoning = intersect_parcels_with_gpu_zoning(source_parcels, planning_document)
    index = index_planning_regulation(planning_document)
    structure_config = _structure_config(index)
    structure = structure_planning_regulation(
        index,
        zoning.zones,
        zoning.intersections,
        structure_config,
    )
    parcels = zoning.parcels.copy(deep=True)
    for column in (
        "planning_surface_relation_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_point_relation_count",
    ):
        parcels[column] = 0
    parcels["planning_feature_document_id"] = index.document_id
    parcels["planning_feature_archive_sha256"] = index.archive_sha256
    return _PhysicalPlanningChain(
        planning_document=planning_document,
        zoning=zoning,
        index=index,
        structure_config=structure_config,
        structure=structure,
        parcels=parcels,
        policy=_policy(index, structure),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_interpret`

**Purpose:** Implements `interpret` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _interpret(chain: _PhysicalPlanningChain) -> BessZoningPrecheckResult:
```

- Exact decorators: none.
- Declared return annotation: `BessZoningPrecheckResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `chain` | positional-or-keyword | `_PhysicalPlanningChain` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `interpret_bess_zoning(<br>        chain.index,<br>        chain.structure,<br>        chain.structure_config,<br>        chain.zoning.zones,<br>        chain.zoning.intersections,<br>        chain.parcels,<br>        chain.planning_document,<br>        chain.policy,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_planning_chain_builds_and_revalidates` via `_interpret`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_planning_chain_builds_and_revalidates` via `_interpret`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_source_byte_mutation_is_rejected` via `_interpret`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_source_byte_mutation_is_rejected` via `_interpret`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_config_hash_mutation_is_rejected` via `_interpret`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_config_hash_mutation_is_rejected` via `_interpret`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_missing_required_article_is_rejected` via `_interpret`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_missing_required_article_is_rejected` via `_interpret`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |

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
def _interpret(chain: _PhysicalPlanningChain) -> BessZoningPrecheckResult:
    return interpret_bess_zoning(
        chain.index,
        chain.structure,
        chain.structure_config,
        chain.zoning.zones,
        chain.zoning.intersections,
        chain.parcels,
        chain.planning_document,
        chain.policy,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_validate`

**Purpose:** Implements `validate` within the file role: Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation.

**Exact signature**

```python
def _validate(
    chain: _PhysicalPlanningChain,
    result: BessZoningPrecheckResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `chain` | positional-or-keyword | `_PhysicalPlanningChain` | `required` |
| `result` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_planning_chain_builds_and_revalidates` via `_validate`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_planning_chain_builds_and_revalidates` via `_validate`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_source_byte_mutation_is_rejected` via `_validate`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_source_byte_mutation_is_rejected` via `_validate`
- direct call: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_config_hash_mutation_is_rejected` via `_validate`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_config_hash_mutation_is_rejected` via `_validate`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_bess_zoning_precheck` | `landscout.stages.interpret_bess_zoning.validate_bess_zoning_precheck` |

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
def _validate(
    chain: _PhysicalPlanningChain,
    result: BessZoningPrecheckResult,
) -> None:
    validate_bess_zoning_precheck(
        chain.index,
        chain.structure,
        chain.structure_config,
        chain.zoning.zones,
        chain.zoning.intersections,
        chain.parcels,
        chain.planning_document,
        chain.policy,
        result,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_gpu_planning_chain_builds_and_revalidates`

**Purpose:** Regression invariant: physical gpu planning chain builds and revalidates. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_physical_gpu_planning_chain_builds_and_revalidates(tmp_path: Path) -> None:
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
- Exact assertions:
  - `assert len(chain.zoning.zones) == 1`
  - `assert len(chain.zoning.intersections) == 1`
  - `assert len(result.parcels) == 1`
  - `assert result.parcels["prior_fact"].tolist() == ["unchanged"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_physical_chain` | `tests.integration.test_gpu_planning_end_to_end._build_physical_chain` |
| `_interpret` | `tests.integration.test_gpu_planning_end_to_end._interpret` |
| `_validate` | `tests.integration.test_gpu_planning_end_to_end._validate` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["prior_fact"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_physical_gpu_planning_chain_builds_and_revalidates(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)

    _validate(chain, result)

    assert len(chain.zoning.zones) == 1
    assert len(chain.zoning.intersections) == 1
    assert len(result.parcels) == 1
    assert result.parcels["prior_fact"].tolist() == ["unchanged"]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_gpu_source_byte_mutation_is_rejected`

**Purpose:** Regression invariant: physical gpu source byte mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_physical_gpu_source_byte_mutation_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(BessZoningPrecheckError, match="source\|GPU\|zoning")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_physical_chain` | `tests.integration.test_gpu_planning_end_to_end._build_physical_chain` |
| `_interpret` | `tests.integration.test_gpu_planning_end_to_end._interpret` |
| `dataset.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.integration.test_gpu_planning_end_to_end._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `dataset.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_physical_gpu_source_byte_mutation_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)
    dataset = chain.planning_document.zoning.reference.dataset_path
    with dataset.open("ab") as output:
        output.write(b"mutated-after-interpretation")

    with pytest.raises(BessZoningPrecheckError, match="source|GPU|zoning"):
        _validate(chain, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_gpu_config_hash_mutation_is_rejected`

**Purpose:** Regression invariant: physical gpu config hash mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_physical_gpu_config_hash_mutation_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(BessZoningPrecheckError, match="source\|GPU\|zoning")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_physical_chain` | `tests.integration.test_gpu_planning_end_to_end._build_physical_chain` |
| `_interpret` | `tests.integration.test_gpu_planning_end_to_end._interpret` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.integration.test_gpu_planning_end_to_end._validate` |

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
def test_physical_gpu_config_hash_mutation_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)
    forged_document = replace(
        chain.planning_document,
        source_config_sha256="0" * 64,
    )
    forged_chain = replace(chain, planning_document=forged_document)

    with pytest.raises(BessZoningPrecheckError, match="source|GPU|zoning"):
        _validate(forged_chain, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_gpu_missing_required_article_is_rejected`

**Purpose:** Regression invariant: physical gpu missing required article is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_physical_gpu_missing_required_article_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(<br>        BessZoningPrecheckError,<br>        match="exactly one configured article '2'",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_physical_chain` | `tests.integration.test_gpu_planning_end_to_end._build_physical_chain` |
| `pytest.raises` | `pytest.raises` |
| `_interpret` | `tests.integration.test_gpu_planning_end_to_end._interpret` |

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
def test_physical_gpu_missing_required_article_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path, include_article_two=False)

    with pytest.raises(
        BessZoningPrecheckError,
        match="exactly one configured article '2'",
    ):
        _interpret(chain)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **4**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_physical_gpu_planning_chain_builds_and_revalidates` | none | none | 4 | Proves physical gpu planning chain builds and revalidates using the exact source reproduced in section 7. |
| `test_physical_gpu_source_byte_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="source\|GPU\|zoning") | 0 | Proves physical gpu source byte mutation is rejected using the exact source reproduced in section 7. |
| `test_physical_gpu_config_hash_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="source\|GPU\|zoning") | 0 | Proves physical gpu config hash mutation is rejected using the exact source reproduced in section 7. |
| `test_physical_gpu_missing_required_article_is_rejected` | none | pytest.raises(<br>        BessZoningPrecheckError,<br>        match="exactly one configured article '2'",<br>    ) | 0 | Proves physical gpu missing required article is rejected using the exact source reproduced in section 7. |

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

from dataclasses import dataclass, replace
from hashlib import sha256
from pathlib import Path
from urllib.parse import quote
from zipfile import ZIP_DEFLATED, ZipFile

import geopandas as gpd  # type: ignore[import-untyped]
import pytest
from pypdf import PdfWriter
from pypdf.generic import (
    DecodedStreamObject,
    DictionaryObject,
    NameObject,
)
from shapely.geometry import Polygon

from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)
from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    intersect_parcels_with_gpu_zoning,
)
from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    index_planning_regulation,
)
from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureResult,
    structure_planning_regulation,
)

_ARCHIVE_NAME = "synthetic_gpu_document"
_DOCUMENT_ID = "synthetic-document"
_REGULATION_FILENAME = "reglement.pdf"


@dataclass(frozen=True)
class _PhysicalPlanningChain:
    planning_document: GpuPlanningDocument
    zoning: ParcelZoningResult
    index: PlanningRegulationIndex
    structure_config: PlanningRegulationStructureConfig
    structure: PlanningRegulationStructureResult
    parcels: gpd.GeoDataFrame
    policy: BessZoningPolicyConfig


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _write_text_pdf(path: Path, *, include_article_two: bool) -> None:
    lines = [
        "ZONE U",
        "ARTICLE U 1 - USES",
        "First factual source sentence.",
    ]
    if include_article_two:
        lines.extend(
            (
                "ARTICLE U 2 - OTHER",
                "Second factual source sentence.",
            )
        )
    writer = PdfWriter()
    page = writer.add_blank_page(width=612, height=792)
    font = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject("/Helvetica"),
        }
    )
    page[NameObject("/Resources")] = DictionaryObject(
        {
            NameObject("/Font"): DictionaryObject(
                {NameObject("/F1"): writer._add_object(font)}
            )
        }
    )
    operations = [b"BT", b"/F1 12 Tf", b"72 720 Td"]
    for position, line in enumerate(lines):
        if position:
            operations.append(b"0 -18 Td")
        operations.append(f"({line}) Tj".encode("ascii"))
    operations.append(b"ET")
    stream = DecodedStreamObject()
    stream.set_data(b"\n".join(operations))
    page[NameObject("/Contents")] = writer._add_object(stream)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as output:
        writer.write(output)


def _write_gpu_archive(
    tmp_path: Path,
    *,
    include_article_two: bool,
) -> Path:
    package = tmp_path / "package-source"
    package.mkdir()
    zoning_path = package / "planning.gpkg"
    zones = gpd.GeoDataFrame(
        {
            "LIB_IDZONE": ["ZONE-U"],
            "LIBELLE": ["U"],
            "LIBELONG": ["Zone U"],
            "TYPEZONE": ["U"],
            "NOMFIC": [_REGULATION_FILENAME],
            "URLFIC": ["https://example.invalid/reglement.pdf"],
            "IDURBA": [_ARCHIVE_NAME],
            "DATVALID": ["2026-01-01"],
        },
        geometry=[Polygon([(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)])],
        crs="EPSG:2154",
    )
    zones.to_file(
        zoning_path,
        layer="zone_urba",
        driver="GPKG",
        engine="pyogrio",
    )
    pdf_path = package / _REGULATION_FILENAME
    _write_text_pdf(pdf_path, include_article_two=include_article_two)
    archive_path = tmp_path / f"{_ARCHIVE_NAME}.zip"
    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        archive.write(zoning_path, "package/planning.gpkg")
        archive.write(pdf_path, f"package/{_REGULATION_FILENAME}")
    return archive_path


def _gpu_document(config: GpuSourceConfig) -> GpuDocumentMetadata:
    written_url = (
        f"{str(config.api.base_url).rstrip('/')}/document/"
        f"{quote(_DOCUMENT_ID, safe='')}/files/"
        f"{quote(_REGULATION_FILENAME, safe='')}"
    )
    return GpuDocumentMetadata(
        provider=config.provider,
        portal=config.portal,
        commune_code=config.pilot.commune_code,
        partition=build_gpu_partition(config),
        document_id=_DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Synthetic planning document",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="1",
        archive_name=_ARCHIVE_NAME,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url=build_gpu_partition_download_url(config),
        written_files=(
            GpuWrittenFile(
                filename=_REGULATION_FILENAME,
                title="Synthetic regulation",
                document_path=None,
                source_url=written_url,
            ),
        ),
    )


def _structure_config(
    index: PlanningRegulationIndex,
) -> PlanningRegulationStructureConfig:
    return PlanningRegulationStructureConfig.model_validate(
        {
            "schema_version": 2,
            "structure_profile": "synthetic_physical_v1",
            "document_lock": {
                "document_id": index.document_id,
                "pdf_sha256": index.pdf_sha256,
                "pages_content_sha256": index.pages_content_sha256,
                "index_content_sha256": index.index_content_sha256,
                "normalization_profile": index.search_normalization_profile,
            },
            "document_layout": {
                "body_start_page": 1,
                "table_of_contents_pages": [],
                "max_heading_continuation_lines": 0,
                "include_table_of_contents_in_topic_evidence": False,
            },
            "heading_patterns": {
                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],
                "article": [
                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"
                ],
                "general_section": [r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"],
                "continuation": [],
            },
            "ignored_patterns": {"page_headers": [], "page_footers": []},
            "zone_aliases": {},
            "topics": {"factual": ["factual"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 10,
        }
    )


def _policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
) -> BessZoningPolicyConfig:
    reviewed = tuple(
        structure.sections.loc[
            structure.sections["section_type"].eq("ARTICLE"), "section_id"
        ].tolist()
    )
    return BessZoningPolicyConfig.model_validate(
        {
            "schema_version": 5,
            "policy_profile": "synthetic_physical_policy_v5",
            "planning_precheck_scope": "WRITTEN_ZONING_REGULATION_ONLY",
            "review_scope": "CONFIGURED_USE_CONTROL_ARTICLES_ONLY",
            "source_lock": {
                "document_id": index.document_id,
                "archive_sha256": index.archive_sha256,
                "pdf_sha256": index.pdf_sha256,
                "index_content_sha256": index.index_content_sha256,
                "structure_result_content_sha256": (
                    structure.structure_result_content_sha256
                ),
                "structure_profile": structure.structure_profile,
            },
            "required_zone_article_numbers": ["1", "2"],
            "chapters": [
                {
                    "resolved_zone_chapter_label": "U",
                    "review_completeness": (
                        "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"
                    ),
                    "reviewed_section_ids": reviewed,
                    "review_note": "The configured source articles were reviewed.",
                    "zoning_precheck_status": "UNKNOWN",
                    "zoning_precheck_confidence": "LOW",
                    "rationale": "No decision evidence is configured in this fixture.",
                    "missing_information": "Formal planning review remains required.",
                    "evidence": [],
                    "route_assessments": [],
                }
            ],
        }
    )


def _build_physical_chain(
    tmp_path: Path,
    *,
    include_article_two: bool = True,
) -> _PhysicalPlanningChain:
    config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    archive_path = _write_gpu_archive(
        tmp_path,
        include_article_two=include_article_two,
    )
    document = _gpu_document(config)
    download = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-09-01T00:00:00+00:00",
        filename=archive_path.name,
        archive_format="zip",
        file_size=archive_path.stat().st_size,
        sha256=_sha256(archive_path),
        path=archive_path,
        cache_hit=False,
    )
    extraction = extract_gpu_document(download, tmp_path / "cache")
    planning_document = inspect_gpu_planning_document(extraction, config)
    source_parcels = gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "prior_fact": ["unchanged"]},
        geometry=[Polygon([(10, 10), (60, 10), (60, 60), (10, 60), (10, 10)])],
        crs="EPSG:2154",
    )
    zoning = intersect_parcels_with_gpu_zoning(source_parcels, planning_document)
    index = index_planning_regulation(planning_document)
    structure_config = _structure_config(index)
    structure = structure_planning_regulation(
        index,
        zoning.zones,
        zoning.intersections,
        structure_config,
    )
    parcels = zoning.parcels.copy(deep=True)
    for column in (
        "planning_surface_relation_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_point_relation_count",
    ):
        parcels[column] = 0
    parcels["planning_feature_document_id"] = index.document_id
    parcels["planning_feature_archive_sha256"] = index.archive_sha256
    return _PhysicalPlanningChain(
        planning_document=planning_document,
        zoning=zoning,
        index=index,
        structure_config=structure_config,
        structure=structure,
        parcels=parcels,
        policy=_policy(index, structure),
    )


def _interpret(chain: _PhysicalPlanningChain) -> BessZoningPrecheckResult:
    return interpret_bess_zoning(
        chain.index,
        chain.structure,
        chain.structure_config,
        chain.zoning.zones,
        chain.zoning.intersections,
        chain.parcels,
        chain.planning_document,
        chain.policy,
    )


def _validate(
    chain: _PhysicalPlanningChain,
    result: BessZoningPrecheckResult,
) -> None:
    validate_bess_zoning_precheck(
        chain.index,
        chain.structure,
        chain.structure_config,
        chain.zoning.zones,
        chain.zoning.intersections,
        chain.parcels,
        chain.planning_document,
        chain.policy,
        result,
    )


def test_physical_gpu_planning_chain_builds_and_revalidates(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)

    _validate(chain, result)

    assert len(chain.zoning.zones) == 1
    assert len(chain.zoning.intersections) == 1
    assert len(result.parcels) == 1
    assert result.parcels["prior_fact"].tolist() == ["unchanged"]


def test_physical_gpu_source_byte_mutation_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)
    dataset = chain.planning_document.zoning.reference.dataset_path
    with dataset.open("ab") as output:
        output.write(b"mutated-after-interpretation")

    with pytest.raises(BessZoningPrecheckError, match="source|GPU|zoning"):
        _validate(chain, result)


def test_physical_gpu_config_hash_mutation_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)
    forged_document = replace(
        chain.planning_document,
        source_config_sha256="0" * 64,
    )
    forged_chain = replace(chain, planning_document=forged_document)

    with pytest.raises(BessZoningPrecheckError, match="source|GPU|zoning"):
        _validate(forged_chain, result)


def test_physical_gpu_missing_required_article_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path, include_article_two=False)

    with pytest.raises(
        BessZoningPrecheckError,
        match="exactly one configured article '2'",
    ):
        _interpret(chain)
```
