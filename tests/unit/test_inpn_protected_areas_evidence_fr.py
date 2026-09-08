from __future__ import annotations

import ast
import inspect
import io
import json
import sqlite3
import struct
import zipfile
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import (
    FrozenInstanceError,
    dataclass,
    fields,
    is_dataclass,
    replace,
)
from hashlib import sha256
from pathlib import Path
from typing import Any, ClassVar

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
import pytest
import shapely  # type: ignore[import-untyped]
import yaml
from shapely.geometry import Point  # type: ignore[import-untyped]

from landscout import sources
from landscout.sources import inpn_protected_areas_attributes_fr as attribute_module
from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module
from landscout.sources import inpn_protected_areas_evidence_fr as evidence
from landscout.sources import inpn_protected_areas_fr as source_module
from landscout.sources import inpn_protected_areas_geometry_fr as geometry_module
from landscout.sources.inpn_protected_areas_attributes_fr import (
    InpnProtectedAreasAttributeProfile,
    InpnProtectedAreasAttributeProfileError,
    build_inpn_protected_areas_attribute_profile,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_evidence_fr import (
    InpnProtectedAreasEvidenceBundle,
    InpnProtectedAreasEvidenceError,
    InpnProtectedAreasLayerAlignment,
    build_inpn_protected_areas_evidence_bundle,
    validate_inpn_protected_areas_evidence_bundle,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)
from landscout.sources.inpn_protected_areas_geometry_fr import (
    InpnProtectedAreasGeometryProfile,
    InpnProtectedAreasGeometryProfileError,
    build_inpn_protected_areas_geometry_profile,
)

CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
EXPECTED_EXPORTS = {
    "InpnProtectedAreasEvidenceBundle",
    "InpnProtectedAreasEvidenceError",
    "InpnProtectedAreasLayerAlignment",
    "build_inpn_protected_areas_evidence_bundle",
    "validate_inpn_protected_areas_evidence_bundle",
}
ALIGNMENT_FIELDS = (
    "relative_path",
    "package_position",
    "file_sha256",
    "layer_name",
    "layer_position",
    "feature_count",
    "fid_count",
    "fid_min",
    "fid_max",
    "fid_sequence_sha256",
)
SOURCE_MUTATIONS = (
    ("provider", "other provider"),
    ("authority", "other authority"),
    ("program", "other program"),
    ("dataset_id", "other dataset"),
    ("dataset_name", "other name"),
    ("declared_version", "08/2026"),
    ("reference_page_url", "https://example.test/reference"),
    ("archive_url", "https://example.test/EP.zip"),
    ("archive_filename", "other.zip"),
    ("archive_size", 1),
    ("archive_sha256", "0" * 64),
    ("source_catalog_schema_version", 1),
    ("source_catalog_content_sha256", "0" * 64),
)


class _Response(io.BytesIO):
    headers: ClassVar[dict[str, str]] = {"Content-Type": "application/zip"}


class _StringSubclass(str):
    pass


@dataclass(frozen=True)
class _Source:
    extraction: InpnProtectedAreasExtraction
    config: InpnProtectedAreasSourceConfig
    catalog: InpnProtectedAreasCatalog
    attributes: InpnProtectedAreasAttributeProfile
    geometries: InpnProtectedAreasGeometryProfile


@contextmanager
def _response(payload: bytes) -> Iterator[_Response]:
    with _Response(payload) as response:
        yield response


def _json_hash(payload: object) -> str:
    return sha256(
        json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _point_blob(position: int, layout: str) -> bytes:
    """Fixture-only independent Standard GPB plus ISO dimensional Point WKB."""
    coordinates = (1000.0 + position, 2000.0 + position)
    if "Z" in layout:
        coordinates += (3.0,)
    if "M" in layout:
        coordinates += (4.0,)
    type_word = 1 + 1000 * int("Z" in layout) + 2000 * int("M" in layout)
    return (
        b"GP\x00\x01"
        + struct.pack("<i", 2154)
        + struct.pack(f"<BI{len(coordinates)}d", 1, type_word, *coordinates)
    )


def _package(
    tmp_path: Path,
    layers: tuple[tuple[str, tuple[int, ...]], ...] = (("first", (1, 2, 4)),),
    *,
    layout: str = "XY",
) -> bytes:
    """Write only an ordinary XY container; SQLite installs exact FIDs/raw BLOBs."""
    tmp_path.mkdir(parents=True, exist_ok=True)
    path = tmp_path / "fixture.gpkg"
    seed = gpd.GeoDataFrame(
        {"id_mnhn": ["not-the-physical-fid"], "value": ["évidence"]},
        geometry=[Point(1000, 2000)],
        crs="EPSG:2154",
    )
    for position, (name, _) in enumerate(layers):
        pyogrio.write_dataframe(
            seed,
            path,
            layer=name,
            driver="GPKG",
            append=position > 0,
            geometry_type="Unknown",
            layer_options={"SPATIAL_INDEX": "NO"},
        )
    connection = sqlite3.connect(":memory:")
    try:
        connection.deserialize(path.read_bytes())
        for name, fids in layers:
            quoted = '"' + name.replace('"', '""') + '"'
            connection.execute(f"DELETE FROM {quoted}")
            connection.executemany(
                f"INSERT INTO {quoted} (fid, geom, id_mnhn, value) VALUES (?, ?, ?, ?)",
                [
                    (
                        fid,
                        _point_blob(position, layout),
                        "same-business-id",
                        f"évidence-{fid}",
                    )
                    for position, fid in enumerate(fids)
                ],
            )
            connection.execute(
                "UPDATE gpkg_geometry_columns SET z=2,m=2 WHERE table_name=?", (name,)
            )
            if not fids:
                connection.execute(
                    "UPDATE gpkg_contents SET min_x=NULL,min_y=NULL,max_x=NULL,max_y=NULL WHERE table_name=?",
                    (name,),
                )
        connection.commit()
        return connection.serialize()
    finally:
        connection.close()


def _source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    files: Mapping[str, bytes] | None = None,
    layers: tuple[tuple[str, tuple[int, ...]], ...] = (("first", (1, 2, 4)),),
    layout: str = "XY",
) -> _Source:
    members = (
        files
        if files is not None
        else {"EP/one.gpkg": _package(tmp_path / "p", layers, layout=layout)}
    )
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, value in members.items():
            archive.writestr(zipfile.ZipInfo(name, (2026, 7, 1, 0, 0, 0)), value)
    archive_bytes = stream.getvalue()
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    payload.update(
        cache_root=str(tmp_path / "c"),
        expected_archive_size_bytes=len(archive_bytes),
        expected_archive_sha256=sha256(archive_bytes).hexdigest(),
    )
    config = InpnProtectedAreasSourceConfig.model_validate(payload)
    monkeypatch.setattr(
        source_module, "open_safe_https", lambda *a, **k: _response(archive_bytes)
    )
    download = download_inpn_protected_areas_archive(config)
    extraction = extract_inpn_protected_areas_archive(download, config)
    catalog = build_inpn_protected_areas_catalog(extraction, config)
    attributes = build_inpn_protected_areas_attribute_profile(
        extraction, config, catalog
    )
    geometries = build_inpn_protected_areas_geometry_profile(
        extraction, config, catalog
    )
    return _Source(extraction, config, catalog, attributes, geometries)


@pytest.fixture
def source(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> _Source:
    return _source(tmp_path, monkeypatch)


def _build(source: _Source) -> InpnProtectedAreasEvidenceBundle:
    return build_inpn_protected_areas_evidence_bundle(
        source.extraction,
        source.config,
        source.catalog,
        source.attributes,
        source.geometries,
    )


def _rehash_profile(profile: Any, **changes: object) -> Any:
    """Pure adversarial mutation: recalculate the owning upstream hash, not trust."""
    value = replace(profile, **changes)
    if type(value) is InpnProtectedAreasAttributeProfile:
        return replace(
            value,
            complete_attribute_profile_content_sha256=attribute_module._profile_content_sha256(
                value
            ),
        )
    return replace(
        value,
        complete_geometry_profile_content_sha256=geometry_module._profile_content_sha256(
            value
        ),
    )


def _profile_layers(profile: Any, layers: tuple[Any, ...]) -> Any:
    """Coherently close aggregate counts for pure layer-inventory contradictions."""
    counts = {
        "package_count": len({item.package_position for item in layers}),
        "layer_count": len(layers),
    }
    if type(profile) is InpnProtectedAreasAttributeProfile:
        counts.update(
            field_definition_count=sum(len(item.fields) for item in layers),
            total_row_count=sum(item.feature_count for item in layers),
            total_null_count=sum(
                field.null_count for item in layers for field in item.fields
            ),
            total_distinct_non_null_value_count=sum(
                field.distinct_non_null_count
                for item in layers
                for field in item.fields
            ),
        )
    else:
        names = (
            "null_geometry_count",
            "empty_geometry_count",
            "non_empty_geometry_count",
            "valid_non_empty_geometry_count",
            "invalid_non_empty_geometry_count",
            "has_z_geometry_count",
            "has_m_geometry_count",
            "total_coordinate_count",
        )
        counts.update(
            {name: sum(getattr(item, name) for item in layers) for name in names}
        )
        counts["geometry_row_count"] = sum(item.feature_count for item in layers)
    return _rehash_profile(profile, layers=layers, **counts)


def _expected_payload(bundle: InpnProtectedAreasEvidenceBundle) -> dict[str, object]:
    """Independent specification of the compact bundle payload, never domains."""
    return {
        "evidence_bundle_schema_version": bundle.evidence_bundle_schema_version,
        "catalog": {
            "catalog_schema_version": bundle.catalog.catalog_schema_version,
            "complete_catalog_content_sha256": bundle.catalog.complete_catalog_content_sha256,
        },
        "attributes": {
            "attribute_profile_schema_version": bundle.attributes.attribute_profile_schema_version,
            "complete_attribute_profile_content_sha256": bundle.attributes.complete_attribute_profile_content_sha256,
        },
        "geometries": {
            "geometry_profile_schema_version": bundle.geometries.geometry_profile_schema_version,
            "complete_geometry_profile_content_sha256": bundle.geometries.complete_geometry_profile_content_sha256,
        },
        "layer_alignments": [
            {name: getattr(item, name) for name in ALIGNMENT_FIELDS}
            for item in bundle.layer_alignments
        ],
    }


def _rehash_bundle(
    bundle: InpnProtectedAreasEvidenceBundle, **changes: object
) -> InpnProtectedAreasEvidenceBundle:
    changed = replace(bundle, **changes)
    return replace(
        changed,
        complete_evidence_bundle_content_sha256=_json_hash(_expected_payload(changed)),
    )


def _subclass(value: Any) -> Any:
    cls = type(f"NonExact{type(value).__name__}", (type(value),), {})
    if isinstance(value, InpnProtectedAreasSourceConfig):
        return cls.model_validate(value.model_dump(mode="python"))
    return cls(**{field.name: getattr(value, field.name) for field in fields(value)})


def test_complete_bundle_is_deterministic_and_independently_validated(
    source: _Source,
) -> None:
    first = _build(source)
    assert _build(source) == first
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, first
    )
    assert type(first) is InpnProtectedAreasEvidenceBundle
    assert (
        first.evidence_bundle_schema_version
        == evidence.EVIDENCE_BUNDLE_SCHEMA_VERSION
        == 1
    )
    assert (first.catalog, first.attributes, first.geometries) == (
        source.catalog,
        source.attributes,
        source.geometries,
    )
    assert len(first.layer_alignments) == 1
    alignment = first.layer_alignments[0]
    assert type(alignment) is InpnProtectedAreasLayerAlignment
    assert alignment == InpnProtectedAreasLayerAlignment(
        "EP/one.gpkg",
        0,
        source.catalog.packages[0].file_sha256,
        "first",
        0,
        3,
        3,
        1,
        4,
        _json_hash([1, 2, 4]),
    )
    assert evidence._bundle_payload(first) == _expected_payload(first)
    assert first.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(first)
    )
    assert set(_expected_payload(first)["attributes"]) == {
        "attribute_profile_schema_version",
        "complete_attribute_profile_content_sha256",
    }


@pytest.mark.parametrize(
    "argument", ["extraction", "config", "catalog", "attributes", "geometries"]
)
@pytest.mark.parametrize("kind", ["object", "subclass"])
def test_builder_requires_exact_public_input_types(
    source: _Source, argument: str, kind: str
) -> None:
    inputs = {field.name: getattr(source, field.name) for field in fields(source)}
    inputs[argument] = object() if kind == "object" else _subclass(inputs[argument])
    with pytest.raises(InpnProtectedAreasEvidenceError):
        build_inpn_protected_areas_evidence_bundle(**inputs)


@pytest.mark.parametrize("argument", ["extraction", "config", "bundle"])
@pytest.mark.parametrize("kind", ["object", "subclass"])
def test_validator_requires_exact_public_input_types(
    source: _Source, argument: str, kind: str
) -> None:
    inputs = {
        "extraction": source.extraction,
        "config": source.config,
        "bundle": _build(source),
    }
    inputs[argument] = object() if kind == "object" else _subclass(inputs[argument])
    with pytest.raises(InpnProtectedAreasEvidenceError):
        validate_inpn_protected_areas_evidence_bundle(**inputs)


@pytest.mark.parametrize("boundary", ["builder", "validator"])
def test_public_boundaries_reconstruct_same_type_config_before_physical_validation(
    source: _Source, monkeypatch: pytest.MonkeyPatch, boundary: str
) -> None:
    bundle = _build(source)
    forged_config = source.config.model_copy(
        update={"expected_archive_size_bytes": True}
    )
    assert type(forged_config) is InpnProtectedAreasSourceConfig
    calls: list[str] = []
    original = evidence.validate_inpn_protected_areas_attribute_profile

    def observed(*args: object, **kwargs: object) -> None:
        calls.append("attributes")
        original(*args, **kwargs)

    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_attribute_profile", observed
    )
    with pytest.raises(InpnProtectedAreasEvidenceError, match="config is invalid"):
        if boundary == "builder":
            _build(replace(source, config=forged_config))
        else:
            validate_inpn_protected_areas_evidence_bundle(
                source.extraction, forged_config, bundle
            )
    assert calls == []


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize(("field_name", "value"), SOURCE_MUTATIONS)
def test_pure_alignment_rejects_source_archive_catalog_identity_mismatches(
    source: _Source, owner: str, field_name: str, value: object
) -> None:
    """Structural-only contradictory profiles; this is not physical source proof."""
    changed = replace(
        source,
        **{owner: _rehash_profile(getattr(source, owner), **{field_name: value})},
    )
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "reordered"])
def test_pure_alignment_rejects_layer_inventory_changes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, owner: str, mutation: str
) -> None:
    """Pure inventory combinations are impossible together on one trusted source."""
    source = _source(
        tmp_path, monkeypatch, layers=(("z_first", (1, 2, 4)), ("a_second", (8, 9)))
    )
    profile = getattr(source, owner)
    layers = profile.layers
    if mutation == "missing":
        layers = layers[:1]
    elif mutation == "extra":
        layers += (replace(layers[0], layer_name="extra", layer_position=2),)
    elif mutation == "duplicate":
        layers = (layers[0], replace(layers[0], layer_position=1))
    else:
        layers = tuple(
            replace(layer, layer_position=position)
            for position, layer in enumerate(reversed(layers))
        )
    changed = replace(source, **{owner: _profile_layers(profile, layers)})
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", "EP/other.gpkg"),
        ("file_size", 1),
        ("file_sha256", "0" * 64),
        ("package_position", 1),
        ("driver_name", "SQLite"),
        ("layer_name", "other"),
        ("layer_position", 1),
        ("feature_count", 4),
        ("fid_count", 4),
        ("fid_min", -1),
        ("fid_max", 5),
        ("fid_sequence_sha256", "0" * 64),
    ],
)
def test_pure_alignment_rejects_package_layer_and_fid_contradictions(
    source: _Source, owner: str, field_name: str, value: object
) -> None:
    """Coherently rehashed input contradictions exercise only the cheap helper."""
    profile = getattr(source, owner)
    layer = replace(profile.layers[0], **{field_name: value})
    changed = replace(source, **{owner: _rehash_profile(profile, layers=(layer,))})
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize("field_name", ["package_count", "layer_count"])
def test_pure_alignment_retains_upstream_aggregate_contracts(
    source: _Source, owner: str, field_name: str
) -> None:
    changed = replace(
        source, **{owner: _rehash_profile(getattr(source, owner), **{field_name: 2})}
    )
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


def test_pure_alignment_equal_counts_and_extrema_do_not_hide_different_fids(
    source: _Source,
) -> None:
    """[1,2,4] and [1,3,4] cannot be one physical pair despite equal ranges."""
    geometry_layer = replace(
        source.geometries.layers[0], fid_sequence_sha256=_json_hash([1, 3, 4])
    )
    changed = _rehash_profile(source.geometries, layers=(geometry_layer,))
    assert geometry_module._validate_profile_intrinsic(changed) is changed
    attribute_layer = source.attributes.layers[0]
    assert (
        (attribute_layer.fid_count, attribute_layer.fid_min, attribute_layer.fid_max)
        == (geometry_layer.fid_count, geometry_layer.fid_min, geometry_layer.fid_max)
        == (3, 1, 4)
    )
    assert attribute_layer.fid_sequence_sha256 == _json_hash([1, 2, 4])
    with pytest.raises(InpnProtectedAreasEvidenceError, match="FID|fid"):
        evidence._align_layers(source.catalog, source.attributes, changed)


@pytest.mark.parametrize("fids", [(), (-7, 4, 99), (23,)])
def test_empty_negative_and_sparse_fids_align_without_renumbering(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, fids: tuple[int, ...]
) -> None:
    source = _source(tmp_path, monkeypatch, layers=(("first", fids),))
    bundle = _build(source)
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    record = bundle.layer_alignments[0]
    assert record.fid_count == record.feature_count == len(fids)
    assert record.fid_min == (min(fids) if fids else None)
    assert record.fid_max == (max(fids) if fids else None)
    assert (
        record.fid_sequence_sha256
        == source.attributes.layers[0].fid_sequence_sha256
        == source.geometries.layers[0].fid_sequence_sha256
        == _json_hash(sorted(fids))
    )


def test_full_package_layer_key_handles_identical_names_in_distinct_packages(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _package(tmp_path / "a", (("shared", (1, 2, 4)), ("second", (8, 9))))
    other = _package(tmp_path / "b", (("shared", (17, 41)),))
    source = _source(
        tmp_path / "s", monkeypatch, files={"EP/b.gpkg": other, "EP/a.gpkg": first}
    )
    bundle = _build(source)
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert [
        (
            item.relative_path,
            item.layer_name,
            item.package_position,
            item.layer_position,
            item.fid_count,
        )
        for item in bundle.layer_alignments
    ] == [
        ("EP/a.gpkg", "shared", 0, 0, 3),
        ("EP/a.gpkg", "second", 0, 1, 2),
        ("EP/b.gpkg", "shared", 1, 0, 2),
    ]
    assert (
        bundle.layer_alignments[0].fid_sequence_sha256
        != bundle.layer_alignments[2].fid_sequence_sha256
    )


def test_same_physical_rows_in_reversed_attribute_read_order_still_align(
    source: _Source, monkeypatch: pytest.MonkeyPatch
) -> None:
    original = pyogrio.read_dataframe
    seen: list[tuple[int, ...]] = []

    def reversed_rows(*args: object, **kwargs: object) -> object:
        assert kwargs["read_geometry"] is False
        frame = original(*args, **kwargs)
        reverse = frame.iloc[::-1]
        seen.append(tuple(reverse.index.tolist()))
        return reverse

    monkeypatch.setattr(pyogrio, "read_dataframe", reversed_rows)
    rebuilt = build_inpn_protected_areas_attribute_profile(
        source.extraction, source.config, source.catalog
    )
    assert rebuilt == source.attributes
    bundle = _build(replace(source, attributes=rebuilt))
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert seen and all(item == (4, 2, 1) for item in seen)
    assert bundle.layer_alignments[0].fid_sequence_sha256 == _json_hash([1, 2, 4])


@pytest.mark.parametrize("layout", ["M", "ZM"])
def test_measured_profiles_bundle_through_only_approved_readers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, layout: str
) -> None:
    source = _source(tmp_path, monkeypatch, layers=(("first", (8, 21)),), layout=layout)
    original_read = pyogrio.read_dataframe
    original_parse = geometry_module._parse_gpkg_geometry_blob
    read_calls: list[dict[str, object]] = []
    coordinates: list[list[list[float]]] = []

    def attribute_read(*args: object, **kwargs: object) -> object:
        assert type(args[0]) is bytes
        assert kwargs == {
            "layer": "first",
            "columns": ["id_mnhn", "value"],
            "read_geometry": False,
            "fid_as_index": True,
            "use_arrow": False,
            "datetime_as_string": True,
        }
        read_calls.append(kwargs)
        return original_read(*args, **kwargs)

    def geometry_parse(*args: object, **kwargs: object) -> Any:
        result = original_parse(*args, **kwargs)
        assert bool(shapely.has_m(result.geometry)) is True
        assert bool(shapely.has_z(result.geometry)) is (layout == "ZM")
        coordinates.append(
            shapely.get_coordinates(
                result.geometry, include_z=layout == "ZM", include_m=True
            ).tolist()
        )
        return result

    monkeypatch.setattr(pyogrio, "read_dataframe", attribute_read)
    monkeypatch.setattr(geometry_module, "_parse_gpkg_geometry_blob", geometry_parse)
    bundle = _build(source)
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert bundle.geometries == source.geometries
    assert bundle.geometries.has_m_geometry_count == 2
    assert bundle.geometries.has_z_geometry_count == (2 if layout == "ZM" else 0)
    assert len(read_calls) == 2
    expected = [
        [[1000.0 + index, 2000.0 + index, *([3.0] if layout == "ZM" else []), 4.0]]
        for index in range(2)
    ]
    assert coordinates == expected * 2


def test_portable_bundle_ignores_cache_roots_and_cache_hit_flags(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = _package(tmp_path / "p")
    first_source = _source(tmp_path / "a", monkeypatch, files={"EP/one.gpkg": package})
    second_source = _source(tmp_path / "b", monkeypatch, files={"EP/one.gpkg": package})
    first = _build(first_source)
    assert _build(second_source) == first
    cached = replace(
        second_source.extraction,
        cache_hit=True,
        download=replace(second_source.extraction.download, cache_hit=True),
    )
    assert _build(replace(second_source, extraction=cached)) == first
    encoded = json.dumps(_expected_payload(first), ensure_ascii=False)
    assert str(tmp_path) not in encoded
    assert "cache_hit" not in encoded and "timestamp" not in encoded


@pytest.mark.parametrize("owner", ["attributes", "geometries", "both"])
def test_coordinated_upstream_and_bundle_rehash_cannot_override_physical_bytes(
    source: _Source, owner: str
) -> None:
    bundle = _build(source)
    changes: dict[str, object] = {}
    if owner in ("attributes", "both"):
        layer = replace(bundle.attributes.layers[0], row_content_sha256="0" * 64)
        changes["attributes"] = _rehash_profile(bundle.attributes, layers=(layer,))
    if owner in ("geometries", "both"):
        layer = replace(bundle.geometries.layers[0], geometry_content_sha256="0" * 64)
        changes["geometries"] = _rehash_profile(bundle.geometries, layers=(layer,))
    forged = _rehash_bundle(bundle, **changes)
    assert (
        evidence._align_layers(forged.catalog, forged.attributes, forged.geometries)
        == bundle.layer_alignments
    )
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )
    assert isinstance(
        captured.value.__cause__,
        (
            InpnProtectedAreasAttributeProfileError,
            InpnProtectedAreasGeometryProfileError,
        ),
    )


def test_coordinated_catalog_profiles_and_bundle_rehash_cannot_override_source(
    source: _Source,
) -> None:
    bundle = _build(source)
    package = bundle.catalog.packages[0]
    layer = package.layers[0]
    forged_layer = replace(
        layer, fields=(replace(layer.fields[0], name="forged"), *layer.fields[1:])
    )
    catalog = replace(
        bundle.catalog, packages=(replace(package, layers=(forged_layer,)),)
    )
    catalog = replace(
        catalog,
        complete_catalog_content_sha256=catalog_module._catalog_content_sha256(catalog),
    )
    attribute_layer = bundle.attributes.layers[0]
    attributes = _rehash_profile(
        bundle.attributes,
        source_catalog_content_sha256=catalog.complete_catalog_content_sha256,
        layers=(
            replace(
                attribute_layer,
                fields=(
                    replace(attribute_layer.fields[0], name="forged"),
                    *attribute_layer.fields[1:],
                ),
            ),
        ),
    )
    geometries = _rehash_profile(
        bundle.geometries,
        source_catalog_content_sha256=catalog.complete_catalog_content_sha256,
    )
    forged = _rehash_bundle(
        bundle, catalog=catalog, attributes=attributes, geometries=geometries
    )
    assert (
        evidence._align_layers(catalog, attributes, geometries)
        == bundle.layer_alignments
    )
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )
    causes: list[BaseException] = []
    cause = captured.value.__cause__
    while cause is not None:
        causes.append(cause)
        cause = cause.__cause__
    assert any(isinstance(item, InpnProtectedAreasCatalogError) for item in causes)


@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "reordered"])
def test_rehashed_bundle_alignment_inventory_must_be_exact(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    source = _source(
        tmp_path, monkeypatch, layers=(("z_first", (1, 2, 4)), ("a_second", (8, 9)))
    )
    bundle = _build(source)
    first, second = bundle.layer_alignments
    alternatives = {
        "missing": (first,),
        "extra": (first, second, replace(second, layer_name="extra", layer_position=2)),
        "duplicate": (first, first),
        "reordered": (second, first),
    }
    forged = _rehash_bundle(bundle, layer_alignments=alternatives[mutation])
    assert forged.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(forged)
    )
    with pytest.raises(InpnProtectedAreasEvidenceError, match="alignment"):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", "EP/other.gpkg"),
        ("package_position", 1),
        ("file_sha256", "0" * 64),
        ("layer_name", "other"),
        ("layer_position", 1),
        ("feature_count", 4),
        ("fid_count", 4),
        ("fid_min", 0),
        ("fid_max", 5),
        ("fid_sequence_sha256", "0" * 64),
    ],
)
def test_forged_alignment_record_with_rehashed_bundle_is_rejected(
    source: _Source, field_name: str, value: object
) -> None:
    bundle = _build(source)
    forged = _rehash_bundle(
        bundle,
        layer_alignments=(replace(bundle.layer_alignments[0], **{field_name: value}),),
    )
    assert forged.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(forged)
    )
    with pytest.raises(InpnProtectedAreasEvidenceError):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "schema-bool",
        "schema-version",
        "hash-case",
        "hash-subclass",
        "hash-stale",
        "alignments-list",
        "alignment-object",
        "alignment-subclass",
        "catalog-object",
        "attributes-object",
        "geometries-object",
        "catalog-packages-list",
        "attribute-domain-list",
        "geometry-domain-list",
    ],
)
def test_bundle_validator_rejects_malformed_nested_runtime_evidence(
    source: _Source, mutation: str
) -> None:
    bundle = _build(source)
    changes: dict[str, object]
    if mutation.startswith("schema"):
        changes = {
            "evidence_bundle_schema_version": True if mutation == "schema-bool" else 2
        }
    elif mutation.startswith("hash"):
        values = {
            "hash-case": "A" * 64,
            "hash-subclass": _StringSubclass(
                bundle.complete_evidence_bundle_content_sha256
            ),
            "hash-stale": "0" * 64,
        }
        changes = {"complete_evidence_bundle_content_sha256": values[mutation]}
    elif mutation == "alignments-list":
        changes = {"layer_alignments": list(bundle.layer_alignments)}
    elif mutation in ("alignment-object", "alignment-subclass"):
        changes = {
            "layer_alignments": (
                object()
                if mutation == "alignment-object"
                else _subclass(bundle.layer_alignments[0]),
            )
        }
    elif mutation.endswith("-object"):
        changes = {mutation.removesuffix("-object"): object()}
    elif mutation == "catalog-packages-list":
        changes = {
            "catalog": replace(bundle.catalog, packages=list(bundle.catalog.packages))
        }
    elif mutation == "attribute-domain-list":
        profile = bundle.attributes
        field = replace(
            profile.layers[0].fields[0],
            distinct_values=list(profile.layers[0].fields[0].distinct_values),
        )
        layer = replace(
            profile.layers[0], fields=(field, *profile.layers[0].fields[1:])
        )
        changes = {"attributes": _rehash_profile(profile, layers=(layer,))}
    else:
        profile = bundle.geometries
        layer = replace(
            profile.layers[0],
            geometry_type_counts=list(profile.layers[0].geometry_type_counts),
        )
        changes = {"geometries": _rehash_profile(profile, layers=(layer,))}
    with pytest.raises(InpnProtectedAreasEvidenceError):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, replace(bundle, **changes)
        )


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", _StringSubclass("EP/one.gpkg")),
        ("package_position", False),
        ("file_sha256", _StringSubclass("0" * 64)),
        ("layer_name", _StringSubclass("first")),
        ("layer_position", False),
        ("feature_count", True),
        ("fid_count", np.int64(3)),
        ("fid_min", True),
        ("fid_max", 4.0),
        ("fid_sequence_sha256", _StringSubclass("0" * 64)),
    ],
)
def test_alignment_fields_require_exact_builtin_runtime_types(
    source: _Source, field_name: str, value: object
) -> None:
    bundle = _build(source)
    forged = replace(
        bundle,
        layer_alignments=(replace(bundle.layer_alignments[0], **{field_name: value}),),
    )
    with pytest.raises(
        InpnProtectedAreasEvidenceError, match="noncanonical runtime type"
    ):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )


@pytest.mark.parametrize("target", ["archive", "package"])
def test_persistent_source_mutation_after_alignment_fails_final_postcondition(
    source: _Source, monkeypatch: pytest.MonkeyPatch, target: str
) -> None:
    original = evidence._align_layers
    path = (
        source.extraction.download.path
        if target == "archive"
        else source.extraction.extraction_path / "EP" / "one.gpkg"
    )
    executed = False

    def align_then_mutate(*args: object, **kwargs: object) -> Any:
        nonlocal executed
        result = original(*args, **kwargs)
        payload = path.read_bytes()
        path.write_bytes(payload[:-1] + bytes([payload[-1] ^ 1]))
        executed = True
        return result

    monkeypatch.setattr(evidence, "_align_layers", align_then_mutate)
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        _build(source)
    assert executed
    assert isinstance(captured.value.__cause__, InpnProtectedAreasSourceError)


def test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = _source(
        tmp_path, monkeypatch, layers=(("first", (1, 2)), ("second", (8, 21)))
    )
    calls: list[str] = []
    original_attribute = evidence.validate_inpn_protected_areas_attribute_profile
    original_geometry = evidence.validate_inpn_protected_areas_geometry_profile
    original_source = evidence.validate_inpn_protected_areas_extraction

    def attributes(*args: object, **kwargs: object) -> None:
        calls.append("attributes")
        original_attribute(*args, **kwargs)

    def geometries(*args: object, **kwargs: object) -> None:
        calls.append("geometries")
        original_geometry(*args, **kwargs)

    def extraction(*args: object, **kwargs: object) -> Any:
        calls.append("final-extraction")
        return original_source(*args, **kwargs)

    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_attribute_profile", attributes
    )
    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_geometry_profile", geometries
    )
    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_extraction", extraction
    )
    bundle = _build(source)
    assert calls == ["attributes", "geometries", "final-extraction"]
    calls.clear()
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert calls == ["attributes", "geometries", "final-extraction"]


@pytest.mark.parametrize(
    ("boundary", "error_type"),
    [
        (
            "validate_inpn_protected_areas_attribute_profile",
            InpnProtectedAreasAttributeProfileError,
        ),
        (
            "validate_inpn_protected_areas_attribute_profile",
            InpnProtectedAreasCatalogError,
        ),
        (
            "validate_inpn_protected_areas_geometry_profile",
            InpnProtectedAreasGeometryProfileError,
        ),
        ("validate_inpn_protected_areas_extraction", InpnProtectedAreasSourceError),
    ],
)
def test_controlled_lower_boundary_failure_preserves_cause(
    source: _Source,
    monkeypatch: pytest.MonkeyPatch,
    boundary: str,
    error_type: type[Exception],
) -> None:
    """Fault injection tests error translation, not physical source trust."""
    error = error_type("package EP/one.gpkg layer first: deliberate boundary failure")

    def fail(*args: object, **kwargs: object) -> Any:
        raise error

    monkeypatch.setattr(evidence, boundary, fail)
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        _build(source)
    assert captured.value.__cause__ is error


def test_results_are_deeply_immutable_portable_profiles_not_joined_rows(
    source: _Source,
) -> None:
    bundle = _build(source)

    def walk(value: object) -> None:
        assert not isinstance(
            value,
            (
                dict,
                list,
                set,
                bytes,
                Path,
                np.ndarray,
                pd.DataFrame,
                sqlite3.Connection,
            ),
        )
        assert not hasattr(value, "geom_type")
        if is_dataclass(value) and not isinstance(value, type):
            for field in fields(value):
                walk(getattr(value, field.name))
        elif type(value) is tuple:
            for item in value:
                walk(item)
        else:
            assert type(value) in (str, int, bool, float, type(None))

    walk(bundle)
    with pytest.raises(FrozenInstanceError):
        bundle.layer_alignments = ()
    with pytest.raises(FrozenInstanceError):
        bundle.layer_alignments[0].fid_count = 999
    assert (
        tuple(field.name for field in fields(InpnProtectedAreasLayerAlignment))
        == ALIGNMENT_FIELDS
    )
    assert tuple(field.name for field in fields(InpnProtectedAreasEvidenceBundle)) == (
        "evidence_bundle_schema_version",
        "catalog",
        "attributes",
        "geometries",
        "layer_alignments",
        "complete_evidence_bundle_content_sha256",
    )


def test_module_exposes_only_trusted_public_boundary_and_has_no_third_reader() -> None:
    assert set(evidence.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(
        getattr(sources, name) is getattr(evidence, name) for name in EXPECTED_EXPORTS
    )
    assert not hasattr(sources, "_align_layers")
    assert not hasattr(sources, "_bundle_payload")
    tree = ast.parse(inspect.getsource(evidence))
    imports = {
        name.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for name in node.names
    }
    imports.update(
        node.module.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    assert not imports.intersection(
        {
            "pyogrio",
            "geopandas",
            "pandas",
            "sqlite3",
            "shapely",
            "requests",
            "socket",
            "urllib",
        }
    )
    forbidden = {
        "read_dataframe",
        "read_file",
        "read_arrow",
        "open_arrow",
        "execute",
        "deserialize",
        "from_wkb",
        "read_bytes",
        "open_safe_https",
        "download_inpn_protected_areas_archive",
    }
    calls = {
        node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Attribute, ast.Name))
    }
    assert not calls.intersection(forbidden)
