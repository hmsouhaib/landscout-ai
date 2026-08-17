# `tests/unit/test_assess_grid_coverage.py`

## File identity

- Repository path: `tests/unit/test_assess_grid_coverage.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `e0292900ee8adfefe03c11377328b02ba5d7e033dde473fcff55180df65a32ec`

## 1. Purpose

Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import json` — required by the implementation paths and symbols documented below.
- `import tempfile` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `from uuid import uuid4` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pyogrio` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( LineString, MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources import ( IgnBdTopoCoverageLayerSummary, IgnBdTopoDepartmentCoverage, IgnBdTopoDownload, IgnBdTopoElectricityData, IgnBdTopoExtraction, IgnBdTopoSourceConfig, load_ign_bdtopo_department_coverage, load_ign_bdtopo_source_config, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages import ( GridCoverageAssessmentError, profile_grid_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages import ( assess_grid_coverage as public_assess_grid_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.assess_grid_coverage import ( _assess_grid_coverage_from_proximity as assess_grid_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_grid_proximity import ( _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `ARCHIVE_SHA256` | `"a" * 64` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EDITION` | `"2026-06-15"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_FIXTURE_ROOT` | `Path(tempfile.mkdtemp(prefix="landscout-coverage-ign-"))` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_CONFIG` | `load_ign_bdtopo_source_config()` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALTERNATE_COVERAGE_LAYER` | `"zone_administrative"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_coverage`

**Signature**

```python
def _coverage(
    geometry: object = Polygon(
        [(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]
    ),
    *,
    crs: str | None = "EPSG:2154",
    spatial_role: str = "SOURCE_COVERAGE_BOUNDARY",
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Implements coverage according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`object`; optional/default `Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `spatial_role` (`str`; optional/default `'SOURCE_COVERAGE_BOUNDARY'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDepartmentCoverage`. Observed return expression(s): `IgnBdTopoDepartmentCoverage(extraction=extraction, coverage=frame, summary=summary, source_provider='IGN', source_product='BD TOPO', source_department_code='31', source_edition=EDITION, source_product_version='3.5', source_archive_sha256=ARCHIVE_SHA256, source_layer='departement', spatial_role=spatial_role)`.

**Algorithm**

1. Computes `raw_frame` from `gpd.GeoDataFrame({'code_insee': ['31'], 'nom_officiel': ['Haute-Garonne']}, geometry=[geometry], crs=crs)`.
2. Computes `extraction_path` from `_FIXTURE_ROOT / uuid4().hex`.
3. Calls `extraction_path.mkdir(parents=True)` for its validation or side effect.
4. Computes `geopackage_path` from `extraction_path / 'data.gpkg'`.
5. Computes `dummy` from `gpd.GeoDataFrame({'id': ['dummy']}, geometry=[LineString([(0, 0), (1, 1)])], crs=crs or 'EPSG:2154')`.
6. Calls `pyogrio.write_dataframe(dummy, geopackage_path, layer='ligne_electrique', driver='GPKG')` for its validation or side effect.
7. Calls `pyogrio.write_dataframe(dummy, geopackage_path, layer='poste_de_transformation', driver='GPKG', append=True)` for its validation or side effect.
8. Calls `pyogrio.write_dataframe(raw_frame, geopackage_path, layer='departement', driver='GPKG', append=True)` for its validation or side effect.
9. Computes `raw_frame` from `gpd.read_file(geopackage_path, layer='departement', engine='pyogrio')`.
10. Computes `payload` from `geopackage_path.read_bytes()`.
11. Computes `digest` from `sha256(payload).hexdigest()`.
12. Computes `layer_names` from `tuple((str(row[0]) for row in pyogrio.list_layers(geopackage_path)))`.
13. Calls `(extraction_path / '.landscout-extraction.json').write_text(json.dumps({'schema_version': 2, 'archive_sha256': ARCHIVE_SHA256, 'geopackage_relative_path': 'data.gpkg', 'geopackage_size_bytes': len(payload), 'geopackage_sha256': digest, 'all_layer_names': list(layer_names), 'electric_lines_layer': 'ligne_electrique', 'transformation_posts_layer': 'poste_de_t…` for its validation or side effect.
14. Computes `archive` from `IgnBdTopoDownload(provider='IGN', product='BD TOPO', department_code='31', edition=EDITION, product_version='3.5', projection='EPSG:2154', package_format='GPKG', archive_format='7z', source_url='https://example.test/BDTOPO.7z', checksum_url=None, download_timestamp='2026-08-11T15:32:03+00:00', filename='BDTOPO.7z', fi…`.
15. Computes `extraction` from `IgnBdTopoExtraction(archive=archive, extraction_path=extraction_path, geopackage_path=geopackage_path, geopackage_filename='data.gpkg', geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=layer_names, electric_lines_layer='ligne_electrique', transformation_posts_layer='poste_de_transformation…`.
16. Computes `frame` from `raw_frame.copy()`.
17. Iterates `(column, value)` over `{'source_provider': 'IGN', 'source_product': 'BD TOPO', 'source_department_code': '31', 'source_edition': EDITION, 'source_product_version': '3.5', 'source_archive_sha256': ARCHIVE_SHA256, 'source_layer': 'departement', 'spatial_role': spatial_role}.items()`. For each value: Computes `frame[column]` from `value`.
18. Computes `geometry_type` from `tuple(sorted((str(value) for value in raw_frame.geometry.dropna().geom_type.unique())))`.
19. Computes `non_null_geometry` from `~frame.geometry.isna()`.
20. Computes `non_empty_geometry` from `non_null_geometry & ~frame.geometry.is_empty`.
21. Computes `summary` from `IgnBdTopoCoverageLayerSummary(source_layer_name='departement', crs=crs or '', source_feature_count=1, selected_feature_count=1, columns=('code_insee', 'nom_officiel', 'geometry'), dtypes=tuple(((str(column), str(dtype)) for column, dtype in raw_frame.dtypes.items())), null_geometry_count=int(raw_frame.geometry.isna().…`.
22. Returns `IgnBdTopoDepartmentCoverage(extraction=extraction, coverage=frame, summary=summary, source_provider='IGN', source_product='BD TOPO', source_department_code='31', source_edition=EDITION, source_product_version='3.5', source_archive_sha256=ARCHIVE_SHA256, source_layer='departement', spatial_role=spatial_role)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(extraction_path / '.landscout-extraction.json').write_text`, `IgnBdTopoDownload`, `extraction_path.mkdir`, `geopackage_path.read_bytes`, `gpd.read_file`, `pyogrio.write_dataframe`, `raw_frame.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(extraction_path / '.landscout-extraction.json').write_text`, `(non_empty_geometry & ~raw_frame.geometry.is_valid).sum`, `(non_null_geometry & raw_frame.geometry.is_empty).sum`, `IgnBdTopoCoverageLayerSummary`, `IgnBdTopoDepartmentCoverage`, `IgnBdTopoDownload`, `IgnBdTopoExtraction`, `LineString`, `Polygon`, `extraction_path.mkdir`, `frame.geometry.isna`, `geopackage_path.read_bytes`, `gpd.GeoDataFrame`, `gpd.read_file`, `int`, `json.dumps`, `len`, `list`, `pyogrio.list_layers`, `pyogrio.write_dataframe`, `raw_frame.copy`, `raw_frame.dtypes.items`, `raw_frame.geometry.dropna`, `raw_frame.geometry.dropna().geom_type.unique`, `raw_frame.geometry.isna`, `raw_frame.geometry.isna().sum`, `sha256`, `sha256(payload).hexdigest`, `sorted`, `str`, `tuple`, `uuid4`, `{'source_provider': 'IGN', 'source_product': 'BD TOPO', 'source_department_code': '31', 'source_edition': EDITION, 'source_product_version': '3.5', 'source_archive_sha256': ARCHIVE_SHA256, 'source_layer': 'departement', 'spatial_role': spatial_role}.items`.

**Known repository callers**

- `tests/unit/test_assess_grid_coverage.py` — `test_assessment_preserves_proximity_values_and_does_not_mutate_input`
- `tests/unit/test_assess_grid_coverage.py` — `test_caller_provided_proximity_and_coverage_are_not_public_inputs`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_assessment_reproduces_configured_logical_layer`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_rejects_arbitrary_source_identity`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_source_layer_lineage_must_match_summary_and_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_crs_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_department_field_must_be_exact`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_geometry_facts_are_validated`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_schema_must_match_selected_source_columns`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_selected_count_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_selected_department_must_match`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_source_count_cannot_be_smaller_than_selection`
- `tests/unit/test_assess_grid_coverage.py` — `test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_assess_grid_coverage.py` — `test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_grid_coverage.py` — `test_no_exact_match_uses_explicit_no_match_status`
- `tests/unit/test_assess_grid_coverage.py` — `test_outside_crossing_or_touching_parcel_is_conservative`
- `tests/unit/test_assess_grid_coverage.py` — `test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_grid_coverage.py` — `test_profile_reports_dynamic_voltage_and_boundary_distributions`
- `tests/unit/test_assess_grid_coverage.py` — `test_proximity_and_coverage_package_lineage_must_match`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_coverage_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_grid_coverage.py` — `test_strict_geometric_boundary_proof`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input`
- `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection`
- `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status`
- `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative`
- `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions`
- `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match`
- `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_with_alternate_coverage_layer`

**Signature**

```python
def _with_alternate_coverage_layer(
    source: IgnBdTopoDepartmentCoverage,
) -> tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]:
```

**Purpose**

Implements with alternate coverage layer according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoDepartmentCoverage`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]`. Observed return expression(s): `(configured, forged)`.

**Algorithm**

1. Computes `alternate` from `gpd.GeoDataFrame({'code_insee': ['31'], 'nom_officiel': ['Alternate coverage']}, geometry=[Polygon([(0, 0), (0, 900), (900, 900), (900, 0), (0, 0)])], crs='EPSG:2154')`.
2. Computes `geopackage_path` from `source.extraction.geopackage_path`.
3. Calls `pyogrio.write_dataframe(alternate, geopackage_path, layer=ALTERNATE_COVERAGE_LAYER, driver='GPKG', append=True)` for its validation or side effect.
4. Computes `payload` from `geopackage_path.read_bytes()`.
5. Computes `layer_names` from `tuple((str(row[0]) for row in pyogrio.list_layers(geopackage_path)))`.
6. Computes `digest` from `sha256(payload).hexdigest()`.
7. Computes `marker_path` from `source.extraction.extraction_path / '.landscout-extraction.json'`.
8. Computes `marker` from `json.loads(marker_path.read_text(encoding='utf-8'))`.
9. Calls `marker.update(geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=list(layer_names))` for its validation or side effect.
10. Calls `marker_path.write_text(json.dumps(marker), encoding='utf-8')` for its validation or side effect.
11. Computes `extraction` from `replace(source.extraction, geopackage_size_bytes=len(payload), geopackage_sha256=digest, all_layer_names=layer_names)`.
12. Computes `configured` from `replace(source, extraction=extraction, coverage=source.coverage.copy())`.
13. Computes `configured.coverage['source_layer']` from `'departement'`.
14. Computes `alternate_config_payload` from `SOURCE_CONFIG.model_dump(mode='python')`.
15. Computes `alternate_config_payload['coverage']['department_layer']` from `{'class_label': 'Zone administrative', 'match_tokens': ('zone', 'administrative'), 'department_code_field': 'code_insee'}`.
16. Computes `alternate_config` from `IgnBdTopoSourceConfig.model_validate(alternate_config_payload)`.
17. Computes `forged` from `load_ign_bdtopo_department_coverage(extraction, alternate_config)`.
18. Returns `(configured, forged)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `geopackage_path.read_bytes`, `load_ign_bdtopo_department_coverage`, `marker_path.read_text`, `marker_path.write_text`, `pyogrio.write_dataframe`, `replace`, `source.coverage.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoSourceConfig.model_validate`, `Polygon`, `SOURCE_CONFIG.model_dump`, `geopackage_path.read_bytes`, `gpd.GeoDataFrame`, `json.dumps`, `json.loads`, `len`, `list`, `load_ign_bdtopo_department_coverage`, `marker.update`, `marker_path.read_text`, `marker_path.write_text`, `pyogrio.list_layers`, `pyogrio.write_dataframe`, `replace`, `sha256`, `sha256(payload).hexdigest`, `source.coverage.copy`, `str`, `tuple`.

**Known repository callers**

- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_assessment_reproduces_configured_logical_layer`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_parcels`

**Signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    crs: str = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': [f'PARCEL-{position + 1}' for position in range(len(values))], 'preserved_value': list(range(len(values)))}, geometry=values, crs=crs, index=[20 + position for position in range(len(values))])`.

**Algorithm**

1. Computes `values` from `geometries or [Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])]`.
2. Returns `gpd.GeoDataFrame({'parcel_id': [f'PARCEL-{position + 1}' for position in range(len(values))], 'preserved_value': list(range(len(values)))}, geometry=values, crs=crs, index=[20 + position for position in range(len(values))])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`, `len`, `list`, `range`.

**Known repository callers**

- `tests/unit/test_assess_grid_coverage.py` — `_proximity`
- `tests/unit/test_assess_grid_coverage.py` — `test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_coverage_proximity_failure_stops_coverage_loading`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_lines`

**Signature**

```python
def _lines(
    distances: list[float] | None = None,
    *,
    voltage_statuses: list[str] | None = None,
    voltages: list[float | None] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements lines according to the exact implementation and guards in this file.

**Inputs**

- `distances` (`list[float] | None`; optional/default `None`) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltage_statuses` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltages` (`list[float | None] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'grid_feature_id': identifiers, 'grid_feature_type': ['ELECTRIC_LINE'] * len(values), 'source_feature_id': [f'SOURCE-{value}' for value in identifiers], 'source_department_code': ['31'] * len(values), 'source_edition': [EDITION] * len(values), 'source_archive_sha256': [ARCHIVE_SHA256] * len(values), 'source_layer': ['ligne_electrique'] * len(values), 'spatial_role': ['PROXY_GEOM…`.

**Algorithm**

1. Computes `values` from `distances or [50.0]`.
2. Computes `statuses` from `voltage_statuses or ['EXACT'] * len(values)`.
3. Computes `voltage_values` from `voltages or [110.0] * len(values)`.
4. Computes `identifiers` from `[f'LINE-{position + 1}' for position in range(len(values))]`.
5. Returns `gpd.GeoDataFrame({'grid_feature_id': identifiers, 'grid_feature_type': ['ELECTRIC_LINE'] * len(values), 'source_feature_id': [f'SOURCE-{value}' for value in identifiers], 'source_department_code': ['31'] * len(values), 'source_edition': [EDITION] * len(values), 'source_archive_sha256': [ARCHIVE_SHA256] * len(values), 'source_layer': ['ligne_electrique'] * l…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `gpd.GeoDataFrame`, `len`, `range`, `str`.

**Known repository callers**

- `tests/unit/test_assess_grid_coverage.py` — `_electricity_source`
- `tests/unit/test_assess_grid_coverage.py` — `_proximity`
- `tests/unit/test_assess_grid_coverage.py` — `test_geographic_parcel_storage_crs_and_geometry_are_preserved`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_posts`

**Signature**

```python
def _posts(distance_m: float = 50.0) -> gpd.GeoDataFrame:
```

**Purpose**

Implements posts according to the exact implementation and guards in this file.

**Inputs**

- `distance_m` (`float`; optional/default `50.0`) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'grid_feature_id': ['POST-1'], 'grid_feature_type': ['TRANSFORMATION_POST'], 'source_feature_id': ['SOURCE-POST-1'], 'source_department_code': ['31'], 'source_edition': [EDITION], 'source_archive_sha256': [ARCHIVE_SHA256], 'source_layer': ['poste_de_transformation'], 'spatial_role': ['PROXY_GEOMETRY'], 'geometry_status': ['VALID'], 'name': ['Test post'], 'importance_raw': ['5'],…`.

**Algorithm**

1. Returns `gpd.GeoDataFrame({'grid_feature_id': ['POST-1'], 'grid_feature_type': ['TRANSFORMATION_POST'], 'source_feature_id': ['SOURCE-POST-1'], 'source_department_code': ['31'], 'source_edition': [EDITION], 'source_archive_sha256': [ARCHIVE_SHA256], 'source_layer': ['poste_de_transformation'], 'spatial_role': ['PROXY_GEOMETRY'], 'geometry_status': ['VALID'], 'name':…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`.

**Known repository callers**

- `tests/unit/test_assess_grid_coverage.py` — `_electricity_source`
- `tests/unit/test_assess_grid_coverage.py` — `_proximity`
- `tests/unit/test_assess_grid_coverage.py` — `test_geographic_parcel_storage_crs_and_geometry_are_preserved`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_electricity_source`

**Signature**

```python
def _electricity_source(
    extraction: IgnBdTopoExtraction,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Implements electricity source according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`IgnBdTopoExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `IgnBdTopoElectricityData(extraction=extraction, electric_lines=_lines(), transformation_posts=_posts(), electric_lines_summary=cast(Any, None), transformation_posts_summary=cast(Any, None))`.

**Algorithm**

1. Returns `IgnBdTopoElectricityData(extraction=extraction, electric_lines=_lines(), transformation_posts=_posts(), electric_lines_summary=cast(Any, None), transformation_posts_summary=cast(Any, None))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoElectricityData`, `_lines`, `_posts`, `cast`.

**Known repository callers**

- `tests/unit/test_assess_grid_coverage.py` — `test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_coverage_proximity_failure_stops_coverage_loading`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_proximity`

**Signature**

```python
def _proximity(
    *,
    parcel_geometries: list[object] | None = None,
    parcel_crs: str = "EPSG:2154",
    line_distances: list[float] | None = None,
    post_distance_m: float = 50.0,
    voltage_statuses: list[str] | None = None,
    voltages: list[float | None] | None = None,
):
```

**Purpose**

Implements proximity according to the exact implementation and guards in this file.

**Inputs**

- `parcel_geometries` (`list[object] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcel_crs` (`str`; optional/default `'EPSG:2154'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_distances` (`list[float] | None`; optional/default `None`) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `post_distance_m` (`float`; optional/default `50.0`) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltage_statuses` (`list[str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltages` (`list[float | None] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `enrich_parcel_grid_proximity(_parcels(parcel_geometries, crs=parcel_crs), _lines(line_distances, voltage_statuses=voltage_statuses, voltages=voltages), _posts(post_distance_m))`.

**Algorithm**

1. Returns `enrich_parcel_grid_proximity(_parcels(parcel_geometries, crs=parcel_crs), _lines(line_distances, voltage_statuses=voltage_statuses, voltages=voltages), _posts(post_distance_m))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_lines`, `_parcels`, `_posts`, `enrich_parcel_grid_proximity`.

**Known repository callers**

- `tests/unit/test_assess_grid_coverage.py` — `test_assessment_preserves_proximity_values_and_does_not_mutate_input`
- `tests/unit/test_assess_grid_coverage.py` — `test_caller_provided_proximity_and_coverage_are_not_public_inputs`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_assessment_reproduces_configured_logical_layer`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_rejects_arbitrary_source_identity`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_source_layer_lineage_must_match_summary_and_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_crs_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_department_field_must_be_exact`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_geometry_facts_are_validated`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_schema_must_match_selected_source_columns`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_selected_count_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_selected_department_must_match`
- `tests/unit/test_assess_grid_coverage.py` — `test_coverage_summary_source_count_cannot_be_smaller_than_selection`
- `tests/unit/test_assess_grid_coverage.py` — `test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_grid_coverage.py` — `test_no_exact_match_uses_explicit_no_match_status`
- `tests/unit/test_assess_grid_coverage.py` — `test_outside_crossing_or_touching_parcel_is_conservative`
- `tests/unit/test_assess_grid_coverage.py` — `test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_grid_coverage.py` — `test_profile_reports_dynamic_voltage_and_boundary_distributions`
- `tests/unit/test_assess_grid_coverage.py` — `test_proximity_and_coverage_package_lineage_must_match`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py` — `test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py` — `test_strict_geometric_boundary_proof`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input`
- `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match`
- `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection`
- `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected`
- `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status`
- `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative`
- `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted`
- `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions`
- `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match`
- `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source`
- `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once`
- `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_assessment_reproduces_configured_logical_layer`

**Signature**

```python
def test_coverage_assessment_reproduces_configured_logical_layer() -> None:
```

**Purpose**

Protects the `coverage assessment reproduces configured logical layer` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(configured, forged)` from `_with_alternate_coverage_layer(_coverage())`.
- Computes `loaded` from `load_ign_bdtopo_department_coverage(configured.extraction, SOURCE_CONFIG)`.
- Computes `result` from `assess_grid_coverage(_proximity(), loaded, SOURCE_CONFIG)`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='physical|configured')` and executes: Calls `assess_grid_coverage(_proximity(), forged, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `_with_alternate_coverage_layer`, `assess_grid_coverage`, `load_ign_bdtopo_department_coverage`.

**Expected result**

- Direct assertions: `assert result.source_coverage.source_layer == 'departement'`.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='physical|configured'): assess_grid_coverage(_proximity(), forged, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage assessment reproduces configured logical layer` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `_with_alternate_coverage_layer`, `assess_grid_coverage`, `load_ign_bdtopo_department_coverage`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_clean_coverage_api_is_exported`

**Signature**

```python
def test_clean_coverage_api_is_exported() -> None:
```

**Purpose**

Protects the `clean coverage api is exported` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls only local assertions/expressions.

**Expected result**

- Direct assertions: `assert stages.assess_grid_coverage is public_assess_grid_coverage`; `assert stages.profile_grid_coverage is profile_grid_coverage`; `assert 'assess_grid_coverage' in stages.__all__`; `assert 'profile_grid_coverage' in stages.__all__`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `clean coverage api is exported` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- No calls.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_coverage_owns_proximity_and_configured_coverage_once`

**Signature**

```python
def test_public_coverage_owns_proximity_and_configured_coverage_once() -> None:
```

**Purpose**

Protects the `public coverage owns proximity and configured coverage once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `source` from `_electricity_source(coverage.extraction)`.
- Computes `parcels` from `_parcels()`.
- Computes `proximity` from `_proximity()`.
- Enters managed context(s) `patch('landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity', return_value=proximity, create=True), patch('landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage', return_value=coverage, create=True)` and executes: Computes `result` from `public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)`.

**Action**

- Calls `_coverage`, `_electricity_source`, `_parcels`, `_proximity`, `coverage_loader.assert_called_once_with`, `proximity_stage.assert_called_once_with`, `public_assess_grid_coverage`.

**Expected result**

- Direct assertions: `assert result.source_coverage is coverage`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public coverage owns proximity and configured coverage once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_electricity_source`, `_parcels`, `_proximity`, `coverage_loader.assert_called_once_with`, `patch`, `proximity_stage.assert_called_once_with`, `public_assess_grid_coverage`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_coverage_proximity_failure_stops_coverage_loading`

**Signature**

```python
def test_public_coverage_proximity_failure_stops_coverage_loading() -> None:
```

**Purpose**

Protects the `public coverage proximity failure stops coverage loading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `source` from `_electricity_source(coverage.extraction)`.
- Enters managed context(s) `patch('landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity', side_effect=ValueError('physical electricity source changed'), create=True), patch('landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage', create=True), pytest.raises(GridCoverageAssessmentError)` and executes: Calls `public_assess_grid_coverage(_parcels(), source, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `ValueError`, `_coverage`, `_electricity_source`, `_parcels`, `coverage_loader.assert_not_called`, `proximity_stage.assert_called_once`, `public_assess_grid_coverage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity', side_effect=ValueError('physical electricity source changed'), create=True) as proximity_stage, patch('landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage', create=True) as coverage_loader, pytest.raises(GridCoverageAssessmentError): public_assess_grid_coverage(_parcels(), source, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `public coverage proximity failure stops coverage loading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ValueError`, `_coverage`, `_electricity_source`, `_parcels`, `coverage_loader.assert_not_called`, `patch`, `proximity_stage.assert_called_once`, `public_assess_grid_coverage`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_caller_provided_proximity_and_coverage_are_not_public_inputs`

**Signature**

```python
def test_caller_provided_proximity_and_coverage_are_not_public_inputs() -> None:
```

**Purpose**

Protects the `caller provided proximity and coverage are not public inputs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `forged_proximity` from `_proximity(line_distances=[0.0], post_distance_m=0.0)`.
- Computes `forged_coverage` from `_coverage()`.
- Enters managed context(s) `patch('landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity', create=True), patch('landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage', create=True), pytest.raises(GridCoverageAssessmentError, match='parcels|GeoDataFrame')` and executes: Calls `public_assess_grid_coverage(cast(Any, forged_proximity), cast(Any, forged_coverage), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `cast`, `coverage_loader.assert_not_called`, `forged_proximity.parcels['nearest_line_proxy_distance_m'].eq`, `forged_proximity.parcels['nearest_line_proxy_distance_m'].eq(0.0).all`, `forged_proximity.parcels['nearest_line_source_archive_sha256'].eq`, `forged_proximity.parcels['nearest_line_source_archive_sha256'].eq(ARCHIVE_SHA256).all`, `proximity_stage.assert_not_called`, `public_assess_grid_coverage`.

**Expected result**

- Direct assertions: `assert forged_proximity.parcels['nearest_line_proxy_distance_m'].eq(0.0).all()`; `assert forged_proximity.parcels['nearest_line_source_archive_sha256'].eq(ARCHIVE_SHA256).all()`.
- Expected exception contexts: `with patch('landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity', create=True) as proximity_stage, patch('landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage', create=True) as coverage_loader, pytest.raises(GridCoverageAssessmentError, match='parcels|GeoDataFrame'): public_assess_grid_coverage(cast(Any, forged_proximity), cast(Any, forged_coverage), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `caller provided proximity and coverage are not public inputs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `cast`, `coverage_loader.assert_not_called`, `forged_proximity.parcels['nearest_line_proxy_distance_m'].eq`, `forged_proximity.parcels['nearest_line_proxy_distance_m'].eq(0.0).all`, `forged_proximity.parcels['nearest_line_source_archive_sha256'].eq`, `forged_proximity.parcels['nearest_line_source_archive_sha256'].eq(ARCHIVE_SHA256).all`, `patch`, `proximity_stage.assert_not_called`, `public_assess_grid_coverage`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_polygonal_coverage_geometry_is_accepted`

**Signature**

```python
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
```

**Purpose**

Protects the `polygonal coverage geometry is accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `assess_grid_coverage(_proximity(), _coverage(geometry), SOURCE_CONFIG)`.

**Action**

- Calls `MultiPolygon`, `Polygon`, `_coverage`, `_proximity`, `assess_grid_coverage`.

**Expected result**

- Direct assertions: `assert result.parcels.iloc[0]['grid_source_boundary_distance_m'] == pytest.approx(100.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `polygonal coverage geometry is accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.approx`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_coverage_geometry_is_rejected`

**Signature**

```python
def test_invalid_coverage_geometry_is_rejected(
    geometry: object,
    crs: str | None,
    message: str,
) -> None:
```

**Purpose**

Protects the `invalid coverage geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`, `crs`, `message`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match=message)` and executes: Calls `assess_grid_coverage(_proximity(), _coverage(geometry, crs=crs), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_coverage`, `_proximity`, `assess_grid_coverage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match=message): assess_grid_coverage(_proximity(), _coverage(geometry, crs=crs), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `invalid coverage geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_strict_geometric_boundary_proof`

**Signature**

```python
def test_strict_geometric_boundary_proof(
    asset_distance: float,
    expected_status: str,
) -> None:
```

**Purpose**

Protects the `strict geometric boundary proof` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `asset_distance`, `expected_status`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `assess_grid_coverage(_proximity(line_distances=[asset_distance], post_distance_m=asset_distance), _coverage(), SOURCE_CONFIG)`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`.

**Expected result**

- Direct assertions: `assert parcel['grid_source_boundary_distance_m'] == pytest.approx(100.0)`; `assert parcel['nearest_line_proxy_distance_m'] == pytest.approx(asset_distance)`; `assert parcel['nearest_line_coverage_status'] == expected_status`; `assert parcel['nearest_exact_line_coverage_status'] == expected_status`; `assert parcel['nearest_post_coverage_status'] == expected_status`; `assert result.voltage_level_proximity.loc[0, 'coverage_status'] == expected_status`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `strict geometric boundary proof` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.approx`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_outside_crossing_or_touching_parcel_is_conservative`

**Signature**

```python
def test_outside_crossing_or_touching_parcel_is_conservative(
    parcel_geometry: Polygon,
) -> None:
```

**Purpose**

Protects the `outside crossing or touching parcel is conservative` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcel_geometry`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `assess_grid_coverage(_proximity(parcel_geometries=[parcel_geometry]), _coverage(), SOURCE_CONFIG)`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `Polygon`, `_coverage`, `_proximity`, `assess_grid_coverage`.

**Expected result**

- Direct assertions: `assert parcel['grid_source_boundary_distance_m'] == 0.0`; `assert parcel['grid_source_coverage_position'] == 'OUTSIDE_OR_CROSSING_COVERAGE'`; `assert parcel['nearest_line_coverage_status'] == 'OUTSIDE_OR_CROSSING_COVERAGE'`; `assert parcel['nearest_exact_line_coverage_status'] == 'OUTSIDE_OR_CROSSING_COVERAGE'`; `assert parcel['nearest_post_coverage_status'] == 'OUTSIDE_OR_CROSSING_COVERAGE'`; `assert result.voltage_level_proximity.loc[0, 'coverage_status'] == 'OUTSIDE_OR_CROSSING_COVERAGE'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `outside crossing or touching parcel is conservative` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_exact_match_uses_explicit_no_match_status`

**Signature**

```python
def test_no_exact_match_uses_explicit_no_match_status() -> None:
```

**Purpose**

Protects the `no exact match uses explicit no match status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `proximity` from `_proximity(voltage_statuses=['UNKNOWN'], voltages=[None])`.
- Computes `result` from `assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)`.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `result.parcels['nearest_exact_line_coverage_status'].eq`, `result.parcels['nearest_exact_line_coverage_status'].eq('NO_MATCH').all`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna().all`.

**Expected result**

- Direct assertions: `assert result.parcels['nearest_exact_line_proxy_distance_m'].isna().all()`; `assert result.parcels['nearest_exact_line_coverage_status'].eq('NO_MATCH').all()`; `assert result.voltage_level_proximity.empty`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no exact match uses explicit no match status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `result.parcels['nearest_exact_line_coverage_status'].eq`, `result.parcels['nearest_exact_line_coverage_status'].eq('NO_MATCH').all`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna`, `result.parcels['nearest_exact_line_proxy_distance_m'].isna().all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_assessment_preserves_proximity_values_and_does_not_mutate_input`

**Signature**

```python
def test_assessment_preserves_proximity_values_and_does_not_mutate_input() -> None:
```

**Purpose**

Protects the `assessment preserves proximity values and does not mutate input` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `proximity` from `_proximity(line_distances=[50.0, 150.0], voltages=[110.0, 275.0])`.
- Computes `parcels_before` from `deepcopy(proximity.parcels)`.
- Computes `table_before` from `deepcopy(proximity.voltage_level_proximity)`.
- Computes `result` from `assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)`.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `deepcopy`, `parcels_before['parcel_id'].tolist`, `result.parcels['parcel_id'].tolist`, `result.voltage_level_proximity[['parcel_id', 'voltage_kv']].equals`.

**Expected result**

- Direct assertions: `assert result.parcels['parcel_id'].tolist() == parcels_before['parcel_id'].tolist()`; `assert result.voltage_level_proximity[['parcel_id', 'voltage_kv']].equals(table_before[['parcel_id', 'voltage_kv']])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `assessment preserves proximity values and does not mutate input` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assert_frame_equal`, `assert_geodataframe_equal`, `assess_grid_coverage`, `deepcopy`, `parcels_before['parcel_id'].tolist`, `result.parcels['parcel_id'].tolist`, `result.voltage_level_proximity[['parcel_id', 'voltage_kv']].equals`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_geographic_parcel_storage_crs_and_geometry_are_preserved`

**Signature**

```python
def test_geographic_parcel_storage_crs_and_geometry_are_preserved() -> None:
```

**Purpose**

Protects the `geographic parcel storage crs and geometry are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `projected` from `_parcels()`.
- Computes `geographic` from `projected.to_crs('EPSG:4326')`.
- Computes `proximity` from `enrich_parcel_grid_proximity(geographic, _lines(), _posts())`.
- Computes `result` from `assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)`.

**Action**

- Calls `_coverage`, `_lines`, `_parcels`, `_posts`, `assess_grid_coverage`, `enrich_parcel_grid_proximity`, `projected.to_crs`, `result.parcels.crs.to_epsg`, `result.parcels.geometry.geom_equals_exact`, `result.parcels.geometry.geom_equals_exact(proximity.parcels.geometry, tolerance=0, align=False).all`.

**Expected result**

- Direct assertions: `assert result.parcels.crs.to_epsg() == 4326`; `assert result.parcels.geometry.geom_equals_exact(proximity.parcels.geometry, tolerance=0, align=False).all()`; `assert result.parcels.iloc[0]['grid_source_boundary_distance_m'] == pytest.approx(100.0, abs=1e-06)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `geographic parcel storage crs and geometry are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_lines`, `_parcels`, `_posts`, `assess_grid_coverage`, `enrich_parcel_grid_proximity`, `projected.to_crs`, `pytest.approx`, `result.parcels.crs.to_epsg`, `result.parcels.geometry.geom_equals_exact`, `result.parcels.geometry.geom_equals_exact(proximity.parcels.geometry, tolerance=0, align=False).all`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_reports_dynamic_voltage_and_boundary_distributions`

**Signature**

```python
def test_profile_reports_dynamic_voltage_and_boundary_distributions() -> None:
```

**Purpose**

Protects the `profile reports dynamic voltage and boundary distributions` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `assess_grid_coverage(_proximity(line_distances=[50.0, 150.0], post_distance_m=100.0, voltages=[110.0, 275.0]), _coverage(), SOURCE_CONFIG)`.
- Computes `profile` from `profile_grid_coverage(result)`.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `profile_grid_coverage`.

**Expected result**

- Direct assertions: `assert profile.parcel_count == 1`; `assert profile.fully_covered_count == 1`; `assert profile.outside_or_crossing_count == 0`; `assert profile.boundary_distance.minimum == pytest.approx(100.0)`; `assert profile.boundary_distance.p50 == pytest.approx(100.0)`; `assert profile.boundary_distance.maximum == pytest.approx(100.0)`; `assert profile.nearest_line.not_boundary_limited == 1`; `assert profile.nearest_post.boundary_limited == 1`; `assert [item.voltage_kv for item in profile.voltage_levels] == [110.0, 275.0]`; `assert profile.voltage_levels[0].statuses.not_boundary_limited == 1`; `assert profile.voltage_levels[1].statuses.boundary_limited == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `profile reports dynamic voltage and boundary distributions` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `profile_grid_coverage`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_proximity_and_coverage_package_lineage_must_match`

**Signature**

```python
def test_proximity_and_coverage_package_lineage_must_match() -> None:
```

**Purpose**

Protects the `proximity and coverage package lineage must match` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `proximity` from `_proximity()`.
- Computes `coverage` from `_coverage()`.
- Computes `coverage.coverage.loc[0, 'source_archive_sha256']` from `'b' * 64`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='lineage')` and executes: Calls `assess_grid_coverage(proximity, coverage, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='lineage'): assess_grid_coverage(proximity, coverage, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `proximity and coverage package lineage must match` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_rejects_arbitrary_source_identity`

**Signature**

```python
def test_coverage_rejects_arbitrary_source_identity(field: str, value: str) -> None:
```

**Purpose**

Protects the `coverage rejects arbitrary source identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `replace(_coverage(), **{field: value})`.
- Computes `coverage.coverage.loc[0, field]` from `value`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='provider|product|identity')` and executes: Calls `assess_grid_coverage(_proximity(), coverage, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='provider|product|identity'): assess_grid_coverage(_proximity(), coverage, SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage rejects arbitrary source identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_summary_selected_count_must_match_frame`

**Signature**

```python
def test_coverage_summary_selected_count_must_match_frame(
    selected_count: int,
) -> None:
```

**Purpose**

Protects the `coverage summary selected count must match frame` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `selected_count`.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `replace(coverage.summary, selected_feature_count=selected_count)`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='selected|count')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='selected|count'): assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage summary selected count must match frame` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_summary_schema_must_match_selected_source_columns`

**Signature**

```python
def test_coverage_summary_schema_must_match_selected_source_columns(
    mutation: str,
) -> None:
```

**Purpose**

Protects the `coverage summary schema must match selected source columns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `coverage.summary`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='summary|column|dtype|schema')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=changed), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`, `reversed`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='summary|column|dtype|schema'): assess_grid_coverage(_proximity(), replace(coverage, summary=changed), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage summary schema must match selected source columns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `reversed`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_summary_crs_must_match_frame`

**Signature**

```python
def test_coverage_summary_crs_must_match_frame() -> None:
```

**Purpose**

Protects the `coverage summary crs must match frame` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `replace(coverage.summary, crs='EPSG:4326')`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='CRS|2154')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='CRS|2154'): assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage summary crs must match frame` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_summary_geometry_facts_are_validated`

**Signature**

```python
def test_coverage_summary_geometry_facts_are_validated(
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `coverage summary geometry facts are validated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `replace(coverage.summary, **{field: value})`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='geometry|summary')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='geometry|summary'): assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage summary geometry facts are validated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_summary_selected_department_must_match`

**Signature**

```python
def test_coverage_summary_selected_department_must_match() -> None:
```

**Purpose**

Protects the `coverage summary selected department must match` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `replace(coverage.summary, selected_department_code='32')`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='department')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='department'): assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage summary selected department must match` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_summary_department_field_must_be_exact`

**Signature**

```python
def test_coverage_summary_department_field_must_be_exact(field: str) -> None:
```

**Purpose**

Protects the `coverage summary department field must be exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `replace(coverage.summary, department_code_field=field)`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='department|field')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='department|field'): assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage summary department field must be exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_summary_source_count_cannot_be_smaller_than_selection`

**Signature**

```python
def test_coverage_summary_source_count_cannot_be_smaller_than_selection() -> None:
```

**Purpose**

Protects the `coverage summary source count cannot be smaller than selection` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `replace(coverage.summary, source_feature_count=0)`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='source|count')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='source|count'): assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage summary source count cannot be smaller than selection` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_source_layer_lineage_must_match_summary_and_frame`

**Signature**

```python
def test_coverage_source_layer_lineage_must_match_summary_and_frame() -> None:
```

**Purpose**

Protects the `coverage source layer lineage must match summary and frame` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `summary` from `replace(coverage.summary, source_layer_name='unknown_layer')`.
- Enters managed context(s) `pytest.raises(GridCoverageAssessmentError, match='layer|lineage')` and executes: Calls `assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `_coverage`, `_proximity`, `assess_grid_coverage`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GridCoverageAssessmentError, match='layer|lineage'): assess_grid_coverage(_proximity(), replace(coverage, summary=summary), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `coverage source layer lineage must match summary and frame` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_proximity`, `assess_grid_coverage`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_assessment_loads_coverage_from_the_physical_source`

**Signature**

```python
def test_public_assessment_loads_coverage_from_the_physical_source() -> None:
```

**Purpose**

Protects the `public assessment loads coverage from the physical source` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `coverage` from `_coverage()`.
- Computes `source` from `_electricity_source(coverage.extraction)`.
- Computes `parcels` from `_parcels()`.
- Computes `proximity` from `_proximity()`.
- Enters managed context(s) `patch('landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity', return_value=proximity)` and executes: Computes `result` from `public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)`.

**Action**

- Calls `_coverage`, `_electricity_source`, `_parcels`, `_proximity`, `public_assess_grid_coverage`.

**Expected result**

- Direct assertions: `assert result.source_coverage.coverage.loc[0, 'nom_officiel'] == 'Haute-Garonne'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public assessment loads coverage from the physical source` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_coverage`, `_electricity_source`, `_parcels`, `_proximity`, `patch`, `public_assess_grid_coverage`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `code_insee` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `coverage` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `department_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_boundary_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `grid_source_coverage_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `id` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `manager_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_post_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `nom_officiel` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `preserved_value` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
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
