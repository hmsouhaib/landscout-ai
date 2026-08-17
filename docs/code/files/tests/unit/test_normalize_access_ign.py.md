# `tests/unit/test_normalize_access_ign.py`

## File identity

- Repository path: `tests/unit/test_normalize_access_ign.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `ed8a0fa4513e82eef5c9192b53c9f47fc32c3fc64ba3d5b7d85f1b94ab7da15c`

## 1. Purpose

Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

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
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `from uuid import uuid4` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pyogrio` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import LineString, MultiLineString, Point, Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoDownload, IgnBdTopoExtraction, IgnBdTopoLayerSummary, IgnBdTopoRoadData, IgnBdTopoSourceConfig, load_ign_bdtopo_roads, load_ign_bdtopo_source_config, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_access_ign import ( IgnRoadNormalizationError, NormalizedIgnRoadData, normalize_ign_roads, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `ROAD_LAYER` | `"troncon_de_route"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALTERNATE_ROAD_LAYER` | `"voie_secondaire"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_SHA256` | `"a" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_URL` | `"https://example.test/BDTOPO_D031.7z"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_FIXTURE_ROOT` | `Path(tempfile.mkdtemp(prefix="landscout-road-ign-"))` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_CONFIG` | `load_ign_bdtopo_source_config()` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OUTPUT_COLUMNS` | `( "road_feature_id", "road_feature_type", "source_provider", "source_product", "source_layer", "source_feature_id", "source_department_code", "source_edition", "source_product_version", "source_download_timestamp", "source_archive_sha256", "source_url", "nature_raw", "importance_raw", "fictitious_raw", "position_relative_to_ground_raw", "asset_status_raw", "lane_count_raw", "carriageway_width_raw", "private_raw", "traffic_direction_raw", "urban_raw", "mean_light_vehicle_speed_raw", "light_vehicle_access_raw", "closure_period_raw", "restriction_nature_raw", "restriction_height_raw", "restriction_total_weight_raw", "restriction_axle_weight_raw", "restriction_width_raw", "restriction_length_raw", "dangerous_goods_forbidden_raw", "administrative_classification_raw", "manager_raw", "source_name_raw", "source_identifiers_raw", "source_created_at", "source_modified_at", "source_confirmed_at", "planimetric_acquisition_method", "planimetric_precision_raw", "spatial_role", "geometry_status", "geometry", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RAW_FIELD_MAPPING` | `( ("nature", "nature_raw"), ("importance", "importance_raw"), ("fictif", "fictitious_raw"), ("position_par_rapport_au_sol", "position_relative_to_ground_raw"), ("etat_de_l_objet", "asset_status_raw"), ("nombre_de_voies", "lane_count_raw"), ("largeur_de_chaussee", "carriageway_width_raw"), ("prive", "private_raw"), ("sens_de_circulation", "traffic_direction_raw"), ("urbain", "urban_raw"), ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"), ("acces_vehicule_leger", "light_vehicle_access_raw"), ("periode_de_fermeture", "closure_period_raw"), ("nature_de_la_restriction", "restriction_nature_raw"), ("restriction_de_hauteur", "restriction_height_raw"), ("restriction_de_poids_total", "restriction_total_weight_raw"), ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"), ("restriction_de_largeur", "restriction_width_raw"), ("restriction_de_longueur", "restriction_length_raw"), ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"), ("cpx_classement_administratif", "administrative_classification_raw"), ("cpx_gestionnaire", "manager_raw"), ("sources", "source_name_raw"), ("identifiants_sources", "source_identifiers_raw"), ("date_creation", "source_created_at"), ("date_modification", "source_modified_at"), ("date_de_confirmation", "source_confirmed_at"), ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"), ("precision_planimetrique", "planimetric_precision_raw"), )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_road_frame`

**Signature**

```python
def _road_frame(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements road frame according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `identifiers` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `index` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame(values, geometry=source_geometries, crs=crs, index=source_index)`.

**Algorithm**

1. Computes `source_geometries` from `geometries or [LineString([(0, 0), (100, 100)])]`.
2. Computes `count` from `len(source_geometries)`.
3. Computes `source_ids` from `identifiers or [f'ROAD-{number + 1}' for number in range(count)]`.
4. Computes `source_index` from `index or [100 + number for number in range(count)]`.
5. Defines `values` with annotation `dict[str, list[object]]` from `{'cleabs': source_ids, 'nature': ['Route à 1 chaussée'] * count, 'importance': ['2'] * count, 'fictif': ['Non'] * count, 'position_par_rapport_au_sol': [-1] * count, 'etat_de_l_objet': ['En service'] * count, 'nombre_de_voies': [2] * count, 'largeur_de_chaussee': [7.5] * count, 'prive': ['Non'] * count, 'sens_de_circu…`.
6. Returns `gpd.GeoDataFrame(values, geometry=source_geometries, crs=crs, index=source_index)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `gpd.GeoDataFrame`, `len`, `pd.Timestamp`, `range`.

**Known repository callers**

- `tests/unit/test_normalize_access_ign.py` — `_source`
- `tests/unit/test_normalize_access_ign.py` — `_with_alternate_road_layer`
- `tests/unit/test_normalize_access_ign.py` — `test_duplicate_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_null_empty_and_invalid_geometry_are_preserved_with_status`
- `tests/unit/test_normalize_access_ign.py` — `test_null_or_empty_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_raw_access_and_restriction_values_are_copied_without_interpretation`
- `tests/unit/test_normalize_access_ign.py` — `test_row_count_order_geometry_and_range_index_are_preserved`
- `tests/unit/test_normalize_access_ign.py` — `test_unsafe_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_multilinestring_is_preserved`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_unsupported_geometry_type_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_wrong_or_missing_road_crs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_z_coordinates_are_preserved_exactly`

**Tests**

- `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_null_empty_and_invalid_geometry_are_preserved_with_status`
- `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_raw_access_and_restriction_values_are_copied_without_interpretation`
- `tests/unit/test_normalize_access_ign.py::test_row_count_order_geometry_and_range_index_are_preserved`
- `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_valid_multilinestring_is_preserved`
- `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_z_coordinates_are_preserved_exactly`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_summary`

**Signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    layer: str = ROAD_LAYER,
) -> IgnBdTopoLayerSummary:
```

**Purpose**

Implements summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer` (`str`; optional/default `ROAD_LAYER`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoLayerSummary`. Observed return expression(s): `IgnBdTopoLayerSummary(logical_name='road_segments', source_layer_name=layer, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), invalid_geometry_count=int(invalid_mask.sum()),…`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Returns `IgnBdTopoLayerSummary(logical_name='road_segments', source_layer_name=layer, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), invalid…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerSummary`, `empty_mask.sum`, `frame.dtypes.items`, `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`, `int`, `invalid_mask.sum`, `len`, `null_mask.sum`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_normalize_access_ign.py` — `_source`
- `tests/unit/test_normalize_access_ign.py` — `test_high_level_rejects_coordinated_road_frame_and_summary_forgery`

**Tests**

- `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source`

**Signature**

```python
def _source(frame: gpd.GeoDataFrame | None = None) -> IgnBdTopoRoadData:
```

**Purpose**

Implements source according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoRoadData`. Observed return expression(s): `IgnBdTopoRoadData(extraction=extraction, road_segments=road_frame, road_segments_summary=_summary(road_frame))`.

**Algorithm**

1. Computes `road_frame` from `frame if frame is not None else _road_frame()`.
2. Computes `extraction_path` from `_FIXTURE_ROOT / uuid4().hex`.
3. Calls `extraction_path.mkdir(parents=True)` for its validation or side effect.
4. Computes `geopackage_path` from `extraction_path / 'data.gpkg'`.
5. Computes `crs` from `road_frame.crs or 'EPSG:2154'`.
6. Computes `dummy` from `gpd.GeoDataFrame({'id': ['dummy']}, geometry=[LineString([(0, 0), (1, 1)])], crs=crs)`.
7. Calls `pyogrio.write_dataframe(dummy, geopackage_path, layer='ligne_electrique', driver='GPKG')` for its validation or side effect.
8. Calls `pyogrio.write_dataframe(dummy, geopackage_path, layer='poste_de_transformation', driver='GPKG', append=True)` for its validation or side effect.
9. Calls `pyogrio.write_dataframe(road_frame, geopackage_path, layer=ROAD_LAYER, driver='GPKG', append=True)` for its validation or side effect.
10. Computes `road_frame` from `gpd.read_file(geopackage_path, layer=ROAD_LAYER, engine='pyogrio')`.
11. Computes `payload` from `geopackage_path.read_bytes()`.
12. Computes `layer_names` from `tuple((str(row[0]) for row in pyogrio.list_layers(geopackage_path)))`.
13. Computes `digest` from `sha256(payload).hexdigest()`.
14. Calls `(extraction_path / '.landscout-extraction.json').write_text(json.dumps({'schema_version': 2, 'archive_sha256': ARCHIVE_SHA256, 'geopackage_relative_path': 'data.gpkg', 'geopackage_size_bytes': len(payload), 'geopackage_sha256': digest, 'all_layer_names': list(layer_names), 'electric_lines_layer': 'ligne_electrique', 'transformation_posts_layer': 'poste_de_t…` for its validation or side effect.
15. Computes `archive` from `IgnBdTopoDownload(provider='IGN', product='BD TOPO', department_code='31', edition='2026-06-15', product_version='3.5', projection='EPSG:2154', package_format='GPKG', archive_format='7z', source_url=SOURCE_URL, checksum_url=None, download_timestamp='2026-08-11T15:32:03+00:00', filename='BDTOPO_D031.7z', file_size=1234…`.
16. Computes `extraction` from `IgnBdTopoExtraction(archive=archive, extraction_path=extraction_path, geopackage_path=geopackage_path, geopackage_filename='data.gpkg', geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=layer_names, electric_lines_layer='ligne_electrique', transformation_posts_layer='poste_de_transformation…`.
17. Returns `IgnBdTopoRoadData(extraction=extraction, road_segments=road_frame, road_segments_summary=_summary(road_frame))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(extraction_path / '.landscout-extraction.json').write_text`, `IgnBdTopoDownload`, `extraction_path.mkdir`, `geopackage_path.read_bytes`, `gpd.read_file`, `pyogrio.write_dataframe`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(extraction_path / '.landscout-extraction.json').write_text`, `IgnBdTopoDownload`, `IgnBdTopoExtraction`, `IgnBdTopoRoadData`, `LineString`, `Path`, `_road_frame`, `_summary`, `extraction_path.mkdir`, `geopackage_path.read_bytes`, `gpd.GeoDataFrame`, `gpd.read_file`, `json.dumps`, `len`, `list`, `pyogrio.list_layers`, `pyogrio.write_dataframe`, `sha256`, `sha256(payload).hexdigest`, `str`, `tuple`, `uuid4`.

**Known repository callers**

- `tests/unit/test_normalize_access_ign.py` — `test_duplicate_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_every_raw_field_preserves_source_values_nulls_and_dtype`
- `tests/unit/test_normalize_access_ign.py` — `test_forged_ordered_summary_schema_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_high_level_rejects_coordinated_road_frame_and_summary_forgery`
- `tests/unit/test_normalize_access_ign.py` — `test_missing_required_source_field_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_access_ign.py` — `test_null_empty_and_invalid_geometry_are_preserved_with_status`
- `tests/unit/test_normalize_access_ign.py` — `test_null_or_empty_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_raw_access_and_restriction_values_are_copied_without_interpretation`
- `tests/unit/test_normalize_access_ign.py` — `test_road_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_access_ign.py` — `test_road_normalization_reproduces_configured_logical_layer`
- `tests/unit/test_normalize_access_ign.py` — `test_road_source_rejects_duplicate_layer_inventory`
- `tests/unit/test_normalize_access_ign.py` — `test_road_source_rejects_physical_role_collision`
- `tests/unit/test_normalize_access_ign.py` — `test_road_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_access_ign.py` — `test_row_count_order_geometry_and_range_index_are_preserved`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_crs_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_geometry_facts_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_layer_and_logical_name_must_be_exact`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_layer_must_exist_in_extraction_inventory`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_row_count_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_unsafe_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_linestring_normalization_has_exact_schema_identity_and_lineage`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_multilinestring_is_preserved`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_unsupported_geometry_type_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_wrong_archive_identity_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_wrong_or_missing_road_crs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_wrong_source_spatial_role_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_z_coordinates_are_preserved_exactly`

**Tests**

- `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_every_raw_field_preserves_source_values_nulls_and_dtype`
- `tests/unit/test_normalize_access_ign.py::test_forged_ordered_summary_schema_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery`
- `tests/unit/test_normalize_access_ign.py::test_missing_required_source_field_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_access_ign.py::test_null_empty_and_invalid_geometry_are_preserved_with_status`
- `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_raw_access_and_restriction_values_are_copied_without_interpretation`
- `tests/unit/test_normalize_access_ign.py::test_road_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer`
- `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_duplicate_layer_inventory`
- `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_physical_role_collision`
- `tests/unit/test_normalize_access_ign.py::test_road_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_access_ign.py::test_row_count_order_geometry_and_range_index_are_preserved`
- `tests/unit/test_normalize_access_ign.py::test_summary_crs_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_summary_geometry_facts_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_summary_layer_and_logical_name_must_be_exact`
- `tests/unit/test_normalize_access_ign.py::test_summary_layer_must_exist_in_extraction_inventory`
- `tests/unit/test_normalize_access_ign.py::test_summary_row_count_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage`
- `tests/unit/test_normalize_access_ign.py::test_valid_multilinestring_is_preserved`
- `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_wrong_archive_identity_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_wrong_source_spatial_role_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_z_coordinates_are_preserved_exactly`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_with_alternate_road_layer`

**Signature**

```python
def _with_alternate_road_layer(
    source: IgnBdTopoRoadData,
) -> tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]:
```

**Purpose**

Implements with alternate road layer according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]`. Observed return expression(s): `(configured, forged)`.

**Algorithm**

1. Computes `alternate` from `_road_frame([LineString([(500, 500), (600, 600)])], identifiers=['ALTERNATE-ROAD'])`.
2. Computes `geopackage_path` from `source.extraction.geopackage_path`.
3. Calls `pyogrio.write_dataframe(alternate, geopackage_path, layer=ALTERNATE_ROAD_LAYER, driver='GPKG', append=True)` for its validation or side effect.
4. Computes `payload` from `geopackage_path.read_bytes()`.
5. Computes `layer_names` from `tuple((str(row[0]) for row in pyogrio.list_layers(geopackage_path)))`.
6. Computes `digest` from `sha256(payload).hexdigest()`.
7. Computes `marker_path` from `source.extraction.extraction_path / '.landscout-extraction.json'`.
8. Computes `marker` from `json.loads(marker_path.read_text(encoding='utf-8'))`.
9. Calls `marker.update(geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=list(layer_names))` for its validation or side effect.
10. Calls `marker_path.write_text(json.dumps(marker), encoding='utf-8')` for its validation or side effect.
11. Computes `extraction` from `replace(source.extraction, geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=layer_names)`.
12. Computes `configured` from `replace(source, extraction=extraction)`.
13. Computes `alternate_config_payload` from `SOURCE_CONFIG.model_dump(mode='python')`.
14. Computes `alternate_config_payload['access']['road_segments']` from `{'class_label': 'Voie secondaire', 'match_tokens': ('voie', 'secondaire')}`.
15. Computes `alternate_config` from `IgnBdTopoSourceConfig.model_validate(alternate_config_payload)`.
16. Computes `forged` from `load_ign_bdtopo_roads(extraction, alternate_config)`.
17. Returns `(configured, forged)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `geopackage_path.read_bytes`, `load_ign_bdtopo_roads`, `marker_path.read_text`, `marker_path.write_text`, `pyogrio.write_dataframe`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `LineString`, `SOURCE_CONFIG.model_dump`, `_road_frame`, `geopackage_path.read_bytes`, `json.dumps`, `json.loads`, `len`, `list`, `load_ign_bdtopo_roads`, `marker.update`, `marker_path.read_text`, `marker_path.write_text`, `pyogrio.list_layers`, `pyogrio.write_dataframe`, `replace`, `sha256`, `sha256(payload).hexdigest`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_normalize_access_ign.py` — `test_road_normalization_reproduces_configured_logical_layer`

**Tests**

- `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_normalization_reproduces_configured_logical_layer`

**Signature**

```python
def test_road_normalization_reproduces_configured_logical_layer() -> None:
```

**Purpose**

Protects the `road normalization reproduces configured logical layer` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(configured, forged)` from `_with_alternate_road_layer(_source())`.
- Computes `loaded` from `load_ign_bdtopo_roads(configured.extraction, SOURCE_CONFIG)`.
- Computes `normalized` from `normalize_ign_roads(loaded, SOURCE_CONFIG)`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='source|configured|physical')` and executes: Calls `normalize_ign_roads(forged, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `_with_alternate_road_layer`, `load_ign_bdtopo_roads`, `normalize_ign_roads`, `normalized.road_segments['source_layer'].eq`, `normalized.road_segments['source_layer'].eq(ROAD_LAYER).all`.

**Expected result**

- Direct assertions: `assert normalized.road_segments['source_layer'].eq(ROAD_LAYER).all()`.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='source|configured|physical'): normalize_ign_roads(forged, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `road normalization reproduces configured logical layer` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `_with_alternate_road_layer`, `load_ign_bdtopo_roads`, `normalize_ign_roads`, `normalized.road_segments['source_layer'].eq`, `normalized.road_segments['source_layer'].eq(ROAD_LAYER).all`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_road_normalization_symbols`

**Signature**

```python
def test_public_api_exports_only_stable_road_normalization_symbols() -> None:
```

**Purpose**

Protects the `public api exports only stable road normalization symbols` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `expected` from `{'IgnRoadNormalizationError', 'NormalizedIgnRoadData', 'normalize_ign_roads'}`.

**Action**

- Calls `all`, `hasattr`.

**Expected result**

- Direct assertions: `assert set(access_normalization.__all__) == expected`; `assert expected <= set(stages.__all__)`; `assert all((hasattr(stages, name) for name in expected))`; `assert not hasattr(stages, '_validate_road_source')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public api exports only stable road normalization symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `hasattr`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_linestring_normalization_has_exact_schema_identity_and_lineage`

**Signature**

```python
def test_valid_linestring_normalization_has_exact_schema_identity_and_lineage() -> None:
```

**Purpose**

Protects the `valid linestring normalization has exact schema identity and lineage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `normalized` from `normalize_ign_roads(_source(), SOURCE_CONFIG)`.
- Computes `roads` from `normalized.road_segments`.
- Computes `row` from `roads.iloc[0]`.

**Action**

- Calls `_source`, `isinstance`, `normalize_ign_roads`, `roads.crs.to_epsg`, `roads.index.tolist`, `type`.

**Expected result**

- Direct assertions: `assert type(normalized) is NormalizedIgnRoadData`; `assert list(roads.columns) == list(OUTPUT_COLUMNS)`; `assert isinstance(roads.index, pd.RangeIndex)`; `assert roads.index.tolist() == [0]`; `assert row['road_feature_id'] == 'IGN_BDTOPO:ROAD_SEGMENT:ROAD-1'`; `assert row['road_feature_type'] == 'ROAD_SEGMENT'`; `assert row['source_feature_id'] == 'ROAD-1'`; `assert row['source_provider'] == 'IGN'`; `assert row['source_product'] == 'BD_TOPO'`; `assert row['source_layer'] == ROAD_LAYER`; `assert row['source_department_code'] == '31'`; `assert row['source_edition'] == '2026-06-15'`; `assert row['source_product_version'] == '3.5'`; `assert row['source_download_timestamp'] == '2026-08-11T15:32:03+00:00'`; `assert row['source_archive_sha256'] == ARCHIVE_SHA256`; `assert row['source_url'] == SOURCE_URL`; `assert row['spatial_role'] == 'PROXY_GEOMETRY'`; `assert row['geometry_status'] == 'VALID'`; `assert roads.crs is not None and roads.crs.to_epsg() == 2154`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid linestring normalization has exact schema identity and lineage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `isinstance`, `list`, `normalize_ign_roads`, `roads.crs.to_epsg`, `roads.index.tolist`, `type`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_multilinestring_is_preserved`

**Signature**

```python
def test_valid_multilinestring_is_preserved() -> None:
```

**Purpose**

Protects the `valid multilinestring is preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `geometry` from `MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])`.
- Computes `roads` from `normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG).road_segments`.

**Action**

- Calls `MultiLineString`, `_road_frame`, `_source`, `normalize_ign_roads`, `roads.geometry.iloc[0].equals_exact`.

**Expected result**

- Direct assertions: `assert roads.iloc[0]['geometry_status'] == 'VALID'`; `assert roads.geometry.iloc[0].equals_exact(geometry, tolerance=0)`; `assert roads.geometry.iloc[0].geom_type == 'MultiLineString'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid multilinestring is preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiLineString`, `_road_frame`, `_source`, `normalize_ign_roads`, `roads.geometry.iloc[0].equals_exact`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_z_coordinates_are_preserved_exactly`

**Signature**

```python
def test_z_coordinates_are_preserved_exactly() -> None:
```

**Purpose**

Protects the `z coordinates are preserved exactly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `geometry` from `LineString([(0, 0, 12), (10, 10, 24)])`.
- Computes `roads` from `normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG).road_segments`.

**Action**

- Calls `LineString`, `_road_frame`, `_source`, `normalize_ign_roads`.

**Expected result**

- Direct assertions: `assert roads.geometry.iloc[0].has_z`; `assert roads.geometry.iloc[0].wkb == geometry.wkb`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `z coordinates are preserved exactly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_road_frame`, `_source`, `normalize_ign_roads`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_row_count_order_geometry_and_range_index_are_preserved`

**Signature**

```python
def test_row_count_order_geometry_and_range_index_are_preserved() -> None:
```

**Purpose**

Protects the `row count order geometry and range index are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `geometries` from `[LineString([(20, 0), (20, 10)]), LineString([(5, 0), (5, 10)])]`.
- Computes `source` from `_source(_road_frame(geometries, identifiers=['SECOND', 'FIRST'], index=[91, 14]))`.
- Computes `roads` from `normalize_ign_roads(source, SOURCE_CONFIG).road_segments`.

**Action**

- Calls `LineString`, `_road_frame`, `_source`, `isinstance`, `normalize_ign_roads`, `roads.geometry.to_wkb`, `roads.geometry.to_wkb().tolist`, `roads['road_feature_id'].tolist`, `roads['source_feature_id'].tolist`.

**Expected result**

- Direct assertions: `assert len(roads) == 2`; `assert roads['source_feature_id'].tolist() == ['SECOND', 'FIRST']`; `assert roads['road_feature_id'].tolist() == ['IGN_BDTOPO:ROAD_SEGMENT:SECOND', 'IGN_BDTOPO:ROAD_SEGMENT:FIRST']`; `assert isinstance(roads.index, pd.RangeIndex)`; `assert roads.geometry.to_wkb().tolist() == [value.wkb for value in geometries]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `row count order geometry and range index are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_road_frame`, `_source`, `isinstance`, `len`, `normalize_ign_roads`, `roads.geometry.to_wkb`, `roads.geometry.to_wkb().tolist`, `roads['road_feature_id'].tolist`, `roads['source_feature_id'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_raw_access_and_restriction_values_are_copied_without_interpretation`

**Signature**

```python
def test_raw_access_and_restriction_values_are_copied_without_interpretation() -> None:
```

**Purpose**

Protects the `raw access and restriction values are copied without interpretation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `source` from `_road_frame()`.
- Computes `source.loc[source.index[0], 'importance']` from `'00'`.
- Computes `source.loc[source.index[0], 'prive']` from `'Valeur IGN non interprétée'`.
- Computes `source.loc[source.index[0], 'acces_vehicule_leger']` from `'Inconnu'`.
- Computes `source.loc[source.index[0], 'restriction_de_poids_total']` from `19.75`.
- Computes `source.loc[source.index[0], 'nature_de_la_restriction']` from `None`.
- Computes `row` from `normalize_ign_roads(_source(source), SOURCE_CONFIG).road_segments.iloc[0]`.

**Action**

- Calls `_road_frame`, `_source`, `normalize_ign_roads`, `pd.isna`.

**Expected result**

- Direct assertions: `assert row['importance_raw'] == '00'`; `assert row['private_raw'] == 'Valeur IGN non interprétée'`; `assert row['light_vehicle_access_raw'] == 'Inconnu'`; `assert row['restriction_total_weight_raw'] == 19.75`; `assert pd.isna(row['restriction_nature_raw'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `raw access and restriction values are copied without interpretation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_road_frame`, `_source`, `normalize_ign_roads`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_raw_field_preserves_source_values_nulls_and_dtype`

**Signature**

```python
def test_every_raw_field_preserves_source_values_nulls_and_dtype() -> None:
```

**Purpose**

Protects the `every raw field preserves source values nulls and dtype` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `roads` from `normalize_ign_roads(source, SOURCE_CONFIG).road_segments`.

**Action**

- Calls `_source`, `normalize_ign_roads`, `pd.testing.assert_series_equal`, `source.road_segments[source_column].reset_index`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `every raw field preserves source values nulls and dtype` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pd.testing.assert_series_equal`, `source.road_segments[source_column].reset_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_required_source_field_is_rejected`

**Signature**

```python
def test_missing_required_source_field_is_rejected(column: str) -> None:
```

**Purpose**

Protects the `missing required source field is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `frame` from `source.road_segments.drop(columns=column)`.
- Computes `mutated` from `replace(source, road_segments=frame)`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match=column)` and executes: Calls `normalize_ign_roads(mutated, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`, `source.road_segments.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match=column): normalize_ign_roads(mutated, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `missing required source field is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `source.road_segments.drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_or_empty_cleabs_is_rejected`

**Signature**

```python
def test_null_or_empty_cleabs_is_rejected(identifier: object) -> None:
```

**Purpose**

Protects the `null or empty cleabs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identifier`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='cleabs')` and executes: Calls `normalize_ign_roads(_source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_road_frame`, `_source`, `normalize_ign_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='cleabs'): normalize_ign_roads(_source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `null or empty cleabs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_road_frame`, `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_cleabs_is_rejected`

**Signature**

```python
def test_unsafe_cleabs_is_rejected(identifier: str) -> None:
```

**Purpose**

Protects the `unsafe cleabs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `identifier`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='cleabs')` and executes: Calls `normalize_ign_roads(_source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_road_frame`, `_source`, `normalize_ign_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='cleabs'): normalize_ign_roads(_source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `unsafe cleabs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_road_frame`, `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_cleabs_is_rejected`

**Signature**

```python
def test_duplicate_cleabs_is_rejected() -> None:
```

**Purpose**

Protects the `duplicate cleabs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `frame` from `_road_frame([LineString([(0, 0), (1, 1)]), LineString([(2, 2), (3, 3)])], identifiers=['DUPLICATE', 'DUPLICATE'])`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='unique')` and executes: Calls `normalize_ign_roads(_source(frame), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `LineString`, `_road_frame`, `_source`, `normalize_ign_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='unique'): normalize_ign_roads(_source(frame), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `duplicate cleabs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_road_frame`, `_source`, `normalize_ign_roads`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_or_missing_road_crs_is_rejected`

**Signature**

```python
def test_wrong_or_missing_road_crs_is_rejected(crs: str | None) -> None:
```

**Purpose**

Protects the `wrong or missing road crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `crs`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='CRS|2154')` and executes: Calls `normalize_ign_roads(_source(_road_frame(crs=crs)), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_road_frame`, `_source`, `normalize_ign_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='CRS|2154'): normalize_ign_roads(_source(_road_frame(crs=crs)), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `wrong or missing road crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_road_frame`, `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_archive_identity_is_rejected`

**Signature**

```python
def test_wrong_archive_identity_is_rejected(
    field: str,
    value: str,
    message: str,
) -> None:
```

**Purpose**

Protects the `wrong archive identity is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`, `message`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `archive` from `replace(source.extraction.archive, **{field: value})`.
- Computes `mutated` from `replace(source, extraction=replace(source.extraction, archive=archive))`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match=message)` and executes: Calls `normalize_ign_roads(mutated, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match=message): normalize_ign_roads(mutated, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `wrong archive identity is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_source_spatial_role_is_rejected`

**Signature**

```python
def test_wrong_source_spatial_role_is_rejected(component: str) -> None:
```

**Purpose**

Protects the `wrong source spatial role is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `component`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `wrong_role` from `cast(Any, 'AUTHORITATIVE_ACCESS')`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='PROXY_GEOMETRY')` and executes: Calls `normalize_ign_roads(mutated, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `cast`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='PROXY_GEOMETRY'): normalize_ign_roads(mutated, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `wrong source spatial role is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `cast`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_summary_row_count_mismatch_is_rejected`

**Signature**

```python
def test_summary_row_count_mismatch_is_rejected() -> None:
```

**Purpose**

Protects the `summary row count mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `summary` from `replace(source.road_segments_summary, feature_count=2)`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='row count')` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='row count'): normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `summary row count mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_summary_requires_strict_structural_types`

**Signature**

```python
def test_road_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
```

**Purpose**

Protects the `road summary requires strict structural types` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `changed` from `replace(source.road_segments_summary, **{field: value})`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError)` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=changed), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError): normalize_ign_roads(replace(source, road_segments_summary=changed), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `road summary requires strict structural types` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_archive_sha256_requires_canonical_lowercase`

**Signature**

```python
def test_road_archive_sha256_requires_canonical_lowercase(value: str) -> None:
```

**Purpose**

Protects the `road archive sha256 requires canonical lowercase` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `extraction` from `replace(source.extraction, archive=replace(source.extraction.archive, sha256=value))`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError)` and executes: Calls `normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError): normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `road archive sha256 requires canonical lowercase` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_summary_crs_mismatch_is_rejected`

**Signature**

```python
def test_summary_crs_mismatch_is_rejected() -> None:
```

**Purpose**

Protects the `summary crs mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `summary` from `replace(source.road_segments_summary, crs='EPSG:4326')`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='CRS|2154')` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='CRS|2154'): normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `summary crs mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_forged_ordered_summary_schema_is_rejected`

**Signature**

```python
def test_forged_ordered_summary_schema_is_rejected(mutation: str) -> None:
```

**Purpose**

Protects the `forged ordered summary schema is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `summary` from `source.road_segments_summary`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='schema|columns|dtype')` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=changed), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`, `reversed`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='schema|columns|dtype'): normalize_ign_roads(replace(source, road_segments_summary=changed), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `forged ordered summary schema is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `list`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `reversed`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_source_rejects_physical_role_collision`

**Signature**

```python
def test_road_source_rejects_physical_role_collision(role: str) -> None:
```

**Purpose**

Protects the `road source rejects physical role collision` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `role`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `selected` from `source.extraction.electric_lines_layer if role == 'electric' else source.extraction.transformation_posts_layer`.
- Computes `summary` from `replace(source.road_segments_summary, source_layer_name=selected)`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='same layer|distinct|role')` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='same layer|distinct|role'): normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `road source rejects physical role collision` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_source_rejects_duplicate_layer_inventory`

**Signature**

```python
def test_road_source_rejects_duplicate_layer_inventory() -> None:
```

**Purpose**

Protects the `road source rejects duplicate layer inventory` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `extraction` from `replace(source.extraction, all_layer_names=(*source.extraction.all_layer_names, ROAD_LAYER))`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='inventory|duplicate')` and executes: Calls `normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='inventory|duplicate'): normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `road source rejects duplicate layer inventory` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_summary_geometry_facts_mismatch_is_rejected`

**Signature**

```python
def test_summary_geometry_facts_mismatch_is_rejected(
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `summary geometry facts mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `summary` from `replace(source.road_segments_summary, **{field: value})`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='geometry summary')` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='geometry summary'): normalize_ign_roads(replace(source, road_segments_summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `summary geometry facts mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_summary_layer_must_exist_in_extraction_inventory`

**Signature**

```python
def test_summary_layer_must_exist_in_extraction_inventory() -> None:
```

**Purpose**

Protects the `summary layer must exist in extraction inventory` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `extraction` from `replace(source.extraction, all_layer_names=('other_layer',))`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='layer inventory')` and executes: Calls `normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='layer inventory'): normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `summary layer must exist in extraction inventory` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `normalize_ign_roads`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_summary_layer_and_logical_name_must_be_exact`

**Signature**

```python
def test_summary_layer_and_logical_name_must_be_exact() -> None:
```

**Purpose**

Protects the `summary layer and logical name must be exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `wrong_layer` from `replace(source.road_segments_summary, source_layer_name='route')`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='physical layer')` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=wrong_layer), SOURCE_CONFIG)` for its validation or side effect.
- Computes `wrong_logical` from `replace(source.road_segments_summary, logical_name=cast(Any, 'electric_lines'))`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='logical name')` and executes: Calls `normalize_ign_roads(replace(source, road_segments_summary=wrong_logical), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `cast`, `normalize_ign_roads`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='physical layer'): normalize_ign_roads(replace(source, road_segments_summary=wrong_layer), SOURCE_CONFIG)`; `with pytest.raises(IgnRoadNormalizationError, match='logical name'): normalize_ign_roads(replace(source, road_segments_summary=wrong_logical), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `summary layer and logical name must be exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `cast`, `normalize_ign_roads`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_unsupported_geometry_type_is_rejected`

**Signature**

```python
def test_valid_unsupported_geometry_type_is_rejected(geometry: object) -> None:
```

**Purpose**

Protects the `valid unsupported geometry type is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='geometry types')` and executes: Calls `normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `Point`, `Polygon`, `_road_frame`, `_source`, `normalize_ign_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='geometry types'): normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `valid unsupported geometry type is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `Polygon`, `_road_frame`, `_source`, `normalize_ign_roads`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_empty_and_invalid_geometry_are_preserved_with_status`

**Signature**

```python
def test_null_empty_and_invalid_geometry_are_preserved_with_status() -> None:
```

**Purpose**

Protects the `null empty and invalid geometry are preserved with status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])`.
- Computes `frame` from `_road_frame([None, LineString(), invalid], identifiers=['NULL', 'EMPTY', 'INVALID'])`.
- Computes `roads` from `normalize_ign_roads(_source(frame), SOURCE_CONFIG).road_segments`.

**Action**

- Calls `LineString`, `Polygon`, `_road_frame`, `_source`, `normalize_ign_roads`, `roads.geometry.iloc[2].equals_exact`, `roads['geometry_status'].tolist`.

**Expected result**

- Direct assertions: `assert roads['geometry_status'].tolist() == ['NULL', 'EMPTY', 'INVALID']`; `assert roads.geometry.iloc[0] is None`; `assert roads.geometry.iloc[1].is_empty`; `assert roads.geometry.iloc[2].equals_exact(invalid, tolerance=0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `null empty and invalid geometry are preserved with status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Polygon`, `_road_frame`, `_source`, `normalize_ign_roads`, `roads.geometry.iloc[2].equals_exact`, `roads['geometry_status'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normalization_does_not_mutate_input`

**Signature**

```python
def test_normalization_does_not_mutate_input() -> None:
```

**Purpose**

Protects the `normalization does not mutate input` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `before` from `deepcopy(source.road_segments)`.

**Action**

- Calls `_source`, `deepcopy`, `normalize_ign_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `normalization does not mutate input` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `assert_geodataframe_equal`, `deepcopy`, `normalize_ign_roads`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_high_level_rejects_coordinated_road_frame_and_summary_forgery`

**Signature**

```python
def test_high_level_rejects_coordinated_road_frame_and_summary_forgery() -> None:
```

**Purpose**

Protects the `high level rejects coordinated road frame and summary forgery` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `forged` from `source.road_segments.copy()`.
- Computes `forged.loc[0, 'nature']` from `'Invented road nature'`.
- Computes `forged_summary` from `_summary(forged)`.
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError, match='physical|fresh|source')` and executes: Calls `normalize_ign_roads(replace(source, road_segments=forged, road_segments_summary=forged_summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_source`, `_summary`, `normalize_ign_roads`, `replace`, `source.road_segments.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError, match='physical|fresh|source'): normalize_ign_roads(replace(source, road_segments=forged, road_segments_summary=forged_summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `high level rejects coordinated road frame and summary forgery` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `_summary`, `normalize_ign_roads`, `pytest.raises`, `replace`, `source.road_segments.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_public_input_has_controlled_error`

**Signature**

```python
def test_malformed_public_input_has_controlled_error() -> None:
```

**Purpose**

Protects the `malformed public input has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadNormalizationError)` and executes: Calls `normalize_ign_roads(cast(Any, object()), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `cast`, `normalize_ign_roads`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadNormalizationError): normalize_ign_roads(cast(Any, object()), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `malformed public input has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `cast`, `normalize_ign_roads`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `acces_vehicule_leger` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `access` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `administrative_classification_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `carriageway_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `closure_period_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `dangerous_goods_forbidden_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `fictitious_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `id` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `lane_count_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `light_vehicle_access_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `manager_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `mean_light_vehicle_speed_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nature` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nature_de_la_restriction` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `planimetric_acquisition_method` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planimetric_precision_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `position_relative_to_ground_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `private_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `prive` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_axle_weight_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_de_poids_total` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_height_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_length_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_total_weight_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `road_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_feature_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `road_segments` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_confirmed_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_created_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identifiers_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_modified_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_name_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `traffic_direction_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `urban_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |

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
