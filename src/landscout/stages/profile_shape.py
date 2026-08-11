from dataclasses import dataclass

import geopandas as gpd  # type: ignore[import-untyped]

PROFILE_METRICS = (
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
)
REPRESENTATIVE_FIELDS = (
    "parcel_id",
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
    "centroid_lat",
    "centroid_lon",
)
REQUIRED_COLUMNS = frozenset({"parcel_id", "shape_status", *REPRESENTATIVE_FIELDS})
PERCENTILES = {
    "min": 0.0,
    "p01": 0.01,
    "p05": 0.05,
    "p10": 0.10,
    "p25": 0.25,
    "p50": 0.50,
    "p75": 0.75,
    "p90": 0.90,
    "p95": 0.95,
    "p99": 0.99,
    "max": 1.0,
}


class ShapeProfileError(ValueError):
    """Raised when shape candidates cannot be profiled safely."""


@dataclass(frozen=True)
class DiagnosticScenario:
    retained_count: int
    retained_percentage: float


@dataclass(frozen=True)
class ShapeDistributionProfile:
    input_count: int
    distributions: dict[str, dict[str, float]]
    width_buckets: dict[str, int]
    ratio_buckets: dict[str, int]
    compactness_buckets: dict[str, int]
    scenarios: dict[str, DiagnosticScenario]
    median_parcels: list[dict[str, object]]
    extreme_parcels: list[dict[str, object]]


def _records(frame: gpd.GeoDataFrame) -> list[dict[str, object]]:
    return frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient="records")


def profile_shape_distribution(
    parcels: gpd.GeoDataFrame,
) -> ShapeDistributionProfile:
    missing_columns = REQUIRED_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ShapeProfileError(f"Missing required shape columns: {formatted}")
    if parcels.crs is None:
        raise ShapeProfileError("Shape candidate CRS is required")
    if parcels["parcel_id"].isna().any():
        raise ShapeProfileError("parcel_id values must not be null")
    if parcels["parcel_id"].duplicated().any():
        raise ShapeProfileError("parcel_id values must be unique")

    valid_shapes = parcels["shape_status"] == "VALID"
    required_valid_metrics = [
        *PROFILE_METRICS,
        "centroid_lat",
        "centroid_lon",
    ]
    if parcels.loc[valid_shapes, required_valid_metrics].isna().any().any():
        raise ShapeProfileError("VALID shape rows must have complete shape metrics")

    working = parcels.copy()
    distributions = {
        metric: {
            label: float(working[metric].quantile(quantile))
            for label, quantile in PERCENTILES.items()
        }
        for metric in PROFILE_METRICS
    }

    width = working["width_m"]
    width_buckets = {
        "width < 5 m": int((width < 5).sum()),
        "5–10 m": int(((width >= 5) & (width < 10)).sum()),
        "10–15 m": int(((width >= 10) & (width < 15)).sum()),
        "15–20 m": int(((width >= 15) & (width < 20)).sum()),
        "20–25 m": int(((width >= 20) & (width < 25)).sum()),
        "25–30 m": int(((width >= 25) & (width < 30)).sum()),
        "30–40 m": int(((width >= 30) & (width < 40)).sum()),
        "40–50 m": int(((width >= 40) & (width < 50)).sum()),
        "width >= 50 m": int((width >= 50).sum()),
    }

    ratio = working["length_width_ratio"]
    ratio_buckets = {
        "ratio <= 2": int((ratio <= 2).sum()),
        "2–3": int(((ratio > 2) & (ratio <= 3)).sum()),
        "3–4": int(((ratio > 3) & (ratio <= 4)).sum()),
        "4–5": int(((ratio > 4) & (ratio <= 5)).sum()),
        "5–7": int(((ratio > 5) & (ratio <= 7)).sum()),
        "7–10": int(((ratio > 7) & (ratio <= 10)).sum()),
        "10–15": int(((ratio > 10) & (ratio <= 15)).sum()),
        "15–25": int(((ratio > 15) & (ratio <= 25)).sum()),
        "ratio > 25": int((ratio > 25).sum()),
    }

    compactness = working["compactness"]
    compactness_buckets = {
        "compactness < 0.05": int((compactness < 0.05).sum()),
        "0.05–0.10": int(((compactness >= 0.05) & (compactness < 0.10)).sum()),
        "0.10–0.20": int(((compactness >= 0.10) & (compactness < 0.20)).sum()),
        "0.20–0.30": int(((compactness >= 0.20) & (compactness < 0.30)).sum()),
        "0.30–0.40": int(((compactness >= 0.30) & (compactness < 0.40)).sum()),
        "0.40–0.50": int(((compactness >= 0.40) & (compactness < 0.50)).sum()),
        "0.50–0.60": int(((compactness >= 0.50) & (compactness < 0.60)).sum()),
        "0.60–0.70": int(((compactness >= 0.60) & (compactness < 0.70)).sum()),
        "compactness >= 0.70": int((compactness >= 0.70).sum()),
    }

    scenario_masks = {
        "A": width >= 10,
        "B": width >= 15,
        "C": width >= 20,
        "D": (width >= 15) & (ratio <= 10),
        "E": (width >= 20) & (ratio <= 7),
        "F": (width >= 20) & (ratio <= 5) & (compactness >= 0.20),
    }
    count = len(working)
    scenarios = {
        name: DiagnosticScenario(
            retained_count=int(mask.sum()),
            retained_percentage=float(mask.sum() / count * 100) if count else 0.0,
        )
        for name, mask in scenario_masks.items()
    }

    working["_median_score"] = 0.0
    for metric in PROFILE_METRICS:
        median = working[metric].median()
        scale = working[metric].quantile(0.75) - working[metric].quantile(0.25)
        if scale == 0:
            scale = 1.0
        working["_median_score"] += (working[metric] - median).abs() / scale
    median_frame = working.nsmallest(5, "_median_score")

    working["_extreme_score"] = (
        working["length_width_ratio"].rank(pct=True)
        + (-working["width_m"]).rank(pct=True)
        + (-working["compactness"]).rank(pct=True)
    )
    extreme_pool = working.loc[
        ~working["parcel_id"].isin(median_frame["parcel_id"])
    ]
    extreme_frame = extreme_pool.nlargest(5, "_extreme_score")

    return ShapeDistributionProfile(
        input_count=count,
        distributions=distributions,
        width_buckets=width_buckets,
        ratio_buckets=ratio_buckets,
        compactness_buckets=compactness_buckets,
        scenarios=scenarios,
        median_parcels=_records(median_frame),
        extreme_parcels=_records(extreme_frame),
    )
