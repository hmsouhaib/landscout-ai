# `src/landscout/geo/geometry.py`

## File identity

- Repository path: `src/landscout/geo/geometry.py`
- File type: Python source
- Layer: Geo/GIS utility
- Domain: geo/GIS
- Responsibility: Validates parcel geometry and computes metric shape measurements on calculation-only Lambert-93 copies.
- Source SHA256: `465e20701bcf325f0191548e4ed7c7c471d7764e595ada632efabcd1404fced6`

## 1. Purpose

Validates parcel geometry and computes metric shape measurements on calculation-only Lambert-93 copies.

## 2. Position in LandScout architecture

This file belongs to the **Geo/GIS utility** layer and the **geo/GIS** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from dataclasses import dataclass`
- `from itertools import pairwise`
- `from math import hypot, isfinite, pi`

### Third-party packages

- `from pyproj import CRS, Transformer`
- `from shapely import get_coordinate_dimension`
- `from shapely.geometry import (  # type: ignore[import-untyped]
    MultiPolygon,
    Point,
    Polygon,
)`
- `from shapely.geometry.base import BaseGeometry`
- `from shapely.ops import transform`

### Internal LandScout imports

- `from landscout.geo.crs import LAMBERT93, WGS84`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

#### `Geometry`

```python
type Geometry = Polygon | MultiPolygon
```

Semantic type alias shown exactly above. It is consumed by annotations or Pydantic validation in this module.


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `ParcelShapeMetrics`

**Purpose:** Immutable metric-geometry measurements calculated for one valid parcel geometry.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `length_m` | `length_m: float` | Metre value; whether measured geometry or configured policy is determined by the owning model/function, not the suffix alone. |
| `width_m` | `width_m: float` | Metre value; whether measured geometry or configured policy is determined by the owning model/function, not the suffix alone. |
| `length_width_ratio` | `length_width_ratio: float` | Stores `ParcelShapeMetrics`'s `length width ratio` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `compactness` | `compactness: float` | Stores `ParcelShapeMetrics`'s `compactness` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::parcel_shape_metrics_m` via `ParcelShapeMetrics`.

**Exact class source**

```python
class ParcelShapeMetrics:
    length_m: float
    width_m: float
    length_width_ratio: float
    compactness: float
```

### `GeometryError`

**Purpose:** Base error for controlled geometry validation failures.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::parcel_shape_metrics_m` via `GeometryError`.
- direct call or construction: `src/landscout/geo/geometry.py::centroid_to_latlon` via `GeometryError`.
- callback/function object: `tests/unit/test_geometry.py::test_zero_area_geometry_raises_controlled_error` via `pytest.raises(GeometryError)`.
- callback/function object: `tests/unit/test_geometry.py::test_centralized_shape_metrics_reject_zero_area_geometry` via `pytest.raises(GeometryError)`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Exact class source**

```python
class GeometryError(ValueError):
    """Base error for controlled geometry validation failures."""
```

### `EmptyGeometryError`

**Purpose:** Raised when an operation receives an empty geometry.

**Kind:** controlled exception.

**Inheritance:** `GeometryError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::_validate_geometry` via `EmptyGeometryError`.
- callback/function object: `tests/unit/test_geometry.py::test_empty_geometry_fails` via `pytest.raises(EmptyGeometryError)`.
- callback/function object: `tests/unit/test_geometry.py::test_shape_metrics_reject_empty_geometry` via `pytest.raises(EmptyGeometryError)`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Exact class source**

```python
class EmptyGeometryError(GeometryError):
    """Raised when an operation receives an empty geometry."""
```

### `InvalidGeometryError`

**Purpose:** Raised when an operation receives an invalid geometry.

**Kind:** controlled exception.

**Inheritance:** `GeometryError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::_validate_geometry` via `InvalidGeometryError`.
- callback/function object: `tests/unit/test_geometry.py::test_invalid_geometry_fails` via `pytest.raises(InvalidGeometryError)`.
- callback/function object: `tests/unit/test_geometry.py::test_shape_metrics_reject_invalid_geometry` via `pytest.raises(InvalidGeometryError)`.
- callback/function object: `tests/unit/test_geometry.py::test_centralized_shape_metrics_reject_invalid_geometry` via `pytest.raises(InvalidGeometryError)`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Exact class source**

```python
class InvalidGeometryError(GeometryError):
    """Raised when an operation receives an invalid geometry."""
```

### `UnsupportedGeometryError`

**Purpose:** Raised when an operation receives an unsupported geometry type.

**Kind:** controlled exception.

**Inheritance:** `GeometryError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::_validate_geometry` via `UnsupportedGeometryError`.
- callback/function object: `tests/unit/test_geometry.py::test_non_geometry_inputs_raise_controlled_error` via `pytest.raises(UnsupportedGeometryError)`.
- callback/function object: `tests/unit/test_geometry.py::test_unsupported_geometry_family_raises_controlled_error` via `pytest.raises(UnsupportedGeometryError)`.
- callback/function object: `tests/unit/test_geometry.py::test_three_dimensional_parcel_is_rejected` via `pytest.raises(UnsupportedGeometryError, match='two-dimensional')`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Exact class source**

```python
class UnsupportedGeometryError(GeometryError):
    """Raised when an operation receives an unsupported geometry type."""
```

### `MetricCrsError`

**Purpose:** Raised when a CRS is unsafe for metric calculations.

**Kind:** controlled exception.

**Inheritance:** `GeometryError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::_parse_crs` via `MetricCrsError`.
- direct call or construction: `src/landscout/geo/geometry.py::_validate_metric_crs` via `MetricCrsError`.
- callback/function object: `tests/unit/test_crs.py::test_reprojection_rejects_malformed_crs_with_controlled_error` via `pytest.raises(MetricCrsError)`.
- import/re-export: `tests/unit/test_crs.py::<module>` via `from landscout.geo import LAMBERT93, WGS84, MetricCrsError, centroid_to_latlon`.
- callback/function object: `tests/unit/test_geometry.py::test_metric_calculation_in_wgs84_fails` via `pytest.raises(MetricCrsError)`.
- callback/function object: `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` via `pytest.raises(MetricCrsError)`.
- callback/function object: `tests/unit/test_geometry.py::test_centralized_shape_metrics_reject_geographic_crs` via `pytest.raises(MetricCrsError)`.
- callback/function object: `tests/unit/test_geometry.py::test_malformed_crs_inputs_raise_controlled_error` via `pytest.raises(MetricCrsError)`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Exact class source**

```python
class MetricCrsError(GeometryError):
    """Raised when a CRS is unsafe for metric calculations."""
```

### `ZeroAreaGeometryError`

**Purpose:** Raised when a shape metric receives a zero-area geometry.

**Kind:** controlled exception.

**Inheritance:** `GeometryError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::parcel_shape_metrics_m` via `ZeroAreaGeometryError`.

**Exact class source**

```python
class ZeroAreaGeometryError(GeometryError):
    """Raised when a shape metric receives a zero-area geometry."""
```


## 6. Functions and methods

### `_validate_geometry`

**Exact signature**

```python
def _validate_geometry(geometry: BaseGeometry) -> Geometry:
```

**Purpose**

Rejects malformed or inconsistent geometry; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `Geometry`.
- Every observed return expression is reproduced without truncation:
```python
geometry
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(geometry, BaseGeometry)`.
- Guard with a raise path: `geometry.is_empty`.
- Guard with a raise path: `not isinstance(geometry, (Polygon, MultiPolygon))`.
- Guard with a raise path: `get_coordinate_dimension(geometry) != 2`.
- Guard with a raise path: `not geometry.is_valid`.
- Explicit raise expressions: `EmptyGeometryError('Geometry must not be empty')`, `InvalidGeometryError('Geometry is invalid and was not repaired')`, `UnsupportedGeometryError('Input must be a Shapely geometry')`, `UnsupportedGeometryError('Only Polygon and MultiPolygon geometries are supported')`, `UnsupportedGeometryError('Parcel geometries must be canonical two-dimensional geometries')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `EmptyGeometryError`, `InvalidGeometryError`, `UnsupportedGeometryError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/geo/geometry.py::reproject_to_lambert93` via `_validate_geometry`.
- direct call or construction: `src/landscout/geo/geometry.py::area_m2` via `_validate_geometry`.
- direct call or construction: `src/landscout/geo/geometry.py::perimeter_m` via `_validate_geometry`.
- direct call or construction: `src/landscout/geo/geometry.py::parcel_shape_metrics_m` via `_validate_geometry`.
- direct call or construction: `src/landscout/geo/geometry.py::centroid` via `_validate_geometry`.

**Complete source-ordered implementation**

```python
def _validate_geometry(geometry: BaseGeometry) -> Geometry:
    if not isinstance(geometry, BaseGeometry):
        raise UnsupportedGeometryError("Input must be a Shapely geometry")
    if geometry.is_empty:
        raise EmptyGeometryError("Geometry must not be empty")
    if not isinstance(geometry, (Polygon, MultiPolygon)):
        raise UnsupportedGeometryError(
            "Only Polygon and MultiPolygon geometries are supported"
        )
    if get_coordinate_dimension(geometry) != 2:
        raise UnsupportedGeometryError(
            "Parcel geometries must be canonical two-dimensional geometries"
        )
    if not geometry.is_valid:
        raise InvalidGeometryError("Geometry is invalid and was not repaired")
    return geometry
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `_parse_crs`

**Exact signature**

```python
def _parse_crs(crs: CRS | str | int) -> CRS:
```

**Purpose**

Parses crs; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
CRS.from_user_input(crs)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `MetricCrsError('Invalid CRS input')`.

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

- direct call or construction: `src/landscout/geo/geometry.py::_validate_metric_crs` via `_parse_crs`.
- direct call or construction: `src/landscout/geo/geometry.py::reproject_to_lambert93` via `_parse_crs`.
- direct call or construction: `src/landscout/geo/geometry.py::centroid_to_latlon` via `_parse_crs`.

**Complete source-ordered implementation**

```python
def _parse_crs(crs: CRS | str | int) -> CRS:
    try:
        return CRS.from_user_input(crs)
    except Exception as error:
        raise MetricCrsError("Invalid CRS input") from error
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `_validate_metric_crs`

**Exact signature**

```python
def _validate_metric_crs(crs: CRS | str | int) -> CRS:
```

**Purpose**

Rejects malformed or inconsistent metric crs; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
parsed
```

**Validation and exceptions**

- Guard with a raise path: `parsed.is_geographic`.
- Guard with a raise path: `not parsed.is_projected`.
- Guard with a raise path: `any((axis.unit_conversion_factor != 1.0 for axis in parsed.axis_info))`.
- Explicit raise expressions: `MetricCrsError('Metric calculations require CRS units in metres')`, `MetricCrsError('Metric calculations require a projected CRS')`.

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

- direct call or construction: `src/landscout/geo/geometry.py::area_m2` via `_validate_metric_crs`.
- direct call or construction: `src/landscout/geo/geometry.py::perimeter_m` via `_validate_metric_crs`.
- direct call or construction: `src/landscout/geo/geometry.py::parcel_shape_metrics_m` via `_validate_metric_crs`.

**Complete source-ordered implementation**

```python
def _validate_metric_crs(crs: CRS | str | int) -> CRS:
    parsed = _parse_crs(crs)
    if parsed.is_geographic:
        raise MetricCrsError("Metric calculations require a projected CRS")
    if not parsed.is_projected:
        raise MetricCrsError("Metric calculations require a projected CRS")
    if any(axis.unit_conversion_factor != 1.0 for axis in parsed.axis_info):
        raise MetricCrsError("Metric calculations require CRS units in metres")
    return parsed
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `reproject_to_lambert93`

**Exact signature**

```python
def reproject_to_lambert93(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> Geometry:
```

**Purpose**

Private `geo/GIS` helper for reproject to lambert93; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Geometry`.
- Every observed return expression is reproduced without truncation:
```python
_validate_geometry(transform(transformer.transform, validated))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_validate_geometry`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `tests/unit/test_crs.py::test_reproject_to_lambert93_and_back_to_latlon` via `reproject_to_lambert93`.
- direct call or construction: `tests/unit/test_crs.py::test_reprojection_rejects_malformed_crs_with_controlled_error` via `reproject_to_lambert93`.
- import/re-export: `tests/unit/test_crs.py::<module>` via `from landscout.geo.geometry import reproject_to_lambert93`.

**Complete source-ordered implementation**

```python
def reproject_to_lambert93(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> Geometry:
    validated = _validate_geometry(geometry)
    transformer = Transformer.from_crs(
        _parse_crs(source_crs), LAMBERT93, always_xy=True
    )
    return _validate_geometry(transform(transformer.transform, validated))
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `area_m2`

**Exact signature**

```python
def area_m2(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Private `geo/GIS` helper for area m2; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
float(validated.area)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_validate_geometry`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `tests/unit/test_geometry.py::test_valid_polygon_in_lambert93` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_area_in_square_metres` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_empty_geometry_fails` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_invalid_geometry_fails` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_multipolygon` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_non_geometry_inputs_raise_controlled_error` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_unsupported_geometry_family_raises_controlled_error` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_three_dimensional_parcel_is_rejected` via `area_m2`.
- direct call or construction: `tests/unit/test_geometry.py::test_malformed_crs_inputs_raise_controlled_error` via `area_m2`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def area_m2(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    validated = _validate_geometry(geometry)
    _validate_metric_crs(crs)
    return float(validated.area)
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `perimeter_m`

**Exact signature**

```python
def perimeter_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Private `geo/GIS` helper for perimeter m; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
float(validated.length)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_validate_geometry`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `tests/unit/test_geometry.py::test_perimeter_in_metres` via `perimeter_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_multipolygon` via `perimeter_m`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def perimeter_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    validated = _validate_geometry(geometry)
    _validate_metric_crs(crs)
    return float(validated.length)
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `parcel_shape_metrics_m`

**Exact signature**

```python
def parcel_shape_metrics_m(
    geometry: BaseGeometry, crs: CRS | str | int
) -> ParcelShapeMetrics:
```

**Purpose**

Private `geo/GIS` helper for parcel shape metrics m; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `ParcelShapeMetrics`.
- Every observed return expression is reproduced without truncation:
```python
ParcelShapeMetrics(length_m=length, width_m=width, length_width_ratio=length / width, compactness=compactness)
```

**Validation and exceptions**

- Guard with a raise path: `area <= 0 or perimeter <= 0`.
- Guard with a raise path: `width <= 0`.
- Guard with a raise path: `length < width`.
- Guard with a raise path: `compactness <= 0`.
- Explicit raise expressions: `GeometryError('Parcel length must be greater than or equal to width')`, `ZeroAreaGeometryError('Parcel compactness must be positive')`, `ZeroAreaGeometryError('Parcel geometry must have a positive area')`, `ZeroAreaGeometryError('Parcel width must be greater than zero')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `GeometryError`, `ZeroAreaGeometryError`, `_validate_geometry`.
- Hashing: `ParcelShapeMetrics`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::approximate_length_m` via `parcel_shape_metrics_m`.
- direct call or construction: `src/landscout/geo/geometry.py::approximate_width_m` via `parcel_shape_metrics_m`.
- direct call or construction: `src/landscout/geo/geometry.py::length_width_ratio` via `parcel_shape_metrics_m`.
- direct call or construction: `src/landscout/geo/geometry.py::compactness_score` via `parcel_shape_metrics_m`.
- direct call or construction: `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` via `parcel_shape_metrics_m`.
- import/re-export: `src/landscout/stages/enrich_shape.py::<module>` via `from landscout.geo.geometry import parcel_shape_metrics_m`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics` via `parcel_shape_metrics_m`.
- import/re-export: `tests/unit/test_enrich_shape.py::<module>` via `from landscout.geo import LAMBERT93, parcel_shape_metrics_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_centralized_shape_metrics` via `parcel_shape_metrics_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_centralized_shape_metrics_support_multipolygon` via `parcel_shape_metrics_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_centralized_shape_metrics_reject_invalid_geometry` via `parcel_shape_metrics_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_centralized_shape_metrics_reject_zero_area_geometry` via `parcel_shape_metrics_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_centralized_shape_metrics_reject_geographic_crs` via `parcel_shape_metrics_m`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def parcel_shape_metrics_m(
    geometry: BaseGeometry, crs: CRS | str | int
) -> ParcelShapeMetrics:
    validated = _validate_geometry(geometry)
    _validate_metric_crs(crs)
    area = float(validated.area)
    perimeter = float(validated.length)
    if area <= 0 or perimeter <= 0:
        raise ZeroAreaGeometryError("Parcel geometry must have a positive area")

    rectangle = validated.minimum_rotated_rectangle
    coordinates = list(rectangle.exterior.coords)
    edge_lengths = [
        hypot(end[0] - start[0], end[1] - start[1])
        for start, end in pairwise(coordinates)
    ]
    length = float(max(edge_lengths))
    width = float(min(edge_lengths))
    if width <= 0:
        raise ZeroAreaGeometryError("Parcel width must be greater than zero")
    if length < width:
        raise GeometryError("Parcel length must be greater than or equal to width")

    compactness = min(float(4 * pi * area / perimeter**2), 1.0)
    if compactness <= 0:
        raise ZeroAreaGeometryError("Parcel compactness must be positive")
    return ParcelShapeMetrics(
        length_m=length,
        width_m=width,
        length_width_ratio=length / width,
        compactness=compactness,
    )
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `approximate_length_m`

**Exact signature**

```python
def approximate_length_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Private `geo/GIS` helper for approximate length m; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
parcel_shape_metrics_m(geometry, crs).length_m
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `parcel_shape_metrics_m`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `tests/unit/test_geometry.py::test_square_shape_metrics` via `approximate_length_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_simple_rectangle_shape_metrics` via `approximate_length_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_rotated_rectangle_is_orientation_independent` via `approximate_length_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_multipolygon_shape_metrics` via `approximate_length_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` via `approximate_length_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_shape_metrics_reject_invalid_geometry` via `approximate_length_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_length_is_always_at_least_width` via `approximate_length_m`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def approximate_length_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).length_m
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `approximate_width_m`

**Exact signature**

```python
def approximate_width_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Private `geo/GIS` helper for approximate width m; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
parcel_shape_metrics_m(geometry, crs).width_m
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `parcel_shape_metrics_m`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `tests/unit/test_geometry.py::test_square_shape_metrics` via `approximate_width_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_simple_rectangle_shape_metrics` via `approximate_width_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_rotated_rectangle_is_orientation_independent` via `approximate_width_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_multipolygon_shape_metrics` via `approximate_width_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` via `approximate_width_m`.
- direct call or construction: `tests/unit/test_geometry.py::test_length_is_always_at_least_width` via `approximate_width_m`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def approximate_width_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).width_m
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `length_width_ratio`

**Exact signature**

```python
def length_width_ratio(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Private `geo/GIS` helper for length width ratio; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
parcel_shape_metrics_m(geometry, crs).length_width_ratio
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `parcel_shape_metrics_m`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- property/attribute access: `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` via `shape.length_width_ratio`.
- callback/property argument: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `float(row.length_width_ratio)`.
- property/attribute access: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `row.length_width_ratio`.
- callback/property argument: `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics` via `pytest.approx(expected.length_width_ratio)`.
- property/attribute access: `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics` via `expected.length_width_ratio`.
- direct call or construction: `tests/unit/test_geometry.py::test_square_shape_metrics` via `length_width_ratio`.
- direct call or construction: `tests/unit/test_geometry.py::test_simple_rectangle_shape_metrics` via `length_width_ratio`.
- direct call or construction: `tests/unit/test_geometry.py::test_rotated_rectangle_is_orientation_independent` via `length_width_ratio`.
- direct call or construction: `tests/unit/test_geometry.py::test_elongated_rectangle_is_less_compact_than_square` via `length_width_ratio`.
- direct call or construction: `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` via `length_width_ratio`.
- direct call or construction: `tests/unit/test_geometry.py::test_zero_area_geometry_raises_controlled_error` via `length_width_ratio`.
- property/attribute access: `tests/unit/test_geometry.py::test_centralized_shape_metrics` via `metrics.length_width_ratio`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def length_width_ratio(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).length_width_ratio
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `compactness_score`

**Exact signature**

```python
def compactness_score(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Private `geo/GIS` helper for compactness score; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
parcel_shape_metrics_m(geometry, crs).compactness
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `parcel_shape_metrics_m`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `tests/unit/test_geometry.py::test_square_shape_metrics` via `compactness_score`.
- direct call or construction: `tests/unit/test_geometry.py::test_elongated_rectangle_is_less_compact_than_square` via `compactness_score`.
- direct call or construction: `tests/unit/test_geometry.py::test_multipolygon_shape_metrics` via `compactness_score`.
- direct call or construction: `tests/unit/test_geometry.py::test_shape_metrics_reject_geographic_crs` via `compactness_score`.
- direct call or construction: `tests/unit/test_geometry.py::test_shape_metrics_reject_empty_geometry` via `compactness_score`.
- direct call or construction: `tests/unit/test_geometry.py::test_compactness_range` via `compactness_score`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def compactness_score(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).compactness
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `centroid`

**Exact signature**

```python
def centroid(geometry: BaseGeometry) -> Point:
```

**Purpose**

Private `geo/GIS` helper for centroid; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Point`.
- Every observed return expression is reproduced without truncation:
```python
_validate_geometry(geometry).centroid
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_validate_geometry`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `src/landscout/geo/geometry.py::centroid_to_latlon` via `centroid`.
- property/attribute access: `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` via `projected.geometry.centroid`.
- property/attribute access: `tests/unit/test_enrich_shape.py::test_centroid_coordinates` via `square.centroid`.
- direct call or construction: `tests/unit/test_geometry.py::test_centroid` via `centroid`.
- import/re-export: `tests/unit/test_geometry.py::<module>` via `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`.

**Complete source-ordered implementation**

```python
def centroid(geometry: BaseGeometry) -> Point:
    return _validate_geometry(geometry).centroid
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.

### `centroid_to_latlon`

**Exact signature**

```python
def centroid_to_latlon(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> tuple[float, float]:
```

**Purpose**

Private `geo/GIS` helper for centroid to latlon; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[float, float]`.
- Every observed return expression is reproduced without truncation:
```python
(latitude, longitude)
```

**Validation and exceptions**

- Guard with a raise path: `not isfinite(latitude) or not isfinite(longitude) or (not -90 <= latitude <= 90) or (not -180 <= longitude <= 180)`.
- Explicit raise expressions: `GeometryError('Centroid transform produced invalid latitude/longitude')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `GeometryError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/geo/__init__.py::<module>` via `from landscout.geo.geometry import (
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
)`.
- direct call or construction: `tests/unit/test_crs.py::test_reproject_to_lambert93_and_back_to_latlon` via `centroid_to_latlon`.
- import/re-export: `tests/unit/test_crs.py::<module>` via `from landscout.geo import LAMBERT93, WGS84, MetricCrsError, centroid_to_latlon`.

**Complete source-ordered implementation**

```python
def centroid_to_latlon(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> tuple[float, float]:
    center = centroid(geometry)
    transformer = Transformer.from_crs(_parse_crs(source_crs), WGS84, always_xy=True)
    longitude, latitude = transformer.transform(center.x, center.y)
    latitude = float(latitude)
    longitude = float(longitude)
    if (
        not isfinite(latitude)
        or not isfinite(longitude)
        or not -90 <= latitude <= 90
        or not -180 <= longitude <= 180
    ):
        raise GeometryError("Centroid transform produced invalid latitude/longitude")
    return latitude, longitude
```

**Business boundary**

- Geometry utilities measure or validate geometry only; they do not decide parcel suitability, authorization, capacity, access, or ownership.


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
