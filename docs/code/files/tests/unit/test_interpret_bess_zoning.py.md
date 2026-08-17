# `tests/unit/test_interpret_bess_zoning.py`

## File identity

- Repository path: `tests/unit/test_interpret_bess_zoning.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.
- Source SHA256: `ad1c19efd0af0fca02ac633836edf8f4be194580ba06e389ebde64795335d7a8`

## 1. Purpose

Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_index`

**Exact signature**

```python
def _index() -> PlanningRegulationIndex:
```

**Purpose**

Private `test` helper for index; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningRegulationIndex`.
- Every observed return expression is reproduced without truncation:
```python
replace(index, index_content_sha256=_index_content_sha256(index))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_index_content_sha256`, `_page_content_sha256`, `_pages_content_sha256`.
- Environment/process effects: none.
- In-memory mutation: `row['page_content_sha256']`, `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_interpret_bess_zoning.py::inputs` via `_index`.

**Complete source-ordered implementation**

```python
def _index() -> PlanningRegulationIndex:
    raw_pages = (
        "ARTICLE 1 - GENERAL\nGeneral factual text.",
        (
            "ZONE U\nARTICLE U 1 - USES\nTechnical equipment is permitted only when "
            "formal review is required.\nTechnical equipment is permitted only when "
            "formal review is required."
        ),
        (
            "ZONE N\nARTICLE N 1 - USES\nBattery facilities are restricted.\n"
            "Technical equipment is permitted only when formal review is required."
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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zones`

**Exact signature**

```python
def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for zones; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
pd.DataFrame({'planning_zone_id': ['ZONE-U', 'ZONE-UA', 'ZONE-N'], 'source_zone_id': ['SRC-U', 'SRC-UA', 'SRC-N'], 'zone_label_raw': ['U', 'Ua', 'N'], 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256, 'source_layer': 'ZONE'})
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

- direct call: `tests/unit/test_interpret_bess_zoning.py::inputs` via `_zones`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_relations`

**Exact signature**

```python
def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for relations; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
pd.DataFrame([{'parcel_id': parcel_id, 'planning_zone_id': planning_zone_id, 'source_zone_id': source_zone_id, 'zone_label_raw': label, 'relation_type': relation_type, 'intersection_area_m2': area, 'parcel_share_pct': share, 'zone_share_pct': area / 10.0, 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256, 'source_layer': 'ZONE', 'parcel_metric_area_m2': 100.0, 'zone_area_m2': 1000.0} for parcel_id, planning_zone_id, source_zone_id, label, relation_type, area, share in rows])
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

- direct call: `tests/unit/test_interpret_bess_zoning.py::inputs` via `_relations`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_structure_config`

**Exact signature**

```python
def _structure_config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
```

**Purpose**

Private `test` helper for structure config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningRegulationStructureConfig`.
- Every observed return expression is reproduced without truncation:
```python
PlanningRegulationStructureConfig.model_validate({'schema_version': 2, 'structure_profile': 'synthetic_v1', 'document_lock': {'document_id': index.document_id, 'pdf_sha256': index.pdf_sha256, 'pages_content_sha256': index.pages_content_sha256, 'index_content_sha256': index.index_content_sha256, 'normalization_profile': index.search_normalization_profile}, 'document_layout': {'body_start_page': 1, 'table_of_contents_pages': [], 'max_heading_continuation_lines': 0, 'include_table_of_contents_in_topic_evidence': False}, 'heading_patterns': {'zone_chapter': ['^ZONE\\s+(?P<label>[A-Za-z0-9]+)$'], 'article': ['^ARTICLE\\s+(?P<zone>[A-Za-z0-9]+)\\s+(?P<number>\\d+)\\s*-\\s*(?P<title>.*)$'], 'general_section': ['^ARTICLE\\s+(?P<number>\\d+)\\s*-\\s*(?P<title>.*)$'], 'continuation': []}, 'ignored_patterns': {'page_headers': [], 'page_footers': []}, 'zone_aliases': {'Ua': 'U'}, 'topics': {'technical': ['technical equipment']}, 'topic_match_policy': {'boundary_mode': 'token', 'overlap_resolution': 'longest_match'}, 'topic_context_characters': 20})
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

- direct call: `tests/unit/test_interpret_bess_zoning.py::inputs` via `_structure_config`.

**Complete source-ordered implementation**

```python
def _structure_config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
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
                "general_section": [
                    r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"
                ],
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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_parcels`

**Exact signature**

```python
def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
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

- direct call: `tests/unit/test_interpret_bess_zoning.py::inputs` via `_parcels`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy`

**Exact signature**

```python
def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
```

**Purpose**

Private `test` helper for policy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessZoningPolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
BessZoningPolicyConfig.model_validate({'schema_version': 5, 'policy_profile': 'synthetic_policy_v5', 'planning_precheck_scope': 'WRITTEN_ZONING_REGULATION_ONLY', 'review_scope': 'CONFIGURED_USE_CONTROL_ARTICLES_ONLY', 'source_lock': {'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'index_content_sha256': index.index_content_sha256, 'structure_result_content_sha256': structure.structure_result_content_sha256, 'structure_profile': structure.structure_profile}, 'required_zone_article_numbers': ['1', '2'], 'chapters': [{'resolved_zone_chapter_label': 'U', 'review_completeness': 'COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES', 'reviewed_section_ids': [u_article['section_id']], 'review_note': 'The required use-control article was reviewed.', 'zoning_precheck_status': 'CONDITIONAL_REVIEW', 'zoning_precheck_confidence': 'MEDIUM', 'rationale': 'The source states a review condition.', 'missing_information': 'Formal classification and review.', 'evidence': [evidence('E-U-POSITIVE', u_article['section_id'], 2, 'USE_PERMISSION', 'SUPPORTS_POTENTIAL_COMPATIBILITY', u_positive, 'RULE-U-CONDITIONAL', 'Technical equipment is permitted only when formal review is required.', 'This is positive route evidence only.'), evidence('E-U-CONDITION', u_article['section_id'], 2, 'TECHNICAL_EQUIPMENT_RULE', 'CONDITION', u_condition, 'RULE-U-CONDITIONAL', 'Technical equipment is permitted only when formal review is required.', 'This is a condition only.')], 'route_assessments': [{'route_id': 'ROUTE-U-CONDITIONAL', 'route_kind': 'CONDITIONAL_ROUTE', 'positive_evidence_ids': ['E-U-POSITIVE'], 'condition_evidence_ids': ['E-U-CONDITION'], 'difficulty_evidence_ids': [], 'applicability_note': 'The positive route and its condition are assessed together.'}]}, {'resolved_zone_chapter_label': 'N', 'review_completeness': 'COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES', 'reviewed_section_ids': [n_article['section_id']], 'review_note': 'The required use-control article was reviewed.', 'zoning_precheck_status': 'LIKELY_DIFFICULT', 'zoning_precheck_confidence': 'HIGH', 'rationale': 'The source states a relevant restriction.', 'missing_information': 'Formal classification and review.', 'evidence': [evidence('E-N-1', n_article['section_id'], 3, 'USE_RESTRICTION', 'SUPPORTS_DIFFICULTY', n_excerpt, 'RULE-N-RESTRICTION', n_excerpt, 'This is difficulty evidence only.')], 'route_assessments': [{'route_id': 'ROUTE-N-DIFFICULT', 'route_kind': 'DIFFICULTY_ONLY', 'positive_evidence_ids': [], 'condition_evidence_ids': [], 'difficulty_evidence_ids': ['E-N-1'], 'applicability_note': 'The restriction is assessed without a positive route.'}]}]})

{'evidence_id': evidence_id, 'section_id': section_id, 'page_number': page_number, 'evidence_kind': kind, 'evidence_direction': direction, 'exact_raw_excerpt': excerpt, 'excerpt_sha256': sha256(excerpt.encode()).hexdigest(), 'section_page_fragment_sha256': fragment['section_page_fragment_sha256'], 'excerpt_start': start, 'excerpt_end': start + len(excerpt), 'source_rule_id': source_rule_id, 'source_rule_excerpt': source_rule, 'source_rule_sha256': sha256(source_rule.encode()).hexdigest(), 'source_rule_start': rule_start, 'source_rule_end': rule_start + len(source_rule), 'interpretation_note': note}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(excerpt.encode()).hexdigest`, `sha256(source_rule.encode()).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_interpret_bess_zoning.py::inputs` via `_policy`.

**Complete source-ordered implementation**

```python
def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
    sections = structure.sections
    u_article = sections.loc[
        sections["section_type"].eq("ARTICLE")
        & sections["zone_chapter_label"].eq("U")
    ].iloc[0]
    n_article = sections.loc[
        sections["section_type"].eq("ARTICLE")
        & sections["zone_chapter_label"].eq("N")
    ].iloc[0]
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
            "section_page_fragment_sha256": fragment[
                "section_page_fragment_sha256"
            ],
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
                    "reviewed_section_ids": [u_article["section_id"]],
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
                    "reviewed_section_ids": [n_article["section_id"]],
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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy.evidence`

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

**Purpose**

Private `test` helper for evidence; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'evidence_id': evidence_id, 'section_id': section_id, 'page_number': page_number, 'evidence_kind': kind, 'evidence_direction': direction, 'exact_raw_excerpt': excerpt, 'excerpt_sha256': sha256(excerpt.encode()).hexdigest(), 'section_page_fragment_sha256': fragment['section_page_fragment_sha256'], 'excerpt_start': start, 'excerpt_end': start + len(excerpt), 'source_rule_id': source_rule_id, 'source_rule_excerpt': source_rule, 'source_rule_sha256': sha256(source_rule.encode()).hexdigest(), 'source_rule_start': rule_start, 'source_rule_end': rule_start + len(source_rule), 'interpretation_note': note}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(excerpt.encode()).hexdigest`, `sha256(source_rule.encode()).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_interpret_bess_zoning.py::_policy` via `evidence`.

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
            "section_page_fragment_sha256": fragment[
                "section_page_fragment_sha256"
            ],
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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `inputs` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `(index, structure, config, zones, relations, parcels, planning_document, policy)`.
- Tests requesting it by parameter injection: `valid_result`, `_validate`, `test_valid_locked_policy_builds_complete_outputs`, `test_source_lock_mismatch_is_rejected`, `test_missing_and_extra_chapter_are_rejected`, `test_regulation_zone_chapter_labels_and_ids_must_be_unique`, `test_source_complete_validator_rejects_later_duplicate_chapter`, `test_duplicate_chapter_and_evidence_id_are_rejected`, `test_one_excerpt_cannot_be_reused_with_contradictory_directions`, `test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected`, `test_duplicate_occurrence_in_different_compatible_routes_is_rejected`, `test_forbidden_or_invalid_final_status_is_rejected`, `test_invalid_confidence_and_unknown_field_are_rejected`, `test_old_policy_schema_versions_are_rejected`, `test_every_evidence_kind_has_an_explicit_direction_matrix`, `test_valid_exact_evidence_is_preserved`, `test_source_rule_identity_and_containment_are_strict`, `test_same_rule_text_at_distinct_offsets_has_distinct_identity`, `test_absent_excerpt_and_section_page_mismatch_are_rejected`, `test_excerpt_hash_and_length_are_rejected`, `test_declared_status_must_equal_derived_route_status`, `test_condition_alone_cannot_create_conditional_review`, `test_unrelated_positive_and_condition_do_not_create_conditional_review`, `test_unlinked_context_only_unknown_succeeds`, `test_positive_condition_and_conflict_status_routes`, `test_route_references_must_be_same_chapter_and_role_compatible`, `test_route_ids_are_globally_unique`, `test_unlinked_difficulty_evidence_is_rejected`, `test_unlinked_positive_and_condition_evidence_are_rejected`, `test_context_only_evidence_must_be_unlinked`, `test_one_evidence_may_link_to_multiple_compatible_routes`, `test_difficulty_and_positive_only_status_routes`, `test_incomplete_review_requires_unknown_low`, `test_incomplete_review_persists_exact_missing_required_sections`, `test_unknown_is_accepted_when_evidence_is_insufficient`, `test_reviewed_sections_cover_required_articles`, `test_evidence_must_be_inside_reviewed_sections`, `test_review_cannot_claim_another_chapter_section`, `test_general_section_review_is_explicit_and_valid`, `test_same_general_occurrence_may_be_scoped_to_different_chapters`, `test_exact_section_page_occurrence_is_auditable`, `test_repeated_excerpt_occurrence_is_bound_to_policy`, `test_wrong_occurrence_identity_is_rejected`, `test_unmapped_dominant_zone_is_rejected`, `test_context_evidence_is_separate_from_decision_outputs`, `test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved`, `test_inputs_are_not_mutated`, `test_policy_change_after_result_creation_is_rejected`, `test_evidence_change_after_result_creation_is_rejected`, `test_zoning_relation_and_zone_mapping_changes_are_rejected`, `test_structure_config_and_hierarchy_changes_are_rejected`, `test_public_source_complete_validator_is_invoked`, `test_one_precheck_build_performs_one_zoning_source_complete_validation`, `test_invalid_physical_zoning_fails_before_policy_interpretation`, `test_one_build_result_performs_one_factual_structure_rebuild`, `test_relation_area_denominators_are_required`, `test_relation_percentages_must_match_denominators`, `test_factual_zone_mapping_counts_are_recomputed`, `test_coordinated_result_mutation_is_rejected`, `test_coordinated_evidence_catalog_mutation_is_rejected`, `test_coordinated_catalog_occurrence_duplicate_is_rejected`, `test_coordinated_route_table_mutation_is_rejected`, `test_coordinated_evidence_route_link_mutation_is_rejected`, `test_coordinated_reverse_link_mutation_is_rejected`, `test_evidence_route_link_hash_mutation_is_rejected`, `test_old_result_hash_schemas_are_rejected`, `test_relation_identity_change_is_rejected`, `test_readback_result_validates`, `test_policy_yaml_roundtrip_is_strict`.

**Complete fixture implementation**

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

### `valid_result` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `interpret_bess_zoning(*inputs)`.
- Tests requesting it by parameter injection: `test_valid_locked_policy_builds_complete_outputs`, `test_source_complete_validator_rejects_later_duplicate_chapter`, `test_valid_exact_evidence_is_preserved`, `test_exact_section_page_occurrence_is_auditable`, `test_repeated_excerpt_occurrence_is_bound_to_policy`, `test_exact_and_alias_mappings_are_inherited_without_prefix_logic`, `test_link_table_exactly_reproduces_routes_and_reverse_links`, `test_parcel_aggregation_preserves_conflicts_and_touch_only`, `test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved`, `test_policy_change_after_result_creation_is_rejected`, `test_evidence_change_after_result_creation_is_rejected`, `test_zoning_relation_and_zone_mapping_changes_are_rejected`, `test_coordinated_result_mutation_is_rejected`, `test_coordinated_evidence_catalog_mutation_is_rejected`, `test_coordinated_catalog_occurrence_duplicate_is_rejected`, `test_coordinated_route_table_mutation_is_rejected`, `test_coordinated_evidence_route_link_mutation_is_rejected`, `test_coordinated_reverse_link_mutation_is_rejected`, `test_evidence_route_link_hash_mutation_is_rejected`, `test_old_result_hash_schemas_are_rejected`, `test_readback_result_validates`.

**Complete fixture implementation**

```python
def valid_result(inputs):
    return interpret_bess_zoning(*inputs)
```

### `_payload`

**Exact signature**

```python
def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
```

**Purpose**

Private `test` helper for payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
policy.model_dump(mode='python')
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

- direct call: `tests/unit/test_interpret_bess_zoning.py::_policy_with_context_only_evidence` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_source_lock_mismatch_is_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_missing_and_extra_chapter_are_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_duplicate_chapter_and_evidence_id_are_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_one_excerpt_cannot_be_reused_with_contradictory_directions` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_duplicate_occurrence_in_different_compatible_routes_is_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_forbidden_or_invalid_final_status_is_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_invalid_confidence_and_unknown_field_are_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_old_policy_schema_versions_are_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_every_evidence_kind_has_an_explicit_direction_matrix` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_source_rule_identity_and_containment_are_strict` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_same_rule_text_at_distinct_offsets_has_distinct_identity` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_excerpt_hash_and_length_are_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_declared_status_must_equal_derived_route_status` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_condition_alone_cannot_create_conditional_review` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_unrelated_positive_and_condition_do_not_create_conditional_review` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_unlinked_context_only_unknown_succeeds` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_positive_condition_and_conflict_status_routes` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_route_references_must_be_same_chapter_and_role_compatible` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_route_ids_are_globally_unique` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_unlinked_difficulty_evidence_is_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_unlinked_positive_and_condition_evidence_are_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_context_only_evidence_must_be_unlinked` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_one_evidence_may_link_to_multiple_compatible_routes` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_difficulty_and_positive_only_status_routes` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_incomplete_review_requires_unknown_low` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_incomplete_review_persists_exact_missing_required_sections` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_unknown_is_accepted_when_evidence_is_insufficient` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_reviewed_sections_cover_required_articles` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_evidence_must_be_inside_reviewed_sections` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_review_cannot_claim_another_chapter_section` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_general_section_review_is_explicit_and_valid` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_wrong_occurrence_identity_is_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_policy_change_after_result_creation_is_rejected` via `_payload`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_evidence_change_after_result_creation_is_rejected` via `_payload`.

**Complete source-ordered implementation**

```python
def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
    return policy.model_dump(mode="python")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy_with_context_only_evidence`

**Exact signature**

```python
def _policy_with_context_only_evidence(
    policy: BessZoningPolicyConfig,
) -> BessZoningPolicyConfig:
```

**Purpose**

Private `test` helper for policy with context only evidence; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessZoningPolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
BessZoningPolicyConfig.model_validate(payload)
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
- In-memory mutation: `chapter['evidence'][1]['evidence_direction']`, `chapter['zoning_precheck_status']`, `route['condition_evidence_ids']`, `route['route_kind']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_interpret_bess_zoning.py::test_context_only_evidence_must_be_unlinked` via `_policy_with_context_only_evidence`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_context_evidence_is_separate_from_decision_outputs` via `_policy_with_context_only_evidence`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_validate`

**Exact signature**

```python
def _validate(inputs, result) -> None:
```

**Purpose**

Rejects malformed or inconsistent validate; exact branches, calls, and return construction are reproduced below.

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

- direct call: `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_repeated_excerpt_occurrence_is_bound_to_policy` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_result_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_catalog_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_route_table_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_route_link_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_reverse_link_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_evidence_route_link_hash_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_old_result_hash_schemas_are_rejected` via `_validate`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_readback_result_validates` via `_validate`.

**Complete source-ordered implementation**

```python
def _validate(inputs, result) -> None:
    validate_bess_zoning_precheck(*inputs, result)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_package_exports_precheck_api`

**Purpose**

Exercises `package exports precheck api`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `package exports precheck api` through the exact asserted conditions: `name in stages.__all__`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_valid_locked_policy_builds_complete_outputs`

**Purpose**

Exercises `valid locked policy builds complete outputs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, _, zones, relations, parcels, _, policy = inputs
result = valid_result
_validate(inputs, result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS
assert tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS
assert tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS
assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS
assert tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS
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
assert result.structure_result_content_sha256 == structure.structure_result_content_sha256
assert result.zoning_relation_hash_columns == tuple(relations.columns)
assert set(result.source_zone_policy["source_zone_label_raw"]) == set(
        zones["zone_label_raw"]
    )
assert result.policy_profile == policy.policy_profile
```

**Regression protected**

Locks `valid locked policy builds complete outputs` through the exact asserted conditions: `tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS`; `tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS`; `tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS`; `tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS`; plus 19 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
    index, structure, _, zones, relations, parcels, _, policy = inputs
    result = valid_result
    _validate(inputs, result)
    assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS
    assert tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS
    assert tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS
    assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS
    assert tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS
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
    assert result.structure_result_content_sha256 == structure.structure_result_content_sha256
    assert result.zoning_relation_hash_columns == tuple(relations.columns)
    assert set(result.source_zone_policy["source_zone_label_raw"]) == set(
        zones["zone_label_raw"]
    )
    assert result.policy_profile == policy.policy_profile
```

### `test_source_lock_mismatch_is_rejected`

**Purpose**

Exercises `source lock mismatch is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
*sources, policy = inputs
payload = _payload(policy)
payload["source_lock"][field] = "f" * 64 if "sha256" in field else "wrong"
bad = BessZoningPolicyConfig.model_validate(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="differs from factual source"):
        interpret_bess_zoning(*sources, bad)
```

**Regression protected**

Locks `source lock mismatch is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["source_lock"][field] = "f" * 64 if "sha256" in field else "wrong"
    bad = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="differs from factual source"):
        interpret_bess_zoning(*sources, bad)
```

### `test_missing_and_extra_chapter_are_rejected`

**Purpose**

Exercises `missing and extra chapter are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
missing_payload = _payload(policy)
missing_payload["chapters"] = missing_payload["chapters"][:-1]
extra_payload = _payload(policy)
extra = dict(extra_payload["chapters"][0])
extra["resolved_zone_chapter_label"] = "EXTRA"
extra["evidence"] = []
extra["route_assessments"] = []
extra["zoning_precheck_status"] = "UNKNOWN"
extra_payload["chapters"] = (*extra_payload["chapters"], extra)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="completeness differs"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(missing_payload))
with pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(extra_payload))
```

**Regression protected**

Locks `missing and extra chapter are rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
    *sources, policy = inputs
    missing_payload = _payload(policy)
    missing_payload["chapters"] = missing_payload["chapters"][:-1]
    with pytest.raises(BessZoningPrecheckError, match="completeness differs"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(missing_payload))
    extra_payload = _payload(policy)
    extra = dict(extra_payload["chapters"][0])
    extra["resolved_zone_chapter_label"] = "EXTRA"
    extra["evidence"] = []
    extra["route_assessments"] = []
    extra["zoning_precheck_status"] = "UNKNOWN"
    extra_payload["chapters"] = (*extra_payload["chapters"], extra)
    with pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(extra_payload))
```

### `test_regulation_zone_chapter_labels_and_ids_must_be_unique`

**Purpose**

Exercises `regulation zone chapter labels and ids must be unique`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
structure = inputs[1]
used = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U")
    ].iloc[0].copy()
used["section_id"] = "SECTION-DUPLICATE-U"
duplicated_used = replace(
        structure,
        sections=pd.concat(
            [structure.sections, used.to_frame().T], ignore_index=True
        ),
    )
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(interpret_module._zone_chapter_rows(structure)) == 2
with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_used)
with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_unused)
with pytest.raises(BessZoningPrecheckError, match="section IDs must be unique"):
        interpret_module._zone_chapter_rows(duplicated_section_id)
```

**Regression protected**

Locks `regulation zone chapter labels and ids must be unique`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_regulation_zone_chapter_labels_and_ids_must_be_unique(inputs) -> None:
    structure = inputs[1]
    assert len(interpret_module._zone_chapter_rows(structure)) == 2

    used = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U")
    ].iloc[0].copy()
    used["section_id"] = "SECTION-DUPLICATE-U"
    duplicated_used = replace(
        structure,
        sections=pd.concat(
            [structure.sections, used.to_frame().T], ignore_index=True
        ),
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

### `test_source_complete_validator_rejects_later_duplicate_chapter`

**Purpose**

Exercises `source complete validator rejects later duplicate chapter`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
duplicate = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
    ].iloc[0].copy()
duplicate["section_id"] = "SECTION-LATE-DUPLICATE"
changed = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate.to_frame().T], ignore_index=True
        ),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_complete_validator_rejects_later_duplicate_chapter(
    inputs, valid_result
) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
    duplicate = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
    ].iloc[0].copy()
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

### `test_duplicate_chapter_and_evidence_id_are_rejected`

**Purpose**

Exercises `duplicate chapter and evidence id are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
policy = inputs[-1]
chapter_payload = _payload(policy)
chapter_payload["chapters"] = (
        *chapter_payload["chapters"],
        chapter_payload["chapters"][0],
    )
evidence_payload = _payload(policy)
evidence_payload["chapters"][1]["evidence"][0]["evidence_id"] = "E-U-POSITIVE"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="chapter policy labels must be unique"):
        BessZoningPolicyConfig.model_validate(chapter_payload)
with pytest.raises(ValueError, match="evidence IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(evidence_payload)
```

**Regression protected**

Locks `duplicate chapter and evidence id are rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_one_excerpt_cannot_be_reused_with_contradictory_directions`

**Purpose**

Exercises `one excerpt cannot be reused with contradictory directions`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
first = dict(payload["chapters"][0]["evidence"][1])
second = dict(first)
first["evidence_direction"] = "SUPPORTS_POTENTIAL_COMPATIBILITY"
second["evidence_id"] = "E-U-2"
second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
payload["chapters"][0]["evidence"] = (first, second)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `one excerpt cannot be reused with contradictory directions`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected`

**Purpose**

Exercises `duplicate chapter scoped occurrence in one route is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
duplicate = dict(payload["chapters"][0]["evidence"][0])
duplicate["evidence_id"] = "E-U-POSITIVE-DUPLICATE"
payload["chapters"][0]["evidence"] = (
        *payload["chapters"][0]["evidence"],
        duplicate,
    )
payload["chapters"][0]["route_assessments"][0][
        "positive_evidence_ids"
    ] = ["E-U-POSITIVE", "E-U-POSITIVE-DUPLICATE"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `duplicate chapter scoped occurrence in one route is rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    duplicate = dict(payload["chapters"][0]["evidence"][0])
    duplicate["evidence_id"] = "E-U-POSITIVE-DUPLICATE"
    payload["chapters"][0]["evidence"] = (
        *payload["chapters"][0]["evidence"],
        duplicate,
    )
    payload["chapters"][0]["route_assessments"][0][
        "positive_evidence_ids"
    ] = ["E-U-POSITIVE", "E-U-POSITIVE-DUPLICATE"]

    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)
```

### `test_duplicate_occurrence_in_different_compatible_routes_is_rejected`

**Purpose**

Exercises `duplicate occurrence in different compatible routes is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `duplicate occurrence in different compatible routes is rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_forbidden_or_invalid_final_status_is_rejected`

**Purpose**

Exercises `forbidden or invalid final status is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
payload = _payload(inputs[-1])
payload["chapters"][0]["zoning_precheck_status"] = status
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `forbidden or invalid final status is rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

### `test_invalid_confidence_and_unknown_field_are_rejected`

**Purpose**

Exercises `invalid confidence and unknown field are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
payload["chapters"][0]["zoning_precheck_confidence"] = "CERTAIN"
payload = _payload(inputs[-1])
payload["automatic_classifier"] = True
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `invalid confidence and unknown field are rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_duplicate_yaml_key_is_rejected`

**Purpose**

Exercises `duplicate yaml key is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "duplicate.yaml"
path.write_text(
        "schema_version: 2\nschema_version: 2\n",
        encoding="utf-8",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="Duplicate YAML policy key"):
        load_bess_zoning_policy_config(path)
```

**Regression protected**

Locks `duplicate yaml key is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text(
        "schema_version: 2\nschema_version: 2\n",
        encoding="utf-8",
    )
    with pytest.raises(BessZoningPrecheckError, match="Duplicate YAML policy key"):
        load_bess_zoning_policy_config(path)
```

### `test_old_policy_schema_versions_are_rejected`

**Purpose**

Exercises `old policy schema versions are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `version`.

**Setup**

```python
payload = _payload(inputs[-1])
payload["schema_version"] = version
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="unsupported BESS zoning policy schema"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `old policy schema versions are rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_old_policy_schema_versions_are_rejected(inputs, version: int) -> None:
    payload = _payload(inputs[-1])
    payload["schema_version"] = version
    with pytest.raises(ValueError, match="unsupported BESS zoning policy schema"):
        BessZoningPolicyConfig.model_validate(payload)
```

### `test_every_evidence_kind_has_an_explicit_direction_matrix`

**Purpose**

Exercises `every evidence kind has an explicit direction matrix`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Prevents unresolved ICPE applicability evidence from being treated as a decision-linked BESS condition or legal conclusion.

**Test boundary**

- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_valid_exact_evidence_is_preserved`

**Purpose**

Exercises `valid exact evidence is preserved`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
policy = inputs[-1]
excerpt = policy.chapters[0].evidence[0].exact_raw_excerpt
row = valid_result.evidence_catalog.set_index("evidence_id").loc[
        "E-U-POSITIVE"
    ]
relative_start = row["excerpt_start"] - row["source_rule_start"]
relative_end = row["excerpt_end"] - row["source_rule_start"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert excerpt == "Technical equipment is permitted"
assert policy.chapters[0].evidence[0].excerpt_sha256 == sha256(
        excerpt.encode()
    ).hexdigest()
assert valid_result.chapter_policy.iloc[0]["evidence_ids"] == (
        "E-U-POSITIVE",
        "E-U-CONDITION",
    )
assert "only when" in row["source_rule_excerpt"]
assert row["source_rule_excerpt"][relative_start:relative_end] == excerpt
```

**Regression protected**

Locks `valid exact evidence is preserved` through the exact asserted conditions: `excerpt == 'Technical equipment is permitted'`; `policy.chapters[0].evidence[0].excerpt_sha256 == sha256(excerpt.encode()).hexdigest()`; `valid_result.chapter_policy.iloc[0]['evidence_ids'] == ('E-U-POSITIVE', 'E-U-CONDITION')`; `'only when' in row['source_rule_excerpt']`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
    policy = inputs[-1]
    excerpt = policy.chapters[0].evidence[0].exact_raw_excerpt
    assert excerpt == "Technical equipment is permitted"
    assert policy.chapters[0].evidence[0].excerpt_sha256 == sha256(
        excerpt.encode()
    ).hexdigest()
    assert valid_result.chapter_policy.iloc[0]["evidence_ids"] == (
        "E-U-POSITIVE",
        "E-U-CONDITION",
    )
    row = valid_result.evidence_catalog.set_index("evidence_id").loc[
        "E-U-POSITIVE"
    ]
    assert "only when" in row["source_rule_excerpt"]
    relative_start = row["excerpt_start"] - row["source_rule_start"]
    relative_end = row["excerpt_end"] - row["source_rule_start"]
    assert row["source_rule_excerpt"][relative_start:relative_end] == excerpt
```

### `test_source_rule_identity_and_containment_are_strict`

**Purpose**

Exercises `source rule identity and containment are strict`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
*sources, policy = inputs
payload = _payload(policy)
evidence = payload["chapters"][0]["evidence"][0]
for related in payload["chapters"][0]["evidence"]:
        if mutation == "start":
            related["source_rule_start"] -= 1
        else:
            related["source_rule_end"] += 1
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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
with pytest.raises(BessZoningPrecheckError, match="source-rule offsets"):
        interpret_bess_zoning(
            *sources,
            BessZoningPolicyConfig.model_validate(payload),
        )
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_same_rule_text_at_distinct_offsets_has_distinct_identity`

**Purpose**

Exercises `same rule text at distinct offsets has distinct identity`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert policy.chapters[0].evidence[-1].evidence_direction == "SUPPORTS_DIFFICULTY"
```

**Regression protected**

Locks `same rule text at distinct offsets has distinct identity` through the exact asserted conditions: `policy.chapters[0].evidence[-1].evidence_direction == 'SUPPORTS_DIFFICULTY'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_real_muret_source_rules_preserve_conditional_and_exception_frames`

**Purpose**

Exercises `real muret source rules preserve conditional and exception frames`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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

**Action**

```python
policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `real muret source rules preserve conditional and exception frames` through the exact asserted conditions: `'ne sont autorisées qu’à' in positive.source_rule_excerpt`; `'condition' in positive.source_rule_excerpt`; `positive.source_rule_excerpt.startswith('Toutes constructions')`; `'autres que celles' in positive.source_rule_excerpt`; plus 3 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_real_muret_up_route_does_not_use_the_separate_icpe_condition`

**Purpose**

Exercises `real muret up route does not use the separate icpe condition`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "UP"
    )
route = chapter.route_assessments[0]
restriction = next(
        evidence
        for evidence in chapter.evidence
        if evidence.evidence_id == "MURET-UP-RESTRICTION-01"
    )
```

**Action**

```python
policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
```

**Expected result**

```python
assert policy.schema_version == 5
assert policy.policy_profile == "muret_bess_written_zoning_v6"
assert route.route_kind == "RESTRICTION_EXCEPTION_ROUTE"
assert route.positive_evidence_ids == ("MURET-UP-PUBLIC-ROUTE-01",)
assert route.condition_evidence_ids == ()
assert route.difficulty_evidence_ids == ("MURET-UP-RESTRICTION-01",)
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

**Regression protected**

Prevents unresolved ICPE applicability evidence from being treated as a decision-linked BESS condition or legal conclusion.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite`

**Purpose**

Exercises `real muret aup route uses the general infrastructure prerequisite`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "AUp"
    )
route = chapter.route_assessments[0]
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
```

**Action**

```python
policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
```

**Expected result**

```python
assert route.route_kind == "CONDITIONAL_ROUTE"
assert route.positive_evidence_ids == ("MURET-AUP-PUBLIC-ROUTE-01",)
assert route.condition_evidence_ids == (
        "MURET-AUP-INFRASTRUCTURE-CONDITION-01",
    )
assert route.difficulty_evidence_ids == ()
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

**Regression protected**

Locks `real muret aup route uses the general infrastructure prerequisite` through the exact asserted conditions: `route.route_kind == 'CONDITIONAL_ROUTE'`; `route.positive_evidence_ids == ('MURET-AUP-PUBLIC-ROUTE-01',)`; `route.condition_evidence_ids == ('MURET-AUP-INFRASTRUCTURE-CONDITION-01',)`; `route.difficulty_evidence_ids == ()`; plus 14 additional reproduced assertion(s).

**Test boundary**

- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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
    assert route.condition_evidence_ids == (
        "MURET-AUP-INFRASTRUCTURE-CONDITION-01",
    )
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

### `test_real_muret_up_and_aup_keep_icpe_applicability_as_context`

**Purpose**

Exercises `real muret up and aup keep icpe applicability as context`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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

**Action**

```python
policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents unresolved ICPE applicability evidence from being treated as a decision-linked BESS condition or legal conclusion.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_absent_excerpt_and_section_page_mismatch_are_rejected`

**Purpose**

Exercises `absent excerpt and section page mismatch are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
payload = _payload(policy)
excerpt = "Not present in the indexed source."
payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
payload = _payload(policy)
for evidence in payload["chapters"][0]["evidence"]:
        evidence["page_number"] = 3
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="offsets"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
with pytest.raises(BessZoningPrecheckError, match="section/page fragment"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
```

**Regression protected**

Locks `absent excerpt and section page mismatch are rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_excerpt_hash_and_length_are_rejected`

**Purpose**

Exercises `excerpt hash and length are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = "f" * 64
payload = _payload(inputs[-1])
excerpt = "x" * 601
payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="excerpt SHA256 differs"):
        BessZoningPolicyConfig.model_validate(payload)
with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `excerpt hash and length are rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_declared_status_must_equal_derived_route_status`

**Purpose**

Exercises `declared status must equal derived route status`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
payload = _payload(inputs[-1])
payload["chapters"][0]["zoning_precheck_status"] = status
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="differs from coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `declared status must equal derived route status`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_declared_status_must_equal_derived_route_status(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError, match="differs from coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

### `test_condition_alone_cannot_create_conditional_review`

**Purpose**

Exercises `condition alone cannot create conditional review`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
payload["chapters"][0]["evidence"] = [
        payload["chapters"][0]["evidence"][1]
    ]
payload["chapters"][0]["route_assessments"] = []
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `condition alone cannot create conditional review`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    payload["chapters"][0]["evidence"] = [
        payload["chapters"][0]["evidence"][1]
    ]
    payload["chapters"][0]["route_assessments"] = []
    with pytest.raises(ValueError, match="coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

### `test_unrelated_positive_and_condition_do_not_create_conditional_review`

**Purpose**

Exercises `unrelated positive and condition do not create conditional review`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="coherent|linked route"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `unrelated positive and condition do not create conditional review`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_unlinked_context_only_unknown_succeeds`

**Purpose**

Exercises `unlinked context only unknown succeeds`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
chapter = payload["chapters"][0]
chapter["zoning_precheck_status"] = "UNKNOWN"
chapter["zoning_precheck_confidence"] = "LOW"
chapter["evidence"] = [chapter["evidence"][1]]
chapter["evidence"][0]["evidence_direction"] = "CONTEXT_ONLY"
chapter["route_assessments"] = []
policy = BessZoningPolicyConfig.model_validate(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert policy.chapters[0].zoning_precheck_status == "UNKNOWN"
```

**Regression protected**

Locks `unlinked context only unknown succeeds` through the exact asserted conditions: `policy.chapters[0].zoning_precheck_status == 'UNKNOWN'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_positive_condition_and_conflict_status_routes`

**Purpose**

Exercises `positive condition and conflict status routes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
conflict = _payload(inputs[-1])
conflict["chapters"][0]["evidence"][1][
        "evidence_direction"
    ] = "SUPPORTS_DIFFICULTY"
route = conflict["chapters"][0]["route_assessments"][0]
route["route_kind"] = "RESTRICTION_EXCEPTION_ROUTE"
route["condition_evidence_ids"] = []
route["difficulty_evidence_ids"] = ["E-U-CONDITION"]
policy = BessZoningPolicyConfig.model_validate(conflict)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert BessZoningPolicyConfig.model_validate(payload).chapters[
        0
    ].zoning_precheck_status == "CONDITIONAL_REVIEW"
assert policy.chapters[0].zoning_precheck_status == "CONDITIONAL_REVIEW"
```

**Regression protected**

Locks `positive condition and conflict status routes` through the exact asserted conditions: `BessZoningPolicyConfig.model_validate(payload).chapters[0].zoning_precheck_status == 'CONDITIONAL_REVIEW'`; `policy.chapters[0].zoning_precheck_status == 'CONDITIONAL_REVIEW'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_positive_condition_and_conflict_status_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    assert BessZoningPolicyConfig.model_validate(payload).chapters[
        0
    ].zoning_precheck_status == "CONDITIONAL_REVIEW"
    conflict = _payload(inputs[-1])
    conflict["chapters"][0]["evidence"][1][
        "evidence_direction"
    ] = "SUPPORTS_DIFFICULTY"
    route = conflict["chapters"][0]["route_assessments"][0]
    route["route_kind"] = "RESTRICTION_EXCEPTION_ROUTE"
    route["condition_evidence_ids"] = []
    route["difficulty_evidence_ids"] = ["E-U-CONDITION"]
    policy = BessZoningPolicyConfig.model_validate(conflict)
    assert policy.chapters[0].zoning_precheck_status == "CONDITIONAL_REVIEW"
```

### `test_route_references_must_be_same_chapter_and_role_compatible`

**Purpose**

Exercises `route references must be same chapter and role compatible`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
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
            payload["chapters"][0]["zoning_precheck_status"] = (
                "POTENTIALLY_COMPATIBLE"
            )
        with pytest.raises(ValueError, match=message):
            BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `route references must be same chapter and role compatible`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
            payload["chapters"][0]["zoning_precheck_status"] = (
                "POTENTIALLY_COMPATIBLE"
            )
        with pytest.raises(ValueError, match=message):
            BessZoningPolicyConfig.model_validate(payload)
```

### `test_route_ids_are_globally_unique`

**Purpose**

Exercises `route ids are globally unique`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
payload["chapters"][1]["route_assessments"][0]["route_id"] = (
        payload["chapters"][0]["route_assessments"][0]["route_id"]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="route IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `route ids are globally unique`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_route_ids_are_globally_unique(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][1]["route_assessments"][0]["route_id"] = (
        payload["chapters"][0]["route_assessments"][0]["route_id"]
    )
    with pytest.raises(ValueError, match="route IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(payload)
```

### `test_unlinked_difficulty_evidence_is_rejected`

**Purpose**

Exercises `unlinked difficulty evidence is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="decision evidence must be linked"):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `unlinked difficulty evidence is rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_unlinked_positive_and_condition_evidence_are_rejected`

**Purpose**

Exercises `unlinked positive and condition evidence are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
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

**Regression protected**

Locks `unlinked positive and condition evidence are rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_context_only_evidence_must_be_unlinked`

**Purpose**

Exercises `context only evidence must be unlinked`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
policy = _policy_with_context_only_evidence(inputs[-1])
payload = _payload(policy)
payload["chapters"][0]["route_assessments"][0][
        "condition_evidence_ids"
    ] = ["E-U-CONDITION"]
payload["chapters"][0]["route_assessments"][0][
        "route_kind"
    ] = "CONDITIONAL_ROUTE"
payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert policy.chapters[0].evidence[1].evidence_direction == "CONTEXT_ONLY"
with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

**Regression protected**

Locks `context only evidence must be unlinked`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_context_only_evidence_must_be_unlinked(inputs) -> None:
    policy = _policy_with_context_only_evidence(inputs[-1])
    assert policy.chapters[0].evidence[1].evidence_direction == "CONTEXT_ONLY"

    payload = _payload(policy)
    payload["chapters"][0]["route_assessments"][0][
        "condition_evidence_ids"
    ] = ["E-U-CONDITION"]
    payload["chapters"][0]["route_assessments"][0][
        "route_kind"
    ] = "CONDITIONAL_ROUTE"
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
```

### `test_one_evidence_may_link_to_multiple_compatible_routes`

**Purpose**

Exercises `one evidence may link to multiple compatible routes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
route = dict(payload["chapters"][1]["route_assessments"][0])
route["route_id"] = "ROUTE-N-DIFFICULT-SECOND"
payload["chapters"][1]["route_assessments"] = (
        *payload["chapters"][1]["route_assessments"],
        route,
    )
policy = BessZoningPolicyConfig.model_validate(payload)
*sources, _ = inputs
evidence = result.evidence_catalog.set_index("evidence_id").loc["E-N-1"]
```

**Action**

```python
result = interpret_bess_zoning(*sources, policy)
```

**Expected result**

```python
assert evidence["linked_route_ids"] == (
        "ROUTE-N-DIFFICULT",
        "ROUTE-N-DIFFICULT-SECOND",
    )
assert evidence["linked_route_roles"] == ("DIFFICULTY", "DIFFICULTY")
```

**Regression protected**

Locks `one evidence may link to multiple compatible routes` through the exact asserted conditions: `evidence['linked_route_ids'] == ('ROUTE-N-DIFFICULT', 'ROUTE-N-DIFFICULT-SECOND')`; `evidence['linked_route_roles'] == ('DIFFICULTY', 'DIFFICULTY')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_difficulty_and_positive_only_status_routes`

**Purpose**

Exercises `difficulty and positive only status routes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert BessZoningPolicyConfig.model_validate(difficult).chapters[
        0
    ].zoning_precheck_status == "LIKELY_DIFFICULT"
assert BessZoningPolicyConfig.model_validate(potential).chapters[
        0
    ].zoning_precheck_status == "POTENTIALLY_COMPATIBLE"
```

**Regression protected**

Locks `difficulty and positive only status routes` through the exact asserted conditions: `BessZoningPolicyConfig.model_validate(difficult).chapters[0].zoning_precheck_status == 'LIKELY_DIFFICULT'`; `BessZoningPolicyConfig.model_validate(potential).chapters[0].zoning_precheck_status == 'POTENTIALLY_COMPATIBLE'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
    assert BessZoningPolicyConfig.model_validate(difficult).chapters[
        0
    ].zoning_precheck_status == "LIKELY_DIFFICULT"
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
    assert BessZoningPolicyConfig.model_validate(potential).chapters[
        0
    ].zoning_precheck_status == "POTENTIALLY_COMPATIBLE"
```

### `test_incomplete_review_requires_unknown_low`

**Purpose**

Exercises `incomplete review requires unknown low`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
chapter = payload["chapters"][0]
chapter["review_completeness"] = "INCOMPLETE"
chapter["zoning_precheck_status"] = "UNKNOWN"
chapter["zoning_precheck_confidence"] = "LOW"
chapter["evidence"] = []
chapter["route_assessments"] = []
chapter["reviewed_section_ids"] = []
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert BessZoningPolicyConfig.model_validate(payload).chapters[
        0
    ].review_completeness == "INCOMPLETE"
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

**Regression protected**

Locks `incomplete review requires unknown low`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
    assert BessZoningPolicyConfig.model_validate(payload).chapters[
        0
    ].review_completeness == "INCOMPLETE"
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

### `test_incomplete_review_persists_exact_missing_required_sections`

**Purpose**

Exercises `incomplete review persists exact missing required sections`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
payload = _payload(policy)
chapter = payload["chapters"][0]
chapter["review_completeness"] = "INCOMPLETE"
chapter["reviewed_section_ids"] = []
chapter["zoning_precheck_status"] = "UNKNOWN"
chapter["zoning_precheck_confidence"] = "LOW"
chapter["evidence"] = []
chapter["route_assessments"] = []
row = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
```

**Action**

```python
result = interpret_bess_zoning(
        *sources,
        BessZoningPolicyConfig.model_validate(payload),
    )
```

**Expected result**

```python
assert row["reviewed_section_ids"] == ()
assert row["missing_required_section_ids"] == ("SECTION-0003",)
assert row["zoning_precheck_status"] == "UNKNOWN"
assert row["zoning_precheck_confidence"] == "LOW"
```

**Regression protected**

Locks `incomplete review persists exact missing required sections` through the exact asserted conditions: `row['reviewed_section_ids'] == ()`; `row['missing_required_section_ids'] == ('SECTION-0003',)`; `row['zoning_precheck_status'] == 'UNKNOWN'`; `row['zoning_precheck_confidence'] == 'LOW'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
    assert row["missing_required_section_ids"] == ("SECTION-0003",)
    assert row["zoning_precheck_status"] == "UNKNOWN"
    assert row["zoning_precheck_confidence"] == "LOW"
```

### `test_unknown_is_accepted_when_evidence_is_insufficient`

**Purpose**

Exercises `unknown is accepted when evidence is insufficient`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
payload = _payload(policy)
payload["chapters"][0]["zoning_precheck_status"] = "UNKNOWN"
payload["chapters"][0]["evidence"] = []
payload["chapters"][0]["route_assessments"] = []
```

**Action**

```python
result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
```

**Expected result**

```python
assert result.chapter_policy.iloc[0]["zoning_precheck_status"] == "UNKNOWN"
```

**Regression protected**

Locks `unknown is accepted when evidence is insufficient` through the exact asserted conditions: `result.chapter_policy.iloc[0]['zoning_precheck_status'] == 'UNKNOWN'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_reviewed_sections_cover_required_articles`

**Purpose**

Exercises `reviewed sections cover required articles`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
index, structure = inputs[:2]
payload = _payload(policy)
chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="omits required reviewed"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
assert index.document_id == "doc-1"
```

**Regression protected**

Locks `reviewed sections cover required articles`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
    assert index.document_id == "doc-1"
```

### `test_evidence_must_be_inside_reviewed_sections`

**Purpose**

Exercises `evidence must be inside reviewed sections`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
structure = inputs[1]
payload = _payload(policy)
payload["required_zone_article_numbers"] = ["2"]
chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="outside reviewed sections"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
```

**Regression protected**

Locks `evidence must be inside reviewed sections`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
    with pytest.raises(BessZoningPrecheckError, match="outside reviewed sections"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
```

### `test_review_cannot_claim_another_chapter_section`

**Purpose**

Exercises `review cannot claim another chapter section`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
structure = inputs[1]
payload = _payload(policy)
n_article = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
payload["chapters"][0]["reviewed_section_ids"] += (n_article,)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="another chapter"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
```

**Regression protected**

Locks `review cannot claim another chapter section`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
```

### `test_general_section_review_is_explicit_and_valid`

**Purpose**

Exercises `general section review is explicit and valid`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
structure = inputs[1]
payload = _payload(policy)
general_id = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL"), "section_id"
    ].iloc[0]
payload["chapters"][0]["reviewed_section_ids"] += (general_id,)
reviewed = result.chapter_policy.set_index("resolved_zone_chapter_label").loc[
        "U", "reviewed_section_ids"
    ]
```

**Action**

```python
result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
```

**Expected result**

```python
assert general_id in reviewed
```

**Regression protected**

Locks `general section review is explicit and valid` through the exact asserted conditions: `general_id in reviewed`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_same_general_occurrence_may_be_scoped_to_different_chapters`

**Purpose**

Exercises `same general occurrence may be scoped to different chapters`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
general = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL")
    ].iloc[0]
excerpt = "General factual text."
start = fragment["raw_text"].index(excerpt)
base = {
        "section_id": general["section_id"],
        "page_number": 1,
        "evidence_kind": "TECHNICAL_EQUIPMENT_RULE",
        "evidence_direction": "CONTEXT_ONLY",
        "exact_raw_excerpt": excerpt,
        "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
        "section_page_fragment_sha256": fragment[
            "section_page_fragment_sha256"
        ],
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
scoped = result.evidence_catalog.loc[
        result.evidence_catalog["section_id"].eq(general["section_id"])
        & result.evidence_catalog["excerpt_start"].eq(start)
    ]
```

**Action**

```python
fragment = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"]).loc[(general["section_id"], 1)]
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
```

**Expected result**

```python
assert set(scoped["resolved_zone_chapter_label"]) == {"U", "N"}
assert len(scoped) == 2
```

**Regression protected**

Locks `same general occurrence may be scoped to different chapters` through the exact asserted conditions: `set(scoped['resolved_zone_chapter_label']) == {'U', 'N'}`; `len(scoped) == 2`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_same_general_occurrence_may_be_scoped_to_different_chapters(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
    general = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL")
    ].iloc[0]
    fragment = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"]).loc[(general["section_id"], 1)]
    excerpt = "General factual text."
    start = fragment["raw_text"].index(excerpt)
    base = {
        "section_id": general["section_id"],
        "page_number": 1,
        "evidence_kind": "TECHNICAL_EQUIPMENT_RULE",
        "evidence_direction": "CONTEXT_ONLY",
        "exact_raw_excerpt": excerpt,
        "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
        "section_page_fragment_sha256": fragment[
            "section_page_fragment_sha256"
        ],
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

### `test_exact_section_page_occurrence_is_auditable`

**Purpose**

Exercises `exact section page occurrence is auditable`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, *_ = inputs
for row in valid_result.evidence_catalog.to_dict("records"):
        fragment = fragments.loc[(row["section_id"], row["page_number"])]
        assert row["section_page_fragment_sha256"] == fragment[
            "section_page_fragment_sha256"
        ]
        assert fragment["raw_text"][row["excerpt_start"] : row["excerpt_end"]] == row[
            "exact_raw_excerpt"
        ]
```

**Action**

```python
fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `exact section page occurrence is auditable` through the exact asserted conditions: `row['section_page_fragment_sha256'] == fragment['section_page_fragment_sha256']`; `fragment['raw_text'][row['excerpt_start']:row['excerpt_end']] == row['exact_raw_excerpt']`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    for row in valid_result.evidence_catalog.to_dict("records"):
        fragment = fragments.loc[(row["section_id"], row["page_number"])]
        assert row["section_page_fragment_sha256"] == fragment[
            "section_page_fragment_sha256"
        ]
        assert fragment["raw_text"][row["excerpt_start"] : row["excerpt_end"]] == row[
            "exact_raw_excerpt"
        ]
```

### `test_repeated_excerpt_occurrence_is_bound_to_policy`

**Purpose**

Exercises `repeated excerpt occurrence is bound to policy`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, *_ = inputs
row_index = valid_result.evidence_catalog.index[
        valid_result.evidence_catalog["evidence_id"].eq("E-U-POSITIVE")
    ][0]
row = valid_result.evidence_catalog.loc[row_index]
raw = fragments.loc[(row["section_id"], row["page_number"]), "raw_text"]
first = raw.index(row["exact_raw_excerpt"])
second = raw.index(row["exact_raw_excerpt"], first + 1)
catalog = valid_result.evidence_catalog.copy(deep=True)
catalog.loc[row_index, "excerpt_start"] = second
catalog.loc[row_index, "excerpt_end"] = second + len(row["exact_raw_excerpt"])
```

**Action**

```python
fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
coordinated = _result_with_hashes(
        replace(valid_result, evidence_catalog=catalog)
    )
```

**Expected result**

```python
assert second > first
with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, coordinated)
```

**Regression protected**

Locks `repeated excerpt occurrence is bound to policy`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
    coordinated = _result_with_hashes(
        replace(valid_result, evidence_catalog=catalog)
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, coordinated)
```

### `test_wrong_occurrence_identity_is_rejected`

**Purpose**

Exercises `wrong occurrence identity is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="fragment|offset"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
```

### `test_exact_and_alias_mappings_are_inherited_without_prefix_logic`

**Purpose**

Exercises `exact and alias mappings are inherited without prefix logic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
policies = valid_result.source_zone_policy.set_index("source_zone_label_raw")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert policies.loc["U", "mapping_status"] == "EXACT"
assert policies.loc["Ua", "mapping_status"] == "CONFIG_ALIAS"
assert policies.loc["Ua", "resolved_zone_chapter_label"] == "U"
assert policies.loc["Ua", "zoning_precheck_status"] == policies.loc[
        "U", "zoning_precheck_status"
    ]
```

**Regression protected**

Locks `exact and alias mappings are inherited without prefix logic` through the exact asserted conditions: `policies.loc['U', 'mapping_status'] == 'EXACT'`; `policies.loc['Ua', 'mapping_status'] == 'CONFIG_ALIAS'`; `policies.loc['Ua', 'resolved_zone_chapter_label'] == 'U'`; `policies.loc['Ua', 'zoning_precheck_status'] == policies.loc['U', 'zoning_precheck_status']`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(valid_result) -> None:
    policies = valid_result.source_zone_policy.set_index("source_zone_label_raw")
    assert policies.loc["U", "mapping_status"] == "EXACT"
    assert policies.loc["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert policies.loc["Ua", "resolved_zone_chapter_label"] == "U"
    assert policies.loc["Ua", "zoning_precheck_status"] == policies.loc[
        "U", "zoning_precheck_status"
    ]
```

### `test_unmapped_dominant_zone_is_rejected`

**Purpose**

Exercises `unmapped dominant zone is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
mapping = structure.zone_mapping.copy()
mapping.loc[mapping["source_zone_label_raw"].eq("U"), [
        "resolved_zone_chapter_label",
        "matched_section_id",
    ]] = None
mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_status"] = "UNMAPPED"
mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_method"] = "NONE"
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
```

**Action**

```python
mutated = _structure_with_hashes(replace(structure, zone_mapping=mapping))
```

**Expected result**

```python
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

**Regression protected**

Locks `unmapped dominant zone is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
    mapping = structure.zone_mapping.copy()
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), [
        "resolved_zone_chapter_label",
        "matched_section_id",
    ]] = None
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

### `test_link_table_exactly_reproduces_routes_and_reverse_links`

**Purpose**

Exercises `link table exactly reproduces routes and reverse links`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
expected = {
        ("ROUTE-U-CONDITIONAL", "E-U-POSITIVE", "POSITIVE"),
        ("ROUTE-U-CONDITIONAL", "E-U-CONDITION", "CONDITION"),
        ("ROUTE-N-DIFFICULT", "E-N-1", "DIFFICULTY"),
    }
actual = {
        (row.route_id, row.evidence_id, row.route_role)
        for row in valid_result.evidence_route_links.itertuples(index=False)
    }
catalog = valid_result.evidence_catalog.set_index("evidence_id")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert actual == expected
assert catalog.loc["E-U-POSITIVE", "linked_route_ids"] == (
        "ROUTE-U-CONDITIONAL",
    )
assert catalog.loc["E-U-POSITIVE", "linked_route_roles"] == ("POSITIVE",)
assert bool(catalog["decision_linked"].all())
```

**Regression protected**

Locks `link table exactly reproduces routes and reverse links` through the exact asserted conditions: `actual == expected`; `catalog.loc['E-U-POSITIVE', 'linked_route_ids'] == ('ROUTE-U-CONDITIONAL',)`; `catalog.loc['E-U-POSITIVE', 'linked_route_roles'] == ('POSITIVE',)`; `bool(catalog['decision_linked'].all())`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
    assert catalog.loc["E-U-POSITIVE", "linked_route_ids"] == (
        "ROUTE-U-CONDITIONAL",
    )
    assert catalog.loc["E-U-POSITIVE", "linked_route_roles"] == ("POSITIVE",)
    assert bool(catalog["decision_linked"].all())
```

### `test_context_evidence_is_separate_from_decision_outputs`

**Purpose**

Exercises `context evidence is separate from decision outputs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
*sources, policy = inputs
context_policy = _policy_with_context_only_evidence(policy)
catalog = result.evidence_catalog.set_index("evidence_id")
context = catalog.loc["E-U-CONDITION"]
chapter = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
source = result.source_zone_policy.set_index("source_zone_label_raw").loc["U"]
relation = result.parcel_zone_interpretations.loc[
        result.parcel_zone_interpretations["resolved_zone_chapter_label"].eq("U")
    ].iloc[0]
parcel = result.parcels.loc[result.parcels["parcel_id"].eq("P-1")].iloc[0]
```

**Action**

```python
result = interpret_bess_zoning(*sources, context_policy)
```

**Expected result**

```python
assert context["linked_route_ids"] == ()
assert context["linked_route_roles"] == ()
assert not bool(context["decision_linked"])
assert chapter["evidence_ids"] == ("E-U-POSITIVE", "E-U-CONDITION")
assert chapter["decision_evidence_ids"] == ("E-U-POSITIVE",)
assert chapter["context_evidence_ids"] == ("E-U-CONDITION",)
assert source["decision_evidence_ids"] == ("E-U-POSITIVE",)
assert source["context_evidence_ids"] == ("E-U-CONDITION",)
assert relation["decision_evidence_ids"] == ("E-U-POSITIVE",)
assert relation["context_evidence_ids"] == ("E-U-CONDITION",)
assert parcel["zoning_precheck_evidence_ids"] == ("E-U-POSITIVE",)
assert parcel["zoning_precheck_context_evidence_ids"] == ("E-U-CONDITION",)
```

**Regression protected**

Locks `context evidence is separate from decision outputs` through the exact asserted conditions: `context['linked_route_ids'] == ()`; `context['linked_route_roles'] == ()`; `not bool(context['decision_linked'])`; `chapter['evidence_ids'] == ('E-U-POSITIVE', 'E-U-CONDITION')`; plus 8 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_parcel_aggregation_preserves_conflicts_and_touch_only`

**Purpose**

Exercises `parcel aggregation preserves conflicts and touch only`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = valid_result.parcels.set_index("parcel_id")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Locks `parcel aggregation preserves conflicts and touch only` through the exact asserted conditions: `parcels.loc['P-1', 'zoning_precheck_status'] == 'CONDITIONAL_REVIEW'`; `parcels.loc['P-1', 'positive_area_zone_count'] == 1`; `parcels.loc['P-2', 'zoning_precheck_status'] == 'CONDITIONAL_REVIEW'`; `parcels.loc['P-2', 'positive_area_zone_count'] == 2`; plus 10 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved`

**Purpose**

Exercises `prior parcel fields geometry order index and crs are preserved`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
original = inputs[5]
prior = valid_result.parcels.loc[:, original.columns]
assert_geodataframe_equal(prior, original)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert valid_result.parcels.index.equals(original.index)
assert valid_result.parcels.crs == original.crs
assert valid_result.parcels["planning_surface_relation_count"].equals(
        original["planning_surface_relation_count"]
    )
assert valid_result.parcels["non_zoning_planning_features_interpreted"].eq(
        False
    ).all()
assert valid_result.parcels["zoning_precheck_requires_formal_review"].eq(
        True
    ).all()
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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
    assert valid_result.parcels["non_zoning_planning_features_interpreted"].eq(
        False
    ).all()
    assert valid_result.parcels["zoning_precheck_requires_formal_review"].eq(
        True
    ).all()
```

### `test_inputs_are_not_mutated`

**Purpose**

Exercises `inputs are not mutated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, structure, _, zones, relations, parcels, _, _ = inputs
zone_snapshot = zones.copy(deep=True)
relation_snapshot = relations.copy(deep=True)
parcel_snapshot = parcels.copy(deep=True)
section_snapshot = structure.sections.copy(deep=True)
pd.testing.assert_frame_equal(zones, zone_snapshot)
pd.testing.assert_frame_equal(relations, relation_snapshot)
assert_geodataframe_equal(parcels, parcel_snapshot)
pd.testing.assert_frame_equal(structure.sections, section_snapshot)
```

**Action**

```python
interpret_bess_zoning(*inputs)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `inputs are not mutated` by requiring the reproduced call path `zones.copy`, `relations.copy`, `parcels.copy`, `structure.sections.copy` without an unasserted exception.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `test_policy_change_after_result_creation_is_rejected`

**Purpose**

Exercises `policy change after result creation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
payload["chapters"][0]["rationale"] = "Changed checked-in rationale."
changed = BessZoningPolicyConfig.model_validate(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="policy_config_sha256"):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)
```

**Regression protected**

Locks `policy change after result creation is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["rationale"] = "Changed checked-in rationale."
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="policy_config_sha256"):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)
```

### `test_evidence_change_after_result_creation_is_rejected`

**Purpose**

Exercises `evidence change after result creation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload(inputs[-1])
excerpt = "equipment is permitted"
evidence = payload["chapters"][0]["evidence"][0]
evidence["exact_raw_excerpt"] = excerpt
evidence["excerpt_sha256"] = sha256(excerpt.encode()).hexdigest()
evidence["excerpt_start"] += len("Technical ")
changed = BessZoningPolicyConfig.model_validate(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)
```

**Regression protected**

Locks `evidence change after result creation is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_evidence_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
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

### `test_zoning_relation_and_zone_mapping_changes_are_rejected`

**Purpose**

Exercises `zoning relation and zone mapping changes are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
changed_relations = relations.copy()
changed_relations.loc[0, "intersection_area_m2"] = 99.0
changed_relations.loc[0, "parcel_share_pct"] = 99.0
changed_relations.loc[0, "zone_share_pct"] = 9.9
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Locks `zoning relation and zone mapping changes are rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_zoning_relation_and_zone_mapping_changes_are_rejected(inputs, valid_result) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
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

### `test_structure_config_and_hierarchy_changes_are_rejected`

**Purpose**

Exercises `structure config and hierarchy changes are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
changed_config = config.model_copy(update={"structure_profile": "changed"})
changed_sections = structure.sections.copy(deep=True)
article = changed_sections["section_type"].eq("ARTICLE")
changed_sections.loc[article.idxmax(), "parent_section_id"] = "SECTION-UNKNOWN"
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
```

**Action**

```python
changed_structure = _structure_with_hashes(
        replace(structure, sections=changed_sections)
    )
```

**Expected result**

```python
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

**Regression protected**

Locks `structure config and hierarchy changes are rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
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

### `test_public_source_complete_validator_is_invoked`

**Purpose**

Exercises `public source complete validator is invoked`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
interpret_bess_zoning(*inputs)
```

**Expected result**

```python
assert calls >= 1
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_public_source_complete_validator_is_invoked.counted`

**Exact signature**

```python
def counted(*args, **kwargs):
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
original(*args, **kwargs)
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

- function object argument: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_precheck_build_performs_one_zoning_source_complete_validation`

**Purpose**

Exercises `one precheck build performs one zoning source complete validation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
calls = 0
def counted(*args) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        counted,
    )
```

**Action**

```python
interpret_bess_zoning(*inputs)
```

**Expected result**

```python
assert calls == 1
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_one_precheck_build_performs_one_zoning_source_complete_validation.counted`

**Exact signature**

```python
def counted(*args) -> None:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

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

- function object argument: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_physical_zoning_fails_before_policy_interpretation`

**Purpose**

Exercises `invalid physical zoning fails before policy interpretation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="physical source invalid"):
        interpret_bess_zoning(*inputs)
assert policy_calls == 0
```

**Regression protected**

Locks `invalid physical zoning fails before policy interpretation`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_invalid_physical_zoning_fails_before_policy_interpretation.invalid_source`

**Exact signature**

```python
def invalid_source(*args) -> None:
```

**Purpose**

Private `test` helper for invalid source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `interpret_module.PlanningZoningError('physical source invalid')`.

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

- function object argument: `tests/unit/test_interpret_bess_zoning.py::test_invalid_physical_zoning_fails_before_policy_interpretation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', invalid_source)`.

**Complete source-ordered implementation**

```python
def invalid_source(*args) -> None:
        raise interpret_module.PlanningZoningError("physical source invalid")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_physical_zoning_fails_before_policy_interpretation.counted_policy`

**Exact signature**

```python
def counted_policy(*args):
```

**Purpose**

Private `test` helper for counted policy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
inputs[-1]
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

- function object argument: `tests/unit/test_interpret_bess_zoning.py::test_invalid_physical_zoning_fails_before_policy_interpretation` via `monkeypatch.setattr(interpret_module, '_resolved_policy', counted_policy)`.

**Complete source-ordered implementation**

```python
def counted_policy(*args):
        nonlocal policy_calls
        policy_calls += 1
        return inputs[-1]
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_build_result_performs_one_factual_structure_rebuild`

**Purpose**

Exercises `one build result performs one factual structure rebuild`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert calls == 1
```

**Regression protected**

Locks `one build result performs one factual structure rebuild` through the exact asserted conditions: `calls == 1`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_one_build_result_performs_one_factual_structure_rebuild.counted`

**Exact signature**

```python
def counted(*args, **kwargs):
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
original(*args, **kwargs)
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

- function object argument: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_area_denominators_are_required`

**Purpose**

Exercises `relation area denominators are required`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Locks `relation area denominators are required`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
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

### `test_relation_percentages_must_match_denominators`

**Purpose**

Exercises `relation percentages must match denominators`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
changed = relations.copy(deep=True)
changed.loc[0, column] += 1.0
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Locks `relation percentages must match denominators`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
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

### `test_factual_zone_mapping_counts_are_recomputed`

**Purpose**

Exercises `factual zone mapping counts are recomputed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
changed_mapping = structure.zone_mapping.copy(deep=True)
changed_mapping.loc[0, "candidate_intersection_count"] += 1
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
changed_mapping = structure.zone_mapping.copy()
changed_mapping.loc[0, "source_zone_label_raw"] = "CHANGED"
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
```

**Action**

```python
changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
```

**Expected result**

```python
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

**Regression protected**

Locks `factual zone mapping counts are recomputed`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
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

### `test_coordinated_result_mutation_is_rejected`

**Purpose**

Exercises `coordinated result mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
chapter = valid_result.chapter_policy.copy(deep=True)
chapter.loc[0, "zoning_precheck_confidence"] = "HIGH"
```

**Action**

```python
mutated = _result_with_hashes(replace(valid_result, chapter_policy=chapter))
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Regression protected**

Locks `coordinated result mutation is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
    chapter = valid_result.chapter_policy.copy(deep=True)
    chapter.loc[0, "zoning_precheck_confidence"] = "HIGH"
    mutated = _result_with_hashes(replace(valid_result, chapter_policy=chapter))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

### `test_coordinated_evidence_catalog_mutation_is_rejected`

**Purpose**

Exercises `coordinated evidence catalog mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
catalog = valid_result.evidence_catalog.copy(deep=True)
catalog.loc[0, "interpretation_note"] = "Coordinated mutation."
```

**Action**

```python
mutated = _result_with_hashes(
        replace(valid_result, evidence_catalog=catalog)
    )
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Regression protected**

Locks `coordinated evidence catalog mutation is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_evidence_catalog_mutation_is_rejected(inputs, valid_result) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[0, "interpretation_note"] = "Coordinated mutation."
    mutated = _result_with_hashes(
        replace(valid_result, evidence_catalog=catalog)
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

### `test_coordinated_catalog_occurrence_duplicate_is_rejected`

**Purpose**

Exercises `coordinated catalog occurrence duplicate is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
```

**Expected result**

```python
with pytest.raises(
        BessZoningPrecheckError,
        match="duplicate chapter-scoped evidence occurrence",
    ):
        _validate(inputs, mutated)
```

**Regression protected**

Locks `coordinated catalog occurrence duplicate is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_coordinated_route_table_mutation_is_rejected`

**Purpose**

Exercises `coordinated route table mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
routes = valid_result.route_assessments.copy(deep=True)
routes.loc[0, "applicability_note"] = "Coordinated route mutation."
```

**Action**

```python
mutated = _result_with_hashes(
        replace(valid_result, route_assessments=routes)
    )
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Regression protected**

Locks `coordinated route table mutation is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_route_table_mutation_is_rejected(inputs, valid_result) -> None:
    routes = valid_result.route_assessments.copy(deep=True)
    routes.loc[0, "applicability_note"] = "Coordinated route mutation."
    mutated = _result_with_hashes(
        replace(valid_result, route_assessments=routes)
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

### `test_coordinated_evidence_route_link_mutation_is_rejected`

**Purpose**

Exercises `coordinated evidence route link mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
links = valid_result.evidence_route_links.copy(deep=True)
links.loc[0, "route_role"] = "BROKEN"
```

**Action**

```python
mutated = _result_with_hashes(
        replace(valid_result, evidence_route_links=links)
    )
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Regression protected**

Locks `coordinated evidence route link mutation is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_evidence_route_link_mutation_is_rejected(
    inputs, valid_result
) -> None:
    links = valid_result.evidence_route_links.copy(deep=True)
    links.loc[0, "route_role"] = "BROKEN"
    mutated = _result_with_hashes(
        replace(valid_result, evidence_route_links=links)
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

### `test_coordinated_reverse_link_mutation_is_rejected`

**Purpose**

Exercises `coordinated reverse link mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
catalog = valid_result.evidence_catalog.copy(deep=True)
catalog.at[0, "linked_route_roles"] = ("DIFFICULTY",)
```

**Action**

```python
mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Regression protected**

Locks `coordinated reverse link mutation is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_reverse_link_mutation_is_rejected(inputs, valid_result) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.at[0, "linked_route_roles"] = ("DIFFICULTY",)
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

### `test_evidence_route_link_hash_mutation_is_rejected`

**Purpose**

Exercises `evidence route link hash mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
mutated = replace(
        valid_result,
        evidence_route_links_content_sha256="f" * 64,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_evidence_route_link_hash_mutation_is_rejected(inputs, valid_result) -> None:
    mutated = replace(
        valid_result,
        evidence_route_links_content_sha256="f" * 64,
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)
```

### `test_old_result_hash_schemas_are_rejected`

**Purpose**

Exercises `old result hash schemas are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `version`.

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
with pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version"):
        _validate(inputs, replace(valid_result, result_hash_schema_version=version))
```

**Regression protected**

Locks `old result hash schemas are rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_old_result_hash_schemas_are_rejected(
    inputs, valid_result, version: int
) -> None:
    with pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version"):
        _validate(inputs, replace(valid_result, result_hash_schema_version=version))
```

### `test_relation_identity_change_is_rejected`

**Purpose**

Exercises `relation identity change is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, structure, config, zones, relations, parcels, planning_document, policy = inputs
changed = relations.copy()
changed.loc[0, "source_zone_id"] = "SRC-N"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Locks `relation identity change is rejected`: the reproduced adversarial input must raise `BessZoningPrecheckError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_relation_identity_change_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = inputs
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

### `test_readback_result_validates`

**Purpose**

Exercises `readback result validates`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `inputs` (local fixture, scope `function`), `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert not persisted.evidence_catalog.duplicated(occurrence_columns).any()
```

**Regression protected**

Locks `readback result validates` through the exact asserted conditions: `not persisted.evidence_catalog.duplicated(occurrence_columns).any()`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_policy_yaml_roundtrip_is_strict`

**Purpose**

Exercises `policy yaml roundtrip is strict`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `inputs` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
policy = inputs[-1]
path = tmp_path / "policy.yaml"
import yaml
path.write_text(
        yaml.safe_dump(
            policy.model_dump(mode="json"),
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert load_bess_zoning_policy_config(path) == policy
```

**Regression protected**

Locks `policy yaml roundtrip is strict` through the exact asserted conditions: `load_bess_zoning_policy_config(path) == policy`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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
