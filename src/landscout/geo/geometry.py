from dataclasses import dataclass
from itertools import pairwise
from math import hypot, isfinite, pi

from pyproj import CRS, Transformer
from shapely import get_coordinate_dimension  # type: ignore[import-untyped]
from shapely.geometry import (  # type: ignore[import-untyped]
    MultiPolygon,
    Point,
    Polygon,
)
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]
from shapely.ops import transform  # type: ignore[import-untyped]

from landscout.geo.crs import LAMBERT93, WGS84

type Geometry = Polygon | MultiPolygon


@dataclass(frozen=True)
class ParcelShapeMetrics:
    length_m: float
    width_m: float
    length_width_ratio: float
    compactness: float


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


class ZeroAreaGeometryError(GeometryError):
    """Raised when a shape metric receives a zero-area geometry."""


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


def _parse_crs(crs: CRS | str | int) -> CRS:
    try:
        return CRS.from_user_input(crs)
    except Exception as error:
        raise MetricCrsError("Invalid CRS input") from error


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


def approximate_length_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).length_m


def approximate_width_m(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).width_m


def length_width_ratio(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).length_width_ratio


def compactness_score(geometry: BaseGeometry, crs: CRS | str | int) -> float:
    return parcel_shape_metrics_m(geometry, crs).compactness


def centroid(geometry: BaseGeometry) -> Point:
    return _validate_geometry(geometry).centroid


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
