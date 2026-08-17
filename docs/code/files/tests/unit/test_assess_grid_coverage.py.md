# `tests/unit/test_assess_grid_coverage.py`

## File identity

- Repository path: `tests/unit/test_assess_grid_coverage.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.
- Source SHA256: `e0292900ee8adfefe03c11377328b02ba5d7e033dde473fcff55180df65a32ec`

## 1. Purpose

Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import json`
- `import tempfile`
- `from copy import deepcopy`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`
- `from uuid import uuid4`

### Third-party packages

- `import geopandas as gpd`
- `import pyogrio`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import (
    LineString,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages import (
    GridCoverageAssessmentError,
    profile_grid_coverage,
)`
- `from landscout.stages import (
    assess_grid_coverage as public_assess_grid_coverage,
)`
- `from landscout.stages.assess_grid_coverage import (
    _assess_grid_coverage_from_proximity as assess_grid_coverage,
)`
- `from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)`

## 4. Contract taxonomy

### A. Python constants

#### `ARCHIVE_SHA256`

```python
ARCHIVE_SHA256 = "a" * 64
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract. Consumers include `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_road_proximity_coverage.py::_archive` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_normalize_access_ign.py::_source` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_context` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference).

#### `EDITION`

```python
EDITION = "2026-06-15"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_road_proximity_coverage.py::_archive` (value argument/reference).

#### `_FIXTURE_ROOT`

```python
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-coverage-ign-"))
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `SOURCE_CONFIG`

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` (value argument/reference).

#### `ALTERNATE_COVERAGE_LAYER`

```python
ALTERNATE_COVERAGE_LAYER = "zone_administrative"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_assess_grid_coverage.py::_with_alternate_coverage_layer` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_coverage`

**Exact signature**

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

Private `test` helper for coverage; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoDepartmentCoverage`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoDepartmentCoverage(extraction=extraction, coverage=frame, summary=summary, source_provider='IGN', source_product='BD TOPO', source_department_code='31', source_edition=EDITION, source_product_version='3.5', source_archive_sha256=ARCHIVE_SHA256, source_layer='departement', spatial_role=spatial_role)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `IgnBdTopoDownload`.
- Filesystem read: `geopackage_path.read_bytes`, `gpd.read_file`.
- Filesystem write: `(extraction_path / '.landscout-extraction.json').write_text`, `extraction_path.mkdir`.
- CRS/geometry calculation: `(non_empty_geometry & ~raw_frame.geometry.is_valid).sum`, `(non_null_geometry & raw_frame.geometry.is_empty).sum`, `frame.geometry.isna`, `raw_frame.geometry.dropna`, `raw_frame.geometry.dropna().geom_type.unique`, `raw_frame.geometry.isna`, `raw_frame.geometry.isna().sum`.
- Hashing: `sha256`, `sha256(payload).hexdigest`, `{'source_provider': 'IGN', 'source_product': 'BD TOPO', 'source_department_code': '31', 'source_edition': EDITION, 'source_product_version': '3.5', 'source_archive_sha256': ARCHIVE_SHA256, 'source_layer': 'departement', 'spatial_role': spatial_role}.items`.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_selected_department_identity_is_exact` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_invalid_coverage_geometry_is_rejected` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_exact_coverage_lineage_is_appended_to_every_row` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_coverage`.

**Complete source-ordered implementation**

```python
def _coverage(
    geometry: object = Polygon(
        [(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]
    ),
    *,
    crs: str | None = "EPSG:2154",
    spatial_role: str = "SOURCE_COVERAGE_BOUNDARY",
) -> IgnBdTopoDepartmentCoverage:
    raw_frame = gpd.GeoDataFrame(
        {
            "code_insee": ["31"],
            "nom_officiel": ["Haute-Garonne"],
        },
        geometry=[geometry],
        crs=crs,
    )
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    dummy = gpd.GeoDataFrame(
        {"id": ["dummy"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs=crs or "EPSG:2154",
    )
    pyogrio.write_dataframe(
        dummy, geopackage_path, layer="ligne_electrique", driver="GPKG"
    )
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="poste_de_transformation",
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        raw_frame,
        geopackage_path,
        layer="departement",
        driver="GPKG",
        append=True,
    )
    raw_frame = gpd.read_file(geopackage_path, layer="departement", engine="pyogrio")
    payload = geopackage_path.read_bytes()
    digest = sha256(payload).hexdigest()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": ARCHIVE_SHA256,
                "geopackage_relative_path": "data.gpkg",
                "geopackage_size_bytes": len(payload),
                "geopackage_sha256": digest,
                "all_layer_names": list(layer_names),
                "electric_lines_layer": "ligne_electrique",
                "transformation_posts_layer": "poste_de_transformation",
                "spatial_role": "PROXY_GEOMETRY",
            }
        ),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider="IGN",
        product="BD TOPO",
        department_code="31",
        edition=EDITION,
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url="https://example.test/BDTOPO.7z",
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO.7z",
        file_size=1,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=extraction_path / "BDTOPO.7z",
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        cache_hit=True,
    )
    frame = raw_frame.copy()
    for column, value in {
        "source_provider": "IGN",
        "source_product": "BD TOPO",
        "source_department_code": "31",
        "source_edition": EDITION,
        "source_product_version": "3.5",
        "source_archive_sha256": ARCHIVE_SHA256,
        "source_layer": "departement",
        "spatial_role": spatial_role,
    }.items():
        frame[column] = value
    geometry_type = tuple(
        sorted(str(value) for value in raw_frame.geometry.dropna().geom_type.unique())
    )
    non_null_geometry = ~frame.geometry.isna()
    non_empty_geometry = non_null_geometry & ~frame.geometry.is_empty
    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name="departement",
        crs=crs or "",
        source_feature_count=1,
        selected_feature_count=1,
        columns=("code_insee", "nom_officiel", "geometry"),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in raw_frame.dtypes.items()),
        null_geometry_count=int(raw_frame.geometry.isna().sum()),
        empty_geometry_count=int(
            (non_null_geometry & raw_frame.geometry.is_empty).sum()
        ),
        invalid_geometry_count=int(
            (non_empty_geometry & ~raw_frame.geometry.is_valid).sum()
        ),
        geometry_types=geometry_type,
        department_code_field="code_insee",
        selected_department_code="31",
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=extraction,
        coverage=frame,
        summary=summary,
        source_provider="IGN",
        source_product="BD TOPO",
        source_department_code="31",
        source_edition=EDITION,
        source_product_version="3.5",
        source_archive_sha256=ARCHIVE_SHA256,
        source_layer="departement",
        spatial_role=spatial_role,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_with_alternate_coverage_layer`

**Exact signature**

```python
def _with_alternate_coverage_layer(
    source: IgnBdTopoDepartmentCoverage,
) -> tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]:
```

**Purpose**

Private `test` helper for with alternate coverage layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]`.
- Every observed return expression is reproduced without truncation:
```python
(configured, forged)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `geopackage_path.read_bytes`, `marker_path.read_text`.
- Filesystem write: `marker_path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: `alternate_config_payload['coverage']['department_layer']`, `configured.coverage['source_layer']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `_with_alternate_coverage_layer`.

**Complete source-ordered implementation**

```python
def _with_alternate_coverage_layer(
    source: IgnBdTopoDepartmentCoverage,
) -> tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]:
    alternate = gpd.GeoDataFrame(
        {"code_insee": ["31"], "nom_officiel": ["Alternate coverage"]},
        geometry=[
            Polygon([(0, 0), (0, 900), (900, 900), (900, 0), (0, 0)])
        ],
        crs="EPSG:2154",
    )
    geopackage_path = source.extraction.geopackage_path
    pyogrio.write_dataframe(
        alternate,
        geopackage_path,
        layer=ALTERNATE_COVERAGE_LAYER,
        driver="GPKG",
        append=True,
    )
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker_path = source.extraction.extraction_path / ".landscout-extraction.json"
    marker = json.loads(marker_path.read_text(encoding="utf-8"))
    marker.update(
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=list(layer_names),
    )
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    extraction = replace(
        source.extraction,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
    )
    configured = replace(
        source,
        extraction=extraction,
        coverage=source.coverage.copy(),
    )
    configured.coverage["source_layer"] = "departement"
    alternate_config_payload = SOURCE_CONFIG.model_dump(mode="python")
    alternate_config_payload["coverage"]["department_layer"] = {
        "class_label": "Zone administrative",
        "match_tokens": ("zone", "administrative"),
        "department_code_field": "code_insee",
    }
    alternate_config = IgnBdTopoSourceConfig.model_validate(
        alternate_config_payload
    )
    forged = load_ign_bdtopo_department_coverage(extraction, alternate_config)
    return configured, forged
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coverage_assessment_reproduces_configured_logical_layer`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
configured, forged = _with_alternate_coverage_layer(_coverage())
```

**Action**

```python
loaded = load_ign_bdtopo_department_coverage(
        configured.extraction, SOURCE_CONFIG
    )
result = assess_grid_coverage(_proximity(), loaded, SOURCE_CONFIG)
```

**Expected result**

```python
assert result.source_coverage.source_layer == "departement"
with pytest.raises(GridCoverageAssessmentError, match="physical|configured"):
        assess_grid_coverage(_proximity(), forged, SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_assessment_reproduces_configured_logical_layer() -> None:
    configured, forged = _with_alternate_coverage_layer(_coverage())

    loaded = load_ign_bdtopo_department_coverage(
        configured.extraction, SOURCE_CONFIG
    )
    result = assess_grid_coverage(_proximity(), loaded, SOURCE_CONFIG)
    assert result.source_coverage.source_layer == "departement"

    with pytest.raises(GridCoverageAssessmentError, match="physical|configured"):
        assess_grid_coverage(_proximity(), forged, SOURCE_CONFIG)
```

### `_parcels`

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    crs: str = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'parcel_id': [f'PARCEL-{position + 1}' for position in range(len(values))], 'preserved_value': list(range(len(values)))}, geometry=values, crs=crs, index=[20 + position for position in range(len(values))])
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_proximity` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_is_frozen_and_has_no_business_decision_fields` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_run` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_invalid_parcel_ids_are_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_reserved_output_column_collision_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_contract_result` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_two_parcel_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_run` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column` via `_parcels`.

**Complete source-ordered implementation**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    crs: str = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])
    ]
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"PARCEL-{position + 1}" for position in range(len(values))],
            "preserved_value": list(range(len(values))),
        },
        geometry=values,
        crs=crs,
        index=[20 + position for position in range(len(values))],
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_lines`

**Exact signature**

```python
def _lines(
    distances: list[float] | None = None,
    *,
    voltage_statuses: list[str] | None = None,
    voltages: list[float | None] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for lines; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'grid_feature_id': identifiers, 'grid_feature_type': ['ELECTRIC_LINE'] * len(values), 'source_feature_id': [f'SOURCE-{value}' for value in identifiers], 'source_department_code': ['31'] * len(values), 'source_edition': [EDITION] * len(values), 'source_archive_sha256': [ARCHIVE_SHA256] * len(values), 'source_layer': ['ligne_electrique'] * len(values), 'spatial_role': ['PROXY_GEOMETRY'] * len(values), 'geometry_status': ['VALID'] * len(values), 'voltage_raw': [None if value is None else str(value) for value in voltage_values], 'voltage_status': statuses, 'voltage_kv': voltage_values, 'voltage_upper_bound_kv': [None] * len(values), 'manager_name': ['RTE'] * len(values), 'asset_status_raw': ['En service'] * len(values)}, geometry=[LineString([(200 + value, 50), (200 + value, 250)]) for value in values], crs='EPSG:2154')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_electricity_source` via `_lines`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_proximity` via `_lines`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_electricity_source` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_lines`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `_lines`.

**Complete source-ordered implementation**

```python
def _lines(
    distances: list[float] | None = None,
    *,
    voltage_statuses: list[str] | None = None,
    voltages: list[float | None] | None = None,
) -> gpd.GeoDataFrame:
    values = distances or [50.0]
    statuses = voltage_statuses or ["EXACT"] * len(values)
    voltage_values = voltages or [110.0] * len(values)
    identifiers = [f"LINE-{position + 1}" for position in range(len(values))]
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": identifiers,
            "grid_feature_type": ["ELECTRIC_LINE"] * len(values),
            "source_feature_id": [f"SOURCE-{value}" for value in identifiers],
            "source_department_code": ["31"] * len(values),
            "source_edition": [EDITION] * len(values),
            "source_archive_sha256": [ARCHIVE_SHA256] * len(values),
            "source_layer": ["ligne_electrique"] * len(values),
            "spatial_role": ["PROXY_GEOMETRY"] * len(values),
            "geometry_status": ["VALID"] * len(values),
            "voltage_raw": [None if value is None else str(value) for value in voltage_values],
            "voltage_status": statuses,
            "voltage_kv": voltage_values,
            "voltage_upper_bound_kv": [None] * len(values),
            "manager_name": ["RTE"] * len(values),
            "asset_status_raw": ["En service"] * len(values),
        },
        geometry=[
            LineString([(200 + value, 50), (200 + value, 250)])
            for value in values
        ],
        crs="EPSG:2154",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_posts`

**Exact signature**

```python
def _posts(distance_m: float = 50.0) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for posts; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'grid_feature_id': ['POST-1'], 'grid_feature_type': ['TRANSFORMATION_POST'], 'source_feature_id': ['SOURCE-POST-1'], 'source_department_code': ['31'], 'source_edition': [EDITION], 'source_archive_sha256': [ARCHIVE_SHA256], 'source_layer': ['poste_de_transformation'], 'spatial_role': ['PROXY_GEOMETRY'], 'geometry_status': ['VALID'], 'name': ['Test post'], 'importance_raw': ['5'], 'asset_status_raw': ['En service']}, geometry=[Polygon([(200 + distance_m, 100), (200 + distance_m, 110), (210 + distance_m, 110), (210 + distance_m, 100), (200 + distance_m, 100)])], crs='EPSG:2154')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_electricity_source` via `_posts`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_proximity` via `_posts`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_electricity_source` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_posts`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `_posts`.

**Complete source-ordered implementation**

```python
def _posts(distance_m: float = 50.0) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ["POST-1"],
            "grid_feature_type": ["TRANSFORMATION_POST"],
            "source_feature_id": ["SOURCE-POST-1"],
            "source_department_code": ["31"],
            "source_edition": [EDITION],
            "source_archive_sha256": [ARCHIVE_SHA256],
            "source_layer": ["poste_de_transformation"],
            "spatial_role": ["PROXY_GEOMETRY"],
            "geometry_status": ["VALID"],
            "name": ["Test post"],
            "importance_raw": ["5"],
            "asset_status_raw": ["En service"],
        },
        geometry=[
            Polygon(
                [
                    (200 + distance_m, 100),
                    (200 + distance_m, 110),
                    (210 + distance_m, 110),
                    (210 + distance_m, 100),
                    (200 + distance_m, 100),
                ]
            )
        ],
        crs="EPSG:2154",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_electricity_source`

**Exact signature**

```python
def _electricity_source(
    extraction: IgnBdTopoExtraction,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Private `test` helper for electricity source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoElectricityData(extraction=extraction, electric_lines=_lines(), transformation_posts=_posts(), electric_lines_summary=cast(Any, None), transformation_posts_summary=cast(Any, None))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_electricity_source`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `_electricity_source`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_electricity_source`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_electricity_source`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types` via `_electricity_source`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation` via `_electricity_source`.

**Complete source-ordered implementation**

```python
def _electricity_source(
    extraction: IgnBdTopoExtraction,
) -> IgnBdTopoElectricityData:
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=_lines(),
        transformation_posts=_posts(),
        electric_lines_summary=cast(Any, None),
        transformation_posts_summary=cast(Any, None),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_proximity`

**Exact signature**

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

Private `test` helper for proximity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
enrich_parcel_grid_proximity(_parcels(parcel_geometries, crs=parcel_crs), _lines(line_distances, voltage_statuses=voltage_statuses, voltages=voltages), _posts(post_distance_m))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_road_lineage_must_match_coverage` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `_proximity`.

**Complete source-ordered implementation**

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
    return enrich_parcel_grid_proximity(
        _parcels(parcel_geometries, crs=parcel_crs),
        _lines(
            line_distances,
            voltage_statuses=voltage_statuses,
            voltages=voltages,
        ),
        _posts(post_distance_m),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_clean_coverage_api_is_exported`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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
assert stages.assess_grid_coverage is public_assess_grid_coverage
assert stages.profile_grid_coverage is profile_grid_coverage
assert "assess_grid_coverage" in stages.__all__
assert "profile_grid_coverage" in stages.__all__
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_clean_coverage_api_is_exported() -> None:
    assert stages.assess_grid_coverage is public_assess_grid_coverage
    assert stages.profile_grid_coverage is profile_grid_coverage
    assert "assess_grid_coverage" in stages.__all__
    assert "profile_grid_coverage" in stages.__all__
```

### `test_public_coverage_owns_proximity_and_configured_coverage_once`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
source = _electricity_source(coverage.extraction)
parcels = _parcels()
proximity = _proximity()
proximity_stage.assert_called_once_with(parcels, source, SOURCE_CONFIG)
coverage_loader.assert_called_once_with(source.extraction, SOURCE_CONFIG)
```

**Action**

```python
with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        return_value=proximity,
        create=True,
    ) as proximity_stage, patch(
        "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
        return_value=coverage,
        create=True,
    ) as coverage_loader:
        result = public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)
```

**Expected result**

```python
assert result.source_coverage is coverage
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_public_coverage_owns_proximity_and_configured_coverage_once() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity()

    with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        return_value=proximity,
        create=True,
    ) as proximity_stage, patch(
        "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
        return_value=coverage,
        create=True,
    ) as coverage_loader:
        result = public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)

    proximity_stage.assert_called_once_with(parcels, source, SOURCE_CONFIG)
    coverage_loader.assert_called_once_with(source.extraction, SOURCE_CONFIG)
    assert result.source_coverage is coverage
```

### `test_public_coverage_proximity_failure_stops_coverage_loading`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
source = _electricity_source(coverage.extraction)
proximity_stage.assert_called_once()
coverage_loader.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        side_effect=ValueError("physical electricity source changed"),
        create=True,
    ) as proximity_stage, patch(
        "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
        create=True,
    ) as coverage_loader, pytest.raises(GridCoverageAssessmentError):
        public_assess_grid_coverage(_parcels(), source, SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_public_coverage_proximity_failure_stops_coverage_loading() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)

    with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        side_effect=ValueError("physical electricity source changed"),
        create=True,
    ) as proximity_stage, patch(
        "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
        create=True,
    ) as coverage_loader, pytest.raises(GridCoverageAssessmentError):
        public_assess_grid_coverage(_parcels(), source, SOURCE_CONFIG)

    proximity_stage.assert_called_once()
    coverage_loader.assert_not_called()
```

### `test_caller_provided_proximity_and_coverage_are_not_public_inputs`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
forged_proximity = _proximity(line_distances=[0.0], post_distance_m=0.0)
forged_coverage = _coverage()
proximity_stage.assert_not_called()
coverage_loader.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert forged_proximity.parcels[
        "nearest_line_proxy_distance_m"
    ].eq(0.0).all()
assert forged_proximity.parcels[
        "nearest_line_source_archive_sha256"
    ].eq(ARCHIVE_SHA256).all()
with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        create=True,
    ) as proximity_stage, patch(
        "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
        create=True,
    ) as coverage_loader, pytest.raises(
        GridCoverageAssessmentError,
        match="parcels|GeoDataFrame",
    ):
        public_assess_grid_coverage(
            cast(Any, forged_proximity),
            cast(Any, forged_coverage),
            SOURCE_CONFIG,
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_caller_provided_proximity_and_coverage_are_not_public_inputs() -> None:
    forged_proximity = _proximity(line_distances=[0.0], post_distance_m=0.0)
    forged_coverage = _coverage()
    assert forged_proximity.parcels[
        "nearest_line_proxy_distance_m"
    ].eq(0.0).all()
    assert forged_proximity.parcels[
        "nearest_line_source_archive_sha256"
    ].eq(ARCHIVE_SHA256).all()

    with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        create=True,
    ) as proximity_stage, patch(
        "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
        create=True,
    ) as coverage_loader, pytest.raises(
        GridCoverageAssessmentError,
        match="parcels|GeoDataFrame",
    ):
        public_assess_grid_coverage(
            cast(Any, forged_proximity),
            cast(Any, forged_coverage),
            SOURCE_CONFIG,
        )

    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()
```

### `test_polygonal_coverage_geometry_is_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
result = assess_grid_coverage(_proximity(), _coverage(geometry), SOURCE_CONFIG)
```

**Expected result**

```python
assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    result = assess_grid_coverage(_proximity(), _coverage(geometry), SOURCE_CONFIG)

    assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0
    )
```

### `test_invalid_coverage_geometry_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `crs`, `geometry`, `message`.

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
with pytest.raises(GridCoverageAssessmentError, match=message):
        assess_grid_coverage(
            _proximity(), _coverage(geometry, crs=crs), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_coverage_geometry_is_rejected(
    geometry: object,
    crs: str | None,
    message: str,
) -> None:
    with pytest.raises(GridCoverageAssessmentError, match=message):
        assess_grid_coverage(
            _proximity(), _coverage(geometry, crs=crs), SOURCE_CONFIG
        )
```

### `test_strict_geometric_boundary_proof`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `asset_distance`, `expected_status`.

**Setup**

```python
parcel = result.parcels.iloc[0]
```

**Action**

```python
result = assess_grid_coverage(
        _proximity(line_distances=[asset_distance], post_distance_m=asset_distance),
        _coverage(),
        SOURCE_CONFIG,
    )
```

**Expected result**

```python
assert parcel["grid_source_boundary_distance_m"] == pytest.approx(100.0)
assert parcel["nearest_line_proxy_distance_m"] == pytest.approx(asset_distance)
assert parcel["nearest_line_coverage_status"] == expected_status
assert parcel["nearest_exact_line_coverage_status"] == expected_status
assert parcel["nearest_post_coverage_status"] == expected_status
assert result.voltage_level_proximity.loc[0, "coverage_status"] == expected_status
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_strict_geometric_boundary_proof(
    asset_distance: float,
    expected_status: str,
) -> None:
    result = assess_grid_coverage(
        _proximity(line_distances=[asset_distance], post_distance_m=asset_distance),
        _coverage(),
        SOURCE_CONFIG,
    )

    parcel = result.parcels.iloc[0]
    assert parcel["grid_source_boundary_distance_m"] == pytest.approx(100.0)
    assert parcel["nearest_line_proxy_distance_m"] == pytest.approx(asset_distance)
    assert parcel["nearest_line_coverage_status"] == expected_status
    assert parcel["nearest_exact_line_coverage_status"] == expected_status
    assert parcel["nearest_post_coverage_status"] == expected_status
    assert result.voltage_level_proximity.loc[0, "coverage_status"] == expected_status
```

### `test_outside_crossing_or_touching_parcel_is_conservative`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `parcel_geometry`.

**Setup**

```python
parcel = result.parcels.iloc[0]
```

**Action**

```python
result = assess_grid_coverage(
        _proximity(parcel_geometries=[parcel_geometry]),
        _coverage(),
        SOURCE_CONFIG,
    )
```

**Expected result**

```python
assert parcel["grid_source_boundary_distance_m"] == 0.0
assert parcel["grid_source_coverage_position"] == "OUTSIDE_OR_CROSSING_COVERAGE"
assert parcel["nearest_line_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"
assert parcel["nearest_exact_line_coverage_status"] == (
        "OUTSIDE_OR_CROSSING_COVERAGE"
    )
assert parcel["nearest_post_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"
assert result.voltage_level_proximity.loc[0, "coverage_status"] == (
        "OUTSIDE_OR_CROSSING_COVERAGE"
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_outside_crossing_or_touching_parcel_is_conservative(
    parcel_geometry: Polygon,
) -> None:
    result = assess_grid_coverage(
        _proximity(parcel_geometries=[parcel_geometry]),
        _coverage(),
        SOURCE_CONFIG,
    )

    parcel = result.parcels.iloc[0]
    assert parcel["grid_source_boundary_distance_m"] == 0.0
    assert parcel["grid_source_coverage_position"] == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert parcel["nearest_line_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert parcel["nearest_exact_line_coverage_status"] == (
        "OUTSIDE_OR_CROSSING_COVERAGE"
    )
    assert parcel["nearest_post_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert result.voltage_level_proximity.loc[0, "coverage_status"] == (
        "OUTSIDE_OR_CROSSING_COVERAGE"
    )
```

### `test_no_exact_match_uses_explicit_no_match_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
proximity = _proximity(
        voltage_statuses=["UNKNOWN"],
        voltages=[None],
    )
```

**Action**

```python
result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)
```

**Expected result**

```python
assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
assert result.parcels["nearest_exact_line_coverage_status"].eq("NO_MATCH").all()
assert result.voltage_level_proximity.empty
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_no_exact_match_uses_explicit_no_match_status() -> None:
    proximity = _proximity(
        voltage_statuses=["UNKNOWN"],
        voltages=[None],
    )
    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_coverage_status"].eq("NO_MATCH").all()
    assert result.voltage_level_proximity.empty
```

### `test_assessment_preserves_proximity_values_and_does_not_mutate_input`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
proximity = _proximity(line_distances=[50.0, 150.0], voltages=[110.0, 275.0])
parcels_before = deepcopy(proximity.parcels)
table_before = deepcopy(proximity.voltage_level_proximity)
assert_geodataframe_equal(proximity.parcels, parcels_before)
assert_frame_equal(proximity.voltage_level_proximity, table_before)
assert_geodataframe_equal(
        result.parcels.loc[:, parcels_before.columns],
        parcels_before,
    )
assert_frame_equal(
        result.voltage_level_proximity.loc[:, table_before.columns],
        table_before,
    )
```

**Action**

```python
result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)
```

**Expected result**

```python
assert result.parcels["parcel_id"].tolist() == parcels_before["parcel_id"].tolist()
assert result.voltage_level_proximity[
        ["parcel_id", "voltage_kv"]
    ].equals(table_before[["parcel_id", "voltage_kv"]])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_assessment_preserves_proximity_values_and_does_not_mutate_input() -> None:
    proximity = _proximity(line_distances=[50.0, 150.0], voltages=[110.0, 275.0])
    parcels_before = deepcopy(proximity.parcels)
    table_before = deepcopy(proximity.voltage_level_proximity)

    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert_geodataframe_equal(proximity.parcels, parcels_before)
    assert_frame_equal(proximity.voltage_level_proximity, table_before)
    assert_geodataframe_equal(
        result.parcels.loc[:, parcels_before.columns],
        parcels_before,
    )
    assert_frame_equal(
        result.voltage_level_proximity.loc[:, table_before.columns],
        table_before,
    )
    assert result.parcels["parcel_id"].tolist() == parcels_before["parcel_id"].tolist()
    assert result.voltage_level_proximity[
        ["parcel_id", "voltage_kv"]
    ].equals(table_before[["parcel_id", "voltage_kv"]])
```

### `test_geographic_parcel_storage_crs_and_geometry_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
projected = _parcels()
geographic = projected.to_crs("EPSG:4326")
```

**Action**

```python
proximity = enrich_parcel_grid_proximity(geographic, _lines(), _posts())
result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)
```

**Expected result**

```python
assert result.parcels.crs.to_epsg() == 4326
assert result.parcels.geometry.geom_equals_exact(
        proximity.parcels.geometry, tolerance=0, align=False
    ).all()
assert result.parcels.iloc[0][
        "grid_source_boundary_distance_m"
    ] == pytest.approx(100.0, abs=1e-6)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_geographic_parcel_storage_crs_and_geometry_are_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    proximity = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert result.parcels.crs.to_epsg() == 4326
    assert result.parcels.geometry.geom_equals_exact(
        proximity.parcels.geometry, tolerance=0, align=False
    ).all()
    assert result.parcels.iloc[0][
        "grid_source_boundary_distance_m"
    ] == pytest.approx(100.0, abs=1e-6)
```

### `test_profile_reports_dynamic_voltage_and_boundary_distributions`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
result = assess_grid_coverage(
        _proximity(
            line_distances=[50.0, 150.0],
            post_distance_m=100.0,
            voltages=[110.0, 275.0],
        ),
        _coverage(),
        SOURCE_CONFIG,
    )
profile = profile_grid_coverage(result)
```

**Expected result**

```python
assert profile.parcel_count == 1
assert profile.fully_covered_count == 1
assert profile.outside_or_crossing_count == 0
assert profile.boundary_distance.minimum == pytest.approx(100.0)
assert profile.boundary_distance.p50 == pytest.approx(100.0)
assert profile.boundary_distance.maximum == pytest.approx(100.0)
assert profile.nearest_line.not_boundary_limited == 1
assert profile.nearest_post.boundary_limited == 1
assert [item.voltage_kv for item in profile.voltage_levels] == [110.0, 275.0]
assert profile.voltage_levels[0].statuses.not_boundary_limited == 1
assert profile.voltage_levels[1].statuses.boundary_limited == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_profile_reports_dynamic_voltage_and_boundary_distributions() -> None:
    result = assess_grid_coverage(
        _proximity(
            line_distances=[50.0, 150.0],
            post_distance_m=100.0,
            voltages=[110.0, 275.0],
        ),
        _coverage(),
        SOURCE_CONFIG,
    )

    profile = profile_grid_coverage(result)

    assert profile.parcel_count == 1
    assert profile.fully_covered_count == 1
    assert profile.outside_or_crossing_count == 0
    assert profile.boundary_distance.minimum == pytest.approx(100.0)
    assert profile.boundary_distance.p50 == pytest.approx(100.0)
    assert profile.boundary_distance.maximum == pytest.approx(100.0)
    assert profile.nearest_line.not_boundary_limited == 1
    assert profile.nearest_post.boundary_limited == 1
    assert [item.voltage_kv for item in profile.voltage_levels] == [110.0, 275.0]
    assert profile.voltage_levels[0].statuses.not_boundary_limited == 1
    assert profile.voltage_levels[1].statuses.boundary_limited == 1
```

### `test_proximity_and_coverage_package_lineage_must_match`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
proximity = _proximity()
coverage = _coverage()
coverage.coverage.loc[0, "source_archive_sha256"] = "b" * 64
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="lineage"):
        assess_grid_coverage(proximity, coverage, SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_proximity_and_coverage_package_lineage_must_match() -> None:
    proximity = _proximity()
    coverage = _coverage()
    coverage.coverage.loc[0, "source_archive_sha256"] = "b" * 64

    with pytest.raises(GridCoverageAssessmentError, match="lineage"):
        assess_grid_coverage(proximity, coverage, SOURCE_CONFIG)
```

### `test_coverage_rejects_arbitrary_source_identity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
coverage = replace(_coverage(), **{field: value})
coverage.coverage.loc[0, field] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="provider|product|identity"):
        assess_grid_coverage(_proximity(), coverage, SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_rejects_arbitrary_source_identity(field: str, value: str) -> None:
    coverage = replace(_coverage(), **{field: value})
    coverage.coverage.loc[0, field] = value

    with pytest.raises(GridCoverageAssessmentError, match="provider|product|identity"):
        assess_grid_coverage(_proximity(), coverage, SOURCE_CONFIG)
```

### `test_coverage_summary_selected_count_must_match_frame`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `selected_count`.

**Setup**

```python
coverage = _coverage()
summary = replace(
        coverage.summary,
        selected_feature_count=selected_count,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="selected|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_summary_selected_count_must_match_frame(
    selected_count: int,
) -> None:
    coverage = _coverage()
    summary = replace(
        coverage.summary,
        selected_feature_count=selected_count,
    )

    with pytest.raises(GridCoverageAssessmentError, match="selected|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

### `test_coverage_summary_schema_must_match_selected_source_columns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
coverage = _coverage()
summary = coverage.summary
if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "float64")
        changed = replace(summary, dtypes=tuple(dtypes))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="summary|column|dtype|schema"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=changed), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_summary_schema_must_match_selected_source_columns(
    mutation: str,
) -> None:
    coverage = _coverage()
    summary = coverage.summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "float64")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(GridCoverageAssessmentError, match="summary|column|dtype|schema"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=changed), SOURCE_CONFIG
        )
```

### `test_coverage_summary_crs_must_match_frame`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
summary = replace(coverage.summary, crs="EPSG:4326")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="CRS|2154"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_summary_crs_must_match_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, crs="EPSG:4326")

    with pytest.raises(GridCoverageAssessmentError, match="CRS|2154"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

### `test_coverage_summary_geometry_facts_are_validated`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
coverage = _coverage()
summary = replace(coverage.summary, **{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="geometry|summary"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_coverage_summary_geometry_facts_are_validated(
    field: str,
    value: object,
) -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, **{field: value})

    with pytest.raises(GridCoverageAssessmentError, match="geometry|summary"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

### `test_coverage_summary_selected_department_must_match`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
summary = replace(coverage.summary, selected_department_code="32")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="department"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_summary_selected_department_must_match() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, selected_department_code="32")

    with pytest.raises(GridCoverageAssessmentError, match="department"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

### `test_coverage_summary_department_field_must_be_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
coverage = _coverage()
summary = replace(coverage.summary, department_code_field=field)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="department|field"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_summary_department_field_must_be_exact(field: str) -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, department_code_field=field)

    with pytest.raises(GridCoverageAssessmentError, match="department|field"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

### `test_coverage_summary_source_count_cannot_be_smaller_than_selection`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
summary = replace(coverage.summary, source_feature_count=0)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="source|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_summary_source_count_cannot_be_smaller_than_selection() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_feature_count=0)

    with pytest.raises(GridCoverageAssessmentError, match="source|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

### `test_coverage_source_layer_lineage_must_match_summary_and_frame`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
summary = replace(coverage.summary, source_layer_name="unknown_layer")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GridCoverageAssessmentError, match="layer|lineage"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_source_layer_lineage_must_match_summary_and_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_layer_name="unknown_layer")

    with pytest.raises(GridCoverageAssessmentError, match="layer|lineage"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

### `test_public_assessment_loads_coverage_from_the_physical_source`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
source = _electricity_source(coverage.extraction)
parcels = _parcels()
proximity = _proximity()
```

**Action**

```python
with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        return_value=proximity,
    ):
        result = public_assess_grid_coverage(
            parcels,
            source,
            SOURCE_CONFIG,
        )
```

**Expected result**

```python
assert result.source_coverage.coverage.loc[0, "nom_officiel"] == "Haute-Garonne"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_public_assessment_loads_coverage_from_the_physical_source() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity()

    with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        return_value=proximity,
    ):
        result = public_assess_grid_coverage(
            parcels,
            source,
            SOURCE_CONFIG,
        )

    assert result.source_coverage.coverage.loc[0, "nom_officiel"] == "Haute-Garonne"
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
