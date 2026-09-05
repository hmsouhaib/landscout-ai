# `src/landscout/sources/inpn_protected_areas_geometry_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_geometry_fr.py`
- File type: Python source
- Layer/domain: source-bound INPN EP geometry technical-quality evidence
- Responsibility: Profiles physical FIDs and raw geometry BLOBs from verified immutable GeoPackage bytes, preserving Z/M and independently validating raw/parser evidence without environmental meaning.
- Source SHA256: `56b90e1fed87fab0dafda5100e9417a91219c3aa0c2467f47692bc71ce670fb4`

## 1. Architectural and reader contract

This module implements verified extraction -> fresh schema-2 physical catalog -> verified immutable package bytes -> query-only in-memory SQLite deserialize -> exact FID + geometry BLOB -> Standard GeoPackageBinary -> embedded ISO WKB -> Shapely -> schema-1 immutable geometry-quality profile. Pyogrio 0.13.0 is deliberately not used for EP geometry-row materialization because it drops M. It remains the approved metadata-catalog reader; the existing attribute-only reader, source identity, catalog payload/hash/schema, and attribute payload/hash/schema are unchanged.

No geometry read reopens a live package path after the verified byte snapshot is captured. All layers in one package share its deserialized snapshot. Metadata values are parameter-bound and identifiers are validated and double-quote escaped. Supported layers are ordinary spatial feature tables with one INTEGER PRIMARY KEY rowid alias; feature/metadata views, virtual/shadow feature tables, WITHOUT ROWID feature tables, ambiguous keys, and the non-alias column-DESC primary-key form fail closed. No attribute columns, Pyogrio/GeoPandas feature readers, extensions, attached database, database writes, network, download, or persistent output are used.

## 2. Every import and qualified dependency ownership


```python
from __future__ import annotations
import json
import math
import re
import sqlite3
import struct
import unicodedata
from collections import Counter
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from pathlib import PurePosixPath
from types import MappingProxyType
from typing import Any
import numpy as np
import pyogrio
import pyproj
import shapely
from shapely.geometry.base import BaseGeometry
from landscout.sources.inpn_protected_areas_attributes_fr import (
    InpnProtectedAreasAttributeProfileError,
)
from landscout.sources.inpn_protected_areas_attributes_fr import (
    _prepare_inputs as _prepare_source_inputs,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    CATALOG_HASH_SCHEMA_VERSION,
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasGeoPackageCatalog,
    InpnProtectedAreasLayerCatalog,
    _canonical_crs,
    _read_verified_package_bytes,
    _validated_bounds,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    _validate_inventory_relative_path,
    validate_inpn_protected_areas_extraction,
)
```

SQLite/struct implement snapshot and exact binary framing; JSON/SHA256 bind portable evidence; Unicode/PurePosixPath enforce identities; Counter/NumPy derive temporary domains and coordinate checks; frozen dataclasses retain only immutable evidence. Shapely/GEOS parse and inspect geometry without repair. Pyogrio and PyProj provide exact installed identity; canonical CRS validation remains owned by the catalog.

The imported `_prepare_source_inputs` binding is an alias of `landscout.sources.inpn_protected_areas_attributes_fr._prepare_inputs`, reused only for exact type/config/extraction/catalog reconstruction—not attribute reading. `_read_verified_package_bytes`, `_canonical_crs`, and `_validated_bounds` are owned by `landscout.sources.inpn_protected_areas_catalog_fr`. `_validate_inventory_relative_path` and `validate_inpn_protected_areas_extraction` are owned by `landscout.sources.inpn_protected_areas_fr`. These are imports, not redefined geometry-module authorities.

## 3. Every constant and hash version


```python
_CORE_GEOMETRY_TYPES: MappingProxyType[int, tuple[str, str | None]] = MappingProxyType(
    {
        0: ("GEOMETRY", None),
        1: ("POINT", "Point"),
        2: ("LINESTRING", "LineString"),
        3: ("POLYGON", "Polygon"),
        4: ("MULTIPOINT", "MultiPoint"),
        5: ("MULTILINESTRING", "MultiLineString"),
        6: ("MULTIPOLYGON", "MultiPolygon"),
        7: ("GEOMETRYCOLLECTION", "GeometryCollection"),
    }
)

GEOMETRY_PROFILE_SCHEMA_VERSION = 1

GEOMETRY_ENCODING_SCHEMA_VERSION = 1

GEOMETRY_ENCODING_CONTRACT = (
    "SHAPELY_EXTENDED_WKB_LITTLE_ENDIAN_SOURCE_DIMENSION_NO_SRID_V1"
)

_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")

_SOURCE_FIELDS = (
    "provider",
    "authority",
    "program",
    "dataset_id",
    "dataset_name",
    "declared_version",
    "reference_page_url",
    "archive_url",
    "archive_filename",
    "archive_size",
    "archive_sha256",
)

_COUNT_FIELDS = (
    "null_geometry_count",
    "empty_geometry_count",
    "non_empty_geometry_count",
    "valid_non_empty_geometry_count",
    "invalid_non_empty_geometry_count",
    "has_z_geometry_count",
    "has_m_geometry_count",
    "total_coordinate_count",
)

_TOOLCHAIN_FIELDS = (
    "sqlite_version",
    "pyogrio_version",
    "gdal_version",
    "shapely_version",
    "geos_version",
    "pyproj_version",
)
```

Geometry-profile and parser-encoding schemas remain 1. The existing catalog stays at schema 2; no previous persisted hash is migrated. The private MappingProxyType core table owns an unaliased dictionary of immutable records: ID 0 represents only the GEOMETRY declaration; IDs 1–7 bind canonical GeoPackage names to exact Shapely names. It does not enable WKB type ID 0. Source/count/toolchain field tuples define portable comparisons and aggregate closure, not environmental vocabularies. The encoding contract fixes extended little-endian parser WKB at the actual geometry dimension with no SRID; raw source WKB and full BLOB bytes remain distinct identities.

## 4. Every model and field

Public models are frozen dataclasses containing only exact portable scalar values and immutable tuples. Private parser records may retain temporary geometry/WKB/envelope state during construction, but none escapes into public evidence. Dataclass construction alone is not the public trust boundary: builders and validators prove the complete intrinsic/source contracts.

### `InpnProtectedAreasGeometryProfileError`

Raised when exact source-bound geometry evidence cannot be proven.

Base classes: `ValueError`.

### `_GpkgLayerMetadata`

Private metadata for one physical ordinary GeoPackage feature table.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `table_name: str` | Exact physical feature-table spelling; matches the catalog layer. |
| `table_kind: str` | Exact physical SQLite kind; supported value is table. |
| `fid_column_name: str` | Discovered INTEGER PRIMARY KEY rowid-alias column, not a guessed name. |
| `geometry_column_name: str` | Exact physical geometry-BLOB column from GeoPackage metadata. |
| `geometry_type_name: str` | Exact supported uppercase gpkg_geometry_columns declaration, proven equal to the physical geometry-column SQL declared type; no category interpretation. |
| `srs_id: int` | Exact signed int32 GeoPackage source SRS identifier. |
| `z_flag: int` | Exact GeoPackage Z declaration: 0 prohibited, 1 mandatory, 2 optional. |
| `m_flag: int` | Exact GeoPackage M declaration: 0 prohibited, 1 mandatory, 2 optional. |

### `_ParsedGpkgGeometry`

Temporary raw-header/parser state, never retained in public evidence.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `geometry: BaseGeometry` | Temporary exact parsed Shapely scalar; never retained in public records. |
| `embedded_wkb: bytes` | Temporary exact WKB slice extracted from the full source BLOB, not canonical parser output. |
| `srs_id: int` | Exact signed int32 GeoPackage source SRS identifier. |
| `envelope_code: int` | Parsed Standard GeoPackageBinary envelope code 0–4. |
| `envelope: tuple[float, ...]` | Exact header-envelope doubles, retained only in the private parser record; no numerical consistency check against WKB coordinates. |
| `header_little_endian: bool` | Header byte-order flag, independent of embedded WKB byte order. |
| `is_empty: bool` | Parsed header/WKB empty agreement in the private record. |

### `_WkbShape`

Embedded-WKB framing and declared dimensions before GEOS conversion.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `type_id: int` | Core ISO WKB type ID 1–7 before parser conversion. |
| `has_z: bool` | Actual or declared Z-presence evidence according to the owning private/domain record. |
| `has_m: bool` | Actual or declared M-presence evidence according to the owning private/domain record. |
| `children: tuple[_WkbShape, ...]` | Ordered immutable WKB child-declaration tree used to detect parser dimension loss. |

### `InpnProtectedAreasGeometryTypeCount`

One observed non-null Shapely type and its complete frequency.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `geometry_type: str` | Exact observed non-null Shapely geometry type; EMPTY remains in this domain. |
| `count: int` | Exact positive frequency for the owning type/dimension/validity-reason domain. |

### `InpnProtectedAreasCoordinateDimensionCount`

Joint dimension/Z/M evidence, including dimensional empty geometries.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `coordinate_dimension: int` | Actual Shapely coordinate dimension 2, 3, or 4; Z and M are independent evidence. |
| `has_z: bool` | Actual or declared Z-presence evidence according to the owning private/domain record. |
| `has_m: bool` | Actual or declared M-presence evidence according to the owning private/domain record. |
| `count: int` | Exact positive frequency for the owning type/dimension/validity-reason domain. |

### `InpnProtectedAreasGeometryValidityReasonCount`

One exact non-empty validity outcome/reason and complete frequency.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `is_valid: bool` | Exact non-empty topological validity Boolean; NULL and EMPTY have no validity-domain entry. |
| `reason: str` | Exact Shapely non-empty validity reason, without semantic rewriting. |
| `count: int` | Exact positive frequency for the owning type/dimension/validity-reason domain. |

### `InpnProtectedAreasLayerGeometryProfile`

Portable raw-blob and parser-derived evidence for one physical table.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `relative_path: str` | Exact canonical portable package path from the archive-derived inventory, never an absolute Path. |
| `file_size: int` | Exact positive physical package byte size bound to extraction/catalog authority. |
| `file_sha256: str` | Exact physical package SHA256. |
| `package_position: int` | Contiguous zero-based package order, lexically ordered by exact relative path. |
| `driver_name: str` | Exact physical catalog driver GPKG. |
| `layer_name: str` | Exact catalog/feature-table name. |
| `layer_position: int` | Contiguous zero-based layer order within the package. |
| `feature_count: int` | Exact physical catalog feature count. |
| `feature_table_kind: str` | Physical SQLite table kind; views and unsupported key contracts fail closed. |
| `fid_column_name: str` | Discovered INTEGER PRIMARY KEY rowid-alias column, not a guessed name. |
| `geometry_column_name: str` | Exact physical geometry-BLOB column from GeoPackage metadata. |
| `gpkg_geometry_type_name: str` | Exact supported uppercase GeoPackage declaration, independently bound to the physical SQL declared type and assignable observed WKB-type domain. |
| `gpkg_srs_id: int` | Signed source SRS ID agreed by metadata/header and proven integer EPSG authority. |
| `gpkg_z_flag: int` | Exact GeoPackage Z declaration, checked against every non-null parsed geometry. |
| `gpkg_m_flag: int` | Exact GeoPackage M declaration, checked against every non-null parsed geometry. |
| `catalog_geometry_type_raw: str` | Unchanged geometry-type text from the physical Pyogrio catalog. |
| `crs_raw: str` | Unchanged raw physical catalog CRS text. |
| `crs_authority_name: str &#124; None` | Canonical catalog authority name, or None where no authority is proven. |
| `crs_authority_code: str &#124; None` | Canonical catalog authority code text, or None where unavailable. |
| `crs_wkt: str` | Unchanged canonical WKT2_2019 catalog CRS evidence; not reprojected. |
| `fid_count: int` | Number of exact physical identifiers; equals feature_count. |
| `fid_min: int &#124; None` | Exact minimum source FID, or None only for zero rows. |
| `fid_max: int &#124; None` | Exact maximum source FID, or None only for zero rows. |
| `fid_sequence_sha256: str` | Canonical JSON SHA256 of the complete numerically sorted FID sequence. |
| `null_geometry_count: int` | Number of SQLite NULL geometry values. |
| `empty_geometry_count: int` | Number of non-null BLOB geometries parsed as EMPTY. |
| `non_empty_geometry_count: int` | Number of non-null, non-empty parsed geometries. |
| `valid_non_empty_geometry_count: int` | Number of NON_EMPTY geometries with true Shapely validity. |
| `invalid_non_empty_geometry_count: int` | Number of NON_EMPTY geometries with false Shapely validity; unrepaired factual evidence. |
| `has_z_geometry_count: int` | Number of non-null geometries with actual Z, including dimensional EMPTY geometries. |
| `has_m_geometry_count: int` | Number of non-null geometries with actual M, including dimensional EMPTY geometries. |
| `total_coordinate_count: int` | Complete present coordinate count; NULL and EMPTY contribute zero. |
| `geometry_type_counts: tuple[InpnProtectedAreasGeometryTypeCount, ...]` | Every observed non-null type and exact frequency in lexical type order; each type must be assignable to gpkg_geometry_type_name, including EMPTY. |
| `coordinate_dimension_counts: tuple[InpnProtectedAreasCoordinateDimensionCount, ...]` | Complete joint dimension/Z/M domain in sorted tuple order, including EMPTY. |
| `validity_reason_counts: tuple[InpnProtectedAreasGeometryValidityReasonCount, ...]` | Complete NON_EMPTY validity/reason domain sorted by (is_valid, reason). |
| `catalog_total_bounds: tuple[float, float, float, float] &#124; None` | Exact physical catalog XY bounds tuple or None. |
| `observed_total_bounds: tuple[float, float, float, float] &#124; None` | Exact finite XY extrema from non-empty parsed coordinates, or None when none exist. |
| `bounds_relation: str` | Exact catalog/observed relation: EXACT_MATCH, DIFFERENT, or BOTH_NULL. |
| `raw_geometry_blob_content_sha256: str` | Canonical FID-addressed SHA of each exact complete GeoPackageBinary BLOB SHA (or null); toolchain-independent. |
| `geometry_content_sha256: str` | Canonical FID/state/type/dimension/Z/M/validity/reason/parser-WKB stream SHA; distinct from source-BLOB identity. |

### `InpnProtectedAreasGeometryProfile`

Complete immutable technical evidence; no source rows or geometries escape.

Decorators: `dataclass(frozen=True)`.

| Exact field declaration | Factual meaning |
|---|---|
| `geometry_profile_schema_version: int` | New geometry-profile schema 1. |
| `provider: str` | Exact source provider lineage from the fresh catalog. |
| `authority: str` | Exact source authority lineage from the fresh catalog. |
| `program: str` | Exact source program lineage from the fresh catalog. |
| `dataset_id: str` | Exact source dataset ID from the fresh catalog. |
| `dataset_name: str` | Exact source dataset name from the fresh catalog. |
| `declared_version: str` | Exact archive's declared source version. |
| `reference_page_url: str` | Exact approved source-reference URL lineage; not fetched by this module. |
| `archive_url: str` | Exact approved archive URL lineage; not fetched by this module. |
| `archive_filename: str` | Exact archive filename lineage. |
| `archive_size: int` | Exact verified source archive byte size. |
| `archive_sha256: str` | Exact verified source archive SHA256. |
| `source_catalog_schema_version: int` | Approved unchanged physical catalog hash schema 2. |
| `source_catalog_content_sha256: str` | Exact fresh physical catalog complete hash. |
| `sqlite_version: str` | Python sqlite3.sqlite_version used for in-memory snapshot reads. |
| `pyogrio_version: str` | Installed pyogrio.__version__; Pyogrio remains metadata-only in this module. |
| `gdal_version: str` | Installed pyogrio.__gdal_version_string__, the actual exposed GDAL accessor. |
| `shapely_version: str` | Installed shapely.__version__ used for parsing/serialization. |
| `geos_version: str` | Installed shapely.geos_version_string used for geometry evidence. |
| `pyproj_version: str` | Installed pyproj.__version__ used by canonical catalog CRS validation. |
| `geometry_encoding_schema_version: int` | Explicit parser-derived WKB encoding schema 1. |
| `geometry_encoding_contract: str` | SHAPELY_EXTENDED_WKB_LITTLE_ENDIAN_SOURCE_DIMENSION_NO_SRID_V1. |
| `layers: tuple[InpnProtectedAreasLayerGeometryProfile, ...]` | Complete immutable layer-profile tuple in catalog package/layer order. |
| `package_count: int` | Number of distinct catalog packages, recomputed from layer groups. |
| `layer_count: int` | Number of all physical layer profiles. |
| `geometry_row_count: int` | Sum of all layer feature counts; no rows are dropped or duplicated. |
| `null_geometry_count: int` | Number of SQLite NULL geometry values. |
| `empty_geometry_count: int` | Number of non-null BLOB geometries parsed as EMPTY. |
| `non_empty_geometry_count: int` | Number of non-null, non-empty parsed geometries. |
| `valid_non_empty_geometry_count: int` | Number of NON_EMPTY geometries with true Shapely validity. |
| `invalid_non_empty_geometry_count: int` | Number of NON_EMPTY geometries with false Shapely validity; unrepaired factual evidence. |
| `has_z_geometry_count: int` | Number of non-null geometries with actual Z, including dimensional EMPTY geometries. |
| `has_m_geometry_count: int` | Number of non-null geometries with actual M, including dimensional EMPTY geometries. |
| `total_coordinate_count: int` | Complete present coordinate count; NULL and EMPTY contribute zero. |
| `complete_geometry_profile_content_sha256: str` | Canonical SHA256 binding every other portable profile field, including toolchain identity. |

## 5. Every helper and public function

Signatures are source-derived. The contracts below describe each local definition; qualified imported ownership is listed separately above.

### `_require_gpkg_geometry_type`


```python
def _require_gpkg_geometry_type(value: object, label: str) -> str | None:
```

Requires an exact built-in string matching one of the eight canonical uppercase declarations in the private immutable core-type table. It returns the matching concrete Shapely family, or None for the declaration-only GEOMETRY supertype; lowercase, edge whitespace, unknown, extended, and non-string values fail with the controlled geometry error.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
        f"{label}: exact supported uppercase GeoPackage geometry type required"
    )
```

### `_require_geometry_assignable`


```python
def _require_geometry_assignable(
    declared: object, observed: object, label: str
) -> None:
```

Revalidates the declared GeoPackage type, requires an exact supported observed Shapely type string, and rejects any mismatch with a concrete declaration. GEOMETRY accepts all seven core roots. The same helper binds raw WKB root evidence before Shapely parsing and intrinsic observed-type domains; Z/M is deliberately not part of assignability.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: unsupported Shapely WKB geometry type"
        )

raise InpnProtectedAreasGeometryProfileError(
            f"{label}: observed {observed} is not assignable to declared {declared}"
        )
```

### `_open_gpkg_sqlite_snapshot`


```python
@contextmanager
def _open_gpkg_sqlite_snapshot(
    package_bytes: bytes,
    relative_path: str,
) -> Iterator[sqlite3.Connection]:
```

Requires exact nonempty built-in bytes, opens only :memory:, deserializes those exact bytes, verifies query_only=ON, disables/verifies trusted_schema where supported, and forces schema parsing before yielding. Database/overflow/type/value errors become the chained geometry error; closure is guaranteed and the same failure families are controlled if closure raises.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise ValueError("SQLite package snapshot must be exact non-empty bytes")

raise ValueError("SQLite query_only mode was not enabled")

raise ValueError("SQLite trusted_schema mode was not disabled")

raise

raise InpnProtectedAreasGeometryProfileError(
            f"package {relative_path}: SQLite byte-snapshot operation failed"
        ) from error

raise InpnProtectedAreasGeometryProfileError(
                    f"package {relative_path}: SQLite snapshot closure failed"
                ) from error
```

### `_quote_sqlite_identifier`


```python
def _quote_sqlite_identifier(value: object) -> str:
```

Requires an exact nonempty str without any Unicode Cc control character, preserves spelling, doubles embedded quotes, and encloses the result in SQLite double quotes.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            "SQLite identifier must be exact non-empty text without control characters"
        )
```

### `_sqlite_rows`


```python
def _sqlite_rows(
    connection: sqlite3.Connection,
    statement: str,
    parameters: tuple[object, ...] = (),
) -> tuple[tuple[object, ...], ...]:
```

Executes a LandScout-controlled statement with a separate parameter tuple, fetches all rows, closes the cursor, requires exact list-of-tuple DB-API output, and returns an immutable tuple.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError("SQLite rows are malformed")
```

### `_require_physical_sqlite_table`


```python
def _require_physical_sqlite_table(
    connection: sqlite3.Connection,
    table_name: str,
    label: str,
    *,
    require_rowid: bool,
) -> None:
```

Combines parameterized sqlite_schema identity with PRAGMA main.table_list to reject views, virtual/shadow tables, ambiguity, and—when required—WITHOUT ROWID feature tables.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: {table_name} must be one physical table; views are unsupported"
        )

raise InpnProtectedAreasGeometryProfileError(
            f"{label}: ordinary rowid feature table is required; "
            "virtual/shadow or WITHOUT ROWID feature tables are unsupported"
        )
```

### `_read_gpkg_layer_metadata`


```python
def _read_gpkg_layer_metadata(
    connection: sqlite3.Connection,
    relative_path: str,
    layer: InpnProtectedAreasLayerCatalog,
) -> _GpkgLayerMetadata:
```

Requires a spatial catalog layer with CRS and physical metadata tables. Exact parameterized contents/geometry-column rows must agree on feature-table and signed-int32 SRS; Z/M flags are exact 0/1/2 and proven integer EPSG authority must match. The geometry_type_name is checked against the exact uppercase core vocabulary. table_info discovers one distinct geometry column and requires its SQL declared type to be an exact built-in string equal to that GeoPackage declaration, without casefolding or coercion. One INTEGER PRIMARY KEY is required; index_list excludes non-rowid-alias DESC keys. Returns private source spellings without reading attributes.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise ValueError("catalog layer must be spatial with proven CRS")

raise ValueError(
                "exactly one matching gpkg_contents feature entry is required"
            )

raise ValueError(
                "exactly one matching gpkg_geometry_columns entry is required"
            )

raise ValueError("GeoPackage geometry metadata text is malformed")

raise ValueError("GeoPackage table identity differs from catalog layer")

raise ValueError("GeoPackage SRS ID must be an exact signed int32")

raise ValueError("gpkg_contents and gpkg_geometry_columns SRS IDs differ")

raise ValueError("GeoPackage z/m flags must be exact 0, 1, or 2")

raise ValueError("GeoPackage dimension metadata is malformed")

raise ValueError("GeoPackage SRS ID differs from catalog EPSG authority")

raise ValueError("feature table column metadata is malformed")

raise ValueError("feature column or primary-key metadata is malformed")

raise ValueError("exact geometry column is missing or ambiguous")

raise ValueError(
                "SQL geometry column type must exactly match GeoPackage declaration"
            )

raise ValueError("feature table must have exactly one INTEGER PRIMARY KEY")

raise ValueError(
                "INTEGER PRIMARY KEY must alias rowid; column DESC is unsupported"
            )

raise ValueError("FID and geometry must be distinct source columns")

raise

raise InpnProtectedAreasGeometryProfileError(
            f"{label}: GeoPackage table metadata failed validation: {error}"
        ) from error
```

### `_read_gpkg_geometry_rows`


```python
def _read_gpkg_geometry_rows(
    connection: sqlite3.Connection,
    metadata: _GpkgLayerMetadata,
    relative_path: str,
    expected_count: int,
) -> tuple[tuple[int, bytes | None], ...]:
```

Verifies expected count and active query-only state, constructs the exactly quoted two-column FID/geometry SELECT, requires exact row count, rejects malformed shapes/duplicate/non-built-in-int FIDs/non-bytes BLOBs, and returns exact identifiers/BLOBs sorted numerically without renumbering.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise ValueError(
                "expected geometry row count must be an exact non-negative integer"
            )

raise ValueError("geometry rows require a query-only SQLite connection")

raise ValueError("geometry row count differs from physical catalog")

raise ValueError("geometry query must return exactly FID and geometry")

raise ValueError(f"FID at row {position} must be an exact integer")

raise ValueError(f"duplicate FID {fid}")

raise ValueError(
                    f"FID {fid}: geometry must be SQLite NULL or exact BLOB bytes"
                )

raise

raise InpnProtectedAreasGeometryProfileError(
            f"{label}: geometry-only SQLite read failed: {error}"
        ) from error
```

### `_wkb_shape`


```python
def _wkb_shape(wkb: bytes, offset: int = 0) -> tuple[_WkbShape, int]:
```

Recursively validates the exact core ISO WKB framing before GEOS: independent endian marker, dimensional type word, standard type 1–7, coordinate/ring/member lengths, child type relationships, and available-byte limits. EWKB flags and unsupported types fail; the returned byte offset proves full consumption.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise ValueError("embedded WKB header is truncated or has invalid byte order")

raise ValueError("Standard GeoPackageBinary requires ISO WKB, not EWKB flags")

raise ValueError("unsupported embedded WKB dimensional type")

raise ValueError("unsupported embedded WKB geometry type")

raise ValueError("embedded WKB ring count exceeds available bytes")

raise ValueError("embedded WKB ring coordinates are truncated")

raise ValueError("embedded WKB member count exceeds available bytes")

raise ValueError("embedded WKB multi-geometry member type differs")

raise ValueError("embedded WKB coordinates are truncated")
```

### `_assert_wkb_dimensions_preserved`


```python
def _assert_wkb_dimensions_preserved(
    shape: _WkbShape,
    geometry: BaseGeometry,
) -> tuple[bool, bool]:
```

Checks real parsed geometry type against the original WKB tree using the private immutable core-type mapping, verifies child counts, and recursively verifies declared Z/M evidence at every node, rejecting parser loss rather than trusting the outer dimensional count alone.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise ValueError("WKB parser changed the geometry type")

raise ValueError("WKB parser changed the geometry member count")

raise ValueError("WKB parser did not preserve the source Z/M dimensions")
```

### `_parse_gpkg_geometry_blob`


```python
def _parse_gpkg_geometry_blob(
    blob: object,
    metadata: _GpkgLayerMetadata,
    relative_path: str,
    fid: int,
) -> _ParsedGpkgGeometry:
```

Validates exact Standard GeoPackageBinary type/length/magic/version/reserved/extended flags, envelope code/byte order/framing/length, signed SRS, empty-envelope rule, and exact embedded-WKB consumption. After _wkb_shape proves the root type ID, its mapped family must be assignable to the declared GeoPackage type before shapely.from_wkb is called. Parses only WKB with on_invalid='raise', requires one exact core Shapely scalar, verifies recursive type/dimensions, header-empty agreement, and prohibited/mandatory/optional Z/M declarations. Numerical envelope doubles are not checked against WKB coordinates. Parse/shape/struct/recursion failures retain their chained cause.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise ValueError("GeoPackage geometry BLOB must be exact built-in bytes")

raise ValueError("GeoPackageBinary header is truncated")

raise ValueError("GeoPackageBinary magic must be GP")

raise ValueError("unsupported GeoPackageBinary version")

raise ValueError("GeoPackageBinary reserved flag bits must be zero")

raise ValueError("Extended GeoPackageBinary is unsupported")

raise ValueError("invalid GeoPackageBinary envelope code")

raise ValueError(
                "GeoPackageBinary header SRS ID differs from geometry metadata"
            )

raise ValueError("empty GeoPackageBinary must have no envelope")

raise ValueError("GeoPackageBinary envelope is truncated")

raise ValueError("GeoPackageBinary embedded WKB is missing")

raise ValueError("embedded WKB has trailing bytes")

raise ValueError("WKB parser must return an exact scalar Shapely geometry")

raise ValueError(
                "GeoPackageBinary empty flag differs from parsed WKB state"
            )

raise ValueError(f"invalid {ordinate} metadata declaration")

raise ValueError(
                    f"parsed {ordinate} dimension violates GeoPackage declaration"
                )

raise

raise InpnProtectedAreasGeometryProfileError(
            f"{label}: malformed GeoPackage geometry: {error}"
        ) from error
```

### `_canonical_json_bytes`


```python
def _canonical_json_bytes(value: object) -> bytes:
```

Serializes finite portable evidence as UTF-8 JSON with sort_keys=True, compact separators, ensure_ascii=False, allow_nan=False; invalid serialization becomes the controlled geometry error.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            "non-canonical geometry JSON"
        ) from error
```

### `_canonical_json_sha256`


```python
def _canonical_json_sha256(value: object, label: str = "geometry evidence") -> str:
```

Returns lowercase SHA256 of the canonical JSON bytes; integer-list serialization intentionally matches the existing attribute FID hash contract.

### `_profile_payload`


```python
def _profile_payload(profile: InpnProtectedAreasGeometryProfile) -> dict[str, object]:
```

Uses a local dataclass projection containing every public portable field except the complete hash itself; mutable payloads are temporary construction data and never returned as trust-bearing profile state.

### `_profile_content_sha256`


```python
def _profile_content_sha256(profile: InpnProtectedAreasGeometryProfile) -> str:
```

Hashes that complete portable projection, including source/catalog/toolchain/encoding/layers/aggregate evidence.

### `_coordinate_evidence`


```python
def _coordinate_evidence(
    geometry: BaseGeometry,
    label: str,
) -> tuple[int, tuple[float, float, float, float] | None]:
```

Returns zero/no bounds for EMPTY. Recursively visits collection children and polygon rings so mixed-dimensional collections do not manufacture absent-ordinate NaNs. Leaf coordinate extraction uses actual has_z/has_m flags, requires the exact ordinate width and every present coordinate finite, and derives XY bounds without reprojection.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: invalid coordinate layout"
        )

raise InpnProtectedAreasGeometryProfileError(
            f"{label}: non-finite present ordinate(s) {','.join(bad)}"
        )

raise InpnProtectedAreasGeometryProfileError(
            f"{label}: non-empty geometry has no coordinates"
        )
```

### `_merge_bounds`


```python
def _merge_bounds(
    bounds: tuple[tuple[float, float, float, float], ...],
) -> tuple[float, float, float, float] | None:
```

Aggregates already-validated XY bounds by exact minima/maxima; an empty bounds sequence remains None.

### `_bounds_relation`


```python
def _bounds_relation(
    catalog: tuple[float, float, float, float] | None,
    observed: tuple[float, float, float, float] | None,
) -> str:
```

Returns BOTH_NULL only when both tuples are absent, EXACT_MATCH on exact tuple equality, and DIFFERENT otherwise; no tolerance is introduced.

### `_profile_layer`


```python
def _profile_layer(
    connection: sqlite3.Connection,
    package: InpnProtectedAreasGeoPackageCatalog,
    layer: InpnProtectedAreasLayerCatalog,
) -> InpnProtectedAreasLayerGeometryProfile:
```

Discovers physical metadata and reads canonical FID/BLOB rows, tracks NULL/EMPTY/NON_EMPTY separately, accumulates exact type/dimension/Z/M and non-empty validity/reason domains, counts all coordinates, and computes observed bounds. Incremental canonical JSON hashes bind exact full-BLOB SHA evidence separately from explicit parser-derived WKB evidence. Returns one immutable catalog-bound layer record.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
                f"{label} FID {fid}: invalid parser WKB"
            )
```

### `_build_profile`


```python
def _build_profile(
    extraction: InpnProtectedAreasExtraction,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasGeometryProfile:
```

Walks every catalog package/layer in order, matches its archive-derived extraction item, obtains one verified immutable byte snapshot, and uses one SQLite context per package. Aggregates all layer counts, records exact SQLite/Pyogrio/GDAL/Shapely/GEOS/PyProj strings and encoding identity, and calculates the complete profile hash.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
                "extraction/catalog package identity differs"
            )
```

### `_exact_text`


```python
def _exact_text(value: object, label: str) -> str:
```

Rejects anything except exact nonempty built-in text without edge whitespace; it validates identity/evidence spelling rather than silently trimming it.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact nonempty built-in string required"
        )
```

### `_exact_int`


```python
def _exact_int(value: object, label: str, minimum: int = 0) -> int:
```

Rejects bool/subclasses/non-integers and integers below the specified lower bound; the default minimum is zero.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact integer >= {minimum} required"
        )
```

### `_exact_sha`


```python
def _exact_sha(value: object, label: str) -> None:
```

Requires an exact built-in lowercase 64-hex SHA256 string.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: canonical SHA256 required"
        )
```

### `_unique_ordered`


```python
def _unique_ordered(keys: tuple[Any, ...], label: str) -> None:
```

Requires a tuple's keys to equal their sorted order and to be unique; used for complete canonical domains and package ordering.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: duplicate or unordered domain"
        )
```

### `_unique_names`


```python
def _unique_names(names: tuple[str, ...], label: str) -> None:
```

Rejects exact, Unicode-NFKC, and casefold identity collisions while leaving accepted source spellings unchanged.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact/NFKC/casefold identity collision"
        )
```

### `_validate_bounds`


```python
def _validate_bounds(value: object, label: str) -> None:
```

Accepts None or exactly four built-in finite floats in a tuple, and rejects reversed XY extrema.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact finite float bounds tuple required"
        )

raise InpnProtectedAreasGeometryProfileError(f"{label}: reversed bounds")
```

### `_validate_layer_intrinsic`


```python
def _validate_layer_intrinsic(layer: object) -> InpnProtectedAreasLayerGeometryProfile:
```

Proves exact frozen layer/domain classes, shared extraction-owned .gpkg path grammar, table/column/driver identity, a supported canonical GeoPackage declaration, and assignability of every observed type to that declaration. Declaration validation also applies to NULL-only layers with empty type domains. It proves FID count/extrema/inclusive capacity and empty hashes, signed SRS/CRS canonicality, Z/M flags, count equations, positive ordered complete domains, bounds and exact relation, and component-SHA syntax. The catalog-owned _validated_bounds rule is also applied to empty/populated feature counts; comparison-equal forged catalog bounds cannot evade that physical metadata contract. Non-empty source streams are not reconstructed here.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            "exact geometry layer profile required"
        )

raise InpnProtectedAreasGeometryProfileError(
            "invalid canonical package path"
        ) from error

raise InpnProtectedAreasGeometryProfileError(
            "package path requires GeoPackage suffix"
        )

raise InpnProtectedAreasGeometryProfileError(
            "only physical GPKG feature tables supported"
        )

raise InpnProtectedAreasGeometryProfileError(
            "FID and geometry columns must differ"
        )

raise InpnProtectedAreasGeometryProfileError("FID/feature count mismatch")

raise InpnProtectedAreasGeometryProfileError("empty FID range must be null")

raise InpnProtectedAreasGeometryProfileError(
                    "invalid empty stream hash"
                )

raise InpnProtectedAreasGeometryProfileError("exact FID extrema required")

raise InpnProtectedAreasGeometryProfileError("FID range is impossible")

raise InpnProtectedAreasGeometryProfileError(
            "GeoPackage SRS exceeds signed int32"
        )

raise InpnProtectedAreasGeometryProfileError("invalid GeoPackage Z/M flag")

raise InpnProtectedAreasGeometryProfileError("invalid catalog CRS") from error

raise InpnProtectedAreasGeometryProfileError("non-canonical catalog CRS")

raise InpnProtectedAreasGeometryProfileError(
            "GeoPackage SRS differs from catalog EPSG"
        )

raise InpnProtectedAreasGeometryProfileError(
            "geometry count equations are inconsistent"
        )

raise InpnProtectedAreasGeometryProfileError("coordinate count is inconsistent")

raise InpnProtectedAreasGeometryProfileError(
                f"{name}: exact immutable domain required"
            )

raise InpnProtectedAreasGeometryProfileError(
                "invalid dimension/Z/M domain types"
            )

raise InpnProtectedAreasGeometryProfileError(
                "impossible dimension/Z/M relationship"
            )

raise InpnProtectedAreasGeometryProfileError(
                    "geometry dimension contradicts GeoPackage Z/M declaration"
                )

raise InpnProtectedAreasGeometryProfileError(
            "geometry/dimension domain count closure failed"
        )

raise InpnProtectedAreasGeometryProfileError(
                "validity must be an exact Boolean"
            )

raise InpnProtectedAreasGeometryProfileError(
            "validity domain count closure failed"
        )

raise InpnProtectedAreasGeometryProfileError(
            "catalog bounds/feature count relationship is inconsistent"
        ) from error

raise InpnProtectedAreasGeometryProfileError(
            "observed bounds/non-empty count mismatch"
        )

raise InpnProtectedAreasGeometryProfileError("incorrect bounds relation")
```

### `_validate_profile_intrinsic`


```python
def _validate_profile_intrinsic(profile: object) -> InpnProtectedAreasGeometryProfile:
```

Proves exact profile/schema/encoding/toolchain/source scalar types, nonempty immutable layers, contiguous lexical package/layer groups, repeated package facts, identity uniqueness, every aggregate equation, and complete canonical-hash closure. It cannot establish non-empty raw/parser stream content without physical rows.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            "exact InpnProtectedAreasGeometryProfile required"
        )

raise InpnProtectedAreasGeometryProfileError(
                f"{name}: invalid schema version"
            )

raise InpnProtectedAreasGeometryProfileError(
            "geometry encoding contract mismatch"
        )

raise InpnProtectedAreasGeometryProfileError(
            "layers must be an exact non-empty tuple"
        )

raise InpnProtectedAreasGeometryProfileError(
                    "package positions/groups must be contiguous"
                )

raise InpnProtectedAreasGeometryProfileError(
                "inconsistent repeated package metadata"
            )

raise InpnProtectedAreasGeometryProfileError(
                "layer positions must be contiguous"
            )

raise InpnProtectedAreasGeometryProfileError(
                f"{name}: aggregate count mismatch"
            )

raise InpnProtectedAreasGeometryProfileError(
            "complete geometry profile SHA256 mismatch"
        )
```

### `_validate_profile_catalog_contract`


```python
def _validate_profile_catalog_contract(
    profile: InpnProtectedAreasGeometryProfile,
    catalog: InpnProtectedAreasCatalog,
) -> None:
```

Before any SQLite geometry-row read, exact-compares source/archive/catalog summary and all package/layer identity/order/count/type/CRS/bounds fields with the freshly rebuilt physical catalog.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            "geometry profile source/catalog identity mismatch"
        )

raise InpnProtectedAreasGeometryProfileError(
            "geometry profile catalog layer inventory mismatch"
        )

raise InpnProtectedAreasGeometryProfileError(
                "geometry profile package/layer catalog mismatch"
            )
```

### `_prepare_inputs`


```python
def _prepare_inputs(
    extraction: object,
    config: object,
    catalog: object,
) -> tuple[
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasCatalog,
]:
```

Reuses the existing attribute module's source-only exact-type/config/extraction/catalog preparation boundary under a local alias; no attribute reader is invoked. Translates its controlled error into the geometry error with chained cause.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            f"geometry source inputs invalid: {error}"
        ) from error
```

### `_build_with_postconditions`


```python
def _build_with_postconditions(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasGeometryProfile:
```

Builds and intrinsically checks geometry evidence, then revalidates extraction and freshly rebuilds the catalog; rejects any final identity or physical metadata change before returning the profile.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
            "INPN source changed during geometry profiling"
        ) from error

raise InpnProtectedAreasGeometryProfileError(
            "INPN source/catalog changed during geometry profiling"
        )
```

### `build_inpn_protected_areas_geometry_profile`


```python
def build_inpn_protected_areas_geometry_profile(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasGeometryProfile:
```

Public source-complete entry: reconstructs/validates inputs, profiles all fresh archive-bound package bytes, requires final extraction/catalog postconditions, and exposes only immutable factual geometry evidence under one controlled error type.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise

raise InpnProtectedAreasGeometryProfileError(
            "INPN geometry profile cannot be built safely"
        ) from error
```

### `validate_inpn_protected_areas_geometry_profile`


```python
def validate_inpn_protected_areas_geometry_profile(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
    profile: InpnProtectedAreasGeometryProfile,
) -> None:
```

Public independent validator: intrinsically validates supplied evidence, reconstructs fresh source/catalog authority, performs cheap catalog preflight, physically rebuilds every field/hash with postconditions, and requires exact dataclass equality. A caller-rehashed forgery cannot override source bytes.

Direct raise statements (enclosing guards are in the exact source snapshot):


```python
raise InpnProtectedAreasGeometryProfileError(
                "geometry profile differs from independently rebuilt physical evidence"
            )

raise

raise InpnProtectedAreasGeometryProfileError(
            "INPN geometry profile validation failed safely"
        ) from error
```

## 6. Binary identity, dimensions, and geometry facts

### Declared metadata, SQL declaration, and actual WKB family

The three physical checks are distinct: `gpkg_geometry_columns.geometry_type_name` uses the exact supported uppercase vocabulary; the geometry-column row in `PRAGMA table_info` must have an identical exact built-in SQL type string; the parsed ISO WKB root family must be assignable to that declaration before GEOS conversion. The intrinsic layer check repeats declaration/domain assignability without reading rows. These implement the relevant core-type relationships in [GeoPackage 1.4 requirements 25, 31, and 32](https://www.geopackage.org/spec140/).

| Canonical GeoPackage and SQL declaration | Allowed actual WKB / observed Shapely family |
|---|---|
| `GEOMETRY` | Any of the seven supported core families below |
| `POINT` | `Point` |
| `LINESTRING` | `LineString` |
| `POLYGON` | `Polygon` |
| `MULTIPOINT` | `MultiPoint` |
| `MULTILINESTRING` | `MultiLineString` |
| `MULTIPOLYGON` | `MultiPolygon` |
| `GEOMETRYCOLLECTION` | `GeometryCollection` |

No casefold equivalence, coercion, or extended/non-linear type is accepted. Z/M presence does not alter the root family. SQL NULL has no WKB type to compare; EMPTY still has its WKB type. A NULL-only layer still requires a valid declaration. Rehashing a caller-forged declaration/domain mismatch cannot make it intrinsically valid.

### Header framing versus numerical envelope semantics

GeoPackageBinary envelope code, byte order, framing, and length are validated. Header doubles are decoded but not verified numerically against WKB coordinates. Observed geometry bounds are independently calculated from parsed non-empty coordinates and compared with the physical catalog bounds; that comparison is not an envelope-value verification.

Standard GeoPackageBinary ≠ embedded WKB ≠ parser-derived canonical WKB. The complete BLOB includes ASCII GP, version 0, flags, signed int32 SRS, optional envelope, and embedded WKB. Reserved and Extended flags, envelope codes 5–7, truncated headers/envelopes, missing/trailing WKB, unsupported non-core geometry types, and non-ISO EWKB flags fail. Header and WKB endianness are independent. EMPTY requires envelope code 0 and exact parsed empty agreement; SQL NULL has no BLOB, type, dimension, validity, or parser WKB. Header SRS equals geometry metadata and proven integer EPSG authority. Every non-null geometry obeys prohibited/mandatory/optional Z/M declarations.

Recursive raw-WKB framing proves parsed type/member/Z/M preservation rather than assuming GEOS retained every declared dimension. Complete type and dimension domains include EMPTY; validity/reason domains include only NON_EMPTY. Coordinate extraction inspects only present XY/Z/M ordinates and traverses polygon rings/collection children so absent mixed dimensions are not fabricated as NaNs. Every present ordinate must be finite. Invalid but parseable topology is retained with its exact reason; no make_valid, buffer, normalize, precision change, simplification, snapping, overlay, or reprojection is permitted.

Observed bounds use exact XY extrema from NON_EMPTY coordinates; NULL and EMPTY do not contribute. Catalog CRS and bounds remain independently retained, with no coordinate-range inference. EXACT_MATCH/DIFFERENT/BOTH_NULL use exact comparison, never a tolerance or environmental decision.

## 7. Exact portable hash algorithms

All canonical JSON uses sorted keys, compact separators, preserved Unicode, UTF-8, and allow_nan=False. Rows are sorted numerically by exact physical FID without renumbering.

| Evidence | Exact canonical per-row input | Meaning |
|---|---|
| FID sequence | Complete JSON array of sorted integer FIDs | Same integer-list encoding as the attribute profile. |
| Raw BLOB stream | `[FID, null]` or `[FID, SHA256(exact complete GeoPackageBinary BLOB)]` | Toolchain-independent raw geometry-byte identity. |
| Parser stream | `[FID, state, geometry_type, coordinate_dimension, has_z, has_m, validity, validity_reason, canonical_WKB_hex]` | Parser-derived structural evidence, not original BLOB identity. |

NULL uses state NULL and null for all seven geometry/validity/WKB fields; EMPTY retains type/dimension/Z/M/WKB while validity/reason are null. NON_EMPTY retains every field. WKB explicitly uses hex=True, output_dimension=actual dimension, byte_order=1, include_srid=False, flavor=extended; it is not normalized. Raw/parser layer streams are incrementally hashed as the exact compact JSON array, preserving deterministic empty-array hashes.

The complete profile hashes every portable dataclass field except its own hash: schema, source/archive/catalog locks, SQLite/Pyogrio/GDAL/Shapely/GEOS/PyProj versions, encoding identity, all ordered package/layer facts and domains, CRS, bounds, FIDs, component hashes, and aggregates. Absolute paths, cache roots, cache_hit, timing, user/machine identifiers, database state, raw bytes, and geometry objects are absent.

STEP 7F.1B.3.1 adds validation without changing public fields, canonical payloads, raw/parser stream definitions, geometry-profile schema 1, or encoding schema 1/contract. Controlled offline revalidation of the same valid EP snapshot retains exact complete geometry-profile SHA256 `997c8c27cbbedb2860778386b3f2eb5afa9f64de6ad07e41fc67b4cec9060ee7`: all 15 layers declare `MULTIPOLYGON` and contain only observed `MultiPolygon`, totaling 11,381 rows. No hash migration is required.

## 8. Intrinsic versus physical validation and TOCTOU

Intrinsic validation proves exact immutable runtime types, authoritative package-path grammar, contiguous lexical package/layer grouping, consistent repeated package facts, exact/NFKC/casefold uniqueness, FID extrema/inclusive capacity, canonical CRS/bounds, supported GeoPackage declarations and observed-root assignability, Z/M flag and domain/count relationships, component-SHA syntax, deterministic empty-component hashes, aggregate closure, and complete profile hash. It cannot reconstruct non-empty FID/raw/parser hashes without original rows.

Public validation intrinsically validates first, reconstructs config/extraction authority and independently rebuilds the physical catalog, rejects catalog-bound mismatches before SQLite geometry-row reads, physically rebuilds every geometry fact and hash, and exact-compares all fields. Final extraction/catalog reconstruction must equal initial evidence. Temporary physical path replacement after deserialization cannot inject alternate geometry; persistent mutation fails before successful return. Caller-coordinated profile/hash changes do not replace this physical proof.

## 9. Public exports, tests, and semantic boundary


```python
__all__ = [
    "InpnProtectedAreasCoordinateDimensionCount",
    "InpnProtectedAreasGeometryProfile",
    "InpnProtectedAreasGeometryProfileError",
    "InpnProtectedAreasGeometryTypeCount",
    "InpnProtectedAreasGeometryValidityReasonCount",
    "InpnProtectedAreasLayerGeometryProfile",
    "build_inpn_protected_areas_geometry_profile",
    "validate_inpn_protected_areas_geometry_profile",
]
```

`landscout.sources` re-exports these eight approved names with their original qualified ownership. Constants, SQLite handles/readers, parser records, raw BLOB/WKB helpers, payloads, and intrinsic validators remain private. The companion for `tests/unit/test_inpn_protected_areas_geometry_fr.py` documents permanent real-parser M/ZM/EMPTY regressions, metadata/header/finiteness/identity cases, zero-attribute reader sentinels, hashes, forgeries, and TOCTOU tests.

This is EP geometry technical-quality reconnaissance only. It does not interpret type_espace, protected-area categories, legal regimes, Natura 2000, or ZNIEFF; normalize/repair/reproject geometry; load parcels; intersect; measure environmental distance; exclude; score; or rank. The sig_tadl EPSG:32753/coordinate-bounds observation stays unresolved, without CRS substitution.

## 10. Exact complete current file content


```python
"""Source-bound technical geometry evidence from immutable INPN EP bytes."""

from __future__ import annotations

import json
import math
import re
import sqlite3
import struct
import unicodedata
from collections import Counter
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from pathlib import PurePosixPath
from types import MappingProxyType
from typing import Any

import numpy as np
import pyogrio  # type: ignore[import-untyped]
import pyproj
import shapely  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.sources.inpn_protected_areas_attributes_fr import (
    InpnProtectedAreasAttributeProfileError,
)
from landscout.sources.inpn_protected_areas_attributes_fr import (
    _prepare_inputs as _prepare_source_inputs,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    CATALOG_HASH_SCHEMA_VERSION,
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasGeoPackageCatalog,
    InpnProtectedAreasLayerCatalog,
    _canonical_crs,
    _read_verified_package_bytes,
    _validated_bounds,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    _validate_inventory_relative_path,
    validate_inpn_protected_areas_extraction,
)


class InpnProtectedAreasGeometryProfileError(ValueError):
    """Raised when exact source-bound geometry evidence cannot be proven."""


# ID 0 is declaration-only: the raw WKB parser still accepts only core IDs 1..7.
_CORE_GEOMETRY_TYPES: MappingProxyType[int, tuple[str, str | None]] = MappingProxyType(
    {
        0: ("GEOMETRY", None),
        1: ("POINT", "Point"),
        2: ("LINESTRING", "LineString"),
        3: ("POLYGON", "Polygon"),
        4: ("MULTIPOINT", "MultiPoint"),
        5: ("MULTILINESTRING", "MultiLineString"),
        6: ("MULTIPOLYGON", "MultiPolygon"),
        7: ("GEOMETRYCOLLECTION", "GeometryCollection"),
    }
)


def _require_gpkg_geometry_type(value: object, label: str) -> str | None:
    """Require an exact core declaration; return its specific observed type, if any."""
    if type(value) is str:
        for declared, observed in _CORE_GEOMETRY_TYPES.values():
            if value == declared:
                return observed
    raise InpnProtectedAreasGeometryProfileError(
        f"{label}: exact supported uppercase GeoPackage geometry type required"
    )


def _require_geometry_assignable(
    declared: object, observed: object, label: str
) -> None:
    """Bind a supported observed core root to its declaration, independent of Z/M."""
    expected = _require_gpkg_geometry_type(declared, label)
    if type(observed) is not str or not any(
        observed == name for _, name in _CORE_GEOMETRY_TYPES.values()
    ):
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: unsupported Shapely WKB geometry type"
        )
    if expected is not None and observed != expected:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: observed {observed} is not assignable to declared {declared}"
        )


@dataclass(frozen=True)
class _GpkgLayerMetadata:
    """Private metadata for one physical ordinary GeoPackage feature table."""

    table_name: str
    table_kind: str
    fid_column_name: str
    geometry_column_name: str
    geometry_type_name: str
    srs_id: int
    z_flag: int
    m_flag: int


@dataclass(frozen=True)
class _ParsedGpkgGeometry:
    """Temporary raw-header/parser state, never retained in public evidence."""

    geometry: BaseGeometry
    embedded_wkb: bytes
    srs_id: int
    envelope_code: int
    envelope: tuple[float, ...]
    header_little_endian: bool
    is_empty: bool


@dataclass(frozen=True)
class _WkbShape:
    """Embedded-WKB framing and declared dimensions before GEOS conversion."""

    type_id: int
    has_z: bool
    has_m: bool
    children: tuple[_WkbShape, ...]


@contextmanager
def _open_gpkg_sqlite_snapshot(
    package_bytes: bytes,
    relative_path: str,
) -> Iterator[sqlite3.Connection]:
    """Deserialize exact verified bytes into a closed-after-use query-only database."""

    connection: sqlite3.Connection | None = None
    try:
        if type(package_bytes) is not bytes or not package_bytes:
            raise ValueError("SQLite package snapshot must be exact non-empty bytes")
        connection = sqlite3.connect(":memory:")
        connection.deserialize(package_bytes)
        connection.execute("PRAGMA query_only = ON")
        if connection.execute("PRAGMA query_only").fetchone() != (1,):
            raise ValueError("SQLite query_only mode was not enabled")
        trusted_schema = connection.execute("PRAGMA trusted_schema").fetchone()
        if trusted_schema is not None:
            connection.execute("PRAGMA trusted_schema = OFF")
            if connection.execute("PRAGMA trusted_schema").fetchone() != (0,):
                raise ValueError("SQLite trusted_schema mode was not disabled")
        # Force SQLite to parse the snapshot before exposing a usable connection.
        connection.execute("SELECT name FROM sqlite_schema LIMIT 0").fetchall()
        yield connection
    except InpnProtectedAreasGeometryProfileError:
        raise
    except (sqlite3.DatabaseError, OverflowError, TypeError, ValueError) as error:
        raise InpnProtectedAreasGeometryProfileError(
            f"package {relative_path}: SQLite byte-snapshot operation failed"
        ) from error
    finally:
        if connection is not None:
            try:
                connection.close()
            except (
                sqlite3.DatabaseError,
                OverflowError,
                TypeError,
                ValueError,
            ) as error:
                raise InpnProtectedAreasGeometryProfileError(
                    f"package {relative_path}: SQLite snapshot closure failed"
                ) from error


def _quote_sqlite_identifier(value: object) -> str:
    """Quote one exact source identifier without changing its spelling."""

    if (
        type(value) is not str
        or not value
        or any(unicodedata.category(character) == "Cc" for character in value)
    ):
        raise InpnProtectedAreasGeometryProfileError(
            "SQLite identifier must be exact non-empty text without control characters"
        )
    return '"' + value.replace('"', '""') + '"'


def _sqlite_rows(
    connection: sqlite3.Connection,
    statement: str,
    parameters: tuple[object, ...] = (),
) -> tuple[tuple[object, ...], ...]:
    """Collect rows from a LandScout-controlled metadata or two-column statement."""

    cursor = connection.execute(statement, parameters)
    try:
        result = cursor.fetchall()
    finally:
        cursor.close()
    if type(result) is not list or any(type(row) is not tuple for row in result):
        raise InpnProtectedAreasGeometryProfileError("SQLite rows are malformed")
    return tuple(result)


def _require_physical_sqlite_table(
    connection: sqlite3.Connection,
    table_name: str,
    label: str,
    *,
    require_rowid: bool,
) -> None:
    """Prove ordinary table identity; views and virtual/shadow tables are unsupported."""

    _quote_sqlite_identifier(table_name)
    schema_rows = _sqlite_rows(
        connection,
        "SELECT type, name, tbl_name FROM sqlite_schema WHERE name = ? COLLATE BINARY",
        (table_name,),
    )
    if schema_rows != (("table", table_name, table_name),):
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: {table_name} must be one physical table; views are unsupported"
        )
    matching = tuple(
        row
        for row in _sqlite_rows(connection, "PRAGMA main.table_list")
        if len(row) >= 6 and row[0] == "main" and row[1] == table_name
    )
    if (
        len(matching) != 1
        or matching[0][2] != "table"
        or type(matching[0][4]) is not int
        or matching[0][4] not in (0, 1)
        or (require_rowid and matching[0][4] != 0)
    ):
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: ordinary rowid feature table is required; "
            "virtual/shadow or WITHOUT ROWID feature tables are unsupported"
        )


def _read_gpkg_layer_metadata(
    connection: sqlite3.Connection,
    relative_path: str,
    layer: InpnProtectedAreasLayerCatalog,
) -> _GpkgLayerMetadata:
    """Bind source table, rowid-alias FID, geometry column and declarations."""

    label = f"package {relative_path} layer {layer.layer_name}"
    try:
        if not layer.is_spatial or layer.crs_wkt is None:
            raise ValueError("catalog layer must be spatial with proven CRS")
        for table_name in ("gpkg_contents", "gpkg_geometry_columns"):
            _require_physical_sqlite_table(
                connection, table_name, label, require_rowid=False
            )
        contents = _sqlite_rows(
            connection,
            "SELECT table_name, data_type, srs_id FROM gpkg_contents "
            "WHERE table_name = ? COLLATE BINARY",
            (layer.layer_name,),
        )
        if (
            len(contents) != 1
            or len(contents[0]) != 3
            or contents[0][0] != layer.layer_name
            or contents[0][1] != "features"
            or type(contents[0][2]) is not int
        ):
            raise ValueError(
                "exactly one matching gpkg_contents feature entry is required"
            )
        geometry_rows = _sqlite_rows(
            connection,
            "SELECT table_name, column_name, geometry_type_name, srs_id, z, m "
            "FROM gpkg_geometry_columns WHERE table_name = ? COLLATE BINARY",
            (layer.layer_name,),
        )
        if len(geometry_rows) != 1 or len(geometry_rows[0]) != 6:
            raise ValueError(
                "exactly one matching gpkg_geometry_columns entry is required"
            )
        table, column, geometry_type, srs_id, z_flag, m_flag = geometry_rows[0]
        for value in (table, column, geometry_type):
            _quote_sqlite_identifier(value)
        if (
            type(table) is not str
            or type(column) is not str
            or type(geometry_type) is not str
        ):
            raise ValueError("GeoPackage geometry metadata text is malformed")
        _require_gpkg_geometry_type(geometry_type, label)
        if table != layer.layer_name:
            raise ValueError("GeoPackage table identity differs from catalog layer")
        if type(srs_id) is not int or not -(2**31) <= srs_id < 2**31:
            raise ValueError("GeoPackage SRS ID must be an exact signed int32")
        if contents[0][2] != srs_id:
            raise ValueError("gpkg_contents and gpkg_geometry_columns SRS IDs differ")
        if any(
            type(value) is not int or value not in (0, 1, 2)
            for value in (z_flag, m_flag)
        ):
            raise ValueError("GeoPackage z/m flags must be exact 0, 1, or 2")
        if type(z_flag) is not int or type(m_flag) is not int:
            raise ValueError("GeoPackage dimension metadata is malformed")
        if (
            layer.crs_authority_name == "EPSG"
            and layer.crs_authority_code is not None
            and layer.crs_authority_code.isascii()
            and layer.crs_authority_code.isdecimal()
            and srs_id != int(layer.crs_authority_code)
        ):
            raise ValueError("GeoPackage SRS ID differs from catalog EPSG authority")
        _require_physical_sqlite_table(connection, table, label, require_rowid=True)
        table_info = _sqlite_rows(
            connection, f"PRAGMA main.table_info({_quote_sqlite_identifier(table)})"
        )
        if not table_info or any(len(row) != 6 for row in table_info):
            raise ValueError("feature table column metadata is malformed")
        names: list[str] = []
        primary_columns: list[tuple[object, ...]] = []
        for row in table_info:
            name = row[1]
            _quote_sqlite_identifier(name)
            if type(name) is not str or type(row[5]) is not int or row[5] < 0:
                raise ValueError("feature column or primary-key metadata is malformed")
            names.append(name)
            if row[5] != 0:
                primary_columns.append(row)
        if len(names) != len(set(names)) or names.count(column) != 1:
            raise ValueError("exact geometry column is missing or ambiguous")
        sql_geometry_type = table_info[names.index(column)][2]
        if type(sql_geometry_type) is not str or sql_geometry_type != geometry_type:
            raise ValueError(
                "SQL geometry column type must exactly match GeoPackage declaration"
            )
        if (
            len(primary_columns) != 1
            or primary_columns[0][5] != 1
            or type(primary_columns[0][2]) is not str
            or primary_columns[0][2].upper() != "INTEGER"
        ):
            raise ValueError("feature table must have exactly one INTEGER PRIMARY KEY")
        indexes = _sqlite_rows(
            connection, f"PRAGMA main.index_list({_quote_sqlite_identifier(table)})"
        )
        if any(len(row) != 5 or row[3] == "pk" for row in indexes):
            raise ValueError(
                "INTEGER PRIMARY KEY must alias rowid; column DESC is unsupported"
            )
        fid_name = primary_columns[0][1]
        if type(fid_name) is not str or fid_name == column:
            raise ValueError("FID and geometry must be distinct source columns")
        return _GpkgLayerMetadata(
            table_name=table,
            table_kind="table",
            fid_column_name=fid_name,
            geometry_column_name=column,
            geometry_type_name=geometry_type,
            srs_id=srs_id,
            z_flag=z_flag,
            m_flag=m_flag,
        )
    except InpnProtectedAreasGeometryProfileError:
        raise
    except (
        sqlite3.DatabaseError,
        OverflowError,
        TypeError,
        ValueError,
        IndexError,
    ) as error:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: GeoPackage table metadata failed validation: {error}"
        ) from error


def _read_gpkg_geometry_rows(
    connection: sqlite3.Connection,
    metadata: _GpkgLayerMetadata,
    relative_path: str,
    expected_count: int,
) -> tuple[tuple[int, bytes | None], ...]:
    """Read exactly the physical FID and geometry BLOB, preserving immutable bytes."""

    label = f"package {relative_path} layer {metadata.table_name}"
    try:
        if type(expected_count) is not int or expected_count < 0:
            raise ValueError(
                "expected geometry row count must be an exact non-negative integer"
            )
        if connection.execute("PRAGMA query_only").fetchone() != (1,):
            raise ValueError("geometry rows require a query-only SQLite connection")
        rows = _sqlite_rows(
            connection,
            f"SELECT {_quote_sqlite_identifier(metadata.fid_column_name)}, "
            f"{_quote_sqlite_identifier(metadata.geometry_column_name)} "
            f"FROM {_quote_sqlite_identifier(metadata.table_name)}",
        )
        if len(rows) != expected_count:
            raise ValueError("geometry row count differs from physical catalog")
        result: list[tuple[int, bytes | None]] = []
        seen: set[int] = set()
        for position, row in enumerate(rows):
            if len(row) != 2:
                raise ValueError("geometry query must return exactly FID and geometry")
            fid, blob = row
            if type(fid) is not int:
                raise ValueError(f"FID at row {position} must be an exact integer")
            if fid in seen:
                raise ValueError(f"duplicate FID {fid}")
            seen.add(fid)
            if blob is not None and type(blob) is not bytes:
                raise ValueError(
                    f"FID {fid}: geometry must be SQLite NULL or exact BLOB bytes"
                )
            result.append((fid, blob))
        return tuple(sorted(result, key=lambda item: item[0]))
    except InpnProtectedAreasGeometryProfileError:
        raise
    except (sqlite3.DatabaseError, OverflowError, TypeError, ValueError) as error:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: geometry-only SQLite read failed: {error}"
        ) from error


def _wkb_shape(wkb: bytes, offset: int = 0) -> tuple[_WkbShape, int]:
    """Validate complete core WKB framing without converting source coordinates."""

    if offset + 5 > len(wkb) or wkb[offset] not in (0, 1):
        raise ValueError("embedded WKB header is truncated or has invalid byte order")
    byte_order = "<" if wkb[offset] else ">"
    raw_type = struct.unpack_from(byte_order + "I", wkb, offset + 1)[0]
    offset += 5
    if raw_type & 0xE0000000:
        raise ValueError("Standard GeoPackageBinary requires ISO WKB, not EWKB flags")
    dimension_code, type_id = divmod(raw_type, 1000)
    if dimension_code not in (0, 1, 2, 3):
        raise ValueError("unsupported embedded WKB dimensional type")
    has_z = dimension_code in (1, 3)
    has_m = dimension_code in (2, 3)
    if type_id not in (1, 2, 3, 4, 5, 6, 7):
        raise ValueError("unsupported embedded WKB geometry type")
    coordinate_size = 8 * (2 + int(has_z) + int(has_m))
    children: list[_WkbShape] = []
    if type_id == 1:
        offset += coordinate_size
    else:
        count = struct.unpack_from(byte_order + "I", wkb, offset)[0]
        offset += 4
        if type_id == 2:
            offset += count * coordinate_size
        elif type_id == 3:
            if count > (len(wkb) - offset) // 4:
                raise ValueError("embedded WKB ring count exceeds available bytes")
            for _ in range(count):
                points = struct.unpack_from(byte_order + "I", wkb, offset)[0]
                offset += 4 + points * coordinate_size
                if offset > len(wkb):
                    raise ValueError("embedded WKB ring coordinates are truncated")
        else:
            if count > (len(wkb) - offset) // 5:
                raise ValueError("embedded WKB member count exceeds available bytes")
            for _ in range(count):
                child, offset = _wkb_shape(wkb, offset)
                if type_id != 7 and child.type_id != type_id - 3:
                    raise ValueError("embedded WKB multi-geometry member type differs")
                children.append(child)
    if offset > len(wkb):
        raise ValueError("embedded WKB coordinates are truncated")
    return _WkbShape(type_id, has_z, has_m, tuple(children)), offset


def _assert_wkb_dimensions_preserved(
    shape: _WkbShape,
    geometry: BaseGeometry,
) -> tuple[bool, bool]:
    """Reject loss of declared Z/M at every parsed geometry-tree node."""

    if geometry.geom_type != _CORE_GEOMETRY_TYPES[shape.type_id][1]:
        raise ValueError("WKB parser changed the geometry type")
    expected_z, expected_m = shape.has_z, shape.has_m
    if shape.type_id in (4, 5, 6, 7):
        if len(geometry.geoms) != len(shape.children):
            raise ValueError("WKB parser changed the geometry member count")
        for child_shape, child_geometry in zip(
            shape.children, geometry.geoms, strict=True
        ):
            child_z, child_m = _assert_wkb_dimensions_preserved(
                child_shape, child_geometry
            )
            expected_z = expected_z or child_z
            expected_m = expected_m or child_m
    if (bool(shapely.has_z(geometry)), bool(shapely.has_m(geometry))) != (
        expected_z,
        expected_m,
    ):
        raise ValueError("WKB parser did not preserve the source Z/M dimensions")
    return expected_z, expected_m


def _parse_gpkg_geometry_blob(
    blob: object,
    metadata: _GpkgLayerMetadata,
    relative_path: str,
    fid: int,
) -> _ParsedGpkgGeometry:
    """Validate header framing and typed WKB, not numerical envelope semantics."""

    label = f"package {relative_path} layer {metadata.table_name} FID {fid}"
    try:
        if type(blob) is not bytes:
            raise ValueError("GeoPackage geometry BLOB must be exact built-in bytes")
        if len(blob) < 8:
            raise ValueError("GeoPackageBinary header is truncated")
        if blob[:2] != b"GP":
            raise ValueError("GeoPackageBinary magic must be GP")
        if blob[2] != 0:
            raise ValueError("unsupported GeoPackageBinary version")
        flags = blob[3]
        if flags & 0xC0:
            raise ValueError("GeoPackageBinary reserved flag bits must be zero")
        if flags & 0x20:
            raise ValueError("Extended GeoPackageBinary is unsupported")
        envelope_code = (flags >> 1) & 0x07
        if envelope_code > 4:
            raise ValueError("invalid GeoPackageBinary envelope code")
        little_endian = bool(flags & 1)
        byte_order = "<" if little_endian else ">"
        srs_id = struct.unpack_from(byte_order + "i", blob, 4)[0]
        if srs_id != metadata.srs_id:
            raise ValueError(
                "GeoPackageBinary header SRS ID differs from geometry metadata"
            )
        empty_flag = bool(flags & 0x10)
        if empty_flag and envelope_code != 0:
            raise ValueError("empty GeoPackageBinary must have no envelope")
        envelope_values = (0, 4, 6, 6, 8)[envelope_code]
        wkb_offset = 8 + envelope_values * 8
        if len(blob) < wkb_offset:
            raise ValueError("GeoPackageBinary envelope is truncated")
        if len(blob) == wkb_offset:
            raise ValueError("GeoPackageBinary embedded WKB is missing")
        envelope = struct.unpack_from(byte_order + "d" * envelope_values, blob, 8)
        embedded_wkb = blob[wkb_offset:]
        shape, consumed = _wkb_shape(embedded_wkb)
        if consumed != len(embedded_wkb):
            raise ValueError("embedded WKB has trailing bytes")
        _require_geometry_assignable(
            metadata.geometry_type_name, _CORE_GEOMETRY_TYPES[shape.type_id][1], label
        )
        geometry = shapely.from_wkb(embedded_wkb, on_invalid="raise")
        if type(geometry) not in (
            shapely.Point,
            shapely.LineString,
            shapely.Polygon,
            shapely.MultiPoint,
            shapely.MultiLineString,
            shapely.MultiPolygon,
            shapely.GeometryCollection,
        ):
            raise ValueError("WKB parser must return an exact scalar Shapely geometry")
        _assert_wkb_dimensions_preserved(shape, geometry)
        if bool(shapely.is_empty(geometry)) != empty_flag:
            raise ValueError(
                "GeoPackageBinary empty flag differs from parsed WKB state"
            )
        actual_z = bool(shapely.has_z(geometry))
        actual_m = bool(shapely.has_m(geometry))
        for ordinate, declaration, present in (
            ("Z", metadata.z_flag, actual_z),
            ("M", metadata.m_flag, actual_m),
        ):
            if type(declaration) is not int or declaration not in (0, 1, 2):
                raise ValueError(f"invalid {ordinate} metadata declaration")
            if (declaration == 0 and present) or (declaration == 1 and not present):
                raise ValueError(
                    f"parsed {ordinate} dimension violates GeoPackage declaration"
                )
        return _ParsedGpkgGeometry(
            geometry=geometry,
            embedded_wkb=embedded_wkb,
            srs_id=srs_id,
            envelope_code=envelope_code,
            envelope=envelope,
            header_little_endian=little_endian,
            is_empty=empty_flag,
        )
    except InpnProtectedAreasGeometryProfileError:
        raise
    except (
        shapely.errors.GEOSException,
        OverflowError,
        TypeError,
        ValueError,
        struct.error,
        RecursionError,
    ) as error:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: malformed GeoPackage geometry: {error}"
        ) from error


# Public geometry-profile evidence and source-complete boundaries follow.

GEOMETRY_PROFILE_SCHEMA_VERSION = 1
GEOMETRY_ENCODING_SCHEMA_VERSION = 1
GEOMETRY_ENCODING_CONTRACT = (
    "SHAPELY_EXTENDED_WKB_LITTLE_ENDIAN_SOURCE_DIMENSION_NO_SRID_V1"
)
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
_SOURCE_FIELDS = (
    "provider",
    "authority",
    "program",
    "dataset_id",
    "dataset_name",
    "declared_version",
    "reference_page_url",
    "archive_url",
    "archive_filename",
    "archive_size",
    "archive_sha256",
)
_COUNT_FIELDS = (
    "null_geometry_count",
    "empty_geometry_count",
    "non_empty_geometry_count",
    "valid_non_empty_geometry_count",
    "invalid_non_empty_geometry_count",
    "has_z_geometry_count",
    "has_m_geometry_count",
    "total_coordinate_count",
)
_TOOLCHAIN_FIELDS = (
    "sqlite_version",
    "pyogrio_version",
    "gdal_version",
    "shapely_version",
    "geos_version",
    "pyproj_version",
)


@dataclass(frozen=True)
class InpnProtectedAreasGeometryTypeCount:
    """One observed non-null Shapely type and its complete frequency."""

    geometry_type: str
    count: int


@dataclass(frozen=True)
class InpnProtectedAreasCoordinateDimensionCount:
    """Joint dimension/Z/M evidence, including dimensional empty geometries."""

    coordinate_dimension: int
    has_z: bool
    has_m: bool
    count: int


@dataclass(frozen=True)
class InpnProtectedAreasGeometryValidityReasonCount:
    """One exact non-empty validity outcome/reason and complete frequency."""

    is_valid: bool
    reason: str
    count: int


@dataclass(frozen=True)
class InpnProtectedAreasLayerGeometryProfile:
    """Portable raw-blob and parser-derived evidence for one physical table."""

    relative_path: str
    file_size: int
    file_sha256: str
    package_position: int
    driver_name: str
    layer_name: str
    layer_position: int
    feature_count: int
    feature_table_kind: str
    fid_column_name: str
    geometry_column_name: str
    gpkg_geometry_type_name: str
    gpkg_srs_id: int
    gpkg_z_flag: int
    gpkg_m_flag: int
    catalog_geometry_type_raw: str
    crs_raw: str
    crs_authority_name: str | None
    crs_authority_code: str | None
    crs_wkt: str
    fid_count: int
    fid_min: int | None
    fid_max: int | None
    fid_sequence_sha256: str
    null_geometry_count: int
    empty_geometry_count: int
    non_empty_geometry_count: int
    valid_non_empty_geometry_count: int
    invalid_non_empty_geometry_count: int
    has_z_geometry_count: int
    has_m_geometry_count: int
    total_coordinate_count: int
    geometry_type_counts: tuple[InpnProtectedAreasGeometryTypeCount, ...]
    coordinate_dimension_counts: tuple[InpnProtectedAreasCoordinateDimensionCount, ...]
    validity_reason_counts: tuple[InpnProtectedAreasGeometryValidityReasonCount, ...]
    catalog_total_bounds: tuple[float, float, float, float] | None
    observed_total_bounds: tuple[float, float, float, float] | None
    bounds_relation: str
    raw_geometry_blob_content_sha256: str
    geometry_content_sha256: str


@dataclass(frozen=True)
class InpnProtectedAreasGeometryProfile:
    """Complete immutable technical evidence; no source rows or geometries escape."""

    geometry_profile_schema_version: int
    provider: str
    authority: str
    program: str
    dataset_id: str
    dataset_name: str
    declared_version: str
    reference_page_url: str
    archive_url: str
    archive_filename: str
    archive_size: int
    archive_sha256: str
    source_catalog_schema_version: int
    source_catalog_content_sha256: str
    sqlite_version: str
    pyogrio_version: str
    gdal_version: str
    shapely_version: str
    geos_version: str
    pyproj_version: str
    geometry_encoding_schema_version: int
    geometry_encoding_contract: str
    layers: tuple[InpnProtectedAreasLayerGeometryProfile, ...]
    package_count: int
    layer_count: int
    geometry_row_count: int
    null_geometry_count: int
    empty_geometry_count: int
    non_empty_geometry_count: int
    valid_non_empty_geometry_count: int
    invalid_non_empty_geometry_count: int
    has_z_geometry_count: int
    has_m_geometry_count: int
    total_coordinate_count: int
    complete_geometry_profile_content_sha256: str


def _canonical_json_bytes(value: object) -> bytes:
    """Canonical JSON shared by stream hashes and the complete profile hash."""
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (OverflowError, TypeError, ValueError, UnicodeError) as error:
        raise InpnProtectedAreasGeometryProfileError(
            "non-canonical geometry JSON"
        ) from error


def _canonical_json_sha256(value: object, label: str = "geometry evidence") -> str:
    """Use the same JSON integer-sequence encoding as the attribute FID hash."""
    return sha256(_canonical_json_bytes(value)).hexdigest()


def _profile_payload(profile: InpnProtectedAreasGeometryProfile) -> dict[str, object]:
    """All schema-1 portable dataclass fields except the hash itself."""
    payload = asdict(profile)
    del payload["complete_geometry_profile_content_sha256"]
    return payload


def _profile_content_sha256(profile: InpnProtectedAreasGeometryProfile) -> str:
    return _canonical_json_sha256(_profile_payload(profile))


def _coordinate_evidence(
    geometry: BaseGeometry,
    label: str,
) -> tuple[int, tuple[float, float, float, float] | None]:
    """Check only present ordinates; mixed collections must not invent missing NaNs."""
    if geometry.is_empty:
        return 0, None
    if isinstance(
        geometry,
        (
            shapely.GeometryCollection,
            shapely.MultiPoint,
            shapely.MultiLineString,
            shapely.MultiPolygon,
        ),
    ):
        children = [_coordinate_evidence(child, label) for child in geometry.geoms]
        return sum(count for count, _ in children), _merge_bounds(
            tuple(bounds for _, bounds in children if bounds is not None)
        )
    if type(geometry) is shapely.Polygon:
        rings = (geometry.exterior, *geometry.interiors)
        children = [_coordinate_evidence(ring, label) for ring in rings]
        return sum(count for count, _ in children), _merge_bounds(
            tuple(bounds for _, bounds in children if bounds is not None)
        )
    has_z, has_m = bool(shapely.has_z(geometry)), bool(shapely.has_m(geometry))
    coordinates = shapely.get_coordinates(geometry, include_z=has_z, include_m=has_m)
    if coordinates.ndim != 2 or coordinates.shape[1] != 2 + has_z + has_m:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: invalid coordinate layout"
        )
    if not np.isfinite(coordinates).all():
        ordinates = ("X", "Y", *(("Z",) if has_z else ()), *(("M",) if has_m else ()))
        bad = tuple(
            ordinates[index]
            for index in range(len(ordinates))
            if not np.isfinite(coordinates[:, index]).all()
        )
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: non-finite present ordinate(s) {','.join(bad)}"
        )
    if len(coordinates) == 0:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: non-empty geometry has no coordinates"
        )
    return len(coordinates), (
        float(coordinates[:, 0].min()),
        float(coordinates[:, 1].min()),
        float(coordinates[:, 0].max()),
        float(coordinates[:, 1].max()),
    )


def _merge_bounds(
    bounds: tuple[tuple[float, float, float, float], ...],
) -> tuple[float, float, float, float] | None:
    if not bounds:
        return None
    return (
        min(item[0] for item in bounds),
        min(item[1] for item in bounds),
        max(item[2] for item in bounds),
        max(item[3] for item in bounds),
    )


def _bounds_relation(
    catalog: tuple[float, float, float, float] | None,
    observed: tuple[float, float, float, float] | None,
) -> str:
    if catalog is None and observed is None:
        return "BOTH_NULL"
    return "EXACT_MATCH" if catalog == observed else "DIFFERENT"


def _profile_layer(
    connection: sqlite3.Connection,
    package: InpnProtectedAreasGeoPackageCatalog,
    layer: InpnProtectedAreasLayerCatalog,
) -> InpnProtectedAreasLayerGeometryProfile:
    metadata = _read_gpkg_layer_metadata(connection, package.relative_path, layer)
    rows = _read_gpkg_geometry_rows(
        connection, metadata, package.relative_path, layer.feature_count
    )
    label = f"package {package.relative_path} layer {layer.layer_name}"
    counts: Counter[str] = Counter()
    types: Counter[str] = Counter()
    dimensions: Counter[tuple[int, bool, bool]] = Counter()
    reasons: Counter[tuple[bool, str]] = Counter()
    bounds: tuple[float, float, float, float] | None = None
    raw_digest, parser_digest = sha256(b"["), sha256(b"[")
    for position, (fid, blob) in enumerate(rows):
        if position:
            raw_digest.update(b",")
            parser_digest.update(b",")
        raw_digest.update(
            _canonical_json_bytes(
                [fid, None if blob is None else sha256(blob).hexdigest()]
            )
        )
        if blob is None:
            counts["null_geometry_count"] += 1
            parser_digest.update(
                _canonical_json_bytes(
                    [fid, "NULL", None, None, None, None, None, None, None]
                )
            )
            continue
        parsed = _parse_gpkg_geometry_blob(blob, metadata, package.relative_path, fid)
        geometry = parsed.geometry
        dimension = int(shapely.get_coordinate_dimension(geometry))
        has_z, has_m = bool(shapely.has_z(geometry)), bool(shapely.has_m(geometry))
        geometry_type = str(geometry.geom_type)
        types[geometry_type] += 1
        dimensions[(dimension, has_z, has_m)] += 1
        counts["has_z_geometry_count"] += has_z
        counts["has_m_geometry_count"] += has_m
        coordinate_count, row_bounds = _coordinate_evidence(
            geometry, f"{label} FID {fid}"
        )
        counts["total_coordinate_count"] += coordinate_count
        if row_bounds is not None:
            bounds = (
                row_bounds if bounds is None else _merge_bounds((bounds, row_bounds))
            )
        valid, reason = None, None
        if parsed.is_empty:
            state = "EMPTY"
            counts["empty_geometry_count"] += 1
        else:
            state = "NON_EMPTY"
            counts["non_empty_geometry_count"] += 1
            valid, reason = (
                bool(shapely.is_valid(geometry)),
                str(shapely.is_valid_reason(geometry)),
            )
            counts[
                "valid_non_empty_geometry_count"
                if valid
                else "invalid_non_empty_geometry_count"
            ] += 1
            reasons[(valid, reason)] += 1
        wkb = shapely.to_wkb(
            geometry,
            hex=True,
            output_dimension=dimension,
            byte_order=1,
            include_srid=False,
            flavor="extended",
        )
        if type(wkb) is not str or not wkb:
            raise InpnProtectedAreasGeometryProfileError(
                f"{label} FID {fid}: invalid parser WKB"
            )
        parser_digest.update(
            _canonical_json_bytes(
                [fid, state, geometry_type, dimension, has_z, has_m, valid, reason, wkb]
            )
        )
    raw_digest.update(b"]")
    parser_digest.update(b"]")
    return InpnProtectedAreasLayerGeometryProfile(
        relative_path=package.relative_path,
        file_size=package.file_size,
        file_sha256=package.file_sha256,
        package_position=package.package_position,
        driver_name=package.driver_name,
        layer_name=layer.layer_name,
        layer_position=layer.layer_position,
        feature_count=layer.feature_count,
        feature_table_kind=metadata.table_kind,
        fid_column_name=metadata.fid_column_name,
        geometry_column_name=metadata.geometry_column_name,
        gpkg_geometry_type_name=metadata.geometry_type_name,
        gpkg_srs_id=metadata.srs_id,
        gpkg_z_flag=metadata.z_flag,
        gpkg_m_flag=metadata.m_flag,
        catalog_geometry_type_raw=_exact_text(
            layer.geometry_type_raw, "catalog geometry type"
        ),
        crs_raw=_exact_text(layer.crs_raw, "catalog CRS"),
        crs_authority_name=layer.crs_authority_name,
        crs_authority_code=layer.crs_authority_code,
        crs_wkt=_exact_text(layer.crs_wkt, "catalog CRS WKT"),
        fid_count=len(rows),
        fid_min=rows[0][0] if rows else None,
        fid_max=rows[-1][0] if rows else None,
        fid_sequence_sha256=_canonical_json_sha256([fid for fid, _ in rows]),
        null_geometry_count=counts["null_geometry_count"],
        empty_geometry_count=counts["empty_geometry_count"],
        non_empty_geometry_count=counts["non_empty_geometry_count"],
        valid_non_empty_geometry_count=counts["valid_non_empty_geometry_count"],
        invalid_non_empty_geometry_count=counts["invalid_non_empty_geometry_count"],
        has_z_geometry_count=counts["has_z_geometry_count"],
        has_m_geometry_count=counts["has_m_geometry_count"],
        total_coordinate_count=counts["total_coordinate_count"],
        geometry_type_counts=tuple(
            InpnProtectedAreasGeometryTypeCount(kind, count)
            for kind, count in sorted(types.items())
        ),
        coordinate_dimension_counts=tuple(
            InpnProtectedAreasCoordinateDimensionCount(*key, count)
            for key, count in sorted(dimensions.items())
        ),
        validity_reason_counts=tuple(
            InpnProtectedAreasGeometryValidityReasonCount(*key, count)
            for key, count in sorted(reasons.items())
        ),
        catalog_total_bounds=layer.total_bounds,
        observed_total_bounds=bounds,
        bounds_relation=_bounds_relation(layer.total_bounds, bounds),
        raw_geometry_blob_content_sha256=raw_digest.hexdigest(),
        geometry_content_sha256=parser_digest.hexdigest(),
    )


def _build_profile(
    extraction: InpnProtectedAreasExtraction,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasGeometryProfile:
    layers: list[InpnProtectedAreasLayerGeometryProfile] = []
    for package in catalog.packages:
        item = extraction.files[package.package_position]
        if type(item) is not InpnProtectedAreasExtractedFile or (
            item.relative_path,
            item.file_size,
            item.sha256,
        ) != (package.relative_path, package.file_size, package.file_sha256):
            raise InpnProtectedAreasGeometryProfileError(
                "extraction/catalog package identity differs"
            )
        package_bytes = _read_verified_package_bytes(extraction, item)
        with _open_gpkg_sqlite_snapshot(
            package_bytes, package.relative_path
        ) as connection:
            for layer in package.layers:
                layers.append(_profile_layer(connection, package, layer))
        del package_bytes
    counts = {
        name: sum(getattr(layer, name) for layer in layers) for name in _COUNT_FIELDS
    }
    profile = InpnProtectedAreasGeometryProfile(
        geometry_profile_schema_version=GEOMETRY_PROFILE_SCHEMA_VERSION,
        provider=catalog.provider,
        authority=catalog.authority,
        program=catalog.program,
        dataset_id=catalog.dataset_id,
        dataset_name=catalog.dataset_name,
        declared_version=catalog.declared_version,
        reference_page_url=catalog.reference_page_url,
        archive_url=catalog.archive_url,
        archive_filename=catalog.archive_filename,
        archive_size=catalog.archive_size,
        archive_sha256=catalog.archive_sha256,
        source_catalog_schema_version=catalog.catalog_schema_version,
        source_catalog_content_sha256=catalog.complete_catalog_content_sha256,
        sqlite_version=sqlite3.sqlite_version,
        pyogrio_version=pyogrio.__version__,
        gdal_version=pyogrio.__gdal_version_string__,
        shapely_version=shapely.__version__,
        geos_version=shapely.geos_version_string,
        pyproj_version=pyproj.__version__,
        geometry_encoding_schema_version=GEOMETRY_ENCODING_SCHEMA_VERSION,
        geometry_encoding_contract=GEOMETRY_ENCODING_CONTRACT,
        layers=tuple(layers),
        package_count=catalog.package_count,
        layer_count=len(layers),
        geometry_row_count=sum(layer.feature_count for layer in layers),
        null_geometry_count=counts["null_geometry_count"],
        empty_geometry_count=counts["empty_geometry_count"],
        non_empty_geometry_count=counts["non_empty_geometry_count"],
        valid_non_empty_geometry_count=counts["valid_non_empty_geometry_count"],
        invalid_non_empty_geometry_count=counts["invalid_non_empty_geometry_count"],
        has_z_geometry_count=counts["has_z_geometry_count"],
        has_m_geometry_count=counts["has_m_geometry_count"],
        total_coordinate_count=counts["total_coordinate_count"],
        complete_geometry_profile_content_sha256="",
    )
    return replace(
        profile,
        complete_geometry_profile_content_sha256=_profile_content_sha256(profile),
    )


def _exact_text(value: object, label: str) -> str:
    if type(value) is not str or not value or value != value.strip():
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact nonempty built-in string required"
        )
    return value


def _exact_int(value: object, label: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact integer >= {minimum} required"
        )
    return value


def _exact_sha(value: object, label: str) -> None:
    if type(value) is not str or _SHA_PATTERN.fullmatch(value) is None:
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: canonical SHA256 required"
        )


def _unique_ordered(keys: tuple[Any, ...], label: str) -> None:
    if keys != tuple(sorted(keys)) or len(keys) != len(set(keys)):
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: duplicate or unordered domain"
        )


def _unique_names(names: tuple[str, ...], label: str) -> None:
    keys = tuple(unicodedata.normalize("NFKC", name).casefold() for name in names)
    if len(set(keys)) != len(keys):
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact/NFKC/casefold identity collision"
        )


def _validate_bounds(value: object, label: str) -> None:
    if value is None:
        return
    if (
        type(value) is not tuple
        or len(value) != 4
        or any(type(item) is not float or not math.isfinite(item) for item in value)
    ):
        raise InpnProtectedAreasGeometryProfileError(
            f"{label}: exact finite float bounds tuple required"
        )
    if value[0] > value[2] or value[1] > value[3]:
        raise InpnProtectedAreasGeometryProfileError(f"{label}: reversed bounds")


def _validate_layer_intrinsic(layer: object) -> InpnProtectedAreasLayerGeometryProfile:
    if type(layer) is not InpnProtectedAreasLayerGeometryProfile:
        raise InpnProtectedAreasGeometryProfileError(
            "exact geometry layer profile required"
        )
    try:
        path = _validate_inventory_relative_path(layer.relative_path)
    except (InpnProtectedAreasSourceError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasGeometryProfileError(
            "invalid canonical package path"
        ) from error
    if PurePosixPath(path).suffix.casefold() != ".gpkg":
        raise InpnProtectedAreasGeometryProfileError(
            "package path requires GeoPackage suffix"
        )
    for name in (
        "driver_name",
        "layer_name",
        "feature_table_kind",
        "fid_column_name",
        "geometry_column_name",
        "gpkg_geometry_type_name",
        "catalog_geometry_type_raw",
        "crs_raw",
        "crs_wkt",
        "bounds_relation",
    ):
        _exact_text(getattr(layer, name), name)
    _require_gpkg_geometry_type(layer.gpkg_geometry_type_name, "GeoPackage declaration")
    for name in ("layer_name", "fid_column_name", "geometry_column_name"):
        _quote_sqlite_identifier(getattr(layer, name))
    if layer.driver_name != "GPKG" or layer.feature_table_kind != "table":
        raise InpnProtectedAreasGeometryProfileError(
            "only physical GPKG feature tables supported"
        )
    if layer.fid_column_name == layer.geometry_column_name:
        raise InpnProtectedAreasGeometryProfileError(
            "FID and geometry columns must differ"
        )
    _exact_int(layer.file_size, "package size", 1)
    _exact_int(layer.package_position, "package position")
    _exact_int(layer.layer_position, "layer position")
    _exact_int(layer.feature_count, "feature count")
    _exact_int(layer.fid_count, "FID count")
    if layer.feature_count != layer.fid_count:
        raise InpnProtectedAreasGeometryProfileError("FID/feature count mismatch")
    for name in (
        "file_sha256",
        "fid_sequence_sha256",
        "raw_geometry_blob_content_sha256",
        "geometry_content_sha256",
    ):
        _exact_sha(getattr(layer, name), name)
    if not layer.fid_count:
        if layer.fid_min is not None or layer.fid_max is not None:
            raise InpnProtectedAreasGeometryProfileError("empty FID range must be null")
        for name in (
            "fid_sequence_sha256",
            "raw_geometry_blob_content_sha256",
            "geometry_content_sha256",
        ):
            if getattr(layer, name) != _canonical_json_sha256([]):
                raise InpnProtectedAreasGeometryProfileError(
                    "invalid empty stream hash"
                )
    else:
        if type(layer.fid_min) is not int or type(layer.fid_max) is not int:
            raise InpnProtectedAreasGeometryProfileError("exact FID extrema required")
        if (
            (layer.fid_count == 1 and layer.fid_min != layer.fid_max)
            or (layer.fid_count > 1 and layer.fid_min >= layer.fid_max)
            or layer.fid_count > layer.fid_max - layer.fid_min + 1
        ):
            raise InpnProtectedAreasGeometryProfileError("FID range is impossible")
    _exact_int(layer.gpkg_srs_id, "GeoPackage SRS", -(2**31))
    if layer.gpkg_srs_id >= 2**31:
        raise InpnProtectedAreasGeometryProfileError(
            "GeoPackage SRS exceeds signed int32"
        )
    for flag in (layer.gpkg_z_flag, layer.gpkg_m_flag):
        if type(flag) is not int or flag not in (0, 1, 2):
            raise InpnProtectedAreasGeometryProfileError("invalid GeoPackage Z/M flag")
    for name in ("crs_authority_name", "crs_authority_code"):
        value = getattr(layer, name)
        if value is not None:
            _exact_text(value, name)
    try:
        expected_crs = _canonical_crs(layer.crs_raw, path, layer.layer_name)
    except InpnProtectedAreasCatalogError as error:
        raise InpnProtectedAreasGeometryProfileError("invalid catalog CRS") from error
    if expected_crs != (
        layer.crs_raw,
        layer.crs_authority_name,
        layer.crs_authority_code,
        layer.crs_wkt,
    ):
        raise InpnProtectedAreasGeometryProfileError("non-canonical catalog CRS")
    if (
        layer.crs_authority_name == "EPSG"
        and layer.crs_authority_code is not None
        and (
            layer.crs_authority_code.isdecimal()
            and layer.gpkg_srs_id != int(layer.crs_authority_code)
        )
    ):
        raise InpnProtectedAreasGeometryProfileError(
            "GeoPackage SRS differs from catalog EPSG"
        )
    for name in _COUNT_FIELDS:
        _exact_int(getattr(layer, name), name)
    non_null = layer.empty_geometry_count + layer.non_empty_geometry_count
    if layer.null_geometry_count + non_null != layer.feature_count or (
        layer.valid_non_empty_geometry_count + layer.invalid_non_empty_geometry_count
        != layer.non_empty_geometry_count
    ):
        raise InpnProtectedAreasGeometryProfileError(
            "geometry count equations are inconsistent"
        )
    if (layer.non_empty_geometry_count == 0) != (layer.total_coordinate_count == 0) or (
        layer.total_coordinate_count < layer.non_empty_geometry_count
    ):
        raise InpnProtectedAreasGeometryProfileError("coordinate count is inconsistent")
    for name, model in (
        ("geometry_type_counts", InpnProtectedAreasGeometryTypeCount),
        ("coordinate_dimension_counts", InpnProtectedAreasCoordinateDimensionCount),
        ("validity_reason_counts", InpnProtectedAreasGeometryValidityReasonCount),
    ):
        domain = getattr(layer, name)
        if type(domain) is not tuple or any(type(item) is not model for item in domain):
            raise InpnProtectedAreasGeometryProfileError(
                f"{name}: exact immutable domain required"
            )
        for item in domain:
            _exact_int(item.count, f"{name} frequency", 1)
    for item in layer.geometry_type_counts:
        _require_geometry_assignable(
            layer.gpkg_geometry_type_name, item.geometry_type, "profile geometry type"
        )
    _unique_ordered(
        tuple(item.geometry_type for item in layer.geometry_type_counts),
        "geometry types",
    )
    for item in layer.coordinate_dimension_counts:
        if (
            type(item.coordinate_dimension) is not int
            or item.coordinate_dimension not in (2, 3, 4)
            or (type(item.has_z) is not bool or type(item.has_m) is not bool)
        ):
            raise InpnProtectedAreasGeometryProfileError(
                "invalid dimension/Z/M domain types"
            )
        if (
            (item.coordinate_dimension == 2 and (item.has_z or item.has_m))
            or (item.coordinate_dimension == 3 and not (item.has_z or item.has_m))
            or (item.coordinate_dimension == 4 and not (item.has_z and item.has_m))
        ):
            raise InpnProtectedAreasGeometryProfileError(
                "impossible dimension/Z/M relationship"
            )
        for flag, actual in (
            (layer.gpkg_z_flag, item.has_z),
            (layer.gpkg_m_flag, item.has_m),
        ):
            if (flag == 0 and actual) or (flag == 1 and not actual):
                raise InpnProtectedAreasGeometryProfileError(
                    "geometry dimension contradicts GeoPackage Z/M declaration"
                )
    _unique_ordered(
        tuple(
            (item.coordinate_dimension, item.has_z, item.has_m)
            for item in layer.coordinate_dimension_counts
        ),
        "coordinate dimensions",
    )
    if (
        sum(item.count for item in layer.geometry_type_counts) != non_null
        or (sum(item.count for item in layer.coordinate_dimension_counts) != non_null)
        or sum(item.count for item in layer.coordinate_dimension_counts if item.has_z)
        != layer.has_z_geometry_count
        or (
            sum(item.count for item in layer.coordinate_dimension_counts if item.has_m)
            != layer.has_m_geometry_count
        )
    ):
        raise InpnProtectedAreasGeometryProfileError(
            "geometry/dimension domain count closure failed"
        )
    for item in layer.validity_reason_counts:
        if type(item.is_valid) is not bool:
            raise InpnProtectedAreasGeometryProfileError(
                "validity must be an exact Boolean"
            )
        _exact_text(item.reason, "validity reason")
    _unique_ordered(
        tuple((item.is_valid, item.reason) for item in layer.validity_reason_counts),
        "validity reasons",
    )
    if sum(
        item.count for item in layer.validity_reason_counts if item.is_valid
    ) != layer.valid_non_empty_geometry_count or (
        sum(item.count for item in layer.validity_reason_counts if not item.is_valid)
        != layer.invalid_non_empty_geometry_count
    ):
        raise InpnProtectedAreasGeometryProfileError(
            "validity domain count closure failed"
        )
    _validate_bounds(layer.catalog_total_bounds, "catalog bounds")
    try:
        _validated_bounds(
            layer.catalog_total_bounds,
            is_spatial=True,
            feature_count=layer.feature_count,
            relative_path=path,
            layer_name=layer.layer_name,
        )
    except InpnProtectedAreasCatalogError as error:
        raise InpnProtectedAreasGeometryProfileError(
            "catalog bounds/feature count relationship is inconsistent"
        ) from error
    _validate_bounds(layer.observed_total_bounds, "observed bounds")
    if (layer.observed_total_bounds is None) != (layer.non_empty_geometry_count == 0):
        raise InpnProtectedAreasGeometryProfileError(
            "observed bounds/non-empty count mismatch"
        )
    if layer.bounds_relation != _bounds_relation(
        layer.catalog_total_bounds, layer.observed_total_bounds
    ):
        raise InpnProtectedAreasGeometryProfileError("incorrect bounds relation")
    return layer


def _validate_profile_intrinsic(profile: object) -> InpnProtectedAreasGeometryProfile:
    """Prove structure and closure, not non-empty stream hashes without source rows."""
    if type(profile) is not InpnProtectedAreasGeometryProfile:
        raise InpnProtectedAreasGeometryProfileError(
            "exact InpnProtectedAreasGeometryProfile required"
        )
    for name, expected in (
        ("geometry_profile_schema_version", GEOMETRY_PROFILE_SCHEMA_VERSION),
        ("source_catalog_schema_version", CATALOG_HASH_SCHEMA_VERSION),
        ("geometry_encoding_schema_version", GEOMETRY_ENCODING_SCHEMA_VERSION),
    ):
        if (
            type(getattr(profile, name)) is not int
            or getattr(profile, name) != expected
        ):
            raise InpnProtectedAreasGeometryProfileError(
                f"{name}: invalid schema version"
            )
    for name in (*_SOURCE_FIELDS[:9], *_TOOLCHAIN_FIELDS, "geometry_encoding_contract"):
        _exact_text(getattr(profile, name), name)
    if profile.geometry_encoding_contract != GEOMETRY_ENCODING_CONTRACT:
        raise InpnProtectedAreasGeometryProfileError(
            "geometry encoding contract mismatch"
        )
    _exact_int(profile.archive_size, "archive size", 1)
    for name in (
        "archive_sha256",
        "source_catalog_content_sha256",
        "complete_geometry_profile_content_sha256",
    ):
        _exact_sha(getattr(profile, name), name)
    if type(profile.layers) is not tuple or not profile.layers:
        raise InpnProtectedAreasGeometryProfileError(
            "layers must be an exact non-empty tuple"
        )
    packages: list[tuple[str, int, str, str]] = []
    names: list[str] = []
    last_position = -1
    for candidate in profile.layers:
        layer = _validate_layer_intrinsic(candidate)
        package = (
            layer.relative_path,
            layer.file_size,
            layer.file_sha256,
            layer.driver_name,
        )
        if layer.package_position != last_position:
            if layer.package_position != len(packages):
                raise InpnProtectedAreasGeometryProfileError(
                    "package positions/groups must be contiguous"
                )
            packages.append(package)
            names = []
            last_position = layer.package_position
        if packages[-1] != package:
            raise InpnProtectedAreasGeometryProfileError(
                "inconsistent repeated package metadata"
            )
        if layer.layer_position != len(names):
            raise InpnProtectedAreasGeometryProfileError(
                "layer positions must be contiguous"
            )
        names.append(layer.layer_name)
        _unique_names(tuple(names), "layer names")
    paths = tuple(package[0] for package in packages)
    _unique_names(paths, "package paths")
    _unique_ordered(paths, "package paths")
    expected_counts = {
        name: sum(getattr(layer, name) for layer in profile.layers)
        for name in _COUNT_FIELDS
    }
    expected_counts.update(
        package_count=len(packages),
        layer_count=len(profile.layers),
        geometry_row_count=sum(layer.feature_count for layer in profile.layers),
    )
    for name, expected in expected_counts.items():
        if _exact_int(getattr(profile, name), name) != expected:
            raise InpnProtectedAreasGeometryProfileError(
                f"{name}: aggregate count mismatch"
            )
    if profile.complete_geometry_profile_content_sha256 != _profile_content_sha256(
        profile
    ):
        raise InpnProtectedAreasGeometryProfileError(
            "complete geometry profile SHA256 mismatch"
        )
    return profile


def _validate_profile_catalog_contract(
    profile: InpnProtectedAreasGeometryProfile,
    catalog: InpnProtectedAreasCatalog,
) -> None:
    """Reject forged catalog-bound facts before any SQLite geometry row access."""
    if tuple(getattr(profile, name) for name in _SOURCE_FIELDS) != tuple(
        getattr(catalog, name) for name in _SOURCE_FIELDS
    ) or (
        profile.source_catalog_schema_version,
        profile.source_catalog_content_sha256,
        profile.package_count,
        profile.layer_count,
        profile.geometry_row_count,
    ) != (
        catalog.catalog_schema_version,
        catalog.complete_catalog_content_sha256,
        catalog.package_count,
        catalog.layer_count,
        catalog.total_feature_count,
    ):
        raise InpnProtectedAreasGeometryProfileError(
            "geometry profile source/catalog identity mismatch"
        )
    catalog_layers = tuple(
        (package, layer) for package in catalog.packages for layer in package.layers
    )
    if len(catalog_layers) != len(profile.layers):
        raise InpnProtectedAreasGeometryProfileError(
            "geometry profile catalog layer inventory mismatch"
        )
    for evidence, (package, layer) in zip(profile.layers, catalog_layers, strict=True):
        actual = (
            evidence.relative_path,
            evidence.file_size,
            evidence.file_sha256,
            evidence.package_position,
            evidence.driver_name,
            evidence.layer_name,
            evidence.layer_position,
            evidence.feature_count,
            evidence.catalog_geometry_type_raw,
            evidence.crs_raw,
            evidence.crs_authority_name,
            evidence.crs_authority_code,
            evidence.crs_wkt,
            evidence.catalog_total_bounds,
        )
        expected = (
            package.relative_path,
            package.file_size,
            package.file_sha256,
            package.package_position,
            package.driver_name,
            layer.layer_name,
            layer.layer_position,
            layer.feature_count,
            layer.geometry_type_raw,
            layer.crs_raw,
            layer.crs_authority_name,
            layer.crs_authority_code,
            layer.crs_wkt,
            layer.total_bounds,
        )
        if not layer.is_spatial or actual != expected:
            raise InpnProtectedAreasGeometryProfileError(
                "geometry profile package/layer catalog mismatch"
            )


def _prepare_inputs(
    extraction: object,
    config: object,
    catalog: object,
) -> tuple[
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasCatalog,
]:
    """Reuse the approved exact-type/config/extraction/catalog reconstruction boundary."""
    try:
        return _prepare_source_inputs(extraction, config, catalog)
    except InpnProtectedAreasAttributeProfileError as error:
        raise InpnProtectedAreasGeometryProfileError(
            f"geometry source inputs invalid: {error}"
        ) from error


def _build_with_postconditions(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasGeometryProfile:
    profile = _validate_profile_intrinsic(_build_profile(extraction, catalog))
    try:
        final_extraction = validate_inpn_protected_areas_extraction(extraction, config)
        final_catalog = build_inpn_protected_areas_catalog(final_extraction, config)
    except (InpnProtectedAreasSourceError, InpnProtectedAreasCatalogError) as error:
        raise InpnProtectedAreasGeometryProfileError(
            "INPN source changed during geometry profiling"
        ) from error
    if final_extraction != extraction or final_catalog != catalog:
        raise InpnProtectedAreasGeometryProfileError(
            "INPN source/catalog changed during geometry profiling"
        )
    return profile


def build_inpn_protected_areas_geometry_profile(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasGeometryProfile:
    """Build all technical geometry evidence from fresh archive-bound package bytes."""
    try:
        fresh_extraction, validated_config, fresh_catalog = _prepare_inputs(
            extraction, config, catalog
        )
        return _build_with_postconditions(
            fresh_extraction, validated_config, fresh_catalog
        )
    except InpnProtectedAreasGeometryProfileError:
        raise
    except Exception as error:
        raise InpnProtectedAreasGeometryProfileError(
            "INPN geometry profile cannot be built safely"
        ) from error


def validate_inpn_protected_areas_geometry_profile(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
    profile: InpnProtectedAreasGeometryProfile,
) -> None:
    """Intrinsically validate, cheaply preflight, independently rebuild, exact-compare."""
    try:
        supplied = _validate_profile_intrinsic(profile)
        fresh_extraction, validated_config, fresh_catalog = _prepare_inputs(
            extraction, config, catalog
        )
        _validate_profile_catalog_contract(supplied, fresh_catalog)
        rebuilt = _build_with_postconditions(
            fresh_extraction, validated_config, fresh_catalog
        )
        if supplied != rebuilt:
            raise InpnProtectedAreasGeometryProfileError(
                "geometry profile differs from independently rebuilt physical evidence"
            )
    except InpnProtectedAreasGeometryProfileError:
        raise
    except Exception as error:
        raise InpnProtectedAreasGeometryProfileError(
            "INPN geometry profile validation failed safely"
        ) from error


__all__ = [
    "InpnProtectedAreasCoordinateDimensionCount",
    "InpnProtectedAreasGeometryProfile",
    "InpnProtectedAreasGeometryProfileError",
    "InpnProtectedAreasGeometryTypeCount",
    "InpnProtectedAreasGeometryValidityReasonCount",
    "InpnProtectedAreasLayerGeometryProfile",
    "build_inpn_protected_areas_geometry_profile",
    "validate_inpn_protected_areas_geometry_profile",
]
```
