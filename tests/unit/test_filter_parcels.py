import geopandas as gpd
import pandas as pd
import pytest
from shapely.geometry import Polygon

from landscout.config import ParcelConfig
from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area


@pytest.fixture
def area_config() -> ParcelConfig:
    return ParcelConfig(min_area_m2=2000, max_area_m2=15000)


@pytest.fixture
def parcels() -> gpd.GeoDataFrame:
    geometry = Polygon([(2.0, 43.0), (2.1, 43.0), (2.1, 43.1), (2.0, 43.0)])
    return gpd.GeoDataFrame(
        {
            "parcel_id": [
                "at-minimum",
                "at-maximum",
                "below-minimum",
                "above-maximum",
                "invalid-geometry",
                "unknown-area",
            ],
            "geometry_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "INVALID",
                "INVALID",
            ],
            "area_m2": [2000.0, 15000.0, 1999.0, 15001.0, 5000.0, None],
            "commune_code": ["31395"] * 6,
        },
        geometry=[geometry] * 6,
        crs="EPSG:4326",
    )


def test_minimum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert "at-minimum" in set(candidates["parcel_id"])


def test_maximum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert "at-maximum" in set(candidates["parcel_id"])


@pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("below-minimum", "AREA_BELOW_MIN"),
        ("above-maximum", "AREA_ABOVE_MAX"),
        ("invalid-geometry", "INVALID_GEOMETRY"),
        ("unknown-area", "INVALID_GEOMETRY"),
    ],
)
def test_rejected_parcel_has_expected_reason(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_area(parcels, area_config)

    row = rejected.loc[rejected["parcel_id"] == parcel_id].iloc[0]
    assert row["rejection_reason"] == expected_reason


def test_no_parcel_disappears(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    assert len(parcels) == len(candidates) + len(rejected)
    assert set(parcels["parcel_id"]) == set(candidates["parcel_id"]) | set(
        rejected["parcel_id"]
    )
    assert candidates.crs == parcels.crs
    assert rejected.crs == parcels.crs


def test_thresholds_come_from_config(parcels: gpd.GeoDataFrame) -> None:
    custom_config = ParcelConfig(min_area_m2=1999, max_area_m2=2000)

    candidates, _ = filter_parcels_by_area(parcels, custom_config)

    assert set(candidates["parcel_id"]) == {"below-minimum", "at-minimum"}


def test_missing_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    without_id = parcels.drop(columns=["parcel_id"])

    with pytest.raises(ParcelFilterError, match="parcel_id"):
        filter_parcels_by_area(without_id, area_config)


def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="null"):
        filter_parcels_by_area(with_null, area_config)


def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="unique"):
        filter_parcels_by_area(with_duplicate, area_config)


def test_candidate_and_rejected_ids_do_not_overlap(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    assert set(candidates["parcel_id"]).isdisjoint(set(rejected["parcel_id"]))


def test_exact_parcel_ids_are_preserved(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    output_ids = list(candidates["parcel_id"]) + list(rejected["parcel_id"])
    assert len(output_ids) == len(set(output_ids))
    assert set(output_ids) == set(parcels["parcel_id"])


@pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "5000", True])
def test_valid_geometry_requires_strict_positive_finite_area(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    area: object,
) -> None:
    invalid = parcels.copy()
    invalid["area_m2"] = invalid["area_m2"].astype(object)
    invalid.loc[0, "area_m2"] = area

    with pytest.raises(ParcelFilterError, match="strict positive finite numeric"):
        filter_parcels_by_area(invalid, area_config)


@pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "])
def test_area_filter_requires_exact_non_empty_parcel_ids(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: object,
) -> None:
    invalid = parcels.copy()
    invalid["parcel_id"] = invalid["parcel_id"].astype(object)
    invalid.loc[0, "parcel_id"] = parcel_id

    with pytest.raises(ParcelFilterError, match="exact non-empty strings"):
        filter_parcels_by_area(invalid, area_config)


def test_area_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    plain = pd.DataFrame(parcels)

    with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_area(plain, area_config)  # type: ignore[arg-type]


def test_area_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    duplicate = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(ParcelFilterError, match="columns.*unique"):
        filter_parcels_by_area(duplicate, area_config)


@pytest.mark.parametrize("mode", ["missing_geometry", "missing_crs", "unreadable_crs"])
def test_area_filter_rejects_malformed_spatial_envelope(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    mode: str,
) -> None:
    invalid = parcels.copy()
    if mode == "missing_geometry":
        invalid = invalid.drop(columns="geometry")
    elif mode == "missing_crs":
        invalid = invalid.set_crs(None, allow_override=True)
    else:
        invalid.geometry.array._crs = "not-a-crs"

    with pytest.raises(ParcelFilterError, match="geometry|CRS"):
        filter_parcels_by_area(invalid, area_config)
