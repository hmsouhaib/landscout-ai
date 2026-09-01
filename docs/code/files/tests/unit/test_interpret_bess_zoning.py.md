# `tests/unit/test_interpret_bess_zoning.py`

## File identity

- Repository path: `tests/unit/test_interpret_bess_zoning.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.
- Source SHA256: `e5ad284bb61a67a348377ad4d68092c4425c16eb13519c6440a0c52de70b70d3`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for interpret bess zoning; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import importlib`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import Polygon`
- `import yaml`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)`
- `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`
- `from landscout.stages.structure_planning_regulation import (
    _result_with_hashes as _structure_with_hashes,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `interpret_module`

- Category: module-level alias/value.
- Exact declaration:

```python
interpret_module = importlib.import_module("landscout.stages.interpret_bess_zoning")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_index`

**Purpose:** Implements `index` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _index() -> PlanningRegulationIndex:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationIndex`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `replace(index, index_content_sha256=_index_content_sha256(index))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::inputs` via `_index`
- value/type reference: `tests.unit.test_interpret_bess_zoning::inputs` via `_index`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text` | `landscout.stages.index_planning_regulation._normalize_search_text` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_page_content_sha256` | `landscout.stages.index_planning_regulation._page_content_sha256` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `PlanningRegulationIndex` | `landscout.stages.index_planning_regulation.PlanningRegulationIndex` |
| `_pages_content_sha256` | `landscout.stages.index_planning_regulation._pages_content_sha256` |
| `replace` | `dataclasses.replace` |
| `_index_content_sha256` | `landscout.stages.index_planning_regulation._index_content_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_page_content_sha256`<br>`_pages_content_sha256`<br>`_index_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `row["page_content_sha256"] = _page_content_sha256(row)`<br>`rows.append(row)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _index() -> PlanningRegulationIndex:
    raw_pages = (
        "ARTICLE 1 - GENERAL\nGeneral factual text.",
        (
            "ZONE U\nARTICLE U 1 - USES\nTechnical equipment is permitted only when "
            "formal review is required.\nTechnical equipment is permitted only when "
            "formal review is required.\nARTICLE U 2 - OTHER\nOther factual text."
        ),
        (
            "ZONE N\nARTICLE N 1 - USES\nBattery facilities are restricted.\n"
            "Technical equipment is permitted only when formal review is required.\n"
            "ARTICLE N 2 - OTHER\nOther factual text."
        ),
    )
    rows: list[dict[str, object]] = []
    for number, raw_text in enumerate(raw_pages, start=1):
        row: dict[str, object] = {
            "page_number": number,
            "extraction_status": "TEXT",
            "raw_text": raw_text,
            "normalized_search_text": _normalize_search_text(raw_text),
            "character_count": len(raw_text),
            "extraction_error": None,
            "page_content_sha256": "",
        }
        row["page_content_sha256"] = _page_content_sha256(row)
        rows.append(row)
    pages = pd.DataFrame(rows)
    index = PlanningRegulationIndex(
        document_id="doc-1",
        archive_sha256="a" * 64,
        regulation_filename="commune_reglement.pdf",
        source_selection_method="ZONING_NOMFIC",
        source_selection_sha256="b" * 64,
        pdf_relative_path="package/commune_reglement.pdf",
        pdf_size_bytes=100,
        pdf_sha256="c" * 64,
        extraction_library="pypdf",
        extraction_library_version="test-version",
        search_normalization_profile=SEARCH_NORMALIZATION_PROFILE,
        page_hash_schema_version=PAGE_HASH_SCHEMA_VERSION,
        index_hash_schema_version=INDEX_HASH_SCHEMA_VERSION,
        total_page_count=len(pages),
        pages_content_sha256=_pages_content_sha256(pages),
        index_content_sha256="d" * 64,
        pages=pages,
    )
    return replace(index, index_content_sha256=_index_content_sha256(index))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_zones`

**Purpose:** Implements `zones` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(<br>        {<br>            "planning_zone_id": ["ZONE-U", "ZONE-UA", "ZONE-N"],<br>            "source_zone_id": ["SRC-U", "SRC-UA", "SRC-N"],<br>            "zone_label_raw": ["U", "Ua", "N"],<br>            "source_document_id": index.document_id,<br>            "source_archive_sha256": index.archive_sha256,<br>            "source_layer": "ZONE",<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::inputs` via `_zones`
- value/type reference: `tests.unit.test_interpret_bess_zoning::inputs` via `_zones`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |

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
def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "planning_zone_id": ["ZONE-U", "ZONE-UA", "ZONE-N"],
            "source_zone_id": ["SRC-U", "SRC-UA", "SRC-N"],
            "zone_label_raw": ["U", "Ua", "N"],
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
            "source_layer": "ZONE",
        }
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_relations`

**Purpose:** Implements `relations` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(<br>        [<br>            {<br>                "parcel_id": parcel_id,<br>                "planning_zone_id": planning_zone_id,<br>                "source_zone_id": source_zone_id,<br>                "zone_label_raw": label,<br>                "relation_type": relation_type,<br>                "intersection_area_m2": area,<br>                "parcel_share_pct": share,<br>                "zone_share_pct": area / 10.0,<br>                "source_document_id": index.document_id,<br>                "source_archive_sha256": index.archive_sha256,<br>                "source_layer": "ZONE",<br>                "parcel_metric_area_m2": 100.0,<br>                "zone_area_m2": 1000.0,<br>            }<br>            for (<br>                parcel_id,<br>                planning_zone_id,<br>                source_zone_id,<br>                label,<br>                relation_type,<br>                area,<br>                share,<br>            ) in rows<br>        ]<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::inputs` via `_relations`
- value/type reference: `tests.unit.test_interpret_bess_zoning::inputs` via `_relations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |

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
def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
    rows = (
        ("P-1", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 100.0, 100.0),
        ("P-2", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-2", "ZONE-UA", "SRC-UA", "Ua", "AREA_OVERLAP", 40.0, 40.0),
        ("P-3", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-3", "ZONE-N", "SRC-N", "N", "AREA_OVERLAP", 40.0, 40.0),
        ("P-4", "ZONE-N", "SRC-N", "N", "TOUCH_ONLY", 0.0, 0.0),
    )
    return pd.DataFrame(
        [
            {
                "parcel_id": parcel_id,
                "planning_zone_id": planning_zone_id,
                "source_zone_id": source_zone_id,
                "zone_label_raw": label,
                "relation_type": relation_type,
                "intersection_area_m2": area,
                "parcel_share_pct": share,
                "zone_share_pct": area / 10.0,
                "source_document_id": index.document_id,
                "source_archive_sha256": index.archive_sha256,
                "source_layer": "ZONE",
                "parcel_metric_area_m2": 100.0,
                "zone_area_m2": 1000.0,
            }
            for (
                parcel_id,
                planning_zone_id,
                source_zone_id,
                label,
                relation_type,
                area,
                share,
            ) in rows
        ]
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_structure_config`

**Purpose:** Implements `structure config` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

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
  - `PlanningRegulationStructureConfig.model_validate(<br>        {<br>            "schema_version": 2,<br>            "structure_profile": "synthetic_v1",<br>            "document_lock": {<br>                "document_id": index.document_id,<br>                "pdf_sha256": index.pdf_sha256,<br>                "pages_content_sha256": index.pages_content_sha256,<br>                "index_content_sha256": index.index_content_sha256,<br>                "normalization_profile": index.search_normalization_profile,<br>            },<br>            "document_layout": {<br>                "body_start_page": 1,<br>                "table_of_contents_pages": [],<br>                "max_heading_continuation_lines": 0,<br>                "include_table_of_contents_in_topic_evidence": False,<br>            },<br>            "heading_patterns": {<br>                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],<br>                "article": [<br>                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"<br>                ],<br>                "general_section": [r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"],<br>                "continuation": [],<br>            },<br>            "ignored_patterns": {"page_headers": [], "page_footers": []},<br>            "zone_aliases": {"Ua": "U"},<br>            "topics": {"technical": ["technical equipment"]},<br>            "topic_match_policy": {<br>                "boundary_mode": "token",<br>                "overlap_resolution": "longest_match",<br>            },<br>            "topic_context_characters": 20,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::inputs` via `_structure_config`
- value/type reference: `tests.unit.test_interpret_bess_zoning::inputs` via `_structure_config`

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
            "structure_profile": "synthetic_v1",
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
            "zone_aliases": {"Ua": "U"},
            "topics": {"technical": ["technical equipment"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 20,
        }
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::inputs` via `_parcels`
- value/type reference: `tests.unit.test_interpret_bess_zoning::inputs` via `_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pd.Index` | `pandas.Index` |

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
def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ["P-1", "P-2", "P-3", "P-4"],
            "dominant_planning_zone_id": ["ZONE-U", "ZONE-U", "ZONE-U", None],
            "planning_surface_relation_count": [0, 1, 2, 0],
            "prescription_surface_relation_count": [0, 1, 1, 0],
            "information_surface_relation_count": [0, 0, 1, 0],
            "planning_line_relation_count": [0, 0, 0, 0],
            "planning_point_relation_count": [0, 0, 0, 0],
            "planning_document_id": index.document_id,
            "planning_archive_sha256": index.archive_sha256,
            "planning_feature_document_id": index.document_id,
            "planning_feature_archive_sha256": index.archive_sha256,
            "prior_fact": ["one", "two", "three", "four"],
        },
        geometry=[
            Polygon([(x, 0), (x + 10, 0), (x + 10, 10), (x, 10), (x, 0)])
            for x in (0, 20, 40, 60)
        ],
        crs="EPSG:2154",
        index=pd.Index([10, 20, 30, 40], name="source_row"),
    )
    return frame
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_policy`

**Purpose:** Implements `policy` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessZoningPolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `None` | `required` |
| `structure` | positional-or-keyword | `None` | `required` |
| `config` | positional-or-keyword | `None` | `required` |
| `zones` | positional-or-keyword | `None` | `required` |
| `relations` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BessZoningPolicyConfig.model_validate(<br>        {<br>            "schema_version": 5,<br>            "policy_profile": "synthetic_policy_v5",<br>            "planning_precheck_scope": "WRITTEN_ZONING_REGULATION_ONLY",<br>            "review_scope": "CONFIGURED_USE_CONTROL_ARTICLES_ONLY",<br>            "source_lock": {<br>                "document_id": index.document_id,<br>                "archive_sha256": index.archive_sha256,<br>                "pdf_sha256": index.pdf_sha256,<br>                "index_content_sha256": index.index_content_sha256,<br>                "structure_result_content_sha256": (<br>                    structure.structure_result_content_sha256<br>                ),<br>                "structure_profile": structure.structure_profile,<br>            },<br>            "required_zone_article_numbers": ["1", "2"],<br>            "chapters": [<br>                {<br>                    "resolved_zone_chapter_label": "U",<br>                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",<br>                    "reviewed_section_ids": u_articles["section_id"].tolist(),<br>                    "review_note": "The required use-control article was reviewed.",<br>                    "zoning_precheck_status": "CONDITIONAL_REVIEW",<br>                    "zoning_precheck_confidence": "MEDIUM",<br>                    "rationale": "The source states a review condition.",<br>                    "missing_information": "Formal classification and review.",<br>                    "evidence": [<br>                        evidence(<br>                            "E-U-POSITIVE",<br>                            u_article["section_id"],<br>                            2,<br>                            "USE_PERMISSION",<br>                            "SUPPORTS_POTENTIAL_COMPATIBILITY",<br>                            u_positive,<br>                            "RULE-U-CONDITIONAL",<br>                            "Technical equipment is permitted only when formal review is required.",<br>                            "This is positive route evidence only.",<br>                        ),<br>                        evidence(<br>                            "E-U-CONDITION",<br>                            u_article["section_id"],<br>                            2,<br>                            "TECHNICAL_EQUIPMENT_RULE",<br>                            "CONDITION",<br>                            u_condition,<br>                            "RULE-U-CONDITIONAL",<br>                            "Technical equipment is permitted only when formal review is required.",<br>                            "This is a condition only.",<br>                        ),<br>                    ],<br>                    "route_assessments": [<br>                        {<br>                            "route_id": "ROUTE-U-CONDITIONAL",<br>                            "route_kind": "CONDITIONAL_ROUTE",<br>                            "positive_evidence_ids": ["E-U-POSITIVE"],<br>                            "condition_evidence_ids": ["E-U-CONDITION"],<br>                            "difficulty_evidence_ids": [],<br>                            "applicability_note": "The positive route and its condition are assessed together.",<br>                        }<br>                    ],<br>                },<br>                {<br>                    "resolved_zone_chapter_label": "N",<br>                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",<br>                    "reviewed_section_ids": n_articles["section_id"].tolist(),<br>                    "review_note": "The required use-control article was reviewed.",<br>                    "zoning_precheck_status": "LIKELY_DIFFICULT",<br>                    "zoning_precheck_confidence": "HIGH",<br>                    "rationale": "The source states a relevant restriction.",<br>                    "missing_information": "Formal classification and review.",<br>                    "evidence": [<br>                        evidence(<br>                            "E-N-1",<br>                            n_article["section_id"],<br>                            3,<br>                            "USE_RESTRICTION",<br>                            "SUPPORTS_DIFFICULTY",<br>                            n_excerpt,<br>                            "RULE-N-RESTRICTION",<br>                            n_excerpt,<br>                            "This is difficulty evidence only.",<br>                        )<br>                    ],<br>                    "route_assessments": [<br>                        {<br>                            "route_id": "ROUTE-N-DIFFICULT",<br>                            "route_kind": "DIFFICULTY_ONLY",<br>                            "positive_evidence_ids": [],<br>                            "condition_evidence_ids": [],<br>                            "difficulty_evidence_ids": ["E-N-1"],<br>                            "applicability_note": "The restriction is assessed without a positive route.",<br>                        }<br>                    ],<br>                },<br>            ],<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::inputs` via `_policy`
- value/type reference: `tests.unit.test_interpret_bess_zoning::inputs` via `_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `u_articles["article_number_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `n_articles["article_number_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_regulation_section_page_fragments(<br>        index, zones, relations, config, structure<br>    ).set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_regulation_section_page_fragments` | `landscout.stages.structure_planning_regulation.planning_regulation_section_page_fragments` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `u_articles["section_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `evidence` | `unresolved local/third-party receiver; no ownership inferred` |
| `n_articles["section_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
    sections = structure.sections
    u_articles = sections.loc[
        sections["section_type"].eq("ARTICLE") & sections["zone_chapter_label"].eq("U")
    ]
    n_articles = sections.loc[
        sections["section_type"].eq("ARTICLE") & sections["zone_chapter_label"].eq("N")
    ]
    u_article = u_articles.loc[u_articles["article_number_raw"].eq("1")].iloc[0]
    n_article = n_articles.loc[n_articles["article_number_raw"].eq("1")].iloc[0]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    u_positive = "Technical equipment is permitted"
    u_condition = "only when formal review is required"
    n_excerpt = "Battery facilities are restricted."

    def evidence(
        evidence_id: str,
        section_id: str,
        page_number: int,
        kind: str,
        direction: str,
        excerpt: str,
        source_rule_id: str,
        source_rule: str,
        note: str,
    ) -> dict[str, object]:
        fragment = fragments.loc[(section_id, page_number)]
        raw = fragment["raw_text"]
        rule_start = raw.index(source_rule)
        start = raw.index(excerpt, rule_start, rule_start + len(source_rule))
        return {
            "evidence_id": evidence_id,
            "section_id": section_id,
            "page_number": page_number,
            "evidence_kind": kind,
            "evidence_direction": direction,
            "exact_raw_excerpt": excerpt,
            "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
            "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],
            "excerpt_start": start,
            "excerpt_end": start + len(excerpt),
            "source_rule_id": source_rule_id,
            "source_rule_excerpt": source_rule,
            "source_rule_sha256": sha256(source_rule.encode()).hexdigest(),
            "source_rule_start": rule_start,
            "source_rule_end": rule_start + len(source_rule),
            "interpretation_note": note,
        }

    return BessZoningPolicyConfig.model_validate(
        {
            "schema_version": 5,
            "policy_profile": "synthetic_policy_v5",
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
                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",
                    "reviewed_section_ids": u_articles["section_id"].tolist(),
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "CONDITIONAL_REVIEW",
                    "zoning_precheck_confidence": "MEDIUM",
                    "rationale": "The source states a review condition.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-U-POSITIVE",
                            u_article["section_id"],
                            2,
                            "USE_PERMISSION",
                            "SUPPORTS_POTENTIAL_COMPATIBILITY",
                            u_positive,
                            "RULE-U-CONDITIONAL",
                            "Technical equipment is permitted only when formal review is required.",
                            "This is positive route evidence only.",
                        ),
                        evidence(
                            "E-U-CONDITION",
                            u_article["section_id"],
                            2,
                            "TECHNICAL_EQUIPMENT_RULE",
                            "CONDITION",
                            u_condition,
                            "RULE-U-CONDITIONAL",
                            "Technical equipment is permitted only when formal review is required.",
                            "This is a condition only.",
                        ),
                    ],
                    "route_assessments": [
                        {
                            "route_id": "ROUTE-U-CONDITIONAL",
                            "route_kind": "CONDITIONAL_ROUTE",
                            "positive_evidence_ids": ["E-U-POSITIVE"],
                            "condition_evidence_ids": ["E-U-CONDITION"],
                            "difficulty_evidence_ids": [],
                            "applicability_note": "The positive route and its condition are assessed together.",
                        }
                    ],
                },
                {
                    "resolved_zone_chapter_label": "N",
                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",
                    "reviewed_section_ids": n_articles["section_id"].tolist(),
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "LIKELY_DIFFICULT",
                    "zoning_precheck_confidence": "HIGH",
                    "rationale": "The source states a relevant restriction.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-N-1",
                            n_article["section_id"],
                            3,
                            "USE_RESTRICTION",
                            "SUPPORTS_DIFFICULTY",
                            n_excerpt,
                            "RULE-N-RESTRICTION",
                            n_excerpt,
                            "This is difficulty evidence only.",
                        )
                    ],
                    "route_assessments": [
                        {
                            "route_id": "ROUTE-N-DIFFICULT",
                            "route_kind": "DIFFICULTY_ONLY",
                            "positive_evidence_ids": [],
                            "condition_evidence_ids": [],
                            "difficulty_evidence_ids": ["E-N-1"],
                            "applicability_note": "The restriction is assessed without a positive route.",
                        }
                    ],
                },
            ],
        }
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_policy.evidence`

**Purpose:** Implements `evidence` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def evidence(
        evidence_id: str,
        section_id: str,
        page_number: int,
        kind: str,
        direction: str,
        excerpt: str,
        source_rule_id: str,
        source_rule: str,
        note: str,
    ) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `evidence_id` | positional-or-keyword | `str` | `required` |
| `section_id` | positional-or-keyword | `str` | `required` |
| `page_number` | positional-or-keyword | `int` | `required` |
| `kind` | positional-or-keyword | `str` | `required` |
| `direction` | positional-or-keyword | `str` | `required` |
| `excerpt` | positional-or-keyword | `str` | `required` |
| `source_rule_id` | positional-or-keyword | `str` | `required` |
| `source_rule` | positional-or-keyword | `str` | `required` |
| `note` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>            "evidence_id": evidence_id,<br>            "section_id": section_id,<br>            "page_number": page_number,<br>            "evidence_kind": kind,<br>            "evidence_direction": direction,<br>            "exact_raw_excerpt": excerpt,<br>            "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),<br>            "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],<br>            "excerpt_start": start,<br>            "excerpt_end": start + len(excerpt),<br>            "source_rule_id": source_rule_id,<br>            "source_rule_excerpt": source_rule,<br>            "source_rule_sha256": sha256(source_rule.encode()).hexdigest(),<br>            "source_rule_start": rule_start,<br>            "source_rule_end": rule_start + len(source_rule),<br>            "interpretation_note": note,<br>        }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `raw.index` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(excerpt.encode()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `excerpt.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(source_rule.encode()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_rule.encode` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(excerpt.encode()).hexdigest`<br>`sha256`<br>`sha256(source_rule.encode()).hexdigest` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def evidence(
        evidence_id: str,
        section_id: str,
        page_number: int,
        kind: str,
        direction: str,
        excerpt: str,
        source_rule_id: str,
        source_rule: str,
        note: str,
    ) -> dict[str, object]:
        fragment = fragments.loc[(section_id, page_number)]
        raw = fragment["raw_text"]
        rule_start = raw.index(source_rule)
        start = raw.index(excerpt, rule_start, rule_start + len(source_rule))
        return {
            "evidence_id": evidence_id,
            "section_id": section_id,
            "page_number": page_number,
            "evidence_kind": kind,
            "evidence_direction": direction,
            "exact_raw_excerpt": excerpt,
            "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
            "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],
            "excerpt_start": start,
            "excerpt_end": start + len(excerpt),
            "source_rule_id": source_rule_id,
            "source_rule_excerpt": source_rule,
            "source_rule_sha256": sha256(source_rule.encode()).hexdigest(),
            "source_rule_start": rule_start,
            "source_rule_end": rule_start + len(source_rule),
            "interpretation_note": note,
        }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `inputs`

**Purpose:** Implements `inputs` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def inputs(monkeypatch):
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        index,<br>        structure,<br>        config,<br>        zones,<br>        relations,<br>        parcels,<br>        planning_document,<br>        policy,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_interpret_bess_zoning::valid_result` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_validate` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_regulation_zone_chapter_labels_and_ids_must_be_unique` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_complete_validator_rejects_later_duplicate_chapter` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_and_evidence_id_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_excerpt_cannot_be_reused_with_contradictory_directions` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_occurrence_in_different_compatible_routes_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_forbidden_or_invalid_final_status_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_confidence_and_unknown_field_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_policy_schema_versions_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_every_evidence_kind_has_an_explicit_direction_matrix` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_exact_evidence_is_preserved` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_rule_text_at_distinct_offsets_has_distinct_identity` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_excerpt_hash_and_length_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_declared_status_must_equal_derived_route_status` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_condition_alone_cannot_create_conditional_review` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unrelated_positive_and_condition_do_not_create_conditional_review` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_context_only_unknown_succeeds` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_positive_condition_and_conflict_status_routes` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_references_must_be_same_chapter_and_role_compatible` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_ids_are_globally_unique` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_difficulty_evidence_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_positive_and_condition_evidence_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_only_evidence_must_be_unlinked` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_evidence_may_link_to_multiple_compatible_routes` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_difficulty_and_positive_only_status_routes` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_requires_unknown_low` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_persists_exact_missing_required_sections` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unknown_is_accepted_when_evidence_is_insufficient` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_every_configured_article_must_exist_once_in_every_chapter` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_configured_article_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_configured_article_with_wrong_chapter_parent_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_general_section_review_is_explicit_and_valid` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_exact_section_page_occurrence_is_auditable` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unmapped_dominant_zone_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_evidence_is_separate_from_decision_outputs` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_inputs_are_not_mutated` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_zoning_relation_and_zone_mapping_changes_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_structure_config_and_hierarchy_changes_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_public_source_complete_validator_is_invoked` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_physical_zoning_fails_before_policy_interpretation` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_physical_zoning_fails_before_policy_interpretation.counted_policy` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_build_result_performs_one_factual_structure_rebuild` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_area_denominators_are_required` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_percentages_must_match_denominators` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_result_mutation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_catalog_mutation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_route_table_mutation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_route_link_mutation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_reverse_link_mutation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_route_link_hash_mutation_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_result_hash_schemas_are_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_identity_change_is_rejected` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_readback_result_validates` via `inputs`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_yaml_roundtrip_is_strict` via `inputs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_index` | `tests.unit.test_interpret_bess_zoning._index` |
| `_zones` | `tests.unit.test_interpret_bess_zoning._zones` |
| `_relations` | `tests.unit.test_interpret_bess_zoning._relations` |
| `_structure_config` | `tests.unit.test_interpret_bess_zoning._structure_config` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_parcels` | `tests.unit.test_interpret_bess_zoning._parcels` |
| `_policy` | `tests.unit.test_interpret_bess_zoning._policy` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def inputs(monkeypatch):
    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        lambda *args: None,
    )
    index = _index()
    zones = _zones(index)
    relations = _relations(index)
    config = _structure_config(index)
    structure = structure_planning_regulation(index, zones, relations, config)
    parcels = _parcels(index)
    policy = _policy(index, structure, config, zones, relations)
    planning_document = object()
    return (
        index,
        structure,
        config,
        zones,
        relations,
        parcels,
        planning_document,
        policy,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `valid_result`

**Purpose:** Implements `valid result` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def valid_result(inputs):
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `interpret_bess_zoning(*inputs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_complete_validator_rejects_later_duplicate_chapter` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_exact_evidence_is_preserved` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_exact_section_page_occurrence_is_auditable` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_exact_and_alias_mappings_are_inherited_without_prefix_logic` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_link_table_exactly_reproduces_routes_and_reverse_links` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_parcel_aggregation_preserves_conflicts_and_touch_only` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_zoning_relation_and_zone_mapping_changes_are_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_result_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_catalog_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_route_table_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_route_link_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_reverse_link_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_route_link_hash_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_result_hash_schemas_are_rejected` via `valid_result`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_readback_result_validates` via `valid_result`

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
def valid_result(inputs):
    return interpret_bess_zoning(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_payload`

**Purpose:** Implements `payload` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `policy.model_dump(mode="python")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::_policy_with_context_only_evidence` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_policy_with_context_only_evidence` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_and_evidence_id_are_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_and_evidence_id_are_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_one_excerpt_cannot_be_reused_with_contradictory_directions` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_excerpt_cannot_be_reused_with_contradictory_directions` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_duplicate_occurrence_in_different_compatible_routes_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_occurrence_in_different_compatible_routes_is_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_forbidden_or_invalid_final_status_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_forbidden_or_invalid_final_status_is_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_invalid_confidence_and_unknown_field_are_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_confidence_and_unknown_field_are_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_old_policy_schema_versions_are_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_policy_schema_versions_are_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_every_evidence_kind_has_an_explicit_direction_matrix` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_every_evidence_kind_has_an_explicit_direction_matrix` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_same_rule_text_at_distinct_offsets_has_distinct_identity` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_rule_text_at_distinct_offsets_has_distinct_identity` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_excerpt_hash_and_length_are_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_excerpt_hash_and_length_are_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_declared_status_must_equal_derived_route_status` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_declared_status_must_equal_derived_route_status` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_condition_alone_cannot_create_conditional_review` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_condition_alone_cannot_create_conditional_review` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unrelated_positive_and_condition_do_not_create_conditional_review` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unrelated_positive_and_condition_do_not_create_conditional_review` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unlinked_context_only_unknown_succeeds` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_context_only_unknown_succeeds` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_positive_condition_and_conflict_status_routes` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_positive_condition_and_conflict_status_routes` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_route_references_must_be_same_chapter_and_role_compatible` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_references_must_be_same_chapter_and_role_compatible` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_route_ids_are_globally_unique` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_ids_are_globally_unique` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unlinked_difficulty_evidence_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_difficulty_evidence_is_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unlinked_positive_and_condition_evidence_are_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_positive_and_condition_evidence_are_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_context_only_evidence_must_be_unlinked` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_only_evidence_must_be_unlinked` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_one_evidence_may_link_to_multiple_compatible_routes` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_evidence_may_link_to_multiple_compatible_routes` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_difficulty_and_positive_only_status_routes` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_difficulty_and_positive_only_status_routes` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_requires_unknown_low` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_requires_unknown_low` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_persists_exact_missing_required_sections` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_persists_exact_missing_required_sections` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unknown_is_accepted_when_evidence_is_insufficient` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unknown_is_accepted_when_evidence_is_insufficient` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_general_section_review_is_explicit_and_valid` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_general_section_review_is_explicit_and_valid` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `_payload`
- direct call: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `policy.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
    return policy.model_dump(mode="python")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_policy_with_context_only_evidence`

**Purpose:** Implements `policy with context only evidence` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _policy_with_context_only_evidence(
    policy: BessZoningPolicyConfig,
) -> BessZoningPolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessZoningPolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BessZoningPolicyConfig.model_validate(payload)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::test_context_only_evidence_must_be_unlinked` via `_policy_with_context_only_evidence`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_only_evidence_must_be_unlinked` via `_policy_with_context_only_evidence`
- direct call: `tests.unit.test_interpret_bess_zoning::test_context_evidence_is_separate_from_decision_outputs` via `_policy_with_context_only_evidence`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_evidence_is_separate_from_decision_outputs` via `_policy_with_context_only_evidence`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
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
| In-memory mutation | `chapter["evidence"][1]["evidence_direction"] = "CONTEXT_ONLY"`<br>`route["route_kind"] = "DIRECT_ROUTE"`<br>`route["condition_evidence_ids"] = []`<br>`chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _policy_with_context_only_evidence(
    policy: BessZoningPolicyConfig,
) -> BessZoningPolicyConfig:
    payload = _payload(policy)
    chapter = payload["chapters"][0]
    chapter["evidence"][1]["evidence_direction"] = "CONTEXT_ONLY"
    route = chapter["route_assessments"][0]
    route["route_kind"] = "DIRECT_ROUTE"
    route["condition_evidence_ids"] = []
    chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
    return BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_validate`

**Purpose:** Implements `validate` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def _validate(inputs, result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_result_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_result_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_catalog_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_catalog_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_route_table_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_route_table_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_route_link_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_route_link_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_reverse_link_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_reverse_link_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_evidence_route_link_hash_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_route_link_hash_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_old_result_hash_schemas_are_rejected` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_result_hash_schemas_are_rejected` via `_validate`
- direct call: `tests.unit.test_interpret_bess_zoning::test_readback_result_validates` via `_validate`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_readback_result_validates` via `_validate`

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
def _validate(inputs, result) -> None:
    validate_bess_zoning_precheck(*inputs, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_package_exports_precheck_api`

**Purpose:** Regression invariant: package exports precheck api. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_package_exports_precheck_api() -> None:
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_package_exports_precheck_api() -> None:
    for name in (
        "BessZoningPolicyConfig",
        "BessZoningPrecheckError",
        "BessZoningPrecheckResult",
        "interpret_bess_zoning",
        "load_bess_zoning_policy_config",
        "planning_regulation_section_page_fragments",
        "validate_bess_zoning_precheck",
        "validate_planning_regulation_structure_with_fragments",
    ):
        assert name in stages.__all__
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_locked_policy_builds_complete_outputs`

**Purpose:** Regression invariant: valid locked policy builds complete outputs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS`
  - `assert tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS`
  - `assert tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS`
  - `assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS`
  - `assert (<br>        tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS<br>    )`
  - `assert len(result.chapter_policy) == 2`
  - `assert len(result.source_zone_policy) == 3`
  - `assert len(result.parcel_zone_interpretations) == 5`
  - `assert len(result.parcels) == len(parcels)`
  - `assert result.policy_schema_version == 5`
  - `assert result.result_hash_schema_version == 5`
  - `assert tuple(result.evidence_catalog.columns) == EVIDENCE_CATALOG_COLUMNS`
  - `assert result.planning_precheck_scope == "WRITTEN_ZONING_REGULATION_ONLY"`
  - `assert result.review_scope == "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"`
  - `assert result.parcels["review_scope"].eq(result.review_scope).all()`
  - `assert len(result.route_assessments) == 2`
  - `assert len(result.evidence_route_links) == 3`
  - `assert result.touch_only_relation_count == 1`
  - `assert result.document_id == index.document_id`
  - `assert (<br>        result.structure_result_content_sha256<br>        == structure.structure_result_content_sha256<br>    )`
  - `assert result.zoning_relation_hash_columns == tuple(relations.columns)`
  - `assert set(result.source_zone_policy["source_zone_label_raw"]) == set(<br>        zones["zone_label_raw"]<br>    )`
  - `assert result.policy_profile == policy.policy_profile`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["review_scope"].eq(result.review_scope).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["review_scope"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
    index, structure, _, zones, relations, parcels, _, policy = inputs
    result = valid_result
    _validate(inputs, result)
    assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS
    assert tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS
    assert tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS
    assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS
    assert (
        tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS
    )
    assert len(result.chapter_policy) == 2
    assert len(result.source_zone_policy) == 3
    assert len(result.parcel_zone_interpretations) == 5
    assert len(result.parcels) == len(parcels)
    assert result.policy_schema_version == 5
    assert result.result_hash_schema_version == 5
    assert tuple(result.evidence_catalog.columns) == EVIDENCE_CATALOG_COLUMNS
    assert result.planning_precheck_scope == "WRITTEN_ZONING_REGULATION_ONLY"
    assert result.review_scope == "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"
    assert result.parcels["review_scope"].eq(result.review_scope).all()
    assert len(result.route_assessments) == 2
    assert len(result.evidence_route_links) == 3
    assert result.touch_only_relation_count == 1
    assert result.document_id == index.document_id
    assert (
        result.structure_result_content_sha256
        == structure.structure_result_content_sha256
    )
    assert result.zoning_relation_hash_columns == tuple(relations.columns)
    assert set(result.source_zone_policy["source_zone_label_raw"]) == set(
        zones["zone_label_raw"]
    )
    assert result.policy_profile == policy.policy_profile
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_lock_mismatch_is_rejected`

**Purpose:** Regression invariant: source lock mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "field",
    [
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from factual source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
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
| In-memory mutation | `payload["source_lock"][field] = "f" * 64 if "sha256" in field else "wrong"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["source_lock"][field] = "f" * 64 if "sha256" in field else "wrong"
    bad = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="differs from factual source"):
        interpret_bess_zoning(*sources, bad)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_and_extra_chapter_are_rejected`

**Purpose:** Regression invariant: missing and extra chapter are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="completeness differs")`
  - `pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `missing_payload["chapters"] = missing_payload["chapters"][:-1]`<br>`extra["resolved_zone_chapter_label"] = "EXTRA"`<br>`extra["evidence"] = []`<br>`extra["route_assessments"] = []`<br>`extra["zoning_precheck_status"] = "UNKNOWN"`<br>`extra_payload["chapters"] = (*extra_payload["chapters"], extra)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
    *sources, policy = inputs
    missing_payload = _payload(policy)
    missing_payload["chapters"] = missing_payload["chapters"][:-1]
    with pytest.raises(BessZoningPrecheckError, match="completeness differs"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(missing_payload)
        )
    extra_payload = _payload(policy)
    extra = dict(extra_payload["chapters"][0])
    extra["resolved_zone_chapter_label"] = "EXTRA"
    extra["evidence"] = []
    extra["route_assessments"] = []
    extra["zoning_precheck_status"] = "UNKNOWN"
    extra_payload["chapters"] = (*extra_payload["chapters"], extra)
    with pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(extra_payload)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_regulation_zone_chapter_labels_and_ids_must_be_unique`

**Purpose:** Regression invariant: regulation zone chapter labels and ids must be unique. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_regulation_zone_chapter_labels_and_ids_must_be_unique(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="labels must be unique")`
  - `pytest.raises(BessZoningPrecheckError, match="section IDs must be unique")`
- Exact assertions:
  - `assert len(interpret_module._zone_chapter_rows(structure)) == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `interpret_module._zone_chapter_rows` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections.loc[<br>            structure.sections["section_type"].eq("ZONE_CHAPTER")<br>            & structure.sections["zone_chapter_label"].eq("U")<br>        ]<br>        .iloc[0]<br>        .copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pd.concat` | `pandas.concat` |
| `used.to_frame` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `used.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `unused_one.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `unused_one.to_frame` | `unresolved local/third-party receiver; no ownership inferred` |
| `unused_two.to_frame` | `unresolved local/third-party receiver; no ownership inferred` |
| `duplicate_id.to_frame` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `used["section_id"] = "SECTION-DUPLICATE-U"`<br>`unused_one["section_id"] = "SECTION-UNUSED-X-1"`<br>`unused_one["zone_chapter_label"] = "X"`<br>`unused_two["section_id"] = "SECTION-UNUSED-X-2"`<br>`duplicate_id["section_id"] = structure.sections.loc[<br>        structure.sections["section_type"].eq("ZONE_CHAPTER"), "section_id"<br>    ].iloc[1]`<br>`duplicate_id["zone_chapter_label"] = "X"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_regulation_zone_chapter_labels_and_ids_must_be_unique(inputs) -> None:
    structure = inputs[1]
    assert len(interpret_module._zone_chapter_rows(structure)) == 2

    used = (
        structure.sections.loc[
            structure.sections["section_type"].eq("ZONE_CHAPTER")
            & structure.sections["zone_chapter_label"].eq("U")
        ]
        .iloc[0]
        .copy()
    )
    used["section_id"] = "SECTION-DUPLICATE-U"
    duplicated_used = replace(
        structure,
        sections=pd.concat([structure.sections, used.to_frame().T], ignore_index=True),
    )
    with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_used)

    unused_one = used.copy()
    unused_one["section_id"] = "SECTION-UNUSED-X-1"
    unused_one["zone_chapter_label"] = "X"
    unused_two = unused_one.copy()
    unused_two["section_id"] = "SECTION-UNUSED-X-2"
    duplicated_unused = replace(
        structure,
        sections=pd.concat(
            [
                structure.sections,
                unused_one.to_frame().T,
                unused_two.to_frame().T,
            ],
            ignore_index=True,
        ),
    )
    with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_unused)

    duplicate_id = used.copy()
    duplicate_id["section_id"] = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER"), "section_id"
    ].iloc[1]
    duplicate_id["zone_chapter_label"] = "X"
    duplicated_section_id = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate_id.to_frame().T], ignore_index=True
        ),
    )
    with pytest.raises(BessZoningPrecheckError, match="section IDs must be unique"):
        interpret_module._zone_chapter_rows(duplicated_section_id)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_validator_rejects_later_duplicate_chapter`

**Purpose:** Regression invariant: source complete validator rejects later duplicate chapter. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_validator_rejects_later_duplicate_chapter(
    inputs, valid_result
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.sections.loc[structure.sections["section_type"].eq("ZONE_CHAPTER")]<br>        .iloc[0]<br>        .copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pd.concat` | `pandas.concat` |
| `duplicate.to_frame` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `duplicate["section_id"] = "SECTION-LATE-DUPLICATE"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_complete_validator_rejects_later_duplicate_chapter(
    inputs, valid_result
) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    duplicate = (
        structure.sections.loc[structure.sections["section_type"].eq("ZONE_CHAPTER")]
        .iloc[0]
        .copy()
    )
    duplicate["section_id"] = "SECTION-LATE-DUPLICATE"
    changed = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate.to_frame().T], ignore_index=True
        ),
    )
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(
            index,
            changed,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            policy,
            valid_result,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_chapter_and_evidence_id_are_rejected`

**Purpose:** Regression invariant: duplicate chapter and evidence id are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_chapter_and_evidence_id_are_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="chapter policy labels must be unique")`
  - `pytest.raises(ValueError, match="evidence IDs must be globally unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `chapter_payload["chapters"] = (<br>        *chapter_payload["chapters"],<br>        chapter_payload["chapters"][0],<br>    )`<br>`evidence_payload["chapters"][1]["evidence"][0]["evidence_id"] = "E-U-POSITIVE"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_chapter_and_evidence_id_are_rejected(inputs) -> None:
    policy = inputs[-1]
    chapter_payload = _payload(policy)
    chapter_payload["chapters"] = (
        *chapter_payload["chapters"],
        chapter_payload["chapters"][0],
    )
    with pytest.raises(ValueError, match="chapter policy labels must be unique"):
        BessZoningPolicyConfig.model_validate(chapter_payload)
    evidence_payload = _payload(policy)
    evidence_payload["chapters"][1]["evidence"][0]["evidence_id"] = "E-U-POSITIVE"
    with pytest.raises(ValueError, match="evidence IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(evidence_payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_excerpt_cannot_be_reused_with_contradictory_directions`

**Purpose:** Regression invariant: one excerpt cannot be reused with contradictory directions. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_one_excerpt_cannot_be_reused_with_contradictory_directions(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="chapter-scoped evidence occurrence")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `first["evidence_direction"] = "SUPPORTS_POTENTIAL_COMPATIBILITY"`<br>`second["evidence_id"] = "E-U-2"`<br>`second["evidence_direction"] = "SUPPORTS_DIFFICULTY"`<br>`payload["chapters"][0]["evidence"] = (first, second)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_one_excerpt_cannot_be_reused_with_contradictory_directions(inputs) -> None:
    payload = _payload(inputs[-1])
    first = dict(payload["chapters"][0]["evidence"][1])
    second = dict(first)
    first["evidence_direction"] = "SUPPORTS_POTENTIAL_COMPATIBILITY"
    second["evidence_id"] = "E-U-2"
    second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    payload["chapters"][0]["evidence"] = (first, second)
    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected`

**Purpose:** Regression invariant: duplicate chapter scoped occurrence in one route is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="chapter-scoped evidence occurrence")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `duplicate["evidence_id"] = "E-U-POSITIVE-DUPLICATE"`<br>`payload["chapters"][0]["evidence"] = (<br>        *payload["chapters"][0]["evidence"],<br>        duplicate,<br>    )`<br>`payload["chapters"][0]["route_assessments"][0]["positive_evidence_ids"] = [<br>        "E-U-POSITIVE",<br>        "E-U-POSITIVE-DUPLICATE",<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    duplicate = dict(payload["chapters"][0]["evidence"][0])
    duplicate["evidence_id"] = "E-U-POSITIVE-DUPLICATE"
    payload["chapters"][0]["evidence"] = (
        *payload["chapters"][0]["evidence"],
        duplicate,
    )
    payload["chapters"][0]["route_assessments"][0]["positive_evidence_ids"] = [
        "E-U-POSITIVE",
        "E-U-POSITIVE-DUPLICATE",
    ]

    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_occurrence_in_different_compatible_routes_is_rejected`

**Purpose:** Regression invariant: duplicate occurrence in different compatible routes is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_occurrence_in_different_compatible_routes_is_rejected(
    inputs,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="chapter-scoped evidence occurrence")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `duplicate["evidence_id"] = "E-N-DUPLICATE-ROUTE"`<br>`payload["chapters"][1]["evidence"] = (<br>        *payload["chapters"][1]["evidence"],<br>        duplicate,<br>    )`<br>`payload["chapters"][1]["route_assessments"] = (<br>        *payload["chapters"][1]["route_assessments"],<br>        {<br>            "route_id": "ROUTE-N-DUPLICATE-OCCURRENCE",<br>            "route_kind": "DIFFICULTY_ONLY",<br>            "positive_evidence_ids": [],<br>            "condition_evidence_ids": [],<br>            "difficulty_evidence_ids": ["E-N-DUPLICATE-ROUTE"],<br>            "applicability_note": "A second route must not duplicate the occurrence.",<br>        },<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_occurrence_in_different_compatible_routes_is_rejected(
    inputs,
) -> None:
    payload = _payload(inputs[-1])
    duplicate = dict(payload["chapters"][1]["evidence"][0])
    duplicate["evidence_id"] = "E-N-DUPLICATE-ROUTE"
    payload["chapters"][1]["evidence"] = (
        *payload["chapters"][1]["evidence"],
        duplicate,
    )
    payload["chapters"][1]["route_assessments"] = (
        *payload["chapters"][1]["route_assessments"],
        {
            "route_id": "ROUTE-N-DUPLICATE-OCCURRENCE",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-N-DUPLICATE-ROUTE"],
            "applicability_note": "A second route must not duplicate the occurrence.",
        },
    )

    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_forbidden_or_invalid_final_status_is_rejected`

**Purpose:** Regression invariant: forbidden or invalid final status is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
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
| In-memory mutation | `payload["chapters"][0]["zoning_precheck_status"] = status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_confidence_and_unknown_field_are_rejected`

**Purpose:** Regression invariant: invalid confidence and unknown field are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_confidence_and_unknown_field_are_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `payload["chapters"][0]["zoning_precheck_confidence"] = "CERTAIN"`<br>`payload["automatic_classifier"] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_confidence_and_unknown_field_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_confidence"] = "CERTAIN"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    payload["automatic_classifier"] = True
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_yaml_key_is_rejected`

**Purpose:** Regression invariant: duplicate yaml key is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(BessZoningPrecheckError, match="Duplicate YAML.*key")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text(
        "schema_version: 2\nschema_version: 2\n",
        encoding="utf-8",
    )
    with pytest.raises(BessZoningPrecheckError, match="Duplicate YAML.*key"):
        load_bess_zoning_policy_config(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_old_policy_schema_versions_are_rejected`

**Purpose:** Regression invariant: old policy schema versions are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_old_policy_schema_versions_are_rejected(inputs, version: int) -> None:
```

- Exact decorators: `pytest.mark.parametrize("version", [1, 2, 3, 4])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="unsupported BESS zoning policy schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
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
| In-memory mutation | `payload["schema_version"] = version` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_old_policy_schema_versions_are_rejected(inputs, version: int) -> None:
    payload = _payload(inputs[-1])
    payload["schema_version"] = version
    with pytest.raises(ValueError, match="unsupported BESS zoning policy schema"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_evidence_kind_has_an_explicit_direction_matrix`

**Purpose:** Regression invariant: every evidence kind has an explicit direction matrix. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_evidence_kind_has_an_explicit_direction_matrix(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>                    ValueError,<br>                    match="kind and direction are incompatible",<br>                )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `allowed.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `interpret_module.PolicyEvidence.model_validate` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |

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
| In-memory mutation | `evidence["evidence_kind"] = kind`<br>`evidence["evidence_direction"] = direction` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_every_evidence_kind_has_an_explicit_direction_matrix(inputs) -> None:
    allowed = {
        "USE_PERMISSION": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "CONTEXT_ONLY",
        },
        "USE_RESTRICTION": {"SUPPORTS_DIFFICULTY", "CONTEXT_ONLY"},
        "PUBLIC_INTEREST_EXCEPTION": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "TECHNICAL_EQUIPMENT_RULE": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "ICPE_RULE": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "RISK_OR_NUISANCE_CONDITION": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "ACCESS_OR_NETWORK_CONDITION": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "OTHER_RELEVANT_RULE": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
    }
    directions = {
        "SUPPORTS_POTENTIAL_COMPATIBILITY",
        "SUPPORTS_DIFFICULTY",
        "CONDITION",
        "CONTEXT_ONLY",
    }
    base = _payload(inputs[-1])["chapters"][0]["evidence"][0]
    for kind, permitted in allowed.items():
        for direction in directions:
            evidence = dict(base)
            evidence["evidence_kind"] = kind
            evidence["evidence_direction"] = direction
            if direction in permitted:
                interpret_module.PolicyEvidence.model_validate(evidence)
            else:
                with pytest.raises(
                    ValueError,
                    match="kind and direction are incompatible",
                ):
                    interpret_module.PolicyEvidence.model_validate(evidence)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_exact_evidence_is_preserved`

**Purpose:** Regression invariant: valid exact evidence is preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert excerpt == "Technical equipment is permitted"`
  - `assert (<br>        policy.chapters[0].evidence[0].excerpt_sha256<br>        == sha256(excerpt.encode()).hexdigest()<br>    )`
  - `assert valid_result.chapter_policy.iloc[0]["evidence_ids"] == (<br>        "E-U-POSITIVE",<br>        "E-U-CONDITION",<br>    )`
  - `assert "only when" in row["source_rule_excerpt"]`
  - `assert row["source_rule_excerpt"][relative_start:relative_end] == excerpt`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256(excerpt.encode()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `excerpt.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_result.evidence_catalog.set_index` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.set_index` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(excerpt.encode()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
    policy = inputs[-1]
    excerpt = policy.chapters[0].evidence[0].exact_raw_excerpt
    assert excerpt == "Technical equipment is permitted"
    assert (
        policy.chapters[0].evidence[0].excerpt_sha256
        == sha256(excerpt.encode()).hexdigest()
    )
    assert valid_result.chapter_policy.iloc[0]["evidence_ids"] == (
        "E-U-POSITIVE",
        "E-U-CONDITION",
    )
    row = valid_result.evidence_catalog.set_index("evidence_id").loc["E-U-POSITIVE"]
    assert "only when" in row["source_rule_excerpt"]
    relative_start = row["excerpt_start"] - row["source_rule_start"]
    relative_end = row["excerpt_end"] - row["source_rule_start"]
    assert row["source_rule_excerpt"][relative_start:relative_end] == excerpt
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_rule_identity_and_containment_are_strict`

**Purpose:** Regression invariant: source rule identity and containment are strict. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_rule_identity_and_containment_are_strict(inputs, mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["hash", "start", "end", "outside"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="source rule SHA256")`
  - `pytest.raises(ValueError, match="inside its source rule")`
  - `pytest.raises(BessZoningPrecheckError, match="source-rule offsets")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
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
| In-memory mutation | `evidence["source_rule_sha256"] = "f" * 64`<br>`evidence["source_rule_start"] = evidence["excerpt_start"] + 1`<br>`related["source_rule_start"] -= 1`<br>`related["source_rule_end"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_rule_identity_and_containment_are_strict(inputs, mutation: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    evidence = payload["chapters"][0]["evidence"][0]
    if mutation == "hash":
        evidence["source_rule_sha256"] = "f" * 64
        with pytest.raises(ValueError, match="source rule SHA256"):
            BessZoningPolicyConfig.model_validate(payload)
        return
    if mutation == "outside":
        evidence["source_rule_start"] = evidence["excerpt_start"] + 1
        with pytest.raises(ValueError, match="inside its source rule"):
            BessZoningPolicyConfig.model_validate(payload)
        return
    for related in payload["chapters"][0]["evidence"]:
        if mutation == "start":
            related["source_rule_start"] -= 1
        else:
            related["source_rule_end"] += 1
    with pytest.raises(BessZoningPrecheckError, match="source-rule offsets"):
        interpret_bess_zoning(
            *sources,
            BessZoningPolicyConfig.model_validate(payload),
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_same_rule_text_at_distinct_offsets_has_distinct_identity`

**Purpose:** Regression invariant: same rule text at distinct offsets has distinct identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_same_rule_text_at_distinct_offsets_has_distinct_identity(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.chapters[0].evidence[-1].evidence_direction == "SUPPORTS_DIFFICULTY"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `second["evidence_id"] = "E-U-SECOND-OCCURRENCE"`<br>`second["evidence_kind"] = "TECHNICAL_EQUIPMENT_RULE"`<br>`second["evidence_direction"] = "SUPPORTS_DIFFICULTY"`<br>`second["source_rule_id"] = "RULE-U-SECOND-OCCURRENCE"`<br>`second["source_rule_start"] = second_rule_start`<br>`second["source_rule_end"] = second_rule_start + rule_length`<br>`second["excerpt_start"] = second_rule_start`<br>`second["excerpt_end"] = second_rule_start + len(first["exact_raw_excerpt"])`<br>`chapter["evidence"] = (*chapter["evidence"], second)`<br>`chapter["route_assessments"] = (<br>        *chapter["route_assessments"],<br>        {<br>            "route_id": "ROUTE-U-SECOND-DIFFICULTY",<br>            "route_kind": "DIFFICULTY_ONLY",<br>            "positive_evidence_ids": [],<br>            "condition_evidence_ids": [],<br>            "difficulty_evidence_ids": ["E-U-SECOND-OCCURRENCE"],<br>            "applicability_note": "The distinct occurrence is linked explicitly.",<br>        },<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_same_rule_text_at_distinct_offsets_has_distinct_identity(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    first = chapter["evidence"][0]
    second = dict(first)
    rule_length = len(first["source_rule_excerpt"])
    second_rule_start = first["source_rule_end"] + 1
    second["evidence_id"] = "E-U-SECOND-OCCURRENCE"
    second["evidence_kind"] = "TECHNICAL_EQUIPMENT_RULE"
    second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    second["source_rule_id"] = "RULE-U-SECOND-OCCURRENCE"
    second["source_rule_start"] = second_rule_start
    second["source_rule_end"] = second_rule_start + rule_length
    second["excerpt_start"] = second_rule_start
    second["excerpt_end"] = second_rule_start + len(first["exact_raw_excerpt"])
    chapter["evidence"] = (*chapter["evidence"], second)
    chapter["route_assessments"] = (
        *chapter["route_assessments"],
        {
            "route_id": "ROUTE-U-SECOND-DIFFICULTY",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-U-SECOND-OCCURRENCE"],
            "applicability_note": "The distinct occurrence is linked explicitly.",
        },
    )
    policy = BessZoningPolicyConfig.model_validate(payload)
    assert policy.chapters[0].evidence[-1].evidence_direction == "SUPPORTS_DIFFICULTY"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_real_muret_source_rules_preserve_conditional_and_exception_frames`

**Purpose:** Regression invariant: real muret source rules preserve conditional and exception frames. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_real_muret_source_rules_preserve_conditional_and_exception_frames() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert "ne sont autorisées qu’à" in positive.source_rule_excerpt`
  - `assert "condition" in positive.source_rule_excerpt`
  - `assert positive.source_rule_excerpt.startswith("Toutes constructions")`
  - `assert "autres que celles" in positive.source_rule_excerpt`
  - `assert positive.source_rule_excerpt.startswith("Sont interdites")`
  - `assert difficulty.source_rule_id == positive.source_rule_id`
  - `assert difficulty.source_rule_excerpt == positive.source_rule_excerpt`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |
| `Path` | `pathlib.Path` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `positive.source_rule_excerpt.startswith` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_real_muret_source_rules_preserve_conditional_and_exception_frames() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    by_label = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    for label in ("UA", "UB", "UC", "UD", "UF", "AU", "AUf"):
        positive = next(
            evidence
            for evidence in by_label[label].evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert "ne sont autorisées qu’à" in positive.source_rule_excerpt
        assert "condition" in positive.source_rule_excerpt
    for label in ("UP", "AUp"):
        positive = next(
            evidence
            for evidence in by_label[label].evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert positive.source_rule_excerpt.startswith("Toutes constructions")
        assert "autres que celles" in positive.source_rule_excerpt
    for label in ("AU0", "AUf0", "A", "N"):
        chapter = by_label[label]
        positive = next(
            evidence
            for evidence in chapter.evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert positive.source_rule_excerpt.startswith("Sont interdites")
        if label in {"A", "N"}:
            difficulty = next(
                evidence
                for evidence in chapter.evidence
                if evidence.evidence_direction == "SUPPORTS_DIFFICULTY"
            )
            assert difficulty.source_rule_id == positive.source_rule_id
            assert difficulty.source_rule_excerpt == positive.source_rule_excerpt
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_real_muret_up_route_does_not_use_the_separate_icpe_condition`

**Purpose:** Regression invariant: real muret up route does not use the separate icpe condition. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_real_muret_up_route_does_not_use_the_separate_icpe_condition() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.schema_version == 5`
  - `assert policy.policy_profile == "muret_bess_written_zoning_v6"`
  - `assert route.route_kind == "RESTRICTION_EXCEPTION_ROUTE"`
  - `assert route.positive_evidence_ids == ("MURET-UP-PUBLIC-ROUTE-01",)`
  - `assert route.condition_evidence_ids == ()`
  - `assert route.difficulty_evidence_ids == ("MURET-UP-RESTRICTION-01",)`
  - `assert restriction.evidence_kind == "USE_RESTRICTION"`
  - `assert restriction.evidence_direction == "SUPPORTS_DIFFICULTY"`
  - `assert restriction.section_id == "SECTION-0080"`
  - `assert restriction.page_number == 71`
  - `assert (<br>        restriction.exact_raw_excerpt<br>        == "Toutes constructions ou  installations autres que celles"<br>    )`
  - `assert restriction.excerpt_start == 68`
  - `assert restriction.excerpt_end == 124`
  - `assert restriction.excerpt_sha256 == (<br>        "edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462"<br>    )`
  - `assert restriction.section_page_fragment_sha256 == (<br>        "06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"<br>    )`
  - `assert restriction.source_rule_id == "MURET-UP-ROUTE-RULE-01"`
  - `assert restriction.source_rule_start == 68`
  - `assert restriction.source_rule_end == 236`
  - `assert restriction.source_rule_sha256 == (<br>        "de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |
| `Path` | `pathlib.Path` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_real_muret_up_route_does_not_use_the_separate_icpe_condition() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    assert policy.schema_version == 5
    assert policy.policy_profile == "muret_bess_written_zoning_v6"
    chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "UP"
    )
    route = chapter.route_assessments[0]

    assert route.route_kind == "RESTRICTION_EXCEPTION_ROUTE"
    assert route.positive_evidence_ids == ("MURET-UP-PUBLIC-ROUTE-01",)
    assert route.condition_evidence_ids == ()
    assert route.difficulty_evidence_ids == ("MURET-UP-RESTRICTION-01",)

    restriction = next(
        evidence
        for evidence in chapter.evidence
        if evidence.evidence_id == "MURET-UP-RESTRICTION-01"
    )
    assert restriction.evidence_kind == "USE_RESTRICTION"
    assert restriction.evidence_direction == "SUPPORTS_DIFFICULTY"
    assert restriction.section_id == "SECTION-0080"
    assert restriction.page_number == 71
    assert (
        restriction.exact_raw_excerpt
        == "Toutes constructions ou  installations autres que celles"
    )
    assert restriction.excerpt_start == 68
    assert restriction.excerpt_end == 124
    assert restriction.excerpt_sha256 == (
        "edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462"
    )
    assert restriction.section_page_fragment_sha256 == (
        "06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"
    )
    assert restriction.source_rule_id == "MURET-UP-ROUTE-RULE-01"
    assert restriction.source_rule_start == 68
    assert restriction.source_rule_end == 236
    assert restriction.source_rule_sha256 == (
        "de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite`

**Purpose:** Regression invariant: real muret aup route uses the general infrastructure prerequisite. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert route.route_kind == "CONDITIONAL_ROUTE"`
  - `assert route.positive_evidence_ids == ("MURET-AUP-PUBLIC-ROUTE-01",)`
  - `assert route.condition_evidence_ids == ("MURET-AUP-INFRASTRUCTURE-CONDITION-01",)`
  - `assert route.difficulty_evidence_ids == ()`
  - `assert prerequisite.evidence_kind == "ACCESS_OR_NETWORK_CONDITION"`
  - `assert prerequisite.evidence_direction == "CONDITION"`
  - `assert prerequisite.section_id == "SECTION-0111"`
  - `assert prerequisite.page_number == 93`
  - `assert prerequisite.exact_raw_excerpt == exact_rule`
  - `assert prerequisite.excerpt_start == 98`
  - `assert prerequisite.excerpt_end == 325`
  - `assert prerequisite.excerpt_sha256 == (<br>        "b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"<br>    )`
  - `assert prerequisite.section_page_fragment_sha256 == (<br>        "57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"<br>    )`
  - `assert prerequisite.source_rule_id == "MURET-AUp-INFRASTRUCTURE-RULE-01"`
  - `assert prerequisite.source_rule_excerpt == exact_rule`
  - `assert prerequisite.source_rule_start == 98`
  - `assert prerequisite.source_rule_end == 325`
  - `assert prerequisite.source_rule_sha256 == prerequisite.excerpt_sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |
| `Path` | `pathlib.Path` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "AUp"
    )
    route = chapter.route_assessments[0]

    assert route.route_kind == "CONDITIONAL_ROUTE"
    assert route.positive_evidence_ids == ("MURET-AUP-PUBLIC-ROUTE-01",)
    assert route.condition_evidence_ids == ("MURET-AUP-INFRASTRUCTURE-CONDITION-01",)
    assert route.difficulty_evidence_ids == ()

    prerequisite = next(
        evidence
        for evidence in chapter.evidence
        if evidence.evidence_id == "MURET-AUP-INFRASTRUCTURE-CONDITION-01"
    )
    exact_rule = (
        "Les constructions et opérations ne pourront être autorisées qu’après "
        "réalisation des  \n"
        "équipements d’infrastructure indispensable à leur fonctionnement "
        "(accès, voirie et  \n"
        "réseaux divers) conformément aux articles AUp3 et AUp4."
    )
    assert prerequisite.evidence_kind == "ACCESS_OR_NETWORK_CONDITION"
    assert prerequisite.evidence_direction == "CONDITION"
    assert prerequisite.section_id == "SECTION-0111"
    assert prerequisite.page_number == 93
    assert prerequisite.exact_raw_excerpt == exact_rule
    assert prerequisite.excerpt_start == 98
    assert prerequisite.excerpt_end == 325
    assert prerequisite.excerpt_sha256 == (
        "b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"
    )
    assert prerequisite.section_page_fragment_sha256 == (
        "57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"
    )
    assert prerequisite.source_rule_id == "MURET-AUp-INFRASTRUCTURE-RULE-01"
    assert prerequisite.source_rule_excerpt == exact_rule
    assert prerequisite.source_rule_start == 98
    assert prerequisite.source_rule_end == 325
    assert prerequisite.source_rule_sha256 == prerequisite.excerpt_sha256
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_real_muret_up_and_aup_keep_icpe_applicability_as_context`

**Purpose:** Regression invariant: real muret up and aup keep icpe applicability as context. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_real_muret_up_and_aup_keep_icpe_applicability_as_context() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert evidence.evidence_kind == "ICPE_RULE"`
  - `assert evidence.evidence_direction == "CONTEXT_ONLY"`
  - `assert "ICPE" in chapter.missing_information`
  - `assert evidence_id not in linked_ids`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |
| `Path` | `pathlib.Path` |
| `identities.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_real_muret_up_and_aup_keep_icpe_applicability_as_context() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    chapters = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    identities = {
        "UP": "MURET-UP-ICPE-CONDITION-01",
        "AUp": "MURET-AUP-ICPE-CONDITION-01",
    }

    for label, evidence_id in identities.items():
        chapter = chapters[label]
        evidence = next(
            item for item in chapter.evidence if item.evidence_id == evidence_id
        )
        assert evidence.evidence_kind == "ICPE_RULE"
        assert evidence.evidence_direction == "CONTEXT_ONLY"
        assert "ICPE" in chapter.missing_information
        for route in chapter.route_assessments:
            linked_ids = (
                route.positive_evidence_ids
                + route.condition_evidence_ids
                + route.difficulty_evidence_ids
            )
            assert evidence_id not in linked_ids
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_absent_excerpt_and_section_page_mismatch_are_rejected`

**Purpose:** Regression invariant: absent excerpt and section page mismatch are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_absent_excerpt_and_section_page_mismatch_are_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="offsets")`
  - `pytest.raises(BessZoningPrecheckError, match="section/page fragment")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `sha256(<br>        excerpt.encode()<br>    ).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `excerpt.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(<br>        excerpt.encode()<br>    ).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt`<br>`payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(<br>        excerpt.encode()<br>    ).hexdigest()`<br>`evidence["page_number"] = 3` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_absent_excerpt_and_section_page_mismatch_are_rejected(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    excerpt = "Not present in the indexed source."
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(BessZoningPrecheckError, match="offsets"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
    payload = _payload(policy)
    for evidence in payload["chapters"][0]["evidence"]:
        evidence["page_number"] = 3
    with pytest.raises(BessZoningPrecheckError, match="section/page fragment"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_excerpt_hash_and_length_are_rejected`

**Purpose:** Regression invariant: excerpt hash and length are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_excerpt_hash_and_length_are_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="excerpt SHA256 differs")`
  - `pytest.raises(ValueError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `sha256(<br>        excerpt.encode()<br>    ).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `excerpt.encode` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(<br>        excerpt.encode()<br>    ).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = "f" * 64`<br>`payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt`<br>`payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(<br>        excerpt.encode()<br>    ).hexdigest()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_excerpt_hash_and_length_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="excerpt SHA256 differs"):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    excerpt = "x" * 601
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_declared_status_must_equal_derived_route_status`

**Purpose:** Regression invariant: declared status must equal derived route status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_declared_status_must_equal_derived_route_status(inputs, status: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "status", ["POTENTIALLY_COMPATIBLE", "LIKELY_DIFFICULT", "UNKNOWN"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="differs from coherent linked route")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
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
| In-memory mutation | `payload["chapters"][0]["zoning_precheck_status"] = status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_declared_status_must_equal_derived_route_status(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError, match="differs from coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_condition_alone_cannot_create_conditional_review`

**Purpose:** Regression invariant: condition alone cannot create conditional review. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="coherent linked route")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"`<br>`payload["chapters"][0]["evidence"] = [payload["chapters"][0]["evidence"][1]]`<br>`payload["chapters"][0]["route_assessments"] = []` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    payload["chapters"][0]["evidence"] = [payload["chapters"][0]["evidence"][1]]
    payload["chapters"][0]["route_assessments"] = []
    with pytest.raises(ValueError, match="coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unrelated_positive_and_condition_do_not_create_conditional_review`

**Purpose:** Regression invariant: unrelated positive and condition do not create conditional review. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unrelated_positive_and_condition_do_not_create_conditional_review(
    inputs,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="coherent\|linked route")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `chapter["zoning_precheck_status"] = "CONDITIONAL_REVIEW"`<br>`chapter["route_assessments"] = [<br>        {<br>            "route_id": "ROUTE-U-DIRECT-ONLY",<br>            "route_kind": "DIRECT_ROUTE",<br>            "positive_evidence_ids": ["E-U-POSITIVE"],<br>            "condition_evidence_ids": [],<br>            "difficulty_evidence_ids": [],<br>            "applicability_note": "The separate condition is deliberately unlinked.",<br>        }<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unrelated_positive_and_condition_do_not_create_conditional_review(
    inputs,
) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIRECT-ONLY",
            "route_kind": "DIRECT_ROUTE",
            "positive_evidence_ids": ["E-U-POSITIVE"],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": [],
            "applicability_note": "The separate condition is deliberately unlinked.",
        }
    ]
    with pytest.raises(ValueError, match="coherent|linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unlinked_context_only_unknown_succeeds`

**Purpose:** Regression invariant: unlinked context only unknown succeeds. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unlinked_context_only_unknown_succeeds(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.chapters[0].zoning_precheck_status == "UNKNOWN"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
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
| In-memory mutation | `chapter["zoning_precheck_status"] = "UNKNOWN"`<br>`chapter["zoning_precheck_confidence"] = "LOW"`<br>`chapter["evidence"] = [chapter["evidence"][1]]`<br>`chapter["evidence"][0]["evidence_direction"] = "CONTEXT_ONLY"`<br>`chapter["route_assessments"] = []` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unlinked_context_only_unknown_succeeds(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = [chapter["evidence"][1]]
    chapter["evidence"][0]["evidence_direction"] = "CONTEXT_ONLY"
    chapter["route_assessments"] = []
    policy = BessZoningPolicyConfig.model_validate(payload)
    assert policy.chapters[0].zoning_precheck_status == "UNKNOWN"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_positive_condition_and_conflict_status_routes`

**Purpose:** Regression invariant: positive condition and conflict status routes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_positive_condition_and_conflict_status_routes(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        BessZoningPolicyConfig.model_validate(payload)<br>        .chapters[0]<br>        .zoning_precheck_status<br>        == "CONDITIONAL_REVIEW"<br>    )`
  - `assert policy.chapters[0].zoning_precheck_status == "CONDITIONAL_REVIEW"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
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
| In-memory mutation | `conflict["chapters"][0]["evidence"][1]["evidence_direction"] = "SUPPORTS_DIFFICULTY"`<br>`route["route_kind"] = "RESTRICTION_EXCEPTION_ROUTE"`<br>`route["condition_evidence_ids"] = []`<br>`route["difficulty_evidence_ids"] = ["E-U-CONDITION"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_positive_condition_and_conflict_status_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    assert (
        BessZoningPolicyConfig.model_validate(payload)
        .chapters[0]
        .zoning_precheck_status
        == "CONDITIONAL_REVIEW"
    )
    conflict = _payload(inputs[-1])
    conflict["chapters"][0]["evidence"][1]["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    route = conflict["chapters"][0]["route_assessments"][0]
    route["route_kind"] = "RESTRICTION_EXCEPTION_ROUTE"
    route["condition_evidence_ids"] = []
    route["difficulty_evidence_ids"] = ["E-U-CONDITION"]
    policy = BessZoningPolicyConfig.model_validate(conflict)
    assert policy.chapters[0].zoning_precheck_status == "CONDITIONAL_REVIEW"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_route_references_must_be_same_chapter_and_role_compatible`

**Purpose:** Regression invariant: route references must be same chapter and role compatible. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_route_references_must_be_same_chapter_and_role_compatible(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `route["condition_evidence_ids"] = ["E-UNKNOWN"]`<br>`route["condition_evidence_ids"] = ["E-N-1"]`<br>`route["route_kind"] = "DIRECT_ROUTE"`<br>`route["positive_evidence_ids"] = ["E-U-CONDITION"]`<br>`route["condition_evidence_ids"] = []`<br>`payload["chapters"][0]["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_route_references_must_be_same_chapter_and_role_compatible(inputs) -> None:
    for mutation, message in (
        ("unknown", "unknown or another-chapter"),
        ("another_chapter", "unknown or another-chapter"),
        ("wrong_role", "incompatible positive role"),
    ):
        payload = _payload(inputs[-1])
        route = payload["chapters"][0]["route_assessments"][0]
        if mutation == "unknown":
            route["condition_evidence_ids"] = ["E-UNKNOWN"]
        elif mutation == "another_chapter":
            route["condition_evidence_ids"] = ["E-N-1"]
        else:
            route["route_kind"] = "DIRECT_ROUTE"
            route["positive_evidence_ids"] = ["E-U-CONDITION"]
            route["condition_evidence_ids"] = []
            payload["chapters"][0]["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
        with pytest.raises(ValueError, match=message):
            BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_route_ids_are_globally_unique`

**Purpose:** Regression invariant: route ids are globally unique. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_route_ids_are_globally_unique(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="route IDs must be globally unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `payload["chapters"][1]["route_assessments"][0]["route_id"] = payload["chapters"][0][<br>        "route_assessments"<br>    ][0]["route_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_route_ids_are_globally_unique(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][1]["route_assessments"][0]["route_id"] = payload["chapters"][0][
        "route_assessments"
    ][0]["route_id"]
    with pytest.raises(ValueError, match="route IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unlinked_difficulty_evidence_is_rejected`

**Purpose:** Regression invariant: unlinked difficulty evidence is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unlinked_difficulty_evidence_is_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="decision evidence must be linked")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `unlinked["evidence_id"] = "E-N-UNLINKED"`<br>`unlinked["source_rule_id"] = "RULE-N-UNLINKED"`<br>`unlinked[field] += 100`<br>`payload["chapters"][1]["evidence"] = (<br>        *payload["chapters"][1]["evidence"],<br>        unlinked,<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unlinked_difficulty_evidence_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    unlinked = dict(payload["chapters"][1]["evidence"][0])
    unlinked["evidence_id"] = "E-N-UNLINKED"
    unlinked["source_rule_id"] = "RULE-N-UNLINKED"
    for field in (
        "excerpt_start",
        "excerpt_end",
        "source_rule_start",
        "source_rule_end",
    ):
        unlinked[field] += 100
    payload["chapters"][1]["evidence"] = (
        *payload["chapters"][1]["evidence"],
        unlinked,
    )

    with pytest.raises(ValueError, match="decision evidence must be linked"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unlinked_positive_and_condition_evidence_are_rejected`

**Purpose:** Regression invariant: unlinked positive and condition evidence are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unlinked_positive_and_condition_evidence_are_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="decision evidence must be linked")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `unlinked["evidence_id"] = f"E-U-UNLINKED-{direction}"`<br>`unlinked["source_rule_id"] = f"RULE-U-UNLINKED-{direction}"`<br>`unlinked[field] += 100`<br>`payload["chapters"][0]["evidence"] = (<br>            *payload["chapters"][0]["evidence"],<br>            unlinked,<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unlinked_positive_and_condition_evidence_are_rejected(inputs) -> None:
    for direction, evidence_index in (
        ("SUPPORTS_POTENTIAL_COMPATIBILITY", 0),
        ("CONDITION", 1),
    ):
        payload = _payload(inputs[-1])
        unlinked = dict(payload["chapters"][0]["evidence"][evidence_index])
        unlinked["evidence_id"] = f"E-U-UNLINKED-{direction}"
        unlinked["source_rule_id"] = f"RULE-U-UNLINKED-{direction}"
        for field in (
            "excerpt_start",
            "excerpt_end",
            "source_rule_start",
            "source_rule_end",
        ):
            unlinked[field] += 100
        payload["chapters"][0]["evidence"] = (
            *payload["chapters"][0]["evidence"],
            unlinked,
        )
        with pytest.raises(ValueError, match="decision evidence must be linked"):
            BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_context_only_evidence_must_be_unlinked`

**Purpose:** Regression invariant: context only evidence must be unlinked. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_context_only_evidence_must_be_unlinked(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError)`
- Exact assertions:
  - `assert policy.chapters[0].evidence[1].evidence_direction == "CONTEXT_ONLY"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_policy_with_context_only_evidence` | `tests.unit.test_interpret_bess_zoning._policy_with_context_only_evidence` |
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `payload["chapters"][0]["route_assessments"][0]["condition_evidence_ids"] = [<br>        "E-U-CONDITION"<br>    ]`<br>`payload["chapters"][0]["route_assessments"][0]["route_kind"] = "CONDITIONAL_ROUTE"`<br>`payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_context_only_evidence_must_be_unlinked(inputs) -> None:
    policy = _policy_with_context_only_evidence(inputs[-1])
    assert policy.chapters[0].evidence[1].evidence_direction == "CONTEXT_ONLY"

    payload = _payload(policy)
    payload["chapters"][0]["route_assessments"][0]["condition_evidence_ids"] = [
        "E-U-CONDITION"
    ]
    payload["chapters"][0]["route_assessments"][0]["route_kind"] = "CONDITIONAL_ROUTE"
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_evidence_may_link_to_multiple_compatible_routes`

**Purpose:** Regression invariant: one evidence may link to multiple compatible routes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_one_evidence_may_link_to_multiple_compatible_routes(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert evidence["linked_route_ids"] == (<br>        "ROUTE-N-DIFFICULT",<br>        "ROUTE-N-DIFFICULT-SECOND",<br>    )`
  - `assert evidence["linked_route_roles"] == ("DIFFICULTY", "DIFFICULTY")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `result.evidence_catalog.set_index` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `route["route_id"] = "ROUTE-N-DIFFICULT-SECOND"`<br>`payload["chapters"][1]["route_assessments"] = (<br>        *payload["chapters"][1]["route_assessments"],<br>        route,<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_one_evidence_may_link_to_multiple_compatible_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    route = dict(payload["chapters"][1]["route_assessments"][0])
    route["route_id"] = "ROUTE-N-DIFFICULT-SECOND"
    payload["chapters"][1]["route_assessments"] = (
        *payload["chapters"][1]["route_assessments"],
        route,
    )
    policy = BessZoningPolicyConfig.model_validate(payload)
    *sources, _ = inputs
    result = interpret_bess_zoning(*sources, policy)
    evidence = result.evidence_catalog.set_index("evidence_id").loc["E-N-1"]
    assert evidence["linked_route_ids"] == (
        "ROUTE-N-DIFFICULT",
        "ROUTE-N-DIFFICULT-SECOND",
    )
    assert evidence["linked_route_roles"] == ("DIFFICULTY", "DIFFICULTY")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_difficulty_and_positive_only_status_routes`

**Purpose:** Regression invariant: difficulty and positive only status routes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_difficulty_and_positive_only_status_routes(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        BessZoningPolicyConfig.model_validate(difficult)<br>        .chapters[0]<br>        .zoning_precheck_status<br>        == "LIKELY_DIFFICULT"<br>    )`
  - `assert (<br>        BessZoningPolicyConfig.model_validate(potential)<br>        .chapters[0]<br>        .zoning_precheck_status<br>        == "POTENTIALLY_COMPATIBLE"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
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
| In-memory mutation | `chapter["zoning_precheck_status"] = "LIKELY_DIFFICULT"`<br>`chapter["evidence"] = [chapter["evidence"][1]]`<br>`chapter["evidence"][0]["evidence_direction"] = "SUPPORTS_DIFFICULTY"`<br>`chapter["route_assessments"] = [<br>        {<br>            "route_id": "ROUTE-U-DIFFICULT",<br>            "route_kind": "DIFFICULTY_ONLY",<br>            "positive_evidence_ids": [],<br>            "condition_evidence_ids": [],<br>            "difficulty_evidence_ids": ["E-U-CONDITION"],<br>            "applicability_note": "Only the linked difficulty is assessed.",<br>        }<br>    ]`<br>`chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"`<br>`chapter["evidence"] = [chapter["evidence"][0]]`<br>`chapter["route_assessments"] = [<br>        {<br>            "route_id": "ROUTE-U-DIRECT",<br>            "route_kind": "DIRECT_ROUTE",<br>            "positive_evidence_ids": ["E-U-POSITIVE"],<br>            "condition_evidence_ids": [],<br>            "difficulty_evidence_ids": [],<br>            "applicability_note": "Only the direct linked route is assessed.",<br>        }<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_difficulty_and_positive_only_status_routes(inputs) -> None:
    difficult = _payload(inputs[-1])
    chapter = difficult["chapters"][0]
    chapter["zoning_precheck_status"] = "LIKELY_DIFFICULT"
    chapter["evidence"] = [chapter["evidence"][1]]
    chapter["evidence"][0]["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIFFICULT",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-U-CONDITION"],
            "applicability_note": "Only the linked difficulty is assessed.",
        }
    ]
    assert (
        BessZoningPolicyConfig.model_validate(difficult)
        .chapters[0]
        .zoning_precheck_status
        == "LIKELY_DIFFICULT"
    )
    potential = _payload(inputs[-1])
    chapter = potential["chapters"][0]
    chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
    chapter["evidence"] = [chapter["evidence"][0]]
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIRECT",
            "route_kind": "DIRECT_ROUTE",
            "positive_evidence_ids": ["E-U-POSITIVE"],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": [],
            "applicability_note": "Only the direct linked route is assessed.",
        }
    ]
    assert (
        BessZoningPolicyConfig.model_validate(potential)
        .chapters[0]
        .zoning_precheck_status
        == "POTENTIALLY_COMPATIBLE"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_incomplete_review_requires_unknown_low`

**Purpose:** Regression invariant: incomplete review requires unknown low. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_incomplete_review_requires_unknown_low(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="incomplete review")`
- Exact assertions:
  - `assert (<br>        BessZoningPolicyConfig.model_validate(payload).chapters[0].review_completeness<br>        == "INCOMPLETE"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `pytest.raises` | `pytest.raises` |

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
| In-memory mutation | `chapter["review_completeness"] = "INCOMPLETE"`<br>`chapter["zoning_precheck_status"] = "UNKNOWN"`<br>`chapter["zoning_precheck_confidence"] = "LOW"`<br>`chapter["evidence"] = []`<br>`chapter["route_assessments"] = []`<br>`chapter["reviewed_section_ids"] = []`<br>`candidate["review_completeness"] = "INCOMPLETE"`<br>`candidate["zoning_precheck_status"] = "UNKNOWN"`<br>`candidate["zoning_precheck_confidence"] = "LOW"`<br>`candidate["evidence"] = []`<br>`candidate["route_assessments"] = []`<br>`candidate["reviewed_section_ids"] = []`<br>`candidate[field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_incomplete_review_requires_unknown_low(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["review_completeness"] = "INCOMPLETE"
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = []
    chapter["route_assessments"] = []
    chapter["reviewed_section_ids"] = []
    assert (
        BessZoningPolicyConfig.model_validate(payload).chapters[0].review_completeness
        == "INCOMPLETE"
    )
    for field, value in (
        ("zoning_precheck_status", "CONDITIONAL_REVIEW"),
        ("zoning_precheck_confidence", "MEDIUM"),
    ):
        invalid = _payload(inputs[-1])
        candidate = invalid["chapters"][0]
        candidate["review_completeness"] = "INCOMPLETE"
        candidate["zoning_precheck_status"] = "UNKNOWN"
        candidate["zoning_precheck_confidence"] = "LOW"
        candidate["evidence"] = []
        candidate["route_assessments"] = []
        candidate["reviewed_section_ids"] = []
        candidate[field] = value
        with pytest.raises(ValueError, match="incomplete review"):
            BessZoningPolicyConfig.model_validate(invalid)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_incomplete_review_persists_exact_missing_required_sections`

**Purpose:** Regression invariant: incomplete review persists exact missing required sections. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_incomplete_review_persists_exact_missing_required_sections(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["reviewed_section_ids"] == ()`
  - `assert row["missing_required_section_ids"] == expected_missing`
  - `assert row["zoning_precheck_status"] == "UNKNOWN"`
  - `assert row["zoning_precheck_confidence"] == "LOW"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `result.chapter_policy.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `inputs[1].sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `inputs[1].sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `chapter["review_completeness"] = "INCOMPLETE"`<br>`chapter["reviewed_section_ids"] = []`<br>`chapter["zoning_precheck_status"] = "UNKNOWN"`<br>`chapter["zoning_precheck_confidence"] = "LOW"`<br>`chapter["evidence"] = []`<br>`chapter["route_assessments"] = []` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_incomplete_review_persists_exact_missing_required_sections(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    chapter = payload["chapters"][0]
    chapter["review_completeness"] = "INCOMPLETE"
    chapter["reviewed_section_ids"] = []
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = []
    chapter["route_assessments"] = []
    result = interpret_bess_zoning(
        *sources,
        BessZoningPolicyConfig.model_validate(payload),
    )
    row = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
    assert row["reviewed_section_ids"] == ()
    expected_missing = tuple(
        inputs[1].sections.loc[
            inputs[1].sections["section_type"].eq("ARTICLE")
            & inputs[1].sections["zone_chapter_label"].eq("U"),
            "section_id",
        ]
    )
    assert row["missing_required_section_ids"] == expected_missing
    assert row["zoning_precheck_status"] == "UNKNOWN"
    assert row["zoning_precheck_confidence"] == "LOW"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_is_accepted_when_evidence_is_insufficient`

**Purpose:** Regression invariant: unknown is accepted when evidence is insufficient. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_is_accepted_when_evidence_is_insufficient(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.chapter_policy.iloc[0]["zoning_precheck_status"] == "UNKNOWN"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
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
| In-memory mutation | `payload["chapters"][0]["zoning_precheck_status"] = "UNKNOWN"`<br>`payload["chapters"][0]["evidence"] = []`<br>`payload["chapters"][0]["route_assessments"] = []` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_is_accepted_when_evidence_is_insufficient(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["chapters"][0]["zoning_precheck_status"] = "UNKNOWN"
    payload["chapters"][0]["evidence"] = []
    payload["chapters"][0]["route_assessments"] = []
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    assert result.chapter_policy.iloc[0]["zoning_precheck_status"] == "UNKNOWN"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_reviewed_sections_cover_required_articles`

**Purpose:** Regression invariant: reviewed sections cover required articles. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_reviewed_sections_cover_required_articles(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="omits required reviewed")`
- Exact assertions:
  - `assert index.document_id == "doc-1"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
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
| In-memory mutation | `payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_reviewed_sections_cover_required_articles(inputs) -> None:
    *sources, policy = inputs
    index, structure = inputs[:2]
    payload = _payload(policy)
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
    with pytest.raises(BessZoningPrecheckError, match="omits required reviewed"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
    assert index.document_id == "doc-1"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_configured_article_must_exist_once_in_every_chapter`

**Purpose:** Regression invariant: every configured article must exist once in every chapter. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_configured_article_must_exist_once_in_every_chapter(
    inputs,
    article_number: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("article_number", ["1", "2"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `article_number` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="exactly one.*article")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["article_number_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `structure.sections.loc[keep].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_module._required_section_ids_by_chapter` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_every_configured_article_must_exist_once_in_every_chapter(
    inputs,
    article_number: str,
) -> None:
    structure = inputs[1]
    policy = inputs[-1]
    keep = ~(
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("U")
        & structure.sections["article_number_raw"].eq(article_number)
    )
    changed = replace(
        structure,
        sections=structure.sections.loc[keep].reset_index(drop=True),
    )

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, policy)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_configured_article_is_rejected`

**Purpose:** Regression invariant: duplicate configured article is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_configured_article_is_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="exactly one.*article")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.sections.loc[<br>            structure.sections["section_type"].eq("ARTICLE")<br>            & structure.sections["zone_chapter_label"].eq("U")<br>            & structure.sections["article_number_raw"].eq("2")<br>        ]<br>        .iloc[0]<br>        .copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["article_number_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pd.concat` | `pandas.concat` |
| `duplicate.to_frame` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_module._required_section_ids_by_chapter` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `duplicate["section_id"] = "SECTION-DUPLICATE-U-2"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_configured_article_is_rejected(inputs) -> None:
    structure = inputs[1]
    duplicate = (
        structure.sections.loc[
            structure.sections["section_type"].eq("ARTICLE")
            & structure.sections["zone_chapter_label"].eq("U")
            & structure.sections["article_number_raw"].eq("2")
        ]
        .iloc[0]
        .copy()
    )
    duplicate["section_id"] = "SECTION-DUPLICATE-U-2"
    changed = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate.to_frame().T], ignore_index=True
        ),
    )

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, inputs[-1])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_configured_article_with_wrong_chapter_parent_is_rejected`

**Purpose:** Regression invariant: configured article with wrong chapter parent is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_configured_article_with_wrong_chapter_parent_is_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="exactly one.*article")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections["article_number_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `interpret_module._required_section_ids_by_chapter` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `sections.loc[target, "parent_section_id"] = n_chapter_id` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_configured_article_with_wrong_chapter_parent_is_rejected(inputs) -> None:
    structure = inputs[1]
    sections = structure.sections.copy(deep=True)
    n_chapter_id = sections.loc[
        sections["section_type"].eq("ZONE_CHAPTER")
        & sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
    target = (
        sections["section_type"].eq("ARTICLE")
        & sections["zone_chapter_label"].eq("U")
        & sections["article_number_raw"].eq("2")
    )
    sections.loc[target, "parent_section_id"] = n_chapter_id
    changed = replace(structure, sections=sections)

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, inputs[-1])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_evidence_must_be_inside_reviewed_sections`

**Purpose:** Regression invariant: evidence must be inside reviewed sections. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_evidence_must_be_inside_reviewed_sections(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="outside reviewed sections")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["article_number_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
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
| In-memory mutation | `payload["required_zone_article_numbers"] = ["2"]`<br>`payload["chapters"][0]["reviewed_section_ids"] = [chapter_id, article_2_id]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_evidence_must_be_inside_reviewed_sections(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    payload["required_zone_article_numbers"] = ["2"]
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    article_2_id = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("U")
        & structure.sections["article_number_raw"].eq("2"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id, article_2_id]
    with pytest.raises(BessZoningPrecheckError, match="outside reviewed sections"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_review_cannot_claim_another_chapter_section`

**Purpose:** Regression invariant: review cannot claim another chapter section. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_review_cannot_claim_another_chapter_section(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="another chapter")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
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
| In-memory mutation | `payload["chapters"][0]["reviewed_section_ids"] += (n_article,)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_review_cannot_claim_another_chapter_section(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    n_article = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (n_article,)
    with pytest.raises(BessZoningPrecheckError, match="another chapter"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_general_section_review_is_explicit_and_valid`

**Purpose:** Regression invariant: general section review is explicit and valid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_general_section_review_is_explicit_and_valid(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert general_id in reviewed`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `result.chapter_policy.set_index` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `payload["chapters"][0]["reviewed_section_ids"] += (general_id,)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_general_section_review_is_explicit_and_valid(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    general_id = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL"), "section_id"
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (general_id,)
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    reviewed = result.chapter_policy.set_index("resolved_zone_chapter_label").loc[
        "U", "reviewed_section_ids"
    ]
    assert general_id in reviewed
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_same_general_occurrence_may_be_scoped_to_different_chapters`

**Purpose:** Regression invariant: same general occurrence may be scoped to different chapters. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_same_general_occurrence_may_be_scoped_to_different_chapters(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(scoped["resolved_zone_chapter_label"]) == {"U", "N"}`
  - `assert len(scoped) == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_regulation_section_page_fragments(<br>            index, zones, relations, config, structure<br>        )<br>        .set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_regulation_section_page_fragments` | `landscout.stages.structure_planning_regulation.planning_regulation_section_page_fragments` |
| `fragment["raw_text"].index` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(excerpt.encode()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `excerpt.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `result.evidence_catalog["section_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.evidence_catalog["excerpt_start"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(excerpt.encode()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `chapter["reviewed_section_ids"] = (<br>            *chapter["reviewed_section_ids"],<br>            general["section_id"],<br>        )`<br>`chapter["evidence"] = (<br>            *chapter["evidence"],<br>            {**base, "evidence_id": evidence_id},<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_same_general_occurrence_may_be_scoped_to_different_chapters(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    general = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL")
    ].iloc[0]
    fragment = (
        planning_regulation_section_page_fragments(
            index, zones, relations, config, structure
        )
        .set_index(["section_id", "page_number"])
        .loc[(general["section_id"], 1)]
    )
    excerpt = "General factual text."
    start = fragment["raw_text"].index(excerpt)
    base = {
        "section_id": general["section_id"],
        "page_number": 1,
        "evidence_kind": "TECHNICAL_EQUIPMENT_RULE",
        "evidence_direction": "CONTEXT_ONLY",
        "exact_raw_excerpt": excerpt,
        "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
        "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],
        "excerpt_start": start,
        "excerpt_end": start + len(excerpt),
        "source_rule_id": "RULE-GENERAL-CONTEXT",
        "source_rule_excerpt": excerpt,
        "source_rule_sha256": sha256(excerpt.encode()).hexdigest(),
        "source_rule_start": start,
        "source_rule_end": start + len(excerpt),
        "interpretation_note": "The same factual GENERAL occurrence is chapter-scoped.",
    }
    payload = _payload(policy)
    for chapter, evidence_id in zip(
        payload["chapters"],
        ("E-U-GENERAL-CONTEXT", "E-N-GENERAL-CONTEXT"),
        strict=True,
    ):
        chapter["reviewed_section_ids"] = (
            *chapter["reviewed_section_ids"],
            general["section_id"],
        )
        chapter["evidence"] = (
            *chapter["evidence"],
            {**base, "evidence_id": evidence_id},
        )
    scoped_policy = BessZoningPolicyConfig.model_validate(payload)
    result = interpret_bess_zoning(
        index,
        structure,
        config,
        zones,
        relations,
        parcels,
        planning_document,
        scoped_policy,
    )
    scoped = result.evidence_catalog.loc[
        result.evidence_catalog["section_id"].eq(general["section_id"])
        & result.evidence_catalog["excerpt_start"].eq(start)
    ]
    assert set(scoped["resolved_zone_chapter_label"]) == {"U", "N"}
    assert len(scoped) == 2
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_section_page_occurrence_is_auditable`

**Purpose:** Regression invariant: exact section page occurrence is auditable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>            row["section_page_fragment_sha256"]<br>            == fragment["section_page_fragment_sha256"]<br>        )`
  - `assert (<br>            fragment["raw_text"][row["excerpt_start"] : row["excerpt_end"]]<br>            == row["exact_raw_excerpt"]<br>        )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `planning_regulation_section_page_fragments(<br>        index, zones, relations, config, structure<br>    ).set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_regulation_section_page_fragments` | `landscout.stages.structure_planning_regulation.planning_regulation_section_page_fragments` |
| `valid_result.evidence_catalog.to_dict` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.to_dict` |

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
def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    for row in valid_result.evidence_catalog.to_dict("records"):
        fragment = fragments.loc[(row["section_id"], row["page_number"])]
        assert (
            row["section_page_fragment_sha256"]
            == fragment["section_page_fragment_sha256"]
        )
        assert (
            fragment["raw_text"][row["excerpt_start"] : row["excerpt_end"]]
            == row["exact_raw_excerpt"]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_repeated_excerpt_occurrence_is_bound_to_policy`

**Purpose:** Regression invariant: repeated excerpt occurrence is bound to policy. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_repeated_excerpt_occurrence_is_bound_to_policy(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from rebuilt")`
- Exact assertions:
  - `assert second > first`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.evidence_catalog["evidence_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_regulation_section_page_fragments(<br>        index, zones, relations, config, structure<br>    ).set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `planning_regulation_section_page_fragments` | `landscout.stages.structure_planning_regulation.planning_regulation_section_page_fragments` |
| `raw.index` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_result.evidence_catalog.copy` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.copy` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `catalog.loc[row_index, "excerpt_start"] = second`<br>`catalog.loc[row_index, "excerpt_end"] = second + len(row["exact_raw_excerpt"])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_repeated_excerpt_occurrence_is_bound_to_policy(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    row_index = valid_result.evidence_catalog.index[
        valid_result.evidence_catalog["evidence_id"].eq("E-U-POSITIVE")
    ][0]
    row = valid_result.evidence_catalog.loc[row_index]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    raw = fragments.loc[(row["section_id"], row["page_number"]), "raw_text"]
    first = raw.index(row["exact_raw_excerpt"])
    second = raw.index(row["exact_raw_excerpt"], first + 1)
    assert second > first

    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[row_index, "excerpt_start"] = second
    catalog.loc[row_index, "excerpt_end"] = second + len(row["exact_raw_excerpt"])
    coordinated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, coordinated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_occurrence_identity_is_rejected`

**Purpose:** Regression invariant: wrong occurrence identity is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_occurrence_identity_is_rejected(inputs, mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["page", "fragment_hash", "start", "end"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="fragment\|offset")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
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
| In-memory mutation | `related["page_number"] = 1`<br>`related["section_page_fragment_sha256"] = "f" * 64`<br>`evidence["excerpt_start"] += 1`<br>`evidence["excerpt_end"] -= 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_wrong_occurrence_identity_is_rejected(inputs, mutation: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    evidence = payload["chapters"][0]["evidence"][0]
    if mutation == "page":
        for related in payload["chapters"][0]["evidence"]:
            related["page_number"] = 1
    elif mutation == "fragment_hash":
        for related in payload["chapters"][0]["evidence"]:
            related["section_page_fragment_sha256"] = "f" * 64
    elif mutation == "start":
        evidence["excerpt_start"] += 1
    else:
        evidence["excerpt_end"] -= 1
    with pytest.raises(BessZoningPrecheckError, match="fragment|offset"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_and_alias_mappings_are_inherited_without_prefix_logic`

**Purpose:** Regression invariant: exact and alias mappings are inherited without prefix logic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(
    valid_result,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policies.loc["U", "mapping_status"] == "EXACT"`
  - `assert policies.loc["Ua", "mapping_status"] == "CONFIG_ALIAS"`
  - `assert policies.loc["Ua", "resolved_zone_chapter_label"] == "U"`
  - `assert (<br>        policies.loc["Ua", "zoning_precheck_status"]<br>        == policies.loc["U", "zoning_precheck_status"]<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.source_zone_policy.set_index` | `tests.unit.test_interpret_bess_zoning.valid_result.source_zone_policy.set_index` |

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
def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(
    valid_result,
) -> None:
    policies = valid_result.source_zone_policy.set_index("source_zone_label_raw")
    assert policies.loc["U", "mapping_status"] == "EXACT"
    assert policies.loc["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert policies.loc["Ua", "resolved_zone_chapter_label"] == "U"
    assert (
        policies.loc["Ua", "zoning_precheck_status"]
        == policies.loc["U", "zoning_precheck_status"]
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unmapped_dominant_zone_is_rejected`

**Purpose:** Regression invariant: unmapped dominant zone is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="Factual regulation structure")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.zone_mapping.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `mapping["source_zone_label_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_structure_with_hashes` | `landscout.stages.structure_planning_regulation._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `policy.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy.source_lock.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_structure_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `mapping.loc[<br>        mapping["source_zone_label_raw"].eq("U"),<br>        [<br>            "resolved_zone_chapter_label",<br>            "matched_section_id",<br>        ],<br>    ] = None`<br>`mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_status"] = "UNMAPPED"`<br>`mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_method"] = "NONE"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    mapping = structure.zone_mapping.copy()
    mapping.loc[
        mapping["source_zone_label_raw"].eq("U"),
        [
            "resolved_zone_chapter_label",
            "matched_section_id",
        ],
    ] = None
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_status"] = "UNMAPPED"
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_method"] = "NONE"
    mutated = _structure_with_hashes(replace(structure, zone_mapping=mapping))
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        mutated.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            mutated,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_link_table_exactly_reproduces_routes_and_reverse_links`

**Purpose:** Regression invariant: link table exactly reproduces routes and reverse links. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_link_table_exactly_reproduces_routes_and_reverse_links(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert actual == expected`
  - `assert catalog.loc["E-U-POSITIVE", "linked_route_ids"] == ("ROUTE-U-CONDITIONAL",)`
  - `assert catalog.loc["E-U-POSITIVE", "linked_route_roles"] == ("POSITIVE",)`
  - `assert bool(catalog["decision_linked"].all())`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.evidence_route_links.itertuples` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_route_links.itertuples` |
| `valid_result.evidence_catalog.set_index` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.set_index` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog["decision_linked"].all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_link_table_exactly_reproduces_routes_and_reverse_links(valid_result) -> None:
    expected = {
        ("ROUTE-U-CONDITIONAL", "E-U-POSITIVE", "POSITIVE"),
        ("ROUTE-U-CONDITIONAL", "E-U-CONDITION", "CONDITION"),
        ("ROUTE-N-DIFFICULT", "E-N-1", "DIFFICULTY"),
    }
    actual = {
        (row.route_id, row.evidence_id, row.route_role)
        for row in valid_result.evidence_route_links.itertuples(index=False)
    }
    assert actual == expected
    catalog = valid_result.evidence_catalog.set_index("evidence_id")
    assert catalog.loc["E-U-POSITIVE", "linked_route_ids"] == ("ROUTE-U-CONDITIONAL",)
    assert catalog.loc["E-U-POSITIVE", "linked_route_roles"] == ("POSITIVE",)
    assert bool(catalog["decision_linked"].all())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_context_evidence_is_separate_from_decision_outputs`

**Purpose:** Regression invariant: context evidence is separate from decision outputs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_context_evidence_is_separate_from_decision_outputs(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert context["linked_route_ids"] == ()`
  - `assert context["linked_route_roles"] == ()`
  - `assert not bool(context["decision_linked"])`
  - `assert chapter["evidence_ids"] == ("E-U-POSITIVE", "E-U-CONDITION")`
  - `assert chapter["decision_evidence_ids"] == ("E-U-POSITIVE",)`
  - `assert chapter["context_evidence_ids"] == ("E-U-CONDITION",)`
  - `assert source["decision_evidence_ids"] == ("E-U-POSITIVE",)`
  - `assert source["context_evidence_ids"] == ("E-U-CONDITION",)`
  - `assert relation["decision_evidence_ids"] == ("E-U-POSITIVE",)`
  - `assert relation["context_evidence_ids"] == ("E-U-CONDITION",)`
  - `assert parcel["zoning_precheck_evidence_ids"] == ("E-U-POSITIVE",)`
  - `assert parcel["zoning_precheck_context_evidence_ids"] == ("E-U-CONDITION",)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_policy_with_context_only_evidence` | `tests.unit.test_interpret_bess_zoning._policy_with_context_only_evidence` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `result.evidence_catalog.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.chapter_policy.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.source_zone_policy.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcel_zone_interpretations["resolved_zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["parcel_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_context_evidence_is_separate_from_decision_outputs(inputs) -> None:
    *sources, policy = inputs
    context_policy = _policy_with_context_only_evidence(policy)
    result = interpret_bess_zoning(*sources, context_policy)
    catalog = result.evidence_catalog.set_index("evidence_id")
    context = catalog.loc["E-U-CONDITION"]
    assert context["linked_route_ids"] == ()
    assert context["linked_route_roles"] == ()
    assert not bool(context["decision_linked"])
    chapter = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
    assert chapter["evidence_ids"] == ("E-U-POSITIVE", "E-U-CONDITION")
    assert chapter["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert chapter["context_evidence_ids"] == ("E-U-CONDITION",)
    source = result.source_zone_policy.set_index("source_zone_label_raw").loc["U"]
    assert source["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert source["context_evidence_ids"] == ("E-U-CONDITION",)
    relation = result.parcel_zone_interpretations.loc[
        result.parcel_zone_interpretations["resolved_zone_chapter_label"].eq("U")
    ].iloc[0]
    assert relation["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert relation["context_evidence_ids"] == ("E-U-CONDITION",)
    parcel = result.parcels.loc[result.parcels["parcel_id"].eq("P-1")].iloc[0]
    assert parcel["zoning_precheck_evidence_ids"] == ("E-U-POSITIVE",)
    assert parcel["zoning_precheck_context_evidence_ids"] == ("E-U-CONDITION",)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_aggregation_preserves_conflicts_and_touch_only`

**Purpose:** Regression invariant: parcel aggregation preserves conflicts and touch only. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_aggregation_preserves_conflicts_and_touch_only(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcels.loc["P-1", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"`
  - `assert parcels.loc["P-1", "positive_area_zone_count"] == 1`
  - `assert parcels.loc["P-2", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"`
  - `assert parcels.loc["P-2", "positive_area_zone_count"] == 2`
  - `assert parcels.loc["P-2", "distinct_zone_status_count"] == 1`
  - `assert parcels.loc["P-3", "zoning_precheck_status"] == "MIXED_REVIEW_REQUIRED"`
  - `assert parcels.loc["P-3", "dominant_zone_precheck_status"] == "CONDITIONAL_REVIEW"`
  - `assert parcels.loc["P-3", "non_dominant_different_status_count"] == 1`
  - `assert parcels.loc["P-4", "zoning_precheck_status"] == "UNKNOWN"`
  - `assert parcels.loc["P-4", "positive_area_zone_count"] == 0`
  - `assert parcels.loc["P-4", "touch_only_zone_count"] == 1`
  - `assert pd.isna(parcels.loc["P-4", "dominant_zone_precheck_status"])`
  - `assert valid_result.touch_only_relation_count == 1`
  - `assert "P-4" not in set(valid_result.parcel_zone_interpretations["parcel_id"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.parcels.set_index` | `tests.unit.test_interpret_bess_zoning.valid_result.parcels.set_index` |
| `pd.isna` | `pandas.isna` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_parcel_aggregation_preserves_conflicts_and_touch_only(valid_result) -> None:
    parcels = valid_result.parcels.set_index("parcel_id")
    assert parcels.loc["P-1", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-1", "positive_area_zone_count"] == 1
    assert parcels.loc["P-2", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-2", "positive_area_zone_count"] == 2
    assert parcels.loc["P-2", "distinct_zone_status_count"] == 1
    assert parcels.loc["P-3", "zoning_precheck_status"] == "MIXED_REVIEW_REQUIRED"
    assert parcels.loc["P-3", "dominant_zone_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-3", "non_dominant_different_status_count"] == 1
    assert parcels.loc["P-4", "zoning_precheck_status"] == "UNKNOWN"
    assert parcels.loc["P-4", "positive_area_zone_count"] == 0
    assert parcels.loc["P-4", "touch_only_zone_count"] == 1
    assert pd.isna(parcels.loc["P-4", "dominant_zone_precheck_status"])
    assert valid_result.touch_only_relation_count == 1
    assert "P-4" not in set(valid_result.parcel_zone_interpretations["parcel_id"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved`

**Purpose:** Regression invariant: prior parcel fields geometry order index and crs are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved(
    inputs, valid_result
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert valid_result.parcels.index.equals(original.index)`
  - `assert valid_result.parcels.crs == original.crs`
  - `assert valid_result.parcels["planning_surface_relation_count"].equals(<br>        original["planning_surface_relation_count"]<br>    )`
  - `assert (<br>        valid_result.parcels["non_zoning_planning_features_interpreted"].eq(False).all()<br>    )`
  - `assert valid_result.parcels["zoning_precheck_requires_formal_review"].eq(True).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `valid_result.parcels.index.equals` | `tests.unit.test_interpret_bess_zoning.valid_result.parcels.index.equals` |
| `valid_result.parcels["planning_surface_relation_count"].equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_result.parcels["non_zoning_planning_features_interpreted"].eq(False).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_result.parcels["non_zoning_planning_features_interpreted"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_result.parcels["zoning_precheck_requires_formal_review"].eq(True).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_result.parcels["zoning_precheck_requires_formal_review"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved(
    inputs, valid_result
) -> None:
    original = inputs[5]
    prior = valid_result.parcels.loc[:, original.columns]
    assert_geodataframe_equal(prior, original)
    assert valid_result.parcels.index.equals(original.index)
    assert valid_result.parcels.crs == original.crs
    assert valid_result.parcels["planning_surface_relation_count"].equals(
        original["planning_surface_relation_count"]
    )
    assert (
        valid_result.parcels["non_zoning_planning_features_interpreted"].eq(False).all()
    )
    assert valid_result.parcels["zoning_precheck_requires_formal_review"].eq(True).all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inputs_are_not_mutated`

**Purpose:** Regression invariant: inputs are not mutated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inputs_are_not_mutated(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `zones.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

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
def test_inputs_are_not_mutated(inputs) -> None:
    _, structure, _, zones, relations, parcels, _, _ = inputs
    zone_snapshot = zones.copy(deep=True)
    relation_snapshot = relations.copy(deep=True)
    parcel_snapshot = parcels.copy(deep=True)
    section_snapshot = structure.sections.copy(deep=True)
    interpret_bess_zoning(*inputs)
    pd.testing.assert_frame_equal(zones, zone_snapshot)
    pd.testing.assert_frame_equal(relations, relation_snapshot)
    assert_geodataframe_equal(parcels, parcel_snapshot)
    pd.testing.assert_frame_equal(structure.sections, section_snapshot)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_change_after_result_creation_is_rejected`

**Purpose:** Regression invariant: policy change after result creation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="policy_config_sha256")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `payload["chapters"][0]["rationale"] = "Changed checked-in rationale."` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["rationale"] = "Changed checked-in rationale."
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="policy_config_sha256"):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_evidence_change_after_result_creation_is_rejected`

**Purpose:** Regression invariant: evidence change after result creation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_evidence_change_after_result_creation_is_rejected(
    inputs, valid_result
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_interpret_bess_zoning._payload` |
| `sha256(excerpt.encode()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `excerpt.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_zoning_precheck` | `landscout.stages.interpret_bess_zoning.validate_bess_zoning_precheck` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(excerpt.encode()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `evidence["exact_raw_excerpt"] = excerpt`<br>`evidence["excerpt_sha256"] = sha256(excerpt.encode()).hexdigest()`<br>`evidence["excerpt_start"] += len("Technical ")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_evidence_change_after_result_creation_is_rejected(
    inputs, valid_result
) -> None:
    payload = _payload(inputs[-1])
    excerpt = "equipment is permitted"
    evidence = payload["chapters"][0]["evidence"][0]
    evidence["exact_raw_excerpt"] = excerpt
    evidence["excerpt_sha256"] = sha256(excerpt.encode()).hexdigest()
    evidence["excerpt_start"] += len("Technical ")
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zoning_relation_and_zone_mapping_changes_are_rejected`

**Purpose:** Regression invariant: zoning relation and zone mapping changes are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_zoning_relation_and_zone_mapping_changes_are_rejected(
    inputs, valid_result
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="Factual regulation structure")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `changed_relations.loc[0, "intersection_area_m2"] = 99.0`<br>`changed_relations.loc[0, "parcel_share_pct"] = 99.0`<br>`changed_relations.loc[0, "zone_share_pct"] = 9.9` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_zoning_relation_and_zone_mapping_changes_are_rejected(
    inputs, valid_result
) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_relations = relations.copy()
    changed_relations.loc[0, "intersection_area_m2"] = 99.0
    changed_relations.loc[0, "parcel_share_pct"] = 99.0
    changed_relations.loc[0, "zone_share_pct"] = 9.9
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        validate_bess_zoning_precheck(
            index,
            structure,
            config,
            zones,
            changed_relations,
            parcels,
            planning_document,
            policy,
            valid_result,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_structure_config_and_hierarchy_changes_are_rejected`

**Purpose:** Regression invariant: structure config and hierarchy changes are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="Factual regulation structure")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `structure.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `changed_sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `article.idxmax` | `unresolved local/third-party receiver; no ownership inferred` |
| `_structure_with_hashes` | `landscout.stages.structure_planning_regulation._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `policy.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy.source_lock.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_structure_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `changed_sections.loc[article.idxmax(), "parent_section_id"] = "SECTION-UNKNOWN"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_config = config.model_copy(update={"structure_profile": "changed"})
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            structure,
            changed_config,
            zones,
            relations,
            parcels,
            planning_document,
            policy,
        )
    changed_sections = structure.sections.copy(deep=True)
    article = changed_sections["section_type"].eq("ARTICLE")
    changed_sections.loc[article.idxmax(), "parent_section_id"] = "SECTION-UNKNOWN"
    changed_structure = _structure_with_hashes(
        replace(structure, sections=changed_sections)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_source_complete_validator_is_invoked`

**Purpose:** Regression invariant: public source complete validator is invoked. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_source_complete_validator_is_invoked(inputs, monkeypatch) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `monkeypatch` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert calls >= 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_public_source_complete_validator_is_invoked(inputs, monkeypatch) -> None:
    calls = 0
    original = interpret_module.validate_planning_regulation_structure_with_fragments

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(
        interpret_module,
        "validate_planning_regulation_structure_with_fragments",
        counted,
    )
    interpret_bess_zoning(*inputs)
    assert calls >= 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_source_complete_validator_is_invoked.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def counted(*args, **kwargs):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `None` | `variadic` |
| `**kwargs` | variadic keyword | `None` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original(*args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original` | `unresolved local/third-party receiver; no ownership inferred` |

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
def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_precheck_build_performs_one_zoning_source_complete_validation`

**Purpose:** Regression invariant: one precheck build performs one zoning source complete validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_one_precheck_build_performs_one_zoning_source_complete_validation(
    inputs,
    monkeypatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `monkeypatch` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert calls == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_one_precheck_build_performs_one_zoning_source_complete_validation(
    inputs,
    monkeypatch,
) -> None:
    calls = 0

    def counted(*args) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        counted,
    )

    interpret_bess_zoning(*inputs)

    assert calls == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_precheck_build_performs_one_zoning_source_complete_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def counted(*args) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `None` | `variadic` |

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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def counted(*args) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_physical_zoning_fails_before_policy_interpretation`

**Purpose:** Regression invariant: invalid physical zoning fails before policy interpretation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_physical_zoning_fails_before_policy_interpretation(
    inputs,
    monkeypatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `monkeypatch` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="physical source invalid")`
- Exact assertions:
  - `assert policy_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
def test_invalid_physical_zoning_fails_before_policy_interpretation(
    inputs,
    monkeypatch,
) -> None:
    policy_calls = 0

    def invalid_source(*args) -> None:
        raise interpret_module.PlanningZoningError("physical source invalid")

    def counted_policy(*args):
        nonlocal policy_calls
        policy_calls += 1
        return inputs[-1]

    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        invalid_source,
    )
    monkeypatch.setattr(interpret_module, "_resolved_policy", counted_policy)

    with pytest.raises(BessZoningPrecheckError, match="physical source invalid"):
        interpret_bess_zoning(*inputs)

    assert policy_calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_physical_zoning_fails_before_policy_interpretation.invalid_source`

**Purpose:** Implements `invalid source` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def invalid_source(*args) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `None` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `interpret_module.PlanningZoningError("physical source invalid")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `interpret_module.PlanningZoningError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def invalid_source(*args) -> None:
        raise interpret_module.PlanningZoningError("physical source invalid")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_physical_zoning_fails_before_policy_interpretation.counted_policy`

**Purpose:** Implements `counted policy` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def counted_policy(*args):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `None` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `inputs[-1]`
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def counted_policy(*args):
        nonlocal policy_calls
        policy_calls += 1
        return inputs[-1]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_build_result_performs_one_factual_structure_rebuild`

**Purpose:** Regression invariant: one build result performs one factual structure rebuild. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_one_build_result_performs_one_factual_structure_rebuild(
    inputs, monkeypatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `monkeypatch` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert calls == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `interpret_module._build_result` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_one_build_result_performs_one_factual_structure_rebuild(
    inputs, monkeypatch
) -> None:
    calls = 0
    original = interpret_module.validate_planning_regulation_structure_with_fragments

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(
        interpret_module,
        "validate_planning_regulation_structure_with_fragments",
        counted,
    )
    interpret_module._build_result(*inputs[:6], inputs[-1])
    assert calls == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_build_result_performs_one_factual_structure_rebuild.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

**Exact signature**

```python
def counted(*args, **kwargs):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `None` | `variadic` |
| `**kwargs` | variadic keyword | `None` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original(*args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original` | `unresolved local/third-party receiver; no ownership inferred` |

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
def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_area_denominators_are_required`

**Purpose:** Regression invariant: relation area denominators are required. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    ["parcel_metric_area_m2", "zone_area_m2"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `relations.drop` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `relations.drop(columns=column)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            relations.drop(columns=column),
            parcels,
            planning_document,
            policy,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_percentages_must_match_denominators`

**Purpose:** Regression invariant: relation percentages must match denominators. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    ["parcel_share_pct", "zone_share_pct"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
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
| In-memory mutation | `changed.loc[0, column] += 1.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed = relations.copy(deep=True)
    changed.loc[0, column] += 1.0
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            changed,
            parcels,
            planning_document,
            policy,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_factual_zone_mapping_counts_are_recomputed`

**Purpose:** Regression invariant: factual zone mapping counts are recomputed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="Factual regulation structure")`
  - `pytest.raises(BessZoningPrecheckError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.zone_mapping.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_structure_with_hashes` | `landscout.stages.structure_planning_regulation._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `policy.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy.source_lock.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `validate_bess_zoning_precheck` | `landscout.stages.interpret_bess_zoning.validate_bess_zoning_precheck` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_structure_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `changed_mapping.loc[0, "candidate_intersection_count"] += 1`<br>`changed_mapping.loc[0, "source_zone_label_raw"] = "CHANGED"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_mapping = structure.zone_mapping.copy(deep=True)
    changed_mapping.loc[0, "candidate_intersection_count"] += 1
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )
    changed_mapping = structure.zone_mapping.copy()
    changed_mapping.loc[0, "source_zone_label_raw"] = "CHANGED"
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
            valid_result,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_result_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated result mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.chapter_policy.copy` | `tests.unit.test_interpret_bess_zoning.valid_result.chapter_policy.copy` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `chapter.loc[0, "zoning_precheck_confidence"] = "HIGH"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
    chapter = valid_result.chapter_policy.copy(deep=True)
    chapter.loc[0, "zoning_precheck_confidence"] = "HIGH"
    mutated = _result_with_hashes(replace(valid_result, chapter_policy=chapter))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_evidence_catalog_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated evidence catalog mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_evidence_catalog_mutation_is_rejected(
    inputs, valid_result
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.evidence_catalog.copy` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.copy` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `catalog.loc[0, "interpretation_note"] = "Coordinated mutation."` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_evidence_catalog_mutation_is_rejected(
    inputs, valid_result
) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[0, "interpretation_note"] = "Coordinated mutation."
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_catalog_occurrence_duplicate_is_rejected`

**Purpose:** Regression invariant: coordinated catalog occurrence duplicate is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_catalog_occurrence_duplicate_is_rejected(
    inputs, valid_result
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessZoningPrecheckError,<br>        match="duplicate chapter-scoped evidence occurrence",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.evidence_catalog.copy` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.copy` |
| `catalog.loc[<br>        catalog.index[0], occurrence_columns<br>    ].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `catalog.loc[catalog.index[1], occurrence_columns] = catalog.loc[<br>        catalog.index[0], occurrence_columns<br>    ].to_numpy()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_catalog_occurrence_duplicate_is_rejected(
    inputs, valid_result
) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    occurrence_columns = [
        "resolved_zone_chapter_label",
        "section_id",
        "page_number",
        "section_page_fragment_sha256",
        "excerpt_start",
        "excerpt_end",
    ]
    catalog.loc[catalog.index[1], occurrence_columns] = catalog.loc[
        catalog.index[0], occurrence_columns
    ].to_numpy()
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(
        BessZoningPrecheckError,
        match="duplicate chapter-scoped evidence occurrence",
    ):
        _validate(inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_route_table_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated route table mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_route_table_mutation_is_rejected(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.route_assessments.copy` | `tests.unit.test_interpret_bess_zoning.valid_result.route_assessments.copy` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `routes.loc[0, "applicability_note"] = "Coordinated route mutation."` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_route_table_mutation_is_rejected(inputs, valid_result) -> None:
    routes = valid_result.route_assessments.copy(deep=True)
    routes.loc[0, "applicability_note"] = "Coordinated route mutation."
    mutated = _result_with_hashes(replace(valid_result, route_assessments=routes))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_evidence_route_link_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated evidence route link mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_evidence_route_link_mutation_is_rejected(
    inputs, valid_result
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.evidence_route_links.copy` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_route_links.copy` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `links.loc[0, "route_role"] = "BROKEN"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_evidence_route_link_mutation_is_rejected(
    inputs, valid_result
) -> None:
    links = valid_result.evidence_route_links.copy(deep=True)
    links.loc[0, "route_role"] = "BROKEN"
    mutated = _result_with_hashes(replace(valid_result, evidence_route_links=links))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_reverse_link_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated reverse link mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_reverse_link_mutation_is_rejected(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.evidence_catalog.copy` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.copy` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `catalog.at[0, "linked_route_roles"] = ("DIFFICULTY",)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_reverse_link_mutation_is_rejected(inputs, valid_result) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.at[0, "linked_route_roles"] = ("DIFFICULTY",)
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_evidence_route_link_hash_mutation_is_rejected`

**Purpose:** Regression invariant: evidence route link hash mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_evidence_route_link_hash_mutation_is_rejected(inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="differs from rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |

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
def test_evidence_route_link_hash_mutation_is_rejected(inputs, valid_result) -> None:
    mutated = replace(
        valid_result,
        evidence_route_links_content_sha256="f" * 64,
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_old_result_hash_schemas_are_rejected`

**Purpose:** Regression invariant: old result hash schemas are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_old_result_hash_schemas_are_rejected(
    inputs, valid_result, version: int
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("version", [1, 2, 3, 4])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |
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
def test_old_result_hash_schemas_are_rejected(
    inputs, valid_result, version: int
) -> None:
    with pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version"):
        _validate(inputs, replace(valid_result, result_hash_schema_version=version))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_identity_change_is_rejected`

**Purpose:** Regression invariant: relation identity change is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_identity_change_is_rejected(inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessZoningPrecheckError, match="Factual regulation structure")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | `changed.loc[0, "source_zone_id"] = "SRC-N"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relation_identity_change_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed = relations.copy()
    changed.loc[0, "source_zone_id"] = "SRC-N"
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            changed,
            parcels,
            planning_document,
            policy,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_readback_result_validates`

**Purpose:** Regression invariant: readback result validates. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_readback_result_validates(tmp_path: Path, inputs, valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `inputs` | positional-or-keyword | `None` | `required` |
| `valid_result` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not persisted.evidence_catalog.duplicated(occurrence_columns).any()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `valid_result.evidence_catalog.to_parquet` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_catalog.to_parquet` |
| `valid_result.route_assessments.to_parquet` | `tests.unit.test_interpret_bess_zoning.valid_result.route_assessments.to_parquet` |
| `valid_result.evidence_route_links.to_parquet` | `tests.unit.test_interpret_bess_zoning.valid_result.evidence_route_links.to_parquet` |
| `valid_result.chapter_policy.to_parquet` | `tests.unit.test_interpret_bess_zoning.valid_result.chapter_policy.to_parquet` |
| `valid_result.source_zone_policy.to_parquet` | `tests.unit.test_interpret_bess_zoning.valid_result.source_zone_policy.to_parquet` |
| `valid_result.parcel_zone_interpretations.to_parquet` | `tests.unit.test_interpret_bess_zoning.valid_result.parcel_zone_interpretations.to_parquet` |
| `valid_result.parcels.to_parquet` | `tests.unit.test_interpret_bess_zoning.valid_result.parcels.to_parquet` |
| `replace` | `dataclasses.replace` |
| `pd.read_parquet` | `pandas.read_parquet` |
| `gpd.read_parquet` | `geopandas.read_parquet` |
| `_validate` | `tests.unit.test_interpret_bess_zoning._validate` |
| `persisted.evidence_catalog.duplicated(occurrence_columns).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `persisted.evidence_catalog.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `pd.read_parquet`<br>`gpd.read_parquet` |
| Filesystem/archive write or publication | `valid_result.evidence_catalog.to_parquet`<br>`valid_result.route_assessments.to_parquet`<br>`valid_result.evidence_route_links.to_parquet`<br>`valid_result.chapter_policy.to_parquet`<br>`valid_result.source_zone_policy.to_parquet`<br>`valid_result.parcel_zone_interpretations.to_parquet`<br>`valid_result.parcels.to_parquet` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_readback_result_validates(tmp_path: Path, inputs, valid_result) -> None:
    chapter_path = tmp_path / "chapter.parquet"
    evidence_path = tmp_path / "evidence.parquet"
    route_path = tmp_path / "routes.parquet"
    link_path = tmp_path / "links.parquet"
    source_path = tmp_path / "source.parquet"
    relation_path = tmp_path / "relations.parquet"
    parcel_path = tmp_path / "parcels.parquet"
    valid_result.evidence_catalog.to_parquet(evidence_path, index=False)
    valid_result.route_assessments.to_parquet(route_path, index=False)
    valid_result.evidence_route_links.to_parquet(link_path, index=False)
    valid_result.chapter_policy.to_parquet(chapter_path, index=False)
    valid_result.source_zone_policy.to_parquet(source_path, index=False)
    valid_result.parcel_zone_interpretations.to_parquet(relation_path, index=False)
    valid_result.parcels.to_parquet(parcel_path)
    persisted = replace(
        valid_result,
        evidence_catalog=pd.read_parquet(evidence_path),
        route_assessments=pd.read_parquet(route_path),
        evidence_route_links=pd.read_parquet(link_path),
        chapter_policy=pd.read_parquet(chapter_path),
        source_zone_policy=pd.read_parquet(source_path),
        parcel_zone_interpretations=pd.read_parquet(relation_path),
        parcels=gpd.read_parquet(parcel_path),
    )
    _validate(inputs, persisted)
    occurrence_columns = [
        "resolved_zone_chapter_label",
        "section_id",
        "page_number",
        "section_page_fragment_sha256",
        "excerpt_start",
        "excerpt_end",
    ]
    assert not persisted.evidence_catalog.duplicated(occurrence_columns).any()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_yaml_roundtrip_is_strict`

**Purpose:** Regression invariant: policy yaml roundtrip is strict. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_yaml_roundtrip_is_strict(tmp_path: Path, inputs) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `inputs` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert load_bess_zoning_policy_config(path) == policy`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |
| `policy.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_yaml_roundtrip_is_strict(tmp_path: Path, inputs) -> None:
    policy = inputs[-1]
    path = tmp_path / "policy.yaml"
    import yaml  # type: ignore[import-untyped]

    path.write_text(
        yaml.safe_dump(
            policy.model_dump(mode="json"),
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    assert load_bess_zoning_policy_config(path) == policy
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **79**.
- Pytest fixtures (decorator-proven): **2**.

### Fixtures

- `inputs` — decorators: `pytest.fixture`.
- `valid_result` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_package_exports_precheck_api` | none | none | 1 | Proves package exports precheck api using the exact source reproduced in section 7. |
| `test_valid_locked_policy_builds_complete_outputs` | none | none | 23 | Proves valid locked policy builds complete outputs using the exact source reproduced in section 7. |
| `test_source_lock_mismatch_is_rejected` | pytest.mark.parametrize(<br>    "field",<br>    [<br>        "document_id",<br>        "archive_sha256",<br>        "pdf_sha256",<br>        "index_content_sha256",<br>        "structure_result_content_sha256",<br>        "structure_profile",<br>    ],<br>) | pytest.raises(BessZoningPrecheckError, match="differs from factual source") | 0 | Proves source lock mismatch is rejected using the exact source reproduced in section 7. |
| `test_missing_and_extra_chapter_are_rejected` | none | pytest.raises(BessZoningPrecheckError, match="completeness differs"); pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA") | 0 | Proves missing and extra chapter are rejected using the exact source reproduced in section 7. |
| `test_regulation_zone_chapter_labels_and_ids_must_be_unique` | none | pytest.raises(BessZoningPrecheckError, match="labels must be unique"); pytest.raises(BessZoningPrecheckError, match="labels must be unique"); pytest.raises(BessZoningPrecheckError, match="section IDs must be unique") | 1 | Proves regulation zone chapter labels and ids must be unique using the exact source reproduced in section 7. |
| `test_source_complete_validator_rejects_later_duplicate_chapter` | none | pytest.raises(BessZoningPrecheckError) | 0 | Proves source complete validator rejects later duplicate chapter using the exact source reproduced in section 7. |
| `test_duplicate_chapter_and_evidence_id_are_rejected` | none | pytest.raises(ValueError, match="chapter policy labels must be unique"); pytest.raises(ValueError, match="evidence IDs must be globally unique") | 0 | Proves duplicate chapter and evidence id are rejected using the exact source reproduced in section 7. |
| `test_one_excerpt_cannot_be_reused_with_contradictory_directions` | none | pytest.raises(ValueError, match="chapter-scoped evidence occurrence") | 0 | Proves one excerpt cannot be reused with contradictory directions using the exact source reproduced in section 7. |
| `test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected` | none | pytest.raises(ValueError, match="chapter-scoped evidence occurrence") | 0 | Proves duplicate chapter scoped occurrence in one route is rejected using the exact source reproduced in section 7. |
| `test_duplicate_occurrence_in_different_compatible_routes_is_rejected` | none | pytest.raises(ValueError, match="chapter-scoped evidence occurrence") | 0 | Proves duplicate occurrence in different compatible routes is rejected using the exact source reproduced in section 7. |
| `test_forbidden_or_invalid_final_status_is_rejected` | pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"]) | pytest.raises(ValueError) | 0 | Proves forbidden or invalid final status is rejected using the exact source reproduced in section 7. |
| `test_invalid_confidence_and_unknown_field_are_rejected` | none | pytest.raises(ValueError); pytest.raises(ValueError) | 0 | Proves invalid confidence and unknown field are rejected using the exact source reproduced in section 7. |
| `test_duplicate_yaml_key_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="Duplicate YAML.*key") | 0 | Proves duplicate yaml key is rejected using the exact source reproduced in section 7. |
| `test_old_policy_schema_versions_are_rejected` | pytest.mark.parametrize("version", [1, 2, 3, 4]) | pytest.raises(ValueError, match="unsupported BESS zoning policy schema") | 0 | Proves old policy schema versions are rejected using the exact source reproduced in section 7. |
| `test_every_evidence_kind_has_an_explicit_direction_matrix` | none | pytest.raises(<br>                    ValueError,<br>                    match="kind and direction are incompatible",<br>                ) | 0 | Proves every evidence kind has an explicit direction matrix using the exact source reproduced in section 7. |
| `test_valid_exact_evidence_is_preserved` | none | none | 5 | Proves valid exact evidence is preserved using the exact source reproduced in section 7. |
| `test_source_rule_identity_and_containment_are_strict` | pytest.mark.parametrize("mutation", ["hash", "start", "end", "outside"]) | pytest.raises(ValueError, match="source rule SHA256"); pytest.raises(ValueError, match="inside its source rule"); pytest.raises(BessZoningPrecheckError, match="source-rule offsets") | 0 | Proves source rule identity and containment are strict using the exact source reproduced in section 7. |
| `test_same_rule_text_at_distinct_offsets_has_distinct_identity` | none | none | 1 | Proves same rule text at distinct offsets has distinct identity using the exact source reproduced in section 7. |
| `test_real_muret_source_rules_preserve_conditional_and_exception_frames` | none | none | 7 | Proves real muret source rules preserve conditional and exception frames using the exact source reproduced in section 7. |
| `test_real_muret_up_route_does_not_use_the_separate_icpe_condition` | none | none | 19 | Proves real muret up route does not use the separate icpe condition using the exact source reproduced in section 7. |
| `test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite` | none | none | 18 | Proves real muret aup route uses the general infrastructure prerequisite using the exact source reproduced in section 7. |
| `test_real_muret_up_and_aup_keep_icpe_applicability_as_context` | none | none | 4 | Proves real muret up and aup keep icpe applicability as context using the exact source reproduced in section 7. |
| `test_absent_excerpt_and_section_page_mismatch_are_rejected` | none | pytest.raises(BessZoningPrecheckError, match="offsets"); pytest.raises(BessZoningPrecheckError, match="section/page fragment") | 0 | Proves absent excerpt and section page mismatch are rejected using the exact source reproduced in section 7. |
| `test_excerpt_hash_and_length_are_rejected` | none | pytest.raises(ValueError, match="excerpt SHA256 differs"); pytest.raises(ValueError) | 0 | Proves excerpt hash and length are rejected using the exact source reproduced in section 7. |
| `test_declared_status_must_equal_derived_route_status` | pytest.mark.parametrize(<br>    "status", ["POTENTIALLY_COMPATIBLE", "LIKELY_DIFFICULT", "UNKNOWN"]<br>) | pytest.raises(ValueError, match="differs from coherent linked route") | 0 | Proves declared status must equal derived route status using the exact source reproduced in section 7. |
| `test_condition_alone_cannot_create_conditional_review` | none | pytest.raises(ValueError, match="coherent linked route") | 0 | Proves condition alone cannot create conditional review using the exact source reproduced in section 7. |
| `test_unrelated_positive_and_condition_do_not_create_conditional_review` | none | pytest.raises(ValueError, match="coherent\|linked route") | 0 | Proves unrelated positive and condition do not create conditional review using the exact source reproduced in section 7. |
| `test_unlinked_context_only_unknown_succeeds` | none | none | 1 | Proves unlinked context only unknown succeeds using the exact source reproduced in section 7. |
| `test_positive_condition_and_conflict_status_routes` | none | none | 2 | Proves positive condition and conflict status routes using the exact source reproduced in section 7. |
| `test_route_references_must_be_same_chapter_and_role_compatible` | none | pytest.raises(ValueError, match=message) | 0 | Proves route references must be same chapter and role compatible using the exact source reproduced in section 7. |
| `test_route_ids_are_globally_unique` | none | pytest.raises(ValueError, match="route IDs must be globally unique") | 0 | Proves route ids are globally unique using the exact source reproduced in section 7. |
| `test_unlinked_difficulty_evidence_is_rejected` | none | pytest.raises(ValueError, match="decision evidence must be linked") | 0 | Proves unlinked difficulty evidence is rejected using the exact source reproduced in section 7. |
| `test_unlinked_positive_and_condition_evidence_are_rejected` | none | pytest.raises(ValueError, match="decision evidence must be linked") | 0 | Proves unlinked positive and condition evidence are rejected using the exact source reproduced in section 7. |
| `test_context_only_evidence_must_be_unlinked` | none | pytest.raises(ValueError) | 1 | Proves context only evidence must be unlinked using the exact source reproduced in section 7. |
| `test_one_evidence_may_link_to_multiple_compatible_routes` | none | none | 2 | Proves one evidence may link to multiple compatible routes using the exact source reproduced in section 7. |
| `test_difficulty_and_positive_only_status_routes` | none | none | 2 | Proves difficulty and positive only status routes using the exact source reproduced in section 7. |
| `test_incomplete_review_requires_unknown_low` | none | pytest.raises(ValueError, match="incomplete review") | 1 | Proves incomplete review requires unknown low using the exact source reproduced in section 7. |
| `test_incomplete_review_persists_exact_missing_required_sections` | none | none | 4 | Proves incomplete review persists exact missing required sections using the exact source reproduced in section 7. |
| `test_unknown_is_accepted_when_evidence_is_insufficient` | none | none | 1 | Proves unknown is accepted when evidence is insufficient using the exact source reproduced in section 7. |
| `test_reviewed_sections_cover_required_articles` | none | pytest.raises(BessZoningPrecheckError, match="omits required reviewed") | 1 | Proves reviewed sections cover required articles using the exact source reproduced in section 7. |
| `test_every_configured_article_must_exist_once_in_every_chapter` | pytest.mark.parametrize("article_number", ["1", "2"]) | pytest.raises(BessZoningPrecheckError, match="exactly one.*article") | 0 | Proves every configured article must exist once in every chapter using the exact source reproduced in section 7. |
| `test_duplicate_configured_article_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="exactly one.*article") | 0 | Proves duplicate configured article is rejected using the exact source reproduced in section 7. |
| `test_configured_article_with_wrong_chapter_parent_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="exactly one.*article") | 0 | Proves configured article with wrong chapter parent is rejected using the exact source reproduced in section 7. |
| `test_evidence_must_be_inside_reviewed_sections` | none | pytest.raises(BessZoningPrecheckError, match="outside reviewed sections") | 0 | Proves evidence must be inside reviewed sections using the exact source reproduced in section 7. |
| `test_review_cannot_claim_another_chapter_section` | none | pytest.raises(BessZoningPrecheckError, match="another chapter") | 0 | Proves review cannot claim another chapter section using the exact source reproduced in section 7. |
| `test_general_section_review_is_explicit_and_valid` | none | none | 1 | Proves general section review is explicit and valid using the exact source reproduced in section 7. |
| `test_same_general_occurrence_may_be_scoped_to_different_chapters` | none | none | 2 | Proves same general occurrence may be scoped to different chapters using the exact source reproduced in section 7. |
| `test_exact_section_page_occurrence_is_auditable` | none | none | 2 | Proves exact section page occurrence is auditable using the exact source reproduced in section 7. |
| `test_repeated_excerpt_occurrence_is_bound_to_policy` | none | pytest.raises(BessZoningPrecheckError, match="differs from rebuilt") | 1 | Proves repeated excerpt occurrence is bound to policy using the exact source reproduced in section 7. |
| `test_wrong_occurrence_identity_is_rejected` | pytest.mark.parametrize("mutation", ["page", "fragment_hash", "start", "end"]) | pytest.raises(BessZoningPrecheckError, match="fragment\|offset") | 0 | Proves wrong occurrence identity is rejected using the exact source reproduced in section 7. |
| `test_exact_and_alias_mappings_are_inherited_without_prefix_logic` | none | none | 4 | Proves exact and alias mappings are inherited without prefix logic using the exact source reproduced in section 7. |
| `test_unmapped_dominant_zone_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="Factual regulation structure") | 0 | Proves unmapped dominant zone is rejected using the exact source reproduced in section 7. |
| `test_link_table_exactly_reproduces_routes_and_reverse_links` | none | none | 4 | Proves link table exactly reproduces routes and reverse links using the exact source reproduced in section 7. |
| `test_context_evidence_is_separate_from_decision_outputs` | none | none | 12 | Proves context evidence is separate from decision outputs using the exact source reproduced in section 7. |
| `test_parcel_aggregation_preserves_conflicts_and_touch_only` | none | none | 14 | Proves parcel aggregation preserves conflicts and touch only using the exact source reproduced in section 7. |
| `test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved` | none | none | 5 | Proves prior parcel fields geometry order index and crs are preserved using the exact source reproduced in section 7. |
| `test_inputs_are_not_mutated` | none | none | 0 | Proves inputs are not mutated using the exact source reproduced in section 7. |
| `test_policy_change_after_result_creation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="policy_config_sha256") | 0 | Proves policy change after result creation is rejected using the exact source reproduced in section 7. |
| `test_evidence_change_after_result_creation_is_rejected` | none | pytest.raises(BessZoningPrecheckError) | 0 | Proves evidence change after result creation is rejected using the exact source reproduced in section 7. |
| `test_zoning_relation_and_zone_mapping_changes_are_rejected` | none | pytest.raises(BessZoningPrecheckError, match="Factual regulation structure") | 0 | Proves zoning relation and zone mapping changes are rejected using the exact source reproduced in section 7. |
| `test_structure_config_and_hierarchy_changes_are_rejected` | none | pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"); pytest.raises(BessZoningPrecheckError, match="Factual regulation structure") | 0 | Proves structure config and hierarchy changes are rejected using the exact source reproduced in section 7. |
| `test_public_source_complete_validator_is_invoked` | none | none | 1 | Proves public source complete validator is invoked using the exact source reproduced in section 7. |
| `test_one_precheck_build_performs_one_zoning_source_complete_validation` | none | none | 1 | Proves one precheck build performs one zoning source complete validation using the exact source reproduced in section 7. |
| `test_invalid_physical_zoning_fails_before_policy_interpretation` | none | pytest.raises(BessZoningPrecheckError, match="physical source invalid") | 1 | Proves invalid physical zoning fails before policy interpretation using the exact source reproduced in section 7. |
| `test_one_build_result_performs_one_factual_structure_rebuild` | none | none | 1 | Proves one build result performs one factual structure rebuild using the exact source reproduced in section 7. |
| `test_relation_area_denominators_are_required` | pytest.mark.parametrize(<br>    "column",<br>    ["parcel_metric_area_m2", "zone_area_m2"],<br>) | pytest.raises(BessZoningPrecheckError) | 0 | Proves relation area denominators are required using the exact source reproduced in section 7. |
| `test_relation_percentages_must_match_denominators` | pytest.mark.parametrize(<br>    "column",<br>    ["parcel_share_pct", "zone_share_pct"],<br>) | pytest.raises(BessZoningPrecheckError) | 0 | Proves relation percentages must match denominators using the exact source reproduced in section 7. |
| `test_factual_zone_mapping_counts_are_recomputed` | none | pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"); pytest.raises(BessZoningPrecheckError) | 0 | Proves factual zone mapping counts are recomputed using the exact source reproduced in section 7. |
| `test_coordinated_result_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="differs from rebuilt") | 0 | Proves coordinated result mutation is rejected using the exact source reproduced in section 7. |
| `test_coordinated_evidence_catalog_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="differs from rebuilt") | 0 | Proves coordinated evidence catalog mutation is rejected using the exact source reproduced in section 7. |
| `test_coordinated_catalog_occurrence_duplicate_is_rejected` | none | pytest.raises(<br>        BessZoningPrecheckError,<br>        match="duplicate chapter-scoped evidence occurrence",<br>    ) | 0 | Proves coordinated catalog occurrence duplicate is rejected using the exact source reproduced in section 7. |
| `test_coordinated_route_table_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="differs from rebuilt") | 0 | Proves coordinated route table mutation is rejected using the exact source reproduced in section 7. |
| `test_coordinated_evidence_route_link_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="differs from rebuilt") | 0 | Proves coordinated evidence route link mutation is rejected using the exact source reproduced in section 7. |
| `test_coordinated_reverse_link_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="differs from rebuilt") | 0 | Proves coordinated reverse link mutation is rejected using the exact source reproduced in section 7. |
| `test_evidence_route_link_hash_mutation_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="differs from rebuilt") | 0 | Proves evidence route link hash mutation is rejected using the exact source reproduced in section 7. |
| `test_old_result_hash_schemas_are_rejected` | pytest.mark.parametrize("version", [1, 2, 3, 4]) | pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version") | 0 | Proves old result hash schemas are rejected using the exact source reproduced in section 7. |
| `test_relation_identity_change_is_rejected` | none | pytest.raises(BessZoningPrecheckError, match="Factual regulation structure") | 0 | Proves relation identity change is rejected using the exact source reproduced in section 7. |
| `test_readback_result_validates` | none | none | 1 | Proves readback result validates using the exact source reproduced in section 7. |
| `test_policy_yaml_roundtrip_is_strict` | none | none | 1 | Proves policy yaml roundtrip is strict using the exact source reproduced in section 7. |

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

import importlib
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import Polygon

interpret_module = importlib.import_module("landscout.stages.interpret_bess_zoning")

from landscout import stages
from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)
from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)
from landscout.stages.structure_planning_regulation import (
    _result_with_hashes as _structure_with_hashes,
)


def _index() -> PlanningRegulationIndex:
    raw_pages = (
        "ARTICLE 1 - GENERAL\nGeneral factual text.",
        (
            "ZONE U\nARTICLE U 1 - USES\nTechnical equipment is permitted only when "
            "formal review is required.\nTechnical equipment is permitted only when "
            "formal review is required.\nARTICLE U 2 - OTHER\nOther factual text."
        ),
        (
            "ZONE N\nARTICLE N 1 - USES\nBattery facilities are restricted.\n"
            "Technical equipment is permitted only when formal review is required.\n"
            "ARTICLE N 2 - OTHER\nOther factual text."
        ),
    )
    rows: list[dict[str, object]] = []
    for number, raw_text in enumerate(raw_pages, start=1):
        row: dict[str, object] = {
            "page_number": number,
            "extraction_status": "TEXT",
            "raw_text": raw_text,
            "normalized_search_text": _normalize_search_text(raw_text),
            "character_count": len(raw_text),
            "extraction_error": None,
            "page_content_sha256": "",
        }
        row["page_content_sha256"] = _page_content_sha256(row)
        rows.append(row)
    pages = pd.DataFrame(rows)
    index = PlanningRegulationIndex(
        document_id="doc-1",
        archive_sha256="a" * 64,
        regulation_filename="commune_reglement.pdf",
        source_selection_method="ZONING_NOMFIC",
        source_selection_sha256="b" * 64,
        pdf_relative_path="package/commune_reglement.pdf",
        pdf_size_bytes=100,
        pdf_sha256="c" * 64,
        extraction_library="pypdf",
        extraction_library_version="test-version",
        search_normalization_profile=SEARCH_NORMALIZATION_PROFILE,
        page_hash_schema_version=PAGE_HASH_SCHEMA_VERSION,
        index_hash_schema_version=INDEX_HASH_SCHEMA_VERSION,
        total_page_count=len(pages),
        pages_content_sha256=_pages_content_sha256(pages),
        index_content_sha256="d" * 64,
        pages=pages,
    )
    return replace(index, index_content_sha256=_index_content_sha256(index))


def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "planning_zone_id": ["ZONE-U", "ZONE-UA", "ZONE-N"],
            "source_zone_id": ["SRC-U", "SRC-UA", "SRC-N"],
            "zone_label_raw": ["U", "Ua", "N"],
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
            "source_layer": "ZONE",
        }
    )


def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
    rows = (
        ("P-1", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 100.0, 100.0),
        ("P-2", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-2", "ZONE-UA", "SRC-UA", "Ua", "AREA_OVERLAP", 40.0, 40.0),
        ("P-3", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-3", "ZONE-N", "SRC-N", "N", "AREA_OVERLAP", 40.0, 40.0),
        ("P-4", "ZONE-N", "SRC-N", "N", "TOUCH_ONLY", 0.0, 0.0),
    )
    return pd.DataFrame(
        [
            {
                "parcel_id": parcel_id,
                "planning_zone_id": planning_zone_id,
                "source_zone_id": source_zone_id,
                "zone_label_raw": label,
                "relation_type": relation_type,
                "intersection_area_m2": area,
                "parcel_share_pct": share,
                "zone_share_pct": area / 10.0,
                "source_document_id": index.document_id,
                "source_archive_sha256": index.archive_sha256,
                "source_layer": "ZONE",
                "parcel_metric_area_m2": 100.0,
                "zone_area_m2": 1000.0,
            }
            for (
                parcel_id,
                planning_zone_id,
                source_zone_id,
                label,
                relation_type,
                area,
                share,
            ) in rows
        ]
    )


def _structure_config(
    index: PlanningRegulationIndex,
) -> PlanningRegulationStructureConfig:
    return PlanningRegulationStructureConfig.model_validate(
        {
            "schema_version": 2,
            "structure_profile": "synthetic_v1",
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
            "zone_aliases": {"Ua": "U"},
            "topics": {"technical": ["technical equipment"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 20,
        }
    )


def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ["P-1", "P-2", "P-3", "P-4"],
            "dominant_planning_zone_id": ["ZONE-U", "ZONE-U", "ZONE-U", None],
            "planning_surface_relation_count": [0, 1, 2, 0],
            "prescription_surface_relation_count": [0, 1, 1, 0],
            "information_surface_relation_count": [0, 0, 1, 0],
            "planning_line_relation_count": [0, 0, 0, 0],
            "planning_point_relation_count": [0, 0, 0, 0],
            "planning_document_id": index.document_id,
            "planning_archive_sha256": index.archive_sha256,
            "planning_feature_document_id": index.document_id,
            "planning_feature_archive_sha256": index.archive_sha256,
            "prior_fact": ["one", "two", "three", "four"],
        },
        geometry=[
            Polygon([(x, 0), (x + 10, 0), (x + 10, 10), (x, 10), (x, 0)])
            for x in (0, 20, 40, 60)
        ],
        crs="EPSG:2154",
        index=pd.Index([10, 20, 30, 40], name="source_row"),
    )
    return frame


def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
    sections = structure.sections
    u_articles = sections.loc[
        sections["section_type"].eq("ARTICLE") & sections["zone_chapter_label"].eq("U")
    ]
    n_articles = sections.loc[
        sections["section_type"].eq("ARTICLE") & sections["zone_chapter_label"].eq("N")
    ]
    u_article = u_articles.loc[u_articles["article_number_raw"].eq("1")].iloc[0]
    n_article = n_articles.loc[n_articles["article_number_raw"].eq("1")].iloc[0]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    u_positive = "Technical equipment is permitted"
    u_condition = "only when formal review is required"
    n_excerpt = "Battery facilities are restricted."

    def evidence(
        evidence_id: str,
        section_id: str,
        page_number: int,
        kind: str,
        direction: str,
        excerpt: str,
        source_rule_id: str,
        source_rule: str,
        note: str,
    ) -> dict[str, object]:
        fragment = fragments.loc[(section_id, page_number)]
        raw = fragment["raw_text"]
        rule_start = raw.index(source_rule)
        start = raw.index(excerpt, rule_start, rule_start + len(source_rule))
        return {
            "evidence_id": evidence_id,
            "section_id": section_id,
            "page_number": page_number,
            "evidence_kind": kind,
            "evidence_direction": direction,
            "exact_raw_excerpt": excerpt,
            "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
            "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],
            "excerpt_start": start,
            "excerpt_end": start + len(excerpt),
            "source_rule_id": source_rule_id,
            "source_rule_excerpt": source_rule,
            "source_rule_sha256": sha256(source_rule.encode()).hexdigest(),
            "source_rule_start": rule_start,
            "source_rule_end": rule_start + len(source_rule),
            "interpretation_note": note,
        }

    return BessZoningPolicyConfig.model_validate(
        {
            "schema_version": 5,
            "policy_profile": "synthetic_policy_v5",
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
                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",
                    "reviewed_section_ids": u_articles["section_id"].tolist(),
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "CONDITIONAL_REVIEW",
                    "zoning_precheck_confidence": "MEDIUM",
                    "rationale": "The source states a review condition.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-U-POSITIVE",
                            u_article["section_id"],
                            2,
                            "USE_PERMISSION",
                            "SUPPORTS_POTENTIAL_COMPATIBILITY",
                            u_positive,
                            "RULE-U-CONDITIONAL",
                            "Technical equipment is permitted only when formal review is required.",
                            "This is positive route evidence only.",
                        ),
                        evidence(
                            "E-U-CONDITION",
                            u_article["section_id"],
                            2,
                            "TECHNICAL_EQUIPMENT_RULE",
                            "CONDITION",
                            u_condition,
                            "RULE-U-CONDITIONAL",
                            "Technical equipment is permitted only when formal review is required.",
                            "This is a condition only.",
                        ),
                    ],
                    "route_assessments": [
                        {
                            "route_id": "ROUTE-U-CONDITIONAL",
                            "route_kind": "CONDITIONAL_ROUTE",
                            "positive_evidence_ids": ["E-U-POSITIVE"],
                            "condition_evidence_ids": ["E-U-CONDITION"],
                            "difficulty_evidence_ids": [],
                            "applicability_note": "The positive route and its condition are assessed together.",
                        }
                    ],
                },
                {
                    "resolved_zone_chapter_label": "N",
                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",
                    "reviewed_section_ids": n_articles["section_id"].tolist(),
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "LIKELY_DIFFICULT",
                    "zoning_precheck_confidence": "HIGH",
                    "rationale": "The source states a relevant restriction.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-N-1",
                            n_article["section_id"],
                            3,
                            "USE_RESTRICTION",
                            "SUPPORTS_DIFFICULTY",
                            n_excerpt,
                            "RULE-N-RESTRICTION",
                            n_excerpt,
                            "This is difficulty evidence only.",
                        )
                    ],
                    "route_assessments": [
                        {
                            "route_id": "ROUTE-N-DIFFICULT",
                            "route_kind": "DIFFICULTY_ONLY",
                            "positive_evidence_ids": [],
                            "condition_evidence_ids": [],
                            "difficulty_evidence_ids": ["E-N-1"],
                            "applicability_note": "The restriction is assessed without a positive route.",
                        }
                    ],
                },
            ],
        }
    )


@pytest.fixture
def inputs(monkeypatch):
    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        lambda *args: None,
    )
    index = _index()
    zones = _zones(index)
    relations = _relations(index)
    config = _structure_config(index)
    structure = structure_planning_regulation(index, zones, relations, config)
    parcels = _parcels(index)
    policy = _policy(index, structure, config, zones, relations)
    planning_document = object()
    return (
        index,
        structure,
        config,
        zones,
        relations,
        parcels,
        planning_document,
        policy,
    )


@pytest.fixture
def valid_result(inputs):
    return interpret_bess_zoning(*inputs)


def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
    return policy.model_dump(mode="python")


def _policy_with_context_only_evidence(
    policy: BessZoningPolicyConfig,
) -> BessZoningPolicyConfig:
    payload = _payload(policy)
    chapter = payload["chapters"][0]
    chapter["evidence"][1]["evidence_direction"] = "CONTEXT_ONLY"
    route = chapter["route_assessments"][0]
    route["route_kind"] = "DIRECT_ROUTE"
    route["condition_evidence_ids"] = []
    chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
    return BessZoningPolicyConfig.model_validate(payload)


def _validate(inputs, result) -> None:
    validate_bess_zoning_precheck(*inputs, result)


def test_package_exports_precheck_api() -> None:
    for name in (
        "BessZoningPolicyConfig",
        "BessZoningPrecheckError",
        "BessZoningPrecheckResult",
        "interpret_bess_zoning",
        "load_bess_zoning_policy_config",
        "planning_regulation_section_page_fragments",
        "validate_bess_zoning_precheck",
        "validate_planning_regulation_structure_with_fragments",
    ):
        assert name in stages.__all__


def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
    index, structure, _, zones, relations, parcels, _, policy = inputs
    result = valid_result
    _validate(inputs, result)
    assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS
    assert tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS
    assert tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS
    assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS
    assert (
        tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS
    )
    assert len(result.chapter_policy) == 2
    assert len(result.source_zone_policy) == 3
    assert len(result.parcel_zone_interpretations) == 5
    assert len(result.parcels) == len(parcels)
    assert result.policy_schema_version == 5
    assert result.result_hash_schema_version == 5
    assert tuple(result.evidence_catalog.columns) == EVIDENCE_CATALOG_COLUMNS
    assert result.planning_precheck_scope == "WRITTEN_ZONING_REGULATION_ONLY"
    assert result.review_scope == "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"
    assert result.parcels["review_scope"].eq(result.review_scope).all()
    assert len(result.route_assessments) == 2
    assert len(result.evidence_route_links) == 3
    assert result.touch_only_relation_count == 1
    assert result.document_id == index.document_id
    assert (
        result.structure_result_content_sha256
        == structure.structure_result_content_sha256
    )
    assert result.zoning_relation_hash_columns == tuple(relations.columns)
    assert set(result.source_zone_policy["source_zone_label_raw"]) == set(
        zones["zone_label_raw"]
    )
    assert result.policy_profile == policy.policy_profile


@pytest.mark.parametrize(
    "field",
    [
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
    ],
)
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["source_lock"][field] = "f" * 64 if "sha256" in field else "wrong"
    bad = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="differs from factual source"):
        interpret_bess_zoning(*sources, bad)


def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
    *sources, policy = inputs
    missing_payload = _payload(policy)
    missing_payload["chapters"] = missing_payload["chapters"][:-1]
    with pytest.raises(BessZoningPrecheckError, match="completeness differs"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(missing_payload)
        )
    extra_payload = _payload(policy)
    extra = dict(extra_payload["chapters"][0])
    extra["resolved_zone_chapter_label"] = "EXTRA"
    extra["evidence"] = []
    extra["route_assessments"] = []
    extra["zoning_precheck_status"] = "UNKNOWN"
    extra_payload["chapters"] = (*extra_payload["chapters"], extra)
    with pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(extra_payload)
        )


def test_regulation_zone_chapter_labels_and_ids_must_be_unique(inputs) -> None:
    structure = inputs[1]
    assert len(interpret_module._zone_chapter_rows(structure)) == 2

    used = (
        structure.sections.loc[
            structure.sections["section_type"].eq("ZONE_CHAPTER")
            & structure.sections["zone_chapter_label"].eq("U")
        ]
        .iloc[0]
        .copy()
    )
    used["section_id"] = "SECTION-DUPLICATE-U"
    duplicated_used = replace(
        structure,
        sections=pd.concat([structure.sections, used.to_frame().T], ignore_index=True),
    )
    with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_used)

    unused_one = used.copy()
    unused_one["section_id"] = "SECTION-UNUSED-X-1"
    unused_one["zone_chapter_label"] = "X"
    unused_two = unused_one.copy()
    unused_two["section_id"] = "SECTION-UNUSED-X-2"
    duplicated_unused = replace(
        structure,
        sections=pd.concat(
            [
                structure.sections,
                unused_one.to_frame().T,
                unused_two.to_frame().T,
            ],
            ignore_index=True,
        ),
    )
    with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_unused)

    duplicate_id = used.copy()
    duplicate_id["section_id"] = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER"), "section_id"
    ].iloc[1]
    duplicate_id["zone_chapter_label"] = "X"
    duplicated_section_id = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate_id.to_frame().T], ignore_index=True
        ),
    )
    with pytest.raises(BessZoningPrecheckError, match="section IDs must be unique"):
        interpret_module._zone_chapter_rows(duplicated_section_id)


def test_source_complete_validator_rejects_later_duplicate_chapter(
    inputs, valid_result
) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    duplicate = (
        structure.sections.loc[structure.sections["section_type"].eq("ZONE_CHAPTER")]
        .iloc[0]
        .copy()
    )
    duplicate["section_id"] = "SECTION-LATE-DUPLICATE"
    changed = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate.to_frame().T], ignore_index=True
        ),
    )
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(
            index,
            changed,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            policy,
            valid_result,
        )


def test_duplicate_chapter_and_evidence_id_are_rejected(inputs) -> None:
    policy = inputs[-1]
    chapter_payload = _payload(policy)
    chapter_payload["chapters"] = (
        *chapter_payload["chapters"],
        chapter_payload["chapters"][0],
    )
    with pytest.raises(ValueError, match="chapter policy labels must be unique"):
        BessZoningPolicyConfig.model_validate(chapter_payload)
    evidence_payload = _payload(policy)
    evidence_payload["chapters"][1]["evidence"][0]["evidence_id"] = "E-U-POSITIVE"
    with pytest.raises(ValueError, match="evidence IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(evidence_payload)


def test_one_excerpt_cannot_be_reused_with_contradictory_directions(inputs) -> None:
    payload = _payload(inputs[-1])
    first = dict(payload["chapters"][0]["evidence"][1])
    second = dict(first)
    first["evidence_direction"] = "SUPPORTS_POTENTIAL_COMPATIBILITY"
    second["evidence_id"] = "E-U-2"
    second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    payload["chapters"][0]["evidence"] = (first, second)
    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)


def test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    duplicate = dict(payload["chapters"][0]["evidence"][0])
    duplicate["evidence_id"] = "E-U-POSITIVE-DUPLICATE"
    payload["chapters"][0]["evidence"] = (
        *payload["chapters"][0]["evidence"],
        duplicate,
    )
    payload["chapters"][0]["route_assessments"][0]["positive_evidence_ids"] = [
        "E-U-POSITIVE",
        "E-U-POSITIVE-DUPLICATE",
    ]

    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)


def test_duplicate_occurrence_in_different_compatible_routes_is_rejected(
    inputs,
) -> None:
    payload = _payload(inputs[-1])
    duplicate = dict(payload["chapters"][1]["evidence"][0])
    duplicate["evidence_id"] = "E-N-DUPLICATE-ROUTE"
    payload["chapters"][1]["evidence"] = (
        *payload["chapters"][1]["evidence"],
        duplicate,
    )
    payload["chapters"][1]["route_assessments"] = (
        *payload["chapters"][1]["route_assessments"],
        {
            "route_id": "ROUTE-N-DUPLICATE-OCCURRENCE",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-N-DUPLICATE-ROUTE"],
            "applicability_note": "A second route must not duplicate the occurrence.",
        },
    )

    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)


@pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_invalid_confidence_and_unknown_field_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_confidence"] = "CERTAIN"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    payload["automatic_classifier"] = True
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text(
        "schema_version: 2\nschema_version: 2\n",
        encoding="utf-8",
    )
    with pytest.raises(BessZoningPrecheckError, match="Duplicate YAML.*key"):
        load_bess_zoning_policy_config(path)


@pytest.mark.parametrize("version", [1, 2, 3, 4])
def test_old_policy_schema_versions_are_rejected(inputs, version: int) -> None:
    payload = _payload(inputs[-1])
    payload["schema_version"] = version
    with pytest.raises(ValueError, match="unsupported BESS zoning policy schema"):
        BessZoningPolicyConfig.model_validate(payload)


def test_every_evidence_kind_has_an_explicit_direction_matrix(inputs) -> None:
    allowed = {
        "USE_PERMISSION": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "CONTEXT_ONLY",
        },
        "USE_RESTRICTION": {"SUPPORTS_DIFFICULTY", "CONTEXT_ONLY"},
        "PUBLIC_INTEREST_EXCEPTION": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "TECHNICAL_EQUIPMENT_RULE": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "ICPE_RULE": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "RISK_OR_NUISANCE_CONDITION": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "ACCESS_OR_NETWORK_CONDITION": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "OTHER_RELEVANT_RULE": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
    }
    directions = {
        "SUPPORTS_POTENTIAL_COMPATIBILITY",
        "SUPPORTS_DIFFICULTY",
        "CONDITION",
        "CONTEXT_ONLY",
    }
    base = _payload(inputs[-1])["chapters"][0]["evidence"][0]
    for kind, permitted in allowed.items():
        for direction in directions:
            evidence = dict(base)
            evidence["evidence_kind"] = kind
            evidence["evidence_direction"] = direction
            if direction in permitted:
                interpret_module.PolicyEvidence.model_validate(evidence)
            else:
                with pytest.raises(
                    ValueError,
                    match="kind and direction are incompatible",
                ):
                    interpret_module.PolicyEvidence.model_validate(evidence)


def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
    policy = inputs[-1]
    excerpt = policy.chapters[0].evidence[0].exact_raw_excerpt
    assert excerpt == "Technical equipment is permitted"
    assert (
        policy.chapters[0].evidence[0].excerpt_sha256
        == sha256(excerpt.encode()).hexdigest()
    )
    assert valid_result.chapter_policy.iloc[0]["evidence_ids"] == (
        "E-U-POSITIVE",
        "E-U-CONDITION",
    )
    row = valid_result.evidence_catalog.set_index("evidence_id").loc["E-U-POSITIVE"]
    assert "only when" in row["source_rule_excerpt"]
    relative_start = row["excerpt_start"] - row["source_rule_start"]
    relative_end = row["excerpt_end"] - row["source_rule_start"]
    assert row["source_rule_excerpt"][relative_start:relative_end] == excerpt


@pytest.mark.parametrize("mutation", ["hash", "start", "end", "outside"])
def test_source_rule_identity_and_containment_are_strict(inputs, mutation: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    evidence = payload["chapters"][0]["evidence"][0]
    if mutation == "hash":
        evidence["source_rule_sha256"] = "f" * 64
        with pytest.raises(ValueError, match="source rule SHA256"):
            BessZoningPolicyConfig.model_validate(payload)
        return
    if mutation == "outside":
        evidence["source_rule_start"] = evidence["excerpt_start"] + 1
        with pytest.raises(ValueError, match="inside its source rule"):
            BessZoningPolicyConfig.model_validate(payload)
        return
    for related in payload["chapters"][0]["evidence"]:
        if mutation == "start":
            related["source_rule_start"] -= 1
        else:
            related["source_rule_end"] += 1
    with pytest.raises(BessZoningPrecheckError, match="source-rule offsets"):
        interpret_bess_zoning(
            *sources,
            BessZoningPolicyConfig.model_validate(payload),
        )


def test_same_rule_text_at_distinct_offsets_has_distinct_identity(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    first = chapter["evidence"][0]
    second = dict(first)
    rule_length = len(first["source_rule_excerpt"])
    second_rule_start = first["source_rule_end"] + 1
    second["evidence_id"] = "E-U-SECOND-OCCURRENCE"
    second["evidence_kind"] = "TECHNICAL_EQUIPMENT_RULE"
    second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    second["source_rule_id"] = "RULE-U-SECOND-OCCURRENCE"
    second["source_rule_start"] = second_rule_start
    second["source_rule_end"] = second_rule_start + rule_length
    second["excerpt_start"] = second_rule_start
    second["excerpt_end"] = second_rule_start + len(first["exact_raw_excerpt"])
    chapter["evidence"] = (*chapter["evidence"], second)
    chapter["route_assessments"] = (
        *chapter["route_assessments"],
        {
            "route_id": "ROUTE-U-SECOND-DIFFICULTY",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-U-SECOND-OCCURRENCE"],
            "applicability_note": "The distinct occurrence is linked explicitly.",
        },
    )
    policy = BessZoningPolicyConfig.model_validate(payload)
    assert policy.chapters[0].evidence[-1].evidence_direction == "SUPPORTS_DIFFICULTY"


def test_real_muret_source_rules_preserve_conditional_and_exception_frames() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    by_label = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    for label in ("UA", "UB", "UC", "UD", "UF", "AU", "AUf"):
        positive = next(
            evidence
            for evidence in by_label[label].evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert "ne sont autorisées qu’à" in positive.source_rule_excerpt
        assert "condition" in positive.source_rule_excerpt
    for label in ("UP", "AUp"):
        positive = next(
            evidence
            for evidence in by_label[label].evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert positive.source_rule_excerpt.startswith("Toutes constructions")
        assert "autres que celles" in positive.source_rule_excerpt
    for label in ("AU0", "AUf0", "A", "N"):
        chapter = by_label[label]
        positive = next(
            evidence
            for evidence in chapter.evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert positive.source_rule_excerpt.startswith("Sont interdites")
        if label in {"A", "N"}:
            difficulty = next(
                evidence
                for evidence in chapter.evidence
                if evidence.evidence_direction == "SUPPORTS_DIFFICULTY"
            )
            assert difficulty.source_rule_id == positive.source_rule_id
            assert difficulty.source_rule_excerpt == positive.source_rule_excerpt


def test_real_muret_up_route_does_not_use_the_separate_icpe_condition() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    assert policy.schema_version == 5
    assert policy.policy_profile == "muret_bess_written_zoning_v6"
    chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "UP"
    )
    route = chapter.route_assessments[0]

    assert route.route_kind == "RESTRICTION_EXCEPTION_ROUTE"
    assert route.positive_evidence_ids == ("MURET-UP-PUBLIC-ROUTE-01",)
    assert route.condition_evidence_ids == ()
    assert route.difficulty_evidence_ids == ("MURET-UP-RESTRICTION-01",)

    restriction = next(
        evidence
        for evidence in chapter.evidence
        if evidence.evidence_id == "MURET-UP-RESTRICTION-01"
    )
    assert restriction.evidence_kind == "USE_RESTRICTION"
    assert restriction.evidence_direction == "SUPPORTS_DIFFICULTY"
    assert restriction.section_id == "SECTION-0080"
    assert restriction.page_number == 71
    assert (
        restriction.exact_raw_excerpt
        == "Toutes constructions ou  installations autres que celles"
    )
    assert restriction.excerpt_start == 68
    assert restriction.excerpt_end == 124
    assert restriction.excerpt_sha256 == (
        "edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462"
    )
    assert restriction.section_page_fragment_sha256 == (
        "06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"
    )
    assert restriction.source_rule_id == "MURET-UP-ROUTE-RULE-01"
    assert restriction.source_rule_start == 68
    assert restriction.source_rule_end == 236
    assert restriction.source_rule_sha256 == (
        "de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"
    )


def test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "AUp"
    )
    route = chapter.route_assessments[0]

    assert route.route_kind == "CONDITIONAL_ROUTE"
    assert route.positive_evidence_ids == ("MURET-AUP-PUBLIC-ROUTE-01",)
    assert route.condition_evidence_ids == ("MURET-AUP-INFRASTRUCTURE-CONDITION-01",)
    assert route.difficulty_evidence_ids == ()

    prerequisite = next(
        evidence
        for evidence in chapter.evidence
        if evidence.evidence_id == "MURET-AUP-INFRASTRUCTURE-CONDITION-01"
    )
    exact_rule = (
        "Les constructions et opérations ne pourront être autorisées qu’après "
        "réalisation des  \n"
        "équipements d’infrastructure indispensable à leur fonctionnement "
        "(accès, voirie et  \n"
        "réseaux divers) conformément aux articles AUp3 et AUp4."
    )
    assert prerequisite.evidence_kind == "ACCESS_OR_NETWORK_CONDITION"
    assert prerequisite.evidence_direction == "CONDITION"
    assert prerequisite.section_id == "SECTION-0111"
    assert prerequisite.page_number == 93
    assert prerequisite.exact_raw_excerpt == exact_rule
    assert prerequisite.excerpt_start == 98
    assert prerequisite.excerpt_end == 325
    assert prerequisite.excerpt_sha256 == (
        "b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"
    )
    assert prerequisite.section_page_fragment_sha256 == (
        "57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"
    )
    assert prerequisite.source_rule_id == "MURET-AUp-INFRASTRUCTURE-RULE-01"
    assert prerequisite.source_rule_excerpt == exact_rule
    assert prerequisite.source_rule_start == 98
    assert prerequisite.source_rule_end == 325
    assert prerequisite.source_rule_sha256 == prerequisite.excerpt_sha256


def test_real_muret_up_and_aup_keep_icpe_applicability_as_context() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    chapters = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    identities = {
        "UP": "MURET-UP-ICPE-CONDITION-01",
        "AUp": "MURET-AUP-ICPE-CONDITION-01",
    }

    for label, evidence_id in identities.items():
        chapter = chapters[label]
        evidence = next(
            item for item in chapter.evidence if item.evidence_id == evidence_id
        )
        assert evidence.evidence_kind == "ICPE_RULE"
        assert evidence.evidence_direction == "CONTEXT_ONLY"
        assert "ICPE" in chapter.missing_information
        for route in chapter.route_assessments:
            linked_ids = (
                route.positive_evidence_ids
                + route.condition_evidence_ids
                + route.difficulty_evidence_ids
            )
            assert evidence_id not in linked_ids


def test_absent_excerpt_and_section_page_mismatch_are_rejected(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    excerpt = "Not present in the indexed source."
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(BessZoningPrecheckError, match="offsets"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
    payload = _payload(policy)
    for evidence in payload["chapters"][0]["evidence"]:
        evidence["page_number"] = 3
    with pytest.raises(BessZoningPrecheckError, match="section/page fragment"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_excerpt_hash_and_length_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="excerpt SHA256 differs"):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    excerpt = "x" * 601
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


@pytest.mark.parametrize(
    "status", ["POTENTIALLY_COMPATIBLE", "LIKELY_DIFFICULT", "UNKNOWN"]
)
def test_declared_status_must_equal_derived_route_status(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError, match="differs from coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)


def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    payload["chapters"][0]["evidence"] = [payload["chapters"][0]["evidence"][1]]
    payload["chapters"][0]["route_assessments"] = []
    with pytest.raises(ValueError, match="coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unrelated_positive_and_condition_do_not_create_conditional_review(
    inputs,
) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIRECT-ONLY",
            "route_kind": "DIRECT_ROUTE",
            "positive_evidence_ids": ["E-U-POSITIVE"],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": [],
            "applicability_note": "The separate condition is deliberately unlinked.",
        }
    ]
    with pytest.raises(ValueError, match="coherent|linked route"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unlinked_context_only_unknown_succeeds(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = [chapter["evidence"][1]]
    chapter["evidence"][0]["evidence_direction"] = "CONTEXT_ONLY"
    chapter["route_assessments"] = []
    policy = BessZoningPolicyConfig.model_validate(payload)
    assert policy.chapters[0].zoning_precheck_status == "UNKNOWN"


def test_positive_condition_and_conflict_status_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    assert (
        BessZoningPolicyConfig.model_validate(payload)
        .chapters[0]
        .zoning_precheck_status
        == "CONDITIONAL_REVIEW"
    )
    conflict = _payload(inputs[-1])
    conflict["chapters"][0]["evidence"][1]["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    route = conflict["chapters"][0]["route_assessments"][0]
    route["route_kind"] = "RESTRICTION_EXCEPTION_ROUTE"
    route["condition_evidence_ids"] = []
    route["difficulty_evidence_ids"] = ["E-U-CONDITION"]
    policy = BessZoningPolicyConfig.model_validate(conflict)
    assert policy.chapters[0].zoning_precheck_status == "CONDITIONAL_REVIEW"


def test_route_references_must_be_same_chapter_and_role_compatible(inputs) -> None:
    for mutation, message in (
        ("unknown", "unknown or another-chapter"),
        ("another_chapter", "unknown or another-chapter"),
        ("wrong_role", "incompatible positive role"),
    ):
        payload = _payload(inputs[-1])
        route = payload["chapters"][0]["route_assessments"][0]
        if mutation == "unknown":
            route["condition_evidence_ids"] = ["E-UNKNOWN"]
        elif mutation == "another_chapter":
            route["condition_evidence_ids"] = ["E-N-1"]
        else:
            route["route_kind"] = "DIRECT_ROUTE"
            route["positive_evidence_ids"] = ["E-U-CONDITION"]
            route["condition_evidence_ids"] = []
            payload["chapters"][0]["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
        with pytest.raises(ValueError, match=message):
            BessZoningPolicyConfig.model_validate(payload)


def test_route_ids_are_globally_unique(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][1]["route_assessments"][0]["route_id"] = payload["chapters"][0][
        "route_assessments"
    ][0]["route_id"]
    with pytest.raises(ValueError, match="route IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unlinked_difficulty_evidence_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    unlinked = dict(payload["chapters"][1]["evidence"][0])
    unlinked["evidence_id"] = "E-N-UNLINKED"
    unlinked["source_rule_id"] = "RULE-N-UNLINKED"
    for field in (
        "excerpt_start",
        "excerpt_end",
        "source_rule_start",
        "source_rule_end",
    ):
        unlinked[field] += 100
    payload["chapters"][1]["evidence"] = (
        *payload["chapters"][1]["evidence"],
        unlinked,
    )

    with pytest.raises(ValueError, match="decision evidence must be linked"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unlinked_positive_and_condition_evidence_are_rejected(inputs) -> None:
    for direction, evidence_index in (
        ("SUPPORTS_POTENTIAL_COMPATIBILITY", 0),
        ("CONDITION", 1),
    ):
        payload = _payload(inputs[-1])
        unlinked = dict(payload["chapters"][0]["evidence"][evidence_index])
        unlinked["evidence_id"] = f"E-U-UNLINKED-{direction}"
        unlinked["source_rule_id"] = f"RULE-U-UNLINKED-{direction}"
        for field in (
            "excerpt_start",
            "excerpt_end",
            "source_rule_start",
            "source_rule_end",
        ):
            unlinked[field] += 100
        payload["chapters"][0]["evidence"] = (
            *payload["chapters"][0]["evidence"],
            unlinked,
        )
        with pytest.raises(ValueError, match="decision evidence must be linked"):
            BessZoningPolicyConfig.model_validate(payload)


def test_context_only_evidence_must_be_unlinked(inputs) -> None:
    policy = _policy_with_context_only_evidence(inputs[-1])
    assert policy.chapters[0].evidence[1].evidence_direction == "CONTEXT_ONLY"

    payload = _payload(policy)
    payload["chapters"][0]["route_assessments"][0]["condition_evidence_ids"] = [
        "E-U-CONDITION"
    ]
    payload["chapters"][0]["route_assessments"][0]["route_kind"] = "CONDITIONAL_ROUTE"
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_one_evidence_may_link_to_multiple_compatible_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    route = dict(payload["chapters"][1]["route_assessments"][0])
    route["route_id"] = "ROUTE-N-DIFFICULT-SECOND"
    payload["chapters"][1]["route_assessments"] = (
        *payload["chapters"][1]["route_assessments"],
        route,
    )
    policy = BessZoningPolicyConfig.model_validate(payload)
    *sources, _ = inputs
    result = interpret_bess_zoning(*sources, policy)
    evidence = result.evidence_catalog.set_index("evidence_id").loc["E-N-1"]
    assert evidence["linked_route_ids"] == (
        "ROUTE-N-DIFFICULT",
        "ROUTE-N-DIFFICULT-SECOND",
    )
    assert evidence["linked_route_roles"] == ("DIFFICULTY", "DIFFICULTY")


def test_difficulty_and_positive_only_status_routes(inputs) -> None:
    difficult = _payload(inputs[-1])
    chapter = difficult["chapters"][0]
    chapter["zoning_precheck_status"] = "LIKELY_DIFFICULT"
    chapter["evidence"] = [chapter["evidence"][1]]
    chapter["evidence"][0]["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIFFICULT",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-U-CONDITION"],
            "applicability_note": "Only the linked difficulty is assessed.",
        }
    ]
    assert (
        BessZoningPolicyConfig.model_validate(difficult)
        .chapters[0]
        .zoning_precheck_status
        == "LIKELY_DIFFICULT"
    )
    potential = _payload(inputs[-1])
    chapter = potential["chapters"][0]
    chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
    chapter["evidence"] = [chapter["evidence"][0]]
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIRECT",
            "route_kind": "DIRECT_ROUTE",
            "positive_evidence_ids": ["E-U-POSITIVE"],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": [],
            "applicability_note": "Only the direct linked route is assessed.",
        }
    ]
    assert (
        BessZoningPolicyConfig.model_validate(potential)
        .chapters[0]
        .zoning_precheck_status
        == "POTENTIALLY_COMPATIBLE"
    )


def test_incomplete_review_requires_unknown_low(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["review_completeness"] = "INCOMPLETE"
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = []
    chapter["route_assessments"] = []
    chapter["reviewed_section_ids"] = []
    assert (
        BessZoningPolicyConfig.model_validate(payload).chapters[0].review_completeness
        == "INCOMPLETE"
    )
    for field, value in (
        ("zoning_precheck_status", "CONDITIONAL_REVIEW"),
        ("zoning_precheck_confidence", "MEDIUM"),
    ):
        invalid = _payload(inputs[-1])
        candidate = invalid["chapters"][0]
        candidate["review_completeness"] = "INCOMPLETE"
        candidate["zoning_precheck_status"] = "UNKNOWN"
        candidate["zoning_precheck_confidence"] = "LOW"
        candidate["evidence"] = []
        candidate["route_assessments"] = []
        candidate["reviewed_section_ids"] = []
        candidate[field] = value
        with pytest.raises(ValueError, match="incomplete review"):
            BessZoningPolicyConfig.model_validate(invalid)


def test_incomplete_review_persists_exact_missing_required_sections(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    chapter = payload["chapters"][0]
    chapter["review_completeness"] = "INCOMPLETE"
    chapter["reviewed_section_ids"] = []
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = []
    chapter["route_assessments"] = []
    result = interpret_bess_zoning(
        *sources,
        BessZoningPolicyConfig.model_validate(payload),
    )
    row = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
    assert row["reviewed_section_ids"] == ()
    expected_missing = tuple(
        inputs[1].sections.loc[
            inputs[1].sections["section_type"].eq("ARTICLE")
            & inputs[1].sections["zone_chapter_label"].eq("U"),
            "section_id",
        ]
    )
    assert row["missing_required_section_ids"] == expected_missing
    assert row["zoning_precheck_status"] == "UNKNOWN"
    assert row["zoning_precheck_confidence"] == "LOW"


def test_unknown_is_accepted_when_evidence_is_insufficient(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["chapters"][0]["zoning_precheck_status"] = "UNKNOWN"
    payload["chapters"][0]["evidence"] = []
    payload["chapters"][0]["route_assessments"] = []
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    assert result.chapter_policy.iloc[0]["zoning_precheck_status"] == "UNKNOWN"


def test_reviewed_sections_cover_required_articles(inputs) -> None:
    *sources, policy = inputs
    index, structure = inputs[:2]
    payload = _payload(policy)
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
    with pytest.raises(BessZoningPrecheckError, match="omits required reviewed"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
    assert index.document_id == "doc-1"


@pytest.mark.parametrize("article_number", ["1", "2"])
def test_every_configured_article_must_exist_once_in_every_chapter(
    inputs,
    article_number: str,
) -> None:
    structure = inputs[1]
    policy = inputs[-1]
    keep = ~(
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("U")
        & structure.sections["article_number_raw"].eq(article_number)
    )
    changed = replace(
        structure,
        sections=structure.sections.loc[keep].reset_index(drop=True),
    )

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, policy)


def test_duplicate_configured_article_is_rejected(inputs) -> None:
    structure = inputs[1]
    duplicate = (
        structure.sections.loc[
            structure.sections["section_type"].eq("ARTICLE")
            & structure.sections["zone_chapter_label"].eq("U")
            & structure.sections["article_number_raw"].eq("2")
        ]
        .iloc[0]
        .copy()
    )
    duplicate["section_id"] = "SECTION-DUPLICATE-U-2"
    changed = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate.to_frame().T], ignore_index=True
        ),
    )

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, inputs[-1])


def test_configured_article_with_wrong_chapter_parent_is_rejected(inputs) -> None:
    structure = inputs[1]
    sections = structure.sections.copy(deep=True)
    n_chapter_id = sections.loc[
        sections["section_type"].eq("ZONE_CHAPTER")
        & sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
    target = (
        sections["section_type"].eq("ARTICLE")
        & sections["zone_chapter_label"].eq("U")
        & sections["article_number_raw"].eq("2")
    )
    sections.loc[target, "parent_section_id"] = n_chapter_id
    changed = replace(structure, sections=sections)

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, inputs[-1])


def test_evidence_must_be_inside_reviewed_sections(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    payload["required_zone_article_numbers"] = ["2"]
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    article_2_id = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("U")
        & structure.sections["article_number_raw"].eq("2"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id, article_2_id]
    with pytest.raises(BessZoningPrecheckError, match="outside reviewed sections"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_review_cannot_claim_another_chapter_section(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    n_article = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (n_article,)
    with pytest.raises(BessZoningPrecheckError, match="another chapter"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_general_section_review_is_explicit_and_valid(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    general_id = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL"), "section_id"
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (general_id,)
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    reviewed = result.chapter_policy.set_index("resolved_zone_chapter_label").loc[
        "U", "reviewed_section_ids"
    ]
    assert general_id in reviewed


def test_same_general_occurrence_may_be_scoped_to_different_chapters(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    general = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL")
    ].iloc[0]
    fragment = (
        planning_regulation_section_page_fragments(
            index, zones, relations, config, structure
        )
        .set_index(["section_id", "page_number"])
        .loc[(general["section_id"], 1)]
    )
    excerpt = "General factual text."
    start = fragment["raw_text"].index(excerpt)
    base = {
        "section_id": general["section_id"],
        "page_number": 1,
        "evidence_kind": "TECHNICAL_EQUIPMENT_RULE",
        "evidence_direction": "CONTEXT_ONLY",
        "exact_raw_excerpt": excerpt,
        "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
        "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],
        "excerpt_start": start,
        "excerpt_end": start + len(excerpt),
        "source_rule_id": "RULE-GENERAL-CONTEXT",
        "source_rule_excerpt": excerpt,
        "source_rule_sha256": sha256(excerpt.encode()).hexdigest(),
        "source_rule_start": start,
        "source_rule_end": start + len(excerpt),
        "interpretation_note": "The same factual GENERAL occurrence is chapter-scoped.",
    }
    payload = _payload(policy)
    for chapter, evidence_id in zip(
        payload["chapters"],
        ("E-U-GENERAL-CONTEXT", "E-N-GENERAL-CONTEXT"),
        strict=True,
    ):
        chapter["reviewed_section_ids"] = (
            *chapter["reviewed_section_ids"],
            general["section_id"],
        )
        chapter["evidence"] = (
            *chapter["evidence"],
            {**base, "evidence_id": evidence_id},
        )
    scoped_policy = BessZoningPolicyConfig.model_validate(payload)
    result = interpret_bess_zoning(
        index,
        structure,
        config,
        zones,
        relations,
        parcels,
        planning_document,
        scoped_policy,
    )
    scoped = result.evidence_catalog.loc[
        result.evidence_catalog["section_id"].eq(general["section_id"])
        & result.evidence_catalog["excerpt_start"].eq(start)
    ]
    assert set(scoped["resolved_zone_chapter_label"]) == {"U", "N"}
    assert len(scoped) == 2


def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    for row in valid_result.evidence_catalog.to_dict("records"):
        fragment = fragments.loc[(row["section_id"], row["page_number"])]
        assert (
            row["section_page_fragment_sha256"]
            == fragment["section_page_fragment_sha256"]
        )
        assert (
            fragment["raw_text"][row["excerpt_start"] : row["excerpt_end"]]
            == row["exact_raw_excerpt"]
        )


def test_repeated_excerpt_occurrence_is_bound_to_policy(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    row_index = valid_result.evidence_catalog.index[
        valid_result.evidence_catalog["evidence_id"].eq("E-U-POSITIVE")
    ][0]
    row = valid_result.evidence_catalog.loc[row_index]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    raw = fragments.loc[(row["section_id"], row["page_number"]), "raw_text"]
    first = raw.index(row["exact_raw_excerpt"])
    second = raw.index(row["exact_raw_excerpt"], first + 1)
    assert second > first

    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[row_index, "excerpt_start"] = second
    catalog.loc[row_index, "excerpt_end"] = second + len(row["exact_raw_excerpt"])
    coordinated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, coordinated)


@pytest.mark.parametrize("mutation", ["page", "fragment_hash", "start", "end"])
def test_wrong_occurrence_identity_is_rejected(inputs, mutation: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    evidence = payload["chapters"][0]["evidence"][0]
    if mutation == "page":
        for related in payload["chapters"][0]["evidence"]:
            related["page_number"] = 1
    elif mutation == "fragment_hash":
        for related in payload["chapters"][0]["evidence"]:
            related["section_page_fragment_sha256"] = "f" * 64
    elif mutation == "start":
        evidence["excerpt_start"] += 1
    else:
        evidence["excerpt_end"] -= 1
    with pytest.raises(BessZoningPrecheckError, match="fragment|offset"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(
    valid_result,
) -> None:
    policies = valid_result.source_zone_policy.set_index("source_zone_label_raw")
    assert policies.loc["U", "mapping_status"] == "EXACT"
    assert policies.loc["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert policies.loc["Ua", "resolved_zone_chapter_label"] == "U"
    assert (
        policies.loc["Ua", "zoning_precheck_status"]
        == policies.loc["U", "zoning_precheck_status"]
    )


def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    mapping = structure.zone_mapping.copy()
    mapping.loc[
        mapping["source_zone_label_raw"].eq("U"),
        [
            "resolved_zone_chapter_label",
            "matched_section_id",
        ],
    ] = None
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_status"] = "UNMAPPED"
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_method"] = "NONE"
    mutated = _structure_with_hashes(replace(structure, zone_mapping=mapping))
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        mutated.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            mutated,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )


def test_link_table_exactly_reproduces_routes_and_reverse_links(valid_result) -> None:
    expected = {
        ("ROUTE-U-CONDITIONAL", "E-U-POSITIVE", "POSITIVE"),
        ("ROUTE-U-CONDITIONAL", "E-U-CONDITION", "CONDITION"),
        ("ROUTE-N-DIFFICULT", "E-N-1", "DIFFICULTY"),
    }
    actual = {
        (row.route_id, row.evidence_id, row.route_role)
        for row in valid_result.evidence_route_links.itertuples(index=False)
    }
    assert actual == expected
    catalog = valid_result.evidence_catalog.set_index("evidence_id")
    assert catalog.loc["E-U-POSITIVE", "linked_route_ids"] == ("ROUTE-U-CONDITIONAL",)
    assert catalog.loc["E-U-POSITIVE", "linked_route_roles"] == ("POSITIVE",)
    assert bool(catalog["decision_linked"].all())


def test_context_evidence_is_separate_from_decision_outputs(inputs) -> None:
    *sources, policy = inputs
    context_policy = _policy_with_context_only_evidence(policy)
    result = interpret_bess_zoning(*sources, context_policy)
    catalog = result.evidence_catalog.set_index("evidence_id")
    context = catalog.loc["E-U-CONDITION"]
    assert context["linked_route_ids"] == ()
    assert context["linked_route_roles"] == ()
    assert not bool(context["decision_linked"])
    chapter = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
    assert chapter["evidence_ids"] == ("E-U-POSITIVE", "E-U-CONDITION")
    assert chapter["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert chapter["context_evidence_ids"] == ("E-U-CONDITION",)
    source = result.source_zone_policy.set_index("source_zone_label_raw").loc["U"]
    assert source["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert source["context_evidence_ids"] == ("E-U-CONDITION",)
    relation = result.parcel_zone_interpretations.loc[
        result.parcel_zone_interpretations["resolved_zone_chapter_label"].eq("U")
    ].iloc[0]
    assert relation["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert relation["context_evidence_ids"] == ("E-U-CONDITION",)
    parcel = result.parcels.loc[result.parcels["parcel_id"].eq("P-1")].iloc[0]
    assert parcel["zoning_precheck_evidence_ids"] == ("E-U-POSITIVE",)
    assert parcel["zoning_precheck_context_evidence_ids"] == ("E-U-CONDITION",)


def test_parcel_aggregation_preserves_conflicts_and_touch_only(valid_result) -> None:
    parcels = valid_result.parcels.set_index("parcel_id")
    assert parcels.loc["P-1", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-1", "positive_area_zone_count"] == 1
    assert parcels.loc["P-2", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-2", "positive_area_zone_count"] == 2
    assert parcels.loc["P-2", "distinct_zone_status_count"] == 1
    assert parcels.loc["P-3", "zoning_precheck_status"] == "MIXED_REVIEW_REQUIRED"
    assert parcels.loc["P-3", "dominant_zone_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-3", "non_dominant_different_status_count"] == 1
    assert parcels.loc["P-4", "zoning_precheck_status"] == "UNKNOWN"
    assert parcels.loc["P-4", "positive_area_zone_count"] == 0
    assert parcels.loc["P-4", "touch_only_zone_count"] == 1
    assert pd.isna(parcels.loc["P-4", "dominant_zone_precheck_status"])
    assert valid_result.touch_only_relation_count == 1
    assert "P-4" not in set(valid_result.parcel_zone_interpretations["parcel_id"])


def test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved(
    inputs, valid_result
) -> None:
    original = inputs[5]
    prior = valid_result.parcels.loc[:, original.columns]
    assert_geodataframe_equal(prior, original)
    assert valid_result.parcels.index.equals(original.index)
    assert valid_result.parcels.crs == original.crs
    assert valid_result.parcels["planning_surface_relation_count"].equals(
        original["planning_surface_relation_count"]
    )
    assert (
        valid_result.parcels["non_zoning_planning_features_interpreted"].eq(False).all()
    )
    assert valid_result.parcels["zoning_precheck_requires_formal_review"].eq(True).all()


def test_inputs_are_not_mutated(inputs) -> None:
    _, structure, _, zones, relations, parcels, _, _ = inputs
    zone_snapshot = zones.copy(deep=True)
    relation_snapshot = relations.copy(deep=True)
    parcel_snapshot = parcels.copy(deep=True)
    section_snapshot = structure.sections.copy(deep=True)
    interpret_bess_zoning(*inputs)
    pd.testing.assert_frame_equal(zones, zone_snapshot)
    pd.testing.assert_frame_equal(relations, relation_snapshot)
    assert_geodataframe_equal(parcels, parcel_snapshot)
    pd.testing.assert_frame_equal(structure.sections, section_snapshot)


def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["rationale"] = "Changed checked-in rationale."
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="policy_config_sha256"):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)


def test_evidence_change_after_result_creation_is_rejected(
    inputs, valid_result
) -> None:
    payload = _payload(inputs[-1])
    excerpt = "equipment is permitted"
    evidence = payload["chapters"][0]["evidence"][0]
    evidence["exact_raw_excerpt"] = excerpt
    evidence["excerpt_sha256"] = sha256(excerpt.encode()).hexdigest()
    evidence["excerpt_start"] += len("Technical ")
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)


def test_zoning_relation_and_zone_mapping_changes_are_rejected(
    inputs, valid_result
) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_relations = relations.copy()
    changed_relations.loc[0, "intersection_area_m2"] = 99.0
    changed_relations.loc[0, "parcel_share_pct"] = 99.0
    changed_relations.loc[0, "zone_share_pct"] = 9.9
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        validate_bess_zoning_precheck(
            index,
            structure,
            config,
            zones,
            changed_relations,
            parcels,
            planning_document,
            policy,
            valid_result,
        )


def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_config = config.model_copy(update={"structure_profile": "changed"})
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            structure,
            changed_config,
            zones,
            relations,
            parcels,
            planning_document,
            policy,
        )
    changed_sections = structure.sections.copy(deep=True)
    article = changed_sections["section_type"].eq("ARTICLE")
    changed_sections.loc[article.idxmax(), "parent_section_id"] = "SECTION-UNKNOWN"
    changed_structure = _structure_with_hashes(
        replace(structure, sections=changed_sections)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )


def test_public_source_complete_validator_is_invoked(inputs, monkeypatch) -> None:
    calls = 0
    original = interpret_module.validate_planning_regulation_structure_with_fragments

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(
        interpret_module,
        "validate_planning_regulation_structure_with_fragments",
        counted,
    )
    interpret_bess_zoning(*inputs)
    assert calls >= 1


def test_one_precheck_build_performs_one_zoning_source_complete_validation(
    inputs,
    monkeypatch,
) -> None:
    calls = 0

    def counted(*args) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        counted,
    )

    interpret_bess_zoning(*inputs)

    assert calls == 1


def test_invalid_physical_zoning_fails_before_policy_interpretation(
    inputs,
    monkeypatch,
) -> None:
    policy_calls = 0

    def invalid_source(*args) -> None:
        raise interpret_module.PlanningZoningError("physical source invalid")

    def counted_policy(*args):
        nonlocal policy_calls
        policy_calls += 1
        return inputs[-1]

    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        invalid_source,
    )
    monkeypatch.setattr(interpret_module, "_resolved_policy", counted_policy)

    with pytest.raises(BessZoningPrecheckError, match="physical source invalid"):
        interpret_bess_zoning(*inputs)

    assert policy_calls == 0


def test_one_build_result_performs_one_factual_structure_rebuild(
    inputs, monkeypatch
) -> None:
    calls = 0
    original = interpret_module.validate_planning_regulation_structure_with_fragments

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(
        interpret_module,
        "validate_planning_regulation_structure_with_fragments",
        counted,
    )
    interpret_module._build_result(*inputs[:6], inputs[-1])
    assert calls == 1


@pytest.mark.parametrize(
    "column",
    ["parcel_metric_area_m2", "zone_area_m2"],
)
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            relations.drop(columns=column),
            parcels,
            planning_document,
            policy,
        )


@pytest.mark.parametrize(
    "column",
    ["parcel_share_pct", "zone_share_pct"],
)
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed = relations.copy(deep=True)
    changed.loc[0, column] += 1.0
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            changed,
            parcels,
            planning_document,
            policy,
        )


def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_mapping = structure.zone_mapping.copy(deep=True)
    changed_mapping.loc[0, "candidate_intersection_count"] += 1
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )
    changed_mapping = structure.zone_mapping.copy()
    changed_mapping.loc[0, "source_zone_label_raw"] = "CHANGED"
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
            valid_result,
        )


def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
    chapter = valid_result.chapter_policy.copy(deep=True)
    chapter.loc[0, "zoning_precheck_confidence"] = "HIGH"
    mutated = _result_with_hashes(replace(valid_result, chapter_policy=chapter))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_evidence_catalog_mutation_is_rejected(
    inputs, valid_result
) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[0, "interpretation_note"] = "Coordinated mutation."
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_catalog_occurrence_duplicate_is_rejected(
    inputs, valid_result
) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    occurrence_columns = [
        "resolved_zone_chapter_label",
        "section_id",
        "page_number",
        "section_page_fragment_sha256",
        "excerpt_start",
        "excerpt_end",
    ]
    catalog.loc[catalog.index[1], occurrence_columns] = catalog.loc[
        catalog.index[0], occurrence_columns
    ].to_numpy()
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(
        BessZoningPrecheckError,
        match="duplicate chapter-scoped evidence occurrence",
    ):
        _validate(inputs, mutated)


def test_coordinated_route_table_mutation_is_rejected(inputs, valid_result) -> None:
    routes = valid_result.route_assessments.copy(deep=True)
    routes.loc[0, "applicability_note"] = "Coordinated route mutation."
    mutated = _result_with_hashes(replace(valid_result, route_assessments=routes))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_evidence_route_link_mutation_is_rejected(
    inputs, valid_result
) -> None:
    links = valid_result.evidence_route_links.copy(deep=True)
    links.loc[0, "route_role"] = "BROKEN"
    mutated = _result_with_hashes(replace(valid_result, evidence_route_links=links))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_reverse_link_mutation_is_rejected(inputs, valid_result) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.at[0, "linked_route_roles"] = ("DIFFICULTY",)
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_evidence_route_link_hash_mutation_is_rejected(inputs, valid_result) -> None:
    mutated = replace(
        valid_result,
        evidence_route_links_content_sha256="f" * 64,
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


@pytest.mark.parametrize("version", [1, 2, 3, 4])
def test_old_result_hash_schemas_are_rejected(
    inputs, valid_result, version: int
) -> None:
    with pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version"):
        _validate(inputs, replace(valid_result, result_hash_schema_version=version))


def test_relation_identity_change_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed = relations.copy()
    changed.loc[0, "source_zone_id"] = "SRC-N"
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            changed,
            parcels,
            planning_document,
            policy,
        )


def test_readback_result_validates(tmp_path: Path, inputs, valid_result) -> None:
    chapter_path = tmp_path / "chapter.parquet"
    evidence_path = tmp_path / "evidence.parquet"
    route_path = tmp_path / "routes.parquet"
    link_path = tmp_path / "links.parquet"
    source_path = tmp_path / "source.parquet"
    relation_path = tmp_path / "relations.parquet"
    parcel_path = tmp_path / "parcels.parquet"
    valid_result.evidence_catalog.to_parquet(evidence_path, index=False)
    valid_result.route_assessments.to_parquet(route_path, index=False)
    valid_result.evidence_route_links.to_parquet(link_path, index=False)
    valid_result.chapter_policy.to_parquet(chapter_path, index=False)
    valid_result.source_zone_policy.to_parquet(source_path, index=False)
    valid_result.parcel_zone_interpretations.to_parquet(relation_path, index=False)
    valid_result.parcels.to_parquet(parcel_path)
    persisted = replace(
        valid_result,
        evidence_catalog=pd.read_parquet(evidence_path),
        route_assessments=pd.read_parquet(route_path),
        evidence_route_links=pd.read_parquet(link_path),
        chapter_policy=pd.read_parquet(chapter_path),
        source_zone_policy=pd.read_parquet(source_path),
        parcel_zone_interpretations=pd.read_parquet(relation_path),
        parcels=gpd.read_parquet(parcel_path),
    )
    _validate(inputs, persisted)
    occurrence_columns = [
        "resolved_zone_chapter_label",
        "section_id",
        "page_number",
        "section_page_fragment_sha256",
        "excerpt_start",
        "excerpt_end",
    ]
    assert not persisted.evidence_catalog.duplicated(occurrence_columns).any()


def test_policy_yaml_roundtrip_is_strict(tmp_path: Path, inputs) -> None:
    policy = inputs[-1]
    path = tmp_path / "policy.yaml"
    import yaml  # type: ignore[import-untyped]

    path.write_text(
        yaml.safe_dump(
            policy.model_dump(mode="json"),
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    assert load_bess_zoning_policy_config(path) == policy
```
