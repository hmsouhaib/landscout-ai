# `tests/unit/test_interpret_bess_zoning.py`

## File identity

- Repository path: `tests/unit/test_interpret_bess_zoning.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `ad1c19efd0af0fca02ac633836edf8f4be194580ba06e389ebde64795335d7a8`

## 1. Purpose

Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from dataclasses import replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import importlib` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.stages.index_planning_regulation import ( INDEX_HASH_SCHEMA_VERSION, PAGE_HASH_SCHEMA_VERSION, SEARCH_NORMALIZATION_PROFILE, PlanningRegulationIndex, _index_content_sha256, _normalize_search_text, _page_content_sha256, _pages_content_sha256, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.interpret_bess_zoning import ( CHAPTER_POLICY_COLUMNS, EVIDENCE_CATALOG_COLUMNS, EVIDENCE_ROUTE_LINK_COLUMNS, PARCEL_ZONE_POLICY_COLUMNS, ROUTE_ASSESSMENT_COLUMNS, SOURCE_ZONE_POLICY_COLUMNS, BessZoningPolicyConfig, BessZoningPrecheckError, _result_with_hashes, interpret_bess_…` — required by the implementation paths and symbols documented below.
- `from landscout.stages.structure_planning_regulation import ( PlanningRegulationStructureConfig, planning_regulation_section_page_fragments, structure_planning_regulation, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.structure_planning_regulation import ( _result_with_hashes as _structure_with_hashes, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_index`

**Signature**

```python
def _index() -> PlanningRegulationIndex:
```

**Purpose**

Implements index according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `PlanningRegulationIndex`. Observed return expression(s): `replace(index, index_content_sha256=_index_content_sha256(index))`.

**Algorithm**

1. Computes `raw_pages` from `('ARTICLE 1 - GENERAL\nGeneral factual text.', 'ZONE U\nARTICLE U 1 - USES\nTechnical equipment is permitted only when formal review is required.\nTechnical equipment is permitted only when formal review is required.', 'ZONE N\nARTICLE N 1 - USES\nBattery facilities are restricted.\nTechnical equipment is permitted on…`.
2. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
3. Iterates `(number, raw_text)` over `enumerate(raw_pages, start=1)`. For each value: Defines `row` with annotation `dict[str, object]` from `{'page_number': number, 'extraction_status': 'TEXT', 'raw_text': raw_text, 'normalized_search_text': _normalize_search_text(raw_text), 'character_count': len(raw_text), 'extraction_error': None, 'page_content_sha256': ''}`. Computes `row['page_content_sha256']` from `_page_content_sha256(row)`. Calls `rows.append(row)` for its validation or side effect.
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

- `tests/unit/test_interpret_bess_zoning.py` — `inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

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

- Declared return type: `pd.DataFrame`. Observed return expression(s): `pd.DataFrame({'planning_zone_id': ['ZONE-U', 'ZONE-UA', 'ZONE-N'], 'source_zone_id': ['SRC-U', 'SRC-UA', 'SRC-N'], 'zone_label_raw': ['U', 'Ua', 'N'], 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256, 'source_layer': 'ZONE'})`.

**Algorithm**

1. Returns `pd.DataFrame({'planning_zone_id': ['ZONE-U', 'ZONE-UA', 'ZONE-N'], 'source_zone_id': ['SRC-U', 'SRC-UA', 'SRC-N'], 'zone_label_raw': ['U', 'Ua', 'N'], 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256, 'source_layer': 'ZONE'})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_relations`

**Signature**

```python
def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
```

**Purpose**

Implements relations according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `pd.DataFrame([{'parcel_id': parcel_id, 'planning_zone_id': planning_zone_id, 'source_zone_id': source_zone_id, 'zone_label_raw': label, 'relation_type': relation_type, 'intersection_area_m2': area, 'parcel_share_pct': share, 'zone_share_pct': area / 10.0, 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256, 'source_layer': 'ZONE', 'parcel_metric_area_m2': 100.0,…`.

**Algorithm**

1. Computes `rows` from `(('P-1', 'ZONE-U', 'SRC-U', 'U', 'AREA_OVERLAP', 100.0, 100.0), ('P-2', 'ZONE-U', 'SRC-U', 'U', 'AREA_OVERLAP', 60.0, 60.0), ('P-2', 'ZONE-UA', 'SRC-UA', 'Ua', 'AREA_OVERLAP', 40.0, 40.0), ('P-3', 'ZONE-U', 'SRC-U', 'U', 'AREA_OVERLAP', 60.0, 60.0), ('P-3', 'ZONE-N', 'SRC-N', 'N', 'AREA_OVERLAP', 40.0, 40.0), ('P-4', …`.
2. Returns `pd.DataFrame([{'parcel_id': parcel_id, 'planning_zone_id': planning_zone_id, 'source_zone_id': source_zone_id, 'zone_label_raw': label, 'relation_type': relation_type, 'intersection_area_m2': area, 'parcel_share_pct': share, 'zone_share_pct': area / 10.0, 'source_document_id': index.document_id, 'source_archive_sha256': index.archive_sha256, 'source_layer':…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_structure_config`

**Signature**

```python
def _structure_config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
```

**Purpose**

Implements structure config according to the exact implementation and guards in this file.

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

- `tests/unit/test_interpret_bess_zoning.py` — `inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_parcels`

**Signature**

```python
def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `frame` from `gpd.GeoDataFrame({'parcel_id': ['P-1', 'P-2', 'P-3', 'P-4'], 'dominant_planning_zone_id': ['ZONE-U', 'ZONE-U', 'ZONE-U', None], 'planning_surface_relation_count': [0, 1, 2, 0], 'prescription_surface_relation_count': [0, 1, 1, 0], 'information_surface_relation_count': [0, 0, 1, 0], 'planning_line_relation_count': [0, 0…`.
2. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `pd.Index`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy`

**Signature**

```python
def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
```

**Purpose**

Implements policy according to the exact implementation and guards in this file.

**Inputs**

- `index` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`unannotated`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`unannotated`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`unannotated`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPolicyConfig`. Observed return expression(s): `BessZoningPolicyConfig.model_validate({'schema_version': 5, 'policy_profile': 'synthetic_policy_v5', 'planning_precheck_scope': 'WRITTEN_ZONING_REGULATION_ONLY', 'review_scope': 'CONFIGURED_USE_CONTROL_ARTICLES_ONLY', 'source_lock': {'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'index_content_sha256': index.index_content_sha256, 'struct…`; `{'evidence_id': evidence_id, 'section_id': section_id, 'page_number': page_number, 'evidence_kind': kind, 'evidence_direction': direction, 'exact_raw_excerpt': excerpt, 'excerpt_sha256': sha256(excerpt.encode()).hexdigest(), 'section_page_fragment_sha256': fragment['section_page_fragment_sha256'], 'excerpt_start': start, 'excerpt_end': start + len(excerpt), 'source_rule_id': source_rule_id, 'sour…`.

**Algorithm**

1. Computes `sections` from `structure.sections`.
2. Computes `u_article` from `sections.loc[sections['section_type'].eq('ARTICLE') & sections['zone_chapter_label'].eq('U')].iloc[0]`.
3. Computes `n_article` from `sections.loc[sections['section_type'].eq('ARTICLE') & sections['zone_chapter_label'].eq('N')].iloc[0]`.
4. Computes `fragments` from `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index(['section_id', 'page_number'])`.
5. Computes `u_positive` from `'Technical equipment is permitted'`.
6. Computes `u_condition` from `'only when formal review is required'`.
7. Computes `n_excerpt` from `'Battery facilities are restricted.'`.
8. Defines the local helper `evidence`; its behavior is documented with the parent function's nested helpers.
9. Returns `BessZoningPolicyConfig.model_validate({'schema_version': 5, 'policy_profile': 'synthetic_policy_v5', 'planning_precheck_scope': 'WRITTEN_ZONING_REGULATION_ONLY', 'review_scope': 'CONFIGURED_USE_CONTROL_ARTICLES_ONLY', 'source_lock': {'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'index_content_sha2…`.

**Meaningful nested/local helpers**

- `evidence` — `def evidence(         evidence_id: str,         section_id: str,         page_number: int,         kind: str,         direction: str,         excerpt: str,         source_rule_id: str,         source_rule: str,         note: str,     ) -> dict[str, object]:`. It executes 5 top-level statement(s), uses `excerpt.encode`, `len`, `raw.index`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `sha256(source_rule.encode()).hexdigest`, `source_rule.encode`, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `evidence`, `excerpt.encode`, `len`, `planning_regulation_section_page_fragments`, `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index`, `raw.index`, `sections['section_type'].eq`, `sections['zone_chapter_label'].eq`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `sha256(source_rule.encode()).hexdigest`, `source_rule.encode`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy.evidence`

**Signature**

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

Implements evidence according to the exact implementation and guards in this file.

**Inputs**

- `evidence_id` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `section_id` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `page_number` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `kind` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `direction` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `excerpt` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_rule_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_rule` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `note` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'evidence_id': evidence_id, 'section_id': section_id, 'page_number': page_number, 'evidence_kind': kind, 'evidence_direction': direction, 'exact_raw_excerpt': excerpt, 'excerpt_sha256': sha256(excerpt.encode()).hexdigest(), 'section_page_fragment_sha256': fragment['section_page_fragment_sha256'], 'excerpt_start': start, 'excerpt_end': start + len(excerpt), 'source_rule_id': source_rule_id, 'sour…`.

**Algorithm**

1. Computes `fragment` from `fragments.loc[section_id, page_number]`.
2. Computes `raw` from `fragment['raw_text']`.
3. Computes `rule_start` from `raw.index(source_rule)`.
4. Computes `start` from `raw.index(excerpt, rule_start, rule_start + len(source_rule))`.
5. Returns `{'evidence_id': evidence_id, 'section_id': section_id, 'page_number': page_number, 'evidence_kind': kind, 'evidence_direction': direction, 'exact_raw_excerpt': excerpt, 'excerpt_sha256': sha256(excerpt.encode()).hexdigest(), 'section_page_fragment_sha256': fragment['section_page_fragment_sha256'], 'excerpt_start': start, 'excerpt_end': start + len(excerpt),…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `excerpt.encode`, `len`, `raw.index`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `sha256(source_rule.encode()).hexdigest`, `source_rule.encode`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `inputs`

**Signature**

```python
def inputs(monkeypatch):
```

**Purpose**

Implements inputs according to the exact implementation and guards in this file.

**Inputs**

- `monkeypatch` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `(index, structure, config, zones, relations, parcels, planning_document, policy)`.

**Algorithm**

1. Calls `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', lambda *args: None)` for its validation or side effect.
2. Computes `index` from `_index()`.
3. Computes `zones` from `_zones(index)`.
4. Computes `relations` from `_relations(index)`.
5. Computes `config` from `_structure_config(index)`.
6. Computes `structure` from `structure_planning_regulation(index, zones, relations, config)`.
7. Computes `parcels` from `_parcels(index)`.
8. Computes `policy` from `_policy(index, structure, config, zones, relations)`.
9. Computes `planning_document` from `object()`.
10. Returns `(index, structure, config, zones, relations, parcels, planning_document, policy)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_index`, `_parcels`, `_policy`, `_relations`, `_structure_config`, `_zones`, `monkeypatch.setattr`, `object`, `structure_planning_regulation`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `valid_result`

**Signature**

```python
def valid_result(inputs):
```

**Purpose**

Implements valid result according to the exact implementation and guards in this file.

**Inputs**

- `inputs` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `interpret_bess_zoning(*inputs)`.

**Algorithm**

1. Returns `interpret_bess_zoning(*inputs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `interpret_bess_zoning`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_payload`

**Signature**

```python
def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
```

**Purpose**

Implements payload according to the exact implementation and guards in this file.

**Inputs**

- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `policy.model_dump(mode='python')`.

**Algorithm**

1. Returns `policy.model_dump(mode='python')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `policy.model_dump`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `_policy_with_context_only_evidence`
- `tests/unit/test_interpret_bess_zoning.py` — `test_absent_excerpt_and_section_page_mismatch_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_condition_alone_cannot_create_conditional_review`
- `tests/unit/test_interpret_bess_zoning.py` — `test_context_only_evidence_must_be_unlinked`
- `tests/unit/test_interpret_bess_zoning.py` — `test_declared_status_must_equal_derived_route_status`
- `tests/unit/test_interpret_bess_zoning.py` — `test_difficulty_and_positive_only_status_routes`
- `tests/unit/test_interpret_bess_zoning.py` — `test_duplicate_chapter_and_evidence_id_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_duplicate_occurrence_in_different_compatible_routes_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_every_evidence_kind_has_an_explicit_direction_matrix`
- `tests/unit/test_interpret_bess_zoning.py` — `test_evidence_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_evidence_must_be_inside_reviewed_sections`
- `tests/unit/test_interpret_bess_zoning.py` — `test_excerpt_hash_and_length_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_forbidden_or_invalid_final_status_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_general_section_review_is_explicit_and_valid`
- `tests/unit/test_interpret_bess_zoning.py` — `test_incomplete_review_persists_exact_missing_required_sections`
- `tests/unit/test_interpret_bess_zoning.py` — `test_incomplete_review_requires_unknown_low`
- `tests/unit/test_interpret_bess_zoning.py` — `test_invalid_confidence_and_unknown_field_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_missing_and_extra_chapter_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_old_policy_schema_versions_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_one_evidence_may_link_to_multiple_compatible_routes`
- `tests/unit/test_interpret_bess_zoning.py` — `test_one_excerpt_cannot_be_reused_with_contradictory_directions`
- `tests/unit/test_interpret_bess_zoning.py` — `test_policy_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_positive_condition_and_conflict_status_routes`
- `tests/unit/test_interpret_bess_zoning.py` — `test_review_cannot_claim_another_chapter_section`
- `tests/unit/test_interpret_bess_zoning.py` — `test_reviewed_sections_cover_required_articles`
- `tests/unit/test_interpret_bess_zoning.py` — `test_route_ids_are_globally_unique`
- `tests/unit/test_interpret_bess_zoning.py` — `test_route_references_must_be_same_chapter_and_role_compatible`
- `tests/unit/test_interpret_bess_zoning.py` — `test_same_general_occurrence_may_be_scoped_to_different_chapters`
- `tests/unit/test_interpret_bess_zoning.py` — `test_same_rule_text_at_distinct_offsets_has_distinct_identity`
- `tests/unit/test_interpret_bess_zoning.py` — `test_source_lock_mismatch_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_source_rule_identity_and_containment_are_strict`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unknown_is_accepted_when_evidence_is_insufficient`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unlinked_context_only_unknown_succeeds`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unlinked_difficulty_evidence_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unlinked_positive_and_condition_evidence_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unrelated_positive_and_condition_do_not_create_conditional_review`
- `tests/unit/test_interpret_bess_zoning.py` — `test_wrong_occurrence_identity_is_rejected`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_absent_excerpt_and_section_page_mismatch_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_condition_alone_cannot_create_conditional_review`
- `tests/unit/test_interpret_bess_zoning.py::test_context_only_evidence_must_be_unlinked`
- `tests/unit/test_interpret_bess_zoning.py::test_declared_status_must_equal_derived_route_status`
- `tests/unit/test_interpret_bess_zoning.py::test_difficulty_and_positive_only_status_routes`
- `tests/unit/test_interpret_bess_zoning.py::test_duplicate_chapter_and_evidence_id_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_duplicate_occurrence_in_different_compatible_routes_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_every_evidence_kind_has_an_explicit_direction_matrix`
- `tests/unit/test_interpret_bess_zoning.py::test_evidence_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_evidence_must_be_inside_reviewed_sections`
- `tests/unit/test_interpret_bess_zoning.py::test_excerpt_hash_and_length_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_forbidden_or_invalid_final_status_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_general_section_review_is_explicit_and_valid`
- `tests/unit/test_interpret_bess_zoning.py::test_incomplete_review_persists_exact_missing_required_sections`
- `tests/unit/test_interpret_bess_zoning.py::test_incomplete_review_requires_unknown_low`
- `tests/unit/test_interpret_bess_zoning.py::test_invalid_confidence_and_unknown_field_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_missing_and_extra_chapter_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_old_policy_schema_versions_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_one_evidence_may_link_to_multiple_compatible_routes`
- `tests/unit/test_interpret_bess_zoning.py::test_one_excerpt_cannot_be_reused_with_contradictory_directions`
- `tests/unit/test_interpret_bess_zoning.py::test_policy_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_positive_condition_and_conflict_status_routes`
- `tests/unit/test_interpret_bess_zoning.py::test_review_cannot_claim_another_chapter_section`
- `tests/unit/test_interpret_bess_zoning.py::test_reviewed_sections_cover_required_articles`
- `tests/unit/test_interpret_bess_zoning.py::test_route_ids_are_globally_unique`
- `tests/unit/test_interpret_bess_zoning.py::test_route_references_must_be_same_chapter_and_role_compatible`
- `tests/unit/test_interpret_bess_zoning.py::test_same_general_occurrence_may_be_scoped_to_different_chapters`
- `tests/unit/test_interpret_bess_zoning.py::test_same_rule_text_at_distinct_offsets_has_distinct_identity`
- `tests/unit/test_interpret_bess_zoning.py::test_source_lock_mismatch_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_source_rule_identity_and_containment_are_strict`
- `tests/unit/test_interpret_bess_zoning.py::test_unknown_is_accepted_when_evidence_is_insufficient`
- `tests/unit/test_interpret_bess_zoning.py::test_unlinked_context_only_unknown_succeeds`
- `tests/unit/test_interpret_bess_zoning.py::test_unlinked_difficulty_evidence_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_unlinked_positive_and_condition_evidence_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_unrelated_positive_and_condition_do_not_create_conditional_review`
- `tests/unit/test_interpret_bess_zoning.py::test_wrong_occurrence_identity_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy_with_context_only_evidence`

**Signature**

```python
def _policy_with_context_only_evidence(
    policy: BessZoningPolicyConfig,
) -> BessZoningPolicyConfig:
```

**Purpose**

Implements policy with context only evidence according to the exact implementation and guards in this file.

**Inputs**

- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPolicyConfig`. Observed return expression(s): `BessZoningPolicyConfig.model_validate(payload)`.

**Algorithm**

1. Computes `payload` from `_payload(policy)`.
2. Computes `chapter` from `payload['chapters'][0]`.
3. Computes `chapter['evidence'][1]['evidence_direction']` from `'CONTEXT_ONLY'`.
4. Computes `route` from `chapter['route_assessments'][0]`.
5. Computes `route['route_kind']` from `'DIRECT_ROUTE'`.
6. Computes `route['condition_evidence_ids']` from `[]`.
7. Computes `chapter['zoning_precheck_status']` from `'POTENTIALLY_COMPATIBLE'`.
8. Returns `BessZoningPolicyConfig.model_validate(payload)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `test_context_evidence_is_separate_from_decision_outputs`
- `tests/unit/test_interpret_bess_zoning.py` — `test_context_only_evidence_must_be_unlinked`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_context_evidence_is_separate_from_decision_outputs`
- `tests/unit/test_interpret_bess_zoning.py::test_context_only_evidence_must_be_unlinked`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_validate`

**Signature**

```python
def _validate(inputs, result) -> None:
```

**Purpose**

Validates and rejects malformed validate according to the exact implementation and guards in this file.

**Inputs**

- `inputs` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `validate_bess_zoning_precheck(*inputs, result)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `validate_bess_zoning_precheck`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_catalog_occurrence_duplicate_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_evidence_catalog_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_evidence_route_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_result_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_reverse_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_route_table_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_evidence_route_link_hash_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_old_result_hash_schemas_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_readback_result_validates`
- `tests/unit/test_interpret_bess_zoning.py` — `test_repeated_excerpt_occurrence_is_bound_to_policy`
- `tests/unit/test_interpret_bess_zoning.py` — `test_valid_locked_policy_builds_complete_outputs`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_catalog_occurrence_duplicate_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_catalog_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_route_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_result_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_reverse_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_route_table_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_evidence_route_link_hash_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_old_result_hash_schemas_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_readback_result_validates`
- `tests/unit/test_interpret_bess_zoning.py::test_repeated_excerpt_occurrence_is_bound_to_policy`
- `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_source_complete_validator_is_invoked.counted`

**Signature**

```python
def counted(*args, **kwargs):
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `original(*args, **kwargs)`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.
3. Returns `original(*args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_precheck_build_performs_one_zoning_source_complete_validation.counted`

**Signature**

```python
def counted(*args) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

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

### `test_invalid_physical_zoning_fails_before_policy_interpretation.invalid_source`

**Signature**

```python
def invalid_source(*args) -> None:
```

**Purpose**

Implements invalid source according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `interpret_module.PlanningZoningError('physical source invalid')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `interpret_module.PlanningZoningError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `interpret_module.PlanningZoningError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_physical_zoning_fails_before_policy_interpretation.counted_policy`

**Signature**

```python
def counted_policy(*args):
```

**Purpose**

Implements counted policy according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `inputs[-1]`.

**Algorithm**

1. Executes `nonlocal policy_calls`.
2. Updates `policy_calls` using `` and `1`.
3. Returns `inputs[-1]`.

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

### `test_one_build_result_performs_one_factual_structure_rebuild.counted`

**Signature**

```python
def counted(*args, **kwargs):
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `original(*args, **kwargs)`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.
3. Returns `original(*args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_package_exports_precheck_api`

**Signature**

```python
def test_package_exports_precheck_api() -> None:
```

**Purpose**

Protects the `package exports precheck api` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls only local assertions/expressions.

**Expected result**

- Direct assertions: `assert name in stages.__all__`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `package exports precheck api` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- No calls.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_locked_policy_builds_complete_outputs`

**Signature**

```python
def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
```

**Purpose**

Protects the `valid locked policy builds complete outputs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, structure, _, zones, relations, parcels, _, policy)` from `inputs`.
- Computes `result` from `valid_result`.

**Action**

- Calls `_validate`, `result.parcels['review_scope'].eq`, `result.parcels['review_scope'].eq(result.review_scope).all`.

**Expected result**

- Direct assertions: `assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS`; `assert tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS`; `assert tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS`; `assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS`; `assert tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS`; `assert len(result.chapter_policy) == 2`; `assert len(result.source_zone_policy) == 3`; `assert len(result.parcel_zone_interpretations) == 5`; `assert len(result.parcels) == len(parcels)`; `assert result.policy_schema_version == 5`; `assert result.result_hash_schema_version == 5`; `assert tuple(result.evidence_catalog.columns) == EVIDENCE_CATALOG_COLUMNS`; `assert result.planning_precheck_scope == 'WRITTEN_ZONING_REGULATION_ONLY'`; `assert result.review_scope == 'CONFIGURED_USE_CONTROL_ARTICLES_ONLY'`; `assert result.parcels['review_scope'].eq(result.review_scope).all()`; `assert len(result.route_assessments) == 2`; `assert len(result.evidence_route_links) == 3`; `assert result.touch_only_relation_count == 1`; `assert result.document_id == index.document_id`; `assert result.structure_result_content_sha256 == structure.structure_result_content_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid locked policy builds complete outputs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `len`, `result.parcels['review_scope'].eq`, `result.parcels['review_scope'].eq(result.review_scope).all`, `set`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_lock_mismatch_is_rejected`

**Signature**

```python
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
```

**Purpose**

Protects the `source lock mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `field`.
- Contains 5 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `payload` from `_payload(policy)`.
- Computes `payload['source_lock'][field]` from `'f' * 64 if 'sha256' in field else 'wrong'`.
- Computes `bad` from `BessZoningPolicyConfig.model_validate(payload)`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from factual source')` and executes: Calls `interpret_bess_zoning(*sources, bad)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from factual source'): interpret_bess_zoning(*sources, bad)`.

**Regression protected**

- Protects the exact `source lock mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_and_extra_chapter_are_rejected`

**Signature**

```python
def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
```

**Purpose**

Protects the `missing and extra chapter are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 12 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `missing_payload` from `_payload(policy)`.
- Computes `missing_payload['chapters']` from `missing_payload['chapters'][:-1]`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='completeness differs')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(missing_payload))` for its validation or side effect.
- Computes `extra_payload` from `_payload(policy)`.
- Computes `extra` from `dict(extra_payload['chapters'][0])`.
- Computes `extra['resolved_zone_chapter_label']` from `'EXTRA'`.
- Computes `extra['evidence']` from `[]`.
- Computes `extra['route_assessments']` from `[]`.
- Computes `extra['zoning_precheck_status']` from `'UNKNOWN'`.
- Computes `extra_payload['chapters']` from `(*extra_payload['chapters'], extra)`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='extra=.*EXTRA')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(extra_payload))` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='completeness differs'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(missing_payload))`; `with pytest.raises(BessZoningPrecheckError, match='extra=.*EXTRA'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(extra_payload))`.

**Regression protected**

- Protects the exact `missing and extra chapter are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `interpret_bess_zoning`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_regulation_zone_chapter_labels_and_ids_must_be_unique`

**Signature**

```python
def test_regulation_zone_chapter_labels_and_ids_must_be_unique(inputs) -> None:
```

**Purpose**

Protects the `regulation zone chapter labels and ids must be unique` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 17 explicit setup/context statement(s).
- Computes `structure` from `inputs[1]`.
- Computes `used` from `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER') & structure.sections['zone_chapter_label'].eq('U')].iloc[0].copy()`.
- Computes `used['section_id']` from `'SECTION-DUPLICATE-U'`.
- Computes `duplicated_used` from `replace(structure, sections=pd.concat([structure.sections, used.to_frame().T], ignore_index=True))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='labels must be unique')` and executes: Calls `interpret_module._zone_chapter_rows(duplicated_used)` for its validation or side effect.
- Computes `unused_one` from `used.copy()`.
- Computes `unused_one['section_id']` from `'SECTION-UNUSED-X-1'`.
- Computes `unused_one['zone_chapter_label']` from `'X'`.
- Computes `unused_two` from `unused_one.copy()`.
- Computes `unused_two['section_id']` from `'SECTION-UNUSED-X-2'`.
- Computes `duplicated_unused` from `replace(structure, sections=pd.concat([structure.sections, unused_one.to_frame().T, unused_two.to_frame().T], ignore_index=True))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='labels must be unique')` and executes: Calls `interpret_module._zone_chapter_rows(duplicated_unused)` for its validation or side effect.

**Action**

- Calls `duplicate_id.to_frame`, `interpret_module._zone_chapter_rows`, `pd.concat`, `replace`, `unused_one.copy`, `unused_one.to_frame`, `unused_two.to_frame`, `used.copy`, `used.to_frame`.

**Expected result**

- Direct assertions: `assert len(interpret_module._zone_chapter_rows(structure)) == 2`.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='labels must be unique'): interpret_module._zone_chapter_rows(duplicated_used)`; `with pytest.raises(BessZoningPrecheckError, match='labels must be unique'): interpret_module._zone_chapter_rows(duplicated_unused)`; `with pytest.raises(BessZoningPrecheckError, match='section IDs must be unique'): interpret_module._zone_chapter_rows(duplicated_section_id)`.

**Regression protected**

- Protects the exact `regulation zone chapter labels and ids must be unique` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `duplicate_id.to_frame`, `interpret_module._zone_chapter_rows`, `len`, `pd.concat`, `pytest.raises`, `replace`, `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER') & structure.sections['zone_chapter_label'].eq('U')].iloc[0].copy`, `structure.sections['section_type'].eq`, `structure.sections['zone_chapter_label'].eq`, `unused_one.copy`, `unused_one.to_frame`, `unused_two.to_frame`, `used.copy`, `used.to_frame`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_validator_rejects_later_duplicate_chapter`

**Signature**

```python
def test_source_complete_validator_rejects_later_duplicate_chapter(
    inputs, valid_result
) -> None:
```

**Purpose**

Protects the `source complete validator rejects later duplicate chapter` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 5 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `duplicate` from `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER')].iloc[0].copy()`.
- Computes `duplicate['section_id']` from `'SECTION-LATE-DUPLICATE'`.
- Computes `changed` from `replace(structure, sections=pd.concat([structure.sections, duplicate.to_frame().T], ignore_index=True))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError)` and executes: Calls `validate_bess_zoning_precheck(index, changed, config, zones, relations, parcels, planning_document, policy, valid_result)` for its validation or side effect.

**Action**

- Calls `duplicate.to_frame`, `pd.concat`, `replace`, `validate_bess_zoning_precheck`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError): validate_bess_zoning_precheck(index, changed, config, zones, relations, parcels, planning_document, policy, valid_result)`.

**Regression protected**

- Protects the exact `source complete validator rejects later duplicate chapter` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `duplicate.to_frame`, `pd.concat`, `pytest.raises`, `replace`, `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER')].iloc[0].copy`, `structure.sections['section_type'].eq`, `validate_bess_zoning_precheck`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_chapter_and_evidence_id_are_rejected`

**Signature**

```python
def test_duplicate_chapter_and_evidence_id_are_rejected(inputs) -> None:
```

**Purpose**

Protects the `duplicate chapter and evidence id are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 7 explicit setup/context statement(s).
- Computes `policy` from `inputs[-1]`.
- Computes `chapter_payload` from `_payload(policy)`.
- Computes `chapter_payload['chapters']` from `(*chapter_payload['chapters'], chapter_payload['chapters'][0])`.
- Enters managed context(s) `pytest.raises(ValueError, match='chapter policy labels must be unique')` and executes: Calls `BessZoningPolicyConfig.model_validate(chapter_payload)` for its validation or side effect.
- Computes `evidence_payload` from `_payload(policy)`.
- Computes `evidence_payload['chapters'][1]['evidence'][0]['evidence_id']` from `'E-U-POSITIVE'`.
- Enters managed context(s) `pytest.raises(ValueError, match='evidence IDs must be globally unique')` and executes: Calls `BessZoningPolicyConfig.model_validate(evidence_payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='chapter policy labels must be unique'): BessZoningPolicyConfig.model_validate(chapter_payload)`; `with pytest.raises(ValueError, match='evidence IDs must be globally unique'): BessZoningPolicyConfig.model_validate(evidence_payload)`.

**Regression protected**

- Protects the exact `duplicate chapter and evidence id are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_excerpt_cannot_be_reused_with_contradictory_directions`

**Signature**

```python
def test_one_excerpt_cannot_be_reused_with_contradictory_directions(inputs) -> None:
```

**Purpose**

Protects the `one excerpt cannot be reused with contradictory directions` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `first` from `dict(payload['chapters'][0]['evidence'][1])`.
- Computes `second` from `dict(first)`.
- Computes `first['evidence_direction']` from `'SUPPORTS_POTENTIAL_COMPATIBILITY'`.
- Computes `second['evidence_id']` from `'E-U-2'`.
- Computes `second['evidence_direction']` from `'SUPPORTS_DIFFICULTY'`.
- Computes `payload['chapters'][0]['evidence']` from `(first, second)`.
- Enters managed context(s) `pytest.raises(ValueError, match='chapter-scoped evidence occurrence')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='chapter-scoped evidence occurrence'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `one excerpt cannot be reused with contradictory directions` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected`

**Signature**

```python
def test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected(inputs) -> None:
```

**Purpose**

Protects the `duplicate chapter scoped occurrence in one route is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `duplicate` from `dict(payload['chapters'][0]['evidence'][0])`.
- Computes `duplicate['evidence_id']` from `'E-U-POSITIVE-DUPLICATE'`.
- Computes `payload['chapters'][0]['evidence']` from `(*payload['chapters'][0]['evidence'], duplicate)`.
- Computes `payload['chapters'][0]['route_assessments'][0]['positive_evidence_ids']` from `['E-U-POSITIVE', 'E-U-POSITIVE-DUPLICATE']`.
- Enters managed context(s) `pytest.raises(ValueError, match='chapter-scoped evidence occurrence')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='chapter-scoped evidence occurrence'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `duplicate chapter scoped occurrence in one route is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_occurrence_in_different_compatible_routes_is_rejected`

**Signature**

```python
def test_duplicate_occurrence_in_different_compatible_routes_is_rejected(
    inputs,
) -> None:
```

**Purpose**

Protects the `duplicate occurrence in different compatible routes is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `duplicate` from `dict(payload['chapters'][1]['evidence'][0])`.
- Computes `duplicate['evidence_id']` from `'E-N-DUPLICATE-ROUTE'`.
- Computes `payload['chapters'][1]['evidence']` from `(*payload['chapters'][1]['evidence'], duplicate)`.
- Computes `payload['chapters'][1]['route_assessments']` from `(*payload['chapters'][1]['route_assessments'], {'route_id': 'ROUTE-N-DUPLICATE-OCCURRENCE', 'route_kind': 'DIFFICULTY_ONLY', 'positive_evidence_ids': [], 'condition_evidence_ids': [], 'difficulty_evidence_ids': ['E-N-DUPLICATE-ROUTE'], 'applicability_note': 'A second route must not duplicate the occurrence.'})`.
- Enters managed context(s) `pytest.raises(ValueError, match='chapter-scoped evidence occurrence')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='chapter-scoped evidence occurrence'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `duplicate occurrence in different compatible routes is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_forbidden_or_invalid_final_status_is_rejected`

**Signature**

```python
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
```

**Purpose**

Protects the `forbidden or invalid final status is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `status`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['chapters'][0]['zoning_precheck_status']` from `status`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `forbidden or invalid final status is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_confidence_and_unknown_field_are_rejected`

**Signature**

```python
def test_invalid_confidence_and_unknown_field_are_rejected(inputs) -> None:
```

**Purpose**

Protects the `invalid confidence and unknown field are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['chapters'][0]['zoning_precheck_confidence']` from `'CERTAIN'`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['automatic_classifier']` from `True`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError): BessZoningPolicyConfig.model_validate(payload)`; `with pytest.raises(ValueError): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `invalid confidence and unknown field are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_yaml_key_is_rejected`

**Signature**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate yaml key is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'duplicate.yaml'`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='Duplicate YAML policy key')` and executes: Calls `load_bess_zoning_policy_config(path)` for its validation or side effect.

**Action**

- Calls `load_bess_zoning_policy_config`, `path.write_text`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='Duplicate YAML policy key'): load_bess_zoning_policy_config(path)`.

**Regression protected**

- Protects the exact `duplicate yaml key is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_bess_zoning_policy_config`, `path.write_text`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_old_policy_schema_versions_are_rejected`

**Signature**

```python
def test_old_policy_schema_versions_are_rejected(inputs, version: int) -> None:
```

**Purpose**

Protects the `old policy schema versions are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `version`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['schema_version']` from `version`.
- Enters managed context(s) `pytest.raises(ValueError, match='unsupported BESS zoning policy schema')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='unsupported BESS zoning policy schema'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `old policy schema versions are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_evidence_kind_has_an_explicit_direction_matrix`

**Signature**

```python
def test_every_evidence_kind_has_an_explicit_direction_matrix(inputs) -> None:
```

**Purpose**

Protects the `every evidence kind has an explicit direction matrix` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 3 explicit setup/context statement(s).
- Computes `allowed` from `{'USE_PERMISSION': {'SUPPORTS_POTENTIAL_COMPATIBILITY', 'CONTEXT_ONLY'}, 'USE_RESTRICTION': {'SUPPORTS_DIFFICULTY', 'CONTEXT_ONLY'}, 'PUBLIC_INTEREST_EXCEPTION': {'SUPPORTS_POTENTIAL_COMPATIBILITY', 'CONDITION', 'CONTEXT_ONLY'}, 'TECHNICAL_EQUIPMENT_RULE': {'SUPPORTS_POTENTIAL_COMPATIBILITY', 'SUPPORTS_DIFFICULTY', 'C…`.
- Computes `directions` from `{'SUPPORTS_POTENTIAL_COMPATIBILITY', 'SUPPORTS_DIFFICULTY', 'CONDITION', 'CONTEXT_ONLY'}`.
- Computes `base` from `_payload(inputs[-1])['chapters'][0]['evidence'][0]`.

**Action**

- Calls `_payload`, `allowed.items`, `interpret_module.PolicyEvidence.model_validate`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='kind and direction are incompatible'): interpret_module.PolicyEvidence.model_validate(evidence)`.

**Regression protected**

- Protects the exact `every evidence kind has an explicit direction matrix` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_payload`, `allowed.items`, `dict`, `interpret_module.PolicyEvidence.model_validate`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_exact_evidence_is_preserved`

**Signature**

```python
def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
```

**Purpose**

Protects the `valid exact evidence is preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 5 explicit setup/context statement(s).
- Computes `policy` from `inputs[-1]`.
- Computes `excerpt` from `policy.chapters[0].evidence[0].exact_raw_excerpt`.
- Computes `row` from `valid_result.evidence_catalog.set_index('evidence_id').loc['E-U-POSITIVE']`.
- Computes `relative_start` from `row['excerpt_start'] - row['source_rule_start']`.
- Computes `relative_end` from `row['excerpt_end'] - row['source_rule_start']`.

**Action**

- Calls `excerpt.encode`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `valid_result.evidence_catalog.set_index`.

**Expected result**

- Direct assertions: `assert excerpt == 'Technical equipment is permitted'`; `assert policy.chapters[0].evidence[0].excerpt_sha256 == sha256(excerpt.encode()).hexdigest()`; `assert valid_result.chapter_policy.iloc[0]['evidence_ids'] == ('E-U-POSITIVE', 'E-U-CONDITION')`; `assert 'only when' in row['source_rule_excerpt']`; `assert row['source_rule_excerpt'][relative_start:relative_end] == excerpt`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid exact evidence is preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `excerpt.encode`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `valid_result.evidence_catalog.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_rule_identity_and_containment_are_strict`

**Signature**

```python
def test_source_rule_identity_and_containment_are_strict(inputs, mutation: str) -> None:
```

**Purpose**

Protects the `source rule identity and containment are strict` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `mutation`.
- Contains 4 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `payload` from `_payload(policy)`.
- Computes `evidence` from `payload['chapters'][0]['evidence'][0]`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='source-rule offsets')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='source-rule offsets'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`; `with pytest.raises(ValueError, match='source rule SHA256'): BessZoningPolicyConfig.model_validate(payload)`; `with pytest.raises(ValueError, match='inside its source rule'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `source rule identity and containment are strict` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_same_rule_text_at_distinct_offsets_has_distinct_identity`

**Signature**

```python
def test_same_rule_text_at_distinct_offsets_has_distinct_identity(inputs) -> None:
```

**Purpose**

Protects the `same rule text at distinct offsets has distinct identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 17 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `chapter` from `payload['chapters'][0]`.
- Computes `first` from `chapter['evidence'][0]`.
- Computes `second` from `dict(first)`.
- Computes `rule_length` from `len(first['source_rule_excerpt'])`.
- Computes `second_rule_start` from `first['source_rule_end'] + 1`.
- Computes `second['evidence_id']` from `'E-U-SECOND-OCCURRENCE'`.
- Computes `second['evidence_kind']` from `'TECHNICAL_EQUIPMENT_RULE'`.
- Computes `second['evidence_direction']` from `'SUPPORTS_DIFFICULTY'`.
- Computes `second['source_rule_id']` from `'RULE-U-SECOND-OCCURRENCE'`.
- Computes `second['source_rule_start']` from `second_rule_start`.
- Computes `second['source_rule_end']` from `second_rule_start + rule_length`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: `assert policy.chapters[0].evidence[-1].evidence_direction == 'SUPPORTS_DIFFICULTY'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `same rule text at distinct offsets has distinct identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_real_muret_source_rules_preserve_conditional_and_exception_frames`

**Signature**

```python
def test_real_muret_source_rules_preserve_conditional_and_exception_frames() -> None:
```

**Purpose**

Protects the `real muret source rules preserve conditional and exception frames` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `load_bess_zoning_policy_config(Path('configs/planning/muret_bess_zoning_policy.yaml'))`.
- Computes `by_label` from `{chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters}`.

**Action**

- Calls `Path`, `load_bess_zoning_policy_config`, `next`, `positive.source_rule_excerpt.startswith`.

**Expected result**

- Direct assertions: `assert 'ne sont autorisées qu’à' in positive.source_rule_excerpt`; `assert 'condition' in positive.source_rule_excerpt`; `assert positive.source_rule_excerpt.startswith('Toutes constructions')`; `assert 'autres que celles' in positive.source_rule_excerpt`; `assert positive.source_rule_excerpt.startswith('Sont interdites')`; `assert difficulty.source_rule_id == positive.source_rule_id`; `assert difficulty.source_rule_excerpt == positive.source_rule_excerpt`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `real muret source rules preserve conditional and exception frames` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `load_bess_zoning_policy_config`, `next`, `positive.source_rule_excerpt.startswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_real_muret_up_route_does_not_use_the_separate_icpe_condition`

**Signature**

```python
def test_real_muret_up_route_does_not_use_the_separate_icpe_condition() -> None:
```

**Purpose**

Protects the `real muret up route does not use the separate icpe condition` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `policy` from `load_bess_zoning_policy_config(Path('configs/planning/muret_bess_zoning_policy.yaml'))`.
- Computes `chapter` from `next((item for item in policy.chapters if item.resolved_zone_chapter_label == 'UP'))`.
- Computes `route` from `chapter.route_assessments[0]`.
- Computes `restriction` from `next((evidence for evidence in chapter.evidence if evidence.evidence_id == 'MURET-UP-RESTRICTION-01'))`.

**Action**

- Calls `Path`, `load_bess_zoning_policy_config`, `next`.

**Expected result**

- Direct assertions: `assert policy.schema_version == 5`; `assert policy.policy_profile == 'muret_bess_written_zoning_v6'`; `assert route.route_kind == 'RESTRICTION_EXCEPTION_ROUTE'`; `assert route.positive_evidence_ids == ('MURET-UP-PUBLIC-ROUTE-01',)`; `assert route.condition_evidence_ids == ()`; `assert route.difficulty_evidence_ids == ('MURET-UP-RESTRICTION-01',)`; `assert restriction.evidence_kind == 'USE_RESTRICTION'`; `assert restriction.evidence_direction == 'SUPPORTS_DIFFICULTY'`; `assert restriction.section_id == 'SECTION-0080'`; `assert restriction.page_number == 71`; `assert restriction.exact_raw_excerpt == 'Toutes constructions ou installations autres que celles'`; `assert restriction.excerpt_start == 68`; `assert restriction.excerpt_end == 124`; `assert restriction.excerpt_sha256 == 'edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462'`; `assert restriction.section_page_fragment_sha256 == '06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb'`; `assert restriction.source_rule_id == 'MURET-UP-ROUTE-RULE-01'`; `assert restriction.source_rule_start == 68`; `assert restriction.source_rule_end == 236`; `assert restriction.source_rule_sha256 == 'de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `real muret up route does not use the separate icpe condition` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `load_bess_zoning_policy_config`, `next`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite`

**Signature**

```python
def test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite() -> None:
```

**Purpose**

Protects the `real muret aup route uses the general infrastructure prerequisite` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `policy` from `load_bess_zoning_policy_config(Path('configs/planning/muret_bess_zoning_policy.yaml'))`.
- Computes `chapter` from `next((item for item in policy.chapters if item.resolved_zone_chapter_label == 'AUp'))`.
- Computes `route` from `chapter.route_assessments[0]`.
- Computes `prerequisite` from `next((evidence for evidence in chapter.evidence if evidence.evidence_id == 'MURET-AUP-INFRASTRUCTURE-CONDITION-01'))`.
- Computes `exact_rule` from `'Les constructions et opérations ne pourront être autorisées qu’après réalisation des \néquipements d’infrastructure indispensable à leur fonctionnement (accès, voirie et \nréseaux divers) conformément aux articles AUp3 et AUp4.'`.

**Action**

- Calls `Path`, `load_bess_zoning_policy_config`, `next`.

**Expected result**

- Direct assertions: `assert route.route_kind == 'CONDITIONAL_ROUTE'`; `assert route.positive_evidence_ids == ('MURET-AUP-PUBLIC-ROUTE-01',)`; `assert route.condition_evidence_ids == ('MURET-AUP-INFRASTRUCTURE-CONDITION-01',)`; `assert route.difficulty_evidence_ids == ()`; `assert prerequisite.evidence_kind == 'ACCESS_OR_NETWORK_CONDITION'`; `assert prerequisite.evidence_direction == 'CONDITION'`; `assert prerequisite.section_id == 'SECTION-0111'`; `assert prerequisite.page_number == 93`; `assert prerequisite.exact_raw_excerpt == exact_rule`; `assert prerequisite.excerpt_start == 98`; `assert prerequisite.excerpt_end == 325`; `assert prerequisite.excerpt_sha256 == 'b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b'`; `assert prerequisite.section_page_fragment_sha256 == '57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44'`; `assert prerequisite.source_rule_id == 'MURET-AUp-INFRASTRUCTURE-RULE-01'`; `assert prerequisite.source_rule_excerpt == exact_rule`; `assert prerequisite.source_rule_start == 98`; `assert prerequisite.source_rule_end == 325`; `assert prerequisite.source_rule_sha256 == prerequisite.excerpt_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `real muret aup route uses the general infrastructure prerequisite` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `load_bess_zoning_policy_config`, `next`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_real_muret_up_and_aup_keep_icpe_applicability_as_context`

**Signature**

```python
def test_real_muret_up_and_aup_keep_icpe_applicability_as_context() -> None:
```

**Purpose**

Protects the `real muret up and aup keep icpe applicability as context` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `policy` from `load_bess_zoning_policy_config(Path('configs/planning/muret_bess_zoning_policy.yaml'))`.
- Computes `chapters` from `{chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters}`.
- Computes `identities` from `{'UP': 'MURET-UP-ICPE-CONDITION-01', 'AUp': 'MURET-AUP-ICPE-CONDITION-01'}`.

**Action**

- Calls `Path`, `identities.items`, `load_bess_zoning_policy_config`, `next`.

**Expected result**

- Direct assertions: `assert evidence.evidence_kind == 'ICPE_RULE'`; `assert evidence.evidence_direction == 'CONTEXT_ONLY'`; `assert 'ICPE' in chapter.missing_information`; `assert evidence_id not in linked_ids`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `real muret up and aup keep icpe applicability as context` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `identities.items`, `load_bess_zoning_policy_config`, `next`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_absent_excerpt_and_section_page_mismatch_are_rejected`

**Signature**

```python
def test_absent_excerpt_and_section_page_mismatch_are_rejected(inputs) -> None:
```

**Purpose**

Protects the `absent excerpt and section page mismatch are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `payload` from `_payload(policy)`.
- Computes `excerpt` from `'Not present in the indexed source.'`.
- Computes `payload['chapters'][0]['evidence'][0]['exact_raw_excerpt']` from `excerpt`.
- Computes `payload['chapters'][0]['evidence'][0]['excerpt_sha256']` from `sha256(excerpt.encode()).hexdigest()`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='offsets')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))` for its validation or side effect.
- Computes `payload` from `_payload(policy)`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='section/page fragment')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `interpret_bess_zoning`, `sha256`, `sha256(excerpt.encode()).hexdigest`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='offsets'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`; `with pytest.raises(BessZoningPrecheckError, match='section/page fragment'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.

**Regression protected**

- Protects the exact `absent excerpt and section page mismatch are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `interpret_bess_zoning`, `pytest.raises`, `sha256`, `sha256(excerpt.encode()).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_excerpt_hash_and_length_are_rejected`

**Signature**

```python
def test_excerpt_hash_and_length_are_rejected(inputs) -> None:
```

**Purpose**

Protects the `excerpt hash and length are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['chapters'][0]['evidence'][0]['excerpt_sha256']` from `'f' * 64`.
- Enters managed context(s) `pytest.raises(ValueError, match='excerpt SHA256 differs')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `excerpt` from `'x' * 601`.
- Computes `payload['chapters'][0]['evidence'][0]['exact_raw_excerpt']` from `excerpt`.
- Computes `payload['chapters'][0]['evidence'][0]['excerpt_sha256']` from `sha256(excerpt.encode()).hexdigest()`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `sha256`, `sha256(excerpt.encode()).hexdigest`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='excerpt SHA256 differs'): BessZoningPolicyConfig.model_validate(payload)`; `with pytest.raises(ValueError): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `excerpt hash and length are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `pytest.raises`, `sha256`, `sha256(excerpt.encode()).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_declared_status_must_equal_derived_route_status`

**Signature**

```python
def test_declared_status_must_equal_derived_route_status(inputs, status: str) -> None:
```

**Purpose**

Protects the `declared status must equal derived route status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `status`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['chapters'][0]['zoning_precheck_status']` from `status`.
- Enters managed context(s) `pytest.raises(ValueError, match='differs from coherent linked route')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='differs from coherent linked route'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `declared status must equal derived route status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_condition_alone_cannot_create_conditional_review`

**Signature**

```python
def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
```

**Purpose**

Protects the `condition alone cannot create conditional review` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 5 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['chapters'][0]['zoning_precheck_status']` from `'CONDITIONAL_REVIEW'`.
- Computes `payload['chapters'][0]['evidence']` from `[payload['chapters'][0]['evidence'][1]]`.
- Computes `payload['chapters'][0]['route_assessments']` from `[]`.
- Enters managed context(s) `pytest.raises(ValueError, match='coherent linked route')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='coherent linked route'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `condition alone cannot create conditional review` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unrelated_positive_and_condition_do_not_create_conditional_review`

**Signature**

```python
def test_unrelated_positive_and_condition_do_not_create_conditional_review(
    inputs,
) -> None:
```

**Purpose**

Protects the `unrelated positive and condition do not create conditional review` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 5 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `chapter` from `payload['chapters'][0]`.
- Computes `chapter['zoning_precheck_status']` from `'CONDITIONAL_REVIEW'`.
- Computes `chapter['route_assessments']` from `[{'route_id': 'ROUTE-U-DIRECT-ONLY', 'route_kind': 'DIRECT_ROUTE', 'positive_evidence_ids': ['E-U-POSITIVE'], 'condition_evidence_ids': [], 'difficulty_evidence_ids': [], 'applicability_note': 'The separate condition is deliberately unlinked.'}]`.
- Enters managed context(s) `pytest.raises(ValueError, match='coherent|linked route')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='coherent|linked route'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `unrelated positive and condition do not create conditional review` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unlinked_context_only_unknown_succeeds`

**Signature**

```python
def test_unlinked_context_only_unknown_succeeds(inputs) -> None:
```

**Purpose**

Protects the `unlinked context only unknown succeeds` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `chapter` from `payload['chapters'][0]`.
- Computes `chapter['zoning_precheck_status']` from `'UNKNOWN'`.
- Computes `chapter['zoning_precheck_confidence']` from `'LOW'`.
- Computes `chapter['evidence']` from `[chapter['evidence'][1]]`.
- Computes `chapter['evidence'][0]['evidence_direction']` from `'CONTEXT_ONLY'`.
- Computes `chapter['route_assessments']` from `[]`.
- Computes `policy` from `BessZoningPolicyConfig.model_validate(payload)`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: `assert policy.chapters[0].zoning_precheck_status == 'UNKNOWN'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unlinked context only unknown succeeds` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_positive_condition_and_conflict_status_routes`

**Signature**

```python
def test_positive_condition_and_conflict_status_routes(inputs) -> None:
```

**Purpose**

Protects the `positive condition and conflict status routes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `conflict` from `_payload(inputs[-1])`.
- Computes `conflict['chapters'][0]['evidence'][1]['evidence_direction']` from `'SUPPORTS_DIFFICULTY'`.
- Computes `route` from `conflict['chapters'][0]['route_assessments'][0]`.
- Computes `route['route_kind']` from `'RESTRICTION_EXCEPTION_ROUTE'`.
- Computes `route['condition_evidence_ids']` from `[]`.
- Computes `route['difficulty_evidence_ids']` from `['E-U-CONDITION']`.
- Computes `policy` from `BessZoningPolicyConfig.model_validate(conflict)`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: `assert BessZoningPolicyConfig.model_validate(payload).chapters[0].zoning_precheck_status == 'CONDITIONAL_REVIEW'`; `assert policy.chapters[0].zoning_precheck_status == 'CONDITIONAL_REVIEW'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `positive condition and conflict status routes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_route_references_must_be_same_chapter_and_role_compatible`

**Signature**

```python
def test_route_references_must_be_same_chapter_and_role_compatible(inputs) -> None:
```

**Purpose**

Protects the `route references must be same chapter and role compatible` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match=message): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `route references must be same chapter and role compatible` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_route_ids_are_globally_unique`

**Signature**

```python
def test_route_ids_are_globally_unique(inputs) -> None:
```

**Purpose**

Protects the `route ids are globally unique` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['chapters'][1]['route_assessments'][0]['route_id']` from `payload['chapters'][0]['route_assessments'][0]['route_id']`.
- Enters managed context(s) `pytest.raises(ValueError, match='route IDs must be globally unique')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='route IDs must be globally unique'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `route ids are globally unique` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unlinked_difficulty_evidence_is_rejected`

**Signature**

```python
def test_unlinked_difficulty_evidence_is_rejected(inputs) -> None:
```

**Purpose**

Protects the `unlinked difficulty evidence is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `unlinked` from `dict(payload['chapters'][1]['evidence'][0])`.
- Computes `unlinked['evidence_id']` from `'E-N-UNLINKED'`.
- Computes `unlinked['source_rule_id']` from `'RULE-N-UNLINKED'`.
- Computes `payload['chapters'][1]['evidence']` from `(*payload['chapters'][1]['evidence'], unlinked)`.
- Enters managed context(s) `pytest.raises(ValueError, match='decision evidence must be linked')` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='decision evidence must be linked'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `unlinked difficulty evidence is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unlinked_positive_and_condition_evidence_are_rejected`

**Signature**

```python
def test_unlinked_positive_and_condition_evidence_are_rejected(inputs) -> None:
```

**Purpose**

Protects the `unlinked positive and condition evidence are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='decision evidence must be linked'): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `unlinked positive and condition evidence are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_context_only_evidence_must_be_unlinked`

**Signature**

```python
def test_context_only_evidence_must_be_unlinked(inputs) -> None:
```

**Purpose**

Protects the `context only evidence must be unlinked` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `policy` from `_policy_with_context_only_evidence(inputs[-1])`.
- Computes `payload` from `_payload(policy)`.
- Computes `payload['chapters'][0]['route_assessments'][0]['condition_evidence_ids']` from `['E-U-CONDITION']`.
- Computes `payload['chapters'][0]['route_assessments'][0]['route_kind']` from `'CONDITIONAL_ROUTE'`.
- Computes `payload['chapters'][0]['zoning_precheck_status']` from `'CONDITIONAL_REVIEW'`.
- Enters managed context(s) `pytest.raises(ValueError)` and executes: Calls `BessZoningPolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `_policy_with_context_only_evidence`.

**Expected result**

- Direct assertions: `assert policy.chapters[0].evidence[1].evidence_direction == 'CONTEXT_ONLY'`.
- Expected exception contexts: `with pytest.raises(ValueError): BessZoningPolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `context only evidence must be unlinked` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `_policy_with_context_only_evidence`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_evidence_may_link_to_multiple_compatible_routes`

**Signature**

```python
def test_one_evidence_may_link_to_multiple_compatible_routes(inputs) -> None:
```

**Purpose**

Protects the `one evidence may link to multiple compatible routes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `route` from `dict(payload['chapters'][1]['route_assessments'][0])`.
- Computes `route['route_id']` from `'ROUTE-N-DIFFICULT-SECOND'`.
- Computes `payload['chapters'][1]['route_assessments']` from `(*payload['chapters'][1]['route_assessments'], route)`.
- Computes `policy` from `BessZoningPolicyConfig.model_validate(payload)`.
- Computes `(*sources, _)` from `inputs`.
- Computes `result` from `interpret_bess_zoning(*sources, policy)`.
- Computes `evidence` from `result.evidence_catalog.set_index('evidence_id').loc['E-N-1']`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `result.evidence_catalog.set_index`.

**Expected result**

- Direct assertions: `assert evidence['linked_route_ids'] == ('ROUTE-N-DIFFICULT', 'ROUTE-N-DIFFICULT-SECOND')`; `assert evidence['linked_route_roles'] == ('DIFFICULTY', 'DIFFICULTY')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `one evidence may link to multiple compatible routes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `dict`, `interpret_bess_zoning`, `result.evidence_catalog.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_difficulty_and_positive_only_status_routes`

**Signature**

```python
def test_difficulty_and_positive_only_status_routes(inputs) -> None:
```

**Purpose**

Protects the `difficulty and positive only status routes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 11 explicit setup/context statement(s).
- Computes `difficult` from `_payload(inputs[-1])`.
- Computes `chapter` from `difficult['chapters'][0]`.
- Computes `chapter['zoning_precheck_status']` from `'LIKELY_DIFFICULT'`.
- Computes `chapter['evidence']` from `[chapter['evidence'][1]]`.
- Computes `chapter['evidence'][0]['evidence_direction']` from `'SUPPORTS_DIFFICULTY'`.
- Computes `chapter['route_assessments']` from `[{'route_id': 'ROUTE-U-DIFFICULT', 'route_kind': 'DIFFICULTY_ONLY', 'positive_evidence_ids': [], 'condition_evidence_ids': [], 'difficulty_evidence_ids': ['E-U-CONDITION'], 'applicability_note': 'Only the linked difficulty is assessed.'}]`.
- Computes `potential` from `_payload(inputs[-1])`.
- Computes `chapter` from `potential['chapters'][0]`.
- Computes `chapter['zoning_precheck_status']` from `'POTENTIALLY_COMPATIBLE'`.
- Computes `chapter['evidence']` from `[chapter['evidence'][0]]`.
- Computes `chapter['route_assessments']` from `[{'route_id': 'ROUTE-U-DIRECT', 'route_kind': 'DIRECT_ROUTE', 'positive_evidence_ids': ['E-U-POSITIVE'], 'condition_evidence_ids': [], 'difficulty_evidence_ids': [], 'applicability_note': 'Only the direct linked route is assessed.'}]`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: `assert BessZoningPolicyConfig.model_validate(difficult).chapters[0].zoning_precheck_status == 'LIKELY_DIFFICULT'`; `assert BessZoningPolicyConfig.model_validate(potential).chapters[0].zoning_precheck_status == 'POTENTIALLY_COMPATIBLE'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `difficulty and positive only status routes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_incomplete_review_requires_unknown_low`

**Signature**

```python
def test_incomplete_review_requires_unknown_low(inputs) -> None:
```

**Purpose**

Protects the `incomplete review requires unknown low` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `chapter` from `payload['chapters'][0]`.
- Computes `chapter['review_completeness']` from `'INCOMPLETE'`.
- Computes `chapter['zoning_precheck_status']` from `'UNKNOWN'`.
- Computes `chapter['zoning_precheck_confidence']` from `'LOW'`.
- Computes `chapter['evidence']` from `[]`.
- Computes `chapter['route_assessments']` from `[]`.
- Computes `chapter['reviewed_section_ids']` from `[]`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`.

**Expected result**

- Direct assertions: `assert BessZoningPolicyConfig.model_validate(payload).chapters[0].review_completeness == 'INCOMPLETE'`.
- Expected exception contexts: `with pytest.raises(ValueError, match='incomplete review'): BessZoningPolicyConfig.model_validate(invalid)`.

**Regression protected**

- Protects the exact `incomplete review requires unknown low` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_incomplete_review_persists_exact_missing_required_sections`

**Signature**

```python
def test_incomplete_review_persists_exact_missing_required_sections(inputs) -> None:
```

**Purpose**

Protects the `incomplete review persists exact missing required sections` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 11 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `payload` from `_payload(policy)`.
- Computes `chapter` from `payload['chapters'][0]`.
- Computes `chapter['review_completeness']` from `'INCOMPLETE'`.
- Computes `chapter['reviewed_section_ids']` from `[]`.
- Computes `chapter['zoning_precheck_status']` from `'UNKNOWN'`.
- Computes `chapter['zoning_precheck_confidence']` from `'LOW'`.
- Computes `chapter['evidence']` from `[]`.
- Computes `chapter['route_assessments']` from `[]`.
- Computes `result` from `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.
- Computes `row` from `result.chapter_policy.set_index('resolved_zone_chapter_label').loc['U']`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `result.chapter_policy.set_index`.

**Expected result**

- Direct assertions: `assert row['reviewed_section_ids'] == ()`; `assert row['missing_required_section_ids'] == ('SECTION-0003',)`; `assert row['zoning_precheck_status'] == 'UNKNOWN'`; `assert row['zoning_precheck_confidence'] == 'LOW'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `incomplete review persists exact missing required sections` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `result.chapter_policy.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_is_accepted_when_evidence_is_insufficient`

**Signature**

```python
def test_unknown_is_accepted_when_evidence_is_insufficient(inputs) -> None:
```

**Purpose**

Protects the `unknown is accepted when evidence is insufficient` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `payload` from `_payload(policy)`.
- Computes `payload['chapters'][0]['zoning_precheck_status']` from `'UNKNOWN'`.
- Computes `payload['chapters'][0]['evidence']` from `[]`.
- Computes `payload['chapters'][0]['route_assessments']` from `[]`.
- Computes `result` from `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: `assert result.chapter_policy.iloc[0]['zoning_precheck_status'] == 'UNKNOWN'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unknown is accepted when evidence is insufficient` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_reviewed_sections_cover_required_articles`

**Signature**

```python
def test_reviewed_sections_cover_required_articles(inputs) -> None:
```

**Purpose**

Protects the `reviewed sections cover required articles` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `(index, structure)` from `inputs[:2]`.
- Computes `payload` from `_payload(policy)`.
- Computes `chapter_id` from `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER') & structure.sections['zone_chapter_label'].eq('U'), 'section_id'].iloc[0]`.
- Computes `payload['chapters'][0]['reviewed_section_ids']` from `[chapter_id]`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='omits required reviewed')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: `assert index.document_id == 'doc-1'`.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='omits required reviewed'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.

**Regression protected**

- Protects the exact `reviewed sections cover required articles` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `pytest.raises`, `structure.sections['section_type'].eq`, `structure.sections['zone_chapter_label'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_evidence_must_be_inside_reviewed_sections`

**Signature**

```python
def test_evidence_must_be_inside_reviewed_sections(inputs) -> None:
```

**Purpose**

Protects the `evidence must be inside reviewed sections` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 7 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `structure` from `inputs[1]`.
- Computes `payload` from `_payload(policy)`.
- Computes `payload['required_zone_article_numbers']` from `['2']`.
- Computes `chapter_id` from `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER') & structure.sections['zone_chapter_label'].eq('U'), 'section_id'].iloc[0]`.
- Computes `payload['chapters'][0]['reviewed_section_ids']` from `[chapter_id]`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='outside reviewed sections')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='outside reviewed sections'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.

**Regression protected**

- Protects the exact `evidence must be inside reviewed sections` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `pytest.raises`, `structure.sections['section_type'].eq`, `structure.sections['zone_chapter_label'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_review_cannot_claim_another_chapter_section`

**Signature**

```python
def test_review_cannot_claim_another_chapter_section(inputs) -> None:
```

**Purpose**

Protects the `review cannot claim another chapter section` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 5 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `structure` from `inputs[1]`.
- Computes `payload` from `_payload(policy)`.
- Computes `n_article` from `structure.sections.loc[structure.sections['section_type'].eq('ARTICLE') & structure.sections['zone_chapter_label'].eq('N'), 'section_id'].iloc[0]`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='another chapter')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='another chapter'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.

**Regression protected**

- Protects the exact `review cannot claim another chapter section` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `pytest.raises`, `structure.sections['section_type'].eq`, `structure.sections['zone_chapter_label'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_general_section_review_is_explicit_and_valid`

**Signature**

```python
def test_general_section_review_is_explicit_and_valid(inputs) -> None:
```

**Purpose**

Protects the `general section review is explicit and valid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 6 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `structure` from `inputs[1]`.
- Computes `payload` from `_payload(policy)`.
- Computes `general_id` from `structure.sections.loc[structure.sections['section_type'].eq('GENERAL'), 'section_id'].iloc[0]`.
- Computes `result` from `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.
- Computes `reviewed` from `result.chapter_policy.set_index('resolved_zone_chapter_label').loc['U', 'reviewed_section_ids']`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `result.chapter_policy.set_index`.

**Expected result**

- Direct assertions: `assert general_id in reviewed`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `general section review is explicit and valid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `result.chapter_policy.set_index`, `structure.sections['section_type'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_same_general_occurrence_may_be_scoped_to_different_chapters`

**Signature**

```python
def test_same_general_occurrence_may_be_scoped_to_different_chapters(inputs) -> None:
```

**Purpose**

Protects the `same general occurrence may be scoped to different chapters` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 10 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `general` from `structure.sections.loc[structure.sections['section_type'].eq('GENERAL')].iloc[0]`.
- Computes `fragment` from `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index(['section_id', 'page_number']).loc[general['section_id'], 1]`.
- Computes `excerpt` from `'General factual text.'`.
- Computes `start` from `fragment['raw_text'].index(excerpt)`.
- Computes `base` from `{'section_id': general['section_id'], 'page_number': 1, 'evidence_kind': 'TECHNICAL_EQUIPMENT_RULE', 'evidence_direction': 'CONTEXT_ONLY', 'exact_raw_excerpt': excerpt, 'excerpt_sha256': sha256(excerpt.encode()).hexdigest(), 'section_page_fragment_sha256': fragment['section_page_fragment_sha256'], 'excerpt_start': sta…`.
- Computes `payload` from `_payload(policy)`.
- Computes `scoped_policy` from `BessZoningPolicyConfig.model_validate(payload)`.
- Computes `result` from `interpret_bess_zoning(index, structure, config, zones, relations, parcels, planning_document, scoped_policy)`.
- Computes `scoped` from `result.evidence_catalog.loc[result.evidence_catalog['section_id'].eq(general['section_id']) & result.evidence_catalog['excerpt_start'].eq(start)]`.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `fragment['raw_text'].index`, `interpret_bess_zoning`, `planning_regulation_section_page_fragments`, `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index`, `result.evidence_catalog['excerpt_start'].eq`, `result.evidence_catalog['section_id'].eq`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `zip`.

**Expected result**

- Direct assertions: `assert set(scoped['resolved_zone_chapter_label']) == {'U', 'N'}`; `assert len(scoped) == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `same general occurrence may be scoped to different chapters` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `fragment['raw_text'].index`, `interpret_bess_zoning`, `len`, `planning_regulation_section_page_fragments`, `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index`, `result.evidence_catalog['excerpt_start'].eq`, `result.evidence_catalog['section_id'].eq`, `set`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `structure.sections['section_type'].eq`, `zip`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_section_page_occurrence_is_auditable`

**Signature**

```python
def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
```

**Purpose**

Protects the `exact section page occurrence is auditable` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, *_)` from `inputs`.
- Computes `fragments` from `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index(['section_id', 'page_number'])`.

**Action**

- Calls `planning_regulation_section_page_fragments`, `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index`, `valid_result.evidence_catalog.to_dict`.

**Expected result**

- Direct assertions: `assert row['section_page_fragment_sha256'] == fragment['section_page_fragment_sha256']`; `assert fragment['raw_text'][row['excerpt_start']:row['excerpt_end']] == row['exact_raw_excerpt']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact section page occurrence is auditable` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `planning_regulation_section_page_fragments`, `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index`, `valid_result.evidence_catalog.to_dict`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_repeated_excerpt_occurrence_is_bound_to_policy`

**Signature**

```python
def test_repeated_excerpt_occurrence_is_bound_to_policy(inputs, valid_result) -> None:
```

**Purpose**

Protects the `repeated excerpt occurrence is bound to policy` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 12 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, *_)` from `inputs`.
- Computes `row_index` from `valid_result.evidence_catalog.index[valid_result.evidence_catalog['evidence_id'].eq('E-U-POSITIVE')][0]`.
- Computes `row` from `valid_result.evidence_catalog.loc[row_index]`.
- Computes `fragments` from `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index(['section_id', 'page_number'])`.
- Computes `raw` from `fragments.loc[(row['section_id'], row['page_number']), 'raw_text']`.
- Computes `first` from `raw.index(row['exact_raw_excerpt'])`.
- Computes `second` from `raw.index(row['exact_raw_excerpt'], first + 1)`.
- Computes `catalog` from `valid_result.evidence_catalog.copy(deep=True)`.
- Computes `catalog.loc[row_index, 'excerpt_start']` from `second`.
- Computes `catalog.loc[row_index, 'excerpt_end']` from `second + len(row['exact_raw_excerpt'])`.
- Computes `coordinated` from `_result_with_hashes(replace(valid_result, evidence_catalog=catalog))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')` and executes: Calls `_validate(inputs, coordinated)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `planning_regulation_section_page_fragments`, `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index`, `raw.index`, `replace`, `valid_result.evidence_catalog.copy`, `valid_result.evidence_catalog['evidence_id'].eq`.

**Expected result**

- Direct assertions: `assert second > first`.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from rebuilt'): _validate(inputs, coordinated)`.

**Regression protected**

- Protects the exact `repeated excerpt occurrence is bound to policy` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `len`, `planning_regulation_section_page_fragments`, `planning_regulation_section_page_fragments(index, zones, relations, config, structure).set_index`, `pytest.raises`, `raw.index`, `replace`, `valid_result.evidence_catalog.copy`, `valid_result.evidence_catalog['evidence_id'].eq`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_occurrence_identity_is_rejected`

**Signature**

```python
def test_wrong_occurrence_identity_is_rejected(inputs, mutation: str) -> None:
```

**Purpose**

Protects the `wrong occurrence identity is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `mutation`.
- Contains 4 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `payload` from `_payload(policy)`.
- Computes `evidence` from `payload['chapters'][0]['evidence'][0]`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='fragment|offset')` and executes: Calls `interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='fragment|offset'): interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))`.

**Regression protected**

- Protects the exact `wrong occurrence identity is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `interpret_bess_zoning`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_and_alias_mappings_are_inherited_without_prefix_logic`

**Signature**

```python
def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(valid_result) -> None:
```

**Purpose**

Protects the `exact and alias mappings are inherited without prefix logic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 1 explicit setup/context statement(s).
- Computes `policies` from `valid_result.source_zone_policy.set_index('source_zone_label_raw')`.

**Action**

- Calls `valid_result.source_zone_policy.set_index`.

**Expected result**

- Direct assertions: `assert policies.loc['U', 'mapping_status'] == 'EXACT'`; `assert policies.loc['Ua', 'mapping_status'] == 'CONFIG_ALIAS'`; `assert policies.loc['Ua', 'resolved_zone_chapter_label'] == 'U'`; `assert policies.loc['Ua', 'zoning_precheck_status'] == policies.loc['U', 'zoning_precheck_status']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact and alias mappings are inherited without prefix logic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `valid_result.source_zone_policy.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unmapped_dominant_zone_is_rejected`

**Signature**

```python
def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
```

**Purpose**

Protects the `unmapped dominant zone is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 8 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `mapping` from `structure.zone_mapping.copy()`.
- Computes `mapping.loc[mapping['source_zone_label_raw'].eq('U'), ['resolved_zone_chapter_label', 'matched_section_id']]` from `None`.
- Computes `mapping.loc[mapping['source_zone_label_raw'].eq('U'), 'mapping_status']` from `'UNMAPPED'`.
- Computes `mapping.loc[mapping['source_zone_label_raw'].eq('U'), 'mapping_method']` from `'NONE'`.
- Computes `mutated` from `_structure_with_hashes(replace(structure, zone_mapping=mapping))`.
- Computes `changed_policy` from `policy.model_copy(update={'source_lock': policy.source_lock.model_copy(update={'structure_result_content_sha256': mutated.structure_result_content_sha256})})`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')` and executes: Calls `interpret_bess_zoning(index, mutated, config, zones, relations, parcels, planning_document, changed_policy)` for its validation or side effect.

**Action**

- Calls `_structure_with_hashes`, `interpret_bess_zoning`, `mapping['source_zone_label_raw'].eq`, `policy.model_copy`, `policy.source_lock.model_copy`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='Factual regulation structure'): interpret_bess_zoning(index, mutated, config, zones, relations, parcels, planning_document, changed_policy)`.

**Regression protected**

- Protects the exact `unmapped dominant zone is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_structure_with_hashes`, `interpret_bess_zoning`, `mapping['source_zone_label_raw'].eq`, `policy.model_copy`, `policy.source_lock.model_copy`, `pytest.raises`, `replace`, `structure.zone_mapping.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_link_table_exactly_reproduces_routes_and_reverse_links`

**Signature**

```python
def test_link_table_exactly_reproduces_routes_and_reverse_links(valid_result) -> None:
```

**Purpose**

Protects the `link table exactly reproduces routes and reverse links` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 3 explicit setup/context statement(s).
- Computes `expected` from `{('ROUTE-U-CONDITIONAL', 'E-U-POSITIVE', 'POSITIVE'), ('ROUTE-U-CONDITIONAL', 'E-U-CONDITION', 'CONDITION'), ('ROUTE-N-DIFFICULT', 'E-N-1', 'DIFFICULTY')}`.
- Computes `actual` from `{(row.route_id, row.evidence_id, row.route_role) for row in valid_result.evidence_route_links.itertuples(index=False)}`.
- Computes `catalog` from `valid_result.evidence_catalog.set_index('evidence_id')`.

**Action**

- Calls `bool`, `catalog['decision_linked'].all`, `valid_result.evidence_catalog.set_index`, `valid_result.evidence_route_links.itertuples`.

**Expected result**

- Direct assertions: `assert actual == expected`; `assert catalog.loc['E-U-POSITIVE', 'linked_route_ids'] == ('ROUTE-U-CONDITIONAL',)`; `assert catalog.loc['E-U-POSITIVE', 'linked_route_roles'] == ('POSITIVE',)`; `assert bool(catalog['decision_linked'].all())`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `link table exactly reproduces routes and reverse links` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `bool`, `catalog['decision_linked'].all`, `valid_result.evidence_catalog.set_index`, `valid_result.evidence_route_links.itertuples`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_context_evidence_is_separate_from_decision_outputs`

**Signature**

```python
def test_context_evidence_is_separate_from_decision_outputs(inputs) -> None:
```

**Purpose**

Protects the `context evidence is separate from decision outputs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 9 explicit setup/context statement(s).
- Computes `(*sources, policy)` from `inputs`.
- Computes `context_policy` from `_policy_with_context_only_evidence(policy)`.
- Computes `result` from `interpret_bess_zoning(*sources, context_policy)`.
- Computes `catalog` from `result.evidence_catalog.set_index('evidence_id')`.
- Computes `context` from `catalog.loc['E-U-CONDITION']`.
- Computes `chapter` from `result.chapter_policy.set_index('resolved_zone_chapter_label').loc['U']`.
- Computes `source` from `result.source_zone_policy.set_index('source_zone_label_raw').loc['U']`.
- Computes `relation` from `result.parcel_zone_interpretations.loc[result.parcel_zone_interpretations['resolved_zone_chapter_label'].eq('U')].iloc[0]`.
- Computes `parcel` from `result.parcels.loc[result.parcels['parcel_id'].eq('P-1')].iloc[0]`.

**Action**

- Calls `_policy_with_context_only_evidence`, `bool`, `interpret_bess_zoning`, `result.chapter_policy.set_index`, `result.evidence_catalog.set_index`, `result.parcel_zone_interpretations['resolved_zone_chapter_label'].eq`, `result.parcels['parcel_id'].eq`, `result.source_zone_policy.set_index`.

**Expected result**

- Direct assertions: `assert context['linked_route_ids'] == ()`; `assert context['linked_route_roles'] == ()`; `assert not bool(context['decision_linked'])`; `assert chapter['evidence_ids'] == ('E-U-POSITIVE', 'E-U-CONDITION')`; `assert chapter['decision_evidence_ids'] == ('E-U-POSITIVE',)`; `assert chapter['context_evidence_ids'] == ('E-U-CONDITION',)`; `assert source['decision_evidence_ids'] == ('E-U-POSITIVE',)`; `assert source['context_evidence_ids'] == ('E-U-CONDITION',)`; `assert relation['decision_evidence_ids'] == ('E-U-POSITIVE',)`; `assert relation['context_evidence_ids'] == ('E-U-CONDITION',)`; `assert parcel['zoning_precheck_evidence_ids'] == ('E-U-POSITIVE',)`; `assert parcel['zoning_precheck_context_evidence_ids'] == ('E-U-CONDITION',)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `context evidence is separate from decision outputs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_policy_with_context_only_evidence`, `bool`, `interpret_bess_zoning`, `result.chapter_policy.set_index`, `result.evidence_catalog.set_index`, `result.parcel_zone_interpretations['resolved_zone_chapter_label'].eq`, `result.parcels['parcel_id'].eq`, `result.source_zone_policy.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_aggregation_preserves_conflicts_and_touch_only`

**Signature**

```python
def test_parcel_aggregation_preserves_conflicts_and_touch_only(valid_result) -> None:
```

**Purpose**

Protects the `parcel aggregation preserves conflicts and touch only` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_result`.
- Contains 1 explicit setup/context statement(s).
- Computes `parcels` from `valid_result.parcels.set_index('parcel_id')`.

**Action**

- Calls `pd.isna`, `valid_result.parcels.set_index`.

**Expected result**

- Direct assertions: `assert parcels.loc['P-1', 'zoning_precheck_status'] == 'CONDITIONAL_REVIEW'`; `assert parcels.loc['P-1', 'positive_area_zone_count'] == 1`; `assert parcels.loc['P-2', 'zoning_precheck_status'] == 'CONDITIONAL_REVIEW'`; `assert parcels.loc['P-2', 'positive_area_zone_count'] == 2`; `assert parcels.loc['P-2', 'distinct_zone_status_count'] == 1`; `assert parcels.loc['P-3', 'zoning_precheck_status'] == 'MIXED_REVIEW_REQUIRED'`; `assert parcels.loc['P-3', 'dominant_zone_precheck_status'] == 'CONDITIONAL_REVIEW'`; `assert parcels.loc['P-3', 'non_dominant_different_status_count'] == 1`; `assert parcels.loc['P-4', 'zoning_precheck_status'] == 'UNKNOWN'`; `assert parcels.loc['P-4', 'positive_area_zone_count'] == 0`; `assert parcels.loc['P-4', 'touch_only_zone_count'] == 1`; `assert pd.isna(parcels.loc['P-4', 'dominant_zone_precheck_status'])`; `assert valid_result.touch_only_relation_count == 1`; `assert 'P-4' not in set(valid_result.parcel_zone_interpretations['parcel_id'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel aggregation preserves conflicts and touch only` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `pd.isna`, `set`, `valid_result.parcels.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved`

**Signature**

```python
def test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved(
    inputs, valid_result
) -> None:
```

**Purpose**

Protects the `prior parcel fields geometry order index and crs are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `original` from `inputs[5]`.
- Computes `prior` from `valid_result.parcels.loc[:, original.columns]`.

**Action**

- Calls `valid_result.parcels.index.equals`, `valid_result.parcels['non_zoning_planning_features_interpreted'].eq`, `valid_result.parcels['non_zoning_planning_features_interpreted'].eq(False).all`, `valid_result.parcels['planning_surface_relation_count'].equals`, `valid_result.parcels['zoning_precheck_requires_formal_review'].eq`, `valid_result.parcels['zoning_precheck_requires_formal_review'].eq(True).all`.

**Expected result**

- Direct assertions: `assert valid_result.parcels.index.equals(original.index)`; `assert valid_result.parcels.crs == original.crs`; `assert valid_result.parcels['planning_surface_relation_count'].equals(original['planning_surface_relation_count'])`; `assert valid_result.parcels['non_zoning_planning_features_interpreted'].eq(False).all()`; `assert valid_result.parcels['zoning_precheck_requires_formal_review'].eq(True).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `prior parcel fields geometry order index and crs are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `assert_geodataframe_equal`, `valid_result.parcels.index.equals`, `valid_result.parcels['non_zoning_planning_features_interpreted'].eq`, `valid_result.parcels['non_zoning_planning_features_interpreted'].eq(False).all`, `valid_result.parcels['planning_surface_relation_count'].equals`, `valid_result.parcels['zoning_precheck_requires_formal_review'].eq`, `valid_result.parcels['zoning_precheck_requires_formal_review'].eq(True).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inputs_are_not_mutated`

**Signature**

```python
def test_inputs_are_not_mutated(inputs) -> None:
```

**Purpose**

Protects the `inputs are not mutated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 5 explicit setup/context statement(s).
- Computes `(_, structure, _, zones, relations, parcels, _, _)` from `inputs`.
- Computes `zone_snapshot` from `zones.copy(deep=True)`.
- Computes `relation_snapshot` from `relations.copy(deep=True)`.
- Computes `parcel_snapshot` from `parcels.copy(deep=True)`.
- Computes `section_snapshot` from `structure.sections.copy(deep=True)`.

**Action**

- Calls `interpret_bess_zoning`, `parcels.copy`, `pd.testing.assert_frame_equal`, `relations.copy`, `zones.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `inputs are not mutated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `assert_geodataframe_equal`, `interpret_bess_zoning`, `parcels.copy`, `pd.testing.assert_frame_equal`, `relations.copy`, `structure.sections.copy`, `zones.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_change_after_result_creation_is_rejected`

**Signature**

```python
def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `policy change after result creation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `payload['chapters'][0]['rationale']` from `'Changed checked-in rationale.'`.
- Computes `changed` from `BessZoningPolicyConfig.model_validate(payload)`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='policy_config_sha256')` and executes: Calls `validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `validate_bess_zoning_precheck`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='policy_config_sha256'): validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)`.

**Regression protected**

- Protects the exact `policy change after result creation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `pytest.raises`, `validate_bess_zoning_precheck`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_evidence_change_after_result_creation_is_rejected`

**Signature**

```python
def test_evidence_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `evidence change after result creation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 7 explicit setup/context statement(s).
- Computes `payload` from `_payload(inputs[-1])`.
- Computes `excerpt` from `'equipment is permitted'`.
- Computes `evidence` from `payload['chapters'][0]['evidence'][0]`.
- Computes `evidence['exact_raw_excerpt']` from `excerpt`.
- Computes `evidence['excerpt_sha256']` from `sha256(excerpt.encode()).hexdigest()`.
- Computes `changed` from `BessZoningPolicyConfig.model_validate(payload)`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError)` and executes: Calls `validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)` for its validation or side effect.

**Action**

- Calls `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `validate_bess_zoning_precheck`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError): validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)`.

**Regression protected**

- Protects the exact `evidence change after result creation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `_payload`, `excerpt.encode`, `len`, `pytest.raises`, `sha256`, `sha256(excerpt.encode()).hexdigest`, `validate_bess_zoning_precheck`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zoning_relation_and_zone_mapping_changes_are_rejected`

**Signature**

```python
def test_zoning_relation_and_zone_mapping_changes_are_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `zoning relation and zone mapping changes are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 6 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `changed_relations` from `relations.copy()`.
- Computes `changed_relations.loc[0, 'intersection_area_m2']` from `99.0`.
- Computes `changed_relations.loc[0, 'parcel_share_pct']` from `99.0`.
- Computes `changed_relations.loc[0, 'zone_share_pct']` from `9.9`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')` and executes: Calls `validate_bess_zoning_precheck(index, structure, config, zones, changed_relations, parcels, planning_document, policy, valid_result)` for its validation or side effect.

**Action**

- Calls `relations.copy`, `validate_bess_zoning_precheck`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='Factual regulation structure'): validate_bess_zoning_precheck(index, structure, config, zones, changed_relations, parcels, planning_document, policy, valid_result)`.

**Regression protected**

- Protects the exact `zoning relation and zone mapping changes are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `pytest.raises`, `relations.copy`, `validate_bess_zoning_precheck`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_structure_config_and_hierarchy_changes_are_rejected`

**Signature**

```python
def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
```

**Purpose**

Protects the `structure config and hierarchy changes are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 9 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `changed_config` from `config.model_copy(update={'structure_profile': 'changed'})`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')` and executes: Calls `interpret_bess_zoning(index, structure, changed_config, zones, relations, parcels, planning_document, policy)` for its validation or side effect.
- Computes `changed_sections` from `structure.sections.copy(deep=True)`.
- Computes `article` from `changed_sections['section_type'].eq('ARTICLE')`.
- Computes `changed_sections.loc[article.idxmax(), 'parent_section_id']` from `'SECTION-UNKNOWN'`.
- Computes `changed_structure` from `_structure_with_hashes(replace(structure, sections=changed_sections))`.
- Computes `changed_policy` from `policy.model_copy(update={'source_lock': policy.source_lock.model_copy(update={'structure_result_content_sha256': changed_structure.structure_result_content_sha256})})`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')` and executes: Calls `interpret_bess_zoning(index, changed_structure, config, zones, relations, parcels, planning_document, changed_policy)` for its validation or side effect.

**Action**

- Calls `_structure_with_hashes`, `article.idxmax`, `changed_sections['section_type'].eq`, `config.model_copy`, `interpret_bess_zoning`, `policy.model_copy`, `policy.source_lock.model_copy`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='Factual regulation structure'): interpret_bess_zoning(index, structure, changed_config, zones, relations, parcels, planning_document, policy)`; `with pytest.raises(BessZoningPrecheckError, match='Factual regulation structure'): interpret_bess_zoning(index, changed_structure, config, zones, relations, parcels, planning_document, changed_policy)`.

**Regression protected**

- Protects the exact `structure config and hierarchy changes are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_structure_with_hashes`, `article.idxmax`, `changed_sections['section_type'].eq`, `config.model_copy`, `interpret_bess_zoning`, `policy.model_copy`, `policy.source_lock.model_copy`, `pytest.raises`, `replace`, `structure.sections.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_source_complete_validator_is_invoked`

**Signature**

```python
def test_public_source_complete_validator_is_invoked(inputs, monkeypatch) -> None:
```

**Purpose**

Protects the `public source complete validator is invoked` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `calls` from `0`.
- Computes `original` from `interpret_module.validate_planning_regulation_structure_with_fragments`.

**Action**

- Calls `interpret_bess_zoning`, `monkeypatch.setattr`, `original`.

**Expected result**

- Direct assertions: `assert calls >= 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public source complete validator is invoked` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `interpret_bess_zoning`, `monkeypatch.setattr`, `original`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_precheck_build_performs_one_zoning_source_complete_validation`

**Signature**

```python
def test_one_precheck_build_performs_one_zoning_source_complete_validation(
    inputs,
    monkeypatch,
) -> None:
```

**Purpose**

Protects the `one precheck build performs one zoning source complete validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Computes `calls` from `0`.

**Action**

- Calls `interpret_bess_zoning`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert calls == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `one precheck build performs one zoning source complete validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `interpret_bess_zoning`, `monkeypatch.setattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_physical_zoning_fails_before_policy_interpretation`

**Signature**

```python
def test_invalid_physical_zoning_fails_before_policy_interpretation(
    inputs,
    monkeypatch,
) -> None:
```

**Purpose**

Protects the `invalid physical zoning fails before policy interpretation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `policy_calls` from `0`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='physical source invalid')` and executes: Calls `interpret_bess_zoning(*inputs)` for its validation or side effect.

**Action**

- Calls `interpret_bess_zoning`, `interpret_module.PlanningZoningError`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert policy_calls == 0`.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='physical source invalid'): interpret_bess_zoning(*inputs)`.

**Regression protected**

- Protects the exact `invalid physical zoning fails before policy interpretation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `interpret_bess_zoning`, `interpret_module.PlanningZoningError`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_build_result_performs_one_factual_structure_rebuild`

**Signature**

```python
def test_one_build_result_performs_one_factual_structure_rebuild(
    inputs, monkeypatch
) -> None:
```

**Purpose**

Protects the `one build result performs one factual structure rebuild` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `calls` from `0`.
- Computes `original` from `interpret_module.validate_planning_regulation_structure_with_fragments`.

**Action**

- Calls `interpret_module._build_result`, `monkeypatch.setattr`, `original`.

**Expected result**

- Direct assertions: `assert calls == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `one build result performs one factual structure rebuild` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `interpret_module._build_result`, `monkeypatch.setattr`, `original`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_area_denominators_are_required`

**Signature**

```python
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
```

**Purpose**

Protects the `relation area denominators are required` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `column`.
- Contains 2 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError)` and executes: Calls `interpret_bess_zoning(index, structure, config, zones, relations.drop(columns=column), parcels, planning_document, policy)` for its validation or side effect.

**Action**

- Calls `interpret_bess_zoning`, `relations.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError): interpret_bess_zoning(index, structure, config, zones, relations.drop(columns=column), parcels, planning_document, policy)`.

**Regression protected**

- Protects the exact `relation area denominators are required` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `interpret_bess_zoning`, `pytest.mark.parametrize`, `pytest.raises`, `relations.drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_percentages_must_match_denominators`

**Signature**

```python
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
```

**Purpose**

Protects the `relation percentages must match denominators` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `column`.
- Contains 3 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `changed` from `relations.copy(deep=True)`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError)` and executes: Calls `interpret_bess_zoning(index, structure, config, zones, changed, parcels, planning_document, policy)` for its validation or side effect.

**Action**

- Calls `interpret_bess_zoning`, `relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError): interpret_bess_zoning(index, structure, config, zones, changed, parcels, planning_document, policy)`.

**Regression protected**

- Protects the exact `relation percentages must match denominators` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `interpret_bess_zoning`, `pytest.mark.parametrize`, `pytest.raises`, `relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_factual_zone_mapping_counts_are_recomputed`

**Signature**

```python
def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
```

**Purpose**

Protects the `factual zone mapping counts are recomputed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 10 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `changed_mapping` from `structure.zone_mapping.copy(deep=True)`.
- Computes `changed_structure` from `_structure_with_hashes(replace(structure, zone_mapping=changed_mapping))`.
- Computes `changed_policy` from `policy.model_copy(update={'source_lock': policy.source_lock.model_copy(update={'structure_result_content_sha256': changed_structure.structure_result_content_sha256})})`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')` and executes: Calls `interpret_bess_zoning(index, changed_structure, config, zones, relations, parcels, planning_document, changed_policy)` for its validation or side effect.
- Computes `changed_mapping` from `structure.zone_mapping.copy()`.
- Computes `changed_mapping.loc[0, 'source_zone_label_raw']` from `'CHANGED'`.
- Computes `changed_structure` from `_structure_with_hashes(replace(structure, zone_mapping=changed_mapping))`.
- Computes `changed_policy` from `policy.model_copy(update={'source_lock': policy.source_lock.model_copy(update={'structure_result_content_sha256': changed_structure.structure_result_content_sha256})})`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError)` and executes: Calls `validate_bess_zoning_precheck(index, changed_structure, config, zones, relations, parcels, planning_document, changed_policy, valid_result)` for its validation or side effect.

**Action**

- Calls `_structure_with_hashes`, `interpret_bess_zoning`, `policy.model_copy`, `policy.source_lock.model_copy`, `replace`, `validate_bess_zoning_precheck`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='Factual regulation structure'): interpret_bess_zoning(index, changed_structure, config, zones, relations, parcels, planning_document, changed_policy)`; `with pytest.raises(BessZoningPrecheckError): validate_bess_zoning_precheck(index, changed_structure, config, zones, relations, parcels, planning_document, changed_policy, valid_result)`.

**Regression protected**

- Protects the exact `factual zone mapping counts are recomputed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_structure_with_hashes`, `interpret_bess_zoning`, `policy.model_copy`, `policy.source_lock.model_copy`, `pytest.raises`, `replace`, `structure.zone_mapping.copy`, `validate_bess_zoning_precheck`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_result_mutation_is_rejected`

**Signature**

```python
def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `coordinated result mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `chapter` from `valid_result.chapter_policy.copy(deep=True)`.
- Computes `chapter.loc[0, 'zoning_precheck_confidence']` from `'HIGH'`.
- Computes `mutated` from `_result_with_hashes(replace(valid_result, chapter_policy=chapter))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')` and executes: Calls `_validate(inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `replace`, `valid_result.chapter_policy.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from rebuilt'): _validate(inputs, mutated)`.

**Regression protected**

- Protects the exact `coordinated result mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `pytest.raises`, `replace`, `valid_result.chapter_policy.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_evidence_catalog_mutation_is_rejected`

**Signature**

```python
def test_coordinated_evidence_catalog_mutation_is_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `coordinated evidence catalog mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `catalog` from `valid_result.evidence_catalog.copy(deep=True)`.
- Computes `catalog.loc[0, 'interpretation_note']` from `'Coordinated mutation.'`.
- Computes `mutated` from `_result_with_hashes(replace(valid_result, evidence_catalog=catalog))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')` and executes: Calls `_validate(inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `replace`, `valid_result.evidence_catalog.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from rebuilt'): _validate(inputs, mutated)`.

**Regression protected**

- Protects the exact `coordinated evidence catalog mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `pytest.raises`, `replace`, `valid_result.evidence_catalog.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_catalog_occurrence_duplicate_is_rejected`

**Signature**

```python
def test_coordinated_catalog_occurrence_duplicate_is_rejected(
    inputs, valid_result
) -> None:
```

**Purpose**

Protects the `coordinated catalog occurrence duplicate is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 5 explicit setup/context statement(s).
- Computes `catalog` from `valid_result.evidence_catalog.copy(deep=True)`.
- Computes `occurrence_columns` from `['resolved_zone_chapter_label', 'section_id', 'page_number', 'section_page_fragment_sha256', 'excerpt_start', 'excerpt_end']`.
- Computes `catalog.loc[catalog.index[1], occurrence_columns]` from `catalog.loc[catalog.index[0], occurrence_columns].to_numpy()`.
- Computes `mutated` from `_result_with_hashes(replace(valid_result, evidence_catalog=catalog))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='duplicate chapter-scoped evidence occurrence')` and executes: Calls `_validate(inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `catalog.loc[catalog.index[0], occurrence_columns].to_numpy`, `replace`, `valid_result.evidence_catalog.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='duplicate chapter-scoped evidence occurrence'): _validate(inputs, mutated)`.

**Regression protected**

- Protects the exact `coordinated catalog occurrence duplicate is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `catalog.loc[catalog.index[0], occurrence_columns].to_numpy`, `pytest.raises`, `replace`, `valid_result.evidence_catalog.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_route_table_mutation_is_rejected`

**Signature**

```python
def test_coordinated_route_table_mutation_is_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `coordinated route table mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `routes` from `valid_result.route_assessments.copy(deep=True)`.
- Computes `routes.loc[0, 'applicability_note']` from `'Coordinated route mutation.'`.
- Computes `mutated` from `_result_with_hashes(replace(valid_result, route_assessments=routes))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')` and executes: Calls `_validate(inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `replace`, `valid_result.route_assessments.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from rebuilt'): _validate(inputs, mutated)`.

**Regression protected**

- Protects the exact `coordinated route table mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `pytest.raises`, `replace`, `valid_result.route_assessments.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_evidence_route_link_mutation_is_rejected`

**Signature**

```python
def test_coordinated_evidence_route_link_mutation_is_rejected(
    inputs, valid_result
) -> None:
```

**Purpose**

Protects the `coordinated evidence route link mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `links` from `valid_result.evidence_route_links.copy(deep=True)`.
- Computes `links.loc[0, 'route_role']` from `'BROKEN'`.
- Computes `mutated` from `_result_with_hashes(replace(valid_result, evidence_route_links=links))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')` and executes: Calls `_validate(inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `replace`, `valid_result.evidence_route_links.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from rebuilt'): _validate(inputs, mutated)`.

**Regression protected**

- Protects the exact `coordinated evidence route link mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `pytest.raises`, `replace`, `valid_result.evidence_route_links.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_reverse_link_mutation_is_rejected`

**Signature**

```python
def test_coordinated_reverse_link_mutation_is_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `coordinated reverse link mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 4 explicit setup/context statement(s).
- Computes `catalog` from `valid_result.evidence_catalog.copy(deep=True)`.
- Computes `catalog.at[0, 'linked_route_roles']` from `('DIFFICULTY',)`.
- Computes `mutated` from `_result_with_hashes(replace(valid_result, evidence_catalog=catalog))`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')` and executes: Calls `_validate(inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_result_with_hashes`, `_validate`, `replace`, `valid_result.evidence_catalog.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from rebuilt'): _validate(inputs, mutated)`.

**Regression protected**

- Protects the exact `coordinated reverse link mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_result_with_hashes`, `_validate`, `pytest.raises`, `replace`, `valid_result.evidence_catalog.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_evidence_route_link_hash_mutation_is_rejected`

**Signature**

```python
def test_evidence_route_link_hash_mutation_is_rejected(inputs, valid_result) -> None:
```

**Purpose**

Protects the `evidence route link hash mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`.
- Contains 2 explicit setup/context statement(s).
- Computes `mutated` from `replace(valid_result, evidence_route_links_content_sha256='f' * 64)`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')` and executes: Calls `_validate(inputs, mutated)` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='differs from rebuilt'): _validate(inputs, mutated)`.

**Regression protected**

- Protects the exact `evidence route link hash mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_old_result_hash_schemas_are_rejected`

**Signature**

```python
def test_old_result_hash_schemas_are_rejected(
    inputs, valid_result, version: int
) -> None:
```

**Purpose**

Protects the `old result hash schemas are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`, `valid_result`, `version`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='result_hash_schema_version')` and executes: Calls `_validate(inputs, replace(valid_result, result_hash_schema_version=version))` for its validation or side effect.

**Action**

- Calls `_validate`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='result_hash_schema_version'): _validate(inputs, replace(valid_result, result_hash_schema_version=version))`.

**Regression protected**

- Protects the exact `old result hash schemas are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_identity_change_is_rejected`

**Signature**

```python
def test_relation_identity_change_is_rejected(inputs) -> None:
```

**Purpose**

Protects the `relation identity change is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `inputs`.
- Contains 4 explicit setup/context statement(s).
- Computes `(index, structure, config, zones, relations, parcels, planning_document, policy)` from `inputs`.
- Computes `changed` from `relations.copy()`.
- Computes `changed.loc[0, 'source_zone_id']` from `'SRC-N'`.
- Enters managed context(s) `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')` and executes: Calls `interpret_bess_zoning(index, structure, config, zones, changed, parcels, planning_document, policy)` for its validation or side effect.

**Action**

- Calls `interpret_bess_zoning`, `relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessZoningPrecheckError, match='Factual regulation structure'): interpret_bess_zoning(index, structure, config, zones, changed, parcels, planning_document, policy)`.

**Regression protected**

- Protects the exact `relation identity change is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `interpret_bess_zoning`, `pytest.raises`, `relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_readback_result_validates`

**Signature**

```python
def test_readback_result_validates(tmp_path: Path, inputs, valid_result) -> None:
```

**Purpose**

Protects the `readback result validates` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `inputs`, `valid_result`.
- Contains 9 explicit setup/context statement(s).
- Computes `chapter_path` from `tmp_path / 'chapter.parquet'`.
- Computes `evidence_path` from `tmp_path / 'evidence.parquet'`.
- Computes `route_path` from `tmp_path / 'routes.parquet'`.
- Computes `link_path` from `tmp_path / 'links.parquet'`.
- Computes `source_path` from `tmp_path / 'source.parquet'`.
- Computes `relation_path` from `tmp_path / 'relations.parquet'`.
- Computes `parcel_path` from `tmp_path / 'parcels.parquet'`.
- Computes `persisted` from `replace(valid_result, evidence_catalog=pd.read_parquet(evidence_path), route_assessments=pd.read_parquet(route_path), evidence_route_links=pd.read_parquet(link_path), chapter_policy=pd.read_parquet(chapter_path), source_zone_policy=pd.read_parquet(source_path), parcel_zone_interpretations=pd.read_parquet(relation_path…`.
- Computes `occurrence_columns` from `['resolved_zone_chapter_label', 'section_id', 'page_number', 'section_page_fragment_sha256', 'excerpt_start', 'excerpt_end']`.

**Action**

- Calls `_validate`, `gpd.read_parquet`, `pd.read_parquet`, `persisted.evidence_catalog.duplicated`, `persisted.evidence_catalog.duplicated(occurrence_columns).any`, `replace`, `valid_result.chapter_policy.to_parquet`, `valid_result.evidence_catalog.to_parquet`, `valid_result.evidence_route_links.to_parquet`, `valid_result.parcel_zone_interpretations.to_parquet`, `valid_result.parcels.to_parquet`, `valid_result.route_assessments.to_parquet`, `valid_result.source_zone_policy.to_parquet`.

**Expected result**

- Direct assertions: `assert not persisted.evidence_catalog.duplicated(occurrence_columns).any()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `readback result validates` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_validate`, `gpd.read_parquet`, `pd.read_parquet`, `persisted.evidence_catalog.duplicated`, `persisted.evidence_catalog.duplicated(occurrence_columns).any`, `replace`, `valid_result.chapter_policy.to_parquet`, `valid_result.evidence_catalog.to_parquet`, `valid_result.evidence_route_links.to_parquet`, `valid_result.parcel_zone_interpretations.to_parquet`, `valid_result.parcels.to_parquet`, `valid_result.route_assessments.to_parquet`, `valid_result.source_zone_policy.to_parquet`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_yaml_roundtrip_is_strict`

**Signature**

```python
def test_policy_yaml_roundtrip_is_strict(tmp_path: Path, inputs) -> None:
```

**Purpose**

Protects the `policy yaml roundtrip is strict` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `inputs`.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `inputs[-1]`.
- Computes `path` from `tmp_path / 'policy.yaml'`.

**Action**

- Calls `load_bess_zoning_policy_config`, `path.write_text`, `policy.model_dump`, `yaml.safe_dump`.

**Expected result**

- Direct assertions: `assert load_bess_zoning_policy_config(path) == policy`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy yaml roundtrip is strict` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_bess_zoning_policy_config`, `path.write_text`, `policy.model_dump`, `yaml.safe_dump`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `E-N-1` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `E-U-CONDITION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `E-U-POSITIVE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `P-1` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `P-2` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `P-3` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `P-4` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `U` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `Ua` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `applicability_note` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `automatic_classifier` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `candidate_intersection_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `chapters` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `condition_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `context_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `decision_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `decision_linked` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `difficulty_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `distinct_zone_status_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `evidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_direction` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `exact_raw_excerpt` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `excerpt_end` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `excerpt_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `excerpt_start` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `information_surface_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `interpretation_note` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `linked_route_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `linked_route_roles` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `mapping_method` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `mapping_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `missing_required_section_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `non_dominant_different_status_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `non_zoning_planning_features_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `page_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `page_number` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `parent_section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `planning_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_point_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `positive_area_zone_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `positive_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `prescription_surface_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `prior_fact` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `raw_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `required_zone_article_numbers` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `resolved_zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `review_completeness` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `review_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `reviewed_section_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `route_assessments` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `route_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `route_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `route_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `section_page_fragment_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `section_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_lock` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_end` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_excerpt` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_start` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `touch_only_zone_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `zone_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_context_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_requires_formal_review` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |

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
