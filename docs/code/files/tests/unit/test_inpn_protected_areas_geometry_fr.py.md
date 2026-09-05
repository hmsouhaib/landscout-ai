# `tests/unit/test_inpn_protected_areas_geometry_fr.py`

## File identity

- Repository path: `tests/unit/test_inpn_protected_areas_geometry_fr.py`
- File type: Python unit/regression tests
- Domain: isolated INPN EP raw-geometry source authority and technical evidence
- Source SHA256: `d953df5225ddefb72928e478881ad130ab856f503ecd107ab32e74f892375e8c`
- Collected cases: `327`

## 1. Fixture isolation and actual regression scope

Every source is a synthetic ZIP/GeoPackage under Pytest temporary directories. An ordinary XY container is initially written with Pyogrio only during fixture construction. Test geometries are then installed through SQLite as explicit Standard GeoPackageBinary + ISO WKB bytes; measured geometries never pass through the lossy Pyogrio geometry reader. Raw point type words and XY/XYZ/XYM/XYZM coordinates are independently constructed with struct, including NaN empty encodings. The real Shapely parser, coordinate extraction, WKB serialization, and source download/extraction/catalog authorities remain active. In-memory fake safe HTTPS carries synthetic ZIP bytes; no real EP cache, DNS, HTTP, or download is used.

Header/parser tests isolate byte order, flags, envelope lengths, SRS/empty consistency, dimensional declarations, malformed framing, and topology. They do not assert numerical header-envelope agreement with WKB coordinates; observed coordinate bounds and catalog bounds are independently compared. Source-bound builder/validator tests prove exact package snapshots, FID/BLOB-only projection, complete domains/counts/bounds, portable hashes, immediate immutable outputs, cheap preflight, independent physical rebuild, and effective transient/persistent path swaps. Private seam tests are identified below and do not replace the real-parser measured regressions.

## 2. Every import and constant


```python
from __future__ import annotations
import io
import json
import math
import sqlite3
import struct
import zipfile
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, fields, is_dataclass, replace
from hashlib import sha256
from pathlib import Path
from typing import Any, ClassVar
import geopandas as gpd
import numpy as np
import pyogrio
import pytest
import shapely
import yaml
from shapely.geometry import Point
from landscout import sources
from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module
from landscout.sources import inpn_protected_areas_fr as source_module
from landscout.sources import inpn_protected_areas_geometry_fr as geometry
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)
from landscout.sources.inpn_protected_areas_geometry_fr import (
    InpnProtectedAreasGeometryProfile,
    InpnProtectedAreasGeometryProfileError,
    build_inpn_protected_areas_geometry_profile,
    validate_inpn_protected_areas_geometry_profile,
)
```


```python
CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")

EXPECTED_EXPORTS = {
    "InpnProtectedAreasGeometryTypeCount",
    "InpnProtectedAreasCoordinateDimensionCount",
    "InpnProtectedAreasGeometryValidityReasonCount",
    "InpnProtectedAreasLayerGeometryProfile",
    "InpnProtectedAreasGeometryProfile",
    "InpnProtectedAreasGeometryProfileError",
    "build_inpn_protected_areas_geometry_profile",
    "validate_inpn_protected_areas_geometry_profile",
}

DIMENSIONS = (
    (False, False, (1.0, 2.0)),
    (True, False, (1.0, 2.0, 3.0)),
    (False, True, (1.0, 2.0, 4.0)),
    (True, True, (1.0, 2.0, 3.0, 4.0)),
)

CORE_TYPE_CASES = (
    ("POINT", "Point", "POINT (1 2)"),
    ("LINESTRING", "LineString", "LINESTRING (0 0, 1 2)"),
    ("POLYGON", "Polygon", "POLYGON ((0 0, 2 0, 2 2, 0 0))"),
    ("MULTIPOINT", "MultiPoint", "MULTIPOINT ((1 2), (3 4))"),
    ("MULTILINESTRING", "MultiLineString", "MULTILINESTRING ((0 0, 1 2))"),
    ("MULTIPOLYGON", "MultiPolygon", "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))"),
    ("GEOMETRYCOLLECTION", "GeometryCollection", "GEOMETRYCOLLECTION (POINT (1 2))"),
)

INVALID_DECLARED_TYPES = (
    "point",
    " Point",
    "POINT ",
    "UNKNOWN",
    "NOT_A_TYPE",
    "CURVEPOLYGON",
)
```

Standard-library imports construct and corrupt synthetic bytes, record SQL, hash canonical expectations, and inspect frozen dataclasses. NumPy supplies forbidden scalar/array fixtures; GeoPandas/Pyogrio create ordinary containers and name fatal reader sentinels; Shapely provides real geometry assertions. `geometry` is the imported `landscout.sources.inpn_protected_areas_geometry_fr` module; `catalog_module` and `source_module` refer to their distinct qualified physical trust owners. `EXPECTED_EXPORTS` is the eight-name approved geometry API, and `DIMENSIONS` explicitly separates XY, XYZ, XYM, and XYZM layouts. CORE_TYPE_CASES contains the seven exact declaration/Shapely-name/WKT records used for concrete and GEOMETRY-supertype controls. INVALID_DECLARED_TYPES contains the six exact lowercase/edge-whitespace/unknown/extended negative declarations.

## 3. Every support class

### `_Response`

Closable in-memory archive response with ZIP Content-Type; used only by deterministic fake safe HTTPS.

Bases: `io.BytesIO`.


```python
headers: ClassVar[dict[str, str]] = {"Content-Type": "application/zip"}
```

### `_StringSubclass`

Comparison-equal str subclass used to prove exact built-in text enforcement.

Bases: `str`.

### `_BytesSubclass`

Comparison-equal bytes subclass used to prove exact immutable byte-snapshot/BLOB type enforcement.

Bases: `bytes`.

### `test_deserialize_uses_exact_bytes_once_per_package_for_all_layers.RecordedConnection`

Real SQLite Connection subclass that records exact deserialize inputs while retaining actual SQLite behavior.

Bases: `sqlite3.Connection`.

### `test_sqlite_close_failures_are_controlled_and_chained.CloseFailure`

Real SQLite Connection subclass that closes normally before raising a parametrized cleanup error.

Bases: `sqlite3.Connection`.

## 4. Every fixture, helper, test, and nested callback

Each entry records the exact callable signature/decorators, its source-derived purpose, its own direct assertions and expected exceptions, and any monkeypatch statements. Assertions belonging to nested callbacks are documented under their qualified local name rather than misattributed to the parent test. Parametrization values are exact checked-in source, not inferred case labels. The complete final snapshot preserves all setup/control flow.

### `_response`


```python
@contextmanager
def _response(payload: bytes) -> Iterator[_Response]:
```

Owns and closes a deterministic in-memory ZIP response; no real network is involved.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_json_hash`


```python
def _json_hash(value: object) -> str:
```

Independently reproduces compact sorted-key Unicode finite-only JSON SHA256 for expected FID/raw streams.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_point_wkb`


```python
def _point_wkb(
    coordinates: tuple[float, ...] = (1.0, 2.0),
    *,
    has_z: bool = False,
    has_m: bool = False,
    little_endian: bool = True,
) -> bytes:
    # ISO dimensional type words and ordinates are built independently of Shapely.
```

Constructs ISO dimensional point WKB using struct, independent of Shapely and Pyogrio, with explicit byte order and every supplied ordinate.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_blob`


```python
def _blob(
    wkb: bytes | None = None,
    *,
    srs_id: int = 2154,
    little_endian: bool = True,
    empty: bool = False,
    envelope_code: int = 0,
) -> bytes:
```

Constructs Standard GeoPackageBinary headers/envelopes around exact embedded WKB; header and WKB byte orders are independent.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_wkt_blob`


```python
def _wkt_blob(wkt: str) -> bytes:
```

Creates topology fixtures through Shapely WKT-to-ISO-WKB and preserves its empty flag in a Standard GeoPackageBinary wrapper.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_metadata`


```python
def _metadata(**changes: object) -> Any:
```

Builds private layer metadata for direct parser tests with optional controlled field substitutions.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_gpkg_bytes`


```python
def _gpkg_bytes(
    tmp_path: Path,
    rows: tuple[tuple[int, bytes | None], ...] | None = None,
    *,
    layer_names: tuple[str, ...] = ("physical_layer",),
    z_flag: int = 2,
    m_flag: int = 2,
    geometry_type: str = "Unknown",
) -> bytes:
    # Pyogrio creates ONLY an ordinary XY container. Every tested geometry BLOB
    # is installed through SQLite; M/ZM never pass through Pyogrio conversion.
```

Writes an ordinary XY container only, then replaces FID/geometry BLOB rows and dimensional metadata using fixture-only SQLite. Measured geometries never pass through Pyogrio conversion.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_source`


```python
def _source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    package: bytes | None = None,
    *,
    files: Mapping[str, bytes] | None = None,
) -> tuple[
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasCatalog,
]:
```

Builds a deterministic synthetic ZIP, pins its exact size/SHA in validated source config, replaces safe HTTPS with the in-memory response, and uses real download/extraction/catalog authorities.

Monkeypatch expressions:


```python
monkeypatch.setattr(
        source_module, "open_safe_https", lambda *a, **k: _response(archive_bytes)
    )
```

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_build`


```python
def _build(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    rows: tuple[tuple[int, bytes | None], ...] | None = None,
    **options: Any,
) -> InpnProtectedAreasGeometryProfile:
```

Runs the public geometry builder on a verified synthetic source constructed from explicit FID/BLOB rows.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_rehash`


```python
def _rehash(
    profile: InpnProtectedAreasGeometryProfile,
) -> InpnProtectedAreasGeometryProfile:
```

Recalculates the complete profile hash after a deliberate immutable replacement so structural/physical regressions do not pass only because of a stale outer digest.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_raw_sqlite_point_dimensions_and_empty_roundtrip_are_lossless`


```python
@pytest.mark.parametrize(("has_z", "has_m", "coordinates"), DIMENSIONS)
@pytest.mark.parametrize("empty", [False, True])
def test_raw_sqlite_point_dimensions_and_empty_roundtrip_are_lossless(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    has_z: bool,
    has_m: bool,
    coordinates: tuple[float, ...],
    empty: bool,
) -> None:
```

Exercises all XY/XYZ/XYM/XYZM point layouts and all four EMPTY layouts through actual synthetic GeoPackage BLOB reads, real Shapely parsing, coordinate extraction, explicit WKB roundtrip, and public profile counters/domains. In particular measured M=4 and ZM Z=3/M=4 are never mocked.

Direct assertions:


```python
assert rows == ((11, blob),)

assert parsed.embedded_wkb == blob[8:]

assert bool(shapely.has_z(actual)) is has_z

assert bool(shapely.has_m(actual)) is has_m

assert int(shapely.get_coordinate_dimension(actual)) == len(coordinates)

assert bool(shapely.is_empty(actual)) is empty

assert extracted.tolist() == ([] if empty else [list(coordinates)])

assert bool(shapely.has_z(roundtrip)) is has_z

assert bool(shapely.has_m(roundtrip)) is has_m

assert int(shapely.get_coordinate_dimension(roundtrip)) == len(coordinates)

assert layer.empty_geometry_count == int(empty)

assert layer.null_geometry_count == 0

assert layer.has_z_geometry_count == int(has_z)

assert layer.has_m_geometry_count == int(has_m)

assert layer.total_coordinate_count == int(not empty)

assert (domain.coordinate_dimension, domain.has_z, domain.has_m, domain.count) == (
        len(coordinates),
        has_z,
        has_m,
        1,
    )
```

### `test_standard_header_endianness_and_every_envelope_code`


```python
@pytest.mark.parametrize("header_little", [False, True])
@pytest.mark.parametrize("wkb_little", [False, True])
@pytest.mark.parametrize("envelope_code", range(5))
def test_standard_header_endianness_and_every_envelope_code(
    header_little: bool, wkb_little: bool, envelope_code: int
) -> None:
```

Combines both header byte orders, both independent embedded-WKB byte orders, and every supported envelope code; requires exact embedded bytes and unchanged point coordinates.

Direct assertions:


```python
assert parsed.embedded_wkb == embedded

assert parsed.header_little_endian is header_little

assert parsed.envelope_code == envelope_code

assert len(parsed.envelope) == (0, 4, 6, 6, 8)[envelope_code]

assert shapely.get_coordinates(parsed.geometry).tolist() == [[1.0, 2.0]]
```

### `test_malformed_geometry_blob_is_controlled`


```python
@pytest.mark.parametrize(
    "blob",
    [
        None,
        bytearray(_blob()),
        memoryview(_blob()),
        _BytesSubclass(_blob()),
        b"",
        b"GP\x00",
        b"XX" + _blob()[2:],
        _blob()[:2] + b"\x01" + _blob()[3:],
        _blob()[:3] + b"\x41" + _blob()[4:],
        _blob()[:3] + b"\x81" + _blob()[4:],
        _blob()[:3] + b"\x21" + _blob()[4:],
        *(_blob()[:3] + bytes([1 | code << 1]) + _blob()[4:] for code in (5, 6, 7)),
        _blob(envelope_code=4)[:30],
        _blob()[:8],
        _blob(b"not WKB"),
        _blob(srs_id=4326),
        _blob(empty=True),
        _blob(_point_wkb((math.nan, math.nan)), empty=False),
    ],
)
def test_malformed_geometry_blob_is_controlled(blob: object) -> None:
```

Rejects wrong runtime types, short/empty data, magic/version/reserved/extended flags, forbidden envelope codes, truncation, absent/malformed WKB, mismatched SRS, and disagreement between header-empty and parsed-empty state.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_z_m_declarations_are_enforced`


```python
@pytest.mark.parametrize(
    ("z_flag", "m_flag", "has_z", "has_m", "accepted"),
    [
        (0, 2, True, False, False),
        (1, 2, False, False, False),
        (2, 2, True, False, True),
        (2, 2, False, False, True),
        (2, 0, False, True, False),
        (2, 1, False, False, False),
        (2, 2, False, True, True),
        (1, 1, True, True, True),
    ],
)
@pytest.mark.parametrize("empty", [False, True])
def test_z_m_declarations_are_enforced(
    z_flag: int, m_flag: int, has_z: bool, has_m: bool, accepted: bool, empty: bool
) -> None:
```

Separately tests prohibited, mandatory, and optional Z/M metadata against actual parsed ordinate layouts without dimension erasure.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_sql_identifier_rejects_noncanonical_runtime_values`


```python
@pytest.mark.parametrize(
    "value", [None, "", b"", "a\x00b", "a\x01b", "a\nb", _StringSubclass("name")]
)
def test_sql_identifier_rejects_noncanonical_runtime_values(value: object) -> None:
```

Rejects null/non-string/empty/subclass/NUL/control identifier inputs immediately before SQL construction.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_sql_identifier_preserves_spelling_and_escapes_quotes`


```python
def test_sql_identifier_preserves_spelling_and_escapes_quotes() -> None:
```

Proves quote escaping turns a SQL-looking source identifier into one exact quoted SQLite identifier without trimming or executing source text.

Direct assertions:


```python
assert (
        geometry._quote_sqlite_identifier(value) == '"layer""; DROP TABLE private; --"'
    )
```

### `test_sqlite_snapshot_invalid_bytes_fail_controlled`


```python
@pytest.mark.parametrize(
    "value", [None, b"", b"not sqlite", bytearray(b"sqlite"), _BytesSubclass(b"sqlite")]
)
def test_sqlite_snapshot_invalid_bytes_fail_controlled(value: object) -> None:
```

Exercises wrong/empty/malformed snapshot bytes through the controlled SQLite context rather than a live package path.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_sqlite_snapshot_is_query_only_and_closes`


```python
def test_sqlite_snapshot_is_query_only_and_closes(tmp_path: Path) -> None:
```

Reads the active query-only/trusted-schema settings, proves SQL writes are prohibited, and proves connection use after context exit fails because the handle was closed.

Direct assertions:


```python
assert connection.execute("PRAGMA query_only").fetchone() == (1,)

assert connection.execute("PRAGMA trusted_schema").fetchone() == (0,)
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(sqlite3.OperationalError)

pytest.raises(sqlite3.ProgrammingError)
```

### `test_sqlite_failures_are_translated_and_chained`


```python
@pytest.mark.parametrize(
    "error_type",
    [
        sqlite3.DatabaseError,
        sqlite3.OperationalError,
        sqlite3.IntegrityError,
        OverflowError,
        TypeError,
        ValueError,
    ],
)
def test_sqlite_failures_are_translated_and_chained(
    tmp_path: Path, error_type: type[Exception]
) -> None:
```

Injects each specified database/overflow/type/value failure inside the snapshot boundary and requires the domain error to retain its original chained cause.

Direct assertions:


```python
assert isinstance(captured.value.__cause__, error_type)
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Direct raise statements:


```python
raise error_type("deliberate SQLite boundary failure")
```

### `test_source_complete_profile_and_physical_validation`


```python
def test_source_complete_profile_and_physical_validation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Builds and independently validates a complete source-bound profile with exact source/catalog locks, aggregates, FID hash, and observed bounds.

Direct assertions:


```python
assert type(profile) is InpnProtectedAreasGeometryProfile

assert (
        profile.geometry_profile_schema_version
        == geometry.GEOMETRY_PROFILE_SCHEMA_VERSION
        == 1
    )

assert profile.source_catalog_schema_version == 2

assert (
        profile.source_catalog_content_sha256 == catalog.complete_catalog_content_sha256
    )

assert profile.archive_sha256 == config.expected_archive_sha256

assert profile.package_count == profile.layer_count == 1

assert profile.geometry_row_count == 2

assert profile.valid_non_empty_geometry_count == 2

assert (
        profile.null_geometry_count
        == profile.empty_geometry_count
        == profile.invalid_non_empty_geometry_count
        == 0
    )

assert profile.layers[0].fid_sequence_sha256 == _json_hash([1, 7])

assert profile.layers[0].observed_total_bounds == (1.0, 2.0, 3.0, 5.0)

assert len(profile.complete_geometry_profile_content_sha256) == 64
```

### `test_only_fid_geometry_sql_and_no_feature_reader`


```python
def test_only_fid_geometry_sql_and_no_feature_reader(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Records executed SQLite SQL while fatal sentinels block alternative feature readers and geometry modification; verifies the sole feature projection is FID plus geometry and excludes environmental attribute columns.

Direct assertions:


```python
assert feature_queries == ['SELECT "fid", "geom" FROM "physical_layer"']

assert all(
        "never_read_attribute" not in query and "SELECT *" not in query
        for query in traces
    )

assert profile.geometry_row_count == 2
```

Monkeypatch expressions:


```python
monkeypatch.setattr(geometry, "_open_gpkg_sqlite_snapshot", traced)

monkeypatch.setattr(owner, name, forbidden)

monkeypatch.setattr(gpd.GeoDataFrame, "to_crs", forbidden)
```

### `test_only_fid_geometry_sql_and_no_feature_reader.traced`


```python
@contextmanager
def traced(payload: bytes, relative_path: str) -> Any:
```

Wraps the real SQLite context, asserts query-only state, and records every executed statement before yielding the original connection.

Direct assertions:


```python
assert connection.execute("PRAGMA query_only").fetchone() == (1,)
```

### `test_only_fid_geometry_sql_and_no_feature_reader.forbidden`


```python
def forbidden(*args: object, **kwargs: object) -> Any:
```

Fatal sentinel: any forbidden reader, repair, or reprojection invocation fails the regression immediately.

Direct raise statements:


```python
raise AssertionError("Forbidden feature reader or geometry modification")
```

### `test_deserialize_uses_exact_bytes_once_per_package_for_all_layers`


```python
def test_deserialize_uses_exact_bytes_once_per_package_for_all_layers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Uses two packages and three layers with a recording Connection subclass to prove one exact package-byte deserialization per package, shared layers, distinct snapshots, and in-memory-only connections.

Direct assertions:


```python
assert inputs == [first, second]

assert inputs[0] is not inputs[1]

assert len(calls) == 2

assert profile.package_count == 2 and profile.layer_count == 3
```

Monkeypatch expressions:


```python
monkeypatch.setattr(geometry.sqlite3, "connect", connect)
```

### `test_deserialize_uses_exact_bytes_once_per_package_for_all_layers.RecordedConnection.deserialize`


```python
def deserialize(self, data: bytes, *, name: str = "main") -> None:
```

Records and exact-type-checks each byte argument before invoking the real SQLite deserializer.

Direct assertions:


```python
assert type(data) is bytes
```

### `test_deserialize_uses_exact_bytes_once_per_package_for_all_layers.connect`


```python
def connect(*args: Any, **kwargs: Any) -> Any:
```

Records connection calls, requires :memory:, and injects the recording subclass without replacing SQLite behavior.

Direct assertions:


```python
assert args == (":memory:",)
```

### `test_null_empty_and_invalid_are_separate_factual_evidence`


```python
def test_null_empty_and_invalid_are_separate_factual_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Combines NULL, EMPTY Point, and self-intersecting Polygon; requires distinct state counts, retained invalid topology with exact Shapely reason, coordinate count, and observed bounds.

Direct assertions:


```python
assert (
        layer.null_geometry_count,
        layer.empty_geometry_count,
        layer.non_empty_geometry_count,
    ) == (1, 1, 1)

assert layer.valid_non_empty_geometry_count == 0

assert layer.invalid_non_empty_geometry_count == 1

assert reason.is_valid is False

assert reason.reason == shapely.is_valid_reason(shapely.from_wkt(invalid))

assert reason.count == 1

assert layer.total_coordinate_count == 5

assert layer.observed_total_bounds == (0.0, 0.0, 2.0, 2.0)
```

### `test_null_does_not_violate_mandatory_z_m_flags`


```python
def test_null_does_not_violate_mandatory_z_m_flags(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Shows SQLite NULL carries no geometry dimension and therefore does not violate mandatory Z/M declarations.

Direct assertions:


```python
assert len(captured) == 8

assert profile.null_geometry_count == 1

assert profile.has_z_geometry_count == profile.has_m_geometry_count == 0
```

Expected exception/warning/fatal-check expressions:


```python
pytest.warns(
        UserWarning, match=r"Measured \(M\) geometry types are not supported"
    )
```

### `test_empty_feature_table_has_null_bounds_and_exact_empty_hashes`


```python
def test_empty_feature_table_has_null_bounds_and_exact_empty_hashes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Requires a zero-row feature table to retain null extrema/bounds, empty domains, BOTH_NULL relation, and independently reproduced deterministic empty component hashes.

Direct assertions:


```python
assert layer.fid_count == profile.geometry_row_count == 0

assert layer.fid_min is layer.fid_max is None

assert layer.observed_total_bounds is layer.catalog_total_bounds is None

assert layer.bounds_relation == "BOTH_NULL"

assert (
        layer.geometry_type_counts
        == layer.coordinate_dimension_counts
        == layer.validity_reason_counts
        == ()
    )

assert (
        layer.fid_sequence_sha256
        == layer.geometry_content_sha256
        == layer.raw_geometry_blob_content_sha256
        == _json_hash([])
    )
```

### `test_nonfinite_present_xy_z_m_coordinates_fail_closed`


```python
@pytest.mark.parametrize("ordinate", [0, 1, 2, 3])
@pytest.mark.parametrize("bad", [math.nan, math.inf, -math.inf])
def test_nonfinite_present_xy_z_m_coordinates_fail_closed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, ordinate: int, bad: float
) -> None:
```

Places NaN/+Inf/-Inf separately in X, Y, Z, and M of raw XYZM point WKB; each attempted source profile must fail rather than hide or repair the ordinate.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_wrong_public_inputs_fail_controlled`


```python
@pytest.mark.parametrize("argument", ["extraction", "config", "catalog"])
def test_wrong_public_inputs_fail_controlled(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, argument: str
) -> None:
```

Substitutes arbitrary objects for extraction/config/catalog and requires the public geometry error.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_wrong_profile_type_rejected_before_snapshot`


```python
def test_wrong_profile_type_rejected_before_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Makes SQLite snapshot opening fatal and requires an invalid public profile type to be rejected before geometry reads.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("snapshot opened"),
    )
```

### `test_portable_roots_cache_hit_and_repeated_build_are_identical`


```python
def test_portable_roots_cache_hit_and_repeated_build_are_identical(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Builds identical package bytes under different cache roots, repeats the build, and toggles operational cache-hit fields; portable profile equality must remain exact.

Direct assertions:


```python
assert (
        build_inpn_protected_areas_geometry_profile(extraction_a, config_a, catalog_a)
        == first
    )

assert (
        build_inpn_protected_areas_geometry_profile(extraction_b, config_b, catalog_b)
        == first
    )

assert (
        build_inpn_protected_areas_geometry_profile(cache_hit, config_a, catalog_a)
        == first
    )
```

### `test_exact_raw_and_parser_hash_sensitivity`


```python
@pytest.mark.parametrize("mutation", ["x", "z", "m", "fid", "raw-header", "ring-order"])
def test_exact_raw_and_parser_hash_sensitivity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
```

Independently checks raw-BLOB hashes while changing X/Z/M/FID/header byte order/ring orientation; header-only changes affect raw identity but not parsed geometry, while structural geometry/FID changes affect both streams.

Direct assertions:


```python
assert first.raw_geometry_blob_content_sha256 == _json_hash(
        [[1, sha256(first_blob).hexdigest()]]
    )

assert second.raw_geometry_blob_content_sha256 == _json_hash(
        [[second_fid, sha256(second_blob).hexdigest()]]
    )

assert (
        first.raw_geometry_blob_content_sha256
        != second.raw_geometry_blob_content_sha256
    )

assert (first.geometry_content_sha256 == second.geometry_content_sha256) is (
        mutation == "raw-header"
    )
```

### `test_unsorted_sparse_fids_are_sorted_without_renumbering`


```python
def test_unsorted_sparse_fids_are_sorted_without_renumbering(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Supplies sparse positive and negative source identifiers out of order and requires exact numeric canonical order, preserved extrema, and independently calculated FID digest.

Direct assertions:


```python
assert (layer.fid_count, layer.fid_min, layer.fid_max) == (3, -4, 99)

assert layer.fid_sequence_sha256 == _json_hash([-4, 8, 99])
```

### `test_byte_snapshot_resists_path_swap_and_final_postcondition`


```python
@pytest.mark.parametrize("persistent", [False, True])
def test_byte_snapshot_resists_path_swap_and_final_postcondition(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, persistent: bool
) -> None:
```

Replaces the live physical package only after bytes have been deserialized. Restored transient substitution cannot change output; persistent substitution fails final physical checks. The hook must actually run.

Direct assertions:


```python
assert (
            build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
            == baseline
        )

assert seen
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(geometry, "_open_gpkg_sqlite_snapshot", swapped)
```

### `test_byte_snapshot_resists_path_swap_and_final_postcondition.swapped`


```python
@contextmanager
def swapped(payload: bytes, relative_path: str) -> Any:
```

Enters the actual original snapshot, writes alternate synthetic bytes to the physical path, and restores only for the transient branch.

Direct assertions:


```python
assert payload == first
```

### `test_coordinated_component_and_complete_hash_forgery_fails_physical_rebuild`


```python
@pytest.mark.parametrize(
    "component", ["raw_geometry_blob_content_sha256", "geometry_content_sha256"]
)
def test_coordinated_component_and_complete_hash_forgery_fails_physical_rebuild(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, component: str
) -> None:
```

Changes either raw or parser component SHA and coherently rehashes the profile. Intrinsic validation accepts unreconstructable component syntax, but independent physical validation must reject the forged content.

Direct assertions:


```python
assert geometry._validate_profile_intrinsic(forged) is forged
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_catalog_preflight_rejects_mismatch_before_sqlite_geometry_read`


```python
@pytest.mark.parametrize(
    "mutation", ["source", "catalog", "package", "layer", "crs", "bounds"]
)
def test_catalog_preflight_rejects_mismatch_before_sqlite_geometry_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
```

Rehashes source/catalog/package/layer/CRS/bounds mismatches and makes SQLite opening fatal, isolating rejection before any geometry-row materialization.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("geometry snapshot opened before preflight rejection"),
    )
```

### `test_public_models_are_frozen_portable_and_export_only_factual_api`


```python
def test_public_models_are_frozen_portable_and_export_only_factual_api(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Recursively rejects nonportable/mutable/geometry/handle payloads, tests immediate frozen assignment failures, verifies exact module exports and qualified package bindings, and confirms raw helper names remain private.

Direct assertions:


```python
assert set(geometry.__all__) == EXPECTED_EXPORTS

assert EXPECTED_EXPORTS <= set(sources.__all__)

assert all(
        getattr(sources, name) is getattr(geometry, name) for name in EXPECTED_EXPORTS
    )

assert not hasattr(sources, "_open_gpkg_sqlite_snapshot")

assert not hasattr(sources, "_parse_gpkg_geometry_blob")
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(FrozenInstanceError)

pytest.raises(FrozenInstanceError)
```

### `test_public_models_are_frozen_portable_and_export_only_factual_api.walk`


```python
def walk(value: object) -> None:
```

Recursively visits dataclass fields and tuples, rejects mutable and nonportable values, and requires canonical scalar leaf types.

Direct assertions:


```python
assert not isinstance(
            value, (dict, list, set, bytes, Path, np.ndarray, sqlite3.Connection)
        )

assert not hasattr(value, "geom_type")

assert type(value) in (str, bool, int, float, type(None))
```

### `test_physical_metadata_fails_closed_without_guessing`


```python
@pytest.mark.parametrize(
    "mutation",
    [
        "missing-contents",
        "non-feature",
        "duplicate-contents",
        "missing-geometry",
        "duplicate-geometry",
        "missing-column",
        "contents-srs",
        "catalog-srs",
        "bad-z",
        "bad-m",
        "feature-view",
        "metadata-view",
        "no-pk",
        "wrong-pk",
        "composite-pk",
        "desc-pk",
        "without-rowid",
    ],
)
def test_physical_metadata_fails_closed_without_guessing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
```

Mutates actual SQLite metadata/table schemas to cover missing/duplicate/non-feature rows, missing geometry column, conflicting SRS, invalid Z/M, feature/metadata views, absent/wrong/composite/DESC primary keys, and WITHOUT ROWID. The real metadata reader must fail without guessed keys.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_source_column_identity_is_discovered_not_guessed`


```python
def test_source_column_identity_is_discovered_not_guessed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Renames actual FID/geometry columns to spellings with spaces, updates exact GeoPackage metadata, and requires the public result to retain those names and unchanged FID identity.

Direct assertions:


```python
assert layer.fid_column_name == "source key"

assert layer.geometry_column_name == "source shape"

assert layer.feature_table_kind == "table"

assert layer.fid_sequence_sha256 == _json_hash([1, 7])
```

### `test_impossible_sqlite_fid_and_blob_rows_are_rejected`


```python
@pytest.mark.parametrize(
    "rows",
    [
        ((1, None), (1, None)),
        ((True, None),),
        ((None, None),),
        ((1.5, None),),
        ((np.int64(1), None),),
        ((1, "not blob"),),
        ((1, bytearray(b"x")),),
        ((1,),),
        ((1, None, "attribute"),),
    ],
)
def test_impossible_sqlite_fid_and_blob_rows_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    rows: tuple[tuple[object, ...], ...],
) -> None:
```

Injects impossible DB-API rows at the narrow row-fetch seam while keeping a real SQLite snapshot; proves duplicate/Boolean/null/float/NumPy FIDs and malformed BLOB/column shapes are not coerced.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(geometry, "_sqlite_rows", lambda *a, **k: rows)
```

### `test_geometry_row_count_must_match_catalog`


```python
def test_geometry_row_count_must_match_catalog(tmp_path: Path) -> None:
```

Passes an incorrect expected catalog count to the real two-column row reader and requires controlled rejection.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_unsorted_reader_rows_hash_in_numeric_order`


```python
def test_unsorted_reader_rows_hash_in_numeric_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Supplies a deliberately unsorted DB-API row sequence to isolate exact numeric sorting while preserving FIDs, NULL, and BLOB values.

Direct assertions:


```python
assert result == (rows[1], rows[2], rows[0])
```

Monkeypatch expressions:


```python
monkeypatch.setattr(geometry, "_sqlite_rows", lambda *a, **k: rows)
```

### `test_intrinsic_layer_rejects_noncanonical_evidence`


```python
@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("fid_count", True),
        ("fid_count", 3),
        ("fid_min", None),
        ("fid_min", 7),
        ("fid_max", 1),
        ("gpkg_z_flag", 3),
        ("gpkg_m_flag", True),
        ("file_size", 0),
        ("package_position", 1),
        ("layer_position", 1),
        ("null_geometry_count", 1),
        ("empty_geometry_count", -1),
        ("valid_non_empty_geometry_count", 1),
        ("has_z_geometry_count", 1),
        ("has_m_geometry_count", 3),
        ("total_coordinate_count", True),
        ("raw_geometry_blob_content_sha256", "x" * 64),
        ("geometry_content_sha256", "f" * 63),
        ("driver_name", "GeoJSON"),
        ("feature_table_kind", "view"),
        ("bounds_relation", "CLOSE_ENOUGH"),
        ("observed_total_bounds", (0.0, 0.0, 0.0)),
        ("observed_total_bounds", (9.0, 0.0, 1.0, 2.0)),
        ("observed_total_bounds", (1, 2, 3, 5)),
        ("geometry_type_counts", []),
        ("coordinate_dimension_counts", []),
        ("validity_reason_counts", []),
    ],
)
def test_intrinsic_layer_rejects_noncanonical_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, field_name: str, value: object
) -> None:
```

Coherently rehashes wrong scalar types, impossible FID/count/position/flag evidence, malformed digests/bounds, wrong driver/table kind, and mutable domains; intrinsic validation must reject each actual structural defect.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_intrinsic_profile_rejects_noncanonical_evidence`


```python
@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("geometry_profile_schema_version", 2),
        ("geometry_profile_schema_version", True),
        ("geometry_encoding_schema_version", 2),
        ("geometry_encoding_contract", "unknown"),
        ("source_catalog_schema_version", 1),
        ("geometry_row_count", 99),
        ("package_count", 2),
        ("layer_count", 0),
        ("archive_size", False),
        ("has_z_geometry_count", 1),
        ("provider", _StringSubclass("PatriNat")),
        ("sqlite_version", ""),
        ("geos_version", _StringSubclass("3.13.1")),
        ("source_catalog_content_sha256", "bad"),
        ("layers", []),
    ],
)
def test_intrinsic_profile_rejects_noncanonical_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, field_name: str, value: object
) -> None:
```

Coherently rehashes wrong schema/encoding/catalog/aggregate/archive types, comparison-equal string subclasses, missing toolchain text, malformed SHA, and mutable layer collections; intrinsic validation remains strict.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_intrinsic_package_paths_use_shared_authoritative_grammar`


```python
@pytest.mark.parametrize(
    "relative_path",
    [
        " EP/a.gpkg",
        "EP/a.gpkg ",
        "/EP/a.gpkg",
        "C:/EP/a.gpkg",
        "../a.gpkg",
        "EP\\a.gpkg",
        "EP/a.txt",
        "EP/CON.gpkg",
        "EP/NUL.gpkg",
        "EP/a:b.gpkg",
        "EP/dir /a.gpkg",
        "EP/ dir/a.gpkg",
        "EP/dir./a.gpkg",
        "EP/control\x01.gpkg",
        "EP/ＮＵＬ.gpkg",
        "EP/dir／a.gpkg",
    ],
)
def test_intrinsic_package_paths_use_shared_authoritative_grammar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, relative_path: str
) -> None:
```

Rehashes forbidden absolute/driven/traversing/backslash/suffix/reserved/control/edge-whitespace/NFKC-hazard package paths and requires the authoritative extraction-compatible grammar.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_intrinsic_domains_reject_duplicate_entries`


```python
@pytest.mark.parametrize(
    "domain",
    ["geometry_type_counts", "coordinate_dimension_counts", "validity_reason_counts"],
)
def test_intrinsic_domains_reject_duplicate_entries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, domain: str
) -> None:
```

Splits one two-row domain frequency into duplicate equal keys with otherwise closed counts; proves canonical uniqueness is checked independently of arithmetic.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_intrinsic_profile_hash_mismatch_is_rejected`


```python
def test_intrinsic_profile_hash_mismatch_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Changes only the complete profile SHA to valid-looking incorrect syntax and requires recomputed intrinsic hash comparison to fail.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_toolchain_identity_is_portable_and_hash_significant`


```python
def test_toolchain_identity_is_portable_and_hash_significant(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Checks actual installed runtime version accessors and independently mutates each toolchain string under a recalculated complete hash; all six toolchain identities are hash-significant.

Direct assertions:


```python
assert profile.sqlite_version == sqlite3.sqlite_version

assert profile.pyogrio_version == pyogrio.__version__

assert profile.gdal_version == pyogrio.__gdal_version_string__

assert profile.shapely_version == shapely.__version__

assert profile.geos_version == shapely.geos_version_string

assert (
            changed.complete_geometry_profile_content_sha256
            != profile.complete_geometry_profile_content_sha256
        )
```

### `test_embedded_iso_wkb_framing_is_exact_and_no_ewkb_is_accepted`


```python
@pytest.mark.parametrize(
    "embedded",
    [
        _point_wkb() + b"trailing",
        _point_wkb()[:-1],
        b"\x02" + _point_wkb()[1:],
        struct.pack("<BI", 1, 8),
        struct.pack("<BI", 1, 4001) + struct.pack("<2d", 1, 2),
        struct.pack("<BI", 1, 0x20000001) + struct.pack("<I2d", 2154, 1, 2),
        struct.pack("<BI", 1, 0x80000001) + struct.pack("<3d", 1, 2, 3),
        struct.pack("<BII", 1, 2, 3) + struct.pack("<2d", 1, 2),
        struct.pack("<BII", 1, 7, 2) + _point_wkb(),
    ],
)
def test_embedded_iso_wkb_framing_is_exact_and_no_ewkb_is_accepted(
    embedded: bytes,
) -> None:
```

Constructs explicit trailing/truncated WKB, invalid endian/type/dimensional words, EWKB SRID/Z flag forms, and impossible coordinate/member lengths; only exact fully consumed core ISO WKB may enter the parser.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_embedded_measure_cannot_be_silently_lost_by_parser`


```python
def test_embedded_measure_cannot_be_silently_lost_by_parser(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Supplementary adversarial seam replaces the parser result with an XY Point for actual measured raw WKB; the declared-versus-parsed check must reject lost M. This mock supplements and does not replace permanent real M/ZM regressions.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(shapely, "from_wkb", lambda *a, **k: Point(1, 2))
```

### `test_all_core_geometry_families_preserve_complete_type_and_coordinate_evidence`


```python
@pytest.mark.parametrize(
    "wkt",
    [
        "LINESTRING (0 0, 1 2)",
        "MULTIPOINT ((0 0), (1 2))",
        "MULTILINESTRING ((0 0, 1 2), (3 4, 5 6))",
        "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))",
        "GEOMETRYCOLLECTION (POINT (1 2), LINESTRING (0 0, 3 4))",
        "GEOMETRYCOLLECTION M (POINT M (1 2 4), LINESTRING M (0 0 5, 3 4 6))",
    ],
)
def test_all_core_geometry_families_preserve_complete_type_and_coordinate_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, wkt: str
) -> None:
```

Exercises real LineString, multipart point/line/polygon, ordinary GeometryCollection, and measured GeometryCollection BLOBs; preserves source type, total coordinates, and actual Z/M evidence.

Direct assertions:


```python
assert layer.geometry_type_counts[0].geometry_type == expected.geom_type

assert layer.total_coordinate_count == len(shapely.get_coordinates(expected))

assert layer.has_z_geometry_count == int(shapely.has_z(expected))

assert layer.has_m_geometry_count == int(shapely.has_m(expected))
```

### `test_mixed_collection_absent_ordinates_are_not_source_nan`


```python
def test_mixed_collection_absent_ordinates_are_not_source_nan(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Constructs a raw collection containing one XYM and one XYZ point. Requires both dimensional-presence flags and two real coordinate records without mistaking absent child ordinates for source NaN.

Direct assertions:


```python
assert profile.layers[0].total_coordinate_count == 2

assert profile.layers[0].has_z_geometry_count == 1

assert profile.layers[0].has_m_geometry_count == 1
```

### `test_coordinated_catalog_hash_forgery_rejected_before_snapshot`


```python
def test_coordinated_catalog_hash_forgery_rejected_before_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Changes physical catalog bounds and recalculates the catalog hash, then makes geometry snapshot opening fatal; independent catalog authority must reject the coordinated forgery before geometry reads.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("geometry snapshot opened"),
    )
```

### `test_stale_source_or_catalog_rejected_before_snapshot`


```python
@pytest.mark.parametrize("mutation", ["schema", "archive", "package"])
def test_stale_source_or_catalog_rejected_before_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
```

Downgrades/recalculates catalog schema or mutates actual archive/package bytes while making snapshot opening fatal; stale source evidence must be rejected before geometry materialization.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("geometry snapshot opened"),
    )
```

### `test_intrinsic_accepts_valid_nested_package_paths`


```python
@pytest.mark.parametrize("relative_path", ["EP/subdir/a.gpkg", "EP/subdir/a.GPKG"])
def test_intrinsic_accepts_valid_nested_package_paths(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, relative_path: str
) -> None:
```

Accepts canonical nested lowercase/uppercase GeoPackage suffix paths unchanged under the shared intrinsic path grammar; this is a positive intrinsic control, not a physical-path authorization.

Direct assertions:


```python
assert geometry._validate_profile_intrinsic(changed) is changed
```

### `test_intrinsic_package_grouping_and_identity_collisions_fail`


```python
@pytest.mark.parametrize(
    "mutation",
    [
        "repeated-path",
        "casefold-path",
        "nfkc-path",
        "path-order",
        "repeated-size",
        "repeated-sha",
        "layer-order",
        "duplicate-layer",
        "casefold-layer",
        "nfkc-layer",
        "noncontiguous",
    ],
)
def test_intrinsic_package_grouping_and_identity_collisions_fail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
```

Uses a real two-layer source, then rehashes exact/casefold/NFKC path or layer collisions, nonlexical paths, inconsistent repeated size/SHA, layer gaps, and noncontiguous groups; rejects structural contradictions independently of source rows.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_intrinsic_domain_scalar_types_and_frequencies_are_exact`


```python
@pytest.mark.parametrize(
    ("domain", "changes"),
    [
        ("geometry_type_counts", {"geometry_type": "Unsupported"}),
        ("geometry_type_counts", {"count": True}),
        ("coordinate_dimension_counts", {"coordinate_dimension": True}),
        ("coordinate_dimension_counts", {"has_z": 0}),
        ("coordinate_dimension_counts", {"has_m": 0}),
        ("coordinate_dimension_counts", {"coordinate_dimension": 4}),
        ("validity_reason_counts", {"is_valid": 1}),
        ("validity_reason_counts", {"reason": _StringSubclass("Valid Geometry")}),
        ("validity_reason_counts", {"count": 0}),
    ],
)
def test_intrinsic_domain_scalar_types_and_frequencies_are_exact(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    domain: str,
    changes: dict[str, object],
) -> None:
```

Rehashes unsupported type names, Boolean counts/dimensions, integer pseudo-Booleans, impossible dimension flags, subclass reasons, and zero frequencies; every domain scalar is validated by exact type and value.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_empty_layer_component_hashes_are_reconstructed_intrinsically`


```python
@pytest.mark.parametrize(
    "component",
    [
        "fid_sequence_sha256",
        "raw_geometry_blob_content_sha256",
        "geometry_content_sha256",
    ],
)
def test_empty_layer_component_hashes_are_reconstructed_intrinsically(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, component: str
) -> None:
```

Changes each zero-row FID/raw/parser component digest under a recalculated complete hash; unlike non-empty content, deterministic empty hashes must be rejected intrinsically without geometry rows.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_parser_stream_hash_matches_independent_complete_row_encoding`


```python
def test_parser_stream_hash_matches_independent_complete_row_encoding(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Independently encodes sorted NULL, EMPTY ZM, and NON_EMPTY M rows with exact nine-field parser payloads and exact raw full-BLOB SHA rows; both production component hashes must match those separately computed arrays.

Direct assertions:


```python
assert profile.layers[0].geometry_content_sha256 == _json_hash(expected_rows)

assert profile.layers[0].raw_geometry_blob_content_sha256 == _json_hash(
        [
            [2, None],
            [7, sha256(_blob(empty, empty=True)).hexdigest()],
            [99, sha256(_blob(measured)).hexdigest()],
        ]
    )
```

### `test_parser_serialization_uses_every_explicit_contract_option`


```python
def test_parser_serialization_uses_every_explicit_contract_option(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Wraps real Shapely serialization for a measured source point and requires every exact encoding option, including actual dimension 3, little-endian, no SRID, extended flavor, and hex output.

Direct assertions:


```python
assert options == [
        {
            "hex": True,
            "output_dimension": 3,
            "byte_order": 1,
            "include_srid": False,
            "flavor": "extended",
        }
    ]
```

Monkeypatch expressions:


```python
monkeypatch.setattr(shapely, "to_wkb", recorded)
```

### `test_parser_serialization_uses_every_explicit_contract_option.recorded`


```python
def recorded(value: object, **kwargs: object) -> object:
```

Records serialization keyword arguments and delegates to the original real Shapely serializer without changing geometry.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_intrinsic_catalog_bounds_follow_physical_feature_count`


```python
@pytest.mark.parametrize("empty", [False, True])
def test_intrinsic_catalog_bounds_follow_physical_feature_count(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, empty: bool
) -> None:
```

Supplies non-null catalog bounds for an empty layer or missing catalog bounds for a populated layer and coherently sets DIFFERENT; intrinsic reuse of the physical catalog rule must still reject both.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_sqlite_close_failures_are_controlled_and_chained`


```python
@pytest.mark.parametrize(
    "error_type", [sqlite3.DatabaseError, OverflowError, TypeError, ValueError]
)
def test_sqlite_close_failures_are_controlled_and_chained(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, error_type: type[Exception]
) -> None:
```

Closes a real snapshot through a Connection subclass that raises database/overflow/type/value errors afterward; the context must translate each closure failure with the original cause.

Direct assertions:


```python
assert isinstance(captured.value.__cause__, error_type)
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(
        geometry.sqlite3,
        "connect",
        lambda *a, **k: original(*a, factory=CloseFailure, **k),
    )
```

### `test_sqlite_close_failures_are_controlled_and_chained.CloseFailure.close`


```python
def close(self) -> None:
```

Closes the real connection first, then raises the parametrized controlled fixture failure to isolate cleanup-error translation.

Direct raise statements:


```python
raise error_type("controlled close failure")
```

### `test_exact_and_different_bounds_are_evidence_without_tolerance`


```python
def test_exact_and_different_bounds_are_evidence_without_tolerance(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Builds one exact matching point-bounds case and one catalog/observed mismatch; preserves both raw tuples and records EXACT_MATCH versus DIFFERENT without tolerance.

Direct assertions:


```python
assert (
        exact.catalog_total_bounds
        == exact.observed_total_bounds
        == (1.0, 2.0, 1.0, 2.0)
    )

assert exact.bounds_relation == "EXACT_MATCH"

assert different.catalog_total_bounds != different.observed_total_bounds

assert different.bounds_relation == "DIFFERENT"
```

### `test_quoted_source_table_name_cannot_inject_sql`


```python
def test_quoted_source_table_name_cannot_inject_sql(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Builds an actual feature table whose spelling contains quotes and a DROP TABLE-looking fragment; exact quoted lookup/projection must safely preserve the name and every row.

Direct assertions:


```python
assert profile.layers[0].layer_name == layer_name

assert profile.geometry_row_count == 2
```

### `test_type_contract_metadata_rejects_noncanonical_declared_geometry_type`


```python
@pytest.mark.parametrize("declared_type", INVALID_DECLARED_TYPES)
def test_type_contract_metadata_rejects_noncanonical_declared_geometry_type(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, declared_type: str
) -> None:
```

Mutates the real serialized SQLite gpkg_geometry_columns declaration to each invalid value while retaining a separately built catalog. The private metadata boundary must reject all six lowercase/edge-whitespace/unknown/extended declarations in a verified query-only SQLite snapshot; this isolates metadata validation rather than a prior catalog rejection.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_type_contract_metadata_rejects_different_sql_geometry_column_type`


```python
@pytest.mark.parametrize("sql_type", ["GEOMETRY", "BLOB", "LINESTRING", "point"])
def test_type_contract_metadata_rejects_different_sql_geometry_column_type(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, sql_type: str
) -> None:
```

Rebuilds a real physical SQLite table with one INTEGER PRIMARY KEY and the parametrized quoted SQL geometry type while declaring POINT in gpkg_geometry_columns. It first asserts PRAGMA table_info retained the exact test spelling, including lowercase point, then requires the private metadata boundary to reject all four mismatches. No casefold or normalization can satisfy SQL/declaration equality.

Direct assertions:


```python
assert (
            connection.execute("PRAGMA table_info(physical_layer)").fetchall()[1][2]
            == sql_type
        )
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_type_contract_sql_declared_type_requires_exact_runtime_spelling`


```python
@pytest.mark.parametrize("sql_type", [_StringSubclass("POINT"), None, 1])
def test_type_contract_sql_declared_type_requires_exact_runtime_spelling(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, sql_type: object
) -> None:
```

Uses a valid physical POINT container and alters only the table_info result seam to inject a comparison-equal string subclass, None, or integer SQL declared type. The metadata reader must reject all three impossible/non-exact runtime values; real SQLite normally returns built-in strings, so this narrow seam tests fail-closed DB-API handling.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(geometry, "_sqlite_rows", altered)
```

### `test_type_contract_sql_declared_type_requires_exact_runtime_spelling.altered`


```python
def altered(
        connection: sqlite3.Connection,
        statement: str,
        parameters: tuple[object, ...] = (),
    ) -> tuple[tuple[object, ...], ...]:
```

Delegates every real SQLite query and replaces only the geom column's declared SQL-type slot in PRAGMA main.table_info rows. All other metadata values and statements remain unchanged, isolating the SQL-type exact-runtime contract.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_type_contract_rejects_unassignable_root_wkb_family`


```python
@pytest.mark.parametrize(
    ("declared_type", "wkt"),
    [
        ("POINT", "LINESTRING (0 0, 1 2)"),
        ("LINESTRING", "POINT (1 2)"),
        ("POLYGON", "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))"),
        ("MULTIPOLYGON", "POLYGON ((0 0, 2 0, 2 2, 0 0))"),
        ("MULTIPOINT", "POINT (1 2)"),
        ("MULTILINESTRING", "LINESTRING (0 0, 1 2)"),
        ("GEOMETRYCOLLECTION", "POINT (1 2)"),
        ("POINT", "LINESTRING EMPTY"),
    ],
)
def test_type_contract_rejects_unassignable_root_wkb_family(
    declared_type: str, wkt: str
) -> None:
```

Passes real typed ISO WKB inside Standard GeoPackageBinary to the actual parser with eight contradictory specific declarations. The cases cover each concrete family plus a POINT declaration with LINESTRING EMPTY; EMPTY cannot evade the root assignability check.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_type_contract_accepts_matching_core_roots_and_geometry_supertype`


```python
@pytest.mark.parametrize(("declared_type", "observed_type", "wkt"), CORE_TYPE_CASES)
@pytest.mark.parametrize("use_supertype", [False, True])
def test_type_contract_accepts_matching_core_roots_and_geometry_supertype(
    declared_type: str, observed_type: str, wkt: str, use_supertype: bool
) -> None:
```

Runs all seven real core WKB families twice: once under their matching specific declaration and once under GEOMETRY. The 14 controls assert the exact real Shapely root family; GEOMETRYCOLLECTION accepts a collection root, not an arbitrary noncollection root.

Direct assertions:


```python
assert parsed.geometry.geom_type == observed_type
```

### `test_type_contract_point_null_and_empty_source_controls`


```python
@pytest.mark.parametrize("blob", [None, _wkt_blob("POINT EMPTY")])
def test_type_contract_point_null_and_empty_source_controls(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, blob: bytes | None
) -> None:
```

Builds complete source-bound POINT profiles for SQLite NULL and POINT EMPTY. It requires exact POINT metadata and separate NULL/EMPTY counts, with an empty observed-type domain only for NULL and Point retained for EMPTY.

Direct assertions:


```python
assert layer.gpkg_geometry_type_name == "POINT"

assert layer.null_geometry_count == int(blob is None)

assert layer.empty_geometry_count == int(blob is not None)

assert tuple(item.geometry_type for item in layer.geometry_type_counts) == (
        () if blob is None else ("Point",)
    )
```

### `test_type_contract_point_assignability_preserves_xy_z_m_zm`


```python
@pytest.mark.parametrize(("has_z", "has_m", "coordinates"), DIMENSIONS)
@pytest.mark.parametrize("empty", [False, True])
def test_type_contract_point_assignability_preserves_xy_z_m_zm(
    has_z: bool, has_m: bool, coordinates: tuple[float, ...], empty: bool
) -> None:
```

Constructs raw independent point WKB for all four XY/Z/M/ZM layouts, both populated and NaN-encoded EMPTY, under declared POINT. All eight real-parser controls require unchanged Point identity, Z/M flags, and empty state; dimension does not substitute another family.

Direct assertions:


```python
assert parsed.geometry.geom_type == "Point"

assert bool(shapely.has_z(parsed.geometry)) is has_z

assert bool(shapely.has_m(parsed.geometry)) is has_m

assert bool(shapely.is_empty(parsed.geometry)) is empty
```

### `test_type_contract_intrinsic_rejects_invalid_declaration_even_null_only`


```python
@pytest.mark.parametrize("declared_type", INVALID_DECLARED_TYPES)
def test_type_contract_intrinsic_rejects_invalid_declaration_even_null_only(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, declared_type: str
) -> None:
```

Builds a valid NULL-only source profile, substitutes each invalid declaration, and recalculates its complete profile SHA. The observed domain remains explicitly empty; intrinsic validation must still reject all six malformed/unsupported declarations before physical rebuilding.

Direct assertions:


```python
assert forged.layers[0].geometry_type_counts == ()
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

### `test_type_contract_intrinsic_rejects_rehashed_declared_observed_mismatch`


```python
@pytest.mark.parametrize(
    ("declared_type", "wkt"),
    [
        ("POINT", "LINESTRING (0 0, 1 2)"),
        ("POLYGON", "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))"),
        ("MULTIPOLYGON", "POLYGON ((0 0, 2 0, 2 2, 0 0))"),
    ],
)
def test_type_contract_intrinsic_rejects_rehashed_declared_observed_mismatch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, declared_type: str, wkt: str
) -> None:
```

Builds real source profiles containing LineString, MultiPolygon, or Polygon, changes only the retained GeoPackage declaration to an incompatible specific family, and recalculates the complete hash. It explicitly proves the hash is coherent, then requires the intrinsic profile boundary itself to reject each declaration/domain contradiction.

Direct assertions:


```python
assert (
        forged.complete_geometry_profile_content_sha256
        == geometry._profile_content_sha256(forged)
    )
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasGeometryProfileError)
```

## 5. Hash and mutation proof boundaries

### STEP 7F.1B.3.1 direct type-contract cases

| Contract layer | Collected new cases |
|---|---:|
| Invalid GeoPackage metadata declaration | 6 |
| Physical SQL declaration mismatch | 4 |
| Non-exact SQL declaration runtime values | 3 |
| Specific root-family mismatch, including typed EMPTY | 8 |
| Matching concrete root | 7 |
| GEOMETRY supertype root | 7 |
| Source-bound POINT NULL/EMPTY | 2 |
| POINT XY/Z/M/ZM, populated and EMPTY | 8 |
| Intrinsic invalid NULL-only declaration after rehash | 6 |
| Intrinsic declaration/domain mismatch after rehash | 3 |
| Total | 54 |

Red-first execution against unchanged production at `57edf93611d028092450a58de1b6df73bc6a1ee2` showed 28 failures and 26 passing controls, with the original 273 cases deselected. Subsequent fixture-only adjustments keep the same 54 cases and avoid unrelated metadata warnings. Five existing invalid-primary-key fixture declarations use `geom GEOMETRY` instead of `geom BLOB` so the new SQL-type gate does not mask their intended primary-key regressions. No existing case is removed.

Expected FID/raw-BLOB hashes use an independently implemented canonical JSON helper. Component-forgery tests recalculate the complete profile hash so a stale outer digest does not substitute for the intended physical rejection. Raw header-byte changes are distinguished from parser geometry changes; M-only, Z-only, coordinate, FID, and ring-structure changes remain hash-significant in their correct streams. Portable roots/cache-hit state and repeated builds must produce exact equal public evidence.

Temporary package replacements occur after real SQLite deserialization and explicitly assert the hook ran; restoring the physical path cannot inject alternate geometry, whereas persistent mutation must fail final source checks. Fatal reader/repair/reprojection sentinels fail immediately on forbidden operations. Impossible SQLite DB-API row shapes are tested at the narrow row-fetch seam because real INTEGER PRIMARY KEY rowid aliases cannot naturally return Boolean/float/NumPy identifiers.

## 6. Execution and non-goals

Run this suite with a fresh unique `--basetemp` under `%LOCALAPPDATA%\LandScout\pytest-runs`. The existing 399-case INPN baseline remains required, followed by this geometry suite, combined INPN suites, and the complete repository; exact completed commands and full-suite results are recorded in docs/DEV_LOG.md. The geometry suite passes all 327 cases (273 retained + 54 type-contract regressions), and the combined INPN suites pass all 726 cases; both focused runs report zero unhandled warnings. One all-NULL mandatory Z/M Point metadata fixture explicitly captures eight expected Pyogrio measured-metadata warnings; this does not permit lossy geometry-row conversion. Unit fixtures do not constitute verification of the real EP snapshot. The separately controlled real-source run blocks network, alternative feature readers, attribute projections, geometry repair, and reprojection.

No test adds category/legal semantics, environmental normalization, parcel loading/relations/distances, exclusion, score, ranking, Natura 2000, or ZNIEFF. No fixture archive/GeoPackage/cache or audit dump is committed.

## 7. Exact complete current file content


```python
from __future__ import annotations

import io
import json
import math
import sqlite3
import struct
import zipfile
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, fields, is_dataclass, replace
from hashlib import sha256
from pathlib import Path
from typing import Any, ClassVar

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pyogrio  # type: ignore[import-untyped]
import pytest
import shapely  # type: ignore[import-untyped]
import yaml
from shapely.geometry import Point  # type: ignore[import-untyped]

from landscout import sources
from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module
from landscout.sources import inpn_protected_areas_fr as source_module
from landscout.sources import inpn_protected_areas_geometry_fr as geometry
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)
from landscout.sources.inpn_protected_areas_geometry_fr import (
    InpnProtectedAreasGeometryProfile,
    InpnProtectedAreasGeometryProfileError,
    build_inpn_protected_areas_geometry_profile,
    validate_inpn_protected_areas_geometry_profile,
)

CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
EXPECTED_EXPORTS = {
    "InpnProtectedAreasGeometryTypeCount",
    "InpnProtectedAreasCoordinateDimensionCount",
    "InpnProtectedAreasGeometryValidityReasonCount",
    "InpnProtectedAreasLayerGeometryProfile",
    "InpnProtectedAreasGeometryProfile",
    "InpnProtectedAreasGeometryProfileError",
    "build_inpn_protected_areas_geometry_profile",
    "validate_inpn_protected_areas_geometry_profile",
}
DIMENSIONS = (
    (False, False, (1.0, 2.0)),
    (True, False, (1.0, 2.0, 3.0)),
    (False, True, (1.0, 2.0, 4.0)),
    (True, True, (1.0, 2.0, 3.0, 4.0)),
)
CORE_TYPE_CASES = (
    ("POINT", "Point", "POINT (1 2)"),
    ("LINESTRING", "LineString", "LINESTRING (0 0, 1 2)"),
    ("POLYGON", "Polygon", "POLYGON ((0 0, 2 0, 2 2, 0 0))"),
    ("MULTIPOINT", "MultiPoint", "MULTIPOINT ((1 2), (3 4))"),
    ("MULTILINESTRING", "MultiLineString", "MULTILINESTRING ((0 0, 1 2))"),
    ("MULTIPOLYGON", "MultiPolygon", "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))"),
    ("GEOMETRYCOLLECTION", "GeometryCollection", "GEOMETRYCOLLECTION (POINT (1 2))"),
)
INVALID_DECLARED_TYPES = (
    "point",
    " Point",
    "POINT ",
    "UNKNOWN",
    "NOT_A_TYPE",
    "CURVEPOLYGON",
)


class _Response(io.BytesIO):
    headers: ClassVar[dict[str, str]] = {"Content-Type": "application/zip"}


class _StringSubclass(str):
    pass


class _BytesSubclass(bytes):
    pass


@contextmanager
def _response(payload: bytes) -> Iterator[_Response]:
    with _Response(payload) as response:
        yield response


def _json_hash(value: object) -> str:
    return sha256(
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _point_wkb(
    coordinates: tuple[float, ...] = (1.0, 2.0),
    *,
    has_z: bool = False,
    has_m: bool = False,
    little_endian: bool = True,
) -> bytes:
    # ISO dimensional type words and ordinates are built independently of Shapely.
    endian = "<" if little_endian else ">"
    type_word = 1 + 1000 * int(has_z) + 2000 * int(has_m)
    return struct.pack(
        f"{endian}BI{len(coordinates)}d", int(little_endian), type_word, *coordinates
    )


def _blob(
    wkb: bytes | None = None,
    *,
    srs_id: int = 2154,
    little_endian: bool = True,
    empty: bool = False,
    envelope_code: int = 0,
) -> bytes:
    embedded = _point_wkb() if wkb is None else wkb
    endian = "<" if little_endian else ">"
    size = (0, 4, 6, 6, 8)[envelope_code]
    flags = int(little_endian) | envelope_code << 1 | int(empty) << 4
    envelope = (1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0)[:size]
    return (
        b"GP\x00"
        + bytes([flags])
        + struct.pack(f"{endian}i{size}d", srs_id, *envelope)
        + embedded
    )


def _wkt_blob(wkt: str) -> bytes:
    parsed = shapely.from_wkt(wkt)
    wkb = shapely.to_wkb(parsed, byte_order=1, output_dimension=4, flavor="iso")
    return _blob(wkb, empty=bool(shapely.is_empty(parsed)))


def _metadata(**changes: object) -> Any:
    values = {
        "table_name": "physical_layer",
        "table_kind": "table",
        "fid_column_name": "fid",
        "geometry_column_name": "geom",
        "geometry_type_name": "GEOMETRY",
        "srs_id": 2154,
        "z_flag": 2,
        "m_flag": 2,
    }
    values.update(changes)
    return geometry._GpkgLayerMetadata(**values)


def _gpkg_bytes(
    tmp_path: Path,
    rows: tuple[tuple[int, bytes | None], ...] | None = None,
    *,
    layer_names: tuple[str, ...] = ("physical_layer",),
    z_flag: int = 2,
    m_flag: int = 2,
    geometry_type: str = "Unknown",
) -> bytes:
    # Pyogrio creates ONLY an ordinary XY container. Every tested geometry BLOB
    # is installed through SQLite; M/ZM never pass through Pyogrio conversion.
    selected = (
        ((1, _blob()), (7, _blob(_point_wkb((3.0, 5.0))))) if rows is None else rows
    )
    tmp_path.mkdir(parents=True, exist_ok=True)
    path = tmp_path / "fixture.gpkg"
    frame = gpd.GeoDataFrame(
        {"never_read_attribute": ["secret source text"]},
        geometry=[Point(1, 2)],
        crs="EPSG:2154",
    )
    for position, layer_name in enumerate(layer_names):
        pyogrio.write_dataframe(
            frame,
            path,
            layer=layer_name,
            driver="GPKG",
            geometry_type=geometry_type,
            append=position > 0,
            layer_options={"SPATIAL_INDEX": "NO"},
        )
    connection = sqlite3.connect(":memory:")
    try:
        connection.deserialize(path.read_bytes())
        for layer_name in layer_names:
            quoted = '"' + layer_name.replace('"', '""') + '"'
            connection.execute(f"DELETE FROM {quoted}")
            connection.executemany(
                f'INSERT INTO {quoted} ("fid", "geom", "never_read_attribute") '
                "VALUES (?, ?, ?)",
                [(fid, blob, "never select this value") for fid, blob in selected],
            )
            connection.execute(
                "UPDATE gpkg_geometry_columns SET geometry_type_name = ?, z = ?, m = ? "
                "WHERE table_name = ?",
                (
                    "GEOMETRY" if geometry_type == "Unknown" else geometry_type.upper(),
                    z_flag,
                    m_flag,
                    layer_name,
                ),
            )
            if not selected:
                connection.execute(
                    "UPDATE gpkg_contents SET min_x=NULL, min_y=NULL, max_x=NULL, "
                    "max_y=NULL WHERE table_name=?",
                    (layer_name,),
                )
        connection.commit()
        return connection.serialize()
    finally:
        connection.close()


def _source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    package: bytes | None = None,
    *,
    files: Mapping[str, bytes] | None = None,
) -> tuple[
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasCatalog,
]:
    members = files or {"EP/one.gpkg": package or _gpkg_bytes(tmp_path / "container")}
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, payload in members.items():
            archive.writestr(zipfile.ZipInfo(name, (2026, 7, 1, 0, 0, 0)), payload)
    archive_bytes = stream.getvalue()
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    payload["cache_root"] = str(tmp_path / "cache")
    payload["expected_archive_size_bytes"] = len(archive_bytes)
    payload["expected_archive_sha256"] = sha256(archive_bytes).hexdigest()
    config = InpnProtectedAreasSourceConfig.model_validate(payload)
    monkeypatch.setattr(
        source_module, "open_safe_https", lambda *a, **k: _response(archive_bytes)
    )
    download = download_inpn_protected_areas_archive(config)
    extraction = extract_inpn_protected_areas_archive(download, config)
    return config, extraction, build_inpn_protected_areas_catalog(extraction, config)


def _build(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    rows: tuple[tuple[int, bytes | None], ...] | None = None,
    **options: Any,
) -> InpnProtectedAreasGeometryProfile:
    package = _gpkg_bytes(tmp_path / "container", rows, **options)
    config, extraction, catalog = _source(tmp_path, monkeypatch, package)
    return build_inpn_protected_areas_geometry_profile(extraction, config, catalog)


def _rehash(
    profile: InpnProtectedAreasGeometryProfile,
) -> InpnProtectedAreasGeometryProfile:
    blank = replace(profile, complete_geometry_profile_content_sha256="")
    return replace(
        blank,
        complete_geometry_profile_content_sha256=geometry._profile_content_sha256(
            blank
        ),
    )


@pytest.mark.parametrize(("has_z", "has_m", "coordinates"), DIMENSIONS)
@pytest.mark.parametrize("empty", [False, True])
def test_raw_sqlite_point_dimensions_and_empty_roundtrip_are_lossless(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    has_z: bool,
    has_m: bool,
    coordinates: tuple[float, ...],
    empty: bool,
) -> None:
    values = tuple(math.nan for _ in coordinates) if empty else coordinates
    blob = _blob(_point_wkb(values, has_z=has_z, has_m=has_m), empty=empty)
    package = _gpkg_bytes(tmp_path / "container", ((11, blob),))
    config, extraction, catalog = _source(tmp_path, monkeypatch, package)
    with geometry._open_gpkg_sqlite_snapshot(package, "EP/one.gpkg") as connection:
        metadata = geometry._read_gpkg_layer_metadata(
            connection, "EP/one.gpkg", catalog.packages[0].layers[0]
        )
        rows = geometry._read_gpkg_geometry_rows(connection, metadata, "EP/one.gpkg", 1)
    assert rows == ((11, blob),)
    parsed = geometry._parse_gpkg_geometry_blob(rows[0][1], metadata, "EP/one.gpkg", 11)
    assert parsed.embedded_wkb == blob[8:]
    actual = parsed.geometry
    assert bool(shapely.has_z(actual)) is has_z
    assert bool(shapely.has_m(actual)) is has_m
    assert int(shapely.get_coordinate_dimension(actual)) == len(coordinates)
    assert bool(shapely.is_empty(actual)) is empty
    extracted = shapely.get_coordinates(actual, include_z=has_z, include_m=has_m)
    assert extracted.tolist() == ([] if empty else [list(coordinates)])
    canonical = shapely.to_wkb(
        actual,
        hex=True,
        output_dimension=len(coordinates),
        byte_order=1,
        include_srid=False,
        flavor="extended",
    )
    roundtrip = shapely.from_wkb(canonical, on_invalid="raise")
    assert bool(shapely.has_z(roundtrip)) is has_z
    assert bool(shapely.has_m(roundtrip)) is has_m
    assert int(shapely.get_coordinate_dimension(roundtrip)) == len(coordinates)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    layer = profile.layers[0]
    assert layer.empty_geometry_count == int(empty)
    assert layer.null_geometry_count == 0
    assert layer.has_z_geometry_count == int(has_z)
    assert layer.has_m_geometry_count == int(has_m)
    assert layer.total_coordinate_count == int(not empty)
    domain = layer.coordinate_dimension_counts[0]
    assert (domain.coordinate_dimension, domain.has_z, domain.has_m, domain.count) == (
        len(coordinates),
        has_z,
        has_m,
        1,
    )


@pytest.mark.parametrize("header_little", [False, True])
@pytest.mark.parametrize("wkb_little", [False, True])
@pytest.mark.parametrize("envelope_code", range(5))
def test_standard_header_endianness_and_every_envelope_code(
    header_little: bool, wkb_little: bool, envelope_code: int
) -> None:
    embedded = _point_wkb(little_endian=wkb_little)
    blob = _blob(embedded, little_endian=header_little, envelope_code=envelope_code)
    parsed = geometry._parse_gpkg_geometry_blob(blob, _metadata(), "EP/a.gpkg", 1)
    assert parsed.embedded_wkb == embedded
    assert parsed.header_little_endian is header_little
    assert parsed.envelope_code == envelope_code
    assert len(parsed.envelope) == (0, 4, 6, 6, 8)[envelope_code]
    assert shapely.get_coordinates(parsed.geometry).tolist() == [[1.0, 2.0]]


@pytest.mark.parametrize(
    "blob",
    [
        None,
        bytearray(_blob()),
        memoryview(_blob()),
        _BytesSubclass(_blob()),
        b"",
        b"GP\x00",
        b"XX" + _blob()[2:],
        _blob()[:2] + b"\x01" + _blob()[3:],
        _blob()[:3] + b"\x41" + _blob()[4:],
        _blob()[:3] + b"\x81" + _blob()[4:],
        _blob()[:3] + b"\x21" + _blob()[4:],
        *(_blob()[:3] + bytes([1 | code << 1]) + _blob()[4:] for code in (5, 6, 7)),
        _blob(envelope_code=4)[:30],
        _blob()[:8],
        _blob(b"not WKB"),
        _blob(srs_id=4326),
        _blob(empty=True),
        _blob(_point_wkb((math.nan, math.nan)), empty=False),
    ],
)
def test_malformed_geometry_blob_is_controlled(blob: object) -> None:
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._parse_gpkg_geometry_blob(blob, _metadata(), "EP/a.gpkg", 1)


@pytest.mark.parametrize(
    ("z_flag", "m_flag", "has_z", "has_m", "accepted"),
    [
        (0, 2, True, False, False),
        (1, 2, False, False, False),
        (2, 2, True, False, True),
        (2, 2, False, False, True),
        (2, 0, False, True, False),
        (2, 1, False, False, False),
        (2, 2, False, True, True),
        (1, 1, True, True, True),
    ],
)
@pytest.mark.parametrize("empty", [False, True])
def test_z_m_declarations_are_enforced(
    z_flag: int, m_flag: int, has_z: bool, has_m: bool, accepted: bool, empty: bool
) -> None:
    coordinates = (1.0, 2.0) + ((3.0,) if has_z else ()) + ((4.0,) if has_m else ())
    if empty:
        coordinates = tuple(math.nan for _ in coordinates)
    blob = _blob(_point_wkb(coordinates, has_z=has_z, has_m=has_m), empty=empty)
    metadata = _metadata(z_flag=z_flag, m_flag=m_flag)
    if accepted:
        geometry._parse_gpkg_geometry_blob(blob, metadata, "EP/a.gpkg", 1)
    else:
        with pytest.raises(InpnProtectedAreasGeometryProfileError):
            geometry._parse_gpkg_geometry_blob(blob, metadata, "EP/a.gpkg", 1)


@pytest.mark.parametrize(
    "value", [None, "", b"", "a\x00b", "a\x01b", "a\nb", _StringSubclass("name")]
)
def test_sql_identifier_rejects_noncanonical_runtime_values(value: object) -> None:
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._quote_sqlite_identifier(value)


def test_sql_identifier_preserves_spelling_and_escapes_quotes() -> None:
    value = 'layer"; DROP TABLE private; --'
    assert (
        geometry._quote_sqlite_identifier(value) == '"layer""; DROP TABLE private; --"'
    )


@pytest.mark.parametrize(
    "value", [None, b"", b"not sqlite", bytearray(b"sqlite"), _BytesSubclass(b"sqlite")]
)
def test_sqlite_snapshot_invalid_bytes_fail_controlled(value: object) -> None:
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError),
        geometry._open_gpkg_sqlite_snapshot(value, "EP/one.gpkg") as connection,
    ):
        connection.execute("SELECT name FROM sqlite_schema").fetchall()


def test_sqlite_snapshot_is_query_only_and_closes(tmp_path: Path) -> None:
    package = _gpkg_bytes(tmp_path)
    with geometry._open_gpkg_sqlite_snapshot(package, "EP/one.gpkg") as connection:
        assert connection.execute("PRAGMA query_only").fetchone() == (1,)
        if connection.execute("PRAGMA trusted_schema").fetchone() is not None:
            assert connection.execute("PRAGMA trusted_schema").fetchone() == (0,)
        with pytest.raises(sqlite3.OperationalError):
            connection.execute("CREATE TABLE forbidden (id INTEGER)")
    with pytest.raises(sqlite3.ProgrammingError):
        connection.execute("SELECT 1")


@pytest.mark.parametrize(
    "error_type",
    [
        sqlite3.DatabaseError,
        sqlite3.OperationalError,
        sqlite3.IntegrityError,
        OverflowError,
        TypeError,
        ValueError,
    ],
)
def test_sqlite_failures_are_translated_and_chained(
    tmp_path: Path, error_type: type[Exception]
) -> None:
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError) as captured,
        geometry._open_gpkg_sqlite_snapshot(_gpkg_bytes(tmp_path), "EP/a.gpkg"),
    ):
        raise error_type("deliberate SQLite boundary failure")
    assert isinstance(captured.value.__cause__, error_type)


def test_source_complete_profile_and_physical_validation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    validate_inpn_protected_areas_geometry_profile(extraction, config, catalog, profile)
    assert type(profile) is InpnProtectedAreasGeometryProfile
    assert (
        profile.geometry_profile_schema_version
        == geometry.GEOMETRY_PROFILE_SCHEMA_VERSION
        == 1
    )
    assert profile.source_catalog_schema_version == 2
    assert (
        profile.source_catalog_content_sha256 == catalog.complete_catalog_content_sha256
    )
    assert profile.archive_sha256 == config.expected_archive_sha256
    assert profile.package_count == profile.layer_count == 1
    assert profile.geometry_row_count == 2
    assert profile.valid_non_empty_geometry_count == 2
    assert (
        profile.null_geometry_count
        == profile.empty_geometry_count
        == profile.invalid_non_empty_geometry_count
        == 0
    )
    assert profile.layers[0].fid_sequence_sha256 == _json_hash([1, 7])
    assert profile.layers[0].observed_total_bounds == (1.0, 2.0, 3.0, 5.0)
    assert len(profile.complete_geometry_profile_content_sha256) == 64


def test_only_fid_geometry_sql_and_no_feature_reader(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    traces: list[str] = []
    original = geometry._open_gpkg_sqlite_snapshot

    @contextmanager
    def traced(payload: bytes, relative_path: str) -> Any:
        with original(payload, relative_path) as connection:
            assert connection.execute("PRAGMA query_only").fetchone() == (1,)
            connection.set_trace_callback(traces.append)
            yield connection

    def forbidden(*args: object, **kwargs: object) -> Any:
        raise AssertionError("Forbidden feature reader or geometry modification")

    monkeypatch.setattr(geometry, "_open_gpkg_sqlite_snapshot", traced)
    for owner, names in (
        (pyogrio, ("read_dataframe", "read_arrow", "open_arrow", "read_bounds")),
        (gpd, ("read_file", "read_parquet")),
        (
            shapely,
            (
                "make_valid",
                "buffer",
                "normalize",
                "set_precision",
                "simplify",
                "snap",
                "union",
                "intersection",
            ),
        ),
    ):
        for name in names:
            monkeypatch.setattr(owner, name, forbidden)
    monkeypatch.setattr(gpd.GeoDataFrame, "to_crs", forbidden)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    feature_queries = [query for query in traces if 'FROM "physical_layer"' in query]
    assert feature_queries == ['SELECT "fid", "geom" FROM "physical_layer"']
    assert all(
        "never_read_attribute" not in query and "SELECT *" not in query
        for query in traces
    )
    assert profile.geometry_row_count == 2


def test_deserialize_uses_exact_bytes_once_per_package_for_all_layers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _gpkg_bytes(tmp_path / "first", layer_names=("first", "second"))
    second = _gpkg_bytes(tmp_path / "second", layer_names=("third",))
    config, extraction, catalog = _source(
        tmp_path / "source",
        monkeypatch,
        files={"EP/a.gpkg": first, "EP/z.gpkg": second},
    )
    original_connect = sqlite3.connect
    inputs: list[bytes] = []
    calls: list[tuple[object, ...]] = []

    class RecordedConnection(sqlite3.Connection):
        def deserialize(self, data: bytes, *, name: str = "main") -> None:
            assert type(data) is bytes
            inputs.append(data)
            super().deserialize(data, name=name)

    def connect(*args: Any, **kwargs: Any) -> Any:
        calls.append(args)
        assert args == (":memory:",)
        return original_connect(*args, factory=RecordedConnection, **kwargs)

    monkeypatch.setattr(geometry.sqlite3, "connect", connect)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    assert inputs == [first, second]
    assert inputs[0] is not inputs[1]
    assert len(calls) == 2
    assert profile.package_count == 2 and profile.layer_count == 3


def test_null_empty_and_invalid_are_separate_factual_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    invalid = "POLYGON ((0 0, 2 2, 0 2, 2 0, 0 0))"
    profile = _build(
        tmp_path,
        monkeypatch,
        ((1, None), (3, _wkt_blob("POINT EMPTY")), (9, _wkt_blob(invalid))),
    )
    layer = profile.layers[0]
    assert (
        layer.null_geometry_count,
        layer.empty_geometry_count,
        layer.non_empty_geometry_count,
    ) == (1, 1, 1)
    assert layer.valid_non_empty_geometry_count == 0
    assert layer.invalid_non_empty_geometry_count == 1
    reason = layer.validity_reason_counts[0]
    assert reason.is_valid is False
    assert reason.reason == shapely.is_valid_reason(shapely.from_wkt(invalid))
    assert reason.count == 1
    assert layer.total_coordinate_count == 5
    assert layer.observed_total_bounds == (0.0, 0.0, 2.0, 2.0)


def test_null_does_not_violate_mandatory_z_m_flags(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    with pytest.warns(
        UserWarning, match=r"Measured \(M\) geometry types are not supported"
    ) as captured:
        profile = _build(
            tmp_path,
            monkeypatch,
            ((1, None),),
            z_flag=1,
            m_flag=1,
            geometry_type="Point",
        )
    # These metadata-only warnings are expected: no geometry row uses Pyogrio.
    assert len(captured) == 8
    assert profile.null_geometry_count == 1
    assert profile.has_z_geometry_count == profile.has_m_geometry_count == 0


def test_empty_feature_table_has_null_bounds_and_exact_empty_hashes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = _build(tmp_path, monkeypatch, ())
    layer = profile.layers[0]
    assert layer.fid_count == profile.geometry_row_count == 0
    assert layer.fid_min is layer.fid_max is None
    assert layer.observed_total_bounds is layer.catalog_total_bounds is None
    assert layer.bounds_relation == "BOTH_NULL"
    assert (
        layer.geometry_type_counts
        == layer.coordinate_dimension_counts
        == layer.validity_reason_counts
        == ()
    )
    assert (
        layer.fid_sequence_sha256
        == layer.geometry_content_sha256
        == layer.raw_geometry_blob_content_sha256
        == _json_hash([])
    )


@pytest.mark.parametrize("ordinate", [0, 1, 2, 3])
@pytest.mark.parametrize("bad", [math.nan, math.inf, -math.inf])
def test_nonfinite_present_xy_z_m_coordinates_fail_closed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, ordinate: int, bad: float
) -> None:
    values = [1.0, 2.0, 3.0, 4.0]
    values[ordinate] = bad
    blob = _blob(_point_wkb(tuple(values), has_z=True, has_m=True))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        _build(tmp_path, monkeypatch, ((1, blob),))


@pytest.mark.parametrize("argument", ["extraction", "config", "catalog"])
def test_wrong_public_inputs_fail_controlled(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, argument: str
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    values: dict[str, Any] = {
        "extraction": extraction,
        "config": config,
        "catalog": catalog,
    }
    values[argument] = object()
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        build_inpn_protected_areas_geometry_profile(**values)


def test_wrong_profile_type_rejected_before_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("snapshot opened"),
    )
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        validate_inpn_protected_areas_geometry_profile(
            extraction, config, catalog, object()
        )


def test_portable_roots_cache_hit_and_repeated_build_are_identical(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = _gpkg_bytes(tmp_path / "container")
    config_a, extraction_a, catalog_a = _source(tmp_path / "a", monkeypatch, package)
    config_b, extraction_b, catalog_b = _source(tmp_path / "b", monkeypatch, package)
    first = build_inpn_protected_areas_geometry_profile(
        extraction_a, config_a, catalog_a
    )
    assert (
        build_inpn_protected_areas_geometry_profile(extraction_a, config_a, catalog_a)
        == first
    )
    assert (
        build_inpn_protected_areas_geometry_profile(extraction_b, config_b, catalog_b)
        == first
    )
    cache_hit = replace(
        extraction_a,
        cache_hit=True,
        download=replace(extraction_a.download, cache_hit=True),
    )
    assert (
        build_inpn_protected_areas_geometry_profile(cache_hit, config_a, catalog_a)
        == first
    )


@pytest.mark.parametrize("mutation", ["x", "z", "m", "fid", "raw-header", "ring-order"])
def test_exact_raw_and_parser_hash_sensitivity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    first_blob = _blob(_point_wkb((1.0, 2.0, 3.0, 4.0), has_z=True, has_m=True))
    second_blob = first_blob
    second_fid = 1
    if mutation in {"x", "z", "m"}:
        coordinates = [1.0, 2.0, 3.0, 4.0]
        coordinates[{"x": 0, "z": 2, "m": 3}[mutation]] += 1
        second_blob = _blob(_point_wkb(tuple(coordinates), has_z=True, has_m=True))
    elif mutation == "fid":
        second_fid = 99
    elif mutation == "raw-header":
        second_blob = _blob(first_blob[8:], little_endian=False)
    else:
        first_blob = _wkt_blob("POLYGON ((0 0, 2 0, 2 2, 0 0))")
        second_blob = _wkt_blob("POLYGON ((0 0, 2 2, 2 0, 0 0))")
    first = _build(tmp_path / "a", monkeypatch, ((1, first_blob),)).layers[0]
    second = _build(tmp_path / "b", monkeypatch, ((second_fid, second_blob),)).layers[0]
    assert first.raw_geometry_blob_content_sha256 == _json_hash(
        [[1, sha256(first_blob).hexdigest()]]
    )
    assert second.raw_geometry_blob_content_sha256 == _json_hash(
        [[second_fid, sha256(second_blob).hexdigest()]]
    )
    assert (
        first.raw_geometry_blob_content_sha256
        != second.raw_geometry_blob_content_sha256
    )
    assert (first.geometry_content_sha256 == second.geometry_content_sha256) is (
        mutation == "raw-header"
    )


def test_unsorted_sparse_fids_are_sorted_without_renumbering(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = _build(tmp_path, monkeypatch, ((99, _blob()), (-4, _blob()), (8, None)))
    layer = profile.layers[0]
    assert (layer.fid_count, layer.fid_min, layer.fid_max) == (3, -4, 99)
    assert layer.fid_sequence_sha256 == _json_hash([-4, 8, 99])


@pytest.mark.parametrize("persistent", [False, True])
def test_byte_snapshot_resists_path_swap_and_final_postcondition(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, persistent: bool
) -> None:
    first = _gpkg_bytes(tmp_path / "a", ((1, _blob()),))
    other = _gpkg_bytes(tmp_path / "b", ((1, _blob(_point_wkb((99.0, 88.0)))),))
    config, extraction, catalog = _source(tmp_path / "source", monkeypatch, first)
    baseline = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    physical = extraction.extraction_path / "EP" / "one.gpkg"
    original = geometry._open_gpkg_sqlite_snapshot
    seen = False

    @contextmanager
    def swapped(payload: bytes, relative_path: str) -> Any:
        nonlocal seen
        assert payload == first
        with original(payload, relative_path) as connection:
            physical.write_bytes(other)
            seen = True
            try:
                yield connection
            finally:
                if not persistent:
                    physical.write_bytes(first)

    monkeypatch.setattr(geometry, "_open_gpkg_sqlite_snapshot", swapped)
    if persistent:
        with pytest.raises(InpnProtectedAreasGeometryProfileError):
            build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    else:
        assert (
            build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
            == baseline
        )
    assert seen


@pytest.mark.parametrize(
    "component", ["raw_geometry_blob_content_sha256", "geometry_content_sha256"]
)
def test_coordinated_component_and_complete_hash_forgery_fails_physical_rebuild(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, component: str
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    layer = replace(profile.layers[0], **{component: "9" * 64})
    forged = _rehash(replace(profile, layers=(layer,)))
    assert geometry._validate_profile_intrinsic(forged) is forged
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        validate_inpn_protected_areas_geometry_profile(
            extraction, config, catalog, forged
        )


@pytest.mark.parametrize(
    "mutation", ["source", "catalog", "package", "layer", "crs", "bounds"]
)
def test_catalog_preflight_rejects_mismatch_before_sqlite_geometry_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    if mutation == "source":
        forged = replace(profile, provider="forged")
    elif mutation == "catalog":
        forged = replace(profile, source_catalog_content_sha256="9" * 64)
    else:
        changed = {
            "package": {"file_size": profile.layers[0].file_size + 1},
            "layer": {"layer_name": "other"},
            "crs": {"crs_raw": "EPSG:4326"},
            "bounds": {"catalog_total_bounds": (-1.0, -1.0, 9.0, 9.0)},
        }[mutation]
        forged = replace(profile, layers=(replace(profile.layers[0], **changed),))
    forged = _rehash(forged)
    monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("geometry snapshot opened before preflight rejection"),
    )
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        validate_inpn_protected_areas_geometry_profile(
            extraction, config, catalog, forged
        )


def test_public_models_are_frozen_portable_and_export_only_factual_api(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = _build(tmp_path, monkeypatch)

    def walk(value: object) -> None:
        assert not isinstance(
            value, (dict, list, set, bytes, Path, np.ndarray, sqlite3.Connection)
        )
        assert not hasattr(value, "geom_type")
        if is_dataclass(value) and not isinstance(value, type):
            for field in fields(value):
                walk(getattr(value, field.name))
        elif type(value) is tuple:
            for member in value:
                walk(member)
        else:
            assert type(value) in (str, bool, int, float, type(None))

    walk(profile)
    with pytest.raises(FrozenInstanceError):
        profile.geometry_row_count = 99
    with pytest.raises(FrozenInstanceError):
        profile.layers[0].fid_count = 99
    assert set(geometry.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(
        getattr(sources, name) is getattr(geometry, name) for name in EXPECTED_EXPORTS
    )
    assert not hasattr(sources, "_open_gpkg_sqlite_snapshot")
    assert not hasattr(sources, "_parse_gpkg_geometry_blob")


@pytest.mark.parametrize(
    "mutation",
    [
        "missing-contents",
        "non-feature",
        "duplicate-contents",
        "missing-geometry",
        "duplicate-geometry",
        "missing-column",
        "contents-srs",
        "catalog-srs",
        "bad-z",
        "bad-m",
        "feature-view",
        "metadata-view",
        "no-pk",
        "wrong-pk",
        "composite-pk",
        "desc-pk",
        "without-rowid",
    ],
)
def test_physical_metadata_fails_closed_without_guessing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    package = _gpkg_bytes(tmp_path / "container")
    _, _, catalog = _source(tmp_path / "source", monkeypatch, package)
    layer = catalog.packages[0].layers[0]
    connection = sqlite3.connect(":memory:")
    try:
        connection.deserialize(package)
        if mutation == "missing-contents":
            connection.execute("DELETE FROM gpkg_contents")
        elif mutation == "non-feature":
            connection.execute("UPDATE gpkg_contents SET data_type='attributes'")
        elif mutation == "duplicate-contents":
            connection.execute(
                "CREATE TABLE contents_copy AS SELECT * FROM gpkg_contents"
            )
            connection.execute("DROP TABLE gpkg_contents")
            connection.execute("ALTER TABLE contents_copy RENAME TO gpkg_contents")
            connection.execute("INSERT INTO gpkg_contents SELECT * FROM gpkg_contents")
        elif mutation == "missing-geometry":
            connection.execute("DELETE FROM gpkg_geometry_columns")
        elif mutation == "duplicate-geometry":
            connection.execute(
                "CREATE TABLE geometry_copy AS SELECT * FROM gpkg_geometry_columns"
            )
            connection.execute("DROP TABLE gpkg_geometry_columns")
            connection.execute(
                "ALTER TABLE geometry_copy RENAME TO gpkg_geometry_columns"
            )
            connection.execute(
                "INSERT INTO gpkg_geometry_columns SELECT * FROM gpkg_geometry_columns"
            )
        elif mutation == "missing-column":
            connection.execute("UPDATE gpkg_geometry_columns SET column_name='missing'")
        elif mutation == "contents-srs":
            connection.execute("UPDATE gpkg_contents SET srs_id=4326")
        elif mutation == "catalog-srs":
            layer = replace(layer, crs_authority_code="4326")
        elif mutation in {"bad-z", "bad-m"}:
            column = "z" if mutation == "bad-z" else "m"
            connection.execute(f"UPDATE gpkg_geometry_columns SET {column}=3")
        elif mutation == "feature-view":
            connection.execute("ALTER TABLE physical_layer RENAME TO backing_table")
            connection.execute(
                "CREATE VIEW physical_layer AS SELECT fid, geom FROM backing_table"
            )
        elif mutation == "metadata-view":
            connection.execute(
                "ALTER TABLE gpkg_geometry_columns RENAME TO backing_metadata"
            )
            connection.execute(
                "CREATE VIEW gpkg_geometry_columns AS SELECT * FROM backing_metadata"
            )
        else:
            connection.execute("DROP TABLE physical_layer")
            declaration = {
                "no-pk": "fid INTEGER, geom GEOMETRY",
                "wrong-pk": "fid TEXT PRIMARY KEY, geom GEOMETRY",
                "composite-pk": "fid INTEGER, other INTEGER, geom GEOMETRY, PRIMARY KEY(fid, other)",
                "desc-pk": "fid INTEGER PRIMARY KEY DESC, geom GEOMETRY",
                "without-rowid": "fid INTEGER PRIMARY KEY, geom GEOMETRY",
            }[mutation]
            suffix = " WITHOUT ROWID" if mutation == "without-rowid" else ""
            connection.execute(f"CREATE TABLE physical_layer ({declaration}){suffix}")
        connection.commit()
        mutated = connection.serialize()
    finally:
        connection.close()
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError),
        geometry._open_gpkg_sqlite_snapshot(mutated, "EP/one.gpkg") as snapshot,
    ):
        geometry._read_gpkg_layer_metadata(snapshot, "EP/one.gpkg", layer)


def test_source_column_identity_is_discovered_not_guessed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = _gpkg_bytes(tmp_path / "container")
    connection = sqlite3.connect(":memory:")
    try:
        connection.deserialize(package)
        connection.execute(
            'ALTER TABLE physical_layer RENAME COLUMN fid TO "source key"'
        )
        connection.execute(
            'ALTER TABLE physical_layer RENAME COLUMN geom TO "source shape"'
        )
        connection.execute(
            "UPDATE gpkg_geometry_columns SET column_name='source shape'"
        )
        connection.commit()
        package = connection.serialize()
    finally:
        connection.close()
    config, extraction, catalog = _source(tmp_path / "source", monkeypatch, package)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    layer = profile.layers[0]
    assert layer.fid_column_name == "source key"
    assert layer.geometry_column_name == "source shape"
    assert layer.feature_table_kind == "table"
    assert layer.fid_sequence_sha256 == _json_hash([1, 7])


@pytest.mark.parametrize(
    "rows",
    [
        ((1, None), (1, None)),
        ((True, None),),
        ((None, None),),
        ((1.5, None),),
        ((np.int64(1), None),),
        ((1, "not blob"),),
        ((1, bytearray(b"x")),),
        ((1,),),
        ((1, None, "attribute"),),
    ],
)
def test_impossible_sqlite_fid_and_blob_rows_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    rows: tuple[tuple[object, ...], ...],
) -> None:
    package = _gpkg_bytes(tmp_path)
    # SQLite itself guarantees integer rowid aliases; this targeted reader seam
    # proves no coercion if a nonconforming DB API ever returns another shape.
    monkeypatch.setattr(geometry, "_sqlite_rows", lambda *a, **k: rows)
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError),
        geometry._open_gpkg_sqlite_snapshot(package, "EP/a.gpkg") as connection,
    ):
        geometry._read_gpkg_geometry_rows(
            connection, _metadata(), "EP/a.gpkg", len(rows)
        )


def test_geometry_row_count_must_match_catalog(tmp_path: Path) -> None:
    package = _gpkg_bytes(tmp_path)
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError),
        geometry._open_gpkg_sqlite_snapshot(package, "EP/a.gpkg") as connection,
    ):
        geometry._read_gpkg_geometry_rows(connection, _metadata(), "EP/a.gpkg", 99)


def test_unsorted_reader_rows_hash_in_numeric_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = _gpkg_bytes(tmp_path)
    rows = ((99, _blob()), (-4, None), (8, _blob()))
    monkeypatch.setattr(geometry, "_sqlite_rows", lambda *a, **k: rows)
    with geometry._open_gpkg_sqlite_snapshot(package, "EP/a.gpkg") as connection:
        result = geometry._read_gpkg_geometry_rows(
            connection, _metadata(), "EP/a.gpkg", 3
        )
    assert result == (rows[1], rows[2], rows[0])


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("fid_count", True),
        ("fid_count", 3),
        ("fid_min", None),
        ("fid_min", 7),
        ("fid_max", 1),
        ("gpkg_z_flag", 3),
        ("gpkg_m_flag", True),
        ("file_size", 0),
        ("package_position", 1),
        ("layer_position", 1),
        ("null_geometry_count", 1),
        ("empty_geometry_count", -1),
        ("valid_non_empty_geometry_count", 1),
        ("has_z_geometry_count", 1),
        ("has_m_geometry_count", 3),
        ("total_coordinate_count", True),
        ("raw_geometry_blob_content_sha256", "x" * 64),
        ("geometry_content_sha256", "f" * 63),
        ("driver_name", "GeoJSON"),
        ("feature_table_kind", "view"),
        ("bounds_relation", "CLOSE_ENOUGH"),
        ("observed_total_bounds", (0.0, 0.0, 0.0)),
        ("observed_total_bounds", (9.0, 0.0, 1.0, 2.0)),
        ("observed_total_bounds", (1, 2, 3, 5)),
        ("geometry_type_counts", []),
        ("coordinate_dimension_counts", []),
        ("validity_reason_counts", []),
    ],
)
def test_intrinsic_layer_rejects_noncanonical_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, field_name: str, value: object
) -> None:
    profile = _build(tmp_path, monkeypatch)
    changed = replace(profile.layers[0], **{field_name: value})
    forged = _rehash(replace(profile, layers=(changed,)))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(forged)


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("geometry_profile_schema_version", 2),
        ("geometry_profile_schema_version", True),
        ("geometry_encoding_schema_version", 2),
        ("geometry_encoding_contract", "unknown"),
        ("source_catalog_schema_version", 1),
        ("geometry_row_count", 99),
        ("package_count", 2),
        ("layer_count", 0),
        ("archive_size", False),
        ("has_z_geometry_count", 1),
        ("provider", _StringSubclass("PatriNat")),
        ("sqlite_version", ""),
        ("geos_version", _StringSubclass("3.13.1")),
        ("source_catalog_content_sha256", "bad"),
        ("layers", []),
    ],
)
def test_intrinsic_profile_rejects_noncanonical_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, field_name: str, value: object
) -> None:
    profile = _build(tmp_path, monkeypatch)
    forged = _rehash(replace(profile, **{field_name: value}))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(forged)


@pytest.mark.parametrize(
    "relative_path",
    [
        " EP/a.gpkg",
        "EP/a.gpkg ",
        "/EP/a.gpkg",
        "C:/EP/a.gpkg",
        "../a.gpkg",
        "EP\\a.gpkg",
        "EP/a.txt",
        "EP/CON.gpkg",
        "EP/NUL.gpkg",
        "EP/a:b.gpkg",
        "EP/dir /a.gpkg",
        "EP/ dir/a.gpkg",
        "EP/dir./a.gpkg",
        "EP/control\x01.gpkg",
        "EP/ＮＵＬ.gpkg",
        "EP/dir／a.gpkg",
    ],
)
def test_intrinsic_package_paths_use_shared_authoritative_grammar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, relative_path: str
) -> None:
    profile = _build(tmp_path, monkeypatch)
    forged = _rehash(
        replace(
            profile, layers=(replace(profile.layers[0], relative_path=relative_path),)
        )
    )
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(forged)


@pytest.mark.parametrize(
    "domain",
    ["geometry_type_counts", "coordinate_dimension_counts", "validity_reason_counts"],
)
def test_intrinsic_domains_reject_duplicate_entries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, domain: str
) -> None:
    profile = _build(tmp_path, monkeypatch)
    layer = profile.layers[0]
    value = getattr(layer, domain)[0]
    duplicate = (replace(value, count=1), replace(value, count=1))
    forged = _rehash(replace(profile, layers=(replace(layer, **{domain: duplicate}),)))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(forged)


def test_intrinsic_profile_hash_mismatch_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = _build(tmp_path, monkeypatch)
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(
            replace(profile, complete_geometry_profile_content_sha256="0" * 64)
        )


def test_toolchain_identity_is_portable_and_hash_significant(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = _build(tmp_path, monkeypatch)
    assert profile.sqlite_version == sqlite3.sqlite_version
    assert profile.pyogrio_version == pyogrio.__version__
    assert profile.gdal_version == pyogrio.__gdal_version_string__
    assert profile.shapely_version == shapely.__version__
    assert profile.geos_version == shapely.geos_version_string
    for name in (
        "sqlite_version",
        "pyogrio_version",
        "gdal_version",
        "shapely_version",
        "geos_version",
        "pyproj_version",
    ):
        changed = _rehash(
            replace(profile, **{name: getattr(profile, name) + ".changed"})
        )
        assert (
            changed.complete_geometry_profile_content_sha256
            != profile.complete_geometry_profile_content_sha256
        )


@pytest.mark.parametrize(
    "embedded",
    [
        _point_wkb() + b"trailing",
        _point_wkb()[:-1],
        b"\x02" + _point_wkb()[1:],
        struct.pack("<BI", 1, 8),
        struct.pack("<BI", 1, 4001) + struct.pack("<2d", 1, 2),
        struct.pack("<BI", 1, 0x20000001) + struct.pack("<I2d", 2154, 1, 2),
        struct.pack("<BI", 1, 0x80000001) + struct.pack("<3d", 1, 2, 3),
        struct.pack("<BII", 1, 2, 3) + struct.pack("<2d", 1, 2),
        struct.pack("<BII", 1, 7, 2) + _point_wkb(),
    ],
)
def test_embedded_iso_wkb_framing_is_exact_and_no_ewkb_is_accepted(
    embedded: bytes,
) -> None:
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._parse_gpkg_geometry_blob(_blob(embedded), _metadata(), "EP/a.gpkg", 1)


def test_embedded_measure_cannot_be_silently_lost_by_parser(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    blob = _blob(_point_wkb((1.0, 2.0, 4.0), has_m=True))
    # This adversarial seam supplements, never replaces, all real M/ZM parser tests.
    monkeypatch.setattr(shapely, "from_wkb", lambda *a, **k: Point(1, 2))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._parse_gpkg_geometry_blob(blob, _metadata(), "EP/a.gpkg", 1)


@pytest.mark.parametrize(
    "wkt",
    [
        "LINESTRING (0 0, 1 2)",
        "MULTIPOINT ((0 0), (1 2))",
        "MULTILINESTRING ((0 0, 1 2), (3 4, 5 6))",
        "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))",
        "GEOMETRYCOLLECTION (POINT (1 2), LINESTRING (0 0, 3 4))",
        "GEOMETRYCOLLECTION M (POINT M (1 2 4), LINESTRING M (0 0 5, 3 4 6))",
    ],
)
def test_all_core_geometry_families_preserve_complete_type_and_coordinate_evidence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, wkt: str
) -> None:
    expected = shapely.from_wkt(wkt)
    profile = _build(tmp_path, monkeypatch, ((1, _wkt_blob(wkt)),))
    layer = profile.layers[0]
    assert layer.geometry_type_counts[0].geometry_type == expected.geom_type
    assert layer.total_coordinate_count == len(shapely.get_coordinates(expected))
    assert layer.has_z_geometry_count == int(shapely.has_z(expected))
    assert layer.has_m_geometry_count == int(shapely.has_m(expected))


def test_mixed_collection_absent_ordinates_are_not_source_nan(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    embedded = (
        struct.pack("<BII", 1, 3007, 2)
        + _point_wkb((1.0, 2.0, 4.0), has_m=True)
        + _point_wkb((3.0, 4.0, 5.0), has_z=True)
    )
    profile = _build(tmp_path, monkeypatch, ((1, _blob(embedded)),))
    assert profile.layers[0].total_coordinate_count == 2
    assert profile.layers[0].has_z_geometry_count == 1
    assert profile.layers[0].has_m_geometry_count == 1


def test_coordinated_catalog_hash_forgery_rejected_before_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    changed_layer = replace(
        catalog.packages[0].layers[0], total_bounds=(0.0, 0.0, 10.0, 10.0)
    )
    forged = replace(
        catalog, packages=(replace(catalog.packages[0], layers=(changed_layer,)),)
    )
    forged = replace(
        forged,
        complete_catalog_content_sha256=catalog_module._catalog_content_sha256(forged),
    )
    monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("geometry snapshot opened"),
    )
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        build_inpn_protected_areas_geometry_profile(extraction, config, forged)


@pytest.mark.parametrize("mutation", ["schema", "archive", "package"])
def test_stale_source_or_catalog_rejected_before_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    if mutation == "schema":
        catalog = replace(catalog, catalog_schema_version=1)
        catalog = replace(
            catalog,
            complete_catalog_content_sha256=catalog_module._catalog_content_sha256(
                catalog
            ),
        )
    elif mutation == "archive":
        extraction.download.path.write_bytes(b"not the configured archive")
    else:
        (extraction.extraction_path / "EP" / "one.gpkg").write_bytes(
            b"not the verified package"
        )
    monkeypatch.setattr(
        geometry,
        "_open_gpkg_sqlite_snapshot",
        lambda *a: pytest.fail("geometry snapshot opened"),
    )
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        build_inpn_protected_areas_geometry_profile(extraction, config, catalog)


@pytest.mark.parametrize("relative_path", ["EP/subdir/a.gpkg", "EP/subdir/a.GPKG"])
def test_intrinsic_accepts_valid_nested_package_paths(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, relative_path: str
) -> None:
    profile = _build(tmp_path, monkeypatch)
    changed = _rehash(
        replace(
            profile, layers=(replace(profile.layers[0], relative_path=relative_path),)
        )
    )
    assert geometry._validate_profile_intrinsic(changed) is changed


@pytest.mark.parametrize(
    "mutation",
    [
        "repeated-path",
        "casefold-path",
        "nfkc-path",
        "path-order",
        "repeated-size",
        "repeated-sha",
        "layer-order",
        "duplicate-layer",
        "casefold-layer",
        "nfkc-layer",
        "noncontiguous",
    ],
)
def test_intrinsic_package_grouping_and_identity_collisions_fail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    package = _gpkg_bytes(tmp_path / "container", layer_names=("first", "second"))
    config, extraction, catalog = _source(tmp_path / "source", monkeypatch, package)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    first, second = profile.layers
    if mutation in {"repeated-path", "casefold-path", "nfkc-path", "path-order"}:
        paths = {
            "repeated-path": ("EP/a.gpkg", "EP/a.gpkg"),
            "casefold-path": ("EP/A.gpkg", "EP/a.gpkg"),
            "nfkc-path": ("EP/K.gpkg", "EP/K.gpkg"),
            "path-order": ("EP/z.gpkg", "EP/a.gpkg"),
        }[mutation]
        first = replace(first, relative_path=paths[0])
        second = replace(
            second, relative_path=paths[1], package_position=1, layer_position=0
        )
        changed = replace(profile, package_count=2, layers=(first, second))
    elif mutation == "noncontiguous":
        other = replace(
            second, relative_path="EP/z.gpkg", package_position=1, layer_position=0
        )
        changed = replace(profile, layers=(first, other, second))
    else:
        updates = {
            "repeated-size": {"file_size": second.file_size + 1},
            "repeated-sha": {"file_sha256": "9" * 64},
            "layer-order": {"layer_position": 2},
            "duplicate-layer": {"layer_name": first.layer_name},
            "casefold-layer": {"layer_name": first.layer_name.upper()},
            "nfkc-layer": {"layer_name": "K"},
        }[mutation]
        if mutation == "nfkc-layer":
            first = replace(first, layer_name="K")
        changed = replace(profile, layers=(first, replace(second, **updates)))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(_rehash(changed))


@pytest.mark.parametrize(
    ("domain", "changes"),
    [
        ("geometry_type_counts", {"geometry_type": "Unsupported"}),
        ("geometry_type_counts", {"count": True}),
        ("coordinate_dimension_counts", {"coordinate_dimension": True}),
        ("coordinate_dimension_counts", {"has_z": 0}),
        ("coordinate_dimension_counts", {"has_m": 0}),
        ("coordinate_dimension_counts", {"coordinate_dimension": 4}),
        ("validity_reason_counts", {"is_valid": 1}),
        ("validity_reason_counts", {"reason": _StringSubclass("Valid Geometry")}),
        ("validity_reason_counts", {"count": 0}),
    ],
)
def test_intrinsic_domain_scalar_types_and_frequencies_are_exact(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    domain: str,
    changes: dict[str, object],
) -> None:
    profile = _build(tmp_path, monkeypatch)
    layer = profile.layers[0]
    value = replace(getattr(layer, domain)[0], **changes)
    changed = _rehash(replace(profile, layers=(replace(layer, **{domain: (value,)}),)))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(changed)


@pytest.mark.parametrize(
    "component",
    [
        "fid_sequence_sha256",
        "raw_geometry_blob_content_sha256",
        "geometry_content_sha256",
    ],
)
def test_empty_layer_component_hashes_are_reconstructed_intrinsically(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, component: str
) -> None:
    profile = _build(tmp_path, monkeypatch, ())
    changed = _rehash(
        replace(profile, layers=(replace(profile.layers[0], **{component: "9" * 64}),))
    )
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(changed)


def test_parser_stream_hash_matches_independent_complete_row_encoding(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    measured = _point_wkb((1.0, 2.0, 4.0), has_m=True)
    empty = _point_wkb((math.nan, math.nan, math.nan, math.nan), has_z=True, has_m=True)
    profile = _build(
        tmp_path,
        monkeypatch,
        ((99, _blob(measured)), (2, None), (7, _blob(empty, empty=True))),
    )
    measured_geometry = shapely.from_wkb(measured)
    empty_geometry = shapely.from_wkb(empty)
    expected_rows = [
        [2, "NULL", None, None, None, None, None, None, None],
        [
            7,
            "EMPTY",
            "Point",
            4,
            True,
            True,
            None,
            None,
            shapely.to_wkb(
                empty_geometry,
                hex=True,
                output_dimension=4,
                byte_order=1,
                include_srid=False,
                flavor="extended",
            ),
        ],
        [
            99,
            "NON_EMPTY",
            "Point",
            3,
            False,
            True,
            True,
            "Valid Geometry",
            shapely.to_wkb(
                measured_geometry,
                hex=True,
                output_dimension=3,
                byte_order=1,
                include_srid=False,
                flavor="extended",
            ),
        ],
    ]
    assert profile.layers[0].geometry_content_sha256 == _json_hash(expected_rows)
    assert profile.layers[0].raw_geometry_blob_content_sha256 == _json_hash(
        [
            [2, None],
            [7, sha256(_blob(empty, empty=True)).hexdigest()],
            [99, sha256(_blob(measured)).hexdigest()],
        ]
    )


def test_parser_serialization_uses_every_explicit_contract_option(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = _gpkg_bytes(
        tmp_path / "container", ((1, _blob(_point_wkb((1.0, 2.0, 4.0), has_m=True))),)
    )
    config, extraction, catalog = _source(tmp_path / "source", monkeypatch, package)
    original = shapely.to_wkb
    options: list[dict[str, object]] = []

    def recorded(value: object, **kwargs: object) -> object:
        options.append(kwargs)
        return original(value, **kwargs)

    monkeypatch.setattr(shapely, "to_wkb", recorded)
    build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    assert options == [
        {
            "hex": True,
            "output_dimension": 3,
            "byte_order": 1,
            "include_srid": False,
            "flavor": "extended",
        }
    ]


@pytest.mark.parametrize("empty", [False, True])
def test_intrinsic_catalog_bounds_follow_physical_feature_count(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, empty: bool
) -> None:
    profile = _build(tmp_path, monkeypatch, () if empty else None)
    layer = replace(
        profile.layers[0],
        catalog_total_bounds=(1.0, 2.0, 1.0, 2.0) if empty else None,
        bounds_relation="DIFFERENT",
    )
    changed = _rehash(replace(profile, layers=(layer,)))
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(changed)


@pytest.mark.parametrize(
    "error_type", [sqlite3.DatabaseError, OverflowError, TypeError, ValueError]
)
def test_sqlite_close_failures_are_controlled_and_chained(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, error_type: type[Exception]
) -> None:
    package = _gpkg_bytes(tmp_path)
    original = sqlite3.connect

    class CloseFailure(sqlite3.Connection):
        def close(self) -> None:
            super().close()
            raise error_type("controlled close failure")

    monkeypatch.setattr(
        geometry.sqlite3,
        "connect",
        lambda *a, **k: original(*a, factory=CloseFailure, **k),
    )
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError) as captured,
        geometry._open_gpkg_sqlite_snapshot(package, "EP/a.gpkg"),
    ):
        pass
    assert isinstance(captured.value.__cause__, error_type)


def test_exact_and_different_bounds_are_evidence_without_tolerance(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    exact = _build(tmp_path / "exact", monkeypatch, ((1, _blob()),)).layers[0]
    different = _build(tmp_path / "different", monkeypatch).layers[0]
    assert (
        exact.catalog_total_bounds
        == exact.observed_total_bounds
        == (1.0, 2.0, 1.0, 2.0)
    )
    assert exact.bounds_relation == "EXACT_MATCH"
    assert different.catalog_total_bounds != different.observed_total_bounds
    assert different.bounds_relation == "DIFFERENT"


def test_quoted_source_table_name_cannot_inject_sql(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    layer_name = 'physical"; DROP TABLE gpkg_contents; --'
    package = _gpkg_bytes(tmp_path / "container", layer_names=(layer_name,))
    config, extraction, catalog = _source(tmp_path / "source", monkeypatch, package)
    profile = build_inpn_protected_areas_geometry_profile(extraction, config, catalog)
    assert profile.layers[0].layer_name == layer_name
    assert profile.geometry_row_count == 2


@pytest.mark.parametrize("declared_type", INVALID_DECLARED_TYPES)
def test_type_contract_metadata_rejects_noncanonical_declared_geometry_type(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, declared_type: str
) -> None:
    package = _gpkg_bytes(tmp_path / "container")
    _, _, catalog = _source(tmp_path / "source", monkeypatch, package)
    connection = sqlite3.connect(":memory:")
    try:
        connection.deserialize(package)
        connection.execute(
            "UPDATE gpkg_geometry_columns SET geometry_type_name=?", (declared_type,)
        )
        connection.commit()
        changed = connection.serialize()
    finally:
        connection.close()
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError),
        geometry._open_gpkg_sqlite_snapshot(changed, "EP/one.gpkg") as snapshot,
    ):
        geometry._read_gpkg_layer_metadata(
            snapshot, "EP/one.gpkg", catalog.packages[0].layers[0]
        )


@pytest.mark.parametrize("sql_type", ["GEOMETRY", "BLOB", "LINESTRING", "point"])
def test_type_contract_metadata_rejects_different_sql_geometry_column_type(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, sql_type: str
) -> None:
    package = _gpkg_bytes(tmp_path / "container")
    _, _, catalog = _source(tmp_path / "source", monkeypatch, package)
    connection = sqlite3.connect(":memory:")
    try:
        connection.deserialize(package)
        connection.execute("DROP TABLE physical_layer")
        connection.execute(
            f'CREATE TABLE physical_layer (fid INTEGER PRIMARY KEY, geom "{sql_type}")'
        )
        connection.execute(
            "UPDATE gpkg_geometry_columns SET geometry_type_name='POINT'"
        )
        assert (
            connection.execute("PRAGMA table_info(physical_layer)").fetchall()[1][2]
            == sql_type
        )
        connection.commit()
        changed = connection.serialize()
    finally:
        connection.close()
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError),
        geometry._open_gpkg_sqlite_snapshot(changed, "EP/one.gpkg") as snapshot,
    ):
        geometry._read_gpkg_layer_metadata(
            snapshot, "EP/one.gpkg", catalog.packages[0].layers[0]
        )


@pytest.mark.parametrize("sql_type", [_StringSubclass("POINT"), None, 1])
def test_type_contract_sql_declared_type_requires_exact_runtime_spelling(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, sql_type: object
) -> None:
    package = _gpkg_bytes(
        tmp_path / "container", geometry_type="Point", z_flag=0, m_flag=0
    )
    _, _, catalog = _source(tmp_path / "source", monkeypatch, package)
    original = geometry._sqlite_rows

    def altered(
        connection: sqlite3.Connection,
        statement: str,
        parameters: tuple[object, ...] = (),
    ) -> tuple[tuple[object, ...], ...]:
        rows = original(connection, statement, parameters)
        if statement.startswith("PRAGMA main.table_info("):
            return tuple(
                (*row[:2], sql_type, *row[3:]) if row[1] == "geom" else row
                for row in rows
            )
        return rows

    monkeypatch.setattr(geometry, "_sqlite_rows", altered)
    with (
        pytest.raises(InpnProtectedAreasGeometryProfileError),
        geometry._open_gpkg_sqlite_snapshot(package, "EP/one.gpkg") as snapshot,
    ):
        geometry._read_gpkg_layer_metadata(
            snapshot, "EP/one.gpkg", catalog.packages[0].layers[0]
        )


@pytest.mark.parametrize(
    ("declared_type", "wkt"),
    [
        ("POINT", "LINESTRING (0 0, 1 2)"),
        ("LINESTRING", "POINT (1 2)"),
        ("POLYGON", "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))"),
        ("MULTIPOLYGON", "POLYGON ((0 0, 2 0, 2 2, 0 0))"),
        ("MULTIPOINT", "POINT (1 2)"),
        ("MULTILINESTRING", "LINESTRING (0 0, 1 2)"),
        ("GEOMETRYCOLLECTION", "POINT (1 2)"),
        ("POINT", "LINESTRING EMPTY"),
    ],
)
def test_type_contract_rejects_unassignable_root_wkb_family(
    declared_type: str, wkt: str
) -> None:
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._parse_gpkg_geometry_blob(
            _wkt_blob(wkt),
            _metadata(geometry_type_name=declared_type),
            "EP/one.gpkg",
            1,
        )


@pytest.mark.parametrize(("declared_type", "observed_type", "wkt"), CORE_TYPE_CASES)
@pytest.mark.parametrize("use_supertype", [False, True])
def test_type_contract_accepts_matching_core_roots_and_geometry_supertype(
    declared_type: str, observed_type: str, wkt: str, use_supertype: bool
) -> None:
    metadata = _metadata(
        geometry_type_name="GEOMETRY" if use_supertype else declared_type
    )
    parsed = geometry._parse_gpkg_geometry_blob(
        _wkt_blob(wkt), metadata, "EP/one.gpkg", 1
    )
    assert parsed.geometry.geom_type == observed_type


@pytest.mark.parametrize("blob", [None, _wkt_blob("POINT EMPTY")])
def test_type_contract_point_null_and_empty_source_controls(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, blob: bytes | None
) -> None:
    profile = _build(
        tmp_path, monkeypatch, ((1, blob),), geometry_type="Point", z_flag=0, m_flag=0
    )
    layer = profile.layers[0]
    assert layer.gpkg_geometry_type_name == "POINT"
    assert layer.null_geometry_count == int(blob is None)
    assert layer.empty_geometry_count == int(blob is not None)
    assert tuple(item.geometry_type for item in layer.geometry_type_counts) == (
        () if blob is None else ("Point",)
    )


@pytest.mark.parametrize(("has_z", "has_m", "coordinates"), DIMENSIONS)
@pytest.mark.parametrize("empty", [False, True])
def test_type_contract_point_assignability_preserves_xy_z_m_zm(
    has_z: bool, has_m: bool, coordinates: tuple[float, ...], empty: bool
) -> None:
    ordinates = tuple(math.nan for _ in coordinates) if empty else coordinates
    blob = _blob(_point_wkb(ordinates, has_z=has_z, has_m=has_m), empty=empty)
    parsed = geometry._parse_gpkg_geometry_blob(
        blob, _metadata(geometry_type_name="POINT"), "EP/one.gpkg", 1
    )
    assert parsed.geometry.geom_type == "Point"
    assert bool(shapely.has_z(parsed.geometry)) is has_z
    assert bool(shapely.has_m(parsed.geometry)) is has_m
    assert bool(shapely.is_empty(parsed.geometry)) is empty


@pytest.mark.parametrize("declared_type", INVALID_DECLARED_TYPES)
def test_type_contract_intrinsic_rejects_invalid_declaration_even_null_only(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, declared_type: str
) -> None:
    profile = _build(tmp_path, monkeypatch, ((1, None),))
    forged = _rehash(
        replace(
            profile,
            layers=(replace(profile.layers[0], gpkg_geometry_type_name=declared_type),),
        )
    )
    assert forged.layers[0].geometry_type_counts == ()
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(forged)


@pytest.mark.parametrize(
    ("declared_type", "wkt"),
    [
        ("POINT", "LINESTRING (0 0, 1 2)"),
        ("POLYGON", "MULTIPOLYGON (((0 0, 2 0, 2 2, 0 0)))"),
        ("MULTIPOLYGON", "POLYGON ((0 0, 2 0, 2 2, 0 0))"),
    ],
)
def test_type_contract_intrinsic_rejects_rehashed_declared_observed_mismatch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, declared_type: str, wkt: str
) -> None:
    profile = _build(tmp_path, monkeypatch, ((1, _wkt_blob(wkt)),))
    forged = _rehash(
        replace(
            profile,
            layers=(replace(profile.layers[0], gpkg_geometry_type_name=declared_type),),
        )
    )
    assert (
        forged.complete_geometry_profile_content_sha256
        == geometry._profile_content_sha256(forged)
    )
    with pytest.raises(InpnProtectedAreasGeometryProfileError):
        geometry._validate_profile_intrinsic(forged)
```
