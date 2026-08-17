# `tests/unit/test_structure_planning_regulation.py`

## File identity

- Repository path: `tests/unit/test_structure_planning_regulation.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `structure_planning_regulation` contracts exercised in this file.
- Source SHA256: `982f563beb37fe123241b878646904d140d33644dc42640d07b8076f54d623b4`

## 1. Purpose

Provides complete unit and regression coverage for the `structure_planning_regulation` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import replace`
- `from pathlib import Path`

### Third-party packages

- `import pandas as pd`
- `import pytest`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.common.planning_text import normalize_planning_search_text`
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
- `from landscout.stages.planning_overlay import technical_overlay_tolerance`
- `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
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
def _index(raw_pages: tuple[str, ...] | None = None) -> PlanningRegulationIndex:
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

- direct call: `tests/unit/test_structure_planning_regulation.py::valid_result` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_config_schema_versions_are_rejected` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_accepts_exact_booleans` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_positional_header_footer_filter_preserves_matching_body_lines` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_page_without_configured_header_or_footer_is_unchanged` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_heading_patterns_require_mandatory_named_captures` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_optional_pattern_lists_may_be_empty` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_identical_structural_regex_across_groups_is_rejected_by_config` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `_index`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target` via `_index`.

**Complete source-ordered implementation**

```python
def _index(raw_pages: tuple[str, ...] | None = None) -> PlanningRegulationIndex:
    if raw_pages is None:
        raw_pages = (
            "Test PLU\n1\nZONE U\nARTICLE U 1 - TOC ENTRY",
            "Test PLU\n2\nARTICLE 1 - GENERAL PROVISIONS\nGeneral energy rule.",
            "Test PLU\n3\nZONE U\nCharacter of U.\nARTICLE U 1 - USES\nFirst page energy text.",
            "Test PLU\n4\nSecond page of the same article.\nARTICLE U 2 - NETWORKS\nNetwork text.",
            "Test PLU\n5\nZONE N\nARTICLE N 1 - RISK\nRisk text.",
            "Test PLU\n6\nZONE Z\nARTICLE Z 1 - FIRST\nText.",
            "Test PLU\n7\nZONE Z\nARTICLE Z 2 - SECOND\nText.",
        )
    rows: list[dict[str, object]] = []
    for number, raw_text in enumerate(raw_pages, start=1):
        normalized_text = _normalize_search_text(raw_text)
        row: dict[str, object] = {
            "page_number": number,
            "extraction_status": "TEXT" if normalized_text else "EMPTY",
            "raw_text": raw_text,
            "normalized_search_text": normalized_text,
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

### `_config`

**Exact signature**

```python
def _config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
```

**Purpose**

Private `test` helper for config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningRegulationStructureConfig`.
- Every observed return expression is reproduced without truncation:
```python
PlanningRegulationStructureConfig.model_validate({'schema_version': 2, 'structure_profile': 'synthetic_v1', 'document_lock': {'document_id': index.document_id, 'pdf_sha256': index.pdf_sha256, 'pages_content_sha256': index.pages_content_sha256, 'index_content_sha256': index.index_content_sha256, 'normalization_profile': index.search_normalization_profile}, 'document_layout': {'body_start_page': 1, 'table_of_contents_pages': [1], 'max_heading_continuation_lines': 2, 'include_table_of_contents_in_topic_evidence': False}, 'heading_patterns': {'zone_chapter': ['^ZONE\\s+(?P<label>[A-Za-z0-9]+)$'], 'article': ['^ARTICLE\\s+(?P<zone>[A-Za-z0-9]+)\\s+(?P<number>\\d+)\\s*[-–—]\\s*(?P<title>.*)$'], 'general_section': ['^ARTICLE\\s+(?P<number>\\d+)\\s*[-–—]\\s*(?P<title>.*)$'], 'continuation': ['^[^a-z]*[A-Z][^a-z]*$']}, 'ignored_patterns': {'page_headers': ['^Test PLU$'], 'page_footers': ['^\\d+$']}, 'zone_aliases': {'Ua': 'U'}, 'topics': {'energy': ['energy'], 'risk': ['risk']}, 'topic_match_policy': {'boundary_mode': 'token', 'overlap_resolution': 'longest_match'}, 'topic_context_characters': 20})
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

- direct call: `tests/unit/test_structure_planning_regulation.py::valid_result` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_validate` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_structure_schema_versions_are_explicit` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_config_schema_versions_are_rejected` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_accepts_exact_booleans` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_positional_header_footer_filter_preserves_matching_body_lines` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_page_without_configured_header_or_footer_is_unchanged` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_heading_patterns_require_mandatory_named_captures` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_optional_pattern_lists_may_be_empty` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_config_with_structural_patterns` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_identical_structural_regex_across_groups_is_rejected_by_config` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target` via `_config`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change` via `_config`.

**Complete source-ordered implementation**

```python
def _config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
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
                "table_of_contents_pages": [1],
                "max_heading_continuation_lines": 2,
                "include_table_of_contents_in_topic_evidence": False,
            },
            "heading_patterns": {
                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],
                "article": [
                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*[-–—]\s*(?P<title>.*)$"
                ],
                "general_section": [
                    r"^ARTICLE\s+(?P<number>\d+)\s*[-–—]\s*(?P<title>.*)$"
                ],
                "continuation": [r"^[^a-z]*[A-Z][^a-z]*$"],
            },
            "ignored_patterns": {
                "page_headers": [r"^Test PLU$"],
                "page_footers": [r"^\d+$"],
            },
            "zone_aliases": {"Ua": "U"},
            "topics": {"energy": ["energy"], "risk": ["risk"]},
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
pd.DataFrame({'planning_zone_id': [f'ZONE-{label}' for label in labels], 'source_zone_id': [f'SRC-{label}' for label in labels], 'zone_label_raw': labels, 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256})
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

- direct call: `tests/unit/test_structure_planning_regulation.py::valid_result` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_validate` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target` via `_zones`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change` via `_zones`.

**Complete source-ordered implementation**

```python
def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
    labels = ["U", "Ua", "X", "UX", "Z"]
    return pd.DataFrame(
        {
            "planning_zone_id": [f"ZONE-{label}" for label in labels],
            "source_zone_id": [f"SRC-{label}" for label in labels],
            "zone_label_raw": labels,
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
        }
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_intersections`

**Exact signature**

```python
def _intersections(index: PlanningRegulationIndex) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for intersections; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
pd.DataFrame({'parcel_id': ['PARCEL-1', 'PARCEL-2'], 'planning_zone_id': ['ZONE-U', 'ZONE-Ua'], 'source_zone_id': ['SRC-U', 'SRC-Ua'], 'zone_label_raw': ['U', 'Ua'], 'relation_type': ['AREA_OVERLAP', 'AREA_OVERLAP'], 'intersection_area_m2': [100.0, 50.0], 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256})
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

- direct call: `tests/unit/test_structure_planning_regulation.py::valid_result` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_validate` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::_structure_with_document_layout` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target` via `_intersections`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change` via `_intersections`.

**Complete source-ordered implementation**

```python
def _intersections(index: PlanningRegulationIndex) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "parcel_id": ["PARCEL-1", "PARCEL-2"],
            "planning_zone_id": ["ZONE-U", "ZONE-Ua"],
            "source_zone_id": ["SRC-U", "SRC-Ua"],
            "zone_label_raw": ["U", "Ua"],
            "relation_type": ["AREA_OVERLAP", "AREA_OVERLAP"],
            "intersection_area_m2": [100.0, 50.0],
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
        }
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `valid_result` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `(index, result)`.
- Tests requesting it by parameter injection: `test_source_complete_validator_can_return_validated_fragments`, `test_structure_schema_versions_are_explicit`, `test_old_and_unknown_result_config_schema_versions_are_rejected`, `test_old_and_unknown_section_hash_schema_versions_are_rejected`, `test_realistic_structure_is_deterministic_and_toc_heading_is_ignored`, `test_zone_article_parent_and_multi_page_text_are_preserved`, `test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping`, `test_topic_evidence_distinguishes_general_and_zone_specific`, `test_coordinated_frame_mutation_is_rejected`, `test_unknown_topic_page_reference_is_rejected`, `test_coordinated_section_row_mutation_is_caught_by_outer_envelope`, `test_source_complete_validator_rejects_changed_ambiguous_grammar`, `test_lossless_partition_mutation_is_rejected`, `test_duplicate_or_reordered_record_partition_is_rejected`, `test_unsorted_section_pages_are_rejected`, `test_article_parent_semantics_are_enforced`, `test_wrong_intersection_source_zone_id_is_rejected`, `test_zone_mapping_contract_mutations_are_rejected`, `test_topic_evidence_semantic_mutations_are_rejected`, `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`, `test_source_complete_validator_rejects_post_build_source_change`, `test_source_and_result_hash_mutation_is_rejected`.

**Complete fixture implementation**

```python
def valid_result():
    index = _index()
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), _config(index)
    )
    return index, result
```

### `_validate`

**Exact signature**

```python
def _validate(
    index: PlanningRegulationIndex,
    result,
) -> None:
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
- CRS/geometry calculation: `_intersections`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_result_config_schema_versions_are_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_section_hash_schema_versions_are_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_realistic_structure_is_deterministic_and_toc_heading_is_ignored` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_coordinated_frame_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_unknown_topic_page_reference_is_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_lossless_partition_mutation_is_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_duplicate_or_reordered_record_partition_is_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_unsorted_section_pages_are_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_article_parent_semantics_are_enforced` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_zone_mapping_contract_mutations_are_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_topic_evidence_semantic_mutations_are_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `_validate`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_source_and_result_hash_mutation_is_rejected` via `_validate`.

**Complete source-ordered implementation**

```python
def _validate(
    index: PlanningRegulationIndex,
    result,
) -> None:
    validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        _config(index),
        result,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_package_exports_clean_high_level_api`

**Purpose**

Exercises `package exports clean high level api`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
assert "structure_planning_regulation" in stages.__all__
assert "validate_planning_regulation_structure" in stages.__all__
assert "validate_planning_regulation_structure_with_fragments" in stages.__all__
assert not any(name.startswith("_build_") for name in stages.__all__)
```

**Regression protected**

Locks `package exports clean high level api` through the exact asserted conditions: `'structure_planning_regulation' in stages.__all__`; `'validate_planning_regulation_structure' in stages.__all__`; `'validate_planning_regulation_structure_with_fragments' in stages.__all__`; `not any((name.startswith('_build_') for name in stages.__all__))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_package_exports_clean_high_level_api() -> None:
    assert "structure_planning_regulation" in stages.__all__
    assert "validate_planning_regulation_structure" in stages.__all__
    assert "validate_planning_regulation_structure_with_fragments" in stages.__all__
    assert not any(name.startswith("_build_") for name in stages.__all__)
```

### `test_source_complete_validator_can_return_validated_fragments`

**Purpose**

Exercises `source complete validator can return validated fragments`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
```

**Action**

```python
fragments = validate_planning_regulation_structure_with_fragments(
        index,
        _zones(index),
        _intersections(index),
        _config(index),
        result,
    )
```

**Expected result**

```python
assert tuple(fragments.columns) == (
        "section_id",
        "page_number",
        "raw_text",
        "section_page_fragment_sha256",
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
    )
assert not fragments.duplicated(["section_id", "page_number"]).any()
assert fragments["document_id"].eq(index.document_id).all()
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_complete_validator_can_return_validated_fragments(valid_result) -> None:
    index, result = valid_result
    fragments = validate_planning_regulation_structure_with_fragments(
        index,
        _zones(index),
        _intersections(index),
        _config(index),
        result,
    )
    assert tuple(fragments.columns) == (
        "section_id",
        "page_number",
        "raw_text",
        "section_page_fragment_sha256",
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
    )
    assert not fragments.duplicated(["section_id", "page_number"]).any()
    assert fragments["document_id"].eq(index.document_id).all()
```

### `test_structure_schema_versions_are_explicit`

**Purpose**

Exercises `structure schema versions are explicit`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
config = _config(index)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert config.schema_version == 2
assert result.structure_config_schema_version == 2
assert SECTION_HASH_SCHEMA_VERSION == 3
assert result.section_hash_schema_version == 3
assert STRUCTURE_MANIFEST_SCHEMA_VERSION == 4
```

**Regression protected**

Locks `structure schema versions are explicit` through the exact asserted conditions: `config.schema_version == 2`; `result.structure_config_schema_version == 2`; `SECTION_HASH_SCHEMA_VERSION == 3`; `result.section_hash_schema_version == 3`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_structure_schema_versions_are_explicit(valid_result) -> None:
    index, result = valid_result
    config = _config(index)
    assert config.schema_version == 2
    assert result.structure_config_schema_version == 2
    assert SECTION_HASH_SCHEMA_VERSION == 3
    assert result.section_hash_schema_version == 3
    assert STRUCTURE_MANIFEST_SCHEMA_VERSION == 4
```

### `test_old_and_unknown_config_schema_versions_are_rejected`

**Purpose**

Exercises `old and unknown config schema versions are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `schema_version`.

**Setup**

```python
index = _index()
payload = _config(index).model_dump(mode="python")
payload["schema_version"] = schema_version
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="unsupported structure config schema"):
        PlanningRegulationStructureConfig.model_validate(payload)
```

**Regression protected**

Locks `old and unknown config schema versions are rejected`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_old_and_unknown_config_schema_versions_are_rejected(
    schema_version: int,
) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["schema_version"] = schema_version
    with pytest.raises(ValueError, match="unsupported structure config schema"):
        PlanningRegulationStructureConfig.model_validate(payload)
```

### `test_old_and_unknown_result_config_schema_versions_are_rejected`

**Purpose**

Exercises `old and unknown result config schema versions are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `schema_version`.

**Setup**

```python
index, result = valid_result
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="schema version"):
        _validate(
            index,
            replace(result, structure_config_schema_version=schema_version),
        )
```

**Regression protected**

Locks `old and unknown result config schema versions are rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_old_and_unknown_result_config_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError, match="schema version"):
        _validate(
            index,
            replace(result, structure_config_schema_version=schema_version),
        )
```

### `test_old_and_unknown_section_hash_schema_versions_are_rejected`

**Purpose**

Exercises `old and unknown section hash schema versions are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `schema_version`.

**Setup**

```python
index, result = valid_result
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="schema version"):
        _validate(index, replace(result, section_hash_schema_version=schema_version))
```

**Regression protected**

Locks `old and unknown section hash schema versions are rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_old_and_unknown_section_hash_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError, match="schema version"):
        _validate(index, replace(result, section_hash_schema_version=schema_version))
```

### `test_toc_topic_evidence_flag_rejects_boolean_coercion`

**Purpose**

Exercises `toc topic evidence flag rejects boolean coercion`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
index = _index()
payload = _config(index).model_dump(mode="python")
payload["document_layout"][
        "include_table_of_contents_in_topic_evidence"
    ] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError):
        PlanningRegulationStructureConfig.model_validate(payload)
```

**Regression protected**

Locks `toc topic evidence flag rejects boolean coercion`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_toc_topic_evidence_flag_rejects_boolean_coercion(value: object) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"][
        "include_table_of_contents_in_topic_evidence"
    ] = value
    with pytest.raises(ValueError):
        PlanningRegulationStructureConfig.model_validate(payload)
```

### `test_toc_topic_evidence_flag_accepts_exact_booleans`

**Purpose**

Exercises `toc topic evidence flag accepts exact booleans`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
index = _index()
payload = _config(index).model_dump(mode="python")
payload["document_layout"][
        "include_table_of_contents_in_topic_evidence"
    ] = value
validated = PlanningRegulationStructureConfig.model_validate(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert validated.document_layout.include_table_of_contents_in_topic_evidence is value
```

**Regression protected**

Locks `toc topic evidence flag accepts exact booleans` through the exact asserted conditions: `validated.document_layout.include_table_of_contents_in_topic_evidence is value`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_toc_topic_evidence_flag_accepts_exact_booleans(value: bool) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"][
        "include_table_of_contents_in_topic_evidence"
    ] = value
    validated = PlanningRegulationStructureConfig.model_validate(payload)
    assert validated.document_layout.include_table_of_contents_in_topic_evidence is value
```

### `test_document_layout_accepts_real_first_and_last_indexed_pages`

**Purpose**

Exercises `document layout accepts real first and last indexed pages`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, config, result = _structure_with_document_layout(
        (
            "CONTENTS",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
            "END CONTENTS",
        ),
        toc_pages=(1, 3),
        body_start_page=1,
    )
```

**Action**

```python
validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )
```

**Expected result**

```python
assert result.sections.iloc[0]["page_numbers"] == (1,)
assert result.sections.iloc[-1]["page_numbers"] == (3,)
```

**Regression protected**

Locks `document layout accepts real first and last indexed pages` through the exact asserted conditions: `result.sections.iloc[0]['page_numbers'] == (1,)`; `result.sections.iloc[-1]['page_numbers'] == (3,)`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_document_layout_accepts_real_first_and_last_indexed_pages() -> None:
    index, config, result = _structure_with_document_layout(
        (
            "CONTENTS",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
            "END CONTENTS",
        ),
        toc_pages=(1, 3),
        body_start_page=1,
    )
    validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )
    assert result.sections.iloc[0]["page_numbers"] == (1,)
    assert result.sections.iloc[-1]["page_numbers"] == (3,)
```

### `test_document_layout_rejects_nonexistent_indexed_pages`

**Purpose**

Exercises `document layout rejects nonexistent indexed pages`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
index = _index()
config = _config(index)
layout = config.document_layout.model_copy(update={field: value})
forged = config.model_copy(update={"document_layout": layout})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            forged,
        )
```

**Regression protected**

Locks `document layout rejects nonexistent indexed pages`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_document_layout_rejects_nonexistent_indexed_pages(
    field: str,
    value: object,
) -> None:
    index = _index()
    config = _config(index)
    layout = config.document_layout.model_copy(update={field: value})
    forged = config.model_copy(update={"document_layout": layout})
    with pytest.raises(PlanningRegulationStructureError):
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            forged,
        )
```

### `test_existing_empty_toc_page_is_valid_not_nonexistent`

**Purpose**

Exercises `existing empty toc page is valid not nonexistent`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, config, result = _structure_with_document_layout(
        (
            "",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        ),
        toc_pages=(1,),
        body_start_page=2,
    )
```

**Action**

```python
validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )
```

**Expected result**

```python
assert index.pages.loc[0, "extraction_status"] == "EMPTY"
```

**Regression protected**

Locks `existing empty toc page is valid not nonexistent` through the exact asserted conditions: `index.pages.loc[0, 'extraction_status'] == 'EMPTY'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_existing_empty_toc_page_is_valid_not_nonexistent() -> None:
    index, config, result = _structure_with_document_layout(
        (
            "",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        ),
        toc_pages=(1,),
        body_start_page=2,
    )
    assert index.pages.loc[0, "extraction_status"] == "EMPTY"
    validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )
```

### `test_document_lock_mismatch_is_rejected`

**Purpose**

Exercises `document lock mismatch is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `lock_field`.

**Setup**

```python
index = _index()
config = _config(index)
lock = config.document_lock.model_copy(
        update={lock_field: "f" * 64 if "sha256" in lock_field else "wrong"}
    )
changed = config.model_copy(update={"document_lock": lock})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="document lock"):
        structure_planning_regulation(index, _zones(index), _intersections(index), changed)
```

**Regression protected**

Locks `document lock mismatch is rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_document_lock_mismatch_is_rejected(lock_field: str) -> None:
    index = _index()
    config = _config(index)
    lock = config.document_lock.model_copy(
        update={lock_field: "f" * 64 if "sha256" in lock_field else "wrong"}
    )
    changed = config.model_copy(update={"document_lock": lock})
    with pytest.raises(PlanningRegulationStructureError, match="document lock"):
        structure_planning_regulation(index, _zones(index), _intersections(index), changed)
```

### `test_invalid_regex_and_unknown_yaml_field_are_controlled`

**Purpose**

Exercises `invalid regex and unknown yaml field are controlled`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
payload = _config(index).model_dump(mode="json")
payload["heading_patterns"]["zone_chapter"] = ["["]
payload["unexpected"] = True
import yaml
path = tmp_path / "bad.yaml"
path.write_text(yaml.safe_dump(payload), encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        load_planning_regulation_structure_config(path)
```

**Regression protected**

Locks `invalid regex and unknown yaml field are controlled`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_regex_and_unknown_yaml_field_are_controlled(tmp_path: Path) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="json")
    payload["heading_patterns"]["zone_chapter"] = ["["]
    payload["unexpected"] = True
    import yaml

    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(payload), encoding="utf-8")
    with pytest.raises(PlanningRegulationStructureError):
        load_planning_regulation_structure_config(path)
```

### `test_duplicate_yaml_alias_and_alias_cycle_are_rejected`

**Purpose**

Exercises `duplicate yaml alias and alias cycle are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
config = _config(index).model_dump(mode="json")
import yaml
cycle = tmp_path / "cycle.yaml"
config["zone_aliases"] = {"A": "B", "B": "A"}
cycle.write_text(yaml.safe_dump(config), encoding="utf-8")
duplicate = tmp_path / "duplicate.yaml"
text = yaml.safe_dump(_config(index).model_dump(mode="json"))
text = text.replace("zone_aliases:\n", "zone_aliases:\n  A: U\n  A: N\n")
duplicate.write_text(text, encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        load_planning_regulation_structure_config(cycle)
with pytest.raises(PlanningRegulationStructureError, match="Duplicate YAML"):
        load_planning_regulation_structure_config(duplicate)
```

**Regression protected**

Locks `duplicate yaml alias and alias cycle are rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_yaml_alias_and_alias_cycle_are_rejected(tmp_path: Path) -> None:
    index = _index()
    config = _config(index).model_dump(mode="json")
    import yaml

    cycle = tmp_path / "cycle.yaml"
    config["zone_aliases"] = {"A": "B", "B": "A"}
    cycle.write_text(yaml.safe_dump(config), encoding="utf-8")
    with pytest.raises(PlanningRegulationStructureError):
        load_planning_regulation_structure_config(cycle)
    duplicate = tmp_path / "duplicate.yaml"
    text = yaml.safe_dump(_config(index).model_dump(mode="json"))
    text = text.replace("zone_aliases:\n", "zone_aliases:\n  A: U\n  A: N\n")
    duplicate.write_text(text, encoding="utf-8")
    with pytest.raises(PlanningRegulationStructureError, match="Duplicate YAML"):
        load_planning_regulation_structure_config(duplicate)
```

### `test_realistic_structure_is_deterministic_and_toc_heading_is_ignored`

**Purpose**

Exercises `realistic structure is deterministic and toc heading is ignored`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
_validate(index, result)
chapters = result.sections.loc[result.sections["section_type"].eq("ZONE_CHAPTER")]
general = result.sections.loc[result.sections["section_type"].eq("GENERAL")].iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.sections["section_id"].tolist() == [
        f"SECTION-{number:04d}" for number in range(1, len(result.sections) + 1)
    ]
assert chapters["zone_chapter_label"].tolist() == ["U", "N", "Z", "Z"]
assert len(chapters.loc[chapters["zone_chapter_label"].eq("U")]) == 1
assert general["heading_raw"] == "ARTICLE 1 - GENERAL PROVISIONS"
assert "General energy rule." in general["raw_text"]
```

**Regression protected**

Locks `realistic structure is deterministic and toc heading is ignored` through the exact asserted conditions: `result.sections['section_id'].tolist() == [f'SECTION-{number:04d}' for number in range(1, len(result.sections) + 1)]`; `chapters['zone_chapter_label'].tolist() == ['U', 'N', 'Z', 'Z']`; `len(chapters.loc[chapters['zone_chapter_label'].eq('U')]) == 1`; `general['heading_raw'] == 'ARTICLE 1 - GENERAL PROVISIONS'`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_realistic_structure_is_deterministic_and_toc_heading_is_ignored(
    valid_result,
) -> None:
    index, result = valid_result
    _validate(index, result)
    assert result.sections["section_id"].tolist() == [
        f"SECTION-{number:04d}" for number in range(1, len(result.sections) + 1)
    ]
    chapters = result.sections.loc[result.sections["section_type"].eq("ZONE_CHAPTER")]
    assert chapters["zone_chapter_label"].tolist() == ["U", "N", "Z", "Z"]
    assert len(chapters.loc[chapters["zone_chapter_label"].eq("U")]) == 1
    general = result.sections.loc[result.sections["section_type"].eq("GENERAL")].iloc[0]
    assert general["heading_raw"] == "ARTICLE 1 - GENERAL PROVISIONS"
    assert "General energy rule." in general["raw_text"]
```

### `test_zone_article_parent_and_multi_page_text_are_preserved`

**Purpose**

Exercises `zone article parent and multi page text are preserved`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, result = valid_result
article = result.sections.loc[
        result.sections["heading_raw"].str.startswith("ARTICLE U 1")
    ].iloc[0]
parent = result.sections.set_index("section_id").loc[article["parent_section_id"]]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parent["section_type"] == "ZONE_CHAPTER"
assert tuple(article["page_numbers"]) == (3, 4)
assert "First page energy text." in article["raw_text"]
assert "Second page of the same article." in article["raw_text"]
```

**Regression protected**

Locks `zone article parent and multi page text are preserved` through the exact asserted conditions: `parent['section_type'] == 'ZONE_CHAPTER'`; `tuple(article['page_numbers']) == (3, 4)`; `'First page energy text.' in article['raw_text']`; `'Second page of the same article.' in article['raw_text']`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_zone_article_parent_and_multi_page_text_are_preserved(valid_result) -> None:
    _, result = valid_result
    article = result.sections.loc[
        result.sections["heading_raw"].str.startswith("ARTICLE U 1")
    ].iloc[0]
    parent = result.sections.set_index("section_id").loc[article["parent_section_id"]]
    assert parent["section_type"] == "ZONE_CHAPTER"
    assert tuple(article["page_numbers"]) == (3, 4)
    assert "First page energy text." in article["raw_text"]
    assert "Second page of the same article." in article["raw_text"]
```

### `test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping`

**Purpose**

Exercises `exact alias unmapped ambiguous and no fuzzy mapping`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, result = valid_result
mappings = result.zone_mapping.set_index("source_zone_label_raw")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert mappings.at["U", "mapping_status"] == "EXACT"
assert mappings.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
assert mappings.at["X", "mapping_status"] == "UNMAPPED"
assert mappings.at["UX", "mapping_status"] == "UNMAPPED"
assert mappings.at["Z", "mapping_status"] == "AMBIGUOUS"
assert mappings.at["X", "dominant_candidate_count"] == 0
```

**Regression protected**

Locks `exact alias unmapped ambiguous and no fuzzy mapping` through the exact asserted conditions: `mappings.at['U', 'mapping_status'] == 'EXACT'`; `mappings.at['Ua', 'mapping_status'] == 'CONFIG_ALIAS'`; `mappings.at['X', 'mapping_status'] == 'UNMAPPED'`; `mappings.at['UX', 'mapping_status'] == 'UNMAPPED'`; plus 2 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping(valid_result) -> None:
    _, result = valid_result
    mappings = result.zone_mapping.set_index("source_zone_label_raw")
    assert mappings.at["U", "mapping_status"] == "EXACT"
    assert mappings.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert mappings.at["X", "mapping_status"] == "UNMAPPED"
    assert mappings.at["UX", "mapping_status"] == "UNMAPPED"
    assert mappings.at["Z", "mapping_status"] == "AMBIGUOUS"
    assert mappings.at["X", "dominant_candidate_count"] == 0
```

### `test_topic_evidence_distinguishes_general_and_zone_specific`

**Purpose**

Exercises `topic evidence distinguishes general and zone specific`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, result = valid_result
energy = result.topic_evidence.loc[result.topic_evidence["topic"].eq("energy")]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(energy["evidence_scope"]) == {"GENERAL_RULE", "ZONE_SPECIFIC_RULE"}
assert set(energy["occurrence_count"]) == {1}
assert all(context for context in energy["raw_context"])
```

**Regression protected**

Locks `topic evidence distinguishes general and zone specific` through the exact asserted conditions: `set(energy['evidence_scope']) == {'GENERAL_RULE', 'ZONE_SPECIFIC_RULE'}`; `set(energy['occurrence_count']) == {1}`; `all((context for context in energy['raw_context']))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_topic_evidence_distinguishes_general_and_zone_specific(valid_result) -> None:
    _, result = valid_result
    energy = result.topic_evidence.loc[result.topic_evidence["topic"].eq("energy")]
    assert set(energy["evidence_scope"]) == {"GENERAL_RULE", "ZONE_SPECIFIC_RULE"}
    assert set(energy["occurrence_count"]) == {1}
    assert all(context for context in energy["raw_context"])
```

### `test_evidence_scope_is_derived_from_exact_section_type`

**Purpose**

Exercises `evidence scope is derived from exact section type`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(
        (
            "energy cover text",
            "ARTICLE 1 - GENERAL\nenergy general text",
            (
                "ZONE U\nenergy chapter text\n"
                "ARTICLE U 1 - BODY\nenergy article text"
            ),
        )
    )
payload = _config(index).model_dump(mode="python")
payload["document_layout"]["table_of_contents_pages"] = ()
payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
config = PlanningRegulationStructureConfig.model_validate(payload)
section_types = result.sections.set_index("section_id")["section_type"]
scopes_by_type = {
        section_type: set(
            result.topic_evidence.loc[
                result.topic_evidence["section_id"].map(section_types).eq(
                    section_type
                ),
                "evidence_scope",
            ]
        )
        for section_type in ("GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER")
    }
evidence = result.topic_evidence.copy(deep=True)
other_section_ids = set(
        result.sections.loc[
            result.sections["section_type"].eq("OTHER"), "section_id"
        ]
    )
row_index = evidence.index[evidence["section_id"].isin(other_section_ids)][0]
evidence.loc[row_index, "evidence_scope"] = "GENERAL_RULE"
```

**Action**

```python
result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
```

**Expected result**

```python
assert scopes_by_type == {
        "GENERAL": {"GENERAL_RULE"},
        "ZONE_CHAPTER": {"ZONE_SPECIFIC_RULE"},
        "ARTICLE": {"ZONE_SPECIFIC_RULE"},
        "OTHER": {"OTHER_TEXT"},
    }
with pytest.raises(PlanningRegulationStructureError, match="scope"):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            _intersections(index),
            config,
            replace(result, topic_evidence=evidence),
        )
```

**Regression protected**

Locks `evidence scope is derived from exact section type`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_evidence_scope_is_derived_from_exact_section_type() -> None:
    index = _index(
        (
            "energy cover text",
            "ARTICLE 1 - GENERAL\nenergy general text",
            (
                "ZONE U\nenergy chapter text\n"
                "ARTICLE U 1 - BODY\nenergy article text"
            ),
        )
    )
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["table_of_contents_pages"] = ()
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    config = PlanningRegulationStructureConfig.model_validate(payload)
    result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )

    section_types = result.sections.set_index("section_id")["section_type"]
    scopes_by_type = {
        section_type: set(
            result.topic_evidence.loc[
                result.topic_evidence["section_id"].map(section_types).eq(
                    section_type
                ),
                "evidence_scope",
            ]
        )
        for section_type in ("GENERAL", "ZONE_CHAPTER", "ARTICLE", "OTHER")
    }
    assert scopes_by_type == {
        "GENERAL": {"GENERAL_RULE"},
        "ZONE_CHAPTER": {"ZONE_SPECIFIC_RULE"},
        "ARTICLE": {"ZONE_SPECIFIC_RULE"},
        "OTHER": {"OTHER_TEXT"},
    }

    evidence = result.topic_evidence.copy(deep=True)
    other_section_ids = set(
        result.sections.loc[
            result.sections["section_type"].eq("OTHER"), "section_id"
        ]
    )
    row_index = evidence.index[evidence["section_id"].isin(other_section_ids)][0]
    evidence.loc[row_index, "evidence_scope"] = "GENERAL_RULE"
    with pytest.raises(PlanningRegulationStructureError, match="scope"):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            _intersections(index),
            config,
            replace(result, topic_evidence=evidence),
        )
```

### `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`

**Purpose**

Exercises `reversed topic mapping keys do not change output or hashes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
forward = _config(index)
payload = forward.model_dump(mode="python")
payload["topics"] = dict(reversed(tuple(payload["topics"].items())))
reversed_topics = PlanningRegulationStructureConfig.model_validate(payload)
pd.testing.assert_frame_equal(
        forward_result.topic_evidence,
        reversed_result.topic_evidence,
    )
```

**Action**

```python
forward_result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        forward,
    )
reversed_result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        reversed_topics,
    )
```

**Expected result**

```python
assert tuple(reversed_topics.topics) == tuple(reversed(tuple(forward.topics)))
assert forward_result.topic_evidence["topic"].tolist() == sorted(
        forward_result.topic_evidence["topic"].tolist()
    )
assert (
        forward_result.structure_config_sha256
        == reversed_result.structure_config_sha256
    )
assert (
        forward_result.topic_evidence_content_sha256
        == reversed_result.topic_evidence_content_sha256
    )
assert (
        forward_result.structure_result_content_sha256
        == reversed_result.structure_result_content_sha256
    )
```

**Regression protected**

Locks `reversed topic mapping keys do not change output or hashes` through the exact asserted conditions: `tuple(reversed_topics.topics) == tuple(reversed(tuple(forward.topics)))`; `forward_result.topic_evidence['topic'].tolist() == sorted(forward_result.topic_evidence['topic'].tolist())`; `forward_result.structure_config_sha256 == reversed_result.structure_config_sha256`; `forward_result.topic_evidence_content_sha256 == reversed_result.topic_evidence_content_sha256`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_reversed_topic_mapping_keys_do_not_change_output_or_hashes() -> None:
    index = _index()
    forward = _config(index)
    payload = forward.model_dump(mode="python")
    payload["topics"] = dict(reversed(tuple(payload["topics"].items())))
    reversed_topics = PlanningRegulationStructureConfig.model_validate(payload)
    assert tuple(reversed_topics.topics) == tuple(reversed(tuple(forward.topics)))

    forward_result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        forward,
    )
    reversed_result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        reversed_topics,
    )

    pd.testing.assert_frame_equal(
        forward_result.topic_evidence,
        reversed_result.topic_evidence,
    )
    assert forward_result.topic_evidence["topic"].tolist() == sorted(
        forward_result.topic_evidence["topic"].tolist()
    )
    assert (
        forward_result.structure_config_sha256
        == reversed_result.structure_config_sha256
    )
    assert (
        forward_result.topic_evidence_content_sha256
        == reversed_result.topic_evidence_content_sha256
    )
    assert (
        forward_result.structure_result_content_sha256
        == reversed_result.structure_result_content_sha256
    )
```

### `test_equal_length_overlap_uses_configured_term_order_as_tie_break`

**Purpose**

Exercises `equal length overlap uses configured term order as tie break`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
forward_terms = ("alpha beta", "beta gamma")
reverse_terms = tuple(reversed(forward_terms))
index = _index(("ZONE U\nARTICLE U 1 - TEST\nalpha beta gamma",))
base_payload = _config(index).model_dump(mode="python")
base_payload["document_layout"]["table_of_contents_pages"] = ()
base_payload["topics"] = {"tie": forward_terms}
forward_config = PlanningRegulationStructureConfig.model_validate(base_payload)
reverse_payload = forward_config.model_dump(mode="python")
reverse_payload["topics"] = {"tie": reverse_terms}
reverse_config = PlanningRegulationStructureConfig.model_validate(reverse_payload)
```

**Action**

```python
normalized = normalize_planning_search_text("alpha beta gamma")
forward_matches = _literal_topic_matches(normalized, forward_terms)
reverse_matches = _literal_topic_matches(normalized, reverse_terms)
forward_result = structure_planning_regulation(
        index, _zones(index), _intersections(index), forward_config
    )
reverse_result = structure_planning_regulation(
        index, _zones(index), _intersections(index), reverse_config
    )
```

**Expected result**

```python
assert [match.search_term for match in forward_matches] == ["alpha beta"]
assert [match.search_term for match in reverse_matches] == ["beta gamma"]
assert (
        forward_matches[0].normalized_start,
        forward_matches[0].normalized_end,
    ) == (0, 10)
assert (
        reverse_matches[0].normalized_start,
        reverse_matches[0].normalized_end,
    ) == (6, 16)
assert forward_result.topic_evidence["search_term"].tolist() == ["alpha beta"]
assert reverse_result.topic_evidence["search_term"].tolist() == ["beta gamma"]
assert forward_result.structure_config_sha256 != reverse_result.structure_config_sha256
```

**Regression protected**

Locks `equal length overlap uses configured term order as tie break` through the exact asserted conditions: `[match.search_term for match in forward_matches] == ['alpha beta']`; `[match.search_term for match in reverse_matches] == ['beta gamma']`; `(forward_matches[0].normalized_start, forward_matches[0].normalized_end) == (0, 10)`; `(reverse_matches[0].normalized_start, reverse_matches[0].normalized_end) == (6, 16)`; plus 3 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_equal_length_overlap_uses_configured_term_order_as_tie_break() -> None:
    normalized = normalize_planning_search_text("alpha beta gamma")
    forward_terms = ("alpha beta", "beta gamma")
    reverse_terms = tuple(reversed(forward_terms))

    forward_matches = _literal_topic_matches(normalized, forward_terms)
    reverse_matches = _literal_topic_matches(normalized, reverse_terms)
    assert [match.search_term for match in forward_matches] == ["alpha beta"]
    assert [match.search_term for match in reverse_matches] == ["beta gamma"]
    assert (
        forward_matches[0].normalized_start,
        forward_matches[0].normalized_end,
    ) == (0, 10)
    assert (
        reverse_matches[0].normalized_start,
        reverse_matches[0].normalized_end,
    ) == (6, 16)

    index = _index(("ZONE U\nARTICLE U 1 - TEST\nalpha beta gamma",))
    base_payload = _config(index).model_dump(mode="python")
    base_payload["document_layout"]["table_of_contents_pages"] = ()
    base_payload["topics"] = {"tie": forward_terms}
    forward_config = PlanningRegulationStructureConfig.model_validate(base_payload)
    reverse_payload = forward_config.model_dump(mode="python")
    reverse_payload["topics"] = {"tie": reverse_terms}
    reverse_config = PlanningRegulationStructureConfig.model_validate(reverse_payload)
    forward_result = structure_planning_regulation(
        index, _zones(index), _intersections(index), forward_config
    )
    reverse_result = structure_planning_regulation(
        index, _zones(index), _intersections(index), reverse_config
    )
    assert forward_result.topic_evidence["search_term"].tolist() == ["alpha beta"]
    assert reverse_result.topic_evidence["search_term"].tolist() == ["beta gamma"]
    assert forward_result.structure_config_sha256 != reverse_result.structure_config_sha256
```

### `test_inputs_are_not_mutated`

**Purpose**

Exercises `inputs are not mutated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
zones = _zones(index)
intersections = _intersections(index)
pages_before = index.pages.copy(deep=True)
zones_before = zones.copy(deep=True)
intersections_before = intersections.copy(deep=True)
pd.testing.assert_frame_equal(index.pages, pages_before)
pd.testing.assert_frame_equal(zones, zones_before)
pd.testing.assert_frame_equal(intersections, intersections_before)
```

**Action**

```python
structure_planning_regulation(index, zones, intersections, _config(index))
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `inputs are not mutated` by requiring the reproduced call path `_index`, `_zones`, `_intersections`, `index.pages.copy` without an unasserted exception.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_inputs_are_not_mutated() -> None:
    index = _index()
    zones = _zones(index)
    intersections = _intersections(index)
    pages_before = index.pages.copy(deep=True)
    zones_before = zones.copy(deep=True)
    intersections_before = intersections.copy(deep=True)
    structure_planning_regulation(index, zones, intersections, _config(index))
    pd.testing.assert_frame_equal(index.pages, pages_before)
    pd.testing.assert_frame_equal(zones, zones_before)
    pd.testing.assert_frame_equal(intersections, intersections_before)
```

### `test_coordinated_frame_mutation_is_rejected`

**Purpose**

Exercises `coordinated frame mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`, `frame_name`, `hash_name`.

**Setup**

```python
index, result = valid_result
frame = getattr(result, frame_name).copy(deep=True)
if column == "candidate_parcel_count":
        frame.loc[0, column] = int(frame.loc[0, column]) + 1
    else:
        frame.loc[0, column] = f"{frame.loc[0, column]} changed"
changed = replace(result, **{frame_name: frame})
changed = replace(changed, **{hash_name: "f" * 64})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_frame_mutation_is_rejected(
    valid_result,
    frame_name: str,
    hash_name: str,
    column: str,
) -> None:
    index, result = valid_result
    frame = getattr(result, frame_name).copy(deep=True)
    if column == "candidate_parcel_count":
        frame.loc[0, column] = int(frame.loc[0, column]) + 1
    else:
        frame.loc[0, column] = f"{frame.loc[0, column]} changed"
    changed = replace(result, **{frame_name: frame})
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)
    # Updating only the exposed envelope hash cannot legitimize inner-row corruption.
    changed = replace(changed, **{hash_name: "f" * 64})
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)
```

### `test_unknown_topic_page_reference_is_rejected`

**Purpose**

Exercises `unknown topic page reference is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
evidence = result.topic_evidence.copy(deep=True)
evidence.loc[0, "page_number"] = 999
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="unknown page"):
        _validate(index, replace(result, topic_evidence=evidence))
```

**Regression protected**

Locks `unknown topic page reference is rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_topic_page_reference_is_rejected(valid_result) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    evidence.loc[0, "page_number"] = 999
    with pytest.raises(PlanningRegulationStructureError, match="unknown page"):
        _validate(index, replace(result, topic_evidence=evidence))
```

### `test_coordinated_section_row_mutation_is_caught_by_outer_envelope`

**Purpose**

Exercises `coordinated section row mutation is caught by outer envelope`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
sections = result.sections.copy(deep=True)
sections.loc[0, "raw_text"] = f"{sections.loc[0, 'raw_text']} changed"
sections.loc[0, "character_count"] = len(sections.loc[0, "raw_text"])
row = sections.loc[0].to_dict()
```

**Action**

```python
sections.loc[0, "normalized_text"] = _normalize_search_text(
        sections.loc[0, "raw_text"]
    )
sections.loc[0, "section_content_sha256"] = _section_content_sha256(row)
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_section_row_mutation_is_caught_by_outer_envelope(
    valid_result,
) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[0, "raw_text"] = f"{sections.loc[0, 'raw_text']} changed"
    sections.loc[0, "normalized_text"] = _normalize_search_text(
        sections.loc[0, "raw_text"]
    )
    sections.loc[0, "character_count"] = len(sections.loc[0, "raw_text"])
    row = sections.loc[0].to_dict()
    sections.loc[0, "section_content_sha256"] = _section_content_sha256(row)
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))
```

### `test_dominant_unmapped_zone_stops_processing`

**Purpose**

Exercises `dominant unmapped zone stops processing`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
relations = _intersections(index).copy(deep=True)
relations.loc[0, ["planning_zone_id", "source_zone_id", "zone_label_raw"]] = [
        "ZONE-X",
        "SRC-X",
        "X",
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="Dominant candidate"):
        structure_planning_regulation(index, _zones(index), relations, _config(index))
```

**Regression protected**

Locks `dominant unmapped zone stops processing`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_dominant_unmapped_zone_stops_processing() -> None:
    index = _index()
    relations = _intersections(index).copy(deep=True)
    relations.loc[0, ["planning_zone_id", "source_zone_id", "zone_label_raw"]] = [
        "ZONE-X",
        "SRC-X",
        "X",
    ]
    with pytest.raises(PlanningRegulationStructureError, match="Dominant candidate"):
        structure_planning_regulation(index, _zones(index), relations, _config(index))
```

### `test_positional_header_footer_filter_preserves_matching_body_lines`

**Purpose**

Exercises `positional header footer filter preserves matching body lines`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(
        (
            (
                "\nTest PLU\n\nARTICLE 1 - GENERAL PROVISIONS\n"
                "Test PLU\n100\nBody text\n\n42\n"
            ),
        )
    )
config = _config(index)
retained = [record.raw for record in records]
```

**Action**

```python
records = _line_records(index, config)
```

**Expected result**

```python
assert "Test PLU" in retained
assert "100" in retained
assert "42" not in retained
assert retained[0] == "ARTICLE 1 - GENERAL PROVISIONS"
assert records[0].page_line_number == 4
```

**Regression protected**

Locks `positional header footer filter preserves matching body lines` through the exact asserted conditions: `'Test PLU' in retained`; `'100' in retained`; `'42' not in retained`; `retained[0] == 'ARTICLE 1 - GENERAL PROVISIONS'`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_positional_header_footer_filter_preserves_matching_body_lines() -> None:
    index = _index(
        (
            (
                "\nTest PLU\n\nARTICLE 1 - GENERAL PROVISIONS\n"
                "Test PLU\n100\nBody text\n\n42\n"
            ),
        )
    )
    config = _config(index)
    records = _line_records(index, config)
    retained = [record.raw for record in records]
    assert "Test PLU" in retained
    assert "100" in retained
    assert "42" not in retained
    assert retained[0] == "ARTICLE 1 - GENERAL PROVISIONS"
    assert records[0].page_line_number == 4
```

### `test_page_without_configured_header_or_footer_is_unchanged`

**Purpose**

Exercises `page without configured header or footer is unchanged`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(("ARTICLE 1 - GENERAL\n100\nBody",))
config = _config(index)
config = config.model_copy(
        update={
            "ignored_patterns": config.ignored_patterns.model_copy(
                update={"page_headers": (), "page_footers": ()}
            )
        }
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert [record.raw for record in _line_records(index, config)] == [
        "ARTICLE 1 - GENERAL",
        "100",
        "Body",
    ]
```

**Regression protected**

Locks `page without configured header or footer is unchanged` through the exact asserted conditions: `[record.raw for record in _line_records(index, config)] == ['ARTICLE 1 - GENERAL', '100', 'Body']`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_page_without_configured_header_or_footer_is_unchanged() -> None:
    index = _index(("ARTICLE 1 - GENERAL\n100\nBody",))
    config = _config(index)
    config = config.model_copy(
        update={
            "ignored_patterns": config.ignored_patterns.model_copy(
                update={"page_headers": (), "page_footers": ()}
            )
        }
    )
    assert [record.raw for record in _line_records(index, config)] == [
        "ARTICLE 1 - GENERAL",
        "100",
        "Body",
    ]
```

### `test_blank_only_prefix_is_preserved_in_first_actual_section`

**Purpose**

Exercises `blank only prefix is preserved in first actual section`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_pages`, `expected_prefix`, `raw_pages`.

**Setup**

```python
index = _index(raw_pages)
payload = _config(index).model_dump(mode="python")
payload["document_layout"]["table_of_contents_pages"] = ()
payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
config = PlanningRegulationStructureConfig.model_validate(payload)
first = result.sections.iloc[0]
```

**Action**

```python
records = _line_records(index, config)
result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )
```

**Expected result**

```python
assert first["section_type"] == "ZONE_CHAPTER"
assert first["heading_raw"] == "ZONE U"
assert first["start_record_id"] == "RECORD-000001"
assert tuple(first["page_numbers"]) == expected_pages
assert first["raw_text"].startswith(expected_prefix)
assert int(result.sections["source_record_count"].sum()) == len(records)
assert "OTHER" not in result.sections["section_type"].tolist()
```

**Regression protected**

Locks `blank only prefix is preserved in first actual section` through the exact asserted conditions: `first['section_type'] == 'ZONE_CHAPTER'`; `first['heading_raw'] == 'ZONE U'`; `first['start_record_id'] == 'RECORD-000001'`; `tuple(first['page_numbers']) == expected_pages`; plus 3 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_blank_only_prefix_is_preserved_in_first_actual_section(
    raw_pages: tuple[str, ...],
    expected_pages: tuple[int, ...],
    expected_prefix: str,
) -> None:
    index = _index(raw_pages)
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["table_of_contents_pages"] = ()
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    config = PlanningRegulationStructureConfig.model_validate(payload)
    records = _line_records(index, config)
    result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
    validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )

    first = result.sections.iloc[0]
    assert first["section_type"] == "ZONE_CHAPTER"
    assert first["heading_raw"] == "ZONE U"
    assert first["start_record_id"] == "RECORD-000001"
    assert tuple(first["page_numbers"]) == expected_pages
    assert first["raw_text"].startswith(expected_prefix)
    assert int(result.sections["source_record_count"].sum()) == len(records)
    assert "OTHER" not in result.sections["section_type"].tolist()
```

### `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`

**Purpose**

Exercises `toc blocks anywhere are other and toggle topic evidence`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(
        (
            "CONTENTS\nARTICLE 9 - energy",
            "ZONE N\nenergy contents",
            "ARTICLE 1 - GENERAL\nrisk body",
            "ARTICLE 8 - energy",
            "ZONE Z\nenergy contents",
            "ZONE U\nARTICLE U 1 - BODY\nenergy body",
            "ARTICLE 7 - energy",
        )
    )
payload = _config(index).model_dump(mode="python")
payload["document_layout"].update(
        {
            "table_of_contents_pages": (1, 2, 4, 5, 7),
            "include_table_of_contents_in_topic_evidence": False,
        }
    )
payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
excluded_config = PlanningRegulationStructureConfig.model_validate(payload)
included_payload = excluded_config.model_dump(mode="python")
included_payload["document_layout"][
        "include_table_of_contents_in_topic_evidence"
    ] = True
included_config = PlanningRegulationStructureConfig.model_validate(
        included_payload
    )
excluded_other = excluded.sections.loc[
        excluded.sections["section_type"].eq("OTHER")
    ]
pd.testing.assert_frame_equal(excluded.sections, included.sections)
pd.testing.assert_frame_equal(excluded.zone_mapping, included.zone_mapping)
toc_pages = {1, 2, 4, 5, 7}
included_toc = included.topic_evidence.loc[
        included.topic_evidence["page_number"].isin(toc_pages)
    ]
```

**Action**

```python
excluded = structure_planning_regulation(
        index, _zones(index), _intersections(index), excluded_config
    )
included = structure_planning_regulation(
        index, _zones(index), _intersections(index), included_config
    )
for config, result in (
        (excluded_config, excluded),
        (included_config, included),
    ):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            _intersections(index),
            config,
            result,
        )
```

**Expected result**

```python
assert excluded_other["page_numbers"].tolist() == [(1, 2), (4, 5), (7,)]
assert excluded_other["heading_raw"].tolist() == [
        "CONTENTS",
        "ARTICLE 8 - energy",
        "ARTICLE 7 - energy",
    ]
assert toc_pages.isdisjoint(excluded.topic_evidence["page_number"])
assert set(excluded.topic_evidence["page_number"]) == {3, 6}
assert set(included.topic_evidence["page_number"]) == set(range(1, 8))
assert set(included_toc["evidence_scope"]) == {"OTHER_TEXT"}
```

**Regression protected**

Locks `toc blocks anywhere are other and toggle topic evidence` through the exact asserted conditions: `excluded_other['page_numbers'].tolist() == [(1, 2), (4, 5), (7,)]`; `excluded_other['heading_raw'].tolist() == ['CONTENTS', 'ARTICLE 8 - energy', 'ARTICLE 7 - energy']`; `toc_pages.isdisjoint(excluded.topic_evidence['page_number'])`; `set(excluded.topic_evidence['page_number']) == {3, 6}`; plus 2 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence() -> None:
    index = _index(
        (
            "CONTENTS\nARTICLE 9 - energy",
            "ZONE N\nenergy contents",
            "ARTICLE 1 - GENERAL\nrisk body",
            "ARTICLE 8 - energy",
            "ZONE Z\nenergy contents",
            "ZONE U\nARTICLE U 1 - BODY\nenergy body",
            "ARTICLE 7 - energy",
        )
    )
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"].update(
        {
            "table_of_contents_pages": (1, 2, 4, 5, 7),
            "include_table_of_contents_in_topic_evidence": False,
        }
    )
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    excluded_config = PlanningRegulationStructureConfig.model_validate(payload)
    included_payload = excluded_config.model_dump(mode="python")
    included_payload["document_layout"][
        "include_table_of_contents_in_topic_evidence"
    ] = True
    included_config = PlanningRegulationStructureConfig.model_validate(
        included_payload
    )

    excluded = structure_planning_regulation(
        index, _zones(index), _intersections(index), excluded_config
    )
    included = structure_planning_regulation(
        index, _zones(index), _intersections(index), included_config
    )
    for config, result in (
        (excluded_config, excluded),
        (included_config, included),
    ):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            _intersections(index),
            config,
            result,
        )

    excluded_other = excluded.sections.loc[
        excluded.sections["section_type"].eq("OTHER")
    ]
    assert excluded_other["page_numbers"].tolist() == [(1, 2), (4, 5), (7,)]
    assert excluded_other["heading_raw"].tolist() == [
        "CONTENTS",
        "ARTICLE 8 - energy",
        "ARTICLE 7 - energy",
    ]
    pd.testing.assert_frame_equal(excluded.sections, included.sections)
    pd.testing.assert_frame_equal(excluded.zone_mapping, included.zone_mapping)

    toc_pages = {1, 2, 4, 5, 7}
    assert toc_pages.isdisjoint(excluded.topic_evidence["page_number"])
    assert set(excluded.topic_evidence["page_number"]) == {3, 6}
    assert set(included.topic_evidence["page_number"]) == set(range(1, 8))
    included_toc = included.topic_evidence.loc[
        included.topic_evidence["page_number"].isin(toc_pages)
    ]
    assert set(included_toc["evidence_scope"]) == {"OTHER_TEXT"}
```

### `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`

**Purpose**

Exercises `blank gap after toc is preserved without a blank other section`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(
        (
            "ARTICLE 1 - GENERAL\nGeneral text",
            "CONTENTS\nARTICLE 9 - fake entry",
            " \n\t",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        )
    )
payload = _config(index).model_dump(mode="python")
payload["document_layout"]["table_of_contents_pages"] = (2,)
payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
config = PlanningRegulationStructureConfig.model_validate(payload)
other = result.sections.loc[result.sections["section_type"].eq("OTHER")]
chapter = result.sections.loc[
        result.sections["section_type"].eq("ZONE_CHAPTER")
    ].iloc[0]
```

**Action**

```python
result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )
```

**Expected result**

```python
assert other["page_numbers"].tolist() == [(2,)]
assert tuple(chapter["page_numbers"]) == (3, 4)
assert chapter["heading_raw"] == "ZONE U"
assert chapter["raw_text"].startswith(" \n\t\nZONE U")
```

**Regression protected**

Locks `blank gap after toc is preserved without a blank other section` through the exact asserted conditions: `other['page_numbers'].tolist() == [(2,)]`; `tuple(chapter['page_numbers']) == (3, 4)`; `chapter['heading_raw'] == 'ZONE U'`; `chapter['raw_text'].startswith(' \n\t\nZONE U')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_blank_gap_after_toc_is_preserved_without_a_blank_other_section() -> None:
    index = _index(
        (
            "ARTICLE 1 - GENERAL\nGeneral text",
            "CONTENTS\nARTICLE 9 - fake entry",
            " \n\t",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        )
    )
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["table_of_contents_pages"] = (2,)
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    config = PlanningRegulationStructureConfig.model_validate(payload)

    result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
    validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )

    other = result.sections.loc[result.sections["section_type"].eq("OTHER")]
    assert other["page_numbers"].tolist() == [(2,)]
    chapter = result.sections.loc[
        result.sections["section_type"].eq("ZONE_CHAPTER")
    ].iloc[0]
    assert tuple(chapter["page_numbers"]) == (3, 4)
    assert chapter["heading_raw"] == "ZONE U"
    assert chapter["raw_text"].startswith(" \n\t\nZONE U")
```

### `_structure_with_document_layout`

**Exact signature**

```python
def _structure_with_document_layout(
    raw_pages: tuple[str, ...],
    *,
    toc_pages: tuple[int, ...] = (),
    body_start_page: int = 1,
    include_toc_evidence: bool = False,
):
```

**Purpose**

Private `test` helper for structure with document layout; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
(index, config, result)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_intersections`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `payload['document_layout']`, `payload['ignored_patterns']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_structure_with_document_layout`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_structure_with_document_layout`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_only_toc_blocks_remain_separate_other_sections` via `_structure_with_document_layout`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_blank_toc_followed_only_by_blank_tail_remains_other` via `_structure_with_document_layout`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_ordinary_blank_gap_attaches_to_following_real_heading` via `_structure_with_document_layout`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_trailing_blank_records_attach_to_preceding_factual_section` via `_structure_with_document_layout`.

**Complete source-ordered implementation**

```python
def _structure_with_document_layout(
    raw_pages: tuple[str, ...],
    *,
    toc_pages: tuple[int, ...] = (),
    body_start_page: int = 1,
    include_toc_evidence: bool = False,
):
    index = _index(raw_pages)
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"].update(
        {
            "body_start_page": body_start_page,
            "table_of_contents_pages": toc_pages,
            "include_table_of_contents_in_topic_evidence": include_toc_evidence,
        }
    )
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    config = PlanningRegulationStructureConfig.model_validate(payload)
    result = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
    validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        config,
        result,
    )
    assert int(result.sections["source_record_count"].sum()) == len(
        _line_records(index, config)
    )
    return index, config, result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_blank_only_toc_blocks_remain_separate_other_sections`

**Purpose**

Exercises `blank only toc blocks remain separate other sections`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_pages`, `toc_raw_pages`.

**Setup**

```python
_, _, result = _structure_with_document_layout(
        (
            "ARTICLE 1 - GENERAL\nGeneral text",
            *toc_raw_pages,
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        ),
        toc_pages=expected_pages,
    )
other = result.sections.loc[result.sections["section_type"].eq("OTHER")]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(other) == 1
assert tuple(other.iloc[0]["page_numbers"]) == expected_pages
assert not str(other.iloc[0]["raw_text"]).strip()
assert other.iloc[0]["heading_raw"] == ""
```

**Regression protected**

Locks `blank only toc blocks remain separate other sections` through the exact asserted conditions: `len(other) == 1`; `tuple(other.iloc[0]['page_numbers']) == expected_pages`; `not str(other.iloc[0]['raw_text']).strip()`; `other.iloc[0]['heading_raw'] == ''`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_blank_only_toc_blocks_remain_separate_other_sections(
    toc_raw_pages: tuple[str, ...],
    expected_pages: tuple[int, ...],
) -> None:
    _, _, result = _structure_with_document_layout(
        (
            "ARTICLE 1 - GENERAL\nGeneral text",
            *toc_raw_pages,
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        ),
        toc_pages=expected_pages,
    )
    other = result.sections.loc[result.sections["section_type"].eq("OTHER")]
    assert len(other) == 1
    assert tuple(other.iloc[0]["page_numbers"]) == expected_pages
    assert not str(other.iloc[0]["raw_text"]).strip()
    assert other.iloc[0]["heading_raw"] == ""
```

### `test_blank_toc_followed_only_by_blank_tail_remains_other`

**Purpose**

Exercises `blank toc followed only by blank tail remains other`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, result = _structure_with_document_layout(
        (
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
            " \n\t",
            "\t\n ",
        ),
        toc_pages=(2,),
    )
other = result.sections.loc[result.sections["section_type"].eq("OTHER")]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(other) == 1
assert tuple(other.iloc[0]["page_numbers"]) == (2, 3)
assert not str(other.iloc[0]["raw_text"]).strip()
assert other.iloc[0]["heading_raw"] == ""
```

**Regression protected**

Locks `blank toc followed only by blank tail remains other` through the exact asserted conditions: `len(other) == 1`; `tuple(other.iloc[0]['page_numbers']) == (2, 3)`; `not str(other.iloc[0]['raw_text']).strip()`; `other.iloc[0]['heading_raw'] == ''`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_blank_toc_followed_only_by_blank_tail_remains_other() -> None:
    _, _, result = _structure_with_document_layout(
        (
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
            " \n\t",
            "\t\n ",
        ),
        toc_pages=(2,),
    )
    other = result.sections.loc[result.sections["section_type"].eq("OTHER")]
    assert len(other) == 1
    assert tuple(other.iloc[0]["page_numbers"]) == (2, 3)
    assert not str(other.iloc[0]["raw_text"]).strip()
    assert other.iloc[0]["heading_raw"] == ""
```

### `test_ordinary_blank_gap_attaches_to_following_real_heading`

**Purpose**

Exercises `ordinary blank gap attaches to following real heading`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, result = _structure_with_document_layout(
        (
            "ARTICLE 1 - GENERAL\nGeneral text",
            " \n\t",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        )
    )
chapter = result.sections.loc[
        result.sections["section_type"].eq("ZONE_CHAPTER")
    ].iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(chapter["page_numbers"]) == (2, 3)
assert str(chapter["raw_text"]).startswith(" \n\t\nZONE U")
assert chapter["heading_raw"] == "ZONE U"
```

**Regression protected**

Locks `ordinary blank gap attaches to following real heading` through the exact asserted conditions: `tuple(chapter['page_numbers']) == (2, 3)`; `str(chapter['raw_text']).startswith(' \n\t\nZONE U')`; `chapter['heading_raw'] == 'ZONE U'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_ordinary_blank_gap_attaches_to_following_real_heading() -> None:
    _, _, result = _structure_with_document_layout(
        (
            "ARTICLE 1 - GENERAL\nGeneral text",
            " \n\t",
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
        )
    )
    chapter = result.sections.loc[
        result.sections["section_type"].eq("ZONE_CHAPTER")
    ].iloc[0]
    assert tuple(chapter["page_numbers"]) == (2, 3)
    assert str(chapter["raw_text"]).startswith(" \n\t\nZONE U")
    assert chapter["heading_raw"] == "ZONE U"
```

### `test_trailing_blank_records_attach_to_preceding_factual_section`

**Purpose**

Exercises `trailing blank records attach to preceding factual section`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, result = _structure_with_document_layout(
        (
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
            " \n\t",
        )
    )
final_section = result.sections.iloc[-1]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert final_section["section_type"] == "ARTICLE"
assert tuple(final_section["page_numbers"]) == (1, 2)
assert str(final_section["raw_text"]).endswith(" \n\t")
```

**Regression protected**

Locks `trailing blank records attach to preceding factual section` through the exact asserted conditions: `final_section['section_type'] == 'ARTICLE'`; `tuple(final_section['page_numbers']) == (1, 2)`; `str(final_section['raw_text']).endswith(' \n\t')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_trailing_blank_records_attach_to_preceding_factual_section() -> None:
    _, _, result = _structure_with_document_layout(
        (
            "ZONE U\nARTICLE U 1 - BODY\nBody text",
            " \n\t",
        )
    )
    final_section = result.sections.iloc[-1]
    assert final_section["section_type"] == "ARTICLE"
    assert tuple(final_section["page_numbers"]) == (1, 2)
    assert str(final_section["raw_text"]).endswith(" \n\t")
```

### `test_heading_patterns_require_mandatory_named_captures`

**Purpose**

Exercises `heading patterns require mandatory named captures`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `group`, `pattern`.

**Setup**

```python
index = _index()
config = _config(index)
patterns = config.heading_patterns.model_copy(update={group: (pattern,)})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="named captures"):
        PlanningRegulationStructureConfig.model_validate(
            config.model_dump(mode="python")
            | {"heading_patterns": patterns.model_dump(mode="python")}
        )
```

**Regression protected**

Locks `heading patterns require mandatory named captures`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_heading_patterns_require_mandatory_named_captures(
    group: str,
    pattern: str,
) -> None:
    index = _index()
    config = _config(index)
    patterns = config.heading_patterns.model_copy(update={group: (pattern,)})
    with pytest.raises(ValueError, match="named captures"):
        PlanningRegulationStructureConfig.model_validate(
            config.model_dump(mode="python")
            | {"heading_patterns": patterns.model_dump(mode="python")}
        )
```

### `test_optional_pattern_lists_may_be_empty`

**Purpose**

Exercises `optional pattern lists may be empty`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
config = _config(index)
payload = config.model_dump(mode="python")
payload["heading_patterns"]["continuation"] = ()
payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
validated = PlanningRegulationStructureConfig.model_validate(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert validated.heading_patterns.continuation == ()
assert validated.ignored_patterns.page_headers == ()
```

**Regression protected**

Locks `optional pattern lists may be empty` through the exact asserted conditions: `validated.heading_patterns.continuation == ()`; `validated.ignored_patterns.page_headers == ()`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_optional_pattern_lists_may_be_empty() -> None:
    index = _index()
    config = _config(index)
    payload = config.model_dump(mode="python")
    payload["heading_patterns"]["continuation"] = ()
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    validated = PlanningRegulationStructureConfig.model_validate(payload)
    assert validated.heading_patterns.continuation == ()
    assert validated.ignored_patterns.page_headers == ()
```

### `_config_with_structural_patterns`

**Exact signature**

```python
def _config_with_structural_patterns(
    index: PlanningRegulationIndex,
    *,
    zone_chapter: tuple[str, ...] | None = None,
    general_section: tuple[str, ...] | None = None,
    article: tuple[str, ...] | None = None,
) -> PlanningRegulationStructureConfig:
```

**Purpose**

Private `test` helper for config with structural patterns; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningRegulationStructureConfig`.
- Every observed return expression is reproduced without truncation:
```python
PlanningRegulationStructureConfig.model_validate(payload)
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
- In-memory mutation: `payload['document_layout']['table_of_contents_pages']`, `payload['heading_patterns'][name]`, `payload['ignored_patterns']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_config_with_structural_patterns`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_config_with_structural_patterns`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous` via `_config_with_structural_patterns`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous` via `_config_with_structural_patterns`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous` via `_config_with_structural_patterns`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_config_with_structural_patterns`.

**Complete source-ordered implementation**

```python
def _config_with_structural_patterns(
    index: PlanningRegulationIndex,
    *,
    zone_chapter: tuple[str, ...] | None = None,
    general_section: tuple[str, ...] | None = None,
    article: tuple[str, ...] | None = None,
) -> PlanningRegulationStructureConfig:
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["table_of_contents_pages"] = ()
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    replacements = {
        "zone_chapter": zone_chapter,
        "general_section": general_section,
        "article": article,
    }
    for name, patterns in replacements.items():
        if patterns is not None:
            payload["heading_patterns"][name] = patterns
    return PlanningRegulationStructureConfig.model_validate(payload)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`

**Purpose**

Exercises `unique zone heading and nonheading line are classified deterministically`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(
        (
            "Ordinary factual text\nZONE U\nARTICLE U 1 - BODY\nBody text",
        )
    )
config = _config_with_structural_patterns(index)
```

**Action**

```python
records = _line_records(index, config)
events = _heading_events(records, config)
```

**Expected result**

```python
assert [event.section_type for event in events] == ["ZONE_CHAPTER", "ARTICLE"]
assert events[0].record_position == 1
assert events[0].zone_chapter_label == "U"
assert all(event.record_position != 0 for event in events)
```

**Regression protected**

Locks `unique zone heading and nonheading line are classified deterministically` through the exact asserted conditions: `[event.section_type for event in events] == ['ZONE_CHAPTER', 'ARTICLE']`; `events[0].record_position == 1`; `events[0].zone_chapter_label == 'U'`; `all((event.record_position != 0 for event in events))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unique_zone_heading_and_nonheading_line_are_classified_deterministically() -> None:
    index = _index(
        (
            "Ordinary factual text\nZONE U\nARTICLE U 1 - BODY\nBody text",
        )
    )
    config = _config_with_structural_patterns(index)
    records = _line_records(index, config)
    events = _heading_events(records, config)

    assert [event.section_type for event in events] == ["ZONE_CHAPTER", "ARTICLE"]
    assert events[0].record_position == 1
    assert events[0].zone_chapter_label == "U"
    assert all(event.record_position != 0 for event in events)
```

### `test_two_zone_patterns_matching_one_line_are_ambiguous`

**Purpose**

Exercises `two zone patterns matching one line are ambiguous`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(("ZONE U\nARTICLE U 1 - BODY\nBody",))
config = _config_with_structural_patterns(
        index,
        zone_chapter=(
            r"^ZONE\s+(?P<label>[A-Z]+)$",
            r"^ZONE[ ](?P<label>[A-Z]+)$",
        ),
    )
message = str(captured.value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
assert "Ambiguous structural heading" in message
assert "RECORD-000001" in message
assert "page 1" in message
assert "line 1" in message
assert "ZONE_CHAPTER[0]" in message
assert "ZONE_CHAPTER[1]" in message
assert "ZONE U" not in message
```

**Regression protected**

Locks `two zone patterns matching one line are ambiguous`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_two_zone_patterns_matching_one_line_are_ambiguous() -> None:
    index = _index(("ZONE U\nARTICLE U 1 - BODY\nBody",))
    config = _config_with_structural_patterns(
        index,
        zone_chapter=(
            r"^ZONE\s+(?P<label>[A-Z]+)$",
            r"^ZONE[ ](?P<label>[A-Z]+)$",
        ),
    )
    with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
    message = str(captured.value)
    assert "Ambiguous structural heading" in message
    assert "RECORD-000001" in message
    assert "page 1" in message
    assert "line 1" in message
    assert "ZONE_CHAPTER[0]" in message
    assert "ZONE_CHAPTER[1]" in message
    assert "ZONE U" not in message
```

### `test_two_article_patterns_matching_one_line_are_ambiguous`

**Purpose**

Exercises `two article patterns matching one line are ambiguous`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(("ZONE U\nARTICLE U 1 - BODY\nBody",))
config = _config_with_structural_patterns(
        index,
        article=(
            r"^ARTICLE\s+(?P<zone>[A-Z]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$",
            r"^ARTICLE[ ](?P<zone>[A-Z]+)[ ](?P<number>\d+)[ ]-[ ](?P<title>.*)$",
        ),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningRegulationStructureError,
        match=r"ARTICLE\[0\].*ARTICLE\[1\]",
    ):
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
```

**Regression protected**

Locks `two article patterns matching one line are ambiguous`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_two_article_patterns_matching_one_line_are_ambiguous() -> None:
    index = _index(("ZONE U\nARTICLE U 1 - BODY\nBody",))
    config = _config_with_structural_patterns(
        index,
        article=(
            r"^ARTICLE\s+(?P<zone>[A-Z]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$",
            r"^ARTICLE[ ](?P<zone>[A-Z]+)[ ](?P<number>\d+)[ ]-[ ](?P<title>.*)$",
        ),
    )
    with pytest.raises(
        PlanningRegulationStructureError,
        match=r"ARTICLE\[0\].*ARTICLE\[1\]",
    ):
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
```

### `test_general_and_article_cross_category_match_is_ambiguous`

**Purpose**

Exercises `general and article cross category match is ambiguous`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(("ARTICLE 1 - GENERAL\nBody",))
config = _config_with_structural_patterns(
        index,
        article=(
            r"^ARTICLE\s+(?P<zone>[A-Z]*)(?P<number>\d+)\s*-\s*(?P<title>.*)$",
        ),
    )
message = str(captured.value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
assert "GENERAL[0]" in message
assert "ARTICLE[0]" in message
```

**Regression protected**

Locks `general and article cross category match is ambiguous`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_general_and_article_cross_category_match_is_ambiguous() -> None:
    index = _index(("ARTICLE 1 - GENERAL\nBody",))
    config = _config_with_structural_patterns(
        index,
        article=(
            r"^ARTICLE\s+(?P<zone>[A-Z]*)(?P<number>\d+)\s*-\s*(?P<title>.*)$",
        ),
    )
    with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
    message = str(captured.value)
    assert "GENERAL[0]" in message
    assert "ARTICLE[0]" in message
```

### `test_zone_and_general_cross_category_match_is_ambiguous`

**Purpose**

Exercises `zone and general cross category match is ambiguous`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(("ZONE U\nBody",))
config = _config_with_structural_patterns(
        index,
        general_section=(
            r"^ZONE\s+(?P<number>[A-Z]+)(?P<title>)$",
        ),
    )
message = str(captured.value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
assert "ZONE_CHAPTER[0]" in message
assert "GENERAL[0]" in message
```

**Regression protected**

Locks `zone and general cross category match is ambiguous`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_zone_and_general_cross_category_match_is_ambiguous() -> None:
    index = _index(("ZONE U\nBody",))
    config = _config_with_structural_patterns(
        index,
        general_section=(
            r"^ZONE\s+(?P<number>[A-Z]+)(?P<title>)$",
        ),
    )
    with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
    message = str(captured.value)
    assert "ZONE_CHAPTER[0]" in message
    assert "GENERAL[0]" in message
```

### `test_identical_structural_regex_across_groups_is_rejected_by_config`

**Purpose**

Exercises `identical structural regex across groups is rejected by config`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
payload = _config(index).model_dump(mode="python")
repeated = r"^(?P<label>ZONE)$"
payload["heading_patterns"]["zone_chapter"] = (repeated,)
payload["heading_patterns"]["general_section"] = (repeated,)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="reused across groups"):
        PlanningRegulationStructureConfig.model_validate(payload)
```

**Regression protected**

Locks `identical structural regex across groups is rejected by config`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_identical_structural_regex_across_groups_is_rejected_by_config() -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    repeated = r"^(?P<label>ZONE)$"
    payload["heading_patterns"]["zone_chapter"] = (repeated,)
    payload["heading_patterns"]["general_section"] = (repeated,)
    with pytest.raises(ValueError, match="reused across groups"):
        PlanningRegulationStructureConfig.model_validate(payload)
```

### `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`

**Purpose**

Exercises `ambiguous continuation candidate fails with record diagnostic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index(("ARTICLE 1 - GENERAL\nAMBIGUOUS\nBody",))
config = _config_with_structural_patterns(
        index,
        zone_chapter=(
            r"^ZONE\s+(?P<label>[A-Z]+)$",
            r"^(?P<label>AMBIGUOUS)$",
        ),
        general_section=(
            r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$",
            r"^(?P<number>AMBIGUOUS)(?P<title>)$",
        ),
    )
message = str(captured.value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
assert "RECORD-000002" in message
assert "page 1" in message
assert "line 2" in message
assert "ZONE_CHAPTER[1]" in message
assert "GENERAL[1]" in message
```

**Regression protected**

Locks `ambiguous continuation candidate fails with record diagnostic`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_ambiguous_continuation_candidate_fails_with_record_diagnostic() -> None:
    index = _index(("ARTICLE 1 - GENERAL\nAMBIGUOUS\nBody",))
    config = _config_with_structural_patterns(
        index,
        zone_chapter=(
            r"^ZONE\s+(?P<label>[A-Z]+)$",
            r"^(?P<label>AMBIGUOUS)$",
        ),
        general_section=(
            r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$",
            r"^(?P<number>AMBIGUOUS)(?P<title>)$",
        ),
    )
    with pytest.raises(PlanningRegulationStructureError) as captured:
        structure_planning_regulation(
            index,
            _zones(index),
            _intersections(index),
            config,
        )
    message = str(captured.value)
    assert "RECORD-000002" in message
    assert "page 1" in message
    assert "line 2" in message
    assert "ZONE_CHAPTER[1]" in message
    assert "GENERAL[1]" in message
```

### `test_source_complete_validator_rejects_changed_ambiguous_grammar`

**Purpose**

Exercises `source complete validator rejects changed ambiguous grammar`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
config = _config(index)
patterns = config.heading_patterns.model_copy(
        update={
            "article": (
                *config.heading_patterns.article,
                r"^ARTICLE\s+(?P<zone>[A-Z]*)(?P<number>\d+)\s*-\s*(?P<title>.*)$",
            )
        }
    )
ambiguous = config.model_copy(update={"heading_patterns": patterns})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        PlanningRegulationStructureError,
        match="Ambiguous structural heading",
    ):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            _intersections(index),
            ambiguous,
            result,
        )
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_complete_validator_rejects_changed_ambiguous_grammar(
    valid_result,
) -> None:
    index, result = valid_result
    config = _config(index)
    patterns = config.heading_patterns.model_copy(
        update={
            "article": (
                *config.heading_patterns.article,
                r"^ARTICLE\s+(?P<zone>[A-Z]*)(?P<number>\d+)\s*-\s*(?P<title>.*)$",
            )
        }
    )
    ambiguous = config.model_copy(update={"heading_patterns": patterns})
    with pytest.raises(
        PlanningRegulationStructureError,
        match="Ambiguous structural heading",
    ):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            _intersections(index),
            ambiguous,
            result,
        )
```

### `test_normal_muret_compatible_grammar_remains_deterministic`

**Purpose**

Exercises `normal muret compatible grammar remains deterministic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
config = _config(index)
pd.testing.assert_frame_equal(first.sections, second.sections)
pd.testing.assert_frame_equal(first.zone_mapping, second.zone_mapping)
pd.testing.assert_frame_equal(first.topic_evidence, second.topic_evidence)
```

**Action**

```python
first = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
second = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
```

**Expected result**

```python
assert first.structure_result_content_sha256 == second.structure_result_content_sha256
```

**Regression protected**

Locks `normal muret compatible grammar remains deterministic` through the exact asserted conditions: `first.structure_result_content_sha256 == second.structure_result_content_sha256`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_normal_muret_compatible_grammar_remains_deterministic() -> None:
    index = _index()
    config = _config(index)
    first = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
    second = structure_planning_regulation(
        index,
        _zones(index),
        _intersections(index),
        config,
    )
    pd.testing.assert_frame_equal(first.sections, second.sections)
    pd.testing.assert_frame_equal(first.zone_mapping, second.zone_mapping)
    pd.testing.assert_frame_equal(first.topic_evidence, second.topic_evidence)
    assert first.structure_result_content_sha256 == second.structure_result_content_sha256
```

### `test_lossless_partition_mutation_is_rejected`

**Purpose**

Exercises `lossless partition mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `mutation`, `value`.

**Setup**

```python
index, result = valid_result
sections = result.sections.copy(deep=True)
sections.loc[0, mutation] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_lossless_partition_mutation_is_rejected(
    valid_result,
    mutation: str,
    value: object,
) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[0, mutation] = value
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))
```

### `test_duplicate_or_reordered_record_partition_is_rejected`

**Purpose**

Exercises `duplicate or reordered record partition is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
sections = result.sections.copy(deep=True)
sections.loc[1, "start_record_id"] = sections.loc[0, "start_record_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="partition"):
        _validate(index, replace(result, sections=sections))
```

**Regression protected**

Locks `duplicate or reordered record partition is rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_or_reordered_record_partition_is_rejected(valid_result) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[1, "start_record_id"] = sections.loc[0, "start_record_id"]
    with pytest.raises(PlanningRegulationStructureError, match="partition"):
        _validate(index, replace(result, sections=sections))
```

### `test_unsorted_section_pages_are_rejected`

**Purpose**

Exercises `unsorted section pages are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
sections = result.sections.copy(deep=True)
row_index = sections.index[sections["page_numbers"].map(len).gt(1)][0]
sections.at[row_index, "page_numbers"] = tuple(
        reversed(sections.at[row_index, "page_numbers"])
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="page references"):
        _validate(index, replace(result, sections=sections))
```

**Regression protected**

Locks `unsorted section pages are rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unsorted_section_pages_are_rejected(valid_result) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    row_index = sections.index[sections["page_numbers"].map(len).gt(1)][0]
    sections.at[row_index, "page_numbers"] = tuple(
        reversed(sections.at[row_index, "page_numbers"])
    )
    with pytest.raises(PlanningRegulationStructureError, match="page references"):
        _validate(index, replace(result, sections=sections))
```

### `test_article_parent_semantics_are_enforced`

**Purpose**

Exercises `article parent semantics are enforced`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
index, result = valid_result
sections = result.sections.copy(deep=True)
article_index = sections.index[sections["section_type"].eq("ARTICLE")][0]
if mutation == "missing_parent":
        sections.loc[article_index, "parent_section_id"] = None
    elif mutation == "parent_after":
        sections.loc[article_index, "parent_section_id"] = sections.iloc[-1]["section_id"]
    else:
        sections.loc[article_index, "zone_chapter_label"] = "N"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))
```

**Regression protected**

Locks `article parent semantics are enforced`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_article_parent_semantics_are_enforced(valid_result, mutation: str) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    article_index = sections.index[sections["section_type"].eq("ARTICLE")][0]
    if mutation == "missing_parent":
        sections.loc[article_index, "parent_section_id"] = None
    elif mutation == "parent_after":
        sections.loc[article_index, "parent_section_id"] = sections.iloc[-1]["section_id"]
    else:
        sections.loc[article_index, "zone_chapter_label"] = "N"
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))
```

### `test_wrong_intersection_source_zone_id_is_rejected`

**Purpose**

Exercises `wrong intersection source zone id is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
intersections = _intersections(index)
intersections.loc[0, "source_zone_id"] = "WRONG"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="source-zone"):
        validate_planning_regulation_structure(
            index, _zones(index), intersections, _config(index), result
        )
```

**Regression protected**

Locks `wrong intersection source zone id is rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_intersection_source_zone_id_is_rejected(valid_result) -> None:
    index, result = valid_result
    intersections = _intersections(index)
    intersections.loc[0, "source_zone_id"] = "WRONG"
    with pytest.raises(PlanningRegulationStructureError, match="source-zone"):
        validate_planning_regulation_structure(
            index, _zones(index), intersections, _config(index), result
        )
```

### `test_intersection_area_cannot_exceed_available_geometry_area`

**Purpose**

Exercises `intersection area cannot exceed available geometry area`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `upper_column`.

**Setup**

```python
index = _index()
intersections = _intersections(index)
intersections[upper_column] = [99.0, 50.0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="exceeds"):
        structure_planning_regulation(
            index, _zones(index), intersections, _config(index)
        )
```

**Regression protected**

Locks `intersection area cannot exceed available geometry area`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_intersection_area_cannot_exceed_available_geometry_area(
    upper_column: str,
) -> None:
    index = _index()
    intersections = _intersections(index)
    intersections[upper_column] = [99.0, 50.0]
    with pytest.raises(PlanningRegulationStructureError, match="exceeds"):
        structure_planning_regulation(
            index, _zones(index), intersections, _config(index)
        )
```

### `test_intersection_upper_bound_uses_shared_relative_tolerance`

**Purpose**

Exercises `intersection upper bound uses shared relative tolerance`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `upper_column`.

**Setup**

```python
index = _index()
config = _config(index)
reference_area = 1_000_000_000_000.0
within_tolerance = _intersections(index)
within_tolerance[upper_column] = [reference_area, 50.0]
within_tolerance.loc[0, "intersection_area_m2"] = (
        reference_area + tolerance / 2
    )
above_tolerance = within_tolerance.copy(deep=True)
above_tolerance.loc[0, "intersection_area_m2"] = (
        reference_area + tolerance * 2
    )
```

**Action**

```python
tolerance = technical_overlay_tolerance(reference_area)
result = structure_planning_regulation(
        index,
        _zones(index),
        within_tolerance,
        config,
    )
validate_planning_regulation_structure(
        index,
        _zones(index),
        within_tolerance,
        config,
        result,
    )
```

**Expected result**

```python
assert tolerance > 1e-6
with pytest.raises(PlanningRegulationStructureError, match="exceeds"):
        structure_planning_regulation(
            index,
            _zones(index),
            above_tolerance,
            config,
        )
```

**Regression protected**

Locks `intersection upper bound uses shared relative tolerance`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_intersection_upper_bound_uses_shared_relative_tolerance(
    upper_column: str,
) -> None:
    index = _index()
    config = _config(index)
    reference_area = 1_000_000_000_000.0
    tolerance = technical_overlay_tolerance(reference_area)
    assert tolerance > 1e-6

    within_tolerance = _intersections(index)
    within_tolerance[upper_column] = [reference_area, 50.0]
    within_tolerance.loc[0, "intersection_area_m2"] = (
        reference_area + tolerance / 2
    )
    result = structure_planning_regulation(
        index,
        _zones(index),
        within_tolerance,
        config,
    )
    validate_planning_regulation_structure(
        index,
        _zones(index),
        within_tolerance,
        config,
        result,
    )

    above_tolerance = within_tolerance.copy(deep=True)
    above_tolerance.loc[0, "intersection_area_m2"] = (
        reference_area + tolerance * 2
    )
    with pytest.raises(PlanningRegulationStructureError, match="exceeds"):
        structure_planning_regulation(
            index,
            _zones(index),
            above_tolerance,
            config,
        )
```

### `test_intersection_hash_columns_are_actual_and_deterministic`

**Purpose**

Exercises `intersection hash columns are actual and deterministic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `optional_columns`.

**Setup**

```python
index = _index()
intersections = _intersections(index)
for column in reversed(optional_columns):
        intersections.insert(0, column, [200.0, 100.0])
required = (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "relation_type",
        "intersection_area_m2",
        "source_document_id",
        "source_archive_sha256",
    )
expected_optional = tuple(
        column
        for column in ("parcel_metric_area_m2", "zone_area_m2")
        if column in optional_columns
    )
```

**Action**

```python
result = structure_planning_regulation(
        index,
        _zones(index),
        intersections,
        _config(index),
    )
validate_planning_regulation_structure(
        index,
        _zones(index),
        intersections,
        _config(index),
        result,
    )
```

**Expected result**

```python
assert result.zoning_intersection_hash_columns == required + expected_optional
```

**Regression protected**

Locks `intersection hash columns are actual and deterministic` through the exact asserted conditions: `result.zoning_intersection_hash_columns == required + expected_optional`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_intersection_hash_columns_are_actual_and_deterministic(
    optional_columns: tuple[str, ...],
) -> None:
    index = _index()
    intersections = _intersections(index)
    for column in reversed(optional_columns):
        intersections.insert(0, column, [200.0, 100.0])
    result = structure_planning_regulation(
        index,
        _zones(index),
        intersections,
        _config(index),
    )
    required = (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "relation_type",
        "intersection_area_m2",
        "source_document_id",
        "source_archive_sha256",
    )
    expected_optional = tuple(
        column
        for column in ("parcel_metric_area_m2", "zone_area_m2")
        if column in optional_columns
    )
    assert result.zoning_intersection_hash_columns == required + expected_optional
    validate_planning_regulation_structure(
        index,
        _zones(index),
        intersections,
        _config(index),
        result,
    )
```

### `test_optional_intersection_metric_change_invalidates_existing_result`

**Purpose**

Exercises `optional intersection metric change invalidates existing result`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `changed_column`.

**Setup**

```python
index = _index()
intersections = _intersections(index)
intersections["parcel_metric_area_m2"] = [200.0, 100.0]
intersections["zone_area_m2"] = [300.0, 150.0]
changed = intersections.copy(deep=True)
changed.loc[0, changed_column] += 1.0
```

**Action**

```python
result = structure_planning_regulation(
        index,
        _zones(index),
        intersections,
        _config(index),
    )
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="input hash"):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            changed,
            _config(index),
            result,
        )
```

**Regression protected**

Locks `optional intersection metric change invalidates existing result`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_optional_intersection_metric_change_invalidates_existing_result(
    changed_column: str,
) -> None:
    index = _index()
    intersections = _intersections(index)
    intersections["parcel_metric_area_m2"] = [200.0, 100.0]
    intersections["zone_area_m2"] = [300.0, 150.0]
    result = structure_planning_regulation(
        index,
        _zones(index),
        intersections,
        _config(index),
    )
    changed = intersections.copy(deep=True)
    changed.loc[0, changed_column] += 1.0
    with pytest.raises(PlanningRegulationStructureError, match="input hash"):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            changed,
            _config(index),
            result,
        )
```

### `test_intersection_hash_column_lineage_mutation_is_rejected`

**Purpose**

Exercises `intersection hash column lineage mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
intersections = _intersections(index)
intersections["parcel_metric_area_m2"] = [200.0, 100.0]
```

**Action**

```python
result = structure_planning_regulation(
        index,
        _zones(index),
        intersections,
        _config(index),
    )
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError, match="hash columns"):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            intersections,
            _config(index),
            replace(
                result,
                zoning_intersection_hash_columns=tuple(
                    reversed(result.zoning_intersection_hash_columns)
                ),
            ),
        )
```

**Regression protected**

Locks `intersection hash column lineage mutation is rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_intersection_hash_column_lineage_mutation_is_rejected() -> None:
    index = _index()
    intersections = _intersections(index)
    intersections["parcel_metric_area_m2"] = [200.0, 100.0]
    result = structure_planning_regulation(
        index,
        _zones(index),
        intersections,
        _config(index),
    )
    with pytest.raises(PlanningRegulationStructureError, match="hash columns"):
        validate_planning_regulation_structure(
            index,
            _zones(index),
            intersections,
            _config(index),
            replace(
                result,
                zoning_intersection_hash_columns=tuple(
                    reversed(result.zoning_intersection_hash_columns)
                ),
            ),
        )
```

### `test_zone_mapping_contract_mutations_are_rejected`

**Purpose**

Exercises `zone mapping contract mutations are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
index, result = valid_result
mapping = result.zone_mapping.copy(deep=True)
row_index = mapping.index[mapping["source_zone_label_raw"].eq("U")][0]
mapping.loc[row_index, column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, zone_mapping=mapping))
```

**Regression protected**

Locks `zone mapping contract mutations are rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_zone_mapping_contract_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
    index, result = valid_result
    mapping = result.zone_mapping.copy(deep=True)
    row_index = mapping.index[mapping["source_zone_label_raw"].eq("U")][0]
    mapping.loc[row_index, column] = value
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, zone_mapping=mapping))
```

### `test_alias_chain_resolves_to_final_configured_target`

**Purpose**

Exercises `alias chain resolves to final configured target`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index = _index()
config = _config(index).model_copy(update={"zone_aliases": {"Ua": "Urban", "Urban": "U"}})
mapping = result.zone_mapping.set_index("source_zone_label_raw")
```

**Action**

```python
result = structure_planning_regulation(
        index, _zones(index), _intersections(index), config
    )
```

**Expected result**

```python
assert mapping.at["Ua", "resolved_zone_chapter_label"] == "U"
assert mapping.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
assert mapping.at["X", "mapping_status"] == "UNMAPPED"
```

**Regression protected**

Locks `alias chain resolves to final configured target` through the exact asserted conditions: `mapping.at['Ua', 'resolved_zone_chapter_label'] == 'U'`; `mapping.at['Ua', 'mapping_status'] == 'CONFIG_ALIAS'`; `mapping.at['X', 'mapping_status'] == 'UNMAPPED'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_alias_chain_resolves_to_final_configured_target() -> None:
    index = _index()
    config = _config(index).model_copy(update={"zone_aliases": {"Ua": "Urban", "Urban": "U"}})
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), config
    )
    mapping = result.zone_mapping.set_index("source_zone_label_raw")
    assert mapping.at["Ua", "resolved_zone_chapter_label"] == "U"
    assert mapping.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert mapping.at["X", "mapping_status"] == "UNMAPPED"
```

### `test_token_boundary_and_longest_match_policy`

**Purpose**

Exercises `token boundary and longest match policy`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
raw = (
        "risque risques dérisque nuisance nuisances réseau réseaux "
        "équipement d'intérêt collectif intérêt collectif "
        "incendie défense contre l'incendie"
    )
terms = (
        "risque",
        "risques",
        "nuisance",
        "nuisances",
        "réseau",
        "réseaux",
        "équipement d'intérêt collectif",
        "intérêt collectif",
        "incendie",
        "défense contre l'incendie",
    )
retained = [match.search_term for match in matches]
```

**Action**

```python
normalized = normalize_planning_search_text(raw)
matches = _literal_topic_matches(normalized, terms)
```

**Expected result**

```python
assert retained.count("risque") == 1
assert retained.count("risques") == 1
assert retained.count("nuisance") == 1
assert retained.count("nuisances") == 1
assert retained.count("réseau") == 1
assert retained.count("réseaux") == 1
assert retained.count("équipement d'intérêt collectif") == 1
assert retained.count("intérêt collectif") == 1
assert retained.count("incendie") == 1
assert retained.count("défense contre l'incendie") == 1
assert len(matches) == 10
```

**Regression protected**

Locks `token boundary and longest match policy` through the exact asserted conditions: `retained.count('risque') == 1`; `retained.count('risques') == 1`; `retained.count('nuisance') == 1`; `retained.count('nuisances') == 1`; plus 7 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_token_boundary_and_longest_match_policy() -> None:
    raw = (
        "risque risques dérisque nuisance nuisances réseau réseaux "
        "équipement d'intérêt collectif intérêt collectif "
        "incendie défense contre l'incendie"
    )
    normalized = normalize_planning_search_text(raw)
    terms = (
        "risque",
        "risques",
        "nuisance",
        "nuisances",
        "réseau",
        "réseaux",
        "équipement d'intérêt collectif",
        "intérêt collectif",
        "incendie",
        "défense contre l'incendie",
    )
    matches = _literal_topic_matches(normalized, terms)
    retained = [match.search_term for match in matches]
    assert retained.count("risque") == 1
    assert retained.count("risques") == 1
    assert retained.count("nuisance") == 1
    assert retained.count("nuisances") == 1
    assert retained.count("réseau") == 1
    assert retained.count("réseaux") == 1
    assert retained.count("équipement d'intérêt collectif") == 1
    assert retained.count("intérêt collectif") == 1
    assert retained.count("incendie") == 1
    assert retained.count("défense contre l'incendie") == 1
    assert len(matches) == 10
```

### `test_topic_evidence_semantic_mutations_are_rejected`

**Purpose**

Exercises `topic evidence semantic mutations are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
index, result = valid_result
evidence = result.topic_evidence.copy(deep=True)
zone_rows = evidence.index[evidence["evidence_scope"].eq("ZONE_SPECIFIC_RULE")]
row_index = zone_rows[0] if len(zone_rows) else evidence.index[0]
evidence.loc[row_index, column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, topic_evidence=evidence))
```

**Regression protected**

Locks `topic evidence semantic mutations are rejected`: the reproduced adversarial input must raise `PlanningRegulationStructureError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_topic_evidence_semantic_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    zone_rows = evidence.index[evidence["evidence_scope"].eq("ZONE_SPECIFIC_RULE")]
    row_index = zone_rows[0] if len(zone_rows) else evidence.index[0]
    evidence.loc[row_index, column] = value
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, topic_evidence=evidence))
```

### `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`

**Purpose**

Exercises `coordinated topic evidence and hash mutation is rebuilt and rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
index, result = valid_result
evidence = result.topic_evidence.copy(deep=True)
evidence.loc[0, "raw_context"] = "fabricated"
```

**Action**

```python
changed = _result_with_hashes(
        replace(
            result,
            topic_evidence=evidence,
            sections_content_sha256="",
            zone_map_content_sha256="",
            topic_evidence_content_sha256="",
            structure_result_content_sha256="",
        )
    )
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected(
    valid_result,
) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    evidence.loc[0, "raw_context"] = "fabricated"
    changed = _result_with_hashes(
        replace(
            result,
            topic_evidence=evidence,
            sections_content_sha256="",
            zone_map_content_sha256="",
            topic_evidence_content_sha256="",
            structure_result_content_sha256="",
        )
    )
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)
```

### `test_source_complete_validator_rejects_post_build_source_change`

**Purpose**

Exercises `source complete validator rejects post build source change`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `source_change`.

**Setup**

```python
index, result = valid_result
zones = _zones(index)
intersections = _intersections(index)
config = _config(index)
if source_change == "alias":
        config = config.model_copy(update={"zone_aliases": {"Ua": "N"}})
    elif source_change == "topic":
        config = config.model_copy(update={"topics": {"energy": ("electricity",), "risk": ("risk",)}})
    elif source_change == "heading":
        patterns = config.heading_patterns.model_copy(
            update={"zone_chapter": (r"^ZONE\s+(?P<label>[A-Za-z0-9]+)\s*$",)}
        )
        config = config.model_copy(update={"heading_patterns": patterns})
    elif source_change == "zone":
        zones.loc[0, "source_zone_id"] = "CHANGED"
        intersections.loc[0, "source_zone_id"] = "CHANGED"
    elif source_change == "area":
        intersections.loc[0, "intersection_area_m2"] = 99.0
    else:
        intersections.loc[0, "relation_type"] = "TOUCH_ONLY"
        intersections.loc[0, "intersection_area_m2"] = 0.0
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        validate_planning_regulation_structure(
            index, zones, intersections, config, result
        )
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_complete_validator_rejects_post_build_source_change(
    valid_result,
    source_change: str,
) -> None:
    index, result = valid_result
    zones = _zones(index)
    intersections = _intersections(index)
    config = _config(index)
    if source_change == "alias":
        config = config.model_copy(update={"zone_aliases": {"Ua": "N"}})
    elif source_change == "topic":
        config = config.model_copy(update={"topics": {"energy": ("electricity",), "risk": ("risk",)}})
    elif source_change == "heading":
        patterns = config.heading_patterns.model_copy(
            update={"zone_chapter": (r"^ZONE\s+(?P<label>[A-Za-z0-9]+)\s*$",)}
        )
        config = config.model_copy(update={"heading_patterns": patterns})
    elif source_change == "zone":
        zones.loc[0, "source_zone_id"] = "CHANGED"
        intersections.loc[0, "source_zone_id"] = "CHANGED"
    elif source_change == "area":
        intersections.loc[0, "intersection_area_m2"] = 99.0
    else:
        intersections.loc[0, "relation_type"] = "TOUCH_ONLY"
        intersections.loc[0, "intersection_area_m2"] = 0.0
    with pytest.raises(PlanningRegulationStructureError):
        validate_planning_regulation_structure(
            index, zones, intersections, config, result
        )
```

### `test_source_and_result_hash_mutation_is_rejected`

**Purpose**

Exercises `source and result hash mutation is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `valid_result` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `hash_field`.

**Setup**

```python
index, result = valid_result
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, **{hash_field: "f" * 64}))
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_and_result_hash_mutation_is_rejected(valid_result, hash_field: str) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, **{hash_field: "f" * 64}))
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
