# `src/landscout/geo/crs.py`

## File identity

- Repository path: `src/landscout/geo/crs.py`
- File type: Python source
- Layer: Geo/GIS utility
- Domain: geo/GIS
- Responsibility: Exposes canonical storage and metric CRS constants.
- Source SHA256: `22f5eff7b49ed92b2e4fffed3bc02ab2e0f159f809a16bf49d05d6ef177f2de5`

## 1. Purpose

Exposes canonical storage and metric CRS constants.

## 2. Position in LandScout architecture

This file belongs to the **Geo/GIS utility** layer and the **geo/GIS** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `from pyproj import CRS`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `WGS84`

```python
WGS84 = CRS.from_epsg(4326)
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/geo/__init__.py::<module>` (import/re-export), `src/landscout/geo/geometry.py::centroid_to_latlon` (value argument/reference), `src/landscout/geo/geometry.py::<module>` (import/re-export), `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value argument/reference), `src/landscout/stages/enrich_shape.py::<module>` (import/re-export), `src/landscout/stages/normalize_cadastre.py::normalize_cadastre_parcels` (value argument/reference), `src/landscout/stages/normalize_cadastre.py::<module>` (import/re-export), `tests/unit/test_crs.py::test_reproject_to_lambert93_and_back_to_latlon` (value argument/reference), `tests/unit/test_crs.py::<module>` (import/re-export), `tests/unit/test_geometry.py::test_metric_calculation_in_wgs84_fails` (value argument/reference), `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` (value argument/reference), `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` (value argument/reference), `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` (value argument/reference), `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` (value argument/reference), `tests/unit/test_geometry.py::test_centralized_shape_metrics_reject_geographic_crs` (value argument/reference), `tests/unit/test_geometry.py::<module>` (import/re-export).

#### `LAMBERT93`

```python
LAMBERT93 = CRS.from_epsg(2154)
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/geo/__init__.py::<module>` (import/re-export), `src/landscout/geo/geometry.py::reproject_to_lambert93` (value argument/reference), `src/landscout/geo/geometry.py::<module>` (import/re-export), `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value argument/reference), `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value argument/reference), `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value argument/reference), `src/landscout/stages/enrich_shape.py::<module>` (import/re-export), `src/landscout/stages/normalize_cadastre.py::normalize_cadastre_parcels` (value argument/reference), `src/landscout/stages/normalize_cadastre.py::<module>` (import/re-export), `tests/unit/test_crs.py::test_reproject_to_lambert93_and_back_to_latlon` (value argument/reference), `tests/unit/test_crs.py::<module>` (import/re-export), `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics` (value argument/reference), `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics` (value argument/reference), `tests/unit/test_enrich_shape.py::<module>` (import/re-export), `tests/unit/test_geometry.py::test_valid_polygon_in_lambert93` (value argument/reference), `tests/unit/test_geometry.py::test_area_in_square_metres` (value argument/reference), `tests/unit/test_geometry.py::test_perimeter_in_metres` (value argument/reference), `tests/unit/test_geometry.py::test_empty_geometry_fails` (value argument/reference), `tests/unit/test_geometry.py::test_invalid_geometry_fails` (value argument/reference), `tests/unit/test_geometry.py::test_multipolygon` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

No function or method is declared.

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

The module contributes to the geo/GIS flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
