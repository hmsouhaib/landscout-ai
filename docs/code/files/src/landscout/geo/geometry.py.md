# `src/landscout/geo/geometry.py`

## File identity

- Repository path: `src/landscout/geo/geometry.py`
- File type: Python source
- Primary responsibility: Validates parcel geometry and computes metric shape measurements on calculation-only Lambert-93 copies.
- Layer / domain: `GIS utility` / `common`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `465e20701bcf325f0191548e4ed7c7c471d7764e595ada632efabcd1404fced6`

## 1. Purpose

Validates parcel geometry and computes metric shape measurements on calculation-only Lambert-93 copies.

## 2. Position in LandScout architecture

This file is a `GIS utility` artifact in the `common` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from math import hypot, isfinite, pi` — required by the implementation paths and symbols documented below.

### Third-party

- `from itertools import pairwise` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS, Transformer` — required by the implementation paths and symbols documented below.
- `from shapely import get_coordinate_dimension` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( # type: ignore[import-untyped] MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.
- `from shapely.geometry.base import BaseGeometry` — required by the implementation paths and symbols documented below.
- `from shapely.ops import transform` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.geo.crs import LAMBERT93, WGS84` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

### `ParcelShapeMetrics`

**Purpose:** Groups the `ParcelShapeMetrics` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `length_m` | `float` | `required` | Metric distance or length in metres; the full field name identifies the measurement. |
| `width_m` | `float` | `required` | Metric distance or length in metres; the full field name identifies the measurement. |
| `length_width_ratio` | `float` | `required` | `float` state used by `src/landscout/geo/geometry.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `compactness` | `float` | `required` | `float` state used by `src/landscout/geo/geometry.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GeometryError`

**Purpose:** Base error for controlled geometry validation failures.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `EmptyGeometryError`

**Purpose:** Raised when an operation receives an empty geometry.

**Inheritance:** `GeometryError`.

**Model form and mutability:** class inheriting from `GeometryError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `InvalidGeometryError`

**Purpose:** Raised when an operation receives an invalid geometry.

**Inheritance:** `GeometryError`.

**Model form and mutability:** class inheriting from `GeometryError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `UnsupportedGeometryError`

**Purpose:** Raised when an operation receives an unsupported geometry type.

**Inheritance:** `GeometryError`.

**Model form and mutability:** class inheriting from `GeometryError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `MetricCrsError`

**Purpose:** Raised when a CRS is unsafe for metric calculations.

**Inheritance:** `GeometryError`.

**Model form and mutability:** class inheriting from `GeometryError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `ZeroAreaGeometryError`

**Purpose:** Raised when a shape metric receives a zero-area geometry.

**Inheritance:** `GeometryError`.

**Model form and mutability:** class inheriting from `GeometryError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `_validate_geometry`

**Signature**

```python
def _validate_geometry(geometry: BaseGeometry) -> Geometry:
```

**Purpose**

Validates and rejects malformed geometry according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Geometry`. Observed return expression(s): `geometry`.

**Algorithm**

1. Checks `not isinstance(geometry, BaseGeometry)`. When true: Raises `UnsupportedGeometryError('Input must be a Shapely geometry')`.
2. Checks `geometry.is_empty`. When true: Raises `EmptyGeometryError('Geometry must not be empty')`.
3. Checks `not isinstance(geometry, (Polygon, MultiPolygon))`. When true: Raises `UnsupportedGeometryError('Only Polygon and MultiPolygon geometries are supported')`.
4. Checks `get_coordinate_dimension(geometry) != 2`. When true: Raises `UnsupportedGeometryError('Parcel geometries must be canonical two-dimensional geometries')`.
5. Checks `not geometry.is_valid`. When true: Raises `InvalidGeometryError('Geometry is invalid and was not repaired')`.
6. Returns `geometry`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(geometry, BaseGeometry)` is true.
- Rejects or diverts the path when `geometry.is_empty` is true.
- Rejects or diverts the path when `not isinstance(geometry, (Polygon, MultiPolygon))` is true.
- Rejects or diverts the path when `get_coordinate_dimension(geometry) != 2` is true.
- Rejects or diverts the path when `not geometry.is_valid` is true.

**Exceptions**

- Explicitly raises: `EmptyGeometryError`, `InvalidGeometryError`, `UnsupportedGeometryError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `EmptyGeometryError`, `InvalidGeometryError`, `UnsupportedGeometryError`, `get_coordinate_dimension`, `isinstance`.

**Known repository callers**

- `src/landscout/geo/geometry.py` — `area_m2`
- `src/landscout/geo/geometry.py` — `centroid`
- `src/landscout/geo/geometry.py` — `parcel_shape_metrics_m`
- `src/landscout/geo/geometry.py` — `perimeter_m`
- `src/landscout/geo/geometry.py` — `reproject_to_lambert93`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_parse_crs`

**Signature**

```python
def _parse_crs(crs: CRS | str | int) -> CRS:
```

**Purpose**

Parses crs according to the exact implementation and guards in this file.

**Inputs**

- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `CRS.from_user_input(crs)`.

**Algorithm**

1. Runs guarded operation: Returns `CRS.from_user_input(crs)`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `MetricCrsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `MetricCrsError`.

**Known repository callers**

- `src/landscout/geo/geometry.py` — `_validate_metric_crs`
- `src/landscout/geo/geometry.py` — `centroid_to_latlon`
- `src/landscout/geo/geometry.py` — `reproject_to_lambert93`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_validate_metric_crs`

**Signature**

```python
def _validate_metric_crs(crs: CRS | str | int) -> CRS:
```

**Purpose**

Validates and rejects malformed metric crs according to the exact implementation and guards in this file.

**Inputs**

- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `parsed`.

**Algorithm**

1. Computes `parsed` from `_parse_crs(crs)`.
2. Checks `parsed.is_geographic`. When true: Raises `MetricCrsError('Metric calculations require a projected CRS')`.
3. Checks `not parsed.is_projected`. When true: Raises `MetricCrsError('Metric calculations require a projected CRS')`.
4. Checks `any((axis.unit_conversion_factor != 1.0 for axis in parsed.axis_info))`. When true: Raises `MetricCrsError('Metric calculations require CRS units in metres')`.
5. Returns `parsed`.

**Validation and invariants**

- Rejects or diverts the path when `parsed.is_geographic` is true.
- Rejects or diverts the path when `not parsed.is_projected` is true.
- Rejects or diverts the path when `any((axis.unit_conversion_factor != 1.0 for axis in parsed.axis_info))` is true.

**Exceptions**

- Explicitly raises: `MetricCrsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `MetricCrsError`, `_parse_crs`, `any`.

**Known repository callers**

- `src/landscout/geo/geometry.py` — `area_m2`
- `src/landscout/geo/geometry.py` — `parcel_shape_metrics_m`
- `src/landscout/geo/geometry.py` — `perimeter_m`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `reproject_to_lambert93`

**Signature**

```python
def reproject_to_lambert93(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> Geometry:
```

**Purpose**

Implements reproject to lambert93 according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_crs` (`CRS | str | int`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Geometry`. Observed return expression(s): `_validate_geometry(transform(transformer.transform, validated))`.

**Algorithm**

1. Computes `validated` from `_validate_geometry(geometry)`.
2. Computes `transformer` from `Transformer.from_crs(_parse_crs(source_crs), LAMBERT93, always_xy=True)`.
3. Returns `_validate_geometry(transform(transformer.transform, validated))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Transformer.from_crs`, `_parse_crs`, `_validate_geometry`, `transform`.

**Known repository callers**

- `tests/unit/test_crs.py` — `test_reproject_to_lambert93_and_back_to_latlon`
- `tests/unit/test_crs.py` — `test_reprojection_rejects_malformed_crs_with_controlled_error`

**Tests**

- `tests/unit/test_crs.py::test_reproject_to_lambert93_and_back_to_latlon`
- `tests/unit/test_crs.py::test_reprojection_rejects_malformed_crs_with_controlled_error`

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `area_m2`

**Signature**

```python
def area_m2(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Implements area m2 according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `float(validated.area)`.

**Algorithm**

1. Computes `validated` from `_validate_geometry(geometry)`.
2. Calls `_validate_metric_crs(crs)` for its validation or side effect.
3. Returns `float(validated.area)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_geometry`, `_validate_metric_crs`, `float`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `perimeter_m`

**Signature**

```python
def perimeter_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Implements perimeter m according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `float(validated.length)`.

**Algorithm**

1. Computes `validated` from `_validate_geometry(geometry)`.
2. Calls `_validate_metric_crs(crs)` for its validation or side effect.
3. Returns `float(validated.length)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_geometry`, `_validate_metric_crs`, `float`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `parcel_shape_metrics_m`

**Signature**

```python
def parcel_shape_metrics_m(
    geometry: BaseGeometry, crs: CRS | str | int
) -> ParcelShapeMetrics:
```

**Purpose**

Implements parcel shape metrics m according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelShapeMetrics`. Observed return expression(s): `ParcelShapeMetrics(length_m=length, width_m=width, length_width_ratio=length / width, compactness=compactness)`.

**Algorithm**

1. Computes `validated` from `_validate_geometry(geometry)`.
2. Calls `_validate_metric_crs(crs)` for its validation or side effect.
3. Computes `area` from `float(validated.area)`.
4. Computes `perimeter` from `float(validated.length)`.
5. Checks `area <= 0 or perimeter <= 0`. When true: Raises `ZeroAreaGeometryError('Parcel geometry must have a positive area')`.
6. Computes `rectangle` from `validated.minimum_rotated_rectangle`.
7. Computes `coordinates` from `list(rectangle.exterior.coords)`.
8. Computes `edge_lengths` from `[hypot(end[0] - start[0], end[1] - start[1]) for start, end in pairwise(coordinates)]`.
9. Computes `length` from `float(max(edge_lengths))`.
10. Computes `width` from `float(min(edge_lengths))`.
11. Checks `width <= 0`. When true: Raises `ZeroAreaGeometryError('Parcel width must be greater than zero')`.
12. Checks `length < width`. When true: Raises `GeometryError('Parcel length must be greater than or equal to width')`.
13. Computes `compactness` from `min(float(4 * pi * area / perimeter ** 2), 1.0)`.
14. Checks `compactness <= 0`. When true: Raises `ZeroAreaGeometryError('Parcel compactness must be positive')`.
15. Returns `ParcelShapeMetrics(length_m=length, width_m=width, length_width_ratio=length / width, compactness=compactness)`.

**Validation and invariants**

- Rejects or diverts the path when `area <= 0 or perimeter <= 0` is true.
- Rejects or diverts the path when `width <= 0` is true.
- Rejects or diverts the path when `length < width` is true.
- Rejects or diverts the path when `compactness <= 0` is true.

**Exceptions**

- Explicitly raises: `GeometryError`, `ZeroAreaGeometryError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GeometryError`, `ParcelShapeMetrics`, `ZeroAreaGeometryError`, `_validate_geometry`, `_validate_metric_crs`, `float`, `hypot`, `list`, `max`, `min`, `pairwise`.

**Known repository callers**

- `src/landscout/geo/geometry.py` — `approximate_length_m`
- `src/landscout/geo/geometry.py` — `approximate_width_m`
- `src/landscout/geo/geometry.py` — `compactness_score`
- `src/landscout/geo/geometry.py` — `length_width_ratio`
- `src/landscout/stages/enrich_shape.py` — `enrich_parcel_shapes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `approximate_length_m`

**Signature**

```python
def approximate_length_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Implements approximate length m according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `parcel_shape_metrics_m(geometry, crs).length_m`.

**Algorithm**

1. Returns `parcel_shape_metrics_m(geometry, crs).length_m`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `parcel_shape_metrics_m`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `approximate_width_m`

**Signature**

```python
def approximate_width_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Implements approximate width m according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `parcel_shape_metrics_m(geometry, crs).width_m`.

**Algorithm**

1. Returns `parcel_shape_metrics_m(geometry, crs).width_m`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `parcel_shape_metrics_m`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `length_width_ratio`

**Signature**

```python
def length_width_ratio(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Implements length width ratio according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `parcel_shape_metrics_m(geometry, crs).length_width_ratio`.

**Algorithm**

1. Returns `parcel_shape_metrics_m(geometry, crs).length_width_ratio`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `parcel_shape_metrics_m`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `compactness_score`

**Signature**

```python
def compactness_score(geometry: BaseGeometry, crs: CRS | str | int) -> float:
```

**Purpose**

Implements compactness score according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`CRS | str | int`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `parcel_shape_metrics_m(geometry, crs).compactness`.

**Algorithm**

1. Returns `parcel_shape_metrics_m(geometry, crs).compactness`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `parcel_shape_metrics_m`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `centroid`

**Signature**

```python
def centroid(geometry: BaseGeometry) -> Point:
```

**Purpose**

Implements centroid according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Point`. Observed return expression(s): `_validate_geometry(geometry).centroid`.

**Algorithm**

1. Returns `_validate_geometry(geometry).centroid`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_geometry`.

**Known repository callers**

- `src/landscout/geo/geometry.py` — `centroid_to_latlon`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `centroid_to_latlon`

**Signature**

```python
def centroid_to_latlon(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> tuple[float, float]:
```

**Purpose**

Implements centroid to latlon according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`BaseGeometry`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_crs` (`CRS | str | int`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[float, float]`. Observed return expression(s): `(latitude, longitude)`.

**Algorithm**

1. Computes `center` from `centroid(geometry)`.
2. Computes `transformer` from `Transformer.from_crs(_parse_crs(source_crs), WGS84, always_xy=True)`.
3. Computes `(longitude, latitude)` from `transformer.transform(center.x, center.y)`.
4. Computes `latitude` from `float(latitude)`.
5. Computes `longitude` from `float(longitude)`.
6. Checks `not isfinite(latitude) or not isfinite(longitude) or (not -90 <= latitude <= 90) or (not -180 <= longitude <= 180)`. When true: Raises `GeometryError('Centroid transform produced invalid latitude/longitude')`.
7. Returns `(latitude, longitude)`.

**Validation and invariants**

- Rejects or diverts the path when `not isfinite(latitude) or not isfinite(longitude) or (not -90 <= latitude <= 90) or (not -180 <= longitude <= 180)` is true.

**Exceptions**

- Explicitly raises: `GeometryError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GeometryError`, `Transformer.from_crs`, `_parse_crs`, `centroid`, `float`, `isfinite`, `transformer.transform`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

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

This file contributes to LandScout's `common` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
