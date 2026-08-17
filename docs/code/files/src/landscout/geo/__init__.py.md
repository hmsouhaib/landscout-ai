# `src/landscout/geo/__init__.py`

## File identity

- Repository path: `src/landscout/geo/__init__.py`
- File type: Python source
- Layer: Geo/GIS utility
- Domain: geo/GIS
- Responsibility: Re-exports the supported CRS and geometry API from landscout.geo.
- Source SHA256: `1855749b207417104b804e83399266787cf5d0f5cdefd2913fec0b70ad6571c4`

## 1. Purpose

Re-exports the supported CRS and geometry API from landscout.geo.

## 2. Position in LandScout architecture

This file belongs to the **Geo/GIS utility** layer and the **geo/GIS** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `None.`

### Internal LandScout imports

- `from landscout.geo.crs import LAMBERT93, WGS84`
- `from landscout.geo.geometry import (
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    ParcelShapeMetrics,
    UnsupportedGeometryError,
    ZeroAreaGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    centroid_to_latlon,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
    reproject_to_lambert93,
)`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "LAMBERT93",
    "WGS84",
    "EmptyGeometryError",
    "GeometryError",
    "InvalidGeometryError",
    "MetricCrsError",
    "ParcelShapeMetrics",
    "UnsupportedGeometryError",
    "ZeroAreaGeometryError",
    "approximate_length_m",
    "approximate_width_m",
    "area_m2",
    "centroid",
    "centroid_to_latlon",
    "compactness_score",
    "length_width_ratio",
    "parcel_shape_metrics_m",
    "perimeter_m",
    "reproject_to_lambert93",
]
```


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

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `LAMBERT93` | public re-export imported from its declaring module | `landscout.geo.crs.LAMBERT93` | yes |
| `WGS84` | public re-export imported from its declaring module | `landscout.geo.crs.WGS84` | yes |
| `EmptyGeometryError` | public re-export imported from its declaring module | `landscout.geo.geometry.EmptyGeometryError` | yes |
| `GeometryError` | public re-export imported from its declaring module | `landscout.geo.geometry.GeometryError` | yes |
| `InvalidGeometryError` | public re-export imported from its declaring module | `landscout.geo.geometry.InvalidGeometryError` | yes |
| `MetricCrsError` | public re-export imported from its declaring module | `landscout.geo.geometry.MetricCrsError` | yes |
| `ParcelShapeMetrics` | public re-export imported from its declaring module | `landscout.geo.geometry.ParcelShapeMetrics` | yes |
| `UnsupportedGeometryError` | public re-export imported from its declaring module | `landscout.geo.geometry.UnsupportedGeometryError` | yes |
| `ZeroAreaGeometryError` | public re-export imported from its declaring module | `landscout.geo.geometry.ZeroAreaGeometryError` | yes |
| `approximate_length_m` | public re-export imported from its declaring module | `landscout.geo.geometry.approximate_length_m` | yes |
| `approximate_width_m` | public re-export imported from its declaring module | `landscout.geo.geometry.approximate_width_m` | yes |
| `area_m2` | public re-export imported from its declaring module | `landscout.geo.geometry.area_m2` | yes |
| `centroid` | public re-export imported from its declaring module | `landscout.geo.geometry.centroid` | yes |
| `centroid_to_latlon` | public re-export imported from its declaring module | `landscout.geo.geometry.centroid_to_latlon` | yes |
| `compactness_score` | public re-export imported from its declaring module | `landscout.geo.geometry.compactness_score` | yes |
| `length_width_ratio` | public re-export imported from its declaring module | `landscout.geo.geometry.length_width_ratio` | yes |
| `parcel_shape_metrics_m` | public re-export imported from its declaring module | `landscout.geo.geometry.parcel_shape_metrics_m` | yes |
| `perimeter_m` | public re-export imported from its declaring module | `landscout.geo.geometry.perimeter_m` | yes |
| `reproject_to_lambert93` | public re-export imported from its declaring module | `landscout.geo.geometry.reproject_to_lambert93` | yes |

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
