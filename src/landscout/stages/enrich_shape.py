from itertools import pairwise
from math import hypot, isfinite, pi

import geopandas as gpd  # type: ignore[import-untyped]
from shapely.errors import GEOSException  # type: ignore[import-untyped]

from landscout.geo.crs import LAMBERT93, WGS84

REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
DERIVED_METRIC_COLUMNS = (
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
    "centroid_lat",
    "centroid_lon",
)
SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})


class ShapeEnrichmentError(ValueError):
    """Raised when candidate parcels cannot be enriched safely."""


def enrich_parcel_shapes(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    missing_columns = REQUIRED_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ShapeEnrichmentError(f"Missing required candidate columns: {formatted}")
    if parcels.crs is None:
        raise ShapeEnrichmentError("Candidate parcel CRS is required")
    if parcels.crs != WGS84:
        raise ShapeEnrichmentError("Candidate parcels must use EPSG:4326")
    if parcels.active_geometry_name != "geometry":
        raise ShapeEnrichmentError("An active geometry column is required")
    if parcels["parcel_id"].isna().any():
        raise ShapeEnrichmentError("parcel_id values must not be null")
    if parcels["parcel_id"].duplicated().any():
        raise ShapeEnrichmentError("parcel_id values must be unique")

    output = parcels.reset_index(drop=True).copy()
    output["shape_status"] = "ERROR"
    for column in DERIVED_METRIC_COLUMNS:
        output[column] = float("nan")

    measurable = (
        (output["geometry_status"] == "VALID")
        & output.geometry.notna()
        & ~output.geometry.is_empty
        & output.geometry.is_valid
        & output.geometry.geom_type.isin(SUPPORTED_GEOMETRY_TYPES)
    )
    projected = output.loc[measurable].to_crs(LAMBERT93)
    projected_areas = projected.geometry.area
    projected_perimeters = projected.geometry.length
    projected_centroids = projected.geometry.centroid
    centroids_wgs84 = gpd.GeoSeries(
        projected_centroids, index=projected.index, crs=LAMBERT93
    ).to_crs(WGS84)

    for index, geometry in projected.geometry.items():
        try:
            rectangle_coordinates = list(
                geometry.minimum_rotated_rectangle.exterior.coords
            )
            edge_lengths = [
                hypot(end[0] - start[0], end[1] - start[1])
                for start, end in pairwise(rectangle_coordinates)
            ]
            length = float(max(edge_lengths))
            width = float(min(edge_lengths))
            area = float(projected_areas.loc[index])
            perimeter = float(projected_perimeters.loc[index])
            compactness = min(float(4 * pi * area / perimeter**2), 1.0)
            center = centroids_wgs84.loc[index]
            latitude = float(center.y)
            longitude = float(center.x)
            metrics = (
                length,
                width,
                length / width,
                compactness,
                latitude,
                longitude,
            )
            if (
                width <= 0
                or area <= 0
                or perimeter <= 0
                or compactness <= 0
                or not all(isfinite(value) for value in metrics)
            ):
                continue
        except (AttributeError, GEOSException, IndexError, TypeError, ValueError, ZeroDivisionError):
            continue

        output.loc[index, "shape_status"] = "VALID"
        for column, value in zip(DERIVED_METRIC_COLUMNS, metrics, strict=True):
            output.loc[index, column] = value

    input_ids = set(parcels["parcel_id"])
    output_ids = set(output["parcel_id"])
    if len(output) != len(parcels) or input_ids != output_ids:
        raise ShapeEnrichmentError("Shape enrichment did not preserve exact parcel IDs")
    return output
