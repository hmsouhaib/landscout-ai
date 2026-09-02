from __future__ import annotations

import io
import math
import zipfile
from collections.abc import Callable, Mapping
from contextlib import contextmanager
from dataclasses import fields, is_dataclass, replace
from hashlib import sha256
from pathlib import Path
from typing import Any, ClassVar, cast

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
import pytest
import yaml
from shapely.geometry import Point  # type: ignore[import-untyped]

from landscout import sources
from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module
from landscout.sources import inpn_protected_areas_fr as source_module
from landscout.sources.inpn_protected_areas_catalog_fr import (
    CATALOG_HASH_SCHEMA_VERSION,
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasFieldCatalog,
    InpnProtectedAreasGeoPackageCatalog,
    InpnProtectedAreasLayerCatalog,
    build_inpn_protected_areas_catalog,
    validate_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)

CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
EXPECTED_EXPORTS = {
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
    "InpnProtectedAreasLayerCatalog",
    "build_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_catalog",
}


class _Response(io.BytesIO):
    headers: ClassVar[dict[str, str]] = {"Content-Type": "application/zip"}


@contextmanager
def _response(payload: bytes) -> Any:
    response = _Response(payload)
    try:
        yield response
    finally:
        response.close()


def _spatial_frame(
    *,
    field_names: tuple[str, ...] = ("beta", "alpha"),
    feature_count: int = 1,
    crs: str = "EPSG:2154",
) -> gpd.GeoDataFrame:
    data: dict[str, pd.Series[Any]] = {}
    for position, name in enumerate(field_names):
        if position % 2:
            data[name] = pd.Series(range(feature_count), dtype="int64")
        else:
            data[name] = pd.Series(
                [f"value-{index}" for index in range(feature_count)],
                dtype="object",
            )
    geometry = gpd.GeoSeries(
        [Point(1000.0 + index, 2000.0 + index) for index in range(feature_count)],
        crs=crs,
    )
    return gpd.GeoDataFrame(data, geometry=geometry, crs=crs)


def _non_spatial_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "code": pd.Series([1], dtype="int64"),
            "label": pd.Series(["one"], dtype="object"),
        }
    )


def _gpkg_bytes(
    tmp_path: Path,
    name: str,
    layers: tuple[tuple[str, pd.DataFrame], ...],
) -> bytes:
    path = tmp_path / f"build-{name}.gpkg"
    for position, (layer_name, frame) in enumerate(layers):
        pyogrio.write_dataframe(
            frame,
            path,
            layer=layer_name,
            driver="GPKG",
            append=position > 0,
        )
    return path.read_bytes()


def _zip_bytes(files: Mapping[str, bytes]) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, payload in files.items():
            info = zipfile.ZipInfo(name, date_time=(2026, 7, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, payload)
    return stream.getvalue()


def _config(tmp_path: Path, archive: bytes) -> InpnProtectedAreasSourceConfig:
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    payload["cache_root"] = str(tmp_path / "cache")
    payload["expected_archive_size_bytes"] = len(archive)
    payload["expected_archive_sha256"] = sha256(archive).hexdigest()
    return InpnProtectedAreasSourceConfig.model_validate(payload)


def _extraction(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    files: Mapping[str, bytes],
) -> tuple[InpnProtectedAreasSourceConfig, InpnProtectedAreasExtraction]:
    archive = _zip_bytes(files)
    config = _config(tmp_path, archive)

    def fake_open(*args: object, **kwargs: object) -> Any:
        return _response(archive)

    monkeypatch.setattr(source_module, "open_safe_https", fake_open)
    download = download_inpn_protected_areas_archive(config)
    return config, extract_inpn_protected_areas_archive(download, config)


def _one_package(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    frame: pd.DataFrame | None = None,
    layer_name: str = "physical_layer",
) -> tuple[InpnProtectedAreasSourceConfig, InpnProtectedAreasExtraction]:
    package = _gpkg_bytes(
        tmp_path,
        "one",
        ((layer_name, _spatial_frame() if frame is None else frame),),
    )
    return _extraction(tmp_path, monkeypatch, {"EP/one.gpkg": package})


def _patch_info(
    monkeypatch: pytest.MonkeyPatch,
    mutate: Callable[[dict[str, object]], None],
) -> None:
    original = catalog_module.pyogrio.read_info

    def patched(*args: object, **kwargs: object) -> dict[str, object]:
        result = dict(original(*args, **kwargs))
        mutate(result)
        return result

    monkeypatch.setattr(catalog_module.pyogrio, "read_info", patched)


def _catalog_with_hash(
    value: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasCatalog:
    without_hash = replace(value, complete_catalog_content_sha256="")
    return replace(
        without_hash,
        complete_catalog_content_sha256=catalog_module._catalog_content_sha256(
            without_hash
        ),
    )


def test_one_valid_geopackage_with_one_spatial_layer_is_cataloged(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    result = build_inpn_protected_areas_catalog(extraction, config)

    assert type(result) is InpnProtectedAreasCatalog
    assert result.catalog_schema_version == CATALOG_HASH_SCHEMA_VERSION == 1
    assert result.package_count == 1
    assert result.layer_count == 1
    assert result.field_count == 2
    assert result.total_feature_count == 1
    package = result.packages[0]
    assert package.relative_path == "EP/one.gpkg"
    assert package.file_size == extraction.files[0].file_size
    assert package.file_sha256 == extraction.files[0].sha256
    layer = package.layers[0]
    assert layer.layer_name == "physical_layer"
    assert layer.geometry_type_raw == "Point"
    assert layer.is_spatial is True
    assert layer.feature_count == 1
    assert layer.total_bounds == (1000.0, 2000.0, 1000.0, 2000.0)
    assert len(result.complete_catalog_content_sha256) == 64
    validate_inpn_protected_areas_catalog(extraction, config, result)


def test_package_with_multiple_layers_preserves_physical_order(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package = _gpkg_bytes(
        tmp_path,
        "multi",
        (
            ("z_first", _spatial_frame(field_names=("one",))),
            ("a_second", _spatial_frame(field_names=("two",))),
            ("table_last", _non_spatial_frame()),
        ),
    )
    config, extraction = _extraction(
        tmp_path,
        monkeypatch,
        {"EP/multi.gpkg": package},
    )

    result = build_inpn_protected_areas_catalog(extraction, config)

    assert [layer.layer_name for layer in result.packages[0].layers] == [
        "z_first",
        "a_second",
        "table_last",
    ]
    assert [layer.layer_position for layer in result.packages[0].layers] == [0, 1, 2]
    assert result.packages[0].layers[2].is_spatial is False
    assert result.packages[0].layers[2].crs_raw is None
    assert result.packages[0].layers[2].total_bounds is None


def test_multiple_geopackages_remain_in_extraction_order(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first = _gpkg_bytes(tmp_path, "a", (("layer_a", _spatial_frame()),))
    second = _gpkg_bytes(tmp_path, "z", (("layer_z", _spatial_frame()),))
    config, extraction = _extraction(
        tmp_path,
        monkeypatch,
        {"EP/z.gpkg": second, "EP/a.gpkg": first},
    )

    result = build_inpn_protected_areas_catalog(extraction, config)

    assert [item.relative_path for item in extraction.files] == [
        "EP/a.gpkg",
        "EP/z.gpkg",
    ]
    assert [item.relative_path for item in result.packages] == [
        "EP/a.gpkg",
        "EP/z.gpkg",
    ]
    assert [item.package_position for item in result.packages] == [0, 1]


def test_non_geopackage_extracted_file_is_not_silently_ignored(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package = _gpkg_bytes(tmp_path, "one", (("layer", _spatial_frame()),))
    config, extraction = _extraction(
        tmp_path,
        monkeypatch,
        {"EP/one.gpkg": package, "EP/readme.txt": b"source file"},
    )

    with pytest.raises(
        InpnProtectedAreasCatalogError, match="not a GeoPackage|ignored"
    ):
        build_inpn_protected_areas_catalog(extraction, config)


def test_zero_visible_layers_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    monkeypatch.setattr(
        catalog_module.pyogrio,
        "list_layers",
        lambda path: np.empty((0, 2), dtype=object),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="no OGR-visible layer"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_layer_name_with_edge_whitespace_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    monkeypatch.setattr(
        catalog_module.pyogrio,
        "list_layers",
        lambda path: np.array([[" physical_layer", "Point"]], dtype=object),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="layer name|exact string"):
        build_inpn_protected_areas_catalog(extraction, config)


@pytest.mark.parametrize(
    "names",
    [
        ("physical_layer", "physical_layer"),
        ("physical_layer", "PHYSICAL_LAYER"),
        ("K", "\u212a"),
    ],
    ids=["duplicate", "casefold", "nfkc"],
)
def test_duplicate_casefold_or_nfkc_layer_identity_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    names: tuple[str, str],
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    monkeypatch.setattr(
        catalog_module.pyogrio,
        "list_layers",
        lambda path: np.array([[name, "Point"] for name in names], dtype=object),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="duplicate|collision"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_file_byte_mutation_during_metadata_inspection_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    package_path = extraction.extraction_path / "EP" / "one.gpkg"
    original = catalog_module.pyogrio.read_info

    def mutate_after_read(*args: object, **kwargs: object) -> dict[str, object]:
        info = dict(original(*args, **kwargs))
        payload = package_path.read_bytes()
        package_path.write_bytes(payload[:-1] + bytes([payload[-1] ^ 1]))
        return info

    monkeypatch.setattr(catalog_module.pyogrio, "read_info", mutate_after_read)

    with pytest.raises(InpnProtectedAreasCatalogError, match="byte identity|changed"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_exact_field_and_dtype_order_is_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    result = build_inpn_protected_areas_catalog(extraction, config)

    assert result.packages[0].layers[0].fields == (
        InpnProtectedAreasFieldCatalog("beta", "object", 0),
        InpnProtectedAreasFieldCatalog("alpha", "int64", 1),
    )


def test_field_and_dtype_length_mismatch_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(monkeypatch, lambda info: info.__setitem__("dtypes", ["object"]))

    with pytest.raises(InpnProtectedAreasCatalogError, match="lengths differ"):
        build_inpn_protected_areas_catalog(extraction, config)


@pytest.mark.parametrize("name", ["", " beta", "beta "])
def test_empty_or_edge_whitespace_field_name_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    name: str,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    def mutate(info: dict[str, object]) -> None:
        info["fields"] = [name, "alpha"]

    _patch_info(monkeypatch, mutate)

    with pytest.raises(InpnProtectedAreasCatalogError, match="field name|exact string"):
        build_inpn_protected_areas_catalog(extraction, config)


@pytest.mark.parametrize(
    "names",
    [("beta", "beta"), ("beta", "BETA"), ("K", "\u212a")],
    ids=["duplicate", "casefold", "nfkc"],
)
def test_duplicate_casefold_or_nfkc_field_identity_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    names: tuple[str, str],
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    def mutate(info: dict[str, object]) -> None:
        info["fields"] = list(names)

    _patch_info(monkeypatch, mutate)

    with pytest.raises(InpnProtectedAreasCatalogError, match="duplicate|collision"):
        build_inpn_protected_areas_catalog(extraction, config)


@pytest.mark.parametrize("dtype", [None, "", " object"])
def test_malformed_source_dtype_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    dtype: object,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    def mutate(info: dict[str, object]) -> None:
        info["dtypes"] = [dtype, "int64"]

    _patch_info(monkeypatch, mutate)

    with pytest.raises(InpnProtectedAreasCatalogError, match="dtype|exact string"):
        build_inpn_protected_areas_catalog(extraction, config)


@pytest.mark.parametrize("feature_count", [0, 1])
def test_exact_non_negative_feature_count_is_accepted(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    feature_count: int,
) -> None:
    config, extraction = _one_package(
        tmp_path,
        monkeypatch,
        frame=_spatial_frame(feature_count=feature_count),
    )

    result = build_inpn_protected_areas_catalog(extraction, config)

    assert result.packages[0].layers[0].feature_count == feature_count


@pytest.mark.parametrize("feature_count", [True, -1])
def test_boolean_or_negative_feature_count_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    feature_count: object,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(
        monkeypatch,
        lambda info: info.__setitem__("features", feature_count),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="feature count"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_populated_spatial_layer_without_crs_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(monkeypatch, lambda info: info.__setitem__("crs", None))

    with pytest.raises(InpnProtectedAreasCatalogError, match="CRS"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_unparseable_crs_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(monkeypatch, lambda info: info.__setitem__("crs", "not-a-crs"))

    with pytest.raises(InpnProtectedAreasCatalogError, match="CRS.*parseable"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_valid_crs_authority_and_canonical_wkt_are_recorded(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    layer = build_inpn_protected_areas_catalog(extraction, config).packages[0].layers[0]

    assert layer.crs_raw == "EPSG:2154"
    assert layer.crs_authority_name == "EPSG"
    assert layer.crs_authority_code == "2154"
    assert layer.crs_wkt is not None and layer.crs_wkt.startswith("PROJCRS[")


def test_finite_ordered_bounds_are_accepted(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(
        monkeypatch,
        lambda info: info.__setitem__("total_bounds", (1, 2, 3, 4)),
    )

    layer = build_inpn_protected_areas_catalog(extraction, config).packages[0].layers[0]

    assert layer.total_bounds == (1.0, 2.0, 3.0, 4.0)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_populated_bounds_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    value: float,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(
        monkeypatch,
        lambda info: info.__setitem__("total_bounds", (0.0, 0.0, value, 1.0)),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="bounds"):
        build_inpn_protected_areas_catalog(extraction, config)


@pytest.mark.parametrize(
    "bounds",
    [(2.0, 0.0, 1.0, 1.0), (0.0, 2.0, 1.0, 1.0)],
    ids=["x", "y"],
)
def test_reversed_bounds_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    bounds: tuple[float, float, float, float],
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(
        monkeypatch,
        lambda info: info.__setitem__("total_bounds", bounds),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="reversed"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_empty_spatial_layer_normalizes_all_nan_bounds_to_null(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(
        tmp_path,
        monkeypatch,
        frame=_spatial_frame(feature_count=0),
    )
    _patch_info(
        monkeypatch,
        lambda info: info.__setitem__(
            "total_bounds",
            (float("nan"),) * 4,
        ),
    )

    layer = build_inpn_protected_areas_catalog(extraction, config).packages[0].layers[0]

    assert layer.feature_count == 0
    assert layer.total_bounds is None


@pytest.mark.parametrize("violation", ["crs", "bounds"])
def test_non_spatial_layer_with_crs_or_bounds_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    violation: str,
) -> None:
    config, extraction = _one_package(
        tmp_path,
        monkeypatch,
        frame=_non_spatial_frame(),
    )

    def mutate(info: dict[str, object]) -> None:
        info[violation if violation == "crs" else "total_bounds"] = (
            "EPSG:2154" if violation == "crs" else (0.0, 0.0, 1.0, 1.0)
        )

    _patch_info(monkeypatch, mutate)

    with pytest.raises(InpnProtectedAreasCatalogError, match="non-spatial"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_package_layer_field_ordering_produces_deterministic_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first = _gpkg_bytes(
        tmp_path,
        "a",
        (("z_layer", _spatial_frame(field_names=("b", "a"))),),
    )
    second = _gpkg_bytes(
        tmp_path,
        "b",
        (("a_layer", _spatial_frame(field_names=("d", "c"))),),
    )
    config, extraction = _extraction(
        tmp_path,
        monkeypatch,
        {"EP/z.gpkg": second, "EP/a.gpkg": first},
    )

    first_result = build_inpn_protected_areas_catalog(extraction, config)
    second_result = build_inpn_protected_areas_catalog(extraction, config)

    assert first_result == second_result
    assert (
        first_result.complete_catalog_content_sha256
        == second_result.complete_catalog_content_sha256
    )


def test_caller_package_reordering_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first = _gpkg_bytes(tmp_path, "a", (("a", _spatial_frame()),))
    second = _gpkg_bytes(tmp_path, "z", (("z", _spatial_frame()),))
    config, extraction = _extraction(
        tmp_path,
        monkeypatch,
        {"EP/a.gpkg": first, "EP/z.gpkg": second},
    )
    original = build_inpn_protected_areas_catalog(extraction, config)
    reordered = tuple(
        replace(package, package_position=position)
        for position, package in enumerate(reversed(original.packages))
    )
    forged = _catalog_with_hash(replace(original, packages=reordered))

    with pytest.raises(InpnProtectedAreasCatalogError, match="order|rebuilt"):
        validate_inpn_protected_areas_catalog(extraction, config, forged)


def test_coordinated_metadata_and_hash_mutation_is_rejected_by_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    original = build_inpn_protected_areas_catalog(extraction, config)
    layer = original.packages[0].layers[0]
    mutated_fields = (
        replace(layer.fields[0], name="forged"),
        *layer.fields[1:],
    )
    mutated_layer = replace(layer, fields=mutated_fields)
    mutated_package = replace(original.packages[0], layers=(mutated_layer,))
    forged = _catalog_with_hash(replace(original, packages=(mutated_package,)))

    with pytest.raises(InpnProtectedAreasCatalogError, match="rebuilt"):
        validate_inpn_protected_areas_catalog(extraction, config, forged)


def test_absolute_extraction_path_does_not_affect_portable_catalog_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package = _gpkg_bytes(tmp_path, "portable", (("layer", _spatial_frame()),))
    config_a, extraction_a = _extraction(
        tmp_path / "a",
        monkeypatch,
        {"EP/one.gpkg": package},
    )
    config_b, extraction_b = _extraction(
        tmp_path / "b",
        monkeypatch,
        {"EP/one.gpkg": package},
    )

    result_a = build_inpn_protected_areas_catalog(extraction_a, config_a)
    result_b = build_inpn_protected_areas_catalog(extraction_b, config_b)

    assert extraction_a.extraction_path != extraction_b.extraction_path
    assert result_a == result_b
    assert (
        result_a.complete_catalog_content_sha256
        == result_b.complete_catalog_content_sha256
    )


def test_cache_hit_values_do_not_affect_portable_catalog_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    first = build_inpn_protected_areas_catalog(extraction, config)
    changed_cache_state = replace(
        extraction,
        download=replace(
            extraction.download,
            cache_hit=not extraction.download.cache_hit,
        ),
        cache_hit=not extraction.cache_hit,
    )

    second = build_inpn_protected_areas_catalog(changed_cache_state, config)

    assert first == second
    assert (
        first.complete_catalog_content_sha256 == second.complete_catalog_content_sha256
    )


@pytest.mark.parametrize("mutation", ["schema", "feature_count", "crs", "bounds"])
def test_catalog_validation_detects_changed_physical_metadata(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    original = build_inpn_protected_areas_catalog(extraction, config)

    def mutate(info: dict[str, object]) -> None:
        if mutation == "schema":
            info["fields"] = ["beta", "alpha", "added"]
            info["dtypes"] = ["object", "int64", "object"]
        elif mutation == "feature_count":
            info["features"] = 2
        elif mutation == "crs":
            info["crs"] = "EPSG:4326"
        else:
            info["total_bounds"] = (0.0, 0.0, 1.0, 1.0)

    _patch_info(monkeypatch, mutate)

    with pytest.raises(InpnProtectedAreasCatalogError, match="rebuilt"):
        validate_inpn_protected_areas_catalog(extraction, config, original)


def test_catalog_validator_rejects_wrong_runtime_type(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    with pytest.raises(InpnProtectedAreasCatalogError, match="exact"):
        validate_inpn_protected_areas_catalog(
            extraction,
            config,
            object(),  # type: ignore[arg-type]
        )


def test_catalog_construction_never_materializes_feature_rows(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)

    def forbidden(*args: object, **kwargs: object) -> Any:
        raise AssertionError("feature-row reader was called")

    monkeypatch.setattr(catalog_module.pyogrio, "read_dataframe", forbidden)
    monkeypatch.setattr(gpd, "read_file", forbidden)

    result = build_inpn_protected_areas_catalog(extraction, config)

    assert result.package_count == 1

    def assert_no_feature_rows(value: object) -> None:
        assert not isinstance(value, (pd.DataFrame, gpd.GeoDataFrame))
        if is_dataclass(value) and not isinstance(value, type):
            for field in fields(value):
                assert_no_feature_rows(getattr(value, field.name))
        elif isinstance(value, tuple):
            for member in value:
                assert_no_feature_rows(member)

    assert_no_feature_rows(result)


def test_catalog_models_are_exact_factual_metadata_only() -> None:
    assert [field.name for field in fields(InpnProtectedAreasFieldCatalog)] == [
        "name",
        "source_dtype",
        "position",
    ]
    assert [field.name for field in fields(InpnProtectedAreasLayerCatalog)] == [
        "layer_name",
        "layer_position",
        "feature_count",
        "geometry_type_raw",
        "is_spatial",
        "crs_raw",
        "crs_authority_name",
        "crs_authority_code",
        "crs_wkt",
        "total_bounds",
        "fields",
    ]
    assert [field.name for field in fields(InpnProtectedAreasGeoPackageCatalog)] == [
        "relative_path",
        "file_size",
        "file_sha256",
        "package_position",
        "layers",
    ]
    forbidden = {
        "category",
        "natura",
        "znieff",
        "parcel",
        "intersection",
        "exclusion",
        "score",
    }
    names = {
        field.name
        for model in (
            InpnProtectedAreasFieldCatalog,
            InpnProtectedAreasLayerCatalog,
            InpnProtectedAreasGeoPackageCatalog,
            InpnProtectedAreasCatalog,
        )
        for field in fields(model)
    }
    assert not names.intersection(forbidden)


def test_public_api_exports_only_trusted_catalog_symbols() -> None:
    assert set(catalog_module.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(
        getattr(sources, name) is getattr(catalog_module, name)
        for name in EXPECTED_EXPORTS
    )
    assert not hasattr(sources, "_inspect_package")
    assert not hasattr(sources, "_catalog_content_sha256")


def test_metadata_calls_use_exact_forced_metadata_only_api(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    original_list = catalog_module.pyogrio.list_layers
    original_info = catalog_module.pyogrio.read_info
    calls: list[tuple[str, dict[str, object]]] = []

    def listed(*args: object, **kwargs: object) -> object:
        calls.append(("list_layers", dict(kwargs)))
        return original_list(*args, **kwargs)

    def informed(*args: object, **kwargs: object) -> object:
        calls.append(("read_info", dict(kwargs)))
        return original_info(*args, **kwargs)

    monkeypatch.setattr(catalog_module.pyogrio, "list_layers", listed)
    monkeypatch.setattr(catalog_module.pyogrio, "read_info", informed)

    build_inpn_protected_areas_catalog(extraction, config)

    assert calls == [
        ("list_layers", {}),
        (
            "read_info",
            {
                "layer": "physical_layer",
                "force_feature_count": True,
                "force_total_bounds": True,
            },
        ),
    ]


def test_empty_spatial_layer_with_partially_missing_bounds_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(
        tmp_path,
        monkeypatch,
        frame=_spatial_frame(feature_count=0),
    )
    _patch_info(
        monkeypatch,
        lambda info: info.__setitem__(
            "total_bounds",
            (float("nan"), float("nan"), 1.0, float("nan")),
        ),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="partially missing"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_layer_enumeration_and_read_info_geometry_must_agree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(
        monkeypatch,
        lambda info: info.__setitem__("geometry_type", "MultiPolygon"),
    )

    with pytest.raises(InpnProtectedAreasCatalogError, match="geometry types differ"):
        build_inpn_protected_areas_catalog(extraction, config)


@pytest.mark.parametrize("value", [True, 1.5, "1", None])
def test_feature_count_rejects_non_exact_integers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    value: object,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    _patch_info(monkeypatch, lambda info: info.__setitem__("features", value))

    with pytest.raises(InpnProtectedAreasCatalogError, match="feature count"):
        build_inpn_protected_areas_catalog(extraction, config)


def test_catalog_hash_excludes_absolute_paths_and_cache_state(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction = _one_package(tmp_path, monkeypatch)
    result = build_inpn_protected_areas_catalog(extraction, config)
    payload = catalog_module._catalog_payload(result)

    encoded = repr(payload).casefold()
    assert str(extraction.extraction_path).casefold() not in encoded
    assert str(extraction.download.path).casefold() not in encoded
    assert "cache_hit" not in payload
    assert "download_timestamp" not in payload
    assert math.isfinite(cast(float, result.packages[0].layers[0].total_bounds[0]))
