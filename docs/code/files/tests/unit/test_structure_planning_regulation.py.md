# `tests/unit/test_structure_planning_regulation.py`

## File identity

- Repository path: `tests/unit/test_structure_planning_regulation.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Exercises the synthetic structure contracts and bounded assertions documented below; it does not establish exhaustive or official-source coverage.
- Source SHA256: `80ab6feaf5e77d99f538c1aab53f0520f496a45c18758a7d33d4c7554646b6d2`
- Source SHA256 basis: `git-content`
- R13 verification basis: `ddaf1458bf0b0be56bcae8ee0b7452ab7a23d679`; source bytes unchanged.

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for structure planning regulation; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## R13 fixture and evidence boundary

All page/index facts here are synthetic; no original PDF, GPU package, network source, geometry overlay or official Muret configuration is opened. Only the two loader tests write temporary YAML and delegate reads to the public config loader. No monkeypatch counter/no-op/sentinel arrangement is present in this file. Public result tests do perform the real in-memory reconstruction, whereas direct helper and model tests do not implicitly exercise the entire boundary. The three result DataFrames are mutable even though the lineage dataclass is frozen.

The per-test purpose paragraphs qualify earliest possible failures. In particular, invalid-regex plus extra-field input is combined, page zero may fail config reconstruction, unchanged section row hashes precede parent semantics, and fabricated context is compared to rebuilt fragments before final expected-frame equality. These are proof limits, not new production defects. Matching a test title or counting assertions does not establish a stronger invariant.

## 2. Purpose and architectural position

Exercises the synthetic structure contracts and bounded assertions documented below; it does not establish exhaustive or official-source coverage.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import replace`
- `from pathlib import Path`

### Third-party packages

- `import pandas as pd`
- `import pytest`
- `import yaml` (local to the two temporary-YAML loader tests)

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

<a id="r13--index"></a>
### `_index`

Qualified owner: `tests.unit.test_structure_planning_regulation._index`. Source lines 39–84.

**Purpose:** Creates a self-hashed synthetic PlanningRegulationIndex from supplied page strings or seven default Test PLU pages (TOC, general provisions, U/N chapters and two Z chapters). It derives TEXT/EMPTY, normalized text and character counts, hashes every page and the pages envelope, then replaces the complete index digest. doc-1 and repeated-letter archive/PDF identities are fixture values; no PDF is opened or extracted.

**Exact signature**

```python
def _index(raw_pages: tuple[str, ...] | None = None) -> PlanningRegulationIndex:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationIndex`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw_pages` | positional-or-keyword | `tuple[str, ...] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(index, index_content_sha256=_index_content_sha256(index))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_structure_planning_regulation::valid_result` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::valid_result` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_config_schema_versions_are_rejected` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_config_schema_versions_are_rejected` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_accepts_exact_booleans` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_accepts_exact_booleans` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_structure_decision_mappings_are_deeply_immutable` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_structure_decision_mappings_are_deeply_immutable` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_positional_header_footer_filter_preserves_matching_body_lines` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_positional_header_footer_filter_preserves_matching_body_lines` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_page_without_configured_header_or_footer_is_unchanged` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_page_without_configured_header_or_footer_is_unchanged` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_heading_patterns_require_mandatory_named_captures` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_heading_patterns_require_mandatory_named_captures` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_pattern_lists_may_be_empty` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_pattern_lists_may_be_empty` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_identical_structural_regex_across_groups_is_rejected_by_config` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_identical_structural_regex_across_groups_is_rejected_by_config` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_index`
- direct call: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_index`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_index`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text` | `landscout.common.planning_text.normalize_planning_search_text` via the index alias |
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13--config"></a>
### `_config`

Qualified owner: `tests.unit.test_structure_planning_regulation._config`. Source lines 87–127.

**Purpose:** Validates an in-memory schema-2 synthetic_v1 grammar locked to the supplied index. Defaults select body page 1, TOC page 1, two continuation lines, Test PLU headers and numeric footers, Ua→U, energy/risk terms, token_longest_match and a 20-normalized-character context margin. It does not load the Muret YAML.

**Exact signature**

```python
def _config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
```

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationStructureConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `PlanningRegulationStructureConfig.model_validate(<br>        {<br>            "schema_version": 2,<br>            "structure_profile": "synthetic_v1",<br>            "document_lock": {<br>                "document_id": index.document_id,<br>                "pdf_sha256": index.pdf_sha256,<br>                "pages_content_sha256": index.pages_content_sha256,<br>                "index_content_sha256": index.index_content_sha256,<br>                "normalization_profile": index.search_normalization_profile,<br>            },<br>            "document_layout": {<br>                "body_start_page": 1,<br>                "table_of_contents_pages": [1],<br>                "max_heading_continuation_lines": 2,<br>                "include_table_of_contents_in_topic_evidence": False,<br>            },<br>            "heading_patterns": {<br>                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],<br>                "article": [<br>                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*[-–—]\s*(?P<title>.*)$"<br>                ],<br>                "general_section": [<br>                    r"^ARTICLE\s+(?P<number>\d+)\s*[-–—]\s*(?P<title>.*)$"<br>                ],<br>                "continuation": [r"^[^a-z]*[A-Z][^a-z]*$"],<br>            },<br>            "ignored_patterns": {<br>                "page_headers": [r"^Test PLU$"],<br>                "page_footers": [r"^\d+$"],<br>            },<br>            "zone_aliases": {"Ua": "U"},<br>            "topics": {"energy": ["energy"], "risk": ["risk"]},<br>            "topic_match_policy": {<br>                "boundary_mode": "token",<br>                "overlap_resolution": "longest_match",<br>            },<br>            "topic_context_characters": 20,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_structure_planning_regulation::valid_result` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::valid_result` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::_validate` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::_validate` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_structure_schema_versions_are_explicit` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_structure_schema_versions_are_explicit` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_config_schema_versions_are_rejected` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_config_schema_versions_are_rejected` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_accepts_exact_booleans` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_accepts_exact_booleans` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_invalid_regex_and_unknown_yaml_field_are_controlled` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_duplicate_yaml_alias_and_alias_cycle_are_rejected` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_structure_decision_mappings_are_deeply_immutable` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_structure_decision_mappings_are_deeply_immutable` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_positional_header_footer_filter_preserves_matching_body_lines` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_positional_header_footer_filter_preserves_matching_body_lines` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_page_without_configured_header_or_footer_is_unchanged` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_page_without_configured_header_or_footer_is_unchanged` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_heading_patterns_require_mandatory_named_captures` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_heading_patterns_require_mandatory_named_captures` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_pattern_lists_may_be_empty` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_pattern_lists_may_be_empty` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::_config_with_structural_patterns` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::_config_with_structural_patterns` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_identical_structural_regex_across_groups_is_rejected_by_config` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_identical_structural_regex_across_groups_is_rejected_by_config` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_config`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `_config`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13--zones"></a>
### `_zones`

Qualified owner: `tests.unit.test_structure_planning_regulation._zones`. Source lines 130–140.

**Purpose:** Returns five non-geometric catalog rows labelled U, Ua, X, UX and Z, with ZONE-/SRC- identifiers and document/archive lineage copied from the index. This is a DataFrame fixture, not a GPU physical zoning read.

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
  - `pd.DataFrame(<br>        {<br>            "planning_zone_id": [f"ZONE-{label}" for label in labels],<br>            "source_zone_id": [f"SRC-{label}" for label in labels],<br>            "zone_label_raw": labels,<br>            "source_document_id": index.document_id,<br>            "source_archive_sha256": index.archive_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_structure_planning_regulation::valid_result` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::valid_result` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::_validate` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::_validate` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_zones`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `_zones`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `_zones`

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13--intersections"></a>
### `_intersections`

Qualified owner: `tests.unit.test_structure_planning_regulation._intersections`. Source lines 143–155.

**Purpose:** Returns two synthetic AREA_OVERLAP rows: PARCEL-1/U/100.0 and PARCEL-2/Ua/50.0, with matching source identifiers and index lineage. No optional upper-area columns or geometry calculation are present.

**Exact signature**

```python
def _intersections(index: PlanningRegulationIndex) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(<br>        {<br>            "parcel_id": ["PARCEL-1", "PARCEL-2"],<br>            "planning_zone_id": ["ZONE-U", "ZONE-Ua"],<br>            "source_zone_id": ["SRC-U", "SRC-Ua"],<br>            "zone_label_raw": ["U", "Ua"],<br>            "relation_type": ["AREA_OVERLAP", "AREA_OVERLAP"],<br>            "intersection_area_m2": [100.0, 50.0],<br>            "source_document_id": index.document_id,<br>            "source_archive_sha256": index.archive_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_structure_planning_regulation::valid_result` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::valid_result` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::_validate` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::_validate` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_rejects_nonexistent_indexed_pages` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_lock_mismatch_is_rejected` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_inputs_are_not_mutated` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_body_page_extraction_error_stops_structure` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_successfully_extracted_body_page_remains_valid` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_dominant_unmapped_zone_stops_processing` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_normal_muret_compatible_grammar_remains_deterministic` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_area_cannot_exceed_available_geometry_area` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_upper_bound_uses_shared_relative_tolerance` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_columns_are_actual_and_deterministic` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_intersection_metric_change_invalidates_existing_result` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_intersection_hash_column_lineage_mutation_is_rejected` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_alias_chain_resolves_to_final_configured_target` via `_intersections`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `_intersections`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `_intersections`

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-valid-result"></a>
### `valid_result`

Qualified owner: `tests.unit.test_structure_planning_regulation.valid_result`. Source lines 159–164.

**Purpose:** The pytest fixture builds from _index, _zones, _intersections and _config and returns the pair (index, result). Its result has already traversed the public builder and its delegated in-memory validation; this is not a source-acquisition fixture. The function has no return annotation.

**Exact signature**

```python
def valid_result():
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: not declared (not `-> None`).

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `index, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_can_return_validated_fragments` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_structure_schema_versions_are_explicit` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_result_config_schema_versions_are_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_section_hash_schema_versions_are_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_realistic_structure_is_deterministic_and_toc_heading_is_ignored` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_article_parent_and_multi_page_text_are_preserved` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_topic_evidence_distinguishes_general_and_zone_specific` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_frame_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unknown_topic_page_reference_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_changed_ambiguous_grammar` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_lossless_partition_mutation_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_duplicate_or_reordered_record_partition_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unsorted_section_pages_are_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_article_parent_semantics_are_enforced` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_wrong_intersection_source_zone_id_is_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_mapping_contract_mutations_are_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_topic_evidence_semantic_mutations_are_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_complete_validator_rejects_post_build_source_change` via `valid_result`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_and_result_hash_mutation_is_rejected` via `valid_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |

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
def valid_result():
    index = _index()
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), _config(index)
    )
    return index, result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13--validate"></a>
### `_validate`

Qualified owner: `tests.unit.test_structure_planning_regulation._validate`. Source lines 167–177.

**Purpose:** Calls the five-argument public validator with the supplied index/result and freshly regenerated synthetic zones, intersections and config. It returns None and does not reseal a mutated result or replace the supplied index.

**Exact signature**

```python
def _validate(
    index: PlanningRegulationIndex,
    result,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_result_config_schema_versions_are_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_result_config_schema_versions_are_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_section_hash_schema_versions_are_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_section_hash_schema_versions_are_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_realistic_structure_is_deterministic_and_toc_heading_is_ignored` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_realistic_structure_is_deterministic_and_toc_heading_is_ignored` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_coordinated_frame_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_frame_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_unknown_topic_page_reference_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unknown_topic_page_reference_is_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_section_row_mutation_is_caught_by_outer_envelope` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_lossless_partition_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_lossless_partition_mutation_is_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_duplicate_or_reordered_record_partition_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_duplicate_or_reordered_record_partition_is_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_unsorted_section_pages_are_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unsorted_section_pages_are_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_article_parent_semantics_are_enforced` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_article_parent_semantics_are_enforced` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_zone_mapping_contract_mutations_are_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_mapping_contract_mutations_are_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_topic_evidence_semantic_mutations_are_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_topic_evidence_semantic_mutations_are_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` via `_validate`
- direct call: `tests.unit.test_structure_planning_regulation::test_source_and_result_hash_mutation_is_rejected` via `_validate`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_source_and_result_hash_mutation_is_rejected` via `_validate`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-package-exports-clean-high-level-api"></a>
### `test_package_exports_clean_high_level_api`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_package_exports_clean_high_level_api`. Source lines 180–184.

**Purpose:** Checks membership of the builder and two validator names in stages.__all__, and absence of names beginning _build_. It does not assert equality with the complete eight-export inventory.

**Exact signature**

```python
def test_package_exports_clean_high_level_api() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert "structure_planning_regulation" in stages.__all__`
  - `assert "validate_planning_regulation_structure" in stages.__all__`
  - `assert "validate_planning_regulation_structure_with_fragments" in stages.__all__`
  - `assert not any(name.startswith("_build_") for name in stages.__all__)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.startswith` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_package_exports_clean_high_level_api() -> None:
    assert "structure_planning_regulation" in stages.__all__
    assert "validate_planning_regulation_structure" in stages.__all__
    assert "validate_planning_regulation_structure_with_fragments" in stages.__all__
    assert not any(name.startswith("_build_") for name in stages.__all__)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-source-complete-validator-can-return-validated-fragments"></a>
### `test_source_complete_validator_can_return_validated_fragments`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_source_complete_validator_can_return_validated_fragments`. Source lines 187–209.

**Purpose:** Unpacks valid_result and invokes the fragment-returning public validator with all five in-memory inputs. Asserts the exact ten-column tuple, uniqueness of (section_id, page_number), and uniform document_id. It does not independently recompute fragment hashes or compare all raw fragment texts.

**Exact signature**

```python
def test_source_complete_validator_can_return_validated_fragments(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(fragments.columns) == (<br>        "section_id",<br>        "page_number",<br>        "raw_text",<br>        "section_page_fragment_sha256",<br>        "document_id",<br>        "archive_sha256",<br>        "pdf_sha256",<br>        "index_content_sha256",<br>        "structure_result_content_sha256",<br>        "structure_profile",<br>    )`
  - `assert not fragments.duplicated(["section_id", "page_number"]).any()`
  - `assert fragments["document_id"].eq(index.document_id).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_structure_with_fragments` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure_with_fragments` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `fragments.duplicated(["section_id", "page_number"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `fragments.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `fragments["document_id"].eq(index.document_id).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `fragments["document_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-structure-schema-versions-are-explicit"></a>
### `test_structure_schema_versions_are_explicit`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_structure_schema_versions_are_explicit`. Source lines 212–219.

**Purpose:** From the synthetic fixture, asserts config/result config version 2, constant/result section hash version 3 and manifest constant 4. No manifest artifact is loaded.

**Exact signature**

```python
def test_structure_schema_versions_are_explicit(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert config.schema_version == 2`
  - `assert result.structure_config_schema_version == 2`
  - `assert SECTION_HASH_SCHEMA_VERSION == 3`
  - `assert result.section_hash_schema_version == 3`
  - `assert STRUCTURE_MANIFEST_SCHEMA_VERSION == 4`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_structure_planning_regulation._config` |

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
def test_structure_schema_versions_are_explicit(valid_result) -> None:
    index, result = valid_result
    config = _config(index)
    assert config.schema_version == 2
    assert result.structure_config_schema_version == 2
    assert SECTION_HASH_SCHEMA_VERSION == 3
    assert result.section_hash_schema_version == 3
    assert STRUCTURE_MANIFEST_SCHEMA_VERSION == 4
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-old-and-unknown-config-schema-versions-are-rejected"></a>
### `test_old_and_unknown_config_schema_versions_are_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_old_and_unknown_config_schema_versions_are_rejected`. Source lines 223–230.

**Purpose:** Changes only the dumped config schema_version to 1 or 3 and requires model validation to raise ValueError matching unsupported structure config schema. This is a model-only boundary, not the file loader.

**Exact signature**

```python
def test_old_and_unknown_config_schema_versions_are_rejected(
    schema_version: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("schema_version", [1, 3])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `schema_version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="unsupported structure config schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `pytest.raises` | `pytest.raises` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
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
| In-memory mutation | `payload["schema_version"] = schema_version` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-old-and-unknown-result-config-schema-versions-are-rejected"></a>
### `test_old_and_unknown_result_config_schema_versions_are_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_old_and_unknown_result_config_schema_versions_are_rejected`. Source lines 234–243.

**Purpose:** Replaces only the result config schema version by 1 or 3; _validate must raise PlanningRegulationStructureError matching schema version. The original factual inputs remain unchanged.

**Exact signature**

```python
def test_old_and_unknown_result_config_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("schema_version", [1, 3])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `schema_version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="schema version")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-old-and-unknown-section-hash-schema-versions-are-rejected"></a>
### `test_old_and_unknown_section_hash_schema_versions_are_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_old_and_unknown_section_hash_schema_versions_are_rejected`. Source lines 247–253.

**Purpose:** Replaces only the result section hash version by 1, 2 or 4, then requires the public validation helper to raise PlanningRegulationStructureError matching schema version.

**Exact signature**

```python
def test_old_and_unknown_section_hash_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("schema_version", [1, 2, 4])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `schema_version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="schema version")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
def test_old_and_unknown_section_hash_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError, match="schema version"):
        _validate(index, replace(result, section_hash_schema_version=schema_version))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-toc-topic-evidence-flag-rejects-boolean-coercion"></a>
### `test_toc_topic_evidence_flag_rejects_boolean_coercion`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_toc_topic_evidence_flag_rejects_boolean_coercion`. Source lines 257–262.

**Purpose:** Puts 0, 1, false/true strings or yes into the dumped TOC evidence flag and requires ValueError from model_validate. It tests these five non-bool inputs, not all possible coercions.

**Exact signature**

```python
def test_toc_topic_evidence_flag_rejects_boolean_coercion(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [0, 1, "false", "true", "yes"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

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
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `pytest.raises` | `pytest.raises` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
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
| In-memory mutation | `payload["document_layout"]["include_table_of_contents_in_topic_evidence"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_toc_topic_evidence_flag_rejects_boolean_coercion(value: object) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["include_table_of_contents_in_topic_evidence"] = value
    with pytest.raises(ValueError):
        PlanningRegulationStructureConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-toc-topic-evidence-flag-accepts-exact-booleans"></a>
### `test_toc_topic_evidence_flag_accepts_exact_booleans`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_toc_topic_evidence_flag_accepts_exact_booleans`. Source lines 266–273.

**Purpose:** Validates each exact False/True flag and asserts identity (is) with the supplied Boolean; no builder execution is performed by this test body.

**Exact signature**

```python
def test_toc_topic_evidence_flag_accepts_exact_booleans(value: bool) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [False, True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        validated.document_layout.include_table_of_contents_in_topic_evidence is value<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
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
| In-memory mutation | `payload["document_layout"]["include_table_of_contents_in_topic_evidence"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_toc_topic_evidence_flag_accepts_exact_booleans(value: bool) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["include_table_of_contents_in_topic_evidence"] = value
    validated = PlanningRegulationStructureConfig.model_validate(payload)
    assert (
        validated.document_layout.include_table_of_contents_in_topic_evidence is value
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-document-layout-accepts-real-first-and-last-indexed-pages"></a>
### `test_document_layout_accepts_real_first_and_last_indexed_pages`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_document_layout_accepts_real_first_and_last_indexed_pages`. Source lines 276–294.

**Purpose:** Builds three synthetic pages with TOC pages (1, 3), body start 1 and a U body on page 2 through the layout helper, validates again, and asserts first/last section page tuples (1,) and (3,). Real means present in this synthetic index.

**Exact signature**

```python
def test_document_layout_accepts_real_first_and_last_indexed_pages() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.sections.iloc[0]["page_numbers"] == (1,)`
  - `assert result.sections.iloc[-1]["page_numbers"] == (3,)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_structure_with_document_layout` | `tests.unit.test_structure_planning_regulation._structure_with_document_layout` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-document-layout-rejects-nonexistent-indexed-pages"></a>
### `test_document_layout_rejects_nonexistent_indexed_pages`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_document_layout_rejects_nonexistent_indexed_pages`. Source lines 305–319.

**Purpose:** Uses unchecked nested model_copy updates for TOC (0,), TOC (8,) or body start 8 and expects PlanningRegulationStructureError from the builder. Zero can fail during reconstructed config validation before index membership; the test does not isolate that later guard for every case.

**Exact signature**

```python
def test_document_layout_rejects_nonexistent_indexed_pages(
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("table_of_contents_pages", (0,)),
        ("table_of_contents_pages", (8,)),
        ("body_start_page", 8),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `config.document_layout.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-existing-empty-toc-page-is-valid-not-nonexistent"></a>
### `test_existing_empty_toc_page_is_valid_not_nonexistent`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_existing_empty_toc_page_is_valid_not_nonexistent`. Source lines 322–338.

**Purpose:** Builds an empty first TOC page and U body page 2, asserts EMPTY on the first indexed page and completes public validation. This distinguishes an existing empty page from a missing page number.

**Exact signature**

```python
def test_existing_empty_toc_page_is_valid_not_nonexistent() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert index.pages.loc[0, "extraction_status"] == "EMPTY"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_structure_with_document_layout` | `tests.unit.test_structure_planning_regulation._structure_with_document_layout` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-document-lock-mismatch-is-rejected"></a>
### `test_document_lock_mismatch_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_document_lock_mismatch_is_rejected`. Source lines 351–361.

**Purpose:** Individually changes each of the five lock fields using model_copy (f×64 for digests, wrong otherwise), preserving the index. Builder rejection must be PlanningRegulationStructureError matching document lock.

**Exact signature**

```python
def test_document_lock_mismatch_is_rejected(lock_field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "lock_field",
    [
        "document_id",
        "pdf_sha256",
        "pages_content_sha256",
        "index_content_sha256",
        "normalization_profile",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `lock_field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="document lock")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `config.document_lock.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
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
def test_document_lock_mismatch_is_rejected(lock_field: str) -> None:
    index = _index()
    config = _config(index)
    lock = config.document_lock.model_copy(
        update={lock_field: "f" * 64 if "sha256" in lock_field else "wrong"}
    )
    changed = config.model_copy(update={"document_lock": lock})
    with pytest.raises(PlanningRegulationStructureError, match="document lock"):
        structure_planning_regulation(
            index, _zones(index), _intersections(index), changed
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-invalid-regex-and-unknown-yaml-field-are-controlled"></a>
### `test_invalid_regex_and_unknown_yaml_field_are_controlled`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_invalid_regex_and_unknown_yaml_field_are_controlled`. Source lines 364–374.

**Purpose:** Writes temporary bad.yaml containing both zone regex [ and unexpected=True, then requires a controlled loader error without a message constraint. The combined malformed input does not independently prove the regex guard: extra-field rejection may precede the after-validator.

**Exact signature**

```python
def test_invalid_regex_and_unknown_yaml_field_are_controlled(tmp_path: Path) -> None:
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
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |
| `pytest.raises` | `pytest.raises` |
| `load_planning_regulation_structure_config` | `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config` |

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
| In-memory mutation | `payload["heading_patterns"]["zone_chapter"] = ["["]`<br>`payload["unexpected"] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-duplicate-yaml-alias-and-alias-cycle-are-rejected"></a>
### `test_duplicate_yaml_alias_and_alias_cycle_are_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_duplicate_yaml_alias_and_alias_cycle_are_rejected`. Source lines 377–392.

**Purpose:** Writes and loads two separate temporary YAML files: A→B→A must raise a controlled error; duplicated A mapping keys injected under zone_aliases must raise PlanningRegulationStructureError matching Duplicate YAML. str.replace changes text in memory, not a filesystem path.

**Exact signature**

```python
def test_duplicate_yaml_alias_and_alias_cycle_are_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(PlanningRegulationStructureError)`
  - `pytest.raises(PlanningRegulationStructureError, match="Duplicate YAML")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `cycle.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |
| `pytest.raises` | `pytest.raises` |
| `load_planning_regulation_structure_config` | `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config` |
| `text.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `duplicate.write_text` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `cycle.write_text`<br>`duplicate.write_text` (text.replace is in-memory string construction) |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `config["zone_aliases"] = {"A": "B", "B": "A"}` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-realistic-structure-is-deterministic-and-toc-heading-is-ignored"></a>
### `test_realistic_structure_is_deterministic_and_toc_heading_is_ignored`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_realistic_structure_is_deterministic_and_toc_heading_is_ignored`. Source lines 395–408.

**Purpose:** Validates the default synthetic result, checks sequential section IDs, chapter labels exactly [U, N, Z, Z] with one U chapter, and the first GENERAL heading/text. No second build or real PDF is compared here.

**Exact signature**

```python
def test_realistic_structure_is_deterministic_and_toc_heading_is_ignored(
    valid_result,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.sections["section_id"].tolist() == [<br>        f"SECTION-{number:04d}" for number in range(1, len(result.sections) + 1)<br>    ]`
  - `assert chapters["zone_chapter_label"].tolist() == ["U", "N", "Z", "Z"]`
  - `assert len(chapters.loc[chapters["zone_chapter_label"].eq("U")]) == 1`
  - `assert general["heading_raw"] == "ARTICLE 1 - GENERAL PROVISIONS"`
  - `assert "General energy rule." in general["raw_text"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
| `result.sections["section_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapters["zone_chapter_label"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapters["zone_chapter_label"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-zone-article-parent-and-multi-page-text-are-preserved"></a>
### `test_zone_article_parent_and_multi_page_text_are_preserved`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_zone_article_parent_and_multi_page_text_are_preserved`. Source lines 411–420.

**Purpose:** Selects the ARTICLE U 1 row, follows its parent ID and asserts a ZONE_CHAPTER parent, page tuple (3, 4), and both expected page-text substrings. It does not assert all parent fields or fragment hashes.

**Exact signature**

```python
def test_zone_article_parent_and_multi_page_text_are_preserved(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parent["section_type"] == "ZONE_CHAPTER"`
  - `assert tuple(article["page_numbers"]) == (3, 4)`
  - `assert "First page energy text." in article["raw_text"]`
  - `assert "Second page of the same article." in article["raw_text"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.sections["heading_raw"].str.startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.sections.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-exact-alias-unmapped-ambiguous-and-no-fuzzy-mapping"></a>
### `test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping`. Source lines 423–431.

**Purpose:** Checks U=EXACT, Ua=CONFIG_ALIAS, X/UX=UNMAPPED, Z=AMBIGUOUS and X dominant count zero in the default result. No policy/BESS classification or universal fuzzy-match test follows from those selected cells.

**Exact signature**

```python
def test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert mappings.at["U", "mapping_status"] == "EXACT"`
  - `assert mappings.at["Ua", "mapping_status"] == "CONFIG_ALIAS"`
  - `assert mappings.at["X", "mapping_status"] == "UNMAPPED"`
  - `assert mappings.at["UX", "mapping_status"] == "UNMAPPED"`
  - `assert mappings.at["Z", "mapping_status"] == "AMBIGUOUS"`
  - `assert mappings.at["X", "dominant_candidate_count"] == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.zone_mapping.set_index` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-topic-evidence-distinguishes-general-and-zone-specific"></a>
### `test_topic_evidence_distinguishes_general_and_zone_specific`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_topic_evidence_distinguishes_general_and_zone_specific`. Source lines 434–439.

**Purpose:** Filters energy evidence and asserts exactly the two GENERAL_RULE/ZONE_SPECIFIC_RULE scope values, occurrence-count set {1}, and truthy raw contexts; it does not assert exact context strings.

**Exact signature**

```python
def test_topic_evidence_distinguishes_general_and_zone_specific(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(energy["evidence_scope"]) == {"GENERAL_RULE", "ZONE_SPECIFIC_RULE"}`
  - `assert set(energy["occurrence_count"]) == {1}`
  - `assert all(context for context in energy["raw_context"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.topic_evidence["topic"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_topic_evidence_distinguishes_general_and_zone_specific(valid_result) -> None:
    _, result = valid_result
    energy = result.topic_evidence.loc[result.topic_evidence["topic"].eq("energy")]
    assert set(energy["evidence_scope"]) == {"GENERAL_RULE", "ZONE_SPECIFIC_RULE"}
    assert set(energy["occurrence_count"]) == {1}
    assert all(context for context in energy["raw_context"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-evidence-scope-is-derived-from-exact-section-type"></a>
### `test_evidence_scope_is_derived_from_exact_section_type`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_evidence_scope_is_derived_from_exact_section_type`. Source lines 442–491.

**Purpose:** Builds synthetic cover/general/chapter/article energy text with no TOC/filtering, checks all four section-type-to-scope sets, then changes an OTHER evidence row to GENERAL_RULE. Public validation must reject with a scope message; no hashes are resealed.

**Exact signature**

```python
def test_evidence_scope_is_derived_from_exact_section_type() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="scope")`
- Exact assertions:
  - `assert scopes_by_type == {<br>        "GENERAL": {"GENERAL_RULE"},<br>        "ZONE_CHAPTER": {"ZONE_SPECIFIC_RULE"},<br>        "ARTICLE": {"ZONE_SPECIFIC_RULE"},<br>        "OTHER": {"OTHER_TEXT"},<br>    }`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `result.sections.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.topic_evidence["section_id"].map(section_types).eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.topic_evidence["section_id"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.topic_evidence.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `evidence["section_id"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
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
| In-memory mutation | `payload["document_layout"]["table_of_contents_pages"] = ()`<br>`payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}`<br>`evidence.loc[row_index, "evidence_scope"] = "GENERAL_RULE"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_evidence_scope_is_derived_from_exact_section_type() -> None:
    index = _index(
        (
            "energy cover text",
            "ARTICLE 1 - GENERAL\nenergy general text",
            ("ZONE U\nenergy chapter text\nARTICLE U 1 - BODY\nenergy article text"),
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
                result.topic_evidence["section_id"].map(section_types).eq(section_type),
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
        result.sections.loc[result.sections["section_type"].eq("OTHER"), "section_id"]
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-reversed-topic-mapping-keys-do-not-change-output-or-hashes"></a>
### `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`. Source lines 494–533.

**Purpose:** Reverses only topic mapping insertion order and first proves that order survives model creation. Two public builds must have frame-equal topic evidence, sorted topic names, and equal config, topic and outer hashes. Term order is not changed.

**Exact signature**

```python
def test_reversed_topic_mapping_keys_do_not_change_output_or_hashes() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(reversed_topics.topics) == tuple(reversed(tuple(forward.topics)))`
  - `assert forward_result.topic_evidence["topic"].tolist() == sorted(<br>        forward_result.topic_evidence["topic"].tolist()<br>    )`
  - `assert (<br>        forward_result.structure_config_sha256<br>        == reversed_result.structure_config_sha256<br>    )`
  - `assert (<br>        forward_result.topic_evidence_content_sha256<br>        == reversed_result.topic_evidence_content_sha256<br>    )`
  - `assert (<br>        forward_result.structure_result_content_sha256<br>        == reversed_result.structure_result_content_sha256<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `forward.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `payload["topics"].items` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `forward_result.topic_evidence["topic"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `payload["topics"] = dict(reversed(tuple(payload["topics"].items())))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-equal-length-overlap-uses-configured-term-order-as-tie-break"></a>
### `test_equal_length_overlap_uses_configured_term_order_as_tie_break`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_equal_length_overlap_uses_configured_term_order_as_tie_break`. Source lines 536–572.

**Purpose:** On alpha beta gamma, the private matcher selects alpha beta at [0,10) or beta gamma at [6,16) when equal-length term order reverses. Two synthetic public builds retain the corresponding term, and config hashes differ. This combines helper-level and in-memory builder evidence.

**Exact signature**

```python
def test_equal_length_overlap_uses_configured_term_order_as_tie_break() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert [match.search_term for match in forward_matches] == ["alpha beta"]`
  - `assert [match.search_term for match in reverse_matches] == ["beta gamma"]`
  - `assert (<br>        forward_matches[0].normalized_start,<br>        forward_matches[0].normalized_end,<br>    ) == (0, 10)`
  - `assert (<br>        reverse_matches[0].normalized_start,<br>        reverse_matches[0].normalized_end,<br>    ) == (6, 16)`
  - `assert forward_result.topic_evidence["search_term"].tolist() == ["alpha beta"]`
  - `assert reverse_result.topic_evidence["search_term"].tolist() == ["beta gamma"]`
  - `assert (<br>        forward_result.structure_config_sha256 != reverse_result.structure_config_sha256<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_planning_search_text` | `landscout.common.planning_text.normalize_planning_search_text` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `_literal_topic_matches` | `landscout.stages.structure_planning_regulation._literal_topic_matches` |
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `forward_config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `forward_result.topic_evidence["search_term"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `reverse_result.topic_evidence["search_term"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `base_payload["document_layout"]["table_of_contents_pages"] = ()`<br>`base_payload["topics"] = {"tie": forward_terms}`<br>`reverse_payload["topics"] = {"tie": reverse_terms}` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    assert (
        forward_result.structure_config_sha256 != reverse_result.structure_config_sha256
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-inputs-are-not-mutated"></a>
### `test_inputs_are_not_mutated`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_inputs_are_not_mutated`. Source lines 575–585.

**Purpose:** Deep-copies pages, zones and intersections, executes the public builder, then uses three pandas assert_frame_equal calls against the originals. Zero Python assert statements is not absence of assertions; the test does not prove arbitrary nested-object alias isolation.

**Exact signature**

```python
def test_inputs_are_not_mutated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `index.pages.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-structure-decision-mappings-are-deeply-immutable"></a>
### `test_structure_decision_mappings_are_deeply_immutable`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_structure_decision_mappings_are_deeply_immutable`. Source lines 588–597.

**Purpose:** Attempts zone_aliases[Ux]=U and topics[new]=(term,) on a validated synthetic config. Both must immediately raise TypeError matching frozen mapping and the Python dump must remain equal. This body tests two mapping assignments, not an exhaustive collection-operation matrix.

**Exact signature**

```python
def test_structure_decision_mappings_are_deeply_immutable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(TypeError, match="frozen mapping")`
- Exact assertions:
  - `assert config.model_dump(mode="python") == snapshot`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `config.zone_aliases["Ux"] = "U"`<br>`config.topics["new"] = ("term",)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_structure_decision_mappings_are_deeply_immutable() -> None:
    config = _config(_index())
    snapshot = config.model_dump(mode="python")

    with pytest.raises(TypeError, match="frozen mapping"):
        config.zone_aliases["Ux"] = "U"
    with pytest.raises(TypeError, match="frozen mapping"):
        config.topics["new"] = ("term",)

    assert config.model_dump(mode="python") == snapshot
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-body-page-extraction-error-stops-structure"></a>
### `test_body_page_extraction_error_stops_structure`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_body_page_extraction_error_stops_structure`. Source lines 600–623.

**Purpose:** Changes page 3 to a coherent ERROR with empty texts/count zero and a synthetic error string; recalculates its page, pages and complete index hashes and regenerates the matching config lock. Builder rejection must match body page.*ERROR, rather than merely stale hashes.

**Exact signature**

```python
def test_body_page_extraction_error_stops_structure() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="body page.*ERROR")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `index.pages.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pages.loc[2].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_page_content_sha256` | `landscout.stages.index_planning_regulation._page_content_sha256` |
| `replace` | `dataclasses.replace` |
| `_pages_content_sha256` | `landscout.stages.index_planning_regulation._pages_content_sha256` |
| `_index_content_sha256` | `landscout.stages.index_planning_regulation._index_content_sha256` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |

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
| In-memory mutation | `pages.loc[2, "extraction_status"] = "ERROR"`<br>`pages.loc[2, "raw_text"] = ""`<br>`pages.loc[2, "normalized_search_text"] = ""`<br>`pages.loc[2, "character_count"] = 0`<br>`pages.loc[2, "extraction_error"] = "synthetic extraction failure"`<br>`pages.loc[2, "page_content_sha256"] = _page_content_sha256(row)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_body_page_extraction_error_stops_structure() -> None:
    index = _index()
    pages = index.pages.copy(deep=True)
    pages.loc[2, "extraction_status"] = "ERROR"
    pages.loc[2, "raw_text"] = ""
    pages.loc[2, "normalized_search_text"] = ""
    pages.loc[2, "character_count"] = 0
    pages.loc[2, "extraction_error"] = "synthetic extraction failure"
    row = pages.loc[2].to_dict()
    pages.loc[2, "page_content_sha256"] = _page_content_sha256(row)
    changed = replace(
        index,
        pages=pages,
        pages_content_sha256=_pages_content_sha256(pages),
    )
    changed = replace(changed, index_content_sha256=_index_content_sha256(changed))

    with pytest.raises(PlanningRegulationStructureError, match="body page.*ERROR"):
        structure_planning_regulation(
            changed,
            _zones(changed),
            _intersections(changed),
            _config(changed),
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-blank-successfully-extracted-body-page-remains-valid"></a>
### `test_blank_successfully_extracted_body_page_remains_valid`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_blank_successfully_extracted_body_page_remains_valid`. Source lines 626–650.

**Purpose:** Changes page 2 to coherent EMPTY/null error, recalculates page/pages/index hashes, builds with a newly matching lock and asserts sections are nonempty. No actual extraction occurs.

**Exact signature**

```python
def test_blank_successfully_extracted_body_page_remains_valid() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not result.sections.empty`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `index.pages.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pages.loc[1].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_page_content_sha256` | `landscout.stages.index_planning_regulation._page_content_sha256` |
| `replace` | `dataclasses.replace` |
| `_pages_content_sha256` | `landscout.stages.index_planning_regulation._pages_content_sha256` |
| `_index_content_sha256` | `landscout.stages.index_planning_regulation._index_content_sha256` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |

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
| In-memory mutation | `pages.loc[1, "extraction_status"] = "EMPTY"`<br>`pages.loc[1, "raw_text"] = ""`<br>`pages.loc[1, "normalized_search_text"] = ""`<br>`pages.loc[1, "character_count"] = 0`<br>`pages.loc[1, "extraction_error"] = None`<br>`pages.loc[1, "page_content_sha256"] = _page_content_sha256(row)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_blank_successfully_extracted_body_page_remains_valid() -> None:
    index = _index()
    pages = index.pages.copy(deep=True)
    pages.loc[1, "extraction_status"] = "EMPTY"
    pages.loc[1, "raw_text"] = ""
    pages.loc[1, "normalized_search_text"] = ""
    pages.loc[1, "character_count"] = 0
    pages.loc[1, "extraction_error"] = None
    row = pages.loc[1].to_dict()
    pages.loc[1, "page_content_sha256"] = _page_content_sha256(row)
    changed = replace(
        index,
        pages=pages,
        pages_content_sha256=_pages_content_sha256(pages),
    )
    changed = replace(changed, index_content_sha256=_index_content_sha256(changed))

    result = structure_planning_regulation(
        changed,
        _zones(changed),
        _intersections(changed),
        _config(changed),
    )

    assert not result.sections.empty
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-coordinated-frame-mutation-is-rejected"></a>
### `test_coordinated_frame_mutation_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_coordinated_frame_mutation_is_rejected`. Source lines 661–679.

**Purpose:** Copies one frame and changes row 0: section raw_text or topic raw_context gains changed; mapping candidate_parcel_count increases by one. Validation rejects both the original envelope and a second attempt with only the selected component hash set to f×64. This is not a valid recomputation of all hashes; earlier normalization/count/context guards can reject.

**Exact signature**

```python
def test_coordinated_frame_mutation_is_rejected(
    valid_result,
    frame_name: str,
    hash_name: str,
    column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "frame_name,hash_name,column",
    [
        ("sections", "sections_content_sha256", "raw_text"),
        ("zone_mapping", "zone_map_content_sha256", "candidate_parcel_count"),
        ("topic_evidence", "topic_evidence_content_sha256", "raw_context"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `frame_name` | positional-or-keyword | `str` | `required` |
| `hash_name` | positional-or-keyword | `str` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `getattr(result, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `frame.loc[0, column] = int(frame.loc[0, column]) + 1`<br>`frame.loc[0, column] = f"{frame.loc[0, column]} changed"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-unknown-topic-page-reference-is-rejected"></a>
### `test_unknown_topic_page_reference_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_unknown_topic_page_reference_is_rejected`. Source lines 682–687.

**Purpose:** Sets the first evidence page_number to 999 in a copied frame, retains all other inputs/hashes, and requires PlanningRegulationStructureError matching unknown page.

**Exact signature**

```python
def test_unknown_topic_page_reference_is_rejected(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="unknown page")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.topic_evidence.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `evidence.loc[0, "page_number"] = 999` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_topic_page_reference_is_rejected(valid_result) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    evidence.loc[0, "page_number"] = 999
    with pytest.raises(PlanningRegulationStructureError, match="unknown page"):
        _validate(index, replace(result, topic_evidence=evidence))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-coordinated-section-row-mutation-is-caught-by-outer-envelope"></a>
### `test_coordinated_section_row_mutation_is_caught_by_outer_envelope`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_coordinated_section_row_mutation_is_caught_by_outer_envelope`. Source lines 690–703.

**Purpose:** Appends changed to the first section raw_text and recomputes normalized_text, character_count and that section row digest, but not the component/outer envelopes. _validate must reject without a message constraint. The raw-text-versus-retained-record guard precedes outer-hash checks, so the title does not prove rejection specifically by the outer envelope.

**Exact signature**

```python
def test_coordinated_section_row_mutation_is_caught_by_outer_envelope(
    valid_result,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_search_text` | `landscout.common.planning_text.normalize_planning_search_text` via the index alias |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections.loc[0].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_section_content_sha256` | `landscout.stages.structure_planning_regulation._section_content_sha256` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_section_content_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `sections.loc[0, "raw_text"] = f"{sections.loc[0, 'raw_text']} changed"`<br>`sections.loc[0, "normalized_text"] = _normalize_search_text(<br>        sections.loc[0, "raw_text"]<br>    )`<br>`sections.loc[0, "character_count"] = len(sections.loc[0, "raw_text"])`<br>`sections.loc[0, "section_content_sha256"] = _section_content_sha256(row)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-dominant-unmapped-zone-stops-processing"></a>
### `test_dominant_unmapped_zone_stops_processing`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_dominant_unmapped_zone_stops_processing`. Source lines 706–715.

**Purpose:** Changes the first positive relation consistently from U to catalog X across planning_zone_id/source_zone_id/zone_label_raw; its area remains 100.0. Builder rejection must match Dominant candidate because X has no chapter mapping.

**Exact signature**

```python
def test_dominant_unmapped_zone_stops_processing() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="Dominant candidate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_intersections(index).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |

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
| In-memory mutation | `relations.loc[0, ["planning_zone_id", "source_zone_id", "zone_label_raw"]] = [<br>        "ZONE-X",<br>        "SRC-X",<br>        "X",<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-positional-header-footer-filter-preserves-matching-body-lines"></a>
### `test_positional_header_footer_filter_preserves_matching_body_lines`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_positional_header_footer_filter_preserves_matching_body_lines`. Source lines 718–734.

**Purpose:** Calls _line_records directly on one synthetic page with leading Test PLU, interior Test PLU/100 and trailing 42. Asserts interior matches survive, footer 42 is absent, first retained text is the general heading at original line 4. It does not invoke public structure validation.

**Exact signature**

```python
def test_positional_header_footer_filter_preserves_matching_body_lines() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert "Test PLU" in retained`
  - `assert "100" in retained`
  - `assert "42" not in retained`
  - `assert retained[0] == "ARTICLE 1 - GENERAL PROVISIONS"`
  - `assert records[0].page_line_number == 4`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `_line_records` | `landscout.stages.structure_planning_regulation._line_records` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-page-without-configured-header-or-footer-is-unchanged"></a>
### `test_page_without_configured_header_or_footer_is_unchanged`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_page_without_configured_header_or_footer_is_unchanged`. Source lines 737–751.

**Purpose:** Disables both pattern tuples via model_copy and calls _line_records directly, asserting all three raw lines exactly. No public config reconstruction is exercised.

**Exact signature**

```python
def test_page_without_configured_header_or_footer_is_unchanged() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert [record.raw for record in _line_records(index, config)] == [<br>        "ARTICLE 1 - GENERAL",<br>        "100",<br>        "Body",<br>    ]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.ignored_patterns.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_line_records` | `landscout.stages.structure_planning_regulation._line_records` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-blank-only-prefix-is-preserved-in-first-actual-section"></a>
### `test_blank_only_prefix_is_preserved_in_first_actual_section`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_blank_only_prefix_is_preserved_in_first_actual_section`. Source lines 769–801.

**Purpose:** For blanks before a heading on the same page or a preceding blank page, disables TOC/filtering and builds/validates. Asserts the first actual ZONE_CHAPTER retains heading ZONE U, RECORD-000001, expected pages/prefix, complete record-count sum and no OTHER section.

**Exact signature**

```python
def test_blank_only_prefix_is_preserved_in_first_actual_section(
    raw_pages: tuple[str, ...],
    expected_pages: tuple[int, ...],
    expected_prefix: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("raw_pages", "expected_pages", "expected_prefix"),
    [
        (
            ("\n \t\nZONE U\nARTICLE U 1 - TEST\nBody",),
            (1,),
            "\n \t\nZONE U",
        ),
        (
            (" \n", "ZONE U\nARTICLE U 1 - TEST\nBody"),
            (1, 2),
            " \nZONE U",
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw_pages` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `expected_pages` | positional-or-keyword | `tuple[int, ...]` | `required` |
| `expected_prefix` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert first["section_type"] == "ZONE_CHAPTER"`
  - `assert first["heading_raw"] == "ZONE U"`
  - `assert first["start_record_id"] == "RECORD-000001"`
  - `assert tuple(first["page_numbers"]) == expected_pages`
  - `assert first["raw_text"].startswith(expected_prefix)`
  - `assert int(result.sections["source_record_count"].sum()) == len(records)`
  - `assert "OTHER" not in result.sections["section_type"].tolist()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `_line_records` | `landscout.stages.structure_planning_regulation._line_records` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `first["raw_text"].startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.sections["source_record_count"].sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.sections["section_type"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `payload["document_layout"]["table_of_contents_pages"] = ()`<br>`payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-toc-blocks-anywhere-are-other-and-toggle-topic-evidence"></a>
### `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`. Source lines 804–868.

**Purpose:** Builds seven synthetic pages with TOC blocks (1,2), (4,5), (7), with evidence disabled/enabled. Both results validate; OTHER page tuples/headings are exact, sections and mappings are frame-equal, excluded evidence is on {3,6}, included evidence on all seven pages with TOC scope OTHER_TEXT. set.isdisjoint is not a spatial operation.

**Exact signature**

```python
def test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert excluded_other["page_numbers"].tolist() == [(1, 2), (4, 5), (7,)]`
  - `assert excluded_other["heading_raw"].tolist() == [<br>        "CONTENTS",<br>        "ARTICLE 8 - energy",<br>        "ARTICLE 7 - energy",<br>    ]`
  - `assert toc_pages.isdisjoint(excluded.topic_evidence["page_number"])`
  - `assert set(excluded.topic_evidence["page_number"]) == {3, 6}`
  - `assert set(included.topic_evidence["page_number"]) == set(range(1, 8))`
  - `assert set(included_toc["evidence_scope"]) == {"OTHER_TEXT"}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `payload["document_layout"].update` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `excluded_config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `excluded.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `excluded_other["page_numbers"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `excluded_other["heading_raw"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `toc_pages.isdisjoint` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `included.topic_evidence["page_number"].isin` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None; toc_pages.isdisjoint compares Python sets of page numbers. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["document_layout"].update(<br>        {<br>            "table_of_contents_pages": (1, 2, 4, 5, 7),<br>            "include_table_of_contents_in_topic_evidence": False,<br>        }<br>    )`<br>`payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}`<br>`included_payload["document_layout"][<br>        "include_table_of_contents_in_topic_evidence"<br>    ] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    included_config = PlanningRegulationStructureConfig.model_validate(included_payload)

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-blank-gap-after-toc-is-preserved-without-a-blank-other-section"></a>
### `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`. Source lines 871–906.

**Purpose:** With TOC page 2, blank page 3 and U body page 4, builds/validates and asserts only page 2 belongs to OTHER while the chapter retains pages (3,4), heading ZONE U and the exact blank prefix.

**Exact signature**

```python
def test_blank_gap_after_toc_is_preserved_without_a_blank_other_section() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert other["page_numbers"].tolist() == [(2,)]`
  - `assert tuple(chapter["page_numbers"]) == (3, 4)`
  - `assert chapter["heading_raw"] == "ZONE U"`
  - `assert chapter["raw_text"].startswith(" \n\t\nZONE U")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `result.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `other["page_numbers"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapter["raw_text"].startswith` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `payload["document_layout"]["table_of_contents_pages"] = (2,)`<br>`payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13--structure-with-document-layout"></a>
### `_structure_with_document_layout`

Qualified owner: `tests.unit.test_structure_planning_regulation._structure_with_document_layout`. Source lines 909–943.

**Purpose:** Builds synthetic pages with keyword-only defaults toc_pages=(), body_start_page=1 and include_toc_evidence=False, disables header/footer patterns, validates the config, builds and explicitly validates the result, and asserts total record coverage. Returns (index, config, result), without a return annotation.

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

- Exact decorators: none.
- Declared return annotation: not declared (not `-> None`).

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw_pages` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `toc_pages` | keyword-only | `tuple[int, ...]` | `()` |
| `body_start_page` | keyword-only | `int` | `1` |
| `include_toc_evidence` | keyword-only | `bool` | `False` |

**Return and exception contract**

- Exact observed return expressions:
  - `index, config, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert int(result.sections["source_record_count"].sum()) == len(<br>        _line_records(index, config)<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_structure_with_document_layout`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_document_layout_accepts_real_first_and_last_indexed_pages` via `_structure_with_document_layout`
- direct call: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_structure_with_document_layout`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_existing_empty_toc_page_is_valid_not_nonexistent` via `_structure_with_document_layout`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_only_toc_blocks_remain_separate_other_sections` via `_structure_with_document_layout`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_toc_blocks_remain_separate_other_sections` via `_structure_with_document_layout`
- direct call: `tests.unit.test_structure_planning_regulation::test_blank_toc_followed_only_by_blank_tail_remains_other` via `_structure_with_document_layout`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_toc_followed_only_by_blank_tail_remains_other` via `_structure_with_document_layout`
- direct call: `tests.unit.test_structure_planning_regulation::test_ordinary_blank_gap_attaches_to_following_real_heading` via `_structure_with_document_layout`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_ordinary_blank_gap_attaches_to_following_real_heading` via `_structure_with_document_layout`
- direct call: `tests.unit.test_structure_planning_regulation::test_trailing_blank_records_attach_to_preceding_factual_section` via `_structure_with_document_layout`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_trailing_blank_records_attach_to_preceding_factual_section` via `_structure_with_document_layout`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `payload["document_layout"].update` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.sections["source_record_count"].sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_line_records` | `landscout.stages.structure_planning_regulation._line_records` |

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
| In-memory mutation | `payload["document_layout"].update(<br>        {<br>            "body_start_page": body_start_page,<br>            "table_of_contents_pages": toc_pages,<br>            "include_table_of_contents_in_topic_evidence": include_toc_evidence,<br>        }<br>    )`<br>`payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-blank-only-toc-blocks-remain-separate-other-sections"></a>
### `test_blank_only_toc_blocks_remain_separate_other_sections`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_blank_only_toc_blocks_remain_separate_other_sections`. Source lines 953–969.

**Purpose:** Uses the layout helper with one or two whitespace-only TOC pages. Requires exactly one OTHER row with the parameterized pages, blank raw text and empty heading; helper validation and record coverage also run.

**Exact signature**

```python
def test_blank_only_toc_blocks_remain_separate_other_sections(
    toc_raw_pages: tuple[str, ...],
    expected_pages: tuple[int, ...],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("toc_raw_pages", "expected_pages"),
    [
        ((" \n\t",), (2,)),
        ((" \n\t", "\t\n "), (2, 3)),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `toc_raw_pages` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `expected_pages` | positional-or-keyword | `tuple[int, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(other) == 1`
  - `assert tuple(other.iloc[0]["page_numbers"]) == expected_pages`
  - `assert not str(other.iloc[0]["raw_text"]).strip()`
  - `assert other.iloc[0]["heading_raw"] == ""`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_structure_with_document_layout` | `tests.unit.test_structure_planning_regulation._structure_with_document_layout` |
| `result.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str(other.iloc[0]["raw_text"]).strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-blank-toc-followed-only-by-blank-tail-remains-other"></a>
### `test_blank_toc_followed_only_by_blank_tail_remains_other`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_blank_toc_followed_only_by_blank_tail_remains_other`. Source lines 972–985.

**Purpose:** Uses a U body page, blank TOC page 2 and ordinary blank tail page 3; asserts one blank OTHER section covering (2,3) with empty heading. The tail is absorbed into the forced TOC section.

**Exact signature**

```python
def test_blank_toc_followed_only_by_blank_tail_remains_other() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(other) == 1`
  - `assert tuple(other.iloc[0]["page_numbers"]) == (2, 3)`
  - `assert not str(other.iloc[0]["raw_text"]).strip()`
  - `assert other.iloc[0]["heading_raw"] == ""`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_structure_with_document_layout` | `tests.unit.test_structure_planning_regulation._structure_with_document_layout` |
| `result.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str(other.iloc[0]["raw_text"]).strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-ordinary-blank-gap-attaches-to-following-real-heading"></a>
### `test_ordinary_blank_gap_attaches_to_following_real_heading`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_ordinary_blank_gap_attaches_to_following_real_heading`. Source lines 988–1001.

**Purpose:** Builds general text, an ordinary blank page and a U chapter; asserts chapter pages (2,3), blank raw prefix and heading ZONE U through the validating layout helper.

**Exact signature**

```python
def test_ordinary_blank_gap_attaches_to_following_real_heading() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(chapter["page_numbers"]) == (2, 3)`
  - `assert str(chapter["raw_text"]).startswith(" \n\t\nZONE U")`
  - `assert chapter["heading_raw"] == "ZONE U"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_structure_with_document_layout` | `tests.unit.test_structure_planning_regulation._structure_with_document_layout` |
| `result.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str(chapter["raw_text"]).startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-trailing-blank-records-attach-to-preceding-factual-section"></a>
### `test_trailing_blank_records_attach_to_preceding_factual_section`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_trailing_blank_records_attach_to_preceding_factual_section`. Source lines 1004–1014.

**Purpose:** Through the layout helper, builds a U article followed by a blank page. Asserts final type ARTICLE, pages (1,2) and the exact whitespace suffix.

**Exact signature**

```python
def test_trailing_blank_records_attach_to_preceding_factual_section() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert final_section["section_type"] == "ARTICLE"`
  - `assert tuple(final_section["page_numbers"]) == (1, 2)`
  - `assert str(final_section["raw_text"]).endswith(" \n\t")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_structure_with_document_layout` | `tests.unit.test_structure_planning_regulation._structure_with_document_layout` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str(final_section["raw_text"]).endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-heading-patterns-require-mandatory-named-captures"></a>
### `test_heading_patterns_require_mandatory_named_captures`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_heading_patterns_require_mandatory_named_captures`. Source lines 1025–1036.

**Purpose:** Replaces one structural regex family: zone lacks label, article lacks number/title, general lacks title. Reconstructing the config payload must raise ValueError matching named captures; no source matching is attempted.

**Exact signature**

```python
def test_heading_patterns_require_mandatory_named_captures(
    group: str,
    pattern: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("group", "pattern"),
    [
        ("zone_chapter", r"^ZONE\s+[A-Z]+$"),
        ("article", r"^ARTICLE\s+(?P<zone>[A-Z]+)\s+\d+\s+-\s+.*$"),
        ("general_section", r"^ARTICLE\s+(?P<number>\d+)\s+-\s+.*$"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `group` | positional-or-keyword | `str` | `required` |
| `pattern` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="named captures")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `config.heading_patterns.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `patterns.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-optional-pattern-lists-may-be-empty"></a>
### `test_optional_pattern_lists_may_be_empty`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_optional_pattern_lists_may_be_empty`. Source lines 1039–1047.

**Purpose:** Sets continuation and both ignored-pattern families to empty tuples and validates the model. It explicitly asserts continuation and page_headers are empty; page_footers is supplied but not separately asserted.

**Exact signature**

```python
def test_optional_pattern_lists_may_be_empty() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert validated.heading_patterns.continuation == ()`
  - `assert validated.ignored_patterns.page_headers == ()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |

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
| In-memory mutation | `payload["heading_patterns"]["continuation"] = ()`<br>`payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13--config-with-structural-patterns"></a>
### `_config_with_structural_patterns`

Qualified owner: `tests.unit.test_structure_planning_regulation._config_with_structural_patterns`. Source lines 1050–1068.

**Purpose:** Starts from a synthetic config dump, disables TOC and ignored patterns, applies only non-None keyword regex-family replacements, and returns model_validate(payload). None means preserve that original family, not an empty pattern list.

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

- Exact decorators: none.
- Declared return annotation: `PlanningRegulationStructureConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zone_chapter` | keyword-only | `tuple[str, ...] \| None` | `None` |
| `general_section` | keyword-only | `tuple[str, ...] \| None` | `None` |
| `article` | keyword-only | `tuple[str, ...] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `PlanningRegulationStructureConfig.model_validate(payload)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_config_with_structural_patterns`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` via `_config_with_structural_patterns`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_config_with_structural_patterns`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_zone_patterns_matching_one_line_are_ambiguous` via `_config_with_structural_patterns`
- direct call: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_config_with_structural_patterns`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_two_article_patterns_matching_one_line_are_ambiguous` via `_config_with_structural_patterns`
- direct call: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_config_with_structural_patterns`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_general_and_article_cross_category_match_is_ambiguous` via `_config_with_structural_patterns`
- direct call: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_config_with_structural_patterns`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_zone_and_general_cross_category_match_is_ambiguous` via `_config_with_structural_patterns`
- direct call: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_config_with_structural_patterns`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_ambiguous_continuation_candidate_fails_with_record_diagnostic` via `_config_with_structural_patterns`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `replacements.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |

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
| In-memory mutation | `payload["document_layout"]["table_of_contents_pages"] = ()`<br>`payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}`<br>`payload["heading_patterns"][name] = patterns` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-unique-zone-heading-and-nonheading-line-are-classified-deterministically"></a>
### `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`. Source lines 1071–1082.

**Purpose:** Calls _line_records and _heading_events directly on ordinary text then a U chapter/article. Asserts event types [ZONE_CHAPTER, ARTICLE], chapter position 1/label U and no event at position 0; this is helper evidence, not a full mapping build.

**Exact signature**

```python
def test_unique_zone_heading_and_nonheading_line_are_classified_deterministically() -> (
    None
):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert [event.section_type for event in events] == ["ZONE_CHAPTER", "ARTICLE"]`
  - `assert events[0].record_position == 1`
  - `assert events[0].zone_chapter_label == "U"`
  - `assert all(event.record_position != 0 for event in events)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config_with_structural_patterns` | `tests.unit.test_structure_planning_regulation._config_with_structural_patterns` |
| `_line_records` | `landscout.stages.structure_planning_regulation._line_records` |
| `_heading_events` | `landscout.stages.structure_planning_regulation._heading_events` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_unique_zone_heading_and_nonheading_line_are_classified_deterministically() -> (
    None
):
    index = _index(("Ordinary factual text\nZONE U\nARTICLE U 1 - BODY\nBody text",))
    config = _config_with_structural_patterns(index)
    records = _line_records(index, config)
    events = _heading_events(records, config)

    assert [event.section_type for event in events] == ["ZONE_CHAPTER", "ARTICLE"]
    assert events[0].record_position == 1
    assert events[0].zone_chapter_label == "U"
    assert all(event.record_position != 0 for event in events)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-two-zone-patterns-matching-one-line-are-ambiguous"></a>
### `test_two_zone_patterns_matching_one_line_are_ambiguous`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_two_zone_patterns_matching_one_line_are_ambiguous`. Source lines 1085–1108.

**Purpose:** Supplies two distinct zone regexes matching ZONE U and invokes the public builder. The controlled error must include Ambiguous structural heading, RECORD-000001, page/line 1 and ZONE_CHAPTER[0]/[1], but not raw ZONE U.

**Exact signature**

```python
def test_two_zone_patterns_matching_one_line_are_ambiguous() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`
- Exact assertions:
  - `assert "Ambiguous structural heading" in message`
  - `assert "RECORD-000001" in message`
  - `assert "page 1" in message`
  - `assert "line 1" in message`
  - `assert "ZONE_CHAPTER[0]" in message`
  - `assert "ZONE_CHAPTER[1]" in message`
  - `assert "ZONE U" not in message`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config_with_structural_patterns` | `tests.unit.test_structure_planning_regulation._config_with_structural_patterns` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-two-article-patterns-matching-one-line-are-ambiguous"></a>
### `test_two_article_patterns_matching_one_line_are_ambiguous`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_two_article_patterns_matching_one_line_are_ambiguous`. Source lines 1111–1129.

**Purpose:** Supplies two distinct article regexes matching ARTICLE U 1 - BODY, then requires public builder failure matching ARTICLE\[0\].*ARTICLE\[1\]. This tests same-category ambiguity after the U chapter.

**Exact signature**

```python
def test_two_article_patterns_matching_one_line_are_ambiguous() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningRegulationStructureError,<br>        match=r"ARTICLE\[0\].*ARTICLE\[1\]",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config_with_structural_patterns` | `tests.unit.test_structure_planning_regulation._config_with_structural_patterns` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-general-and-article-cross-category-match-is-ambiguous"></a>
### `test_general_and_article_cross_category_match_is_ambiguous`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_general_and_article_cross_category_match_is_ambiguous`. Source lines 1132–1147.

**Purpose:** Allows an empty zone capture in an article regex so ARTICLE 1 - GENERAL matches both categories. Public builder failure is required and the captured message must name GENERAL[0] and ARTICLE[0].

**Exact signature**

```python
def test_general_and_article_cross_category_match_is_ambiguous() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`
- Exact assertions:
  - `assert "GENERAL[0]" in message`
  - `assert "ARTICLE[0]" in message`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config_with_structural_patterns` | `tests.unit.test_structure_planning_regulation._config_with_structural_patterns` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_general_and_article_cross_category_match_is_ambiguous() -> None:
    index = _index(("ARTICLE 1 - GENERAL\nBody",))
    config = _config_with_structural_patterns(
        index,
        article=(r"^ARTICLE\s+(?P<zone>[A-Z]*)(?P<number>\d+)\s*-\s*(?P<title>.*)$",),
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-zone-and-general-cross-category-match-is-ambiguous"></a>
### `test_zone_and_general_cross_category_match_is_ambiguous`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_zone_and_general_cross_category_match_is_ambiguous`. Source lines 1150–1165.

**Purpose:** Adds a general regex matching ZONE U through number/title captures. Builder failure must name ZONE_CHAPTER[0] and GENERAL[0]; no category silently wins.

**Exact signature**

```python
def test_zone_and_general_cross_category_match_is_ambiguous() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`
- Exact assertions:
  - `assert "ZONE_CHAPTER[0]" in message`
  - `assert "GENERAL[0]" in message`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config_with_structural_patterns` | `tests.unit.test_structure_planning_regulation._config_with_structural_patterns` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_zone_and_general_cross_category_match_is_ambiguous() -> None:
    index = _index(("ZONE U\nBody",))
    config = _config_with_structural_patterns(
        index,
        general_section=(r"^ZONE\s+(?P<number>[A-Z]+)(?P<title>)$",),
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-identical-structural-regex-across-groups-is-rejected-by-config"></a>
### `test_identical_structural_regex_across_groups_is_rejected_by_config`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_identical_structural_regex_across_groups_is_rejected_by_config`. Source lines 1168–1175.

**Purpose:** Reuses the identical label-only regex in zone and general groups and requires model ValueError matching reused across groups. This guard runs before the also-missing general captures; the test isolates the reuse diagnostic, not general capture validity.

**Exact signature**

```python
def test_identical_structural_regex_across_groups_is_rejected_by_config() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="reused across groups")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `pytest.raises` | `pytest.raises` |
| `PlanningRegulationStructureConfig.model_validate` | `pydantic.BaseModel.model_validate` (inherited by PlanningRegulationStructureConfig) |

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
| In-memory mutation | `payload["heading_patterns"]["zone_chapter"] = (repeated,)`<br>`payload["heading_patterns"]["general_section"] = (repeated,)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-ambiguous-continuation-candidate-fails-with-record-diagnostic"></a>
### `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_ambiguous_continuation_candidate_fails_with_record_diagnostic`. Source lines 1178–1203.

**Purpose:** After a valid general heading, AMBIGUOUS matches second zone and general regexes during continuation lookahead. Public builder failure must name RECORD-000002, page 1, line 2, ZONE_CHAPTER[1] and GENERAL[1].

**Exact signature**

```python
def test_ambiguous_continuation_candidate_fails_with_record_diagnostic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`
- Exact assertions:
  - `assert "RECORD-000002" in message`
  - `assert "page 1" in message`
  - `assert "line 2" in message`
  - `assert "ZONE_CHAPTER[1]" in message`
  - `assert "GENERAL[1]" in message`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config_with_structural_patterns` | `tests.unit.test_structure_planning_regulation._config_with_structural_patterns` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-source-complete-validator-rejects-changed-ambiguous-grammar"></a>
### `test_source_complete_validator_rejects_changed_ambiguous_grammar`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_source_complete_validator_rejects_changed_ambiguous_grammar`. Source lines 1206–1230.

**Purpose:** Keeps the already-built result and adds an article regex overlapping the general grammar via model_copy. Public validation requires Ambiguous structural heading during expected-result reconstruction, before checking the old result config hash.

**Exact signature**

```python
def test_source_complete_validator_rejects_changed_ambiguous_grammar(
    valid_result,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningRegulationStructureError,<br>        match="Ambiguous structural heading",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `config.heading_patterns.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-normal-muret-compatible-grammar-remains-deterministic"></a>
### `test_normal_muret_compatible_grammar_remains_deterministic`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_normal_muret_compatible_grammar_remains_deterministic`. Source lines 1233–1253.

**Purpose:** Runs two builds from the same _index/_config synthetic_v1 fixtures and asserts all three frames equal plus identical outer result digest. It neither loads Muret YAML nor opens its PDF, despite the test name.

**Exact signature**

```python
def test_normal_muret_compatible_grammar_remains_deterministic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        first.structure_result_content_sha256 == second.structure_result_content_sha256<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |

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
    assert (
        first.structure_result_content_sha256 == second.structure_result_content_sha256
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-lossless-partition-mutation-is-rejected"></a>
### `test_lossless_partition_mutation_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_lossless_partition_mutation_is_rejected`. Source lines 1265–1274.

**Purpose:** Individually changes the first section ID to SECTION-9999, start record to RECORD-999999, record count to 999 or record digest to f×64. The unchanged-input validator must raise a controlled error; no rehash/message assertion isolates later checks.

**Exact signature**

```python
def test_lossless_partition_mutation_is_rejected(
    valid_result,
    mutation: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("mutation", "value"),
    [
        ("section_id", "SECTION-9999"),
        ("start_record_id", "RECORD-999999"),
        ("source_record_count", 999),
        ("source_records_sha256", "f" * 64),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `sections.loc[0, mutation] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-duplicate-or-reordered-record-partition-is-rejected"></a>
### `test_duplicate_or_reordered_record_partition_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_duplicate_or_reordered_record_partition_is_rejected`. Source lines 1277–1282.

**Purpose:** Copies the first section start_record_id into the second section, causing overlap; expects a partition error. No actual row reordering or duplicated frame row is performed.

**Exact signature**

```python
def test_duplicate_or_reordered_record_partition_is_rejected(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="partition")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `sections.loc[1, "start_record_id"] = sections.loc[0, "start_record_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_or_reordered_record_partition_is_rejected(valid_result) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[1, "start_record_id"] = sections.loc[0, "start_record_id"]
    with pytest.raises(PlanningRegulationStructureError, match="partition"):
        _validate(index, replace(result, sections=sections))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-unsorted-section-pages-are-rejected"></a>
### `test_unsorted_section_pages_are_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_unsorted_section_pages_are_rejected`. Source lines 1285–1293.

**Purpose:** Reverses the first multi-page section page_numbers tuple and requires a page references error. Raw text, record boundaries and hashes are not updated.

**Exact signature**

```python
def test_unsorted_section_pages_are_rejected(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="page references")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections["page_numbers"].map(len).gt` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections["page_numbers"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `sections.at[row_index, "page_numbers"] = tuple(<br>        reversed(sections.at[row_index, "page_numbers"])<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-article-parent-semantics-are-enforced"></a>
### `test_article_parent_semantics_are_enforced`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_article_parent_semantics_are_enforced`. Source lines 1299–1312.

**Purpose:** On the first ARTICLE, separately sets parent None, parent to the final section ID, or zone label N. Requires a controlled error without message/reseal. Each change leaves section_content_sha256 stale, so its earlier row-hash check can reject before parent-semantic checks; parent_after also names the final ARTICLE rather than a later chapter.

**Exact signature**

```python
def test_article_parent_semantics_are_enforced(valid_result, mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation", ["missing_parent", "parent_after", "zone_mismatch"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.sections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `sections.loc[article_index, "parent_section_id"] = None`<br>`sections.loc[article_index, "parent_section_id"] = sections.iloc[-1][<br>            "section_id"<br>        ]`<br>`sections.loc[article_index, "zone_chapter_label"] = "N"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_article_parent_semantics_are_enforced(valid_result, mutation: str) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    article_index = sections.index[sections["section_type"].eq("ARTICLE")][0]
    if mutation == "missing_parent":
        sections.loc[article_index, "parent_section_id"] = None
    elif mutation == "parent_after":
        sections.loc[article_index, "parent_section_id"] = sections.iloc[-1][
            "section_id"
        ]
    else:
        sections.loc[article_index, "zone_chapter_label"] = "N"
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-wrong-intersection-source-zone-id-is-rejected"></a>
### `test_wrong_intersection_source_zone_id_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_wrong_intersection_source_zone_id_is_rejected`. Source lines 1315–1322.

**Purpose:** Changes only the first relation source_zone_id to WRONG, preserving the catalog and result. Public validation must fail with source-zone during factual input validation.

**Exact signature**

```python
def test_wrong_intersection_source_zone_id_is_rejected(valid_result) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="source-zone")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |

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
| In-memory mutation | `intersections.loc[0, "source_zone_id"] = "WRONG"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-intersection-area-cannot-exceed-available-geometry-area"></a>
### `test_intersection_area_cannot_exceed_available_geometry_area`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_intersection_area_cannot_exceed_available_geometry_area`. Source lines 1326–1335.

**Purpose:** Adds either optional upper-area column with [99.0,50.0] against [100.0,50.0] intersection areas. Public builder must reject with exceeds; this compares supplied numbers, not measured geometries.

**Exact signature**

```python
def test_intersection_area_cannot_exceed_available_geometry_area(
    upper_column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("upper_column", ["parcel_metric_area_m2", "zone_area_m2"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `upper_column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="exceeds")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `pytest.raises` | `pytest.raises` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
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
| In-memory mutation | `intersections[upper_column] = [99.0, 50.0]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-intersection-upper-bound-uses-shared-relative-tolerance"></a>
### `test_intersection_upper_bound_uses_shared_relative_tolerance`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_intersection_upper_bound_uses_shared_relative_tolerance`. Source lines 1339–1373.

**Purpose:** For each optional upper column, uses reference area 10^12 and the shared tolerance (asserted >1e-6). Building/validating at reference+tolerance/2 succeeds; building at reference+2*tolerance fails with exceeds. No overlay is calculated.

**Exact signature**

```python
def test_intersection_upper_bound_uses_shared_relative_tolerance(
    upper_column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("upper_column", ["parcel_metric_area_m2", "zone_area_m2"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `upper_column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="exceeds")`
- Exact assertions:
  - `assert tolerance > 1e-6`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `technical_overlay_tolerance` | `landscout.common.planning_overlay.technical_overlay_tolerance` via the stage re-export |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `within_tolerance.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | Numerical tolerance on supplied scalar areas only; no geometry/CRS operation. |
| External process/environment | None directly present. |
| In-memory mutation | `within_tolerance[upper_column] = [reference_area, 50.0]`<br>`within_tolerance.loc[0, "intersection_area_m2"] = reference_area + tolerance / 2`<br>`above_tolerance.loc[0, "intersection_area_m2"] = reference_area + tolerance * 2` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    within_tolerance.loc[0, "intersection_area_m2"] = reference_area + tolerance / 2
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
    above_tolerance.loc[0, "intersection_area_m2"] = reference_area + tolerance * 2
    with pytest.raises(PlanningRegulationStructureError, match="exceeds"):
        structure_planning_regulation(
            index,
            _zones(index),
            above_tolerance,
            config,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-intersection-hash-columns-are-actual-and-deterministic"></a>
### `test_intersection_hash_columns_are_actual_and_deterministic`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_intersection_hash_columns_are_actual_and_deterministic`. Source lines 1385–1420.

**Purpose:** Exercises neither, either or both optional metrics, inserting them at position 0 in reversed optional order. Asserts the stored tuple equals the eight required names followed by present optional names in declared parcel-then-zone order, then validates. Does not compare hashes across differently ordered equivalent frames.

**Exact signature**

```python
def test_intersection_hash_columns_are_actual_and_deterministic(
    optional_columns: tuple[str, ...],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "optional_columns",
    [
        (),
        ("parcel_metric_area_m2",),
        ("zone_area_m2",),
        ("parcel_metric_area_m2", "zone_area_m2"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `optional_columns` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.zoning_intersection_hash_columns == required + expected_optional`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersections.insert` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
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
| In-memory mutation | `intersections.insert(0, column, [200.0, 100.0])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-optional-intersection-metric-change-invalidates-existing-result"></a>
### `test_optional_intersection_metric_change_invalidates_existing_result`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_optional_intersection_metric_change_invalidates_existing_result`. Source lines 1427–1449.

**Purpose:** Builds with parcel bounds [200,100] and zone bounds [300,150], increments one selected first-row bound by 1.0, and validates the old result against changed inputs. Requires input hash error while numeric bounds remain admissible.

**Exact signature**

```python
def test_optional_intersection_metric_change_invalidates_existing_result(
    changed_column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "changed_column",
    ["parcel_metric_area_m2", "zone_area_m2"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `changed_column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="input hash")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `intersections.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
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
| In-memory mutation | `intersections["parcel_metric_area_m2"] = [200.0, 100.0]`<br>`intersections["zone_area_m2"] = [300.0, 150.0]`<br>`changed.loc[0, changed_column] += 1.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-intersection-hash-column-lineage-mutation-is-rejected"></a>
### `test_intersection_hash_column_lineage_mutation_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_intersection_hash_column_lineage_mutation_is_rejected`. Source lines 1452–1474.

**Purpose:** Builds with parcel_metric_area_m2, then reverses only the stored zoning_intersection_hash_columns tuple. Original inputs are retained; validation must fail with hash columns.

**Exact signature**

```python
def test_intersection_hash_column_lineage_mutation_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError, match="hash columns")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `intersections["parcel_metric_area_m2"] = [200.0, 100.0]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-zone-mapping-contract-mutations-are-rejected"></a>
### `test_zone_mapping_contract_mutations_are_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_zone_mapping_contract_mutations_are_rejected`. Source lines 1488–1498.

**Purpose:** On mapping U, separately changes method to NONE, matched ID to SECTION-0002 (GENERAL), resolved label to N, polygon count to 99, intersection count to 0 or dominant count to 99. Each must raise a controlled error without reseal/message constraint. Some hit semantic/count checks; polygon count can instead reach the stale component-hash guard, so this does not isolate rebuilt count comparison.

**Exact signature**

```python
def test_zone_mapping_contract_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("mapping_method", "NONE"),
        ("matched_section_id", "SECTION-0002"),
        ("resolved_zone_chapter_label", "N"),
        ("zone_polygon_count", 99),
        ("candidate_intersection_count", 0),
        ("dominant_candidate_count", 99),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.zone_mapping.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `mapping["source_zone_label_raw"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `mapping.loc[row_index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-alias-chain-resolves-to-final-configured-target"></a>
### `test_alias_chain_resolves_to_final_configured_target`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_alias_chain_resolves_to_final_configured_target`. Source lines 1501–1512.

**Purpose:** Supplies an unchecked model_copy mapping Ua→Urban→U; the public builder reconstructs it. Asserts Ua resolves to U with CONFIG_ALIAS and X remains UNMAPPED, without fuzzy matching or a policy conclusion.

**Exact signature**

```python
def test_alias_chain_resolves_to_final_configured_target() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert mapping.at["Ua", "resolved_zone_chapter_label"] == "U"`
  - `assert mapping.at["Ua", "mapping_status"] == "CONFIG_ALIAS"`
  - `assert mapping.at["X", "mapping_status"] == "UNMAPPED"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_index` | `tests.unit.test_structure_planning_regulation._index` |
| `_config(index).model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `result.zone_mapping.set_index` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_alias_chain_resolves_to_final_configured_target() -> None:
    index = _index()
    config = _config(index).model_copy(
        update={"zone_aliases": {"Ua": "Urban", "Urban": "U"}}
    )
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), config
    )
    mapping = result.zone_mapping.set_index("source_zone_label_raw")
    assert mapping.at["Ua", "resolved_zone_chapter_label"] == "U"
    assert mapping.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert mapping.at["X", "mapping_status"] == "UNMAPPED"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-token-boundary-and-longest-match-policy"></a>
### `test_token_boundary_and_longest_match_policy`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_token_boundary_and_longest_match_policy`. Source lines 1515–1546.

**Purpose:** Calls only the shared normalizer and private literal matcher on French singular/plural, dérisque and overlapping phrase examples. Asserts each of ten configured terms is retained exactly once and total matches is ten: longer phrases suppress contained matches while standalone instances survive. No legal or BESS/ICPE equivalence is tested.

**Exact signature**

```python
def test_token_boundary_and_longest_match_policy() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert retained.count("risque") == 1`
  - `assert retained.count("risques") == 1`
  - `assert retained.count("nuisance") == 1`
  - `assert retained.count("nuisances") == 1`
  - `assert retained.count("réseau") == 1`
  - `assert retained.count("réseaux") == 1`
  - `assert retained.count("équipement d'intérêt collectif") == 1`
  - `assert retained.count("intérêt collectif") == 1`
  - `assert retained.count("incendie") == 1`
  - `assert retained.count("défense contre l'incendie") == 1`
  - `assert len(matches) == 10`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_planning_search_text` | `landscout.common.planning_text.normalize_planning_search_text` |
| `_literal_topic_matches` | `landscout.stages.structure_planning_regulation._literal_topic_matches` |
| `retained.count` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-topic-evidence-semantic-mutations-are-rejected"></a>
### `test_topic_evidence_semantic_mutations_are_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_topic_evidence_semantic_mutations_are_rejected`. Source lines 1562–1573.

**Purpose:** Mutates the first zone-specific evidence row (fallback first row) across eight separate cases: scope GENERAL_RULE, zone N, article 999, unconfigured topic/term, count 99, fabricated raw context or normalized start 999. All require controlled rejection against unchanged sources/hashes; no message or independently resealed envelope is asserted.

**Exact signature**

```python
def test_topic_evidence_semantic_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("evidence_scope", "GENERAL_RULE"),
        ("zone_chapter_label", "N"),
        ("article_number_raw", "999"),
        ("topic", "unconfigured"),
        ("search_term", "unconfigured"),
        ("occurrence_count", 99),
        ("raw_context", "fabricated"),
        ("first_match_normalized_start", 999),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.topic_evidence.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `evidence["evidence_scope"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
| In-memory mutation | `evidence.loc[row_index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-coordinated-topic-evidence-and-hash-mutation-is-rebuilt-and-rejected"></a>
### `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`. Source lines 1576–1593.

**Purpose:** Sets first raw_context to fabricated and actually recomputes all three component hashes and the outer digest with _result_with_hashes. Public validation must still reject; intrinsic context comparison to rebuilt source fragments occurs before the final expected-frame comparison, so that final comparison is not isolated.

**Exact signature**

```python
def test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected(
    valid_result,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.topic_evidence.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.structure_planning_regulation._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |

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
| In-memory mutation | `evidence.loc[0, "raw_context"] = "fabricated"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-source-complete-validator-rejects-post-build-source-change"></a>
### `test_source_complete_validator_rejects_post_build_source_change`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_source_complete_validator_rejects_post_build_source_change`. Source lines 1599–1629.

**Purpose:** Validates an old result after one of six source changes: Ua→N alias; energy→electricity term; equivalent but different zone regex; coordinated source_zone_id CHANGED in catalog/relation; area 99; or coherent TOUCH_ONLY/0 relation. Each requires a controlled error, without a message. Config/input identity guards can reject before final rebuilt-frame comparison.

**Exact signature**

```python
def test_source_complete_validator_rejects_post_build_source_change(
    valid_result,
    source_change: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "source_change", ["alias", "topic", "heading", "zone", "area", "relation"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `source_change` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zones` | `tests.unit.test_structure_planning_regulation._zones` |
| `_intersections` | `tests.unit.test_structure_planning_regulation._intersections` |
| `_config` | `tests.unit.test_structure_planning_regulation._config` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.heading_patterns.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
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
| In-memory mutation | `zones.loc[0, "source_zone_id"] = "CHANGED"`<br>`intersections.loc[0, "source_zone_id"] = "CHANGED"`<br>`intersections.loc[0, "intersection_area_m2"] = 99.0`<br>`intersections.loc[0, "relation_type"] = "TOUCH_ONLY"`<br>`intersections.loc[0, "intersection_area_m2"] = 0.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
        config = config.model_copy(
            update={"topics": {"energy": ("electricity",), "risk": ("risk",)}}
        )
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

<a id="r13-test-source-and-result-hash-mutation-is-rejected"></a>
### `test_source_and_result_hash_mutation_is_rejected`

Qualified owner: `tests.unit.test_structure_planning_regulation.test_source_and_result_hash_mutation_is_rejected`. Source lines 1641–1646.

**Purpose:** Individually replaces config, zones, intersections or outer result digest with f×64 and calls _validate. Requires PlanningRegulationStructureError, not a particular message; the actual data remain unchanged.

**Exact signature**

```python
def test_source_and_result_hash_mutation_is_rejected(
    valid_result, hash_field: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "hash_field",
    [
        "structure_config_sha256",
        "zones_content_sha256",
        "zoning_intersections_content_sha256",
        "structure_result_content_sha256",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_result` | positional-or-keyword | not annotated | `required` |
| `hash_field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningRegulationStructureError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_validate` | `tests.unit.test_structure_planning_regulation._validate` |
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
def test_source_and_result_hash_mutation_is_rejected(
    valid_result, hash_field: str
) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, **{hash_field: "f" * 64}))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **66**.
- Pytest fixtures (decorator-proven): **1**.

### Fixtures

- `valid_result` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Python assert statements (excludes assertion helper calls) | Exact regression purpose |
|---|---|---|---:|---|
| `test_package_exports_clean_high_level_api` | none | none | 4 | See [verified scenario and limits](#r13-test-package-exports-clean-high-level-api). |
| `test_source_complete_validator_can_return_validated_fragments` | none | none | 3 | See [verified scenario and limits](#r13-test-source-complete-validator-can-return-validated-fragments). |
| `test_structure_schema_versions_are_explicit` | none | none | 5 | See [verified scenario and limits](#r13-test-structure-schema-versions-are-explicit). |
| `test_old_and_unknown_config_schema_versions_are_rejected` | pytest.mark.parametrize("schema_version", [1, 3]) | pytest.raises(ValueError, match="unsupported structure config schema") | 0 | See [verified scenario and limits](#r13-test-old-and-unknown-config-schema-versions-are-rejected). |
| `test_old_and_unknown_result_config_schema_versions_are_rejected` | pytest.mark.parametrize("schema_version", [1, 3]) | pytest.raises(PlanningRegulationStructureError, match="schema version") | 0 | See [verified scenario and limits](#r13-test-old-and-unknown-result-config-schema-versions-are-rejected). |
| `test_old_and_unknown_section_hash_schema_versions_are_rejected` | pytest.mark.parametrize("schema_version", [1, 2, 4]) | pytest.raises(PlanningRegulationStructureError, match="schema version") | 0 | See [verified scenario and limits](#r13-test-old-and-unknown-section-hash-schema-versions-are-rejected). |
| `test_toc_topic_evidence_flag_rejects_boolean_coercion` | pytest.mark.parametrize("value", [0, 1, "false", "true", "yes"]) | pytest.raises(ValueError) | 0 | See [verified scenario and limits](#r13-test-toc-topic-evidence-flag-rejects-boolean-coercion). |
| `test_toc_topic_evidence_flag_accepts_exact_booleans` | pytest.mark.parametrize("value", [False, True]) | none | 1 | See [verified scenario and limits](#r13-test-toc-topic-evidence-flag-accepts-exact-booleans). |
| `test_document_layout_accepts_real_first_and_last_indexed_pages` | none | none | 2 | See [verified scenario and limits](#r13-test-document-layout-accepts-real-first-and-last-indexed-pages). |
| `test_document_layout_rejects_nonexistent_indexed_pages` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("table_of_contents_pages", (0,)),<br>        ("table_of_contents_pages", (8,)),<br>        ("body_start_page", 8),<br>    ],<br>) | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-document-layout-rejects-nonexistent-indexed-pages). |
| `test_existing_empty_toc_page_is_valid_not_nonexistent` | none | none | 1 | See [verified scenario and limits](#r13-test-existing-empty-toc-page-is-valid-not-nonexistent). |
| `test_document_lock_mismatch_is_rejected` | pytest.mark.parametrize(<br>    "lock_field",<br>    [<br>        "document_id",<br>        "pdf_sha256",<br>        "pages_content_sha256",<br>        "index_content_sha256",<br>        "normalization_profile",<br>    ],<br>) | pytest.raises(PlanningRegulationStructureError, match="document lock") | 0 | See [verified scenario and limits](#r13-test-document-lock-mismatch-is-rejected). |
| `test_invalid_regex_and_unknown_yaml_field_are_controlled` | none | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-invalid-regex-and-unknown-yaml-field-are-controlled). |
| `test_duplicate_yaml_alias_and_alias_cycle_are_rejected` | none | pytest.raises(PlanningRegulationStructureError); pytest.raises(PlanningRegulationStructureError, match="Duplicate YAML") | 0 | See [verified scenario and limits](#r13-test-duplicate-yaml-alias-and-alias-cycle-are-rejected). |
| `test_realistic_structure_is_deterministic_and_toc_heading_is_ignored` | none | none | 5 | See [verified scenario and limits](#r13-test-realistic-structure-is-deterministic-and-toc-heading-is-ignored). |
| `test_zone_article_parent_and_multi_page_text_are_preserved` | none | none | 4 | See [verified scenario and limits](#r13-test-zone-article-parent-and-multi-page-text-are-preserved). |
| `test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping` | none | none | 6 | See [verified scenario and limits](#r13-test-exact-alias-unmapped-ambiguous-and-no-fuzzy-mapping). |
| `test_topic_evidence_distinguishes_general_and_zone_specific` | none | none | 3 | See [verified scenario and limits](#r13-test-topic-evidence-distinguishes-general-and-zone-specific). |
| `test_evidence_scope_is_derived_from_exact_section_type` | none | pytest.raises(PlanningRegulationStructureError, match="scope") | 1 | See [verified scenario and limits](#r13-test-evidence-scope-is-derived-from-exact-section-type). |
| `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` | none | none | 5 | See [verified scenario and limits](#r13-test-reversed-topic-mapping-keys-do-not-change-output-or-hashes). |
| `test_equal_length_overlap_uses_configured_term_order_as_tie_break` | none | none | 7 | See [verified scenario and limits](#r13-test-equal-length-overlap-uses-configured-term-order-as-tie-break). |
| `test_inputs_are_not_mutated` | none | none | 0 | See [verified scenario and limits](#r13-test-inputs-are-not-mutated). |
| `test_structure_decision_mappings_are_deeply_immutable` | none | pytest.raises(TypeError, match="frozen mapping"); pytest.raises(TypeError, match="frozen mapping") | 1 | See [verified scenario and limits](#r13-test-structure-decision-mappings-are-deeply-immutable). |
| `test_body_page_extraction_error_stops_structure` | none | pytest.raises(PlanningRegulationStructureError, match="body page.*ERROR") | 0 | See [verified scenario and limits](#r13-test-body-page-extraction-error-stops-structure). |
| `test_blank_successfully_extracted_body_page_remains_valid` | none | none | 1 | See [verified scenario and limits](#r13-test-blank-successfully-extracted-body-page-remains-valid). |
| `test_coordinated_frame_mutation_is_rejected` | pytest.mark.parametrize(<br>    "frame_name,hash_name,column",<br>    [<br>        ("sections", "sections_content_sha256", "raw_text"),<br>        ("zone_mapping", "zone_map_content_sha256", "candidate_parcel_count"),<br>        ("topic_evidence", "topic_evidence_content_sha256", "raw_context"),<br>    ],<br>) | pytest.raises(PlanningRegulationStructureError); pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-coordinated-frame-mutation-is-rejected). |
| `test_unknown_topic_page_reference_is_rejected` | none | pytest.raises(PlanningRegulationStructureError, match="unknown page") | 0 | See [verified scenario and limits](#r13-test-unknown-topic-page-reference-is-rejected). |
| `test_coordinated_section_row_mutation_is_caught_by_outer_envelope` | none | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-coordinated-section-row-mutation-is-caught-by-outer-envelope). |
| `test_dominant_unmapped_zone_stops_processing` | none | pytest.raises(PlanningRegulationStructureError, match="Dominant candidate") | 0 | See [verified scenario and limits](#r13-test-dominant-unmapped-zone-stops-processing). |
| `test_positional_header_footer_filter_preserves_matching_body_lines` | none | none | 5 | See [verified scenario and limits](#r13-test-positional-header-footer-filter-preserves-matching-body-lines). |
| `test_page_without_configured_header_or_footer_is_unchanged` | none | none | 1 | See [verified scenario and limits](#r13-test-page-without-configured-header-or-footer-is-unchanged). |
| `test_blank_only_prefix_is_preserved_in_first_actual_section` | pytest.mark.parametrize(<br>    ("raw_pages", "expected_pages", "expected_prefix"),<br>    [<br>        (<br>            ("\n \t\nZONE U\nARTICLE U 1 - TEST\nBody",),<br>            (1,),<br>            "\n \t\nZONE U",<br>        ),<br>        (<br>            (" \n", "ZONE U\nARTICLE U 1 - TEST\nBody"),<br>            (1, 2),<br>            " \nZONE U",<br>        ),<br>    ],<br>) | none | 7 | See [verified scenario and limits](#r13-test-blank-only-prefix-is-preserved-in-first-actual-section). |
| `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` | none | none | 6 | See [verified scenario and limits](#r13-test-toc-blocks-anywhere-are-other-and-toggle-topic-evidence). |
| `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` | none | none | 4 | See [verified scenario and limits](#r13-test-blank-gap-after-toc-is-preserved-without-a-blank-other-section). |
| `test_blank_only_toc_blocks_remain_separate_other_sections` | pytest.mark.parametrize(<br>    ("toc_raw_pages", "expected_pages"),<br>    [<br>        ((" \n\t",), (2,)),<br>        ((" \n\t", "\t\n "), (2, 3)),<br>    ],<br>) | none | 4 | See [verified scenario and limits](#r13-test-blank-only-toc-blocks-remain-separate-other-sections). |
| `test_blank_toc_followed_only_by_blank_tail_remains_other` | none | none | 4 | See [verified scenario and limits](#r13-test-blank-toc-followed-only-by-blank-tail-remains-other). |
| `test_ordinary_blank_gap_attaches_to_following_real_heading` | none | none | 3 | See [verified scenario and limits](#r13-test-ordinary-blank-gap-attaches-to-following-real-heading). |
| `test_trailing_blank_records_attach_to_preceding_factual_section` | none | none | 3 | See [verified scenario and limits](#r13-test-trailing-blank-records-attach-to-preceding-factual-section). |
| `test_heading_patterns_require_mandatory_named_captures` | pytest.mark.parametrize(<br>    ("group", "pattern"),<br>    [<br>        ("zone_chapter", r"^ZONE\s+[A-Z]+$"),<br>        ("article", r"^ARTICLE\s+(?P<zone>[A-Z]+)\s+\d+\s+-\s+.*$"),<br>        ("general_section", r"^ARTICLE\s+(?P<number>\d+)\s+-\s+.*$"),<br>    ],<br>) | pytest.raises(ValueError, match="named captures") | 0 | See [verified scenario and limits](#r13-test-heading-patterns-require-mandatory-named-captures). |
| `test_optional_pattern_lists_may_be_empty` | none | none | 2 | See [verified scenario and limits](#r13-test-optional-pattern-lists-may-be-empty). |
| `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically` | none | none | 4 | See [verified scenario and limits](#r13-test-unique-zone-heading-and-nonheading-line-are-classified-deterministically). |
| `test_two_zone_patterns_matching_one_line_are_ambiguous` | none | pytest.raises(PlanningRegulationStructureError) | 7 | See [verified scenario and limits](#r13-test-two-zone-patterns-matching-one-line-are-ambiguous). |
| `test_two_article_patterns_matching_one_line_are_ambiguous` | none | pytest.raises(<br>        PlanningRegulationStructureError,<br>        match=r"ARTICLE\[0\].*ARTICLE\[1\]",<br>    ) | 0 | See [verified scenario and limits](#r13-test-two-article-patterns-matching-one-line-are-ambiguous). |
| `test_general_and_article_cross_category_match_is_ambiguous` | none | pytest.raises(PlanningRegulationStructureError) | 2 | See [verified scenario and limits](#r13-test-general-and-article-cross-category-match-is-ambiguous). |
| `test_zone_and_general_cross_category_match_is_ambiguous` | none | pytest.raises(PlanningRegulationStructureError) | 2 | See [verified scenario and limits](#r13-test-zone-and-general-cross-category-match-is-ambiguous). |
| `test_identical_structural_regex_across_groups_is_rejected_by_config` | none | pytest.raises(ValueError, match="reused across groups") | 0 | See [verified scenario and limits](#r13-test-identical-structural-regex-across-groups-is-rejected-by-config). |
| `test_ambiguous_continuation_candidate_fails_with_record_diagnostic` | none | pytest.raises(PlanningRegulationStructureError) | 5 | See [verified scenario and limits](#r13-test-ambiguous-continuation-candidate-fails-with-record-diagnostic). |
| `test_source_complete_validator_rejects_changed_ambiguous_grammar` | none | pytest.raises(<br>        PlanningRegulationStructureError,<br>        match="Ambiguous structural heading",<br>    ) | 0 | See [verified scenario and limits](#r13-test-source-complete-validator-rejects-changed-ambiguous-grammar). |
| `test_normal_muret_compatible_grammar_remains_deterministic` | none | none | 1 | See [verified scenario and limits](#r13-test-normal-muret-compatible-grammar-remains-deterministic). |
| `test_lossless_partition_mutation_is_rejected` | pytest.mark.parametrize(<br>    ("mutation", "value"),<br>    [<br>        ("section_id", "SECTION-9999"),<br>        ("start_record_id", "RECORD-999999"),<br>        ("source_record_count", 999),<br>        ("source_records_sha256", "f" * 64),<br>    ],<br>) | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-lossless-partition-mutation-is-rejected). |
| `test_duplicate_or_reordered_record_partition_is_rejected` | none | pytest.raises(PlanningRegulationStructureError, match="partition") | 0 | See [verified scenario and limits](#r13-test-duplicate-or-reordered-record-partition-is-rejected). |
| `test_unsorted_section_pages_are_rejected` | none | pytest.raises(PlanningRegulationStructureError, match="page references") | 0 | See [verified scenario and limits](#r13-test-unsorted-section-pages-are-rejected). |
| `test_article_parent_semantics_are_enforced` | pytest.mark.parametrize(<br>    "mutation", ["missing_parent", "parent_after", "zone_mismatch"]<br>) | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-article-parent-semantics-are-enforced). |
| `test_wrong_intersection_source_zone_id_is_rejected` | none | pytest.raises(PlanningRegulationStructureError, match="source-zone") | 0 | See [verified scenario and limits](#r13-test-wrong-intersection-source-zone-id-is-rejected). |
| `test_intersection_area_cannot_exceed_available_geometry_area` | pytest.mark.parametrize("upper_column", ["parcel_metric_area_m2", "zone_area_m2"]) | pytest.raises(PlanningRegulationStructureError, match="exceeds") | 0 | See [verified scenario and limits](#r13-test-intersection-area-cannot-exceed-available-geometry-area). |
| `test_intersection_upper_bound_uses_shared_relative_tolerance` | pytest.mark.parametrize("upper_column", ["parcel_metric_area_m2", "zone_area_m2"]) | pytest.raises(PlanningRegulationStructureError, match="exceeds") | 1 | See [verified scenario and limits](#r13-test-intersection-upper-bound-uses-shared-relative-tolerance). |
| `test_intersection_hash_columns_are_actual_and_deterministic` | pytest.mark.parametrize(<br>    "optional_columns",<br>    [<br>        (),<br>        ("parcel_metric_area_m2",),<br>        ("zone_area_m2",),<br>        ("parcel_metric_area_m2", "zone_area_m2"),<br>    ],<br>) | none | 1 | See [verified scenario and limits](#r13-test-intersection-hash-columns-are-actual-and-deterministic). |
| `test_optional_intersection_metric_change_invalidates_existing_result` | pytest.mark.parametrize(<br>    "changed_column",<br>    ["parcel_metric_area_m2", "zone_area_m2"],<br>) | pytest.raises(PlanningRegulationStructureError, match="input hash") | 0 | See [verified scenario and limits](#r13-test-optional-intersection-metric-change-invalidates-existing-result). |
| `test_intersection_hash_column_lineage_mutation_is_rejected` | none | pytest.raises(PlanningRegulationStructureError, match="hash columns") | 0 | See [verified scenario and limits](#r13-test-intersection-hash-column-lineage-mutation-is-rejected). |
| `test_zone_mapping_contract_mutations_are_rejected` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("mapping_method", "NONE"),<br>        ("matched_section_id", "SECTION-0002"),<br>        ("resolved_zone_chapter_label", "N"),<br>        ("zone_polygon_count", 99),<br>        ("candidate_intersection_count", 0),<br>        ("dominant_candidate_count", 99),<br>    ],<br>) | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-zone-mapping-contract-mutations-are-rejected). |
| `test_alias_chain_resolves_to_final_configured_target` | none | none | 3 | See [verified scenario and limits](#r13-test-alias-chain-resolves-to-final-configured-target). |
| `test_token_boundary_and_longest_match_policy` | none | none | 11 | See [verified scenario and limits](#r13-test-token-boundary-and-longest-match-policy). |
| `test_topic_evidence_semantic_mutations_are_rejected` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("evidence_scope", "GENERAL_RULE"),<br>        ("zone_chapter_label", "N"),<br>        ("article_number_raw", "999"),<br>        ("topic", "unconfigured"),<br>        ("search_term", "unconfigured"),<br>        ("occurrence_count", 99),<br>        ("raw_context", "fabricated"),<br>        ("first_match_normalized_start", 999),<br>    ],<br>) | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-topic-evidence-semantic-mutations-are-rejected). |
| `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` | none | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-coordinated-topic-evidence-and-hash-mutation-is-rebuilt-and-rejected). |
| `test_source_complete_validator_rejects_post_build_source_change` | pytest.mark.parametrize(<br>    "source_change", ["alias", "topic", "heading", "zone", "area", "relation"]<br>) | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-source-complete-validator-rejects-post-build-source-change). |
| `test_source_and_result_hash_mutation_is_rejected` | pytest.mark.parametrize(<br>    "hash_field",<br>    [<br>        "structure_config_sha256",<br>        "zones_content_sha256",<br>        "zoning_intersections_content_sha256",<br>        "structure_result_content_sha256",<br>    ],<br>) | pytest.raises(PlanningRegulationStructureError) | 0 | See [verified scenario and limits](#r13-test-source-and-result-hash-mutation-is-rejected). |

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

from dataclasses import replace
from pathlib import Path

import pandas as pd
import pytest

from landscout import stages
from landscout.common.planning_text import normalize_planning_search_text
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
from landscout.stages.planning_overlay import technical_overlay_tolerance
from landscout.stages.structure_planning_regulation import (
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
)


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


@pytest.fixture
def valid_result():
    index = _index()
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), _config(index)
    )
    return index, result


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


def test_package_exports_clean_high_level_api() -> None:
    assert "structure_planning_regulation" in stages.__all__
    assert "validate_planning_regulation_structure" in stages.__all__
    assert "validate_planning_regulation_structure_with_fragments" in stages.__all__
    assert not any(name.startswith("_build_") for name in stages.__all__)


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


def test_structure_schema_versions_are_explicit(valid_result) -> None:
    index, result = valid_result
    config = _config(index)
    assert config.schema_version == 2
    assert result.structure_config_schema_version == 2
    assert SECTION_HASH_SCHEMA_VERSION == 3
    assert result.section_hash_schema_version == 3
    assert STRUCTURE_MANIFEST_SCHEMA_VERSION == 4


@pytest.mark.parametrize("schema_version", [1, 3])
def test_old_and_unknown_config_schema_versions_are_rejected(
    schema_version: int,
) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["schema_version"] = schema_version
    with pytest.raises(ValueError, match="unsupported structure config schema"):
        PlanningRegulationStructureConfig.model_validate(payload)


@pytest.mark.parametrize("schema_version", [1, 3])
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


@pytest.mark.parametrize("schema_version", [1, 2, 4])
def test_old_and_unknown_section_hash_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError, match="schema version"):
        _validate(index, replace(result, section_hash_schema_version=schema_version))


@pytest.mark.parametrize("value", [0, 1, "false", "true", "yes"])
def test_toc_topic_evidence_flag_rejects_boolean_coercion(value: object) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["include_table_of_contents_in_topic_evidence"] = value
    with pytest.raises(ValueError):
        PlanningRegulationStructureConfig.model_validate(payload)


@pytest.mark.parametrize("value", [False, True])
def test_toc_topic_evidence_flag_accepts_exact_booleans(value: bool) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    payload["document_layout"]["include_table_of_contents_in_topic_evidence"] = value
    validated = PlanningRegulationStructureConfig.model_validate(payload)
    assert (
        validated.document_layout.include_table_of_contents_in_topic_evidence is value
    )


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


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("table_of_contents_pages", (0,)),
        ("table_of_contents_pages", (8,)),
        ("body_start_page", 8),
    ],
)
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


@pytest.mark.parametrize(
    "lock_field",
    [
        "document_id",
        "pdf_sha256",
        "pages_content_sha256",
        "index_content_sha256",
        "normalization_profile",
    ],
)
def test_document_lock_mismatch_is_rejected(lock_field: str) -> None:
    index = _index()
    config = _config(index)
    lock = config.document_lock.model_copy(
        update={lock_field: "f" * 64 if "sha256" in lock_field else "wrong"}
    )
    changed = config.model_copy(update={"document_lock": lock})
    with pytest.raises(PlanningRegulationStructureError, match="document lock"):
        structure_planning_regulation(
            index, _zones(index), _intersections(index), changed
        )


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


def test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping(valid_result) -> None:
    _, result = valid_result
    mappings = result.zone_mapping.set_index("source_zone_label_raw")
    assert mappings.at["U", "mapping_status"] == "EXACT"
    assert mappings.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert mappings.at["X", "mapping_status"] == "UNMAPPED"
    assert mappings.at["UX", "mapping_status"] == "UNMAPPED"
    assert mappings.at["Z", "mapping_status"] == "AMBIGUOUS"
    assert mappings.at["X", "dominant_candidate_count"] == 0


def test_topic_evidence_distinguishes_general_and_zone_specific(valid_result) -> None:
    _, result = valid_result
    energy = result.topic_evidence.loc[result.topic_evidence["topic"].eq("energy")]
    assert set(energy["evidence_scope"]) == {"GENERAL_RULE", "ZONE_SPECIFIC_RULE"}
    assert set(energy["occurrence_count"]) == {1}
    assert all(context for context in energy["raw_context"])


def test_evidence_scope_is_derived_from_exact_section_type() -> None:
    index = _index(
        (
            "energy cover text",
            "ARTICLE 1 - GENERAL\nenergy general text",
            ("ZONE U\nenergy chapter text\nARTICLE U 1 - BODY\nenergy article text"),
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
                result.topic_evidence["section_id"].map(section_types).eq(section_type),
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
        result.sections.loc[result.sections["section_type"].eq("OTHER"), "section_id"]
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
    assert (
        forward_result.structure_config_sha256 != reverse_result.structure_config_sha256
    )


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


def test_structure_decision_mappings_are_deeply_immutable() -> None:
    config = _config(_index())
    snapshot = config.model_dump(mode="python")

    with pytest.raises(TypeError, match="frozen mapping"):
        config.zone_aliases["Ux"] = "U"
    with pytest.raises(TypeError, match="frozen mapping"):
        config.topics["new"] = ("term",)

    assert config.model_dump(mode="python") == snapshot


def test_body_page_extraction_error_stops_structure() -> None:
    index = _index()
    pages = index.pages.copy(deep=True)
    pages.loc[2, "extraction_status"] = "ERROR"
    pages.loc[2, "raw_text"] = ""
    pages.loc[2, "normalized_search_text"] = ""
    pages.loc[2, "character_count"] = 0
    pages.loc[2, "extraction_error"] = "synthetic extraction failure"
    row = pages.loc[2].to_dict()
    pages.loc[2, "page_content_sha256"] = _page_content_sha256(row)
    changed = replace(
        index,
        pages=pages,
        pages_content_sha256=_pages_content_sha256(pages),
    )
    changed = replace(changed, index_content_sha256=_index_content_sha256(changed))

    with pytest.raises(PlanningRegulationStructureError, match="body page.*ERROR"):
        structure_planning_regulation(
            changed,
            _zones(changed),
            _intersections(changed),
            _config(changed),
        )


def test_blank_successfully_extracted_body_page_remains_valid() -> None:
    index = _index()
    pages = index.pages.copy(deep=True)
    pages.loc[1, "extraction_status"] = "EMPTY"
    pages.loc[1, "raw_text"] = ""
    pages.loc[1, "normalized_search_text"] = ""
    pages.loc[1, "character_count"] = 0
    pages.loc[1, "extraction_error"] = None
    row = pages.loc[1].to_dict()
    pages.loc[1, "page_content_sha256"] = _page_content_sha256(row)
    changed = replace(
        index,
        pages=pages,
        pages_content_sha256=_pages_content_sha256(pages),
    )
    changed = replace(changed, index_content_sha256=_index_content_sha256(changed))

    result = structure_planning_regulation(
        changed,
        _zones(changed),
        _intersections(changed),
        _config(changed),
    )

    assert not result.sections.empty


@pytest.mark.parametrize(
    "frame_name,hash_name,column",
    [
        ("sections", "sections_content_sha256", "raw_text"),
        ("zone_mapping", "zone_map_content_sha256", "candidate_parcel_count"),
        ("topic_evidence", "topic_evidence_content_sha256", "raw_context"),
    ],
)
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


def test_unknown_topic_page_reference_is_rejected(valid_result) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    evidence.loc[0, "page_number"] = 999
    with pytest.raises(PlanningRegulationStructureError, match="unknown page"):
        _validate(index, replace(result, topic_evidence=evidence))


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


@pytest.mark.parametrize(
    ("raw_pages", "expected_pages", "expected_prefix"),
    [
        (
            ("\n \t\nZONE U\nARTICLE U 1 - TEST\nBody",),
            (1,),
            "\n \t\nZONE U",
        ),
        (
            (" \n", "ZONE U\nARTICLE U 1 - TEST\nBody"),
            (1, 2),
            " \nZONE U",
        ),
    ],
)
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
    included_config = PlanningRegulationStructureConfig.model_validate(included_payload)

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


@pytest.mark.parametrize(
    ("toc_raw_pages", "expected_pages"),
    [
        ((" \n\t",), (2,)),
        ((" \n\t", "\t\n "), (2, 3)),
    ],
)
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


@pytest.mark.parametrize(
    ("group", "pattern"),
    [
        ("zone_chapter", r"^ZONE\s+[A-Z]+$"),
        ("article", r"^ARTICLE\s+(?P<zone>[A-Z]+)\s+\d+\s+-\s+.*$"),
        ("general_section", r"^ARTICLE\s+(?P<number>\d+)\s+-\s+.*$"),
    ],
)
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


def test_optional_pattern_lists_may_be_empty() -> None:
    index = _index()
    config = _config(index)
    payload = config.model_dump(mode="python")
    payload["heading_patterns"]["continuation"] = ()
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    validated = PlanningRegulationStructureConfig.model_validate(payload)
    assert validated.heading_patterns.continuation == ()
    assert validated.ignored_patterns.page_headers == ()


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


def test_unique_zone_heading_and_nonheading_line_are_classified_deterministically() -> (
    None
):
    index = _index(("Ordinary factual text\nZONE U\nARTICLE U 1 - BODY\nBody text",))
    config = _config_with_structural_patterns(index)
    records = _line_records(index, config)
    events = _heading_events(records, config)

    assert [event.section_type for event in events] == ["ZONE_CHAPTER", "ARTICLE"]
    assert events[0].record_position == 1
    assert events[0].zone_chapter_label == "U"
    assert all(event.record_position != 0 for event in events)


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


def test_general_and_article_cross_category_match_is_ambiguous() -> None:
    index = _index(("ARTICLE 1 - GENERAL\nBody",))
    config = _config_with_structural_patterns(
        index,
        article=(r"^ARTICLE\s+(?P<zone>[A-Z]*)(?P<number>\d+)\s*-\s*(?P<title>.*)$",),
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


def test_zone_and_general_cross_category_match_is_ambiguous() -> None:
    index = _index(("ZONE U\nBody",))
    config = _config_with_structural_patterns(
        index,
        general_section=(r"^ZONE\s+(?P<number>[A-Z]+)(?P<title>)$",),
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


def test_identical_structural_regex_across_groups_is_rejected_by_config() -> None:
    index = _index()
    payload = _config(index).model_dump(mode="python")
    repeated = r"^(?P<label>ZONE)$"
    payload["heading_patterns"]["zone_chapter"] = (repeated,)
    payload["heading_patterns"]["general_section"] = (repeated,)
    with pytest.raises(ValueError, match="reused across groups"):
        PlanningRegulationStructureConfig.model_validate(payload)


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
    assert (
        first.structure_result_content_sha256 == second.structure_result_content_sha256
    )


@pytest.mark.parametrize(
    ("mutation", "value"),
    [
        ("section_id", "SECTION-9999"),
        ("start_record_id", "RECORD-999999"),
        ("source_record_count", 999),
        ("source_records_sha256", "f" * 64),
    ],
)
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


def test_duplicate_or_reordered_record_partition_is_rejected(valid_result) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[1, "start_record_id"] = sections.loc[0, "start_record_id"]
    with pytest.raises(PlanningRegulationStructureError, match="partition"):
        _validate(index, replace(result, sections=sections))


def test_unsorted_section_pages_are_rejected(valid_result) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    row_index = sections.index[sections["page_numbers"].map(len).gt(1)][0]
    sections.at[row_index, "page_numbers"] = tuple(
        reversed(sections.at[row_index, "page_numbers"])
    )
    with pytest.raises(PlanningRegulationStructureError, match="page references"):
        _validate(index, replace(result, sections=sections))


@pytest.mark.parametrize(
    "mutation", ["missing_parent", "parent_after", "zone_mismatch"]
)
def test_article_parent_semantics_are_enforced(valid_result, mutation: str) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    article_index = sections.index[sections["section_type"].eq("ARTICLE")][0]
    if mutation == "missing_parent":
        sections.loc[article_index, "parent_section_id"] = None
    elif mutation == "parent_after":
        sections.loc[article_index, "parent_section_id"] = sections.iloc[-1][
            "section_id"
        ]
    else:
        sections.loc[article_index, "zone_chapter_label"] = "N"
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))


def test_wrong_intersection_source_zone_id_is_rejected(valid_result) -> None:
    index, result = valid_result
    intersections = _intersections(index)
    intersections.loc[0, "source_zone_id"] = "WRONG"
    with pytest.raises(PlanningRegulationStructureError, match="source-zone"):
        validate_planning_regulation_structure(
            index, _zones(index), intersections, _config(index), result
        )


@pytest.mark.parametrize("upper_column", ["parcel_metric_area_m2", "zone_area_m2"])
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


@pytest.mark.parametrize("upper_column", ["parcel_metric_area_m2", "zone_area_m2"])
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
    within_tolerance.loc[0, "intersection_area_m2"] = reference_area + tolerance / 2
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
    above_tolerance.loc[0, "intersection_area_m2"] = reference_area + tolerance * 2
    with pytest.raises(PlanningRegulationStructureError, match="exceeds"):
        structure_planning_regulation(
            index,
            _zones(index),
            above_tolerance,
            config,
        )


@pytest.mark.parametrize(
    "optional_columns",
    [
        (),
        ("parcel_metric_area_m2",),
        ("zone_area_m2",),
        ("parcel_metric_area_m2", "zone_area_m2"),
    ],
)
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


@pytest.mark.parametrize(
    "changed_column",
    ["parcel_metric_area_m2", "zone_area_m2"],
)
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


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("mapping_method", "NONE"),
        ("matched_section_id", "SECTION-0002"),
        ("resolved_zone_chapter_label", "N"),
        ("zone_polygon_count", 99),
        ("candidate_intersection_count", 0),
        ("dominant_candidate_count", 99),
    ],
)
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


def test_alias_chain_resolves_to_final_configured_target() -> None:
    index = _index()
    config = _config(index).model_copy(
        update={"zone_aliases": {"Ua": "Urban", "Urban": "U"}}
    )
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), config
    )
    mapping = result.zone_mapping.set_index("source_zone_label_raw")
    assert mapping.at["Ua", "resolved_zone_chapter_label"] == "U"
    assert mapping.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert mapping.at["X", "mapping_status"] == "UNMAPPED"


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


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("evidence_scope", "GENERAL_RULE"),
        ("zone_chapter_label", "N"),
        ("article_number_raw", "999"),
        ("topic", "unconfigured"),
        ("search_term", "unconfigured"),
        ("occurrence_count", 99),
        ("raw_context", "fabricated"),
        ("first_match_normalized_start", 999),
    ],
)
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


@pytest.mark.parametrize(
    "source_change", ["alias", "topic", "heading", "zone", "area", "relation"]
)
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
        config = config.model_copy(
            update={"topics": {"energy": ("electricity",), "risk": ("risk",)}}
        )
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


@pytest.mark.parametrize(
    "hash_field",
    [
        "structure_config_sha256",
        "zones_content_sha256",
        "zoning_intersections_content_sha256",
        "structure_result_content_sha256",
    ],
)
def test_source_and_result_hash_mutation_is_rejected(
    valid_result, hash_field: str
) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, **{hash_field: "f" * 64}))
```
