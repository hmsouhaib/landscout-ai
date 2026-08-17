# `tests/unit/test_structure_planning_regulation.py`

## File identity

- Repository path: `tests/unit/test_structure_planning_regulation.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `structure_planning_regulation` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `982f563beb37fe123241b878646904d140d33644dc42640d07b8076f54d623b4`

## 1. Purpose

Provides complete unit and regression coverage for the `structure_planning_regulation` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from dataclasses import replace` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_text import normalize_planning_search_text` — required by the implementation paths and symbols documented below.
- `from landscout.stages.index_planning_regulation import ( INDEX_HASH_SCHEMA_VERSION, PAGE_HASH_SCHEMA_VERSION, SEARCH_NORMALIZATION_PROFILE, PlanningRegulationIndex, _index_content_sha256, _normalize_search_text, _page_content_sha256, _pages_content_sha256, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.
- `from landscout.stages.structure_planning_regulation import ( SECTION_HASH_SCHEMA_VERSION, STRUCTURE_MANIFEST_SCHEMA_VERSION, PlanningRegulationStructureConfig, PlanningRegulationStructureError, _heading_events, _line_records, _literal_topic_matches, _result_with_hashes, _section_content_sha256, loa…` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_index`

**Signature**

```python
def _index(raw_pages: tuple[str, ...] | None = None) -> PlanningRegulationIndex:
```

**Purpose**

Implements index according to the exact implementation and guards in this file.

**Inputs**

- `raw_pages` (`tuple[str, ...] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationIndex`. Observed return expression(s): `replace(index, index_content_sha256=_index_content_sha256(index))`.

**Algorithm**

1. Checks `raw_pages is None`. When true: Computes `raw_pages` from `('Test PLU\n1\nZONE U\nARTICLE U 1 - TOC ENTRY', 'Test PLU\n2\nARTICLE 1 - GENERAL PROVISIONS\nGeneral energy rule.', 'Test PLU\n3\nZONE U\nCharacter of U.\nARTICLE U 1 - USES\nFirst page energy text.', 'Test PLU\n4\nSecond page of the same article.\nARTICLE U 2 - NETWORKS\nNetwork text.', 'Test PLU\n5\nZONE N\nARTICL…`.
2. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
3. Iterates `(number, raw_text)` over `enumerate(raw_pages, start=1)`. For each value: Computes `normalized_text` from `_normalize_search_text(raw_text)`. Defines `row` with annotation `dict[str, object]` from `{'page_number': number, 'extraction_status': 'TEXT' if normalized_text else 'EMPTY', 'raw_text': raw_text, 'normalized_search_text': normalized_text, 'character_count': len(raw_text), 'extraction_error': None, 'page_content_sha256': ''}`. Computes `row['page_content_sha256']` from `_page_content_sha256(row)`. Executes 1 additional source-ordered statement(s).
4. Computes `pages` from `pd.DataFrame(rows)`.
5. Computes `index` from `PlanningRegulationIndex(document_id='doc-1', archive_sha256='a' * 64, regulation_filename='commune_reglement.pdf', source_selection_method='ZONING_NOMFIC', source_selection_sha256='b' * 64, pdf_relative_path='package/commune_reglement.pdf', pdf_size_bytes=100, pdf_sha256='c' * 64, extraction_library='pypdf', extractio…`.
6. Returns `replace(index, index_content_sha256=_index_content_sha256(index))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningRegulationIndex`, `_index_content_sha256`, `_normalize_search_text`, `_page_content_sha256`, `_pages_content_sha256`, `enumerate`, `len`, `pd.DataFrame`, `replace`, `rows.append`.

**Known repository callers**

- `tests/unit/test_structure_planning_regulation.py` — `_structure_with_document_layout`
- `tests/unit/test_structure_planning_regulation.py` — `test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py` — `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py` — `test_duplicate_yaml_alias_and_alias_cycle_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py` — `test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py` — `test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_heading_patterns_require_mandatory_named_captures`
- `tests/unit/test_structure_planning_regulation.py` — `test_identical_structural_regex_across_groups_is_rejected_by_config`
- `tests/unit/test_structure_planning_regulation.py` — `test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py` — `test_invalid_regex_and_unknown_yaml_field_are_controlled`
- `tests/unit/test_structure_planning_regulation.py` — `test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_old_and_unknown_config_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_pattern_lists_may_be_empty`
- `tests/unit/test_structure_planning_regulation.py` — `test_page_without_configured_header_or_footer_is_unchanged`
- `tests/unit/test_structure_planning_regulation.py` — `test_positional_header_footer_filter_preserves_matching_body_lines`
- `tests/unit/test_structure_planning_regulation.py` — `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_topic_evidence_flag_accepts_exact_booleans`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_topic_evidence_flag_rejects_boolean_coercion`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`
- `tests/unit/test_structure_planning_regulation.py` — `test_zone_and_general_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `valid_result`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_heading_patterns_require_mandatory_named_captures`
- `tests/unit/test_structure_planning_regulation.py::test_identical_structural_regex_across_groups_is_rejected_by_config`
- `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py::test_invalid_regex_and_unknown_yaml_field_are_controlled`
- `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_config_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py::test_optional_pattern_lists_may_be_empty`
- `tests/unit/test_structure_planning_regulation.py::test_page_without_configured_header_or_footer_is_unchanged`
- `tests/unit/test_structure_planning_regulation.py::test_positional_header_footer_filter_preserves_matching_body_lines`
- `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_accepts_exact_booleans`
- `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_rejects_boolean_coercion`
- `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`
- `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config`

**Signature**

```python
def _config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
```

**Purpose**

Implements config according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationStructureConfig`. Observed return expression(s): `PlanningRegulationStructureConfig.model_validate({'schema_version': 2, 'structure_profile': 'synthetic_v1', 'document_lock': {'document_id': index.document_id, 'pdf_sha256': index.pdf_sha256, 'pages_content_sha256': index.pages_content_sha256, 'index_content_sha256': index.index_content_sha256, 'normalization_profile': index.search_normalization_profile}, 'document_layout': {'body_start_page': 1,…`.

**Algorithm**

1. Returns `PlanningRegulationStructureConfig.model_validate({'schema_version': 2, 'structure_profile': 'synthetic_v1', 'document_lock': {'document_id': index.document_id, 'pdf_sha256': index.pdf_sha256, 'pages_content_sha256': index.pages_content_sha256, 'index_content_sha256': index.index_content_sha256, 'normalization_profile': index.search_normalization_profile}, '…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`.

**Known repository callers**

- `tests/unit/test_structure_planning_regulation.py` — `_config_with_structural_patterns`
- `tests/unit/test_structure_planning_regulation.py` — `_structure_with_document_layout`
- `tests/unit/test_structure_planning_regulation.py` — `_validate`
- `tests/unit/test_structure_planning_regulation.py` — `test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py` — `test_duplicate_yaml_alias_and_alias_cycle_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py` — `test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py` — `test_heading_patterns_require_mandatory_named_captures`
- `tests/unit/test_structure_planning_regulation.py` — `test_identical_structural_regex_across_groups_is_rejected_by_config`
- `tests/unit/test_structure_planning_regulation.py` — `test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py` — `test_invalid_regex_and_unknown_yaml_field_are_controlled`
- `tests/unit/test_structure_planning_regulation.py` — `test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_old_and_unknown_config_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_pattern_lists_may_be_empty`
- `tests/unit/test_structure_planning_regulation.py` — `test_page_without_configured_header_or_footer_is_unchanged`
- `tests/unit/test_structure_planning_regulation.py` — `test_positional_header_footer_filter_preserves_matching_body_lines`
- `tests/unit/test_structure_planning_regulation.py` — `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_can_return_validated_fragments`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py` — `test_structure_schema_versions_are_explicit`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_topic_evidence_flag_accepts_exact_booleans`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_topic_evidence_flag_rejects_boolean_coercion`
- `tests/unit/test_structure_planning_regulation.py` — `test_wrong_intersection_source_zone_id_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `valid_result`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py::test_duplicate_yaml_alias_and_alias_cycle_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py::test_heading_patterns_require_mandatory_named_captures`
- `tests/unit/test_structure_planning_regulation.py::test_identical_structural_regex_across_groups_is_rejected_by_config`
- `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py::test_invalid_regex_and_unknown_yaml_field_are_controlled`
- `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_config_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py::test_optional_pattern_lists_may_be_empty`
- `tests/unit/test_structure_planning_regulation.py::test_page_without_configured_header_or_footer_is_unchanged`
- `tests/unit/test_structure_planning_regulation.py::test_positional_header_footer_filter_preserves_matching_body_lines`
- `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py::test_structure_schema_versions_are_explicit`
- `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_accepts_exact_booleans`
- `tests/unit/test_structure_planning_regulation.py::test_toc_topic_evidence_flag_rejects_boolean_coercion`
- `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zones`

**Signature**

```python
def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
```

**Purpose**

Implements zones according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `pd.DataFrame({'planning_zone_id': [f'ZONE-{label}' for label in labels], 'source_zone_id': [f'SRC-{label}' for label in labels], 'zone_label_raw': labels, 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256})`.

**Algorithm**

1. Computes `labels` from `['U', 'Ua', 'X', 'UX', 'Z']`.
2. Returns `pd.DataFrame({'planning_zone_id': [f'ZONE-{label}' for label in labels], 'source_zone_id': [f'SRC-{label}' for label in labels], 'zone_label_raw': labels, 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`.

**Known repository callers**

- `tests/unit/test_structure_planning_regulation.py` — `_structure_with_document_layout`
- `tests/unit/test_structure_planning_regulation.py` — `_validate`
- `tests/unit/test_structure_planning_regulation.py` — `test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py` — `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py` — `test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py` — `test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py` — `test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py` — `test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py` — `test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py` — `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_can_return_validated_fragments`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_wrong_intersection_source_zone_id_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_zone_and_general_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `valid_result`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_intersections`

**Signature**

```python
def _intersections(index: PlanningRegulationIndex) -> pd.DataFrame:
```

**Purpose**

Implements intersections according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `pd.DataFrame({'parcel_id': ['PARCEL-1', 'PARCEL-2'], 'planning_zone_id': ['ZONE-U', 'ZONE-Ua'], 'source_zone_id': ['SRC-U', 'SRC-Ua'], 'zone_label_raw': ['U', 'Ua'], 'relation_type': ['AREA_OVERLAP', 'AREA_OVERLAP'], 'intersection_area_m2': [100.0, 50.0], 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256})`.

**Algorithm**

1. Returns `pd.DataFrame({'parcel_id': ['PARCEL-1', 'PARCEL-2'], 'planning_zone_id': ['ZONE-U', 'ZONE-Ua'], 'source_zone_id': ['SRC-U', 'SRC-Ua'], 'zone_label_raw': ['U', 'Ua'], 'relation_type': ['AREA_OVERLAP', 'AREA_OVERLAP'], 'intersection_area_m2': [100.0, 50.0], 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`.

**Known repository callers**

- `tests/unit/test_structure_planning_regulation.py` — `_structure_with_document_layout`
- `tests/unit/test_structure_planning_regulation.py` — `_validate`
- `tests/unit/test_structure_planning_regulation.py` — `test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py` — `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py` — `test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py` — `test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py` — `test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py` — `test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py` — `test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py` — `test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py` — `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_can_return_validated_fragments`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py` — `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_wrong_intersection_source_zone_id_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_zone_and_general_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `valid_result`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_alias_chain_resolves_to_final_configured_target`
- `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`
- `tests/unit/test_structure_planning_regulation.py::test_blank_only_prefix_is_preserved_in_first_actual_section`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_rejects_nonexistent_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_document_lock_mismatch_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_dominant_unmapped_zone_stops_processing`
- `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py::test_evidence_scope_is_derived_from_exact_section_type`
- `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_inputs_are_not_mutated`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_area_cannot_exceed_available_geometry_area`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_column_lineage_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_hash_columns_are_actual_and_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance`
- `tests/unit/test_structure_planning_regulation.py::test_normal_muret_compatible_grammar_remains_deterministic`
- `tests/unit/test_structure_planning_regulation.py::test_optional_intersection_metric_change_invalidates_existing_result`
- `tests/unit/test_structure_planning_regulation.py::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_can_return_validated_fragments`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_changed_ambiguous_grammar`
- `tests/unit/test_structure_planning_regulation.py::test_source_complete_validator_rejects_post_build_source_change`
- `tests/unit/test_structure_planning_regulation.py::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`
- `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_wrong_intersection_source_zone_id_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `valid_result`

**Signature**

```python
def valid_result():
```

**Purpose**

Implements valid result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `(index, result)`.

**Algorithm**

1. Computes `index` from `_index()`.
2. Computes `result` from `structure_planning_regulation(index, _zones(index), _intersections(index), _config(index))`.
3. Returns `(index, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `structure_planning_regulation`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_validate`

**Signature**

```python
def _validate(
    index: PlanningRegulationIndex,
    result,
) -> None:
```

**Purpose**

Validates and rejects malformed validate according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `validate_planning_regulation_structure(index, _zones(index), _intersections(index), _config(index), result)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_config`, `_intersections`, `_zones`, `validate_planning_regulation_structure`.

**Known repository callers**

- `tests/unit/test_structure_planning_regulation.py` — `test_article_parent_semantics_are_enforced`
- `tests/unit/test_structure_planning_regulation.py` — `test_coordinated_frame_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_coordinated_section_row_mutation_is_caught_by_outer_envelope`
- `tests/unit/test_structure_planning_regulation.py` — `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_duplicate_or_reordered_record_partition_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_lossless_partition_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_old_and_unknown_result_config_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_old_and_unknown_section_hash_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_realistic_structure_is_deterministic_and_toc_heading_is_ignored`
- `tests/unit/test_structure_planning_regulation.py` — `test_source_and_result_hash_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_topic_evidence_semantic_mutations_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_unknown_topic_page_reference_is_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_unsorted_section_pages_are_rejected`
- `tests/unit/test_structure_planning_regulation.py` — `test_zone_mapping_contract_mutations_are_rejected`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_article_parent_semantics_are_enforced`
- `tests/unit/test_structure_planning_regulation.py::test_coordinated_frame_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_coordinated_section_row_mutation_is_caught_by_outer_envelope`
- `tests/unit/test_structure_planning_regulation.py::test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_duplicate_or_reordered_record_partition_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_lossless_partition_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_result_config_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_old_and_unknown_section_hash_schema_versions_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_realistic_structure_is_deterministic_and_toc_heading_is_ignored`
- `tests/unit/test_structure_planning_regulation.py::test_source_and_result_hash_mutation_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_topic_evidence_semantic_mutations_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_unknown_topic_page_reference_is_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_unsorted_section_pages_are_rejected`
- `tests/unit/test_structure_planning_regulation.py::test_zone_mapping_contract_mutations_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_structure_with_document_layout`

**Signature**

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

Implements structure with document layout according to the exact implementation and guards in this file.

**Inputs**

- `raw_pages` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `toc_pages` (`tuple[int, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `body_start_page` (`int`; optional/default `1`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `include_toc_evidence` (`bool`; optional/default `False`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `(index, config, result)`.

**Algorithm**

1. Computes `index` from `_index(raw_pages)`.
2. Computes `payload` from `_config(index).model_dump(mode='python')`.
3. Calls `payload['document_layout'].update({'body_start_page': body_start_page, 'table_of_contents_pages': toc_pages, 'include_table_of_contents_in_topic_evidence': include_toc_evidence})` for its validation or side effect.
4. Computes `payload['ignored_patterns']` from `{'page_headers': (), 'page_footers': ()}`.
5. Computes `config` from `PlanningRegulationStructureConfig.model_validate(payload)`.
6. Computes `result` from `structure_planning_regulation(index, _zones(index), _intersections(index), config)`.
7. Calls `validate_planning_regulation_structure(index, _zones(index), _intersections(index), config, result)` for its validation or side effect.
8. Asserts `int(result.sections['source_record_count'].sum()) == len(_line_records(index, config))`.
9. Returns `(index, config, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_line_records`, `_zones`, `int`, `len`, `payload['document_layout'].update`, `result.sections['source_record_count'].sum`, `structure_planning_regulation`, `validate_planning_regulation_structure`.

**Known repository callers**

- `tests/unit/test_structure_planning_regulation.py` — `test_blank_only_toc_blocks_remain_separate_other_sections`
- `tests/unit/test_structure_planning_regulation.py` — `test_blank_toc_followed_only_by_blank_tail_remains_other`
- `tests/unit/test_structure_planning_regulation.py` — `test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py` — `test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py` — `test_ordinary_blank_gap_attaches_to_following_real_heading`
- `tests/unit/test_structure_planning_regulation.py` — `test_trailing_blank_records_attach_to_preceding_factual_section`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_blank_only_toc_blocks_remain_separate_other_sections`
- `tests/unit/test_structure_planning_regulation.py::test_blank_toc_followed_only_by_blank_tail_remains_other`
- `tests/unit/test_structure_planning_regulation.py::test_document_layout_accepts_real_first_and_last_indexed_pages`
- `tests/unit/test_structure_planning_regulation.py::test_existing_empty_toc_page_is_valid_not_nonexistent`
- `tests/unit/test_structure_planning_regulation.py::test_ordinary_blank_gap_attaches_to_following_real_heading`
- `tests/unit/test_structure_planning_regulation.py::test_trailing_blank_records_attach_to_preceding_factual_section`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config_with_structural_patterns`

**Signature**

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

Implements config with structural patterns according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zone_chapter` (`tuple[str, ...] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `general_section` (`tuple[str, ...] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `article` (`tuple[str, ...] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationStructureConfig`. Observed return expression(s): `PlanningRegulationStructureConfig.model_validate(payload)`.

**Algorithm**

1. Computes `payload` from `_config(index).model_dump(mode='python')`.
2. Computes `payload['document_layout']['table_of_contents_pages']` from `()`.
3. Computes `payload['ignored_patterns']` from `{'page_headers': (), 'page_footers': ()}`.
4. Computes `replacements` from `{'zone_chapter': zone_chapter, 'general_section': general_section, 'article': article}`.
5. Iterates `(name, patterns)` over `replacements.items()`. For each value: Checks `patterns is not None`. When true: Computes `payload['heading_patterns'][name]` from `patterns`.
6. Returns `PlanningRegulationStructureConfig.model_validate(payload)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replacements.items`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `replacements.items`.

**Known repository callers**

- `tests/unit/test_structure_planning_regulation.py` — `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py` — `test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py` — `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`
- `tests/unit/test_structure_planning_regulation.py` — `test_zone_and_general_cross_category_match_is_ambiguous`

**Tests**

- `tests/unit/test_structure_planning_regulation.py::test_ambiguous_continuation_candidate_fails_with_record_diagnostic`
- `tests/unit/test_structure_planning_regulation.py::test_general_and_article_cross_category_match_is_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_two_article_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_two_zone_patterns_matching_one_line_are_ambiguous`
- `tests/unit/test_structure_planning_regulation.py::test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`
- `tests/unit/test_structure_planning_regulation.py::test_zone_and_general_cross_category_match_is_ambiguous`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_package_exports_clean_high_level_api`

**Signature**

```python
def test_package_exports_clean_high_level_api() -> None:
```

**Purpose**

Protects the `package exports clean high level api` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `any`, `name.startswith`.

**Expected result**

- Direct assertions: `assert 'structure_planning_regulation' in stages.__all__`; `assert 'validate_planning_regulation_structure' in stages.__all__`; `assert 'validate_planning_regulation_structure_with_fragments' in stages.__all__`; `assert not any((name.startswith('_build_') for name in stages.__all__))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `package exports clean high level api` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `any`, `name.startswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_validator_can_return_validated_fragments`

**Signature**

```python
def test_source_complete_validator_can_return_validated_fragments(valid_result) -> None:
```

**Purpose**

Protects the `source complete validator can return validated fragments` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `fragments` from `validate_planning_regulation_structure_with_fragments(index, _zones(index), _intersections(index), _config(index), result)`.

**Action**

- Calls `_config`, `_intersections`, `_zones`, `fragments.duplicated`, `fragments.duplicated(['section_id', 'page_number']).any`, `fragments['document_id'].eq`, `fragments['document_id'].eq(index.document_id).all`, `validate_planning_regulation_structure_with_fragments`.

**Expected result**

- Direct assertions: `assert tuple(fragments.columns) == ('section_id', 'page_number', 'raw_text', 'section_page_fragment_sha256', 'document_id', 'archive_sha256', 'pdf_sha256', 'index_content_sha256', 'structure_result_content_sha256', 'structure_profile')`; `assert not fragments.duplicated(['section_id', 'page_number']).any()`; `assert fragments['document_id'].eq(index.document_id).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source complete validator can return validated fragments` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_intersections`, `_zones`, `fragments.duplicated`, `fragments.duplicated(['section_id', 'page_number']).any`, `fragments['document_id'].eq`, `fragments['document_id'].eq(index.document_id).all`, `tuple`, `validate_planning_regulation_structure_with_fragments`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_structure_schema_versions_are_explicit`

**Signature**

```python
def test_structure_schema_versions_are_explicit(valid_result) -> None:
```

**Purpose**

Protects the `structure schema versions are explicit` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `config` from `_config(index)`.

**Action**

- Calls `_config`.

**Expected result**

- Direct assertions: `assert config.schema_version == 2`; `assert result.structure_config_schema_version == 2`; `assert SECTION_HASH_SCHEMA_VERSION == 3`; `assert result.section_hash_schema_version == 3`; `assert STRUCTURE_MANIFEST_SCHEMA_VERSION == 4`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `structure schema versions are explicit` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_old_and_unknown_config_schema_versions_are_rejected`

**Signature**

```python
def test_old_and_unknown_config_schema_versions_are_rejected(
    schema_version: int,
) -> None:
```

**Purpose**

Protects the `old and unknown config schema versions are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `schema_version`.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `payload['schema_version']` from `schema_version`.
- Enters managed context(s) `pytest.raises(ValueError, match='unsupported structure config schema')` and executes: Calls `PlanningRegulationStructureConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='unsupported structure config schema'): PlanningRegulationStructureConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `old and unknown config schema versions are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_old_and_unknown_result_config_schema_versions_are_rejected`

**Signature**

```python
def test_old_and_unknown_result_config_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
```

**Purpose**

Protects the `old and unknown result config schema versions are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `schema_version`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='schema version')` and executes: Calls `_validate(index, replace(result, structure_config_schema_version=schema_version))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='schema version'): _validate(index, replace(result, structure_config_schema_version=schema_version))`.

**Regression protected**

- Protects the exact `old and unknown result config schema versions are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_old_and_unknown_section_hash_schema_versions_are_rejected`

**Signature**

```python
def test_old_and_unknown_section_hash_schema_versions_are_rejected(
    valid_result,
    schema_version: int,
) -> None:
```

**Purpose**

Protects the `old and unknown section hash schema versions are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `schema_version`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='schema version')` and executes: Calls `_validate(index, replace(result, section_hash_schema_version=schema_version))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='schema version'): _validate(index, replace(result, section_hash_schema_version=schema_version))`.

**Regression protected**

- Protects the exact `old and unknown section hash schema versions are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_toc_topic_evidence_flag_rejects_boolean_coercion`

**Signature**

```python
def test_toc_topic_evidence_flag_rejects_boolean_coercion(value: object) -> None:
```

**Purpose**

Protects the `toc topic evidence flag rejects boolean coercion` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `payload['document_layout']['include_table_of_contents_in_topic_evidence']` from `value`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `PlanningRegulationStructureConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError): PlanningRegulationStructureConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `toc topic evidence flag rejects boolean coercion` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_toc_topic_evidence_flag_accepts_exact_booleans`

**Signature**

```python
def test_toc_topic_evidence_flag_accepts_exact_booleans(value: bool) -> None:
```

**Purpose**

Protects the `toc topic evidence flag accepts exact booleans` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `payload['document_layout']['include_table_of_contents_in_topic_evidence']` from `value`.
- Computes `validated` from `PlanningRegulationStructureConfig.model_validate(payload)`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`.

**Expected result**

- Direct assertions: `assert validated.document_layout.include_table_of_contents_in_topic_evidence is value`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `toc topic evidence flag accepts exact booleans` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_layout_accepts_real_first_and_last_indexed_pages`

**Signature**

```python
def test_document_layout_accepts_real_first_and_last_indexed_pages() -> None:
```

**Purpose**

Protects the `document layout accepts real first and last indexed pages` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `(index, config, result)` from `_structure_with_document_layout(('CONTENTS', 'ZONE U\nARTICLE U 1 - BODY\nBody text', 'END CONTENTS'), toc_pages=(1, 3), body_start_page=1)`.

**Action**

- Calls `_intersections`, `_structure_with_document_layout`, `_zones`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: `assert result.sections.iloc[0]['page_numbers'] == (1,)`; `assert result.sections.iloc[-1]['page_numbers'] == (3,)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `document layout accepts real first and last indexed pages` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_intersections`, `_structure_with_document_layout`, `_zones`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_layout_rejects_nonexistent_indexed_pages`

**Signature**

```python
def test_document_layout_rejects_nonexistent_indexed_pages(
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `document layout rejects nonexistent indexed pages` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index)`.
- Computes `layout` from `config.document_layout.model_copy(update={field: value})`.
- Computes `forged` from `config.model_copy(update={'document_layout': layout})`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `structure_planning_regulation(index, _zones(index), _intersections(index), forged)` for its validation or side effect.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `config.document_layout.model_copy`, `config.model_copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): structure_planning_regulation(index, _zones(index), _intersections(index), forged)`.

**Regression protected**

- Protects the exact `document layout rejects nonexistent indexed pages` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `config.document_layout.model_copy`, `config.model_copy`, `pytest.mark.parametrize`, `pytest.raises`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_existing_empty_toc_page_is_valid_not_nonexistent`

**Signature**

```python
def test_existing_empty_toc_page_is_valid_not_nonexistent() -> None:
```

**Purpose**

Protects the `existing empty toc page is valid not nonexistent` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `(index, config, result)` from `_structure_with_document_layout(('', 'ZONE U\nARTICLE U 1 - BODY\nBody text'), toc_pages=(1,), body_start_page=2)`.

**Action**

- Calls `_intersections`, `_structure_with_document_layout`, `_zones`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: `assert index.pages.loc[0, 'extraction_status'] == 'EMPTY'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `existing empty toc page is valid not nonexistent` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_intersections`, `_structure_with_document_layout`, `_zones`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_lock_mismatch_is_rejected`

**Signature**

```python
def test_document_lock_mismatch_is_rejected(lock_field: str) -> None:
```

**Purpose**

Protects the `document lock mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `lock_field`.
- Contains 5 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index)`.
- Computes `lock` from `config.document_lock.model_copy(update={lock_field: 'f' * 64 if 'sha256' in lock_field else 'wrong'})`.
- Computes `changed` from `config.model_copy(update={'document_lock': lock})`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='document lock')` and executes: Calls `structure_planning_regulation(index, _zones(index), _intersections(index), changed)` for its validation or side effect.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `config.document_lock.model_copy`, `config.model_copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='document lock'): structure_planning_regulation(index, _zones(index), _intersections(index), changed)`.

**Regression protected**

- Protects the exact `document lock mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `config.document_lock.model_copy`, `config.model_copy`, `pytest.mark.parametrize`, `pytest.raises`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_regex_and_unknown_yaml_field_are_controlled`

**Signature**

```python
def test_invalid_regex_and_unknown_yaml_field_are_controlled(tmp_path: Path) -> None:
```

**Purpose**

Protects the `invalid regex and unknown yaml field are controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `payload` from `_config(index).model_dump(mode='json')`.
- Computes `payload['heading_patterns']['zone_chapter']` from `['[']`.
- Computes `payload['unexpected']` from `True`.
- Computes `path` from `tmp_path / 'bad.yaml'`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `load_planning_regulation_structure_config(path)` for its validation or side effect.

**Action**

- Calls `_config`, `_config(index).model_dump`, `_index`, `load_planning_regulation_structure_config`, `path.write_text`, `yaml.safe_dump`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): load_planning_regulation_structure_config(path)`.

**Regression protected**

- Protects the exact `invalid regex and unknown yaml field are controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_config(index).model_dump`, `_index`, `load_planning_regulation_structure_config`, `path.write_text`, `pytest.raises`, `yaml.safe_dump`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_yaml_alias_and_alias_cycle_are_rejected`

**Signature**

```python
def test_duplicate_yaml_alias_and_alias_cycle_are_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate yaml alias and alias cycle are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 9 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index).model_dump(mode='json')`.
- Computes `cycle` from `tmp_path / 'cycle.yaml'`.
- Computes `config['zone_aliases']` from `{'A': 'B', 'B': 'A'}`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `load_planning_regulation_structure_config(cycle)` for its validation or side effect.
- Computes `duplicate` from `tmp_path / 'duplicate.yaml'`.
- Computes `text` from `yaml.safe_dump(_config(index).model_dump(mode='json'))`.
- Computes `text` from `text.replace('zone_aliases:\n', 'zone_aliases:\n A: U\n A: N\n')`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='Duplicate YAML')` and executes: Calls `load_planning_regulation_structure_config(duplicate)` for its validation or side effect.

**Action**

- Calls `_config`, `_config(index).model_dump`, `_index`, `cycle.write_text`, `duplicate.write_text`, `load_planning_regulation_structure_config`, `text.replace`, `yaml.safe_dump`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): load_planning_regulation_structure_config(cycle)`; `with pytest.raises(PlanningRegulationStructureError, match='Duplicate YAML'): load_planning_regulation_structure_config(duplicate)`.

**Regression protected**

- Protects the exact `duplicate yaml alias and alias cycle are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_config(index).model_dump`, `_index`, `cycle.write_text`, `duplicate.write_text`, `load_planning_regulation_structure_config`, `pytest.raises`, `text.replace`, `yaml.safe_dump`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_realistic_structure_is_deterministic_and_toc_heading_is_ignored`

**Signature**

```python
def test_realistic_structure_is_deterministic_and_toc_heading_is_ignored(
    valid_result,
) -> None:
```

**Purpose**

Protects the `realistic structure is deterministic and toc heading is ignored` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 3 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `chapters` from `result.sections.loc[result.sections['section_type'].eq('ZONE_CHAPTER')]`.
- Computes `general` from `result.sections.loc[result.sections['section_type'].eq('GENERAL')].iloc[0]`.

**Action**

- Calls `_validate`, `chapters['zone_chapter_label'].eq`, `chapters['zone_chapter_label'].tolist`, `range`, `result.sections['section_id'].tolist`, `result.sections['section_type'].eq`.

**Expected result**

- Direct assertions: `assert result.sections['section_id'].tolist() == [f'SECTION-{number:04d}' for number in range(1, len(result.sections) + 1)]`; `assert chapters['zone_chapter_label'].tolist() == ['U', 'N', 'Z', 'Z']`; `assert len(chapters.loc[chapters['zone_chapter_label'].eq('U')]) == 1`; `assert general['heading_raw'] == 'ARTICLE 1 - GENERAL PROVISIONS'`; `assert 'General energy rule.' in general['raw_text']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `realistic structure is deterministic and toc heading is ignored` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `chapters['zone_chapter_label'].eq`, `chapters['zone_chapter_label'].tolist`, `len`, `range`, `result.sections['section_id'].tolist`, `result.sections['section_type'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zone_article_parent_and_multi_page_text_are_preserved`

**Signature**

```python
def test_zone_article_parent_and_multi_page_text_are_preserved(valid_result) -> None:
```

**Purpose**

Protects the `zone article parent and multi page text are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 3 explicit setup/context statement(s).
- Computes `(_, result)` from `valid_result`.
- Computes `article` from `result.sections.loc[result.sections['heading_raw'].str.startswith('ARTICLE U 1')].iloc[0]`.
- Computes `parent` from `result.sections.set_index('section_id').loc[article['parent_section_id']]`.

**Action**

- Calls `result.sections.set_index`, `result.sections['heading_raw'].str.startswith`.

**Expected result**

- Direct assertions: `assert parent['section_type'] == 'ZONE_CHAPTER'`; `assert tuple(article['page_numbers']) == (3, 4)`; `assert 'First page energy text.' in article['raw_text']`; `assert 'Second page of the same article.' in article['raw_text']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `zone article parent and multi page text are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `result.sections.set_index`, `result.sections['heading_raw'].str.startswith`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping`

**Signature**

```python
def test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping(valid_result) -> None:
```

**Purpose**

Protects the `exact alias unmapped ambiguous and no fuzzy mapping` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, result)` from `valid_result`.
- Computes `mappings` from `result.zone_mapping.set_index('source_zone_label_raw')`.

**Action**

- Calls `result.zone_mapping.set_index`.

**Expected result**

- Direct assertions: `assert mappings.at['U', 'mapping_status'] == 'EXACT'`; `assert mappings.at['Ua', 'mapping_status'] == 'CONFIG_ALIAS'`; `assert mappings.at['X', 'mapping_status'] == 'UNMAPPED'`; `assert mappings.at['UX', 'mapping_status'] == 'UNMAPPED'`; `assert mappings.at['Z', 'mapping_status'] == 'AMBIGUOUS'`; `assert mappings.at['X', 'dominant_candidate_count'] == 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact alias unmapped ambiguous and no fuzzy mapping` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `result.zone_mapping.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_topic_evidence_distinguishes_general_and_zone_specific`

**Signature**

```python
def test_topic_evidence_distinguishes_general_and_zone_specific(valid_result) -> None:
```

**Purpose**

Protects the `topic evidence distinguishes general and zone specific` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, result)` from `valid_result`.
- Computes `energy` from `result.topic_evidence.loc[result.topic_evidence['topic'].eq('energy')]`.

**Action**

- Calls `all`, `result.topic_evidence['topic'].eq`.

**Expected result**

- Direct assertions: `assert set(energy['evidence_scope']) == {'GENERAL_RULE', 'ZONE_SPECIFIC_RULE'}`; `assert set(energy['occurrence_count']) == {1}`; `assert all((context for context in energy['raw_context']))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `topic evidence distinguishes general and zone specific` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `result.topic_evidence['topic'].eq`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_evidence_scope_is_derived_from_exact_section_type`

**Signature**

```python
def test_evidence_scope_is_derived_from_exact_section_type() -> None:
```

**Purpose**

Protects the `evidence scope is derived from exact section type` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 13 explicit setup/context statement(s).
- Computes `index` from `_index(('energy cover text', 'ARTICLE 1 - GENERAL\nenergy general text', 'ZONE U\nenergy chapter text\nARTICLE U 1 - BODY\nenergy article text'))`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `payload['document_layout']['table_of_contents_pages']` from `()`.
- Computes `payload['ignored_patterns']` from `{'page_headers': (), 'page_footers': ()}`.
- Computes `config` from `PlanningRegulationStructureConfig.model_validate(payload)`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), _intersections(index), config)`.
- Computes `section_types` from `result.sections.set_index('section_id')['section_type']`.
- Computes `scopes_by_type` from `{section_type: set(result.topic_evidence.loc[result.topic_evidence['section_id'].map(section_types).eq(section_type), 'evidence_scope']) for section_type in ('GENERAL', 'ZONE_CHAPTER', 'ARTICLE', 'OTHER')}`.
- Computes `evidence` from `result.topic_evidence.copy(deep=True)`.
- Computes `other_section_ids` from `set(result.sections.loc[result.sections['section_type'].eq('OTHER'), 'section_id'])`.
- Computes `row_index` from `evidence.index[evidence['section_id'].isin(other_section_ids)][0]`.
- Computes `evidence.loc[row_index, 'evidence_scope']` from `'GENERAL_RULE'`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_zones`, `evidence['section_id'].isin`, `replace`, `result.sections.set_index`, `result.sections['section_type'].eq`, `result.topic_evidence.copy`, `result.topic_evidence['section_id'].map`, `result.topic_evidence['section_id'].map(section_types).eq`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: `assert scopes_by_type == {'GENERAL': {'GENERAL_RULE'}, 'ZONE_CHAPTER': {'ZONE_SPECIFIC_RULE'}, 'ARTICLE': {'ZONE_SPECIFIC_RULE'}, 'OTHER': {'OTHER_TEXT'}}`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='scope'): validate_planning_regulation_structure(index, _zones(index), _intersections(index), config, replace(result, topic_evidence=evidence))`.

**Regression protected**

- Protects the exact `evidence scope is derived from exact section type` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_zones`, `evidence['section_id'].isin`, `pytest.raises`, `replace`, `result.sections.set_index`, `result.sections['section_type'].eq`, `result.topic_evidence.copy`, `result.topic_evidence['section_id'].map`, `result.topic_evidence['section_id'].map(section_types).eq`, `set`, `structure_planning_regulation`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_reversed_topic_mapping_keys_do_not_change_output_or_hashes`

**Signature**

```python
def test_reversed_topic_mapping_keys_do_not_change_output_or_hashes() -> None:
```

**Purpose**

Protects the `reversed topic mapping keys do not change output or hashes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `forward` from `_config(index)`.
- Computes `payload` from `forward.model_dump(mode='python')`.
- Computes `payload['topics']` from `dict(reversed(tuple(payload['topics'].items())))`.
- Computes `reversed_topics` from `PlanningRegulationStructureConfig.model_validate(payload)`.
- Computes `forward_result` from `structure_planning_regulation(index, _zones(index), _intersections(index), forward)`.
- Computes `reversed_result` from `structure_planning_regulation(index, _zones(index), _intersections(index), reversed_topics)`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_index`, `_intersections`, `_zones`, `forward.model_dump`, `forward_result.topic_evidence['topic'].tolist`, `payload['topics'].items`, `pd.testing.assert_frame_equal`, `reversed`, `sorted`.

**Expected result**

- Direct assertions: `assert tuple(reversed_topics.topics) == tuple(reversed(tuple(forward.topics)))`; `assert forward_result.topic_evidence['topic'].tolist() == sorted(forward_result.topic_evidence['topic'].tolist())`; `assert forward_result.structure_config_sha256 == reversed_result.structure_config_sha256`; `assert forward_result.topic_evidence_content_sha256 == reversed_result.topic_evidence_content_sha256`; `assert forward_result.structure_result_content_sha256 == reversed_result.structure_result_content_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `reversed topic mapping keys do not change output or hashes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_index`, `_intersections`, `_zones`, `dict`, `forward.model_dump`, `forward_result.topic_evidence['topic'].tolist`, `payload['topics'].items`, `pd.testing.assert_frame_equal`, `reversed`, `sorted`, `structure_planning_regulation`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_equal_length_overlap_uses_configured_term_order_as_tie_break`

**Signature**

```python
def test_equal_length_overlap_uses_configured_term_order_as_tie_break() -> None:
```

**Purpose**

Protects the `equal length overlap uses configured term order as tie break` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 15 explicit setup/context statement(s).
- Computes `normalized` from `normalize_planning_search_text('alpha beta gamma')`.
- Computes `forward_terms` from `('alpha beta', 'beta gamma')`.
- Computes `reverse_terms` from `tuple(reversed(forward_terms))`.
- Computes `forward_matches` from `_literal_topic_matches(normalized, forward_terms)`.
- Computes `reverse_matches` from `_literal_topic_matches(normalized, reverse_terms)`.
- Computes `index` from `_index(('ZONE U\nARTICLE U 1 - TEST\nalpha beta gamma',))`.
- Computes `base_payload` from `_config(index).model_dump(mode='python')`.
- Computes `base_payload['document_layout']['table_of_contents_pages']` from `()`.
- Computes `base_payload['topics']` from `{'tie': forward_terms}`.
- Computes `forward_config` from `PlanningRegulationStructureConfig.model_validate(base_payload)`.
- Computes `reverse_payload` from `forward_config.model_dump(mode='python')`.
- Computes `reverse_payload['topics']` from `{'tie': reverse_terms}`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_literal_topic_matches`, `_zones`, `forward_config.model_dump`, `forward_result.topic_evidence['search_term'].tolist`, `normalize_planning_search_text`, `reverse_result.topic_evidence['search_term'].tolist`, `reversed`.

**Expected result**

- Direct assertions: `assert [match.search_term for match in forward_matches] == ['alpha beta']`; `assert [match.search_term for match in reverse_matches] == ['beta gamma']`; `assert (forward_matches[0].normalized_start, forward_matches[0].normalized_end) == (0, 10)`; `assert (reverse_matches[0].normalized_start, reverse_matches[0].normalized_end) == (6, 16)`; `assert forward_result.topic_evidence['search_term'].tolist() == ['alpha beta']`; `assert reverse_result.topic_evidence['search_term'].tolist() == ['beta gamma']`; `assert forward_result.structure_config_sha256 != reverse_result.structure_config_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `equal length overlap uses configured term order as tie break` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_literal_topic_matches`, `_zones`, `forward_config.model_dump`, `forward_result.topic_evidence['search_term'].tolist`, `normalize_planning_search_text`, `reverse_result.topic_evidence['search_term'].tolist`, `reversed`, `structure_planning_regulation`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inputs_are_not_mutated`

**Signature**

```python
def test_inputs_are_not_mutated() -> None:
```

**Purpose**

Protects the `inputs are not mutated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `zones` from `_zones(index)`.
- Computes `intersections` from `_intersections(index)`.
- Computes `pages_before` from `index.pages.copy(deep=True)`.
- Computes `zones_before` from `zones.copy(deep=True)`.
- Computes `intersections_before` from `intersections.copy(deep=True)`.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `index.pages.copy`, `intersections.copy`, `pd.testing.assert_frame_equal`, `zones.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `inputs are not mutated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `index.pages.copy`, `intersections.copy`, `pd.testing.assert_frame_equal`, `structure_planning_regulation`, `zones.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_frame_mutation_is_rejected`

**Signature**

```python
def test_coordinated_frame_mutation_is_rejected(
    valid_result,
    frame_name: str,
    hash_name: str,
    column: str,
) -> None:
```

**Purpose**

Protects the `coordinated frame mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `frame_name`, `hash_name`, `column`.
- Contains 6 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `frame` from `getattr(result, frame_name).copy(deep=True)`.
- Computes `changed` from `replace(result, **{frame_name: frame})`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, changed)` for its validation or side effect.
- Computes `changed` from `replace(changed, **{hash_name: 'f' * 64})`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, changed)` for its validation or side effect.

**Action**

- Calls `_validate`, `getattr`, `getattr(result, frame_name).copy`, `int`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, changed)`; `with pytest.raises(PlanningRegulationStructureError): _validate(index, changed)`.

**Regression protected**

- Protects the exact `coordinated frame mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `getattr`, `getattr(result, frame_name).copy`, `int`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_topic_page_reference_is_rejected`

**Signature**

```python
def test_unknown_topic_page_reference_is_rejected(valid_result) -> None:
```

**Purpose**

Protects the `unknown topic page reference is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `evidence` from `result.topic_evidence.copy(deep=True)`.
- Computes `evidence.loc[0, 'page_number']` from `999`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='unknown page')` and executes: Calls `_validate(index, replace(result, topic_evidence=evidence))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`, `result.topic_evidence.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='unknown page'): _validate(index, replace(result, topic_evidence=evidence))`.

**Regression protected**

- Protects the exact `unknown topic page reference is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.raises`, `replace`, `result.topic_evidence.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_section_row_mutation_is_caught_by_outer_envelope`

**Signature**

```python
def test_coordinated_section_row_mutation_is_caught_by_outer_envelope(
    valid_result,
) -> None:
```

**Purpose**

Protects the `coordinated section row mutation is caught by outer envelope` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 8 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `sections` from `result.sections.copy(deep=True)`.
- Computes `sections.loc[0, 'raw_text']` from `f"{sections.loc[0, 'raw_text']} changed"`.
- Computes `sections.loc[0, 'normalized_text']` from `_normalize_search_text(sections.loc[0, 'raw_text'])`.
- Computes `sections.loc[0, 'character_count']` from `len(sections.loc[0, 'raw_text'])`.
- Computes `row` from `sections.loc[0].to_dict()`.
- Computes `sections.loc[0, 'section_content_sha256']` from `_section_content_sha256(row)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, replace(result, sections=sections))` for its validation or side effect.

**Action**

- Calls `_normalize_search_text`, `_section_content_sha256`, `_validate`, `replace`, `result.sections.copy`, `sections.loc[0].to_dict`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, replace(result, sections=sections))`.

**Regression protected**

- Protects the exact `coordinated section row mutation is caught by outer envelope` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_normalize_search_text`, `_section_content_sha256`, `_validate`, `len`, `pytest.raises`, `replace`, `result.sections.copy`, `sections.loc[0].to_dict`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_dominant_unmapped_zone_stops_processing`

**Signature**

```python
def test_dominant_unmapped_zone_stops_processing() -> None:
```

**Purpose**

Protects the `dominant unmapped zone stops processing` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `relations` from `_intersections(index).copy(deep=True)`.
- Computes `relations.loc[0, ['planning_zone_id', 'source_zone_id', 'zone_label_raw']]` from `['ZONE-X', 'SRC-X', 'X']`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='Dominant candidate')` and executes: Calls `structure_planning_regulation(index, _zones(index), relations, _config(index))` for its validation or side effect.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_intersections(index).copy`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='Dominant candidate'): structure_planning_regulation(index, _zones(index), relations, _config(index))`.

**Regression protected**

- Protects the exact `dominant unmapped zone stops processing` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_intersections(index).copy`, `_zones`, `pytest.raises`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_positional_header_footer_filter_preserves_matching_body_lines`

**Signature**

```python
def test_positional_header_footer_filter_preserves_matching_body_lines() -> None:
```

**Purpose**

Protects the `positional header footer filter preserves matching body lines` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index(('\nTest PLU\n\nARTICLE 1 - GENERAL PROVISIONS\nTest PLU\n100\nBody text\n\n42\n',))`.
- Computes `config` from `_config(index)`.
- Computes `records` from `_line_records(index, config)`.
- Computes `retained` from `[record.raw for record in records]`.

**Action**

- Calls `_config`, `_index`, `_line_records`.

**Expected result**

- Direct assertions: `assert 'Test PLU' in retained`; `assert '100' in retained`; `assert '42' not in retained`; `assert retained[0] == 'ARTICLE 1 - GENERAL PROVISIONS'`; `assert records[0].page_line_number == 4`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `positional header footer filter preserves matching body lines` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_line_records`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_page_without_configured_header_or_footer_is_unchanged`

**Signature**

```python
def test_page_without_configured_header_or_footer_is_unchanged() -> None:
```

**Purpose**

Protects the `page without configured header or footer is unchanged` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `index` from `_index(('ARTICLE 1 - GENERAL\n100\nBody',))`.
- Computes `config` from `_config(index)`.
- Computes `config` from `config.model_copy(update={'ignored_patterns': config.ignored_patterns.model_copy(update={'page_headers': (), 'page_footers': ()})})`.

**Action**

- Calls `_config`, `_index`, `_line_records`, `config.ignored_patterns.model_copy`, `config.model_copy`.

**Expected result**

- Direct assertions: `assert [record.raw for record in _line_records(index, config)] == ['ARTICLE 1 - GENERAL', '100', 'Body']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `page without configured header or footer is unchanged` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_line_records`, `config.ignored_patterns.model_copy`, `config.model_copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_blank_only_prefix_is_preserved_in_first_actual_section`

**Signature**

```python
def test_blank_only_prefix_is_preserved_in_first_actual_section(
    raw_pages: tuple[str, ...],
    expected_pages: tuple[int, ...],
    expected_prefix: str,
) -> None:
```

**Purpose**

Protects the `blank only prefix is preserved in first actual section` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `raw_pages`, `expected_pages`, `expected_prefix`.
- Contains 8 explicit setup/context statement(s).
- Computes `index` from `_index(raw_pages)`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `payload['document_layout']['table_of_contents_pages']` from `()`.
- Computes `payload['ignored_patterns']` from `{'page_headers': (), 'page_footers': ()}`.
- Computes `config` from `PlanningRegulationStructureConfig.model_validate(payload)`.
- Computes `records` from `_line_records(index, config)`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), _intersections(index), config)`.
- Computes `first` from `result.sections.iloc[0]`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_line_records`, `_zones`, `first['raw_text'].startswith`, `int`, `result.sections['section_type'].tolist`, `result.sections['source_record_count'].sum`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: `assert first['section_type'] == 'ZONE_CHAPTER'`; `assert first['heading_raw'] == 'ZONE U'`; `assert first['start_record_id'] == 'RECORD-000001'`; `assert tuple(first['page_numbers']) == expected_pages`; `assert first['raw_text'].startswith(expected_prefix)`; `assert int(result.sections['source_record_count'].sum()) == len(records)`; `assert 'OTHER' not in result.sections['section_type'].tolist()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `blank only prefix is preserved in first actual section` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_line_records`, `_zones`, `first['raw_text'].startswith`, `int`, `len`, `pytest.mark.parametrize`, `result.sections['section_type'].tolist`, `result.sections['source_record_count'].sum`, `structure_planning_regulation`, `tuple`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence`

**Signature**

```python
def test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence() -> None:
```

**Purpose**

Protects the `toc blocks anywhere are other and toggle topic evidence` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 12 explicit setup/context statement(s).
- Computes `index` from `_index(('CONTENTS\nARTICLE 9 - energy', 'ZONE N\nenergy contents', 'ARTICLE 1 - GENERAL\nrisk body', 'ARTICLE 8 - energy', 'ZONE Z\nenergy contents', 'ZONE U\nARTICLE U 1 - BODY\nenergy body', 'ARTICLE 7 - energy'))`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `payload['ignored_patterns']` from `{'page_headers': (), 'page_footers': ()}`.
- Computes `excluded_config` from `PlanningRegulationStructureConfig.model_validate(payload)`.
- Computes `included_payload` from `excluded_config.model_dump(mode='python')`.
- Computes `included_payload['document_layout']['include_table_of_contents_in_topic_evidence']` from `True`.
- Computes `included_config` from `PlanningRegulationStructureConfig.model_validate(included_payload)`.
- Computes `excluded` from `structure_planning_regulation(index, _zones(index), _intersections(index), excluded_config)`.
- Computes `included` from `structure_planning_regulation(index, _zones(index), _intersections(index), included_config)`.
- Computes `excluded_other` from `excluded.sections.loc[excluded.sections['section_type'].eq('OTHER')]`.
- Computes `toc_pages` from `{1, 2, 4, 5, 7}`.
- Computes `included_toc` from `included.topic_evidence.loc[included.topic_evidence['page_number'].isin(toc_pages)]`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_zones`, `excluded.sections['section_type'].eq`, `excluded_config.model_dump`, `excluded_other['heading_raw'].tolist`, `excluded_other['page_numbers'].tolist`, `included.topic_evidence['page_number'].isin`, `payload['document_layout'].update`, `pd.testing.assert_frame_equal`, `range`, `toc_pages.isdisjoint`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: `assert excluded_other['page_numbers'].tolist() == [(1, 2), (4, 5), (7,)]`; `assert excluded_other['heading_raw'].tolist() == ['CONTENTS', 'ARTICLE 8 - energy', 'ARTICLE 7 - energy']`; `assert toc_pages.isdisjoint(excluded.topic_evidence['page_number'])`; `assert set(excluded.topic_evidence['page_number']) == {3, 6}`; `assert set(included.topic_evidence['page_number']) == set(range(1, 8))`; `assert set(included_toc['evidence_scope']) == {'OTHER_TEXT'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `toc blocks anywhere are other and toggle topic evidence` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_zones`, `excluded.sections['section_type'].eq`, `excluded_config.model_dump`, `excluded_other['heading_raw'].tolist`, `excluded_other['page_numbers'].tolist`, `included.topic_evidence['page_number'].isin`, `payload['document_layout'].update`, `pd.testing.assert_frame_equal`, `range`, `set`, `structure_planning_regulation`, `toc_pages.isdisjoint`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_blank_gap_after_toc_is_preserved_without_a_blank_other_section`

**Signature**

```python
def test_blank_gap_after_toc_is_preserved_without_a_blank_other_section() -> None:
```

**Purpose**

Protects the `blank gap after toc is preserved without a blank other section` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 8 explicit setup/context statement(s).
- Computes `index` from `_index(('ARTICLE 1 - GENERAL\nGeneral text', 'CONTENTS\nARTICLE 9 - fake entry', ' \n\t', 'ZONE U\nARTICLE U 1 - BODY\nBody text'))`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `payload['document_layout']['table_of_contents_pages']` from `(2,)`.
- Computes `payload['ignored_patterns']` from `{'page_headers': (), 'page_footers': ()}`.
- Computes `config` from `PlanningRegulationStructureConfig.model_validate(payload)`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), _intersections(index), config)`.
- Computes `other` from `result.sections.loc[result.sections['section_type'].eq('OTHER')]`.
- Computes `chapter` from `result.sections.loc[result.sections['section_type'].eq('ZONE_CHAPTER')].iloc[0]`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_zones`, `chapter['raw_text'].startswith`, `other['page_numbers'].tolist`, `result.sections['section_type'].eq`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: `assert other['page_numbers'].tolist() == [(2,)]`; `assert tuple(chapter['page_numbers']) == (3, 4)`; `assert chapter['heading_raw'] == 'ZONE U'`; `assert chapter['raw_text'].startswith(' \n\t\nZONE U')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `blank gap after toc is preserved without a blank other section` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `_intersections`, `_zones`, `chapter['raw_text'].startswith`, `other['page_numbers'].tolist`, `result.sections['section_type'].eq`, `structure_planning_regulation`, `tuple`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_blank_only_toc_blocks_remain_separate_other_sections`

**Signature**

```python
def test_blank_only_toc_blocks_remain_separate_other_sections(
    toc_raw_pages: tuple[str, ...],
    expected_pages: tuple[int, ...],
) -> None:
```

**Purpose**

Protects the `blank only toc blocks remain separate other sections` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `toc_raw_pages`, `expected_pages`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, result)` from `_structure_with_document_layout(('ARTICLE 1 - GENERAL\nGeneral text', *toc_raw_pages, 'ZONE U\nARTICLE U 1 - BODY\nBody text'), toc_pages=expected_pages)`.
- Computes `other` from `result.sections.loc[result.sections['section_type'].eq('OTHER')]`.

**Action**

- Calls `_structure_with_document_layout`, `result.sections['section_type'].eq`.

**Expected result**

- Direct assertions: `assert len(other) == 1`; `assert tuple(other.iloc[0]['page_numbers']) == expected_pages`; `assert not str(other.iloc[0]['raw_text']).strip()`; `assert other.iloc[0]['heading_raw'] == ''`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `blank only toc blocks remain separate other sections` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_structure_with_document_layout`, `len`, `pytest.mark.parametrize`, `result.sections['section_type'].eq`, `str`, `str(other.iloc[0]['raw_text']).strip`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_blank_toc_followed_only_by_blank_tail_remains_other`

**Signature**

```python
def test_blank_toc_followed_only_by_blank_tail_remains_other() -> None:
```

**Purpose**

Protects the `blank toc followed only by blank tail remains other` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, result)` from `_structure_with_document_layout(('ZONE U\nARTICLE U 1 - BODY\nBody text', ' \n\t', '\t\n '), toc_pages=(2,))`.
- Computes `other` from `result.sections.loc[result.sections['section_type'].eq('OTHER')]`.

**Action**

- Calls `_structure_with_document_layout`, `result.sections['section_type'].eq`.

**Expected result**

- Direct assertions: `assert len(other) == 1`; `assert tuple(other.iloc[0]['page_numbers']) == (2, 3)`; `assert not str(other.iloc[0]['raw_text']).strip()`; `assert other.iloc[0]['heading_raw'] == ''`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `blank toc followed only by blank tail remains other` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_structure_with_document_layout`, `len`, `result.sections['section_type'].eq`, `str`, `str(other.iloc[0]['raw_text']).strip`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ordinary_blank_gap_attaches_to_following_real_heading`

**Signature**

```python
def test_ordinary_blank_gap_attaches_to_following_real_heading() -> None:
```

**Purpose**

Protects the `ordinary blank gap attaches to following real heading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, result)` from `_structure_with_document_layout(('ARTICLE 1 - GENERAL\nGeneral text', ' \n\t', 'ZONE U\nARTICLE U 1 - BODY\nBody text'))`.
- Computes `chapter` from `result.sections.loc[result.sections['section_type'].eq('ZONE_CHAPTER')].iloc[0]`.

**Action**

- Calls `_structure_with_document_layout`, `result.sections['section_type'].eq`.

**Expected result**

- Direct assertions: `assert tuple(chapter['page_numbers']) == (2, 3)`; `assert str(chapter['raw_text']).startswith(' \n\t\nZONE U')`; `assert chapter['heading_raw'] == 'ZONE U'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `ordinary blank gap attaches to following real heading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_structure_with_document_layout`, `result.sections['section_type'].eq`, `str`, `str(chapter['raw_text']).startswith`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_trailing_blank_records_attach_to_preceding_factual_section`

**Signature**

```python
def test_trailing_blank_records_attach_to_preceding_factual_section() -> None:
```

**Purpose**

Protects the `trailing blank records attach to preceding factual section` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, result)` from `_structure_with_document_layout(('ZONE U\nARTICLE U 1 - BODY\nBody text', ' \n\t'))`.
- Computes `final_section` from `result.sections.iloc[-1]`.

**Action**

- Calls `_structure_with_document_layout`.

**Expected result**

- Direct assertions: `assert final_section['section_type'] == 'ARTICLE'`; `assert tuple(final_section['page_numbers']) == (1, 2)`; `assert str(final_section['raw_text']).endswith(' \n\t')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `trailing blank records attach to preceding factual section` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_structure_with_document_layout`, `str`, `str(final_section['raw_text']).endswith`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_heading_patterns_require_mandatory_named_captures`

**Signature**

```python
def test_heading_patterns_require_mandatory_named_captures(
    group: str,
    pattern: str,
) -> None:
```

**Purpose**

Protects the `heading patterns require mandatory named captures` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `group`, `pattern`.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index)`.
- Computes `patterns` from `config.heading_patterns.model_copy(update={group: (pattern,)})`.
- Enters managed context(s) `pytest.raises(ValueError, match='named captures')` and executes: Calls `PlanningRegulationStructureConfig.model_validate(config.model_dump(mode='python') | {'heading_patterns': patterns.model_dump(mode='python')})` for its validation or side effect.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_index`, `config.heading_patterns.model_copy`, `config.model_dump`, `patterns.model_dump`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='named captures'): PlanningRegulationStructureConfig.model_validate(config.model_dump(mode='python') | {'heading_patterns': patterns.model_dump(mode='python')})`.

**Regression protected**

- Protects the exact `heading patterns require mandatory named captures` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_index`, `config.heading_patterns.model_copy`, `config.model_dump`, `patterns.model_dump`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_optional_pattern_lists_may_be_empty`

**Signature**

```python
def test_optional_pattern_lists_may_be_empty() -> None:
```

**Purpose**

Protects the `optional pattern lists may be empty` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index)`.
- Computes `payload` from `config.model_dump(mode='python')`.
- Computes `payload['heading_patterns']['continuation']` from `()`.
- Computes `payload['ignored_patterns']` from `{'page_headers': (), 'page_footers': ()}`.
- Computes `validated` from `PlanningRegulationStructureConfig.model_validate(payload)`.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_index`, `config.model_dump`.

**Expected result**

- Direct assertions: `assert validated.heading_patterns.continuation == ()`; `assert validated.ignored_patterns.page_headers == ()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `optional pattern lists may be empty` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_index`, `config.model_dump`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unique_zone_heading_and_nonheading_line_are_classified_deterministically`

**Signature**

```python
def test_unique_zone_heading_and_nonheading_line_are_classified_deterministically() -> None:
```

**Purpose**

Protects the `unique zone heading and nonheading line are classified deterministically` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index(('Ordinary factual text\nZONE U\nARTICLE U 1 - BODY\nBody text',))`.
- Computes `config` from `_config_with_structural_patterns(index)`.
- Computes `records` from `_line_records(index, config)`.
- Computes `events` from `_heading_events(records, config)`.

**Action**

- Calls `_config_with_structural_patterns`, `_heading_events`, `_index`, `_line_records`, `all`.

**Expected result**

- Direct assertions: `assert [event.section_type for event in events] == ['ZONE_CHAPTER', 'ARTICLE']`; `assert events[0].record_position == 1`; `assert events[0].zone_chapter_label == 'U'`; `assert all((event.record_position != 0 for event in events))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unique zone heading and nonheading line are classified deterministically` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config_with_structural_patterns`, `_heading_events`, `_index`, `_line_records`, `all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_two_zone_patterns_matching_one_line_are_ambiguous`

**Signature**

```python
def test_two_zone_patterns_matching_one_line_are_ambiguous() -> None:
```

**Purpose**

Protects the `two zone patterns matching one line are ambiguous` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index(('ZONE U\nARTICLE U 1 - BODY\nBody',))`.
- Computes `config` from `_config_with_structural_patterns(index, zone_chapter=('^ZONE\\s+(?P<label>[A-Z]+)$', '^ZONE[ ](?P<label>[A-Z]+)$'))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `structure_planning_regulation(index, _zones(index), _intersections(index), config)` for its validation or side effect.
- Computes `message` from `str(captured.value)`.

**Action**

- Calls `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`.

**Expected result**

- Direct assertions: `assert 'Ambiguous structural heading' in message`; `assert 'RECORD-000001' in message`; `assert 'page 1' in message`; `assert 'line 1' in message`; `assert 'ZONE_CHAPTER[0]' in message`; `assert 'ZONE_CHAPTER[1]' in message`; `assert 'ZONE U' not in message`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError) as captured: structure_planning_regulation(index, _zones(index), _intersections(index), config)`.

**Regression protected**

- Protects the exact `two zone patterns matching one line are ambiguous` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`, `pytest.raises`, `str`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_two_article_patterns_matching_one_line_are_ambiguous`

**Signature**

```python
def test_two_article_patterns_matching_one_line_are_ambiguous() -> None:
```

**Purpose**

Protects the `two article patterns matching one line are ambiguous` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `index` from `_index(('ZONE U\nARTICLE U 1 - BODY\nBody',))`.
- Computes `config` from `_config_with_structural_patterns(index, article=('^ARTICLE\\s+(?P<zone>[A-Z]+)\\s+(?P<number>\\d+)\\s*-\\s*(?P<title>.*)$', '^ARTICLE[ ](?P<zone>[A-Z]+)[ ](?P<number>\\d+)[ ]-[ ](?P<title>.*)$'))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='ARTICLE\\[0\\].*ARTICLE\\[1\\]')` and executes: Calls `structure_planning_regulation(index, _zones(index), _intersections(index), config)` for its validation or side effect.

**Action**

- Calls `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='ARTICLE\\[0\\].*ARTICLE\\[1\\]'): structure_planning_regulation(index, _zones(index), _intersections(index), config)`.

**Regression protected**

- Protects the exact `two article patterns matching one line are ambiguous` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`, `pytest.raises`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_general_and_article_cross_category_match_is_ambiguous`

**Signature**

```python
def test_general_and_article_cross_category_match_is_ambiguous() -> None:
```

**Purpose**

Protects the `general and article cross category match is ambiguous` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index(('ARTICLE 1 - GENERAL\nBody',))`.
- Computes `config` from `_config_with_structural_patterns(index, article=('^ARTICLE\\s+(?P<zone>[A-Z]*)(?P<number>\\d+)\\s*-\\s*(?P<title>.*)$',))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `structure_planning_regulation(index, _zones(index), _intersections(index), config)` for its validation or side effect.
- Computes `message` from `str(captured.value)`.

**Action**

- Calls `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`.

**Expected result**

- Direct assertions: `assert 'GENERAL[0]' in message`; `assert 'ARTICLE[0]' in message`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError) as captured: structure_planning_regulation(index, _zones(index), _intersections(index), config)`.

**Regression protected**

- Protects the exact `general and article cross category match is ambiguous` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`, `pytest.raises`, `str`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zone_and_general_cross_category_match_is_ambiguous`

**Signature**

```python
def test_zone_and_general_cross_category_match_is_ambiguous() -> None:
```

**Purpose**

Protects the `zone and general cross category match is ambiguous` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index(('ZONE U\nBody',))`.
- Computes `config` from `_config_with_structural_patterns(index, general_section=('^ZONE\\s+(?P<number>[A-Z]+)(?P<title>)$',))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `structure_planning_regulation(index, _zones(index), _intersections(index), config)` for its validation or side effect.
- Computes `message` from `str(captured.value)`.

**Action**

- Calls `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`.

**Expected result**

- Direct assertions: `assert 'ZONE_CHAPTER[0]' in message`; `assert 'GENERAL[0]' in message`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError) as captured: structure_planning_regulation(index, _zones(index), _intersections(index), config)`.

**Regression protected**

- Protects the exact `zone and general cross category match is ambiguous` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`, `pytest.raises`, `str`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_identical_structural_regex_across_groups_is_rejected_by_config`

**Signature**

```python
def test_identical_structural_regex_across_groups_is_rejected_by_config() -> None:
```

**Purpose**

Protects the `identical structural regex across groups is rejected by config` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `payload` from `_config(index).model_dump(mode='python')`.
- Computes `repeated` from `'^(?P<label>ZONE)$'`.
- Computes `payload['heading_patterns']['zone_chapter']` from `(repeated,)`.
- Computes `payload['heading_patterns']['general_section']` from `(repeated,)`.
- Enters managed context(s) `pytest.raises(ValueError, match='reused across groups')` and executes: Calls `PlanningRegulationStructureConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='reused across groups'): PlanningRegulationStructureConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `identical structural regex across groups is rejected by config` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `PlanningRegulationStructureConfig.model_validate`, `_config`, `_config(index).model_dump`, `_index`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_ambiguous_continuation_candidate_fails_with_record_diagnostic`

**Signature**

```python
def test_ambiguous_continuation_candidate_fails_with_record_diagnostic() -> None:
```

**Purpose**

Protects the `ambiguous continuation candidate fails with record diagnostic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index(('ARTICLE 1 - GENERAL\nAMBIGUOUS\nBody',))`.
- Computes `config` from `_config_with_structural_patterns(index, zone_chapter=('^ZONE\\s+(?P<label>[A-Z]+)$', '^(?P<label>AMBIGUOUS)$'), general_section=('^ARTICLE\\s+(?P<number>\\d+)\\s*-\\s*(?P<title>.*)$', '^(?P<number>AMBIGUOUS)(?P<title>)$'))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `structure_planning_regulation(index, _zones(index), _intersections(index), config)` for its validation or side effect.
- Computes `message` from `str(captured.value)`.

**Action**

- Calls `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`.

**Expected result**

- Direct assertions: `assert 'RECORD-000002' in message`; `assert 'page 1' in message`; `assert 'line 2' in message`; `assert 'ZONE_CHAPTER[1]' in message`; `assert 'GENERAL[1]' in message`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError) as captured: structure_planning_regulation(index, _zones(index), _intersections(index), config)`.

**Regression protected**

- Protects the exact `ambiguous continuation candidate fails with record diagnostic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config_with_structural_patterns`, `_index`, `_intersections`, `_zones`, `pytest.raises`, `str`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_validator_rejects_changed_ambiguous_grammar`

**Signature**

```python
def test_source_complete_validator_rejects_changed_ambiguous_grammar(
    valid_result,
) -> None:
```

**Purpose**

Protects the `source complete validator rejects changed ambiguous grammar` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `config` from `_config(index)`.
- Computes `patterns` from `config.heading_patterns.model_copy(update={'article': (*config.heading_patterns.article, '^ARTICLE\\s+(?P<zone>[A-Z]*)(?P<number>\\d+)\\s*-\\s*(?P<title>.*)$')})`.
- Computes `ambiguous` from `config.model_copy(update={'heading_patterns': patterns})`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='Ambiguous structural heading')` and executes: Calls `validate_planning_regulation_structure(index, _zones(index), _intersections(index), ambiguous, result)` for its validation or side effect.

**Action**

- Calls `_config`, `_intersections`, `_zones`, `config.heading_patterns.model_copy`, `config.model_copy`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='Ambiguous structural heading'): validate_planning_regulation_structure(index, _zones(index), _intersections(index), ambiguous, result)`.

**Regression protected**

- Protects the exact `source complete validator rejects changed ambiguous grammar` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_intersections`, `_zones`, `config.heading_patterns.model_copy`, `config.model_copy`, `pytest.raises`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normal_muret_compatible_grammar_remains_deterministic`

**Signature**

```python
def test_normal_muret_compatible_grammar_remains_deterministic() -> None:
```

**Purpose**

Protects the `normal muret compatible grammar remains deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index)`.
- Computes `first` from `structure_planning_regulation(index, _zones(index), _intersections(index), config)`.
- Computes `second` from `structure_planning_regulation(index, _zones(index), _intersections(index), config)`.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `pd.testing.assert_frame_equal`.

**Expected result**

- Direct assertions: `assert first.structure_result_content_sha256 == second.structure_result_content_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `normal muret compatible grammar remains deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `pd.testing.assert_frame_equal`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_lossless_partition_mutation_is_rejected`

**Signature**

```python
def test_lossless_partition_mutation_is_rejected(
    valid_result,
    mutation: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `lossless partition mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `mutation`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `sections` from `result.sections.copy(deep=True)`.
- Computes `sections.loc[0, mutation]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, replace(result, sections=sections))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`, `result.sections.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, replace(result, sections=sections))`.

**Regression protected**

- Protects the exact `lossless partition mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.sections.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_or_reordered_record_partition_is_rejected`

**Signature**

```python
def test_duplicate_or_reordered_record_partition_is_rejected(valid_result) -> None:
```

**Purpose**

Protects the `duplicate or reordered record partition is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `sections` from `result.sections.copy(deep=True)`.
- Computes `sections.loc[1, 'start_record_id']` from `sections.loc[0, 'start_record_id']`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='partition')` and executes: Calls `_validate(index, replace(result, sections=sections))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`, `result.sections.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='partition'): _validate(index, replace(result, sections=sections))`.

**Regression protected**

- Protects the exact `duplicate or reordered record partition is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.raises`, `replace`, `result.sections.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsorted_section_pages_are_rejected`

**Signature**

```python
def test_unsorted_section_pages_are_rejected(valid_result) -> None:
```

**Purpose**

Protects the `unsorted section pages are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `sections` from `result.sections.copy(deep=True)`.
- Computes `row_index` from `sections.index[sections['page_numbers'].map(len).gt(1)][0]`.
- Computes `sections.at[row_index, 'page_numbers']` from `tuple(reversed(sections.at[row_index, 'page_numbers']))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='page references')` and executes: Calls `_validate(index, replace(result, sections=sections))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`, `result.sections.copy`, `reversed`, `sections['page_numbers'].map`, `sections['page_numbers'].map(len).gt`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='page references'): _validate(index, replace(result, sections=sections))`.

**Regression protected**

- Protects the exact `unsorted section pages are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.raises`, `replace`, `result.sections.copy`, `reversed`, `sections['page_numbers'].map`, `sections['page_numbers'].map(len).gt`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_article_parent_semantics_are_enforced`

**Signature**

```python
def test_article_parent_semantics_are_enforced(valid_result, mutation: str) -> None:
```

**Purpose**

Protects the `article parent semantics are enforced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `mutation`.
- Contains 4 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `sections` from `result.sections.copy(deep=True)`.
- Computes `article_index` from `sections.index[sections['section_type'].eq('ARTICLE')][0]`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, replace(result, sections=sections))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`, `result.sections.copy`, `sections['section_type'].eq`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, replace(result, sections=sections))`.

**Regression protected**

- Protects the exact `article parent semantics are enforced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.sections.copy`, `sections['section_type'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_intersection_source_zone_id_is_rejected`

**Signature**

```python
def test_wrong_intersection_source_zone_id_is_rejected(valid_result) -> None:
```

**Purpose**

Protects the `wrong intersection source zone id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `intersections` from `_intersections(index)`.
- Computes `intersections.loc[0, 'source_zone_id']` from `'WRONG'`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='source-zone')` and executes: Calls `validate_planning_regulation_structure(index, _zones(index), intersections, _config(index), result)` for its validation or side effect.

**Action**

- Calls `_config`, `_intersections`, `_zones`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='source-zone'): validate_planning_regulation_structure(index, _zones(index), intersections, _config(index), result)`.

**Regression protected**

- Protects the exact `wrong intersection source zone id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_intersections`, `_zones`, `pytest.raises`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_intersection_area_cannot_exceed_available_geometry_area`

**Signature**

```python
def test_intersection_area_cannot_exceed_available_geometry_area(
    upper_column: str,
) -> None:
```

**Purpose**

Protects the `intersection area cannot exceed available geometry area` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `upper_column`.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `intersections` from `_intersections(index)`.
- Computes `intersections[upper_column]` from `[99.0, 50.0]`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='exceeds')` and executes: Calls `structure_planning_regulation(index, _zones(index), intersections, _config(index))` for its validation or side effect.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='exceeds'): structure_planning_regulation(index, _zones(index), intersections, _config(index))`.

**Regression protected**

- Protects the exact `intersection area cannot exceed available geometry area` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_intersection_upper_bound_uses_shared_relative_tolerance`

**Signature**

```python
def test_intersection_upper_bound_uses_shared_relative_tolerance(
    upper_column: str,
) -> None:
```

**Purpose**

Protects the `intersection upper bound uses shared relative tolerance` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `upper_column`.
- Contains 11 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index)`.
- Computes `reference_area` from `1000000000000.0`.
- Computes `tolerance` from `technical_overlay_tolerance(reference_area)`.
- Computes `within_tolerance` from `_intersections(index)`.
- Computes `within_tolerance[upper_column]` from `[reference_area, 50.0]`.
- Computes `within_tolerance.loc[0, 'intersection_area_m2']` from `reference_area + tolerance / 2`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), within_tolerance, config)`.
- Computes `above_tolerance` from `within_tolerance.copy(deep=True)`.
- Computes `above_tolerance.loc[0, 'intersection_area_m2']` from `reference_area + tolerance * 2`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='exceeds')` and executes: Calls `structure_planning_regulation(index, _zones(index), above_tolerance, config)` for its validation or side effect.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `technical_overlay_tolerance`, `validate_planning_regulation_structure`, `within_tolerance.copy`.

**Expected result**

- Direct assertions: `assert tolerance > 1e-06`.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='exceeds'): structure_planning_regulation(index, _zones(index), above_tolerance, config)`.

**Regression protected**

- Protects the exact `intersection upper bound uses shared relative tolerance` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `pytest.mark.parametrize`, `pytest.raises`, `structure_planning_regulation`, `technical_overlay_tolerance`, `validate_planning_regulation_structure`, `within_tolerance.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_intersection_hash_columns_are_actual_and_deterministic`

**Signature**

```python
def test_intersection_hash_columns_are_actual_and_deterministic(
    optional_columns: tuple[str, ...],
) -> None:
```

**Purpose**

Protects the `intersection hash columns are actual and deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `optional_columns`.
- Contains 5 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `intersections` from `_intersections(index)`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), intersections, _config(index))`.
- Computes `required` from `('parcel_id', 'planning_zone_id', 'source_zone_id', 'zone_label_raw', 'relation_type', 'intersection_area_m2', 'source_document_id', 'source_archive_sha256')`.
- Computes `expected_optional` from `tuple((column for column in ('parcel_metric_area_m2', 'zone_area_m2') if column in optional_columns))`.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `intersections.insert`, `reversed`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: `assert result.zoning_intersection_hash_columns == required + expected_optional`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `intersection hash columns are actual and deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `intersections.insert`, `pytest.mark.parametrize`, `reversed`, `structure_planning_regulation`, `tuple`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_optional_intersection_metric_change_invalidates_existing_result`

**Signature**

```python
def test_optional_intersection_metric_change_invalidates_existing_result(
    changed_column: str,
) -> None:
```

**Purpose**

Protects the `optional intersection metric change invalidates existing result` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `changed_column`.
- Contains 7 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `intersections` from `_intersections(index)`.
- Computes `intersections['parcel_metric_area_m2']` from `[200.0, 100.0]`.
- Computes `intersections['zone_area_m2']` from `[300.0, 150.0]`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), intersections, _config(index))`.
- Computes `changed` from `intersections.copy(deep=True)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='input hash')` and executes: Calls `validate_planning_regulation_structure(index, _zones(index), changed, _config(index), result)` for its validation or side effect.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `intersections.copy`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='input hash'): validate_planning_regulation_structure(index, _zones(index), changed, _config(index), result)`.

**Regression protected**

- Protects the exact `optional intersection metric change invalidates existing result` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `intersections.copy`, `pytest.mark.parametrize`, `pytest.raises`, `structure_planning_regulation`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_intersection_hash_column_lineage_mutation_is_rejected`

**Signature**

```python
def test_intersection_hash_column_lineage_mutation_is_rejected() -> None:
```

**Purpose**

Protects the `intersection hash column lineage mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `intersections` from `_intersections(index)`.
- Computes `intersections['parcel_metric_area_m2']` from `[200.0, 100.0]`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), intersections, _config(index))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError, match='hash columns')` and executes: Calls `validate_planning_regulation_structure(index, _zones(index), intersections, _config(index), replace(result, zoning_intersection_hash_columns=tuple(reversed(result.zoning_intersection_hash_columns))))` for its validation or side effect.

**Action**

- Calls `_config`, `_index`, `_intersections`, `_zones`, `replace`, `reversed`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError, match='hash columns'): validate_planning_regulation_structure(index, _zones(index), intersections, _config(index), replace(result, zoning_intersection_hash_columns=tuple(reversed(result.zoning_intersection_hash_columns))))`.

**Regression protected**

- Protects the exact `intersection hash column lineage mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_index`, `_intersections`, `_zones`, `pytest.raises`, `replace`, `reversed`, `structure_planning_regulation`, `tuple`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zone_mapping_contract_mutations_are_rejected`

**Signature**

```python
def test_zone_mapping_contract_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `zone mapping contract mutations are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `column`, `value`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `mapping` from `result.zone_mapping.copy(deep=True)`.
- Computes `row_index` from `mapping.index[mapping['source_zone_label_raw'].eq('U')][0]`.
- Computes `mapping.loc[row_index, column]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, replace(result, zone_mapping=mapping))` for its validation or side effect.

**Action**

- Calls `_validate`, `mapping['source_zone_label_raw'].eq`, `replace`, `result.zone_mapping.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, replace(result, zone_mapping=mapping))`.

**Regression protected**

- Protects the exact `zone mapping contract mutations are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `mapping['source_zone_label_raw'].eq`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.zone_mapping.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_alias_chain_resolves_to_final_configured_target`

**Signature**

```python
def test_alias_chain_resolves_to_final_configured_target() -> None:
```

**Purpose**

Protects the `alias chain resolves to final configured target` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `index` from `_index()`.
- Computes `config` from `_config(index).model_copy(update={'zone_aliases': {'Ua': 'Urban', 'Urban': 'U'}})`.
- Computes `result` from `structure_planning_regulation(index, _zones(index), _intersections(index), config)`.
- Computes `mapping` from `result.zone_mapping.set_index('source_zone_label_raw')`.

**Action**

- Calls `_config`, `_config(index).model_copy`, `_index`, `_intersections`, `_zones`, `result.zone_mapping.set_index`.

**Expected result**

- Direct assertions: `assert mapping.at['Ua', 'resolved_zone_chapter_label'] == 'U'`; `assert mapping.at['Ua', 'mapping_status'] == 'CONFIG_ALIAS'`; `assert mapping.at['X', 'mapping_status'] == 'UNMAPPED'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `alias chain resolves to final configured target` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_config(index).model_copy`, `_index`, `_intersections`, `_zones`, `result.zone_mapping.set_index`, `structure_planning_regulation`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_token_boundary_and_longest_match_policy`

**Signature**

```python
def test_token_boundary_and_longest_match_policy() -> None:
```

**Purpose**

Protects the `token boundary and longest match policy` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `raw` from `"risque risques dérisque nuisance nuisances réseau réseaux équipement d'intérêt collectif intérêt collectif incendie défense contre l'incendie"`.
- Computes `normalized` from `normalize_planning_search_text(raw)`.
- Computes `terms` from `('risque', 'risques', 'nuisance', 'nuisances', 'réseau', 'réseaux', "équipement d'intérêt collectif", 'intérêt collectif', 'incendie', "défense contre l'incendie")`.
- Computes `matches` from `_literal_topic_matches(normalized, terms)`.
- Computes `retained` from `[match.search_term for match in matches]`.

**Action**

- Calls `_literal_topic_matches`, `normalize_planning_search_text`, `retained.count`.

**Expected result**

- Direct assertions: `assert retained.count('risque') == 1`; `assert retained.count('risques') == 1`; `assert retained.count('nuisance') == 1`; `assert retained.count('nuisances') == 1`; `assert retained.count('réseau') == 1`; `assert retained.count('réseaux') == 1`; `assert retained.count("équipement d'intérêt collectif") == 1`; `assert retained.count('intérêt collectif') == 1`; `assert retained.count('incendie') == 1`; `assert retained.count("défense contre l'incendie") == 1`; `assert len(matches) == 10`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `token boundary and longest match policy` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_literal_topic_matches`, `len`, `normalize_planning_search_text`, `retained.count`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_topic_evidence_semantic_mutations_are_rejected`

**Signature**

```python
def test_topic_evidence_semantic_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `topic evidence semantic mutations are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `column`, `value`.
- Contains 6 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `evidence` from `result.topic_evidence.copy(deep=True)`.
- Computes `zone_rows` from `evidence.index[evidence['evidence_scope'].eq('ZONE_SPECIFIC_RULE')]`.
- Computes `row_index` from `zone_rows[0] if len(zone_rows) else evidence.index[0]`.
- Computes `evidence.loc[row_index, column]` from `value`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, replace(result, topic_evidence=evidence))` for its validation or side effect.

**Action**

- Calls `_validate`, `evidence['evidence_scope'].eq`, `replace`, `result.topic_evidence.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, replace(result, topic_evidence=evidence))`.

**Regression protected**

- Protects the exact `topic evidence semantic mutations are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `evidence['evidence_scope'].eq`, `len`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.topic_evidence.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected`

**Signature**

```python
def test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected(
    valid_result,
) -> None:
```

**Purpose**

Protects the `coordinated topic evidence and hash mutation is rebuilt and rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `evidence` from `result.topic_evidence.copy(deep=True)`.
- Computes `evidence.loc[0, 'raw_context']` from `'fabricated'`.
- Computes `changed` from `_result_with_hashes(replace(result, topic_evidence=evidence, sections_content_sha256='', zone_map_content_sha256='', topic_evidence_content_sha256='', structure_result_content_sha256=''))`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, changed)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `replace`, `result.topic_evidence.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, changed)`.

**Regression protected**

- Protects the exact `coordinated topic evidence and hash mutation is rebuilt and rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `pytest.raises`, `replace`, `result.topic_evidence.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_validator_rejects_post_build_source_change`

**Signature**

```python
def test_source_complete_validator_rejects_post_build_source_change(
    valid_result,
    source_change: str,
) -> None:
```

**Purpose**

Protects the `source complete validator rejects post build source change` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `source_change`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Computes `zones` from `_zones(index)`.
- Computes `intersections` from `_intersections(index)`.
- Computes `config` from `_config(index)`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `validate_planning_regulation_structure(index, zones, intersections, config, result)` for its validation or side effect.

**Action**

- Calls `_config`, `_intersections`, `_zones`, `config.heading_patterns.model_copy`, `config.model_copy`, `validate_planning_regulation_structure`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): validate_planning_regulation_structure(index, zones, intersections, config, result)`.

**Regression protected**

- Protects the exact `source complete validator rejects post build source change` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_intersections`, `_zones`, `config.heading_patterns.model_copy`, `config.model_copy`, `pytest.mark.parametrize`, `pytest.raises`, `validate_planning_regulation_structure`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_and_result_hash_mutation_is_rejected`

**Signature**

```python
def test_source_and_result_hash_mutation_is_rejected(valid_result, hash_field: str) -> None:
```

**Purpose**

Protects the `source and result hash mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`, `hash_field`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, result)` from `valid_result`.
- Enters managed context(s) `pytest.raises(PlanningRegulationStructureError)` and executes: Calls `_validate(index, replace(result, **{hash_field: 'f' * 64}))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(PlanningRegulationStructureError): _validate(index, replace(result, **{hash_field: 'f' * 64}))`.

**Regression protected**

- Protects the exact `source and result hash mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `U` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UX` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `Ua` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `X` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `Z` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `character_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `continuation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `document_layout` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_candidate_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `extraction_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `general_section` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `heading_patterns` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `heading_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `ignored_patterns` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `include_table_of_contents_in_topic_evidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `mapping_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `occurrence_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `page_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `page_number` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `page_numbers` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parent_section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `raw_context` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `raw_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `resolved_zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `search_term` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `section_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `section_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_record_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `start_record_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `table_of_contents_pages` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `topic` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `topics` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `unexpected` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_aliases` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `zone_chapter` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |

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
