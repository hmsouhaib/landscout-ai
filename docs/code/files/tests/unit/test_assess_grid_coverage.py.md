# `tests/unit/test_assess_grid_coverage.py`

## File identity

- Repository path: `tests/unit/test_assess_grid_coverage.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.
- Source SHA256: `b2a00d7b4008fdd2daea8fd858866d9d7f51a452aa9da2cd0af6f37c67494664`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for assess grid coverage; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

- `import landscout.sources.ign_bdtopo_fr as ign_source`
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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `ARCHIVE_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_SHA256 = "a" * 64
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EDITION`

- Category: module constant or closed domain.
- Exact declaration:

```python
EDITION = "2026-06-15"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_FIXTURE_ROOT`

- Category: module constant or closed domain.
- Exact declaration:

```python
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-coverage-ign-"))
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SOURCE_CONFIG_PAYLOAD`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SOURCE_CONFIG_PAYLOAD = load_ign_bdtopo_source_config().model_dump(mode="json")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SOURCE_CONFIG`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_CONFIG = IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ALTERNATE_COVERAGE_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
ALTERNATE_COVERAGE_LAYER = "zone_administrative"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

### Module-import-time executable statement at line 53

- Category: executable import-time registration/guard/statement; it is not a constant or function-local side effect.
- Exact call expressions: `_SOURCE_CONFIG_PAYLOAD.update`.
- Exact statement:

```python
_SOURCE_CONFIG_PAYLOAD.update(
    {
        "source_url": "https://example.test/BDTOPO.7z",
        "checksum_url": None,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "expected_archive_size_bytes": 1,
    }
)
```


## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_coverage`

**Purpose:** Implements `coverage` within the file role: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

**Exact signature**

```python
def _coverage(
    geometry: object = Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
    *,
    crs: str | None = "EPSG:2154",
    spatial_role: str = "SOURCE_COVERAGE_BOUNDARY",
) -> IgnBdTopoDepartmentCoverage:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDepartmentCoverage`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `spatial_role` | keyword-only | `str` | `'SOURCE_COVERAGE_BOUNDARY'` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoDepartmentCoverage(<br>        extraction=extraction,<br>        coverage=frame,<br>        summary=summary,<br>        source_provider=SOURCE_CONFIG.provider,<br>        source_product="BD TOPO",<br>        source_department_code="31",<br>        source_edition=EDITION,<br>        source_product_version="3.5",<br>        source_archive_sha256=ARCHIVE_SHA256,<br>        source_layer="departement",<br>        spatial_role=spatial_role,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_proximity_failure_stops_coverage_loading` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_proximity_failure_stops_coverage_loading` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_polygonal_coverage_geometry_is_accepted` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_polygonal_coverage_geometry_is_accepted` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_invalid_coverage_geometry_is_rejected` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_invalid_coverage_geometry_is_rejected` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_strict_geometric_boundary_proof` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_strict_geometric_boundary_proof` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_outside_crossing_or_touching_parcel_is_conservative` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_outside_crossing_or_touching_parcel_is_conservative` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_no_exact_match_uses_explicit_no_match_status` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_no_exact_match_uses_explicit_no_match_status` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_proximity_and_coverage_package_lineage_must_match` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_proximity_and_coverage_package_lineage_must_match` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_rejects_arbitrary_source_identity` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_rejects_arbitrary_source_identity` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_count_must_match_frame` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_count_must_match_frame` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_schema_must_match_selected_source_columns` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_schema_must_match_selected_source_columns` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_crs_must_match_frame` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_crs_must_match_frame` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_geometry_facts_are_validated` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_geometry_facts_are_validated` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_department_must_match` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_department_must_match` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_department_field_must_be_exact` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_department_field_must_be_exact` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `uuid4` | `uuid.uuid4` |
| `extraction_path.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `LineString` | `shapely.geometry.LineString` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `gpd.read_file` | `geopandas.read_file` |
| `geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `(extraction_path / ".landscout-extraction.json").write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownload` | `landscout.sources.IgnBdTopoDownload` |
| `IgnBdTopoExtraction` | `landscout.sources.IgnBdTopoExtraction` |
| `raw_frame.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `{<br>        "source_provider": SOURCE_CONFIG.provider,<br>        "source_product": "BD TOPO",<br>        "source_department_code": "31",<br>        "source_edition": EDITION,<br>        "source_product_version": "3.5",<br>        "source_archive_sha256": ARCHIVE_SHA256,<br>        "source_layer": "departement",<br>        "spatial_role": spatial_role,<br>    }.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_frame.geometry.dropna().geom_type.unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_frame.geometry.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoCoverageLayerSummary` | `landscout.sources.IgnBdTopoCoverageLayerSummary` |
| `raw_frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_frame.geometry.isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_frame.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null_geometry & raw_frame.geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_empty_geometry & ~raw_frame.geometry.is_valid).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDepartmentCoverage` | `landscout.sources.IgnBdTopoDepartmentCoverage` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file`<br>`geopackage_path.read_bytes` |
| Filesystem/archive write or publication | `extraction_path.mkdir`<br>`(extraction_path / ".landscout-extraction.json").write_text` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256`<br>`{<br>        "source_provider": SOURCE_CONFIG.provider,<br>        "source_product": "BD TOPO",<br>        "source_department_code": "31",<br>        "source_edition": EDITION,<br>        "source_product_version": "3.5",<br>        "source_archive_sha256": ARCHIVE_SHA256,<br>        "source_layer": "departement",<br>        "spatial_role": spatial_role,<br>    }.items` |
| CRS/geometry/spatial calculation | `raw_frame.geometry.dropna().geom_type.unique`<br>`raw_frame.geometry.dropna`<br>`frame.geometry.isna`<br>`raw_frame.geometry.isna().sum`<br>`raw_frame.geometry.isna`<br>`(non_null_geometry & raw_frame.geometry.is_empty).sum`<br>`(non_empty_geometry & ~raw_frame.geometry.is_valid).sum` |
| External process/environment | None directly present. |
| In-memory mutation | `frame[column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _coverage(
    geometry: object = Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
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
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="troncon_de_route",
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
                "schema_version": 3,
                "archive_sha256": ARCHIVE_SHA256,
                "geopackage_relative_path": "data.gpkg",
                "geopackage_size_bytes": len(payload),
                "geopackage_sha256": digest,
                "all_layer_names": list(layer_names),
                "electric_lines_layer": "ligne_electrique",
                "transformation_posts_layer": "poste_de_transformation",
                "road_segments_layer": "troncon_de_route",
                "department_layer": "departement",
                "extracted_entries": [
                    {
                        "relative_path": "data.gpkg",
                        "kind": "file",
                        "size_bytes": len(payload),
                        "sha256": digest,
                    }
                ],
                "spatial_role": "PROXY_GEOMETRY",
            }
        ),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
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
        road_segments_layer="troncon_de_route",
        department_layer="departement",
        cache_hit=True,
    )
    frame = raw_frame.copy()
    for column, value in {
        "source_provider": SOURCE_CONFIG.provider,
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
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in raw_frame.dtypes.items()
        ),
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
        source_provider=SOURCE_CONFIG.provider,
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_with_alternate_coverage_layer`

**Purpose:** Implements `with alternate coverage layer` within the file role: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

**Exact signature**

```python
def _with_alternate_coverage_layer(
    source: IgnBdTopoDepartmentCoverage,
) -> tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `configured, forged`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `_with_alternate_coverage_layer`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `_with_alternate_coverage_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `json.loads` | `json.loads` |
| `marker_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `replace` | `dataclasses.replace` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.load_ign_bdtopo_department_coverage` |
| `gpd.read_file` | `geopandas.read_file` |
| `ign_source._department_coverage_from_frame` | `landscout.sources.ign_bdtopo_fr._department_coverage_from_frame` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `geopackage_path.read_bytes`<br>`marker_path.read_text`<br>`gpd.read_file` |
| Filesystem/archive write or publication | `marker_path.write_text` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `marker.update(<br>        geopackage_size_bytes=len(payload),<br>        geopackage_sha256=digest,<br>        all_layer_names=list(layer_names),<br>        extracted_entries=[<br>            {<br>                "relative_path": "data.gpkg",<br>                "kind": "file",<br>                "size_bytes": len(payload),<br>                "sha256": digest,<br>            }<br>        ],<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _with_alternate_coverage_layer(
    source: IgnBdTopoDepartmentCoverage,
) -> tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]:
    alternate = gpd.GeoDataFrame(
        {"code_insee": ["31"], "nom_officiel": ["Alternate coverage"]},
        geometry=[Polygon([(0, 0), (0, 900), (900, 900), (900, 0), (0, 0)])],
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
        extracted_entries=[
            {
                "relative_path": "data.gpkg",
                "kind": "file",
                "size_bytes": len(payload),
                "sha256": digest,
            }
        ],
    )
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    extraction = replace(
        source.extraction,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
    )
    configured = load_ign_bdtopo_department_coverage(
        extraction,
        SOURCE_CONFIG,
    )
    alternate_loaded = gpd.read_file(
        geopackage_path,
        layer=ALTERNATE_COVERAGE_LAYER,
        engine="pyogrio",
    )
    forged = ign_source._department_coverage_from_frame(
        extraction,
        alternate_loaded,
        ALTERNATE_COVERAGE_LAYER,
        "code_insee",
    )
    return configured, forged
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_assessment_reproduces_configured_logical_layer`

**Purpose:** Regression invariant: coverage assessment reproduces configured logical layer. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_assessment_reproduces_configured_logical_layer() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="physical\|configured")`
- Exact assertions:
  - `assert result.source_coverage.source_layer == "departement"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_with_alternate_coverage_layer` | `tests.unit.test_assess_grid_coverage._with_alternate_coverage_layer` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.load_ign_bdtopo_department_coverage` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coverage_assessment_reproduces_configured_logical_layer() -> None:
    configured, forged = _with_alternate_coverage_layer(_coverage())

    loaded = load_ign_bdtopo_department_coverage(configured.extraction, SOURCE_CONFIG)
    result = assess_grid_coverage(_proximity(), loaded, SOURCE_CONFIG)
    assert result.source_coverage.source_layer == "departement"

    with pytest.raises(GridCoverageAssessmentError, match="physical|configured"):
        assess_grid_coverage(_proximity(), forged, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    crs: str = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str` | `'EPSG:2154'` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "parcel_id": [f"PARCEL-{position + 1}" for position in range(len(values))],<br>            "preserved_value": list(range(len(values))),<br>        },<br>        geometry=values,<br>        crs=crs,<br>        index=[20 + position for position in range(len(values))],<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_grid_coverage::_proximity` via `_parcels`
- value/type reference: `tests.unit.test_assess_grid_coverage::_proximity` via `_parcels`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_parcels`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_parcels`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_proximity_failure_stops_coverage_loading` via `_parcels`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_proximity_failure_stops_coverage_loading` via `_parcels`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_rejects_generated_parcel_column_before_proximity` via `_parcels`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_rejects_generated_parcel_column_before_proximity` via `_parcels`
- direct call: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_parcels`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_parcels`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_parcels`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_lines`

**Purpose:** Implements `lines` within the file role: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

**Exact signature**

```python
def _lines(
    distances: list[float] | None = None,
    *,
    voltage_statuses: list[str] | None = None,
    voltages: list[float | None] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `distances` | positional-or-keyword | `list[float] \| None` | `None` |
| `voltage_statuses` | keyword-only | `list[str] \| None` | `None` |
| `voltages` | keyword-only | `list[float \| None] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "grid_feature_id": identifiers,<br>            "grid_feature_type": ["ELECTRIC_LINE"] * len(values),<br>            "source_feature_id": [f"SOURCE-{value}" for value in identifiers],<br>            "source_department_code": ["31"] * len(values),<br>            "source_edition": [EDITION] * len(values),<br>            "source_archive_sha256": [ARCHIVE_SHA256] * len(values),<br>            "source_layer": ["ligne_electrique"] * len(values),<br>            "spatial_role": ["PROXY_GEOMETRY"] * len(values),<br>            "geometry_status": ["VALID"] * len(values),<br>            "voltage_raw": [<br>                None if value is None else str(value) for value in voltage_values<br>            ],<br>            "voltage_status": statuses,<br>            "voltage_kv": voltage_values,<br>            "voltage_upper_bound_kv": [None] * len(values),<br>            "manager_name": ["RTE"] * len(values),<br>            "asset_status_raw": ["En service"] * len(values),<br>        },<br>        geometry=[<br>            LineString([(200 + value, 50), (200 + value, 250)]) for value in values<br>        ],<br>        crs="EPSG:2154",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_grid_coverage::_electricity_source` via `_lines`
- value/type reference: `tests.unit.test_assess_grid_coverage::_electricity_source` via `_lines`
- direct call: `tests.unit.test_assess_grid_coverage::_proximity` via `_lines`
- value/type reference: `tests.unit.test_assess_grid_coverage::_proximity` via `_lines`
- direct call: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_lines`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_lines`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `LineString` | `shapely.geometry.LineString` |

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
            "voltage_raw": [
                None if value is None else str(value) for value in voltage_values
            ],
            "voltage_status": statuses,
            "voltage_kv": voltage_values,
            "voltage_upper_bound_kv": [None] * len(values),
            "manager_name": ["RTE"] * len(values),
            "asset_status_raw": ["En service"] * len(values),
        },
        geometry=[
            LineString([(200 + value, 50), (200 + value, 250)]) for value in values
        ],
        crs="EPSG:2154",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_posts`

**Purpose:** Implements `posts` within the file role: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

**Exact signature**

```python
def _posts(distance_m: float = 50.0) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `distance_m` | positional-or-keyword | `float` | `50.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "grid_feature_id": ["POST-1"],<br>            "grid_feature_type": ["TRANSFORMATION_POST"],<br>            "source_feature_id": ["SOURCE-POST-1"],<br>            "source_department_code": ["31"],<br>            "source_edition": [EDITION],<br>            "source_archive_sha256": [ARCHIVE_SHA256],<br>            "source_layer": ["poste_de_transformation"],<br>            "spatial_role": ["PROXY_GEOMETRY"],<br>            "geometry_status": ["VALID"],<br>            "name": ["Test post"],<br>            "importance_raw": ["5"],<br>            "asset_status_raw": ["En service"],<br>        },<br>        geometry=[<br>            Polygon(<br>                [<br>                    (200 + distance_m, 100),<br>                    (200 + distance_m, 110),<br>                    (210 + distance_m, 110),<br>                    (210 + distance_m, 100),<br>                    (200 + distance_m, 100),<br>                ]<br>            )<br>        ],<br>        crs="EPSG:2154",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_grid_coverage::_electricity_source` via `_posts`
- value/type reference: `tests.unit.test_assess_grid_coverage::_electricity_source` via `_posts`
- direct call: `tests.unit.test_assess_grid_coverage::_proximity` via `_posts`
- value/type reference: `tests.unit.test_assess_grid_coverage::_proximity` via `_posts`
- direct call: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_posts`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_posts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_electricity_source`

**Purpose:** Implements `electricity source` within the file role: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

**Exact signature**

```python
def _electricity_source(
    extraction: IgnBdTopoExtraction,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `IgnBdTopoExtraction` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoElectricityData(<br>        extraction=extraction,<br>        electric_lines=_lines(),<br>        transformation_posts=_posts(),<br>        electric_lines_summary=cast(Any, None),<br>        transformation_posts_summary=cast(Any, None),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_electricity_source`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_electricity_source`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_proximity_failure_stops_coverage_loading` via `_electricity_source`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_proximity_failure_stops_coverage_loading` via `_electricity_source`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_rejects_generated_parcel_column_before_proximity` via `_electricity_source`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_rejects_generated_parcel_column_before_proximity` via `_electricity_source`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_electricity_source`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_electricity_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoElectricityData` | `landscout.sources.IgnBdTopoElectricityData` |
| `_lines` | `tests.unit.test_assess_grid_coverage._lines` |
| `_posts` | `tests.unit.test_assess_grid_coverage._posts` |
| `cast` | `typing.cast` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_proximity`

**Purpose:** Implements `proximity` within the file role: Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_geometries` | keyword-only | `list[object] \| None` | `None` |
| `parcel_crs` | keyword-only | `str` | `'EPSG:2154'` |
| `line_distances` | keyword-only | `list[float] \| None` | `None` |
| `post_distance_m` | keyword-only | `float` | `50.0` |
| `voltage_statuses` | keyword-only | `list[str] \| None` | `None` |
| `voltages` | keyword-only | `list[float \| None] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `enrich_parcel_grid_proximity(<br>        _parcels(parcel_geometries, crs=parcel_crs),<br>        _lines(<br>            line_distances,<br>            voltage_statuses=voltage_statuses,<br>            voltages=voltages,<br>        ),<br>        _posts(post_distance_m),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_polygonal_coverage_geometry_is_accepted` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_polygonal_coverage_geometry_is_accepted` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_invalid_coverage_geometry_is_rejected` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_invalid_coverage_geometry_is_rejected` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_strict_geometric_boundary_proof` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_strict_geometric_boundary_proof` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_outside_crossing_or_touching_parcel_is_conservative` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_outside_crossing_or_touching_parcel_is_conservative` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_no_exact_match_uses_explicit_no_match_status` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_no_exact_match_uses_explicit_no_match_status` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_proximity_and_coverage_package_lineage_must_match` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_proximity_and_coverage_package_lineage_must_match` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_rejects_arbitrary_source_identity` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_rejects_arbitrary_source_identity` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_count_must_match_frame` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_count_must_match_frame` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_schema_must_match_selected_source_columns` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_schema_must_match_selected_source_columns` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_crs_must_match_frame` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_crs_must_match_frame` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_geometry_facts_are_validated` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_geometry_facts_are_validated` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_department_must_match` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_department_must_match` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_department_field_must_be_exact` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_department_field_must_be_exact` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_public_assessment_loads_coverage_from_the_physical_source` via `_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_assess_grid_coverage._parcels` |
| `_lines` | `tests.unit.test_assess_grid_coverage._lines` |
| `_posts` | `tests.unit.test_assess_grid_coverage._posts` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_clean_coverage_api_is_exported`

**Purpose:** Regression invariant: clean coverage api is exported. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_clean_coverage_api_is_exported() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert stages.assess_grid_coverage is public_assess_grid_coverage`
  - `assert stages.profile_grid_coverage is profile_grid_coverage`
  - `assert "assess_grid_coverage" in stages.__all__`
  - `assert "profile_grid_coverage" in stages.__all__`

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
def test_clean_coverage_api_is_exported() -> None:
    assert stages.assess_grid_coverage is public_assess_grid_coverage
    assert stages.profile_grid_coverage is profile_grid_coverage
    assert "assess_grid_coverage" in stages.__all__
    assert "profile_grid_coverage" in stages.__all__
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_coverage_owns_proximity_and_configured_coverage_once`

**Purpose:** Regression invariant: public coverage owns proximity and configured coverage once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_coverage_owns_proximity_and_configured_coverage_once() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.source_coverage is coverage`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `_electricity_source` | `tests.unit.test_assess_grid_coverage._electricity_source` |
| `_parcels` | `tests.unit.test_assess_grid_coverage._parcels` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `patch` | `unittest.mock.patch` |
| `public_assess_grid_coverage` | `landscout.stages.assess_grid_coverage` |
| `proximity_stage.assert_called_once_with` | `unresolved local/third-party receiver; no ownership inferred` |
| `coverage_loader.assert_called_once_with` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_coverage_owns_proximity_and_configured_coverage_once() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity()

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            return_value=proximity,
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            return_value=coverage,
            create=True,
        ) as coverage_loader,
    ):
        result = public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)

    proximity_stage.assert_called_once_with(parcels, source, SOURCE_CONFIG)
    coverage_loader.assert_called_once_with(source.extraction, SOURCE_CONFIG)
    assert result.source_coverage is coverage
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_coverage_proximity_failure_stops_coverage_loading`

**Purpose:** Regression invariant: public coverage proximity failure stops coverage loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_coverage_proximity_failure_stops_coverage_loading() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `_electricity_source` | `tests.unit.test_assess_grid_coverage._electricity_source` |
| `patch` | `unittest.mock.patch` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `public_assess_grid_coverage` | `landscout.stages.assess_grid_coverage` |
| `_parcels` | `tests.unit.test_assess_grid_coverage._parcels` |
| `proximity_stage.assert_called_once` | `unresolved local/third-party receiver; no ownership inferred` |
| `coverage_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_coverage_proximity_failure_stops_coverage_loading() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            side_effect=ValueError("physical electricity source changed"),
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(GridCoverageAssessmentError),
    ):
        public_assess_grid_coverage(_parcels(), source, SOURCE_CONFIG)

    proximity_stage.assert_called_once()
    coverage_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_coverage_rejects_generated_parcel_column_before_proximity`

**Purpose:** Regression invariant: public coverage rejects generated parcel column before proximity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_coverage_rejects_generated_parcel_column_before_proximity() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="collides.*generated")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_grid_coverage._parcels` |
| `_electricity_source` | `tests.unit.test_assess_grid_coverage._electricity_source` |
| `cast` | `typing.cast` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `public_assess_grid_coverage` | `landscout.stages.assess_grid_coverage` |
| `proximity_stage.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `coverage_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `parcels["grid_source_boundary_distance_m"] = 0.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_public_coverage_rejects_generated_parcel_column_before_proximity() -> None:
    parcels = _parcels()
    parcels["grid_source_boundary_distance_m"] = 0.0
    source = _electricity_source(cast(Any, None))

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(GridCoverageAssessmentError, match="collides.*generated"),
    ):
        public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)

    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_caller_provided_proximity_and_coverage_are_not_public_inputs`

**Purpose:** Regression invariant: caller provided proximity and coverage are not public inputs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_caller_provided_proximity_and_coverage_are_not_public_inputs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>            GridCoverageAssessmentError,<br>            match="parcels\|GeoDataFrame",<br>        )`
- Exact assertions:
  - `assert forged_proximity.parcels["nearest_line_proxy_distance_m"].eq(0.0).all()`
  - `assert (<br>        forged_proximity.parcels["nearest_line_source_archive_sha256"]<br>        .eq(ARCHIVE_SHA256)<br>        .all()<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `forged_proximity.parcels["nearest_line_proxy_distance_m"].eq(0.0).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_proximity.parcels["nearest_line_proxy_distance_m"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_proximity.parcels["nearest_line_source_archive_sha256"]<br>        .eq(ARCHIVE_SHA256)<br>        .all` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_proximity.parcels["nearest_line_source_archive_sha256"]<br>        .eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `public_assess_grid_coverage` | `landscout.stages.assess_grid_coverage` |
| `cast` | `typing.cast` |
| `proximity_stage.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `coverage_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `forged_proximity.parcels["nearest_line_source_archive_sha256"]<br>        .eq(ARCHIVE_SHA256)<br>        .all`<br>`forged_proximity.parcels["nearest_line_source_archive_sha256"]<br>        .eq` |
| CRS/geometry/spatial calculation | `forged_proximity.parcels["nearest_line_proxy_distance_m"].eq(0.0).all`<br>`forged_proximity.parcels["nearest_line_proxy_distance_m"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_caller_provided_proximity_and_coverage_are_not_public_inputs() -> None:
    forged_proximity = _proximity(line_distances=[0.0], post_distance_m=0.0)
    forged_coverage = _coverage()
    assert forged_proximity.parcels["nearest_line_proxy_distance_m"].eq(0.0).all()
    assert (
        forged_proximity.parcels["nearest_line_source_archive_sha256"]
        .eq(ARCHIVE_SHA256)
        .all()
    )

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(
            GridCoverageAssessmentError,
            match="parcels|GeoDataFrame",
        ),
    ):
        public_assess_grid_coverage(
            cast(Any, forged_proximity),
            cast(Any, forged_coverage),
            SOURCE_CONFIG,
        )

    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_polygonal_coverage_geometry_is_accepted`

**Purpose:** Regression invariant: polygonal coverage geometry is accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
        MultiPolygon(
            [
                Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
                Polygon([(2000, 0), (2000, 100), (2100, 100), (2100, 0), (2000, 0)]),
            ]
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(<br>        100.0<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `pytest.approx` | `pytest.approx` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |

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
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    result = assess_grid_coverage(_proximity(), _coverage(geometry), SOURCE_CONFIG)

    assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_coverage_geometry_is_rejected`

**Purpose:** Regression invariant: invalid coverage geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_coverage_geometry_is_rejected(
    geometry: object,
    crs: str | None,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry", "crs", "message"),
    [
        (
            Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
            None,
            "CRS",
        ),
        (
            Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
            "EPSG:4326",
            "2154",
        ),
        (Point(0, 0), "EPSG:2154", "Polygon"),
        (LineString([(0, 0), (10, 10)]), "EPSG:2154", "Polygon"),
        (None, "EPSG:2154", "null"),
        (Polygon(), "EPSG:2154", "empty"),
        (
            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),
            "EPSG:2154",
            "valid",
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |
| `crs` | positional-or-keyword | `str \| None` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `Point` | `shapely.geometry.Point` |
| `LineString` | `shapely.geometry.LineString` |

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
def test_invalid_coverage_geometry_is_rejected(
    geometry: object,
    crs: str | None,
    message: str,
) -> None:
    with pytest.raises(GridCoverageAssessmentError, match=message):
        assess_grid_coverage(_proximity(), _coverage(geometry, crs=crs), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_geometric_boundary_proof`

**Purpose:** Regression invariant: strict geometric boundary proof. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_strict_geometric_boundary_proof(
    asset_distance: float,
    expected_status: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("asset_distance", "expected_status"),
    [
        (50.0, "NOT_BOUNDARY_LIMITED"),
        (100.0, "BOUNDARY_LIMITED"),
        (150.0, "BOUNDARY_LIMITED"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `asset_distance` | positional-or-keyword | `float` | `required` |
| `expected_status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel["grid_source_boundary_distance_m"] == pytest.approx(100.0)`
  - `assert parcel["nearest_line_proxy_distance_m"] == pytest.approx(asset_distance)`
  - `assert parcel["nearest_line_coverage_status"] == expected_status`
  - `assert parcel["nearest_exact_line_coverage_status"] == expected_status`
  - `assert parcel["nearest_post_coverage_status"] == expected_status`
  - `assert result.voltage_level_proximity.loc[0, "coverage_status"] == expected_status`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `pytest.approx` | `pytest.approx` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_outside_crossing_or_touching_parcel_is_conservative`

**Purpose:** Regression invariant: outside crossing or touching parcel is conservative. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_outside_crossing_or_touching_parcel_is_conservative(
    parcel_geometry: Polygon,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "parcel_geometry",
    [
        Polygon([(950, 100), (950, 200), (1050, 200), (1050, 100), (950, 100)]),
        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
        Polygon([(1100, 100), (1100, 200), (1200, 200), (1200, 100), (1100, 100)]),
    ],
    ids=["crossing", "touching", "outside"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_geometry` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel["grid_source_boundary_distance_m"] == 0.0`
  - `assert parcel["grid_source_coverage_position"] == "OUTSIDE_OR_CROSSING_COVERAGE"`
  - `assert parcel["nearest_line_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"`
  - `assert parcel["nearest_exact_line_coverage_status"] == (<br>        "OUTSIDE_OR_CROSSING_COVERAGE"<br>    )`
  - `assert parcel["nearest_post_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"`
  - `assert result.voltage_level_proximity.loc[0, "coverage_status"] == (<br>        "OUTSIDE_OR_CROSSING_COVERAGE"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_exact_match_uses_explicit_no_match_status`

**Purpose:** Regression invariant: no exact match uses explicit no match status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_exact_match_uses_explicit_no_match_status() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()`
  - `assert result.parcels["nearest_exact_line_coverage_status"].eq("NO_MATCH").all()`
  - `assert result.voltage_level_proximity.empty`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `result.parcels["nearest_exact_line_proxy_distance_m"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_proxy_distance_m"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_coverage_status"].eq("NO_MATCH").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_coverage_status"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels["nearest_exact_line_proxy_distance_m"].isna().all`<br>`result.parcels["nearest_exact_line_proxy_distance_m"].isna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_assessment_preserves_proximity_values_and_does_not_mutate_input`

**Purpose:** Regression invariant: assessment preserves proximity values and does not mutate input. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_assessment_preserves_proximity_values_and_does_not_mutate_input() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels["parcel_id"].tolist() == parcels_before["parcel_id"].tolist()`
  - `assert result.voltage_level_proximity[["parcel_id", "voltage_kv"]].equals(<br>        table_before[["parcel_id", "voltage_kv"]]<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `deepcopy` | `copy.deepcopy` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `result.parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels_before["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity[["parcel_id", "voltage_kv"]].equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
    assert result.voltage_level_proximity[["parcel_id", "voltage_kv"]].equals(
        table_before[["parcel_id", "voltage_kv"]]
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_geographic_parcel_storage_crs_and_geometry_are_preserved`

**Purpose:** Regression invariant: geographic parcel storage crs and geometry are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_geographic_parcel_storage_crs_and_geometry_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.crs.to_epsg() == 4326`
  - `assert result.parcels.geometry.geom_equals_exact(<br>        proximity.parcels.geometry, tolerance=0, align=False<br>    ).all()`
  - `assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(<br>        100.0, abs=1e-6<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_grid_coverage._parcels` |
| `projected.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_lines` | `tests.unit.test_assess_grid_coverage._lines` |
| `_posts` | `tests.unit.test_assess_grid_coverage._posts` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `result.parcels.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.geometry.geom_equals_exact(<br>        proximity.parcels.geometry, tolerance=0, align=False<br>    ).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.geometry.geom_equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.approx` | `pytest.approx` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `projected.to_crs`<br>`result.parcels.geometry.geom_equals_exact(<br>        proximity.parcels.geometry, tolerance=0, align=False<br>    ).all`<br>`result.parcels.geometry.geom_equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_reports_dynamic_voltage_and_boundary_distributions`

**Purpose:** Regression invariant: profile reports dynamic voltage and boundary distributions. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_reports_dynamic_voltage_and_boundary_distributions() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.parcel_count == 1`
  - `assert profile.fully_covered_count == 1`
  - `assert profile.outside_or_crossing_count == 0`
  - `assert profile.boundary_distance.minimum == pytest.approx(100.0)`
  - `assert profile.boundary_distance.p50 == pytest.approx(100.0)`
  - `assert profile.boundary_distance.maximum == pytest.approx(100.0)`
  - `assert profile.nearest_line.not_boundary_limited == 1`
  - `assert profile.nearest_post.boundary_limited == 1`
  - `assert [item.voltage_kv for item in profile.voltage_levels] == [110.0, 275.0]`
  - `assert profile.voltage_levels[0].statuses.not_boundary_limited == 1`
  - `assert profile.voltage_levels[1].statuses.boundary_limited == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `profile_grid_coverage` | `landscout.stages.profile_grid_coverage` |
| `pytest.approx` | `pytest.approx` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_proximity_and_coverage_package_lineage_must_match`

**Purpose:** Regression invariant: proximity and coverage package lineage must match. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_proximity_and_coverage_package_lineage_must_match() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |

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
| In-memory mutation | `coverage.coverage.loc[0, "source_archive_sha256"] = "b" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_proximity_and_coverage_package_lineage_must_match() -> None:
    proximity = _proximity()
    coverage = _coverage()
    coverage.coverage.loc[0, "source_archive_sha256"] = "b" * 64

    with pytest.raises(GridCoverageAssessmentError, match="lineage"):
        assess_grid_coverage(proximity, coverage, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_rejects_arbitrary_source_identity`

**Purpose:** Regression invariant: coverage rejects arbitrary source identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_rejects_arbitrary_source_identity(field: str, value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [("source_provider", "arbitrary"), ("source_product", "roads")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="provider\|product\|identity")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
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
| In-memory mutation | `coverage.coverage.loc[0, field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coverage_rejects_arbitrary_source_identity(field: str, value: str) -> None:
    coverage = replace(_coverage(), **{field: value})
    coverage.coverage.loc[0, field] = value

    with pytest.raises(GridCoverageAssessmentError, match="provider|product|identity"):
        assess_grid_coverage(_proximity(), coverage, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_summary_selected_count_must_match_frame`

**Purpose:** Regression invariant: coverage summary selected count must match frame. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_summary_selected_count_must_match_frame(
    selected_count: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("selected_count", [0, 2])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `selected_count` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="selected\|count")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_summary_schema_must_match_selected_source_columns`

**Purpose:** Regression invariant: coverage summary schema must match selected source columns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_summary_schema_must_match_selected_source_columns(
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        GridCoverageAssessmentError, match="summary\|column\|dtype\|schema"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
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
| In-memory mutation | `dtypes[0] = (dtypes[0][0], "float64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

    with pytest.raises(
        GridCoverageAssessmentError, match="summary|column|dtype|schema"
    ):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=changed), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_summary_crs_must_match_frame`

**Purpose:** Regression invariant: coverage summary crs must match frame. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_summary_crs_must_match_frame() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="CRS\|2154")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |

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
def test_coverage_summary_crs_must_match_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, crs="EPSG:4326")

    with pytest.raises(GridCoverageAssessmentError, match="CRS|2154"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_summary_geometry_facts_are_validated`

**Purpose:** Regression invariant: coverage summary geometry facts are validated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_summary_geometry_facts_are_validated(
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("null_geometry_count", 1),
        ("empty_geometry_count", 1),
        ("invalid_geometry_count", 1),
        ("geometry_types", ("Point",)),
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
  - `pytest.raises(GridCoverageAssessmentError, match="geometry\|summary")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_summary_selected_department_must_match`

**Purpose:** Regression invariant: coverage summary selected department must match. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_summary_selected_department_must_match() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="department")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |

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
def test_coverage_summary_selected_department_must_match() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, selected_department_code="32")

    with pytest.raises(GridCoverageAssessmentError, match="department"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_summary_department_field_must_be_exact`

**Purpose:** Regression invariant: coverage summary department field must be exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_summary_department_field_must_be_exact(field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["", " ", "missing"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="department\|field")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
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
def test_coverage_summary_department_field_must_be_exact(field: str) -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, department_code_field=field)

    with pytest.raises(GridCoverageAssessmentError, match="department|field"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_summary_source_count_cannot_be_smaller_than_selection`

**Purpose:** Regression invariant: coverage summary source count cannot be smaller than selection. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_summary_source_count_cannot_be_smaller_than_selection() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="source\|count")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |

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
def test_coverage_summary_source_count_cannot_be_smaller_than_selection() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_feature_count=0)

    with pytest.raises(GridCoverageAssessmentError, match="source|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_source_layer_lineage_must_match_summary_and_frame`

**Purpose:** Regression invariant: coverage source layer lineage must match summary and frame. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_source_layer_lineage_must_match_summary_and_frame() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridCoverageAssessmentError, match="layer\|lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |

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
def test_coverage_source_layer_lineage_must_match_summary_and_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_layer_name="unknown_layer")

    with pytest.raises(GridCoverageAssessmentError, match="layer|lineage"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_assessment_loads_coverage_from_the_physical_source`

**Purpose:** Regression invariant: public assessment loads coverage from the physical source. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_assessment_loads_coverage_from_the_physical_source() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.source_coverage.coverage.loc[0, "nom_officiel"] == "Haute-Garonne"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_grid_coverage._coverage` |
| `_electricity_source` | `tests.unit.test_assess_grid_coverage._electricity_source` |
| `_parcels` | `tests.unit.test_assess_grid_coverage._parcels` |
| `_proximity` | `tests.unit.test_assess_grid_coverage._proximity` |
| `patch` | `unittest.mock.patch` |
| `public_assess_grid_coverage` | `landscout.stages.assess_grid_coverage` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **25**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_coverage_assessment_reproduces_configured_logical_layer` | none | pytest.raises(GridCoverageAssessmentError, match="physical\|configured") | 1 | Proves coverage assessment reproduces configured logical layer using the exact source reproduced in section 7. |
| `test_clean_coverage_api_is_exported` | none | none | 4 | Proves clean coverage api is exported using the exact source reproduced in section 7. |
| `test_public_coverage_owns_proximity_and_configured_coverage_once` | none | none | 1 | Proves public coverage owns proximity and configured coverage once using the exact source reproduced in section 7. |
| `test_public_coverage_proximity_failure_stops_coverage_loading` | none | pytest.raises(GridCoverageAssessmentError) | 0 | Proves public coverage proximity failure stops coverage loading using the exact source reproduced in section 7. |
| `test_public_coverage_rejects_generated_parcel_column_before_proximity` | none | pytest.raises(GridCoverageAssessmentError, match="collides.*generated") | 0 | Proves public coverage rejects generated parcel column before proximity using the exact source reproduced in section 7. |
| `test_caller_provided_proximity_and_coverage_are_not_public_inputs` | none | pytest.raises(<br>            GridCoverageAssessmentError,<br>            match="parcels\|GeoDataFrame",<br>        ) | 2 | Proves caller provided proximity and coverage are not public inputs using the exact source reproduced in section 7. |
| `test_polygonal_coverage_geometry_is_accepted` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),<br>        MultiPolygon(<br>            [<br>                Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),<br>                Polygon([(2000, 0), (2000, 100), (2100, 100), (2100, 0), (2000, 0)]),<br>            ]<br>        ),<br>    ],<br>) | none | 1 | Proves polygonal coverage geometry is accepted using the exact source reproduced in section 7. |
| `test_invalid_coverage_geometry_is_rejected` | pytest.mark.parametrize(<br>    ("geometry", "crs", "message"),<br>    [<br>        (<br>            Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),<br>            None,<br>            "CRS",<br>        ),<br>        (<br>            Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),<br>            "EPSG:4326",<br>            "2154",<br>        ),<br>        (Point(0, 0), "EPSG:2154", "Polygon"),<br>        (LineString([(0, 0), (10, 10)]), "EPSG:2154", "Polygon"),<br>        (None, "EPSG:2154", "null"),<br>        (Polygon(), "EPSG:2154", "empty"),<br>        (<br>            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),<br>            "EPSG:2154",<br>            "valid",<br>        ),<br>    ],<br>) | pytest.raises(GridCoverageAssessmentError, match=message) | 0 | Proves invalid coverage geometry is rejected using the exact source reproduced in section 7. |
| `test_strict_geometric_boundary_proof` | pytest.mark.parametrize(<br>    ("asset_distance", "expected_status"),<br>    [<br>        (50.0, "NOT_BOUNDARY_LIMITED"),<br>        (100.0, "BOUNDARY_LIMITED"),<br>        (150.0, "BOUNDARY_LIMITED"),<br>    ],<br>) | none | 6 | Proves strict geometric boundary proof using the exact source reproduced in section 7. |
| `test_outside_crossing_or_touching_parcel_is_conservative` | pytest.mark.parametrize(<br>    "parcel_geometry",<br>    [<br>        Polygon([(950, 100), (950, 200), (1050, 200), (1050, 100), (950, 100)]),<br>        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),<br>        Polygon([(1100, 100), (1100, 200), (1200, 200), (1200, 100), (1100, 100)]),<br>    ],<br>    ids=["crossing", "touching", "outside"],<br>) | none | 6 | Proves outside crossing or touching parcel is conservative using the exact source reproduced in section 7. |
| `test_no_exact_match_uses_explicit_no_match_status` | none | none | 3 | Proves no exact match uses explicit no match status using the exact source reproduced in section 7. |
| `test_assessment_preserves_proximity_values_and_does_not_mutate_input` | none | none | 2 | Proves assessment preserves proximity values and does not mutate input using the exact source reproduced in section 7. |
| `test_geographic_parcel_storage_crs_and_geometry_are_preserved` | none | none | 3 | Proves geographic parcel storage crs and geometry are preserved using the exact source reproduced in section 7. |
| `test_profile_reports_dynamic_voltage_and_boundary_distributions` | none | none | 11 | Proves profile reports dynamic voltage and boundary distributions using the exact source reproduced in section 7. |
| `test_proximity_and_coverage_package_lineage_must_match` | none | pytest.raises(GridCoverageAssessmentError, match="lineage") | 0 | Proves proximity and coverage package lineage must match using the exact source reproduced in section 7. |
| `test_coverage_rejects_arbitrary_source_identity` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [("source_provider", "arbitrary"), ("source_product", "roads")],<br>) | pytest.raises(GridCoverageAssessmentError, match="provider\|product\|identity") | 0 | Proves coverage rejects arbitrary source identity using the exact source reproduced in section 7. |
| `test_coverage_summary_selected_count_must_match_frame` | pytest.mark.parametrize("selected_count", [0, 2]) | pytest.raises(GridCoverageAssessmentError, match="selected\|count") | 0 | Proves coverage summary selected count must match frame using the exact source reproduced in section 7. |
| `test_coverage_summary_schema_must_match_selected_source_columns` | pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"]) | pytest.raises(<br>        GridCoverageAssessmentError, match="summary\|column\|dtype\|schema"<br>    ) | 0 | Proves coverage summary schema must match selected source columns using the exact source reproduced in section 7. |
| `test_coverage_summary_crs_must_match_frame` | none | pytest.raises(GridCoverageAssessmentError, match="CRS\|2154") | 0 | Proves coverage summary crs must match frame using the exact source reproduced in section 7. |
| `test_coverage_summary_geometry_facts_are_validated` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("null_geometry_count", 1),<br>        ("empty_geometry_count", 1),<br>        ("invalid_geometry_count", 1),<br>        ("geometry_types", ("Point",)),<br>    ],<br>) | pytest.raises(GridCoverageAssessmentError, match="geometry\|summary") | 0 | Proves coverage summary geometry facts are validated using the exact source reproduced in section 7. |
| `test_coverage_summary_selected_department_must_match` | none | pytest.raises(GridCoverageAssessmentError, match="department") | 0 | Proves coverage summary selected department must match using the exact source reproduced in section 7. |
| `test_coverage_summary_department_field_must_be_exact` | pytest.mark.parametrize("field", ["", " ", "missing"]) | pytest.raises(GridCoverageAssessmentError, match="department\|field") | 0 | Proves coverage summary department field must be exact using the exact source reproduced in section 7. |
| `test_coverage_summary_source_count_cannot_be_smaller_than_selection` | none | pytest.raises(GridCoverageAssessmentError, match="source\|count") | 0 | Proves coverage summary source count cannot be smaller than selection using the exact source reproduced in section 7. |
| `test_coverage_source_layer_lineage_must_match_summary_and_frame` | none | pytest.raises(GridCoverageAssessmentError, match="layer\|lineage") | 0 | Proves coverage source layer lineage must match summary and frame using the exact source reproduced in section 7. |
| `test_public_assessment_loads_coverage_from_the_physical_source` | none | none | 1 | Proves public assessment loads coverage from the physical source using the exact source reproduced in section 7. |

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
import json
import tempfile
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch
from uuid import uuid4

import geopandas as gpd
import pyogrio
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
    MultiPolygon,
    Point,
    Polygon,
)

import landscout.sources.ign_bdtopo_fr as ign_source
from landscout import stages
from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)
from landscout.stages import (
    GridCoverageAssessmentError,
    profile_grid_coverage,
)
from landscout.stages import (
    assess_grid_coverage as public_assess_grid_coverage,
)
from landscout.stages.assess_grid_coverage import (
    _assess_grid_coverage_from_proximity as assess_grid_coverage,
)
from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)

ARCHIVE_SHA256 = "a" * 64
EDITION = "2026-06-15"
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-coverage-ign-"))
_SOURCE_CONFIG_PAYLOAD = load_ign_bdtopo_source_config().model_dump(mode="json")
_SOURCE_CONFIG_PAYLOAD.update(
    {
        "source_url": "https://example.test/BDTOPO.7z",
        "checksum_url": None,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "expected_archive_size_bytes": 1,
    }
)
SOURCE_CONFIG = IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)
ALTERNATE_COVERAGE_LAYER = "zone_administrative"


def _coverage(
    geometry: object = Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
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
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="troncon_de_route",
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
                "schema_version": 3,
                "archive_sha256": ARCHIVE_SHA256,
                "geopackage_relative_path": "data.gpkg",
                "geopackage_size_bytes": len(payload),
                "geopackage_sha256": digest,
                "all_layer_names": list(layer_names),
                "electric_lines_layer": "ligne_electrique",
                "transformation_posts_layer": "poste_de_transformation",
                "road_segments_layer": "troncon_de_route",
                "department_layer": "departement",
                "extracted_entries": [
                    {
                        "relative_path": "data.gpkg",
                        "kind": "file",
                        "size_bytes": len(payload),
                        "sha256": digest,
                    }
                ],
                "spatial_role": "PROXY_GEOMETRY",
            }
        ),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
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
        road_segments_layer="troncon_de_route",
        department_layer="departement",
        cache_hit=True,
    )
    frame = raw_frame.copy()
    for column, value in {
        "source_provider": SOURCE_CONFIG.provider,
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
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in raw_frame.dtypes.items()
        ),
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
        source_provider=SOURCE_CONFIG.provider,
        source_product="BD TOPO",
        source_department_code="31",
        source_edition=EDITION,
        source_product_version="3.5",
        source_archive_sha256=ARCHIVE_SHA256,
        source_layer="departement",
        spatial_role=spatial_role,
    )


def _with_alternate_coverage_layer(
    source: IgnBdTopoDepartmentCoverage,
) -> tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]:
    alternate = gpd.GeoDataFrame(
        {"code_insee": ["31"], "nom_officiel": ["Alternate coverage"]},
        geometry=[Polygon([(0, 0), (0, 900), (900, 900), (900, 0), (0, 0)])],
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
        extracted_entries=[
            {
                "relative_path": "data.gpkg",
                "kind": "file",
                "size_bytes": len(payload),
                "sha256": digest,
            }
        ],
    )
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    extraction = replace(
        source.extraction,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
    )
    configured = load_ign_bdtopo_department_coverage(
        extraction,
        SOURCE_CONFIG,
    )
    alternate_loaded = gpd.read_file(
        geopackage_path,
        layer=ALTERNATE_COVERAGE_LAYER,
        engine="pyogrio",
    )
    forged = ign_source._department_coverage_from_frame(
        extraction,
        alternate_loaded,
        ALTERNATE_COVERAGE_LAYER,
        "code_insee",
    )
    return configured, forged


def test_coverage_assessment_reproduces_configured_logical_layer() -> None:
    configured, forged = _with_alternate_coverage_layer(_coverage())

    loaded = load_ign_bdtopo_department_coverage(configured.extraction, SOURCE_CONFIG)
    result = assess_grid_coverage(_proximity(), loaded, SOURCE_CONFIG)
    assert result.source_coverage.source_layer == "departement"

    with pytest.raises(GridCoverageAssessmentError, match="physical|configured"):
        assess_grid_coverage(_proximity(), forged, SOURCE_CONFIG)


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
            "voltage_raw": [
                None if value is None else str(value) for value in voltage_values
            ],
            "voltage_status": statuses,
            "voltage_kv": voltage_values,
            "voltage_upper_bound_kv": [None] * len(values),
            "manager_name": ["RTE"] * len(values),
            "asset_status_raw": ["En service"] * len(values),
        },
        geometry=[
            LineString([(200 + value, 50), (200 + value, 250)]) for value in values
        ],
        crs="EPSG:2154",
    )


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


def test_clean_coverage_api_is_exported() -> None:
    assert stages.assess_grid_coverage is public_assess_grid_coverage
    assert stages.profile_grid_coverage is profile_grid_coverage
    assert "assess_grid_coverage" in stages.__all__
    assert "profile_grid_coverage" in stages.__all__


def test_public_coverage_owns_proximity_and_configured_coverage_once() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity()

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            return_value=proximity,
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            return_value=coverage,
            create=True,
        ) as coverage_loader,
    ):
        result = public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)

    proximity_stage.assert_called_once_with(parcels, source, SOURCE_CONFIG)
    coverage_loader.assert_called_once_with(source.extraction, SOURCE_CONFIG)
    assert result.source_coverage is coverage


def test_public_coverage_proximity_failure_stops_coverage_loading() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            side_effect=ValueError("physical electricity source changed"),
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(GridCoverageAssessmentError),
    ):
        public_assess_grid_coverage(_parcels(), source, SOURCE_CONFIG)

    proximity_stage.assert_called_once()
    coverage_loader.assert_not_called()


def test_public_coverage_rejects_generated_parcel_column_before_proximity() -> None:
    parcels = _parcels()
    parcels["grid_source_boundary_distance_m"] = 0.0
    source = _electricity_source(cast(Any, None))

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(GridCoverageAssessmentError, match="collides.*generated"),
    ):
        public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)

    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()


def test_caller_provided_proximity_and_coverage_are_not_public_inputs() -> None:
    forged_proximity = _proximity(line_distances=[0.0], post_distance_m=0.0)
    forged_coverage = _coverage()
    assert forged_proximity.parcels["nearest_line_proxy_distance_m"].eq(0.0).all()
    assert (
        forged_proximity.parcels["nearest_line_source_archive_sha256"]
        .eq(ARCHIVE_SHA256)
        .all()
    )

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(
            GridCoverageAssessmentError,
            match="parcels|GeoDataFrame",
        ),
    ):
        public_assess_grid_coverage(
            cast(Any, forged_proximity),
            cast(Any, forged_coverage),
            SOURCE_CONFIG,
        )

    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
        MultiPolygon(
            [
                Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
                Polygon([(2000, 0), (2000, 100), (2100, 100), (2100, 0), (2000, 0)]),
            ]
        ),
    ],
)
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    result = assess_grid_coverage(_proximity(), _coverage(geometry), SOURCE_CONFIG)

    assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0
    )


@pytest.mark.parametrize(
    ("geometry", "crs", "message"),
    [
        (
            Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
            None,
            "CRS",
        ),
        (
            Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
            "EPSG:4326",
            "2154",
        ),
        (Point(0, 0), "EPSG:2154", "Polygon"),
        (LineString([(0, 0), (10, 10)]), "EPSG:2154", "Polygon"),
        (None, "EPSG:2154", "null"),
        (Polygon(), "EPSG:2154", "empty"),
        (
            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),
            "EPSG:2154",
            "valid",
        ),
    ],
)
def test_invalid_coverage_geometry_is_rejected(
    geometry: object,
    crs: str | None,
    message: str,
) -> None:
    with pytest.raises(GridCoverageAssessmentError, match=message):
        assess_grid_coverage(_proximity(), _coverage(geometry, crs=crs), SOURCE_CONFIG)


@pytest.mark.parametrize(
    ("asset_distance", "expected_status"),
    [
        (50.0, "NOT_BOUNDARY_LIMITED"),
        (100.0, "BOUNDARY_LIMITED"),
        (150.0, "BOUNDARY_LIMITED"),
    ],
)
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


@pytest.mark.parametrize(
    "parcel_geometry",
    [
        Polygon([(950, 100), (950, 200), (1050, 200), (1050, 100), (950, 100)]),
        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
        Polygon([(1100, 100), (1100, 200), (1200, 200), (1200, 100), (1100, 100)]),
    ],
    ids=["crossing", "touching", "outside"],
)
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


def test_no_exact_match_uses_explicit_no_match_status() -> None:
    proximity = _proximity(
        voltage_statuses=["UNKNOWN"],
        voltages=[None],
    )
    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_coverage_status"].eq("NO_MATCH").all()
    assert result.voltage_level_proximity.empty


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
    assert result.voltage_level_proximity[["parcel_id", "voltage_kv"]].equals(
        table_before[["parcel_id", "voltage_kv"]]
    )


def test_geographic_parcel_storage_crs_and_geometry_are_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    proximity = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert result.parcels.crs.to_epsg() == 4326
    assert result.parcels.geometry.geom_equals_exact(
        proximity.parcels.geometry, tolerance=0, align=False
    ).all()
    assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )


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


def test_proximity_and_coverage_package_lineage_must_match() -> None:
    proximity = _proximity()
    coverage = _coverage()
    coverage.coverage.loc[0, "source_archive_sha256"] = "b" * 64

    with pytest.raises(GridCoverageAssessmentError, match="lineage"):
        assess_grid_coverage(proximity, coverage, SOURCE_CONFIG)


@pytest.mark.parametrize(
    ("field", "value"),
    [("source_provider", "arbitrary"), ("source_product", "roads")],
)
def test_coverage_rejects_arbitrary_source_identity(field: str, value: str) -> None:
    coverage = replace(_coverage(), **{field: value})
    coverage.coverage.loc[0, field] = value

    with pytest.raises(GridCoverageAssessmentError, match="provider|product|identity"):
        assess_grid_coverage(_proximity(), coverage, SOURCE_CONFIG)


@pytest.mark.parametrize("selected_count", [0, 2])
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


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"])
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

    with pytest.raises(
        GridCoverageAssessmentError, match="summary|column|dtype|schema"
    ):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=changed), SOURCE_CONFIG
        )


def test_coverage_summary_crs_must_match_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, crs="EPSG:4326")

    with pytest.raises(GridCoverageAssessmentError, match="CRS|2154"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("null_geometry_count", 1),
        ("empty_geometry_count", 1),
        ("invalid_geometry_count", 1),
        ("geometry_types", ("Point",)),
    ],
)
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


def test_coverage_summary_selected_department_must_match() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, selected_department_code="32")

    with pytest.raises(GridCoverageAssessmentError, match="department"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


@pytest.mark.parametrize("field", ["", " ", "missing"])
def test_coverage_summary_department_field_must_be_exact(field: str) -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, department_code_field=field)

    with pytest.raises(GridCoverageAssessmentError, match="department|field"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


def test_coverage_summary_source_count_cannot_be_smaller_than_selection() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_feature_count=0)

    with pytest.raises(GridCoverageAssessmentError, match="source|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


def test_coverage_source_layer_lineage_must_match_summary_and_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_layer_name="unknown_layer")

    with pytest.raises(GridCoverageAssessmentError, match="layer|lineage"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


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
