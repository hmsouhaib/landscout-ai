from pyproj import CRS, Transformer
from pyproj.exceptions import CRSError
from shapely.geometry import (  # type: ignore[import-untyped]
    MultiPolygon,
    Point,
    Polygon,
)
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]
from shapely.ops import transform  # type: ignore[import-untyped]

from landscout.geo.crs import LAMBERT93, WGS84

type Geometry = Polygon | MultiPolygon


class GeometryError(ValueError):
    """Base error for controlled geometry validation failures."""


class EmptyGeometryError(GeometryError):
    """Raised when an operation receives an empty geometry."""


class InvalidGeometryError(GeometryError):
    """Raised when an operation receives an invalid geometry."""


class UnsupportedGeometryError(GeometryError):
    """Raised when an operation receives an unsupported geometry type."""


class MetricCrsError(GeometryError):
    """Raised when a CRS is unsafe for metric calculations."""


def _validate_geometry(geometry: BaseGeometry) -> Geometry:
    if geometry.is_empty:
        raise EmptyGeometryError("Geometry must not be empty")
    if not isinstance(geometry, (Polygon, MultiPolygon)):
        raise UnsupportedGeometryError(
            "Only Polygon and MultiPolygon geometries are supported"
        )
    if not geometry.is_valid:
        raise InvalidGeometryError("Geometry is invalid and was not repaired")
    return geometry


def _parse_crs(crs: CRS | str | int) -> CRS:
    try:
        return CRS.from_user_input(crs)
    except CRSError as error:
        raise MetricCrsError(f"Invalid CRS: {crs}") from error


def _validate_metric_crs(crs: CRS | str | int) -> CRS:
    parsed = _parse_crs(crs)
    if parsed.is_geographic:
        raise MetricCrsError("Metric calculations require a projected CRS")
    if not parsed.is_projected:
        raise MetricCrsError("Metric calculations require a projected CRS")
    if any(axis.unit_conversion_factor != 1.0 for axis in parsed.axis_info):
        raise MetricCrsError("Metric calculations require CRS units in metres")
    return parsed


def reproject_to_lambert93(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> Geometry:
    validated = _validate_geometry(geometry)
    transformer = Transformer.from_crs(
        _parse_crs(source_crs), LAMBERT93, always_xy=True
    )
    return _validate_geometry(transform(transformer.transform, validated))


def area_m2(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    validated = _validate_geometry(geometry)
    _validate_metric_crs(crs)
    return float(validated.area)


def perimeter_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    validated = _validate_geometry(geometry)
    _validate_metric_crs(crs)
    return float(validated.length)


def centroid(geometry: BaseGeometry) -> Point:
    return _validate_geometry(geometry).centroid


def centroid_to_latlon(
    geometry: BaseGeometry, source_crs: CRS | str | int
) -> tuple[float, float]:
    center = centroid(geometry)
    transformer = Transformer.from_crs(_parse_crs(source_crs), WGS84, always_xy=True)
    longitude, latitude = transformer.transform(center.x, center.y)
    return float(latitude), float(longitude)
