# `tests/unit/test_normalize_grid_ign.py`

## File identity

- Repository path: `tests/unit/test_normalize_grid_ign.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `2ef2f253fa949fff73772dd7e05f6f46a0d8b1bccafb33606ad21b2be108c345`

## 1. Purpose

Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import tempfile` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, Literal, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `from uuid import uuid4` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pyogrio` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( LineString, MultiLineString, MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `import landscout.stages.normalize_grid_ign as grid_normalization` — required by the implementation paths and symbols documented below.
- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoDownload, IgnBdTopoElectricityData, IgnBdTopoExtraction, IgnBdTopoLayerSummary, IgnBdTopoSourceConfig, load_ign_bdtopo_source_config, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import ( LINE_OUTPUT_COLUMNS, TRANSFORMATION_POST_OUTPUT_COLUMNS, IgnGridNormalizationError, NormalizedIgnElectricityData, parse_ign_voltage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import ( _IgnGridSourceContext as IgnGridSourceContext, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import ( _normalize_ign_electric_lines as normalize_ign_electric_lines, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import ( _normalize_ign_transformation_posts as normalize_ign_transformation_posts, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import ( normalize_ign_electricity as _normalize_ign_electricity, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `LINE_LAYER` | `"LIGNE_ELECTRIQUE_V2"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POST_LAYER` | `"POSTE_DE_TRANSFORMATION_V2"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_SHA256` | `"a" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_URL` | `"https://example.test/BDTOPO_D031.7z"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_FIXTURE_ROOT` | `Path(tempfile.mkdtemp(prefix="landscout-grid-ign-"))` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SOURCE_CONFIG_PAYLOAD` | `load_ign_bdtopo_source_config().model_dump(mode="json")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_CONFIG` | `IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `normalize_ign_electricity`

**Signature**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
```

**Purpose**

Normalizes ign electricity according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoElectricityData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `NormalizedIgnElectricityData`. Observed return expression(s): `_normalize_ign_electricity(source, SOURCE_CONFIG)`.

**Algorithm**

1. Returns `_normalize_ign_electricity(source, SOURCE_CONFIG)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_normalize_ign_electricity`.

**Known repository callers**

- `tests/unit/test_normalize_grid_ign.py` — `test_grid_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_grid_ign.py` — `test_grid_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_path_uses_discovered_layer_names_and_archive_lineage`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_any_spatial_role_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_colliding_electricity_roles`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_coordinated_frame_and_summary_forgery`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_duplicate_or_missing_layer_inventory`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_forged_ordered_summary_schema`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_incompatible_archive_identity`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_stale_geometry_counts_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_stale_geometry_types_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_summary_crs_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_summary_layer_name_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_summary_row_count_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_wrong_logical_name`
- `tests/unit/test_normalize_grid_ign.py` — `test_source_complete_grid_validation_does_not_mutate_supplied_frames`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_grid_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_grid_ign.py::test_grid_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_path_uses_discovered_layer_names_and_archive_lineage`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_any_spatial_role_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_colliding_electricity_roles`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_duplicate_or_missing_layer_inventory`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_forged_ordered_summary_schema`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_incompatible_archive_identity`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_counts_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_types_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_crs_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_layer_name_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_row_count_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_wrong_logical_name`
- `tests/unit/test_normalize_grid_ign.py::test_source_complete_grid_validation_does_not_mutate_supplied_frames`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_line_source`

**Signature**

```python
def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements line source according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltages` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `precisions` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `index` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'cleabs': source_ids, 'voltage': source_voltages, 'gestionnaire': ["Réseau de Transport d'Électricité"] * count, 'siren_gestionnaire': ['444619258'] * count, 'etat_de_l_objet': ['En service'] * count, 'sources': ['RTE 2024'] * count, 'identifiants_sources': ['source-id'] * count, 'date_creation': pd.to_datetime(['2024-01-01'] * count), 'date_modification': pd.to_datetime(['2025-…`.

**Algorithm**

1. Computes `source_geometries` from `geometries if geometries is not None else [LineString([(0, 0), (100, 100)])]`.
2. Computes `count` from `len(source_geometries)`.
3. Computes `source_ids` from `identifiers if identifiers is not None else [f'LIGNE-{item + 1}' for item in range(count)]`.
4. Computes `source_voltages` from `voltages if voltages is not None else ['225 kV'] * count`.
5. Computes `source_precisions` from `precisions if precisions is not None else [2.5] * count`.
6. Computes `source_index` from `index if index is not None else [100 + item for item in range(count)]`.
7. Returns `gpd.GeoDataFrame({'cleabs': source_ids, 'voltage': source_voltages, 'gestionnaire': ["Réseau de Transport d'Électricité"] * count, 'siren_gestionnaire': ['444619258'] * count, 'etat_de_l_objet': ['En service'] * count, 'sources': ['RTE 2024'] * count, 'identifiants_sources': ['source-id'] * count, 'date_creation': pd.to_datetime(['2024-01-01'] * count), 'da…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `gpd.GeoDataFrame`, `len`, `pd.to_datetime`, `range`.

**Known repository callers**

- `tests/unit/test_normalize_grid_ign.py` — `_source_bundle`
- `tests/unit/test_normalize_grid_ign.py` — `test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py` — `test_deenergized_voltage_does_not_override_source_asset_status`
- `tests/unit/test_normalize_grid_ign.py` — `test_duplicate_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_internal_source_context_rejects_uppercase_sha256`
- `tests/unit/test_normalize_grid_ign.py` — `test_invalid_line_precision_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_geometry_quality_is_preserved_without_row_loss_or_repair`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_missing_or_wrong_crs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_normalization_does_not_mutate_input_and_has_stable_columns`
- `tests/unit/test_normalize_grid_ign.py` — `test_missing_required_line_field_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_normalized_voltage_never_emits_non_finite_numeric_values`
- `tests/unit/test_normalize_grid_ign.py` — `test_null_or_empty_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_unsafe_source_id_is_rejected_without_rewriting`
- `tests/unit/test_normalize_grid_ign.py` — `test_unusual_duplicate_source_index_is_not_preserved_as_identity`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_line_has_stable_identity_lineage_and_range_index`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_or_null_line_precision_is_normalized_to_float`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_polygon_or_point_is_rejected_as_electric_line`
- `tests/unit/test_normalize_grid_ign.py` — `test_z_coordinates_are_preserved`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_does_not_override_source_asset_status`
- `tests/unit/test_normalize_grid_ign.py::test_duplicate_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256`
- `tests/unit/test_normalize_grid_ign.py::test_invalid_line_precision_fails`
- `tests/unit/test_normalize_grid_ign.py::test_line_geometry_quality_is_preserved_without_row_loss_or_repair`
- `tests/unit/test_normalize_grid_ign.py::test_line_missing_or_wrong_crs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_line_normalization_does_not_mutate_input_and_has_stable_columns`
- `tests/unit/test_normalize_grid_ign.py::test_missing_required_line_field_fails`
- `tests/unit/test_normalize_grid_ign.py::test_normalized_voltage_never_emits_non_finite_numeric_values`
- `tests/unit/test_normalize_grid_ign.py::test_null_or_empty_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_unsafe_source_id_is_rejected_without_rewriting`
- `tests/unit/test_normalize_grid_ign.py::test_unusual_duplicate_source_index_is_not_preserved_as_identity`
- `tests/unit/test_normalize_grid_ign.py::test_valid_line_has_stable_identity_lineage_and_range_index`
- `tests/unit/test_normalize_grid_ign.py::test_valid_or_null_line_precision_is_normalized_to_float`
- `tests/unit/test_normalize_grid_ign.py::test_valid_polygon_or_point_is_rejected_as_electric_line`
- `tests/unit/test_normalize_grid_ign.py::test_z_coordinates_are_preserved`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_post_source`

**Signature**

```python
def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements post source according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `precisions` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `index` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'cleabs': source_ids, 'toponyme': ['Poste de test'] * count, 'statut_du_toponyme': ['Validé'] * count, 'importance': ['5'] * count, 'etat_de_l_objet': ['En service'] * count, 'sources': ['RTE 2021'] * count, 'identifiants_sources': ['source-post-id'] * count, 'date_creation': pd.to_datetime(['2023-01-01'] * count), 'date_modification': pd.to_datetime(['2025-02-01'] * count), 'da…`.

**Algorithm**

1. Computes `source_geometries` from `geometries if geometries is not None else [Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])]`.
2. Computes `count` from `len(source_geometries)`.
3. Computes `source_ids` from `identifiers if identifiers is not None else [f'POSTE-{item + 1}' for item in range(count)]`.
4. Computes `source_precisions` from `precisions if precisions is not None else [5.0] * count`.
5. Computes `source_index` from `index if index is not None else [200 + item for item in range(count)]`.
6. Returns `gpd.GeoDataFrame({'cleabs': source_ids, 'toponyme': ['Poste de test'] * count, 'statut_du_toponyme': ['Validé'] * count, 'importance': ['5'] * count, 'etat_de_l_objet': ['En service'] * count, 'sources': ['RTE 2021'] * count, 'identifiants_sources': ['source-post-id'] * count, 'date_creation': pd.to_datetime(['2023-01-01'] * count), 'date_modification': pd.…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `len`, `pd.to_datetime`, `range`.

**Known repository callers**

- `tests/unit/test_normalize_grid_ign.py` — `_source_bundle`
- `tests/unit/test_normalize_grid_ign.py` — `test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py` — `test_duplicate_post_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_invalid_post_precision_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_null_post_geometry_and_precision_are_preserved`
- `tests/unit/test_normalize_grid_ign.py` — `test_post_geometry_crs_and_input_are_preserved`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_line_or_point_is_rejected_as_transformation_post`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_post_has_stable_lineage_and_no_voltage_inference`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py::test_duplicate_post_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_invalid_post_precision_fails`
- `tests/unit/test_normalize_grid_ign.py::test_null_post_geometry_and_precision_are_preserved`
- `tests/unit/test_normalize_grid_ign.py::test_post_geometry_crs_and_input_are_preserved`
- `tests/unit/test_normalize_grid_ign.py::test_valid_line_or_point_is_rejected_as_transformation_post`
- `tests/unit/test_normalize_grid_ign.py::test_valid_post_has_stable_lineage_and_no_voltage_inference`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_context`

**Signature**

```python
def _context(source_layer: str) -> IgnGridSourceContext:
```

**Purpose**

Implements context according to the exact implementation and guards in this file.

**Inputs**

- `source_layer` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnGridSourceContext`. Observed return expression(s): `IgnGridSourceContext(source_layer=source_layer, department_code='31', edition='2026-06-15', product_version='3.5', download_timestamp='2026-08-11T15:32:03+00:00', archive_sha256=ARCHIVE_SHA256, source_url=SOURCE_URL)`.

**Algorithm**

1. Returns `IgnGridSourceContext(source_layer=source_layer, department_code='31', edition='2026-06-15', product_version='3.5', download_timestamp='2026-08-11T15:32:03+00:00', archive_sha256=ARCHIVE_SHA256, source_url=SOURCE_URL)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnGridSourceContext`.

**Known repository callers**

- `tests/unit/test_normalize_grid_ign.py` — `test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py` — `test_deenergized_voltage_does_not_override_source_asset_status`
- `tests/unit/test_normalize_grid_ign.py` — `test_duplicate_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_duplicate_post_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_internal_source_context_accepts_supported_department_codes`
- `tests/unit/test_normalize_grid_ign.py` — `test_internal_source_context_rejects_invalid_lineage_values`
- `tests/unit/test_normalize_grid_ign.py` — `test_internal_source_context_rejects_uppercase_sha256`
- `tests/unit/test_normalize_grid_ign.py` — `test_invalid_line_precision_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_invalid_post_precision_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_geometry_quality_is_preserved_without_row_loss_or_repair`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_missing_or_wrong_crs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_normalization_does_not_mutate_input_and_has_stable_columns`
- `tests/unit/test_normalize_grid_ign.py` — `test_missing_required_line_field_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_normalized_voltage_never_emits_non_finite_numeric_values`
- `tests/unit/test_normalize_grid_ign.py` — `test_null_or_empty_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_null_post_geometry_and_precision_are_preserved`
- `tests/unit/test_normalize_grid_ign.py` — `test_post_geometry_crs_and_input_are_preserved`
- `tests/unit/test_normalize_grid_ign.py` — `test_unsafe_source_id_is_rejected_without_rewriting`
- `tests/unit/test_normalize_grid_ign.py` — `test_unusual_duplicate_source_index_is_not_preserved_as_identity`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_line_has_stable_identity_lineage_and_range_index`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_line_or_point_is_rejected_as_transformation_post`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_or_null_line_precision_is_normalized_to_float`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_polygon_or_point_is_rejected_as_electric_line`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_post_has_stable_lineage_and_no_voltage_inference`
- `tests/unit/test_normalize_grid_ign.py` — `test_z_coordinates_are_preserved`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_does_not_override_source_asset_status`
- `tests/unit/test_normalize_grid_ign.py::test_duplicate_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_duplicate_post_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes`
- `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values`
- `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256`
- `tests/unit/test_normalize_grid_ign.py::test_invalid_line_precision_fails`
- `tests/unit/test_normalize_grid_ign.py::test_invalid_post_precision_fails`
- `tests/unit/test_normalize_grid_ign.py::test_line_geometry_quality_is_preserved_without_row_loss_or_repair`
- `tests/unit/test_normalize_grid_ign.py::test_line_missing_or_wrong_crs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_line_normalization_does_not_mutate_input_and_has_stable_columns`
- `tests/unit/test_normalize_grid_ign.py::test_missing_required_line_field_fails`
- `tests/unit/test_normalize_grid_ign.py::test_normalized_voltage_never_emits_non_finite_numeric_values`
- `tests/unit/test_normalize_grid_ign.py::test_null_or_empty_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_null_post_geometry_and_precision_are_preserved`
- `tests/unit/test_normalize_grid_ign.py::test_post_geometry_crs_and_input_are_preserved`
- `tests/unit/test_normalize_grid_ign.py::test_unsafe_source_id_is_rejected_without_rewriting`
- `tests/unit/test_normalize_grid_ign.py::test_unusual_duplicate_source_index_is_not_preserved_as_identity`
- `tests/unit/test_normalize_grid_ign.py::test_valid_line_has_stable_identity_lineage_and_range_index`
- `tests/unit/test_normalize_grid_ign.py::test_valid_line_or_point_is_rejected_as_transformation_post`
- `tests/unit/test_normalize_grid_ign.py::test_valid_or_null_line_precision_is_normalized_to_float`
- `tests/unit/test_normalize_grid_ign.py::test_valid_polygon_or_point_is_rejected_as_electric_line`
- `tests/unit/test_normalize_grid_ign.py::test_valid_post_has_stable_lineage_and_no_voltage_inference`
- `tests/unit/test_normalize_grid_ign.py::test_z_coordinates_are_preserved`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_summary`

**Signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    logical_name: Literal["electric_lines", "transformation_posts"],
    layer_name: str,
) -> IgnBdTopoLayerSummary:
```

**Purpose**

Implements summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`Literal['electric_lines', 'transformation_posts']`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoLayerSummary`. Observed return expression(s): `IgnBdTopoLayerSummary(logical_name=logical_name, source_layer_name=layer_name, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), invalid_geometry_count=int(invalid_mask.sum()…`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Computes `geometry_types` from `tuple(sorted((str(value) for value in geometry[~null_mask].geom_type.dropna().unique())))`.
6. Returns `IgnBdTopoLayerSummary(logical_name=logical_name, source_layer_name=layer_name, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), inval…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerSummary`, `empty_mask.sum`, `frame.dtypes.items`, `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`, `int`, `invalid_mask.sum`, `len`, `null_mask.sum`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_normalize_grid_ign.py` — `_source_bundle`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_coordinated_frame_and_summary_forgery`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source_bundle`

**Signature**

```python
def _source_bundle(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Implements source bundle according to the exact implementation and guards in this file.

**Inputs**

- `lines` (`gpd.GeoDataFrame | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `posts` (`gpd.GeoDataFrame | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `IgnBdTopoElectricityData(extraction=extraction, electric_lines=line_frame, transformation_posts=post_frame, electric_lines_summary=_summary(line_frame, 'electric_lines', LINE_LAYER), transformation_posts_summary=_summary(post_frame, 'transformation_posts', POST_LAYER))`.

**Algorithm**

1. Computes `line_frame` from `lines if lines is not None else _line_source()`.
2. Computes `post_frame` from `posts if posts is not None else _post_source()`.
3. Computes `extraction_path` from `_FIXTURE_ROOT / uuid4().hex`.
4. Calls `extraction_path.mkdir(parents=True)` for its validation or side effect.
5. Computes `geopackage_path` from `extraction_path / 'data.gpkg'`.
6. Calls `pyogrio.write_dataframe(line_frame, geopackage_path, layer=LINE_LAYER, driver='GPKG')` for its validation or side effect.
7. Calls `pyogrio.write_dataframe(post_frame, geopackage_path, layer=POST_LAYER, driver='GPKG', append=True)` for its validation or side effect.
8. Computes `line_frame` from `gpd.read_file(geopackage_path, layer=LINE_LAYER, engine='pyogrio')`.
9. Computes `post_frame` from `gpd.read_file(geopackage_path, layer=POST_LAYER, engine='pyogrio')`.
10. Computes `payload` from `geopackage_path.read_bytes()`.
11. Computes `layer_names` from `tuple((str(row[0]) for row in pyogrio.list_layers(geopackage_path)))`.
12. Computes `digest` from `sha256(payload).hexdigest()`.
13. Computes `marker` from `{'schema_version': 2, 'archive_sha256': ARCHIVE_SHA256, 'geopackage_relative_path': 'data.gpkg', 'geopackage_size_bytes': len(payload), 'geopackage_sha256': digest, 'all_layer_names': list(layer_names), 'electric_lines_layer': LINE_LAYER, 'transformation_posts_layer': POST_LAYER, 'spatial_role': 'PROXY_GEOMETRY'}`.
14. Calls `(extraction_path / '.landscout-extraction.json').write_text(json.dumps(marker), encoding='utf-8')` for its validation or side effect.
15. Computes `archive` from `IgnBdTopoDownload(provider="Institut national de l'information géographique et forestière", product='BD TOPO', department_code='31', edition='2026-06-15', product_version='3.5', projection='EPSG:2154', package_format='GPKG', archive_format='7z', source_url=SOURCE_URL, checksum_url=None, download_timestamp='2026-08-11T…`.
16. Computes `extraction` from `IgnBdTopoExtraction(archive=archive, extraction_path=extraction_path, geopackage_path=geopackage_path, geopackage_filename='data.gpkg', geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=layer_names, electric_lines_layer=LINE_LAYER, transformation_posts_layer=POST_LAYER, cache_hit=True)`.
17. Returns `IgnBdTopoElectricityData(extraction=extraction, electric_lines=line_frame, transformation_posts=post_frame, electric_lines_summary=_summary(line_frame, 'electric_lines', LINE_LAYER), transformation_posts_summary=_summary(post_frame, 'transformation_posts', POST_LAYER))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(extraction_path / '.landscout-extraction.json').write_text`, `IgnBdTopoDownload`, `extraction_path.mkdir`, `geopackage_path.read_bytes`, `gpd.read_file`, `pyogrio.write_dataframe`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(extraction_path / '.landscout-extraction.json').write_text`, `IgnBdTopoDownload`, `IgnBdTopoElectricityData`, `IgnBdTopoExtraction`, `Path`, `_line_source`, `_post_source`, `_summary`, `extraction_path.mkdir`, `geopackage_path.read_bytes`, `gpd.read_file`, `json.dumps`, `len`, `list`, `pyogrio.list_layers`, `pyogrio.write_dataframe`, `sha256`, `sha256(payload).hexdigest`, `str`, `tuple`, `uuid4`.

**Known repository callers**

- `tests/unit/test_normalize_grid_ign.py` — `_source_bundle_with_archive`
- `tests/unit/test_normalize_grid_ign.py` — `test_grid_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_path_uses_discovered_layer_names_and_archive_lineage`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_any_spatial_role_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_colliding_electricity_roles`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_coordinated_frame_and_summary_forgery`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_duplicate_or_missing_layer_inventory`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_forged_ordered_summary_schema`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_stale_geometry_counts_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_stale_geometry_types_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_summary_crs_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_summary_layer_name_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_summary_row_count_mismatch`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_wrong_logical_name`
- `tests/unit/test_normalize_grid_ign.py` — `test_source_complete_grid_validation_does_not_mutate_supplied_frames`
- `tests/unit/test_normalize_grid_ign.py` — `test_supported_package_api_keeps_high_level_normalization`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_grid_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_path_uses_discovered_layer_names_and_archive_lineage`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_any_spatial_role_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_colliding_electricity_roles`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_duplicate_or_missing_layer_inventory`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_forged_ordered_summary_schema`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_counts_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_types_after_frame_mutation`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_crs_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_layer_name_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_row_count_mismatch`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_wrong_logical_name`
- `tests/unit/test_normalize_grid_ign.py::test_source_complete_grid_validation_does_not_mutate_supplied_frames`
- `tests/unit/test_normalize_grid_ign.py::test_supported_package_api_keeps_high_level_normalization`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source_bundle_with_archive`

**Signature**

```python
def _source_bundle_with_archive(**changes: object) -> IgnBdTopoElectricityData:
```

**Purpose**

Implements source bundle with archive according to the exact implementation and guards in this file.

**Inputs**

- `**changes` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `replace(source, extraction=replace(source.extraction, archive=archive))`.

**Algorithm**

1. Computes `source` from `_source_bundle()`.
2. Computes `archive` from `replace(source.extraction.archive, **changes)`.
3. Returns `replace(source, extraction=replace(source.extraction, archive=archive))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_source_bundle`, `replace`.

**Known repository callers**

- `tests/unit/test_normalize_grid_ign.py` — `test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant`
- `tests/unit/test_normalize_grid_ign.py` — `test_grid_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_grid_ign.py` — `test_high_level_rejects_incompatible_archive_identity`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant`
- `tests/unit/test_normalize_grid_ign.py::test_grid_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_incompatible_archive_identity`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_low_level_normalization_is_not_part_of_stages_public_api`

**Signature**

```python
def test_low_level_normalization_is_not_part_of_stages_public_api(name: str) -> None:
```

**Purpose**

Protects the `low level normalization is not part of stages public api` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `name`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `hasattr`.

**Expected result**

- Direct assertions: `assert name not in stages.__all__`; `assert not hasattr(stages, name)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `low level normalization is not part of stages public api` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `hasattr`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_supported_package_api_keeps_high_level_normalization`

**Signature**

```python
def test_supported_package_api_keeps_high_level_normalization() -> None:
```

**Purpose**

Protects the `supported package api keeps high level normalization` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `expected_names` from `{'IgnGridNormalizationError', 'IgnVoltageNormalization', 'NormalizedIgnElectricityData', 'parse_ign_voltage', 'normalize_ign_electricity'}`.
- Computes `normalized` from `stages.normalize_ign_electricity(_source_bundle(), SOURCE_CONFIG)`.

**Action**

- Calls `_source_bundle`, `normalized.electric_lines['source_layer'].unique`, `normalized.electric_lines['source_layer'].unique().tolist`, `normalized.transformation_posts['source_layer'].unique`, `normalized.transformation_posts['source_layer'].unique().tolist`, `stages.normalize_ign_electricity`.

**Expected result**

- Direct assertions: `assert expected_names <= set(stages.__all__)`; `assert normalized.electric_lines['source_layer'].unique().tolist() == [LINE_LAYER]`; `assert normalized.transformation_posts['source_layer'].unique().tolist() == [POST_LAYER]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `supported package api keeps high level normalization` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalized.electric_lines['source_layer'].unique`, `normalized.electric_lines['source_layer'].unique().tolist`, `normalized.transformation_posts['source_layer'].unique`, `normalized.transformation_posts['source_layer'].unique().tolist`, `set`, `stages.normalize_ign_electricity`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_internal_source_context_accepts_supported_department_codes`

**Signature**

```python
def test_internal_source_context_accepts_supported_department_codes(
    department_code: str,
) -> None:
```

**Purpose**

Protects the `internal source context accepts supported department codes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `department_code`.
- Contains 1 explicit setup/context statement(s).
- Computes `context` from `replace(_context(LINE_LAYER), department_code=department_code)`.

**Action**

- Calls `_context`, `grid_normalization._validate_source_context`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `internal source context accepts supported department codes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `grid_normalization._validate_source_context`, `pytest.mark.parametrize`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_internal_source_context_rejects_uppercase_sha256`

**Signature**

```python
def test_internal_source_context_rejects_uppercase_sha256() -> None:
```

**Purpose**

Protects the `internal source context rejects uppercase sha256` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `archive_sha256` from `'A' * 64`.
- Computes `context` from `replace(_context(LINE_LAYER), archive_sha256=archive_sha256)`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='archive_sha256')` and executes: Calls `normalize_ign_electric_lines(_line_source(), context)` for its validation or side effect.

**Action**

- Calls `_context`, `_line_source`, `normalize_ign_electric_lines`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='archive_sha256'): normalize_ign_electric_lines(_line_source(), context)`.

**Regression protected**

- Protects the exact `internal source context rejects uppercase sha256` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `normalize_ign_electric_lines`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_grid_summary_requires_strict_structural_types`

**Signature**

```python
def test_grid_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
```

**Purpose**

Protects the `grid summary requires strict structural types` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `changed` from `replace(source.electric_lines_summary, **{field: value})`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError)` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines_summary=changed))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError): normalize_ign_electricity(replace(source, electric_lines_summary=changed))`.

**Regression protected**

- Protects the exact `grid summary requires strict structural types` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalize_ign_electricity`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_grid_archive_sha256_requires_canonical_lowercase`

**Signature**

```python
def test_grid_archive_sha256_requires_canonical_lowercase(value: str) -> None:
```

**Purpose**

Protects the `grid archive sha256 requires canonical lowercase` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_bundle_with_archive(sha256=value)`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError)` and executes: Calls `normalize_ign_electricity(source)` for its validation or side effect.

**Action**

- Calls `_source_bundle_with_archive`, `normalize_ign_electricity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError): normalize_ign_electricity(source)`.

**Regression protected**

- Protects the exact `grid archive sha256 requires canonical lowercase` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle_with_archive`, `normalize_ign_electricity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_internal_source_context_rejects_invalid_lineage_values`

**Signature**

```python
def test_internal_source_context_rejects_invalid_lineage_values(
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `internal source context rejects invalid lineage values` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `context` from `replace(_context(LINE_LAYER), **{field: value})`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError)` and executes: Calls `grid_normalization._validate_source_context(context)` for its validation or side effect.

**Action**

- Calls `_context`, `grid_normalization._validate_source_context`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError): grid_normalization._validate_source_context(context)`.

**Regression protected**

- Protects the exact `internal source context rejects invalid lineage values` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `grid_normalization._validate_source_context`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_voltage_parser_is_generic_and_finite`

**Signature**

```python
def test_exact_voltage_parser_is_generic_and_finite(
    raw: str, expected_kv: float
) -> None:
```

**Purpose**

Protects the `exact voltage parser is generic and finite` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `raw`, `expected_kv`.
- Contains 1 explicit setup/context statement(s).
- Computes `parsed` from `parse_ign_voltage(raw)`.

**Action**

- Calls `isfinite`, `parse_ign_voltage`.

**Expected result**

- Direct assertions: `assert parsed.raw == raw`; `assert parsed.status == 'EXACT'`; `assert parsed.voltage_kv == expected_kv`; `assert parsed.voltage_kv is not None and isfinite(parsed.voltage_kv)`; `assert parsed.voltage_upper_bound_kv is None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact voltage parser is generic and finite` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `isfinite`, `parse_ign_voltage`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_bounded_voltage_is_generic_finite_and_not_exact`

**Signature**

```python
def test_bounded_voltage_is_generic_finite_and_not_exact(
    raw: str, expected_upper_bound: float
) -> None:
```

**Purpose**

Protects the `bounded voltage is generic finite and not exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `raw`, `expected_upper_bound`.
- Contains 1 explicit setup/context statement(s).
- Computes `parsed` from `parse_ign_voltage(raw)`.

**Action**

- Calls `isfinite`, `parse_ign_voltage`.

**Expected result**

- Direct assertions: `assert parsed.raw == raw`; `assert parsed.status == 'BELOW'`; `assert parsed.voltage_kv is None`; `assert parsed.voltage_upper_bound_kv == expected_upper_bound`; `assert isfinite(parsed.voltage_upper_bound_kv)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `bounded voltage is generic finite and not exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `isfinite`, `parse_ign_voltage`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_voltage_parser`

**Signature**

```python
def test_unknown_voltage_parser(raw: str | None) -> None:
```

**Purpose**

Protects the `unknown voltage parser` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `raw`.
- Contains 1 explicit setup/context statement(s).
- Computes `parsed` from `parse_ign_voltage(raw)`.

**Action**

- Calls `parse_ign_voltage`.

**Expected result**

- Direct assertions: `assert parsed.raw == raw`; `assert parsed.status == 'UNKNOWN'`; `assert parsed.voltage_kv is None`; `assert parsed.voltage_upper_bound_kv is None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unknown voltage parser` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parse_ign_voltage`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_deenergized_voltage_parser`

**Signature**

```python
def test_deenergized_voltage_parser(raw: str) -> None:
```

**Purpose**

Protects the `deenergized voltage parser` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `raw`.
- Contains 1 explicit setup/context statement(s).
- Computes `parsed` from `parse_ign_voltage(raw)`.

**Action**

- Calls `parse_ign_voltage`.

**Expected result**

- Direct assertions: `assert parsed.raw == raw`; `assert parsed.status == 'DEENERGIZED'`; `assert parsed.voltage_kv is None`; `assert parsed.voltage_upper_bound_kv is None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `deenergized voltage parser` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parse_ign_voltage`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unexpected_or_non_scalar_voltage_is_controlled_unparsed`

**Signature**

```python
def test_unexpected_or_non_scalar_voltage_is_controlled_unparsed(
    value: object,
) -> None:
```

**Purpose**

Protects the `unexpected or non scalar voltage is controlled unparsed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 1 explicit setup/context statement(s).
- Computes `parsed` from `parse_ign_voltage(value)`.

**Action**

- Calls `np.array`, `parse_ign_voltage`.

**Expected result**

- Direct assertions: `assert parsed.status == 'UNPARSED'`; `assert parsed.voltage_kv is None`; `assert parsed.voltage_upper_bound_kv is None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unexpected or non scalar voltage is controlled unparsed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `np.array`, `parse_ign_voltage`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_or_overflowing_numeric_voltage_is_unparsed`

**Signature**

```python
def test_invalid_or_overflowing_numeric_voltage_is_unparsed(raw: str) -> None:
```

**Purpose**

Protects the `invalid or overflowing numeric voltage is unparsed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `raw`.
- Contains 1 explicit setup/context statement(s).
- Computes `parsed` from `parse_ign_voltage(raw)`.

**Action**

- Calls `parse_ign_voltage`.

**Expected result**

- Direct assertions: `assert parsed.status == 'UNPARSED'`; `assert parsed.voltage_kv is None`; `assert parsed.voltage_upper_bound_kv is None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `invalid or overflowing numeric voltage is unparsed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parse_ign_voltage`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_line_has_stable_identity_lineage_and_range_index`

**Signature**

```python
def test_valid_line_has_stable_identity_lineage_and_range_index() -> None:
```

**Purpose**

Protects the `valid line has stable identity lineage and range index` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_line_source()`.
- Computes `normalized` from `normalize_ign_electric_lines(source, _context(LINE_LAYER))`.
- Computes `row` from `normalized.iloc[0]`.

**Action**

- Calls `_context`, `_line_source`, `isinstance`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: `assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)`; `assert isinstance(normalized.index, pd.RangeIndex)`; `assert row['grid_feature_id'] == 'IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1'`; `assert row['source_feature_id'] == 'LIGNE-1'`; `assert row['source_provider'] == 'IGN'`; `assert row['source_product'] == 'BD_TOPO'`; `assert row['source_layer'] == LINE_LAYER`; `assert row['source_department_code'] == '31'`; `assert row['source_edition'] == '2026-06-15'`; `assert row['source_product_version'] == '3.5'`; `assert row['source_download_timestamp'] == '2026-08-11T15:32:03+00:00'`; `assert row['source_archive_sha256'] == ARCHIVE_SHA256`; `assert row['source_url'] == SOURCE_URL`; `assert row['manager_name'] == "Réseau de Transport d'Électricité"`; `assert row['asset_status_raw'] == 'En service'`; `assert row['source_identifiers_raw'] == 'source-id'`; `assert row['planimetric_precision_m'] == 2.5`; `assert row['spatial_role'] == 'PROXY_GEOMETRY'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid line has stable identity lineage and range index` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `isinstance`, `list`, `normalize_ign_electric_lines`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_deenergized_voltage_does_not_override_source_asset_status`

**Signature**

```python
def test_deenergized_voltage_does_not_override_source_asset_status() -> None:
```

**Purpose**

Protects the `deenergized voltage does not override source asset status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `normalized` from `normalize_ign_electric_lines(_line_source(voltages=['Hors tension']), _context(LINE_LAYER))`.

**Action**

- Calls `_context`, `_line_source`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: `assert normalized.iloc[0]['voltage_status'] == 'DEENERGIZED'`; `assert normalized.iloc[0]['asset_status_raw'] == 'En service'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `deenergized voltage does not override source asset status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `normalize_ign_electric_lines`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_or_empty_line_cleabs_fails`

**Signature**

```python
def test_null_or_empty_line_cleabs_fails(identifier: object) -> None:
```

**Purpose**

Protects the `null or empty line cleabs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identifier`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='cleabs|null|empty')` and executes: Calls `normalize_ign_electric_lines(_line_source(identifiers=[identifier]), _context(LINE_LAYER))` for its validation or side effect.

**Action**

- Calls `_context`, `_line_source`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='cleabs|null|empty'): normalize_ign_electric_lines(_line_source(identifiers=[identifier]), _context(LINE_LAYER))`.

**Regression protected**

- Protects the exact `null or empty line cleabs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `normalize_ign_electric_lines`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_source_id_is_rejected_without_rewriting`

**Signature**

```python
def test_unsafe_source_id_is_rejected_without_rewriting(identifier: str) -> None:
```

**Purpose**

Protects the `unsafe source id is rejected without rewriting` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identifier`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='cleabs|whitespace|control|:')` and executes: Calls `normalize_ign_electric_lines(_line_source(identifiers=[identifier]), _context(LINE_LAYER))` for its validation or side effect.

**Action**

- Calls `_context`, `_line_source`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='cleabs|whitespace|control|:'): normalize_ign_electric_lines(_line_source(identifiers=[identifier]), _context(LINE_LAYER))`.

**Regression protected**

- Protects the exact `unsafe source id is rejected without rewriting` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `normalize_ign_electric_lines`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_line_cleabs_fails`

**Signature**

```python
def test_duplicate_line_cleabs_fails() -> None:
```

**Purpose**

Protects the `duplicate line cleabs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_line_source(geometries=[LineString([(0, 0), (10, 10)]), LineString([(20, 20), (30, 30)])], identifiers=['DUPLICATE', 'DUPLICATE'])`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='unique')` and executes: Calls `normalize_ign_electric_lines(source, _context(LINE_LAYER))` for its validation or side effect.

**Action**

- Calls `LineString`, `_context`, `_line_source`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='unique'): normalize_ign_electric_lines(source, _context(LINE_LAYER))`.

**Regression protected**

- Protects the exact `duplicate line cleabs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_missing_or_wrong_crs_fails`

**Signature**

```python
def test_line_missing_or_wrong_crs_fails(crs: str | None) -> None:
```

**Purpose**

Protects the `line missing or wrong crs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `crs`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='CRS|2154')` and executes: Calls `normalize_ign_electric_lines(_line_source(crs=crs), _context(LINE_LAYER))` for its validation or side effect.

**Action**

- Calls `_context`, `_line_source`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='CRS|2154'): normalize_ign_electric_lines(_line_source(crs=crs), _context(LINE_LAYER))`.

**Regression protected**

- Protects the exact `line missing or wrong crs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `normalize_ign_electric_lines`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_geometry_quality_is_preserved_without_row_loss_or_repair`

**Signature**

```python
def test_line_geometry_quality_is_preserved_without_row_loss_or_repair() -> None:
```

**Purpose**

Protects the `line geometry quality is preserved without row loss or repair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])`.
- Computes `source` from `_line_source(geometries=[LineString([(0, 0), (10, 10)]), None, LineString(), invalid], identifiers=['VALID', 'NULL', 'EMPTY', 'INVALID'], voltages=['63 kV'] * 4)`.
- Computes `normalized` from `normalize_ign_electric_lines(source, _context(LINE_LAYER))`.

**Action**

- Calls `LineString`, `Polygon`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `normalized.geometry.iloc[3].equals_exact`, `normalized['geometry_status'].tolist`, `normalized['source_feature_id'].tolist`.

**Expected result**

- Direct assertions: `assert normalized['geometry_status'].tolist() == ['VALID', 'NULL', 'EMPTY', 'INVALID']`; `assert normalized['source_feature_id'].tolist() == ['VALID', 'NULL', 'EMPTY', 'INVALID']`; `assert normalized.geometry.iloc[1] is None`; `assert normalized.geometry.iloc[2].is_empty`; `assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `line geometry quality is preserved without row loss or repair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Polygon`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `normalized.geometry.iloc[3].equals_exact`, `normalized['geometry_status'].tolist`, `normalized['source_feature_id'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_z_coordinates_are_preserved`

**Signature**

```python
def test_z_coordinates_are_preserved() -> None:
```

**Purpose**

Protects the `z coordinates are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_line_source(geometries=[LineString([(0, 0, 10), (10, 10, 20)])])`.
- Computes `normalized` from `normalize_ign_electric_lines(source, _context(LINE_LAYER))`.

**Action**

- Calls `LineString`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `normalized.geometry.iloc[0].equals_exact`.

**Expected result**

- Direct assertions: `assert source.geometry.iloc[0].has_z`; `assert normalized.geometry.iloc[0].has_z`; `assert normalized.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `z coordinates are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `normalized.geometry.iloc[0].equals_exact`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unusual_duplicate_source_index_is_not_preserved_as_identity`

**Signature**

```python
def test_unusual_duplicate_source_index_is_not_preserved_as_identity() -> None:
```

**Purpose**

Protects the `unusual duplicate source index is not preserved as identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_line_source(geometries=[LineString([(0, 0), (10, 10)]), LineString([(20, 20), (30, 30)])], identifiers=['FIRST', 'SECOND'], index=[77, 77])`.
- Computes `normalized` from `normalize_ign_electric_lines(source, _context(LINE_LAYER))`.

**Action**

- Calls `LineString`, `_context`, `_line_source`, `isinstance`, `normalize_ign_electric_lines`, `normalized.index.tolist`, `normalized['grid_feature_id'].tolist`, `normalized['source_feature_id'].tolist`.

**Expected result**

- Direct assertions: `assert isinstance(normalized.index, pd.RangeIndex)`; `assert normalized.index.tolist() == [0, 1]`; `assert normalized['source_feature_id'].tolist() == ['FIRST', 'SECOND']`; `assert normalized['grid_feature_id'].tolist() == ['IGN_BDTOPO:ELECTRIC_LINE:FIRST', 'IGN_BDTOPO:ELECTRIC_LINE:SECOND']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unusual duplicate source index is not preserved as identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_context`, `_line_source`, `isinstance`, `normalize_ign_electric_lines`, `normalized.index.tolist`, `normalized['grid_feature_id'].tolist`, `normalized['source_feature_id'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_line_normalization_does_not_mutate_input_and_has_stable_columns`

**Signature**

```python
def test_line_normalization_does_not_mutate_input_and_has_stable_columns() -> None:
```

**Purpose**

Protects the `line normalization does not mutate input and has stable columns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_line_source()`.
- Computes `reordered` from `source.loc[:, list(reversed(source.columns))].set_geometry('geometry')`.
- Computes `before` from `deepcopy(reordered)`.
- Computes `normalized` from `normalize_ign_electric_lines(reordered, _context(LINE_LAYER))`.

**Action**

- Calls `_context`, `_line_source`, `deepcopy`, `normalize_ign_electric_lines`, `reversed`, `source.loc[:, list(reversed(source.columns))].set_geometry`.

**Expected result**

- Direct assertions: `assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `line normalization does not mutate input and has stable columns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `assert_geodataframe_equal`, `deepcopy`, `list`, `normalize_ign_electric_lines`, `reversed`, `source.loc[:, list(reversed(source.columns))].set_geometry`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_required_line_field_fails`

**Signature**

```python
def test_missing_required_line_field_fails(column: str) -> None:
```

**Purpose**

Protects the `missing required line field fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_line_source().drop(columns=column)`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match=column)` and executes: Calls `normalize_ign_electric_lines(source, _context(LINE_LAYER))` for its validation or side effect.

**Action**

- Calls `_context`, `_line_source`, `_line_source().drop`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match=column): normalize_ign_electric_lines(source, _context(LINE_LAYER))`.

**Regression protected**

- Protects the exact `missing required line field fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `_line_source().drop`, `normalize_ign_electric_lines`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_or_null_line_precision_is_normalized_to_float`

**Signature**

```python
def test_valid_or_null_line_precision_is_normalized_to_float(
    precision: object,
) -> None:
```

**Purpose**

Protects the `valid or null line precision is normalized to float` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `precision`.
- Contains 1 explicit setup/context statement(s).
- Computes `normalized` from `normalize_ign_electric_lines(_line_source(precisions=[precision]), _context(LINE_LAYER))`.

**Action**

- Calls `_context`, `_line_source`, `float`, `isinstance`, `normalize_ign_electric_lines`, `np.isnan`, `pd.isna`.

**Expected result**

- Direct assertions: `assert str(normalized['planimetric_precision_m'].dtype) == 'float64'`; `assert pd.isna(normalized.iloc[0]['planimetric_precision_m'])`; `assert normalized.iloc[0]['planimetric_precision_m'] == float(precision)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid or null line precision is normalized to float` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `float`, `isinstance`, `normalize_ign_electric_lines`, `np.isnan`, `pd.isna`, `pytest.mark.parametrize`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_line_precision_fails`

**Signature**

```python
def test_invalid_line_precision_fails(precision: object) -> None:
```

**Purpose**

Protects the `invalid line precision fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `precision`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='precision_planimetrique')` and executes: Calls `normalize_ign_electric_lines(_line_source(precisions=[precision]), _context(LINE_LAYER))` for its validation or side effect.

**Action**

- Calls `_context`, `_line_source`, `float`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='precision_planimetrique'): normalize_ign_electric_lines(_line_source(precisions=[precision]), _context(LINE_LAYER))`.

**Regression protected**

- Protects the exact `invalid line precision fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_line_source`, `float`, `normalize_ign_electric_lines`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normalized_voltage_never_emits_non_finite_numeric_values`

**Signature**

```python
def test_normalized_voltage_never_emits_non_finite_numeric_values() -> None:
```

**Purpose**

Protects the `normalized voltage never emits non finite numeric values` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `huge` from `f"{'9' * 400} kV"`.
- Computes `source` from `_line_source(geometries=[LineString([(0, 0), (1, 1)])] * 4, identifiers=['EXACT', 'BELOW', 'OVERFLOW', 'MISSING'], voltages=['225 kV', '<90 kV', huge, None])`.
- Computes `normalized` from `normalize_ign_electric_lines(source, _context(LINE_LAYER))`.

**Action**

- Calls `LineString`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `normalized['voltage_kv'].dropna`, `normalized['voltage_status'].tolist`, `normalized['voltage_upper_bound_kv'].dropna`, `np.isfinite`, `np.isfinite(normalized['voltage_kv'].dropna()).all`, `np.isfinite(normalized['voltage_upper_bound_kv'].dropna()).all`.

**Expected result**

- Direct assertions: `assert normalized['voltage_status'].tolist() == ['EXACT', 'BELOW', 'UNPARSED', 'UNKNOWN']`; `assert np.isfinite(normalized['voltage_kv'].dropna()).all()`; `assert np.isfinite(normalized['voltage_upper_bound_kv'].dropna()).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `normalized voltage never emits non finite numeric values` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `normalized['voltage_kv'].dropna`, `normalized['voltage_status'].tolist`, `normalized['voltage_upper_bound_kv'].dropna`, `np.isfinite`, `np.isfinite(normalized['voltage_kv'].dropna()).all`, `np.isfinite(normalized['voltage_upper_bound_kv'].dropna()).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_post_has_stable_lineage_and_no_voltage_inference`

**Signature**

```python
def test_valid_post_has_stable_lineage_and_no_voltage_inference() -> None:
```

**Purpose**

Protects the `valid post has stable lineage and no voltage inference` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_post_source()`.
- Computes `normalized` from `normalize_ign_transformation_posts(source, _context(POST_LAYER))`.
- Computes `row` from `normalized.iloc[0]`.

**Action**

- Calls `_context`, `_post_source`, `isinstance`, `normalize_ign_transformation_posts`, `pd.isna`.

**Expected result**

- Direct assertions: `assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)`; `assert isinstance(normalized.index, pd.RangeIndex)`; `assert row['grid_feature_id'] == 'IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1'`; `assert row['source_layer'] == POST_LAYER`; `assert row['source_department_code'] == '31'`; `assert row['source_archive_sha256'] == ARCHIVE_SHA256`; `assert row['name'] == 'Poste de test'`; `assert row['voltage_status'] == 'UNKNOWN'`; `assert pd.isna(row['voltage_kv'])`; `assert row['spatial_role'] == 'PROXY_GEOMETRY'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid post has stable lineage and no voltage inference` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_post_source`, `isinstance`, `list`, `normalize_ign_transformation_posts`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_post_geometry_crs_and_input_are_preserved`

**Signature**

```python
def test_post_geometry_crs_and_input_are_preserved() -> None:
```

**Purpose**

Protects the `post geometry crs and input are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_post_source()`.
- Computes `before` from `deepcopy(source)`.
- Computes `normalized` from `normalize_ign_transformation_posts(source, _context(POST_LAYER))`.

**Action**

- Calls `_context`, `_post_source`, `deepcopy`, `normalize_ign_transformation_posts`, `normalized.crs.to_epsg`, `normalized.geometry.iloc[0].equals_exact`.

**Expected result**

- Direct assertions: `assert normalized.crs is not None and normalized.crs.to_epsg() == 2154`; `assert normalized.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `post geometry crs and input are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_post_source`, `assert_geodataframe_equal`, `deepcopy`, `normalize_ign_transformation_posts`, `normalized.crs.to_epsg`, `normalized.geometry.iloc[0].equals_exact`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_post_cleabs_fails`

**Signature**

```python
def test_duplicate_post_cleabs_fails() -> None:
```

**Purpose**

Protects the `duplicate post cleabs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `polygon` from `Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])`.
- Computes `source` from `_post_source(geometries=[polygon, polygon], identifiers=['DUPLICATE', 'DUPLICATE'])`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='unique')` and executes: Calls `normalize_ign_transformation_posts(source, _context(POST_LAYER))` for its validation or side effect.

**Action**

- Calls `Polygon`, `_context`, `_post_source`, `normalize_ign_transformation_posts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='unique'): normalize_ign_transformation_posts(source, _context(POST_LAYER))`.

**Regression protected**

- Protects the exact `duplicate post cleabs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_context`, `_post_source`, `normalize_ign_transformation_posts`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_post_geometry_and_precision_are_preserved`

**Signature**

```python
def test_null_post_geometry_and_precision_are_preserved() -> None:
```

**Purpose**

Protects the `null post geometry and precision are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `normalized` from `normalize_ign_transformation_posts(_post_source(geometries=[None], precisions=[None]), _context(POST_LAYER))`.

**Action**

- Calls `_context`, `_post_source`, `normalize_ign_transformation_posts`, `normalized['planimetric_precision_m'].isna`, `normalized['planimetric_precision_m'].isna().all`, `normalized['voltage_kv'].isna`, `normalized['voltage_kv'].isna().all`.

**Expected result**

- Direct assertions: `assert normalized.iloc[0]['geometry_status'] == 'NULL'`; `assert normalized.geometry.iloc[0] is None`; `assert normalized.iloc[0]['voltage_status'] == 'UNKNOWN'`; `assert normalized['voltage_kv'].isna().all()`; `assert normalized['planimetric_precision_m'].isna().all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `null post geometry and precision are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_post_source`, `normalize_ign_transformation_posts`, `normalized['planimetric_precision_m'].isna`, `normalized['planimetric_precision_m'].isna().all`, `normalized['voltage_kv'].isna`, `normalized['voltage_kv'].isna().all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_post_precision_fails`

**Signature**

```python
def test_invalid_post_precision_fails() -> None:
```

**Purpose**

Protects the `invalid post precision fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='precision_planimetrique')` and executes: Calls `normalize_ign_transformation_posts(_post_source(precisions=['5.0']), _context(POST_LAYER))` for its validation or side effect.

**Action**

- Calls `_context`, `_post_source`, `normalize_ign_transformation_posts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='precision_planimetrique'): normalize_ign_transformation_posts(_post_source(precisions=['5.0']), _context(POST_LAYER))`.

**Regression protected**

- Protects the exact `invalid post precision fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_context`, `_post_source`, `normalize_ign_transformation_posts`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_appropriate_multigeometry_types_are_accepted`

**Signature**

```python
def test_appropriate_multigeometry_types_are_accepted() -> None:
```

**Purpose**

Protects the `appropriate multigeometry types are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `multilines` from `MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])`.
- Computes `multipolygon` from `MultiPolygon([Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]), Polygon([(10, 10), (10, 15), (15, 15), (15, 10), (10, 10)])])`.
- Computes `lines` from `normalize_ign_electric_lines(_line_source(geometries=[multilines]), _context(LINE_LAYER))`.
- Computes `posts` from `normalize_ign_transformation_posts(_post_source(geometries=[multipolygon]), _context(POST_LAYER))`.

**Action**

- Calls `MultiLineString`, `MultiPolygon`, `Polygon`, `_context`, `_line_source`, `_post_source`, `normalize_ign_electric_lines`, `normalize_ign_transformation_posts`.

**Expected result**

- Direct assertions: `assert lines.iloc[0]['geometry_status'] == 'VALID'`; `assert lines.geometry.iloc[0].geom_type == 'MultiLineString'`; `assert posts.iloc[0]['geometry_status'] == 'VALID'`; `assert posts.geometry.iloc[0].geom_type == 'MultiPolygon'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `appropriate multigeometry types are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiLineString`, `MultiPolygon`, `Polygon`, `_context`, `_line_source`, `_post_source`, `normalize_ign_electric_lines`, `normalize_ign_transformation_posts`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_polygon_or_point_is_rejected_as_electric_line`

**Signature**

```python
def test_valid_polygon_or_point_is_rejected_as_electric_line(
    geometry: object,
) -> None:
```

**Purpose**

Protects the `valid polygon or point is rejected as electric line` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='geometry types')` and executes: Calls `normalize_ign_electric_lines(_line_source(geometries=[geometry]), _context(LINE_LAYER))` for its validation or side effect.

**Action**

- Calls `Point`, `Polygon`, `_context`, `_line_source`, `normalize_ign_electric_lines`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='geometry types'): normalize_ign_electric_lines(_line_source(geometries=[geometry]), _context(LINE_LAYER))`.

**Regression protected**

- Protects the exact `valid polygon or point is rejected as electric line` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `Polygon`, `_context`, `_line_source`, `normalize_ign_electric_lines`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_line_or_point_is_rejected_as_transformation_post`

**Signature**

```python
def test_valid_line_or_point_is_rejected_as_transformation_post(
    geometry: object,
) -> None:
```

**Purpose**

Protects the `valid line or point is rejected as transformation post` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='geometry types')` and executes: Calls `normalize_ign_transformation_posts(_post_source(geometries=[geometry]), _context(POST_LAYER))` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `_context`, `_post_source`, `normalize_ign_transformation_posts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='geometry types'): normalize_ign_transformation_posts(_post_source(geometries=[geometry]), _context(POST_LAYER))`.

**Regression protected**

- Protects the exact `valid line or point is rejected as transformation post` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `_context`, `_post_source`, `normalize_ign_transformation_posts`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_path_uses_discovered_layer_names_and_archive_lineage`

**Signature**

```python
def test_high_level_path_uses_discovered_layer_names_and_archive_lineage() -> None:
```

**Purpose**

Protects the `high level path uses discovered layer names and archive lineage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `normalized` from `normalize_ign_electricity(source)`.

**Action**

- Calls `_source_bundle`, `frame['source_archive_sha256'].unique`, `frame['source_archive_sha256'].unique().tolist`, `frame['source_department_code'].unique`, `frame['source_department_code'].unique().tolist`, `frame['source_edition'].unique`, `frame['source_edition'].unique().tolist`, `frame['source_product_version'].unique`, `frame['source_product_version'].unique().tolist`, `frame['source_url'].unique`, `frame['source_url'].unique().tolist`, `normalize_ign_electricity`, `normalized.electric_lines['source_layer'].unique`, `normalized.electric_lines['source_layer'].unique().tolist`, `normalized.transformation_posts['source_layer'].unique`, `normalized.transformation_posts['source_layer'].unique().tolist`.

**Expected result**

- Direct assertions: `assert normalized.electric_lines['source_layer'].unique().tolist() == [LINE_LAYER]`; `assert normalized.transformation_posts['source_layer'].unique().tolist() == [POST_LAYER]`; `assert frame['source_department_code'].unique().tolist() == ['31']`; `assert frame['source_edition'].unique().tolist() == ['2026-06-15']`; `assert frame['source_product_version'].unique().tolist() == ['3.5']`; `assert frame['source_archive_sha256'].unique().tolist() == [ARCHIVE_SHA256]`; `assert frame['source_url'].unique().tolist() == [SOURCE_URL]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `high level path uses discovered layer names and archive lineage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `frame['source_archive_sha256'].unique`, `frame['source_archive_sha256'].unique().tolist`, `frame['source_department_code'].unique`, `frame['source_department_code'].unique().tolist`, `frame['source_edition'].unique`, `frame['source_edition'].unique().tolist`, `frame['source_product_version'].unique`, `frame['source_product_version'].unique().tolist`, `frame['source_url'].unique`, `frame['source_url'].unique().tolist`, `normalize_ign_electricity`, `normalized.electric_lines['source_layer'].unique`, `normalized.electric_lines['source_layer'].unique().tolist`, `normalized.transformation_posts['source_layer'].unique`, `normalized.transformation_posts['source_layer'].unique().tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_coordinated_frame_and_summary_forgery`

**Signature**

```python
def test_high_level_rejects_coordinated_frame_and_summary_forgery() -> None:
```

**Purpose**

Protects the `high level rejects coordinated frame and summary forgery` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `forged` from `source.electric_lines.copy()`.
- Computes `forged.loc[0, 'voltage']` from `'400 kV'`.
- Computes `forged_summary` from `_summary(forged, 'electric_lines', LINE_LAYER)`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='physical|fresh|source')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines=forged, electric_lines_summary=forged_summary))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `_summary`, `normalize_ign_electricity`, `replace`, `source.electric_lines.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='physical|fresh|source'): normalize_ign_electricity(replace(source, electric_lines=forged, electric_lines_summary=forged_summary))`.

**Regression protected**

- Protects the exact `high level rejects coordinated frame and summary forgery` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `_summary`, `normalize_ign_electricity`, `pytest.raises`, `replace`, `source.electric_lines.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_grid_validation_does_not_mutate_supplied_frames`

**Signature**

```python
def test_source_complete_grid_validation_does_not_mutate_supplied_frames() -> None:
```

**Purpose**

Protects the `source complete grid validation does not mutate supplied frames` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `lines_before` from `deepcopy(source.electric_lines)`.
- Computes `posts_before` from `deepcopy(source.transformation_posts)`.

**Action**

- Calls `_source_bundle`, `deepcopy`, `normalize_ign_electricity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source complete grid validation does not mutate supplied frames` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `assert_geodataframe_equal`, `deepcopy`, `normalize_ign_electricity`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_incompatible_archive_identity`

**Signature**

```python
def test_high_level_rejects_incompatible_archive_identity(
    field: str,
    value: str,
    message: str,
) -> None:
```

**Purpose**

Protects the `high level rejects incompatible archive identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`, `message`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_bundle_with_archive(**{field: value})`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match=message)` and executes: Calls `normalize_ign_electricity(source)` for its validation or side effect.

**Action**

- Calls `_source_bundle_with_archive`, `normalize_ign_electricity`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match=message): normalize_ign_electricity(source)`.

**Regression protected**

- Protects the exact `high level rejects incompatible archive identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle_with_archive`, `normalize_ign_electricity`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant`

**Signature**

```python
def test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant() -> None:
```

**Purpose**

Protects the `archive identity comparison is case accent and punctuation tolerant` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `provider` from `"INSTITUT NATIONAL DE L'INFORMATION GEOGRAPHIQUE ET FORESTIERE (ign)"`.
- Computes `product` from `'bd-topo'`.
- Computes `source` from `_source_bundle_with_archive(provider=provider, product=product)`.
- Computes `config_payload` from `SOURCE_CONFIG.model_dump(mode='json')`.
- Computes `matching_config` from `IgnBdTopoSourceConfig.model_validate(config_payload)`.
- Computes `normalized` from `_normalize_ign_electricity(source, matching_config)`.

**Action**

- Calls `IgnBdTopoSourceConfig.model_validate`, `SOURCE_CONFIG.model_dump`, `_normalize_ign_electricity`, `_source_bundle_with_archive`, `config_payload.update`.

**Expected result**

- Direct assertions: `assert len(normalized.electric_lines) == 1`; `assert len(normalized.transformation_posts) == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `archive identity comparison is case accent and punctuation tolerant` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `SOURCE_CONFIG.model_dump`, `_normalize_ign_electricity`, `_source_bundle_with_archive`, `config_payload.update`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_summary_row_count_mismatch`

**Signature**

```python
def test_high_level_rejects_summary_row_count_mismatch() -> None:
```

**Purpose**

Protects the `high level rejects summary row count mismatch` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `summary` from `replace(source.electric_lines_summary, feature_count=source.electric_lines_summary.feature_count + 1)`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='row count')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines_summary=summary))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='row count'): normalize_ign_electricity(replace(source, electric_lines_summary=summary))`.

**Regression protected**

- Protects the exact `high level rejects summary row count mismatch` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalize_ign_electricity`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_summary_layer_name_mismatch`

**Signature**

```python
def test_high_level_rejects_summary_layer_name_mismatch() -> None:
```

**Purpose**

Protects the `high level rejects summary layer name mismatch` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `summary` from `replace(source.electric_lines_summary, source_layer_name='WRONG')`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='summary layer')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines_summary=summary))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='summary layer'): normalize_ign_electricity(replace(source, electric_lines_summary=summary))`.

**Regression protected**

- Protects the exact `high level rejects summary layer name mismatch` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalize_ign_electricity`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_wrong_logical_name`

**Signature**

```python
def test_high_level_rejects_wrong_logical_name() -> None:
```

**Purpose**

Protects the `high level rejects wrong logical name` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `summary` from `replace(source.electric_lines_summary, logical_name=cast(Any, 'transformation_posts'))`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='logical name')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines_summary=summary))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `cast`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='logical name'): normalize_ign_electricity(replace(source, electric_lines_summary=summary))`.

**Regression protected**

- Protects the exact `high level rejects wrong logical name` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `cast`, `normalize_ign_electricity`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_summary_crs_mismatch`

**Signature**

```python
def test_high_level_rejects_summary_crs_mismatch() -> None:
```

**Purpose**

Protects the `high level rejects summary crs mismatch` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `summary` from `replace(source.electric_lines_summary, crs='EPSG:4326')`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='CRS|2154')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines_summary=summary))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='CRS|2154'): normalize_ign_electricity(replace(source, electric_lines_summary=summary))`.

**Regression protected**

- Protects the exact `high level rejects summary crs mismatch` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalize_ign_electricity`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_forged_ordered_summary_schema`

**Signature**

```python
def test_high_level_rejects_forged_ordered_summary_schema(mutation: str) -> None:
```

**Purpose**

Protects the `high level rejects forged ordered summary schema` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `summary` from `source.electric_lines_summary`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='schema|columns|dtype')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines_summary=changed))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`, `reversed`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='schema|columns|dtype'): normalize_ign_electricity(replace(source, electric_lines_summary=changed))`.

**Regression protected**

- Protects the exact `high level rejects forged ordered summary schema` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `list`, `normalize_ign_electricity`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `reversed`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_duplicate_or_missing_layer_inventory`

**Signature**

```python
def test_high_level_rejects_duplicate_or_missing_layer_inventory() -> None:
```

**Purpose**

Protects the `high level rejects duplicate or missing layer inventory` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `duplicate` from `replace(source, extraction=replace(source.extraction, all_layer_names=(LINE_LAYER, POST_LAYER, LINE_LAYER)))`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='inventory|duplicate')` and executes: Calls `normalize_ign_electricity(duplicate)` for its validation or side effect.
- Computes `missing` from `replace(source, extraction=replace(source.extraction, all_layer_names=(POST_LAYER,)))`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='inventory|selected')` and executes: Calls `normalize_ign_electricity(missing)` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='inventory|duplicate'): normalize_ign_electricity(duplicate)`; `with pytest.raises(IgnGridNormalizationError, match='inventory|selected'): normalize_ign_electricity(missing)`.

**Regression protected**

- Protects the exact `high level rejects duplicate or missing layer inventory` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalize_ign_electricity`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_colliding_electricity_roles`

**Signature**

```python
def test_high_level_rejects_colliding_electricity_roles() -> None:
```

**Purpose**

Protects the `high level rejects colliding electricity roles` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `extraction` from `replace(source.extraction, transformation_posts_layer=LINE_LAYER)`.
- Computes `post_summary` from `replace(source.transformation_posts_summary, source_layer_name=LINE_LAYER)`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='same layer|distinct|role')` and executes: Calls `normalize_ign_electricity(replace(source, extraction=extraction, transformation_posts_summary=post_summary))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='same layer|distinct|role'): normalize_ign_electricity(replace(source, extraction=extraction, transformation_posts_summary=post_summary))`.

**Regression protected**

- Protects the exact `high level rejects colliding electricity roles` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalize_ign_electricity`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_stale_geometry_counts_after_frame_mutation`

**Signature**

```python
def test_high_level_rejects_stale_geometry_counts_after_frame_mutation() -> None:
```

**Purpose**

Protects the `high level rejects stale geometry counts after frame mutation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `mutated` from `source.electric_lines.copy()`.
- Computes `mutated.at[mutated.index[0], 'geometry']` from `None`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='geometry summary')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines=mutated))` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `normalize_ign_electricity`, `replace`, `source.electric_lines.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='geometry summary'): normalize_ign_electricity(replace(source, electric_lines=mutated))`.

**Regression protected**

- Protects the exact `high level rejects stale geometry counts after frame mutation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `normalize_ign_electricity`, `pytest.raises`, `replace`, `source.electric_lines.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_stale_geometry_types_after_frame_mutation`

**Signature**

```python
def test_high_level_rejects_stale_geometry_types_after_frame_mutation() -> None:
```

**Purpose**

Protects the `high level rejects stale geometry types after frame mutation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `mutated` from `source.electric_lines.copy()`.
- Computes `mutated.at[mutated.index[0], 'geometry']` from `MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='geometry summary')` and executes: Calls `normalize_ign_electricity(replace(source, electric_lines=mutated))` for its validation or side effect.

**Action**

- Calls `MultiLineString`, `_source_bundle`, `normalize_ign_electricity`, `replace`, `source.electric_lines.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='geometry summary'): normalize_ign_electricity(replace(source, electric_lines=mutated))`.

**Regression protected**

- Protects the exact `high level rejects stale geometry types after frame mutation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiLineString`, `_source_bundle`, `normalize_ign_electricity`, `pytest.raises`, `replace`, `source.electric_lines.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_any_spatial_role_mismatch`

**Signature**

```python
def test_high_level_rejects_any_spatial_role_mismatch(component: str) -> None:
```

**Purpose**

Protects the `high level rejects any spatial role mismatch` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `component`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_bundle()`.
- Computes `wrong_role` from `cast(Any, 'EXACT_RTE_GEOMETRY')`.
- Enters managed context(s) `pytest.raises(IgnGridNormalizationError, match='PROXY_GEOMETRY')` and executes: Calls `normalize_ign_electricity(inconsistent)` for its validation or side effect.

**Action**

- Calls `_source_bundle`, `cast`, `normalize_ign_electricity`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnGridNormalizationError, match='PROXY_GEOMETRY'): normalize_ign_electricity(inconsistent)`.

**Regression protected**

- Protects the exact `high level rejects any spatial role mismatch` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_bundle`, `cast`, `normalize_ign_electricity`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `cleabs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `date_creation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `date_de_confirmation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `date_modification` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `electric_lines` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `etat_de_l_objet` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `gestionnaire` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `identifiants_sources` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `manager_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `methode_d_acquisition_planimetrique` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planimetric_precision_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `precision_planimetrique` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `siren_gestionnaire` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identifiers_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sources` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `statut_du_toponyme` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `toponyme` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `transformation_posts` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_upper_bound_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
