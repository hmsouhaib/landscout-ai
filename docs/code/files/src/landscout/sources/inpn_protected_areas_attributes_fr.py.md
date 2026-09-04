# `src/landscout/sources/inpn_protected_areas_attributes_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_attributes_fr.py`
- File type: Python source
- Layer/domain: official INPN EP source-bound factual attribute evidence
- Responsibility: Profiles every non-geometry value from every cataloged EP layer using verified immutable package bytes, without assigning environmental meaning.
- Source SHA256: `8e5b4d8adc000e41c64d173f0918cd74abfeacace9bada382d8c00a9e3752c89`

## 1. Architectural contract

This module implements `verified extraction -> independently rebuilt schema-2 physical catalog -> immutable package-byte reads -> complete attribute-only profile`. It reads all ordered non-geometry fields and physical FIDs, retains every distinct non-null value and frequency, and binds column, FID, row, layer, and complete profile evidence with canonical SHA256. It deliberately does not load, normalize, repair, transform, or interpret geometry.

## 2. Every import

```python
"""Source-bound attribute-only profile of verified INPN EP GeoPackages."""

from __future__ import annotations

import base64
import binascii
import json
import math
import re
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from typing import cast

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
from geopandas.array import GeometryDtype  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.sources.inpn_protected_areas_catalog_fr import (
    CATALOG_HASH_SCHEMA_VERSION,
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasGeoPackageCatalog,
    InpnProtectedAreasLayerCatalog,
    _read_verified_package_bytes,
    _suppress_pyogrio_bytes_gpkg_warning,
    build_inpn_protected_areas_catalog,
    validate_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    validate_inpn_protected_areas_extraction,
)
```

`base64` encodes binary cells; `binascii`, `json`, `math`, and `re` validate canonical representations; frozen dataclasses carry immutable evidence; `date`/`datetime` are explicitly rejected as temporal objects; SHA256 binds portable payloads; NumPy/Pandas/Pyogrio implement scalar and attribute-frame handling; GeoPandas/Shapely types are imported only to reject geometry-bearing results. The catalog and extraction imports reconstruct the complete upstream trust chain. The two underscore-prefixed catalog imports share verified byte snapshots and narrowly scoped known-warning suppression; they are not package exports.

## 3. Constants and value kinds

- `ATTRIBUTE_PROFILE_SCHEMA_VERSION = 1`: first persisted canonical profile/hash contract.
- `ATTRIBUTE_VALUE_KINDS = ("TEXT", "BOOLEAN", "INTEGER", "FLOAT_HEX", "BINARY_BASE64")`: exhaustive supported non-null scalar kinds in canonical sort/validation order.
- `_SHA_PATTERN`: exact lowercase 64-hex digest grammar.
- `_INTEGER_PATTERN`: canonical decimal integer grammar: zero, positive integers without leading zeros, and negative integers without negative zero.

Canonical values are exact built-in strings: Unicode text unchanged; booleans as `true`/`false`; integers in base-10; finite floats as Python's exact hexadecimal form; bytes as RFC 4648 base64. Null is represented outside the domain through `null_count` and a null cell payload.

## 4. Exception and every dataclass field

`InpnProtectedAreasAttributeProfileError(ValueError)` is the sole public controlled failure type for unsafe, malformed, changed, or unverifiable attribute evidence.

| Frozen dataclass | Field | Type | Meaning |
|---|---|---|---|
| `InpnProtectedAreasDistinctAttributeValue` | `value_kind` | `str` | One of the five canonical scalar kinds. |
|  | `canonical_value` | `str` | Portable exact spelling for the non-null scalar. |
|  | `count` | `int` | Exact positive frequency in the field. |
| `InpnProtectedAreasFieldAttributeProfile` | `name` | `str` | Exact physical attribute name. |
|  | `position` | `int` | Zero-based physical catalog order. |
|  | `source_dtype` | `str` | Exact OGR/Pyogrio dtype recorded by the catalog. |
|  | `runtime_dtype` | `str` | Actual pandas dtype returned by the attribute read. |
|  | `null_count` | `int` | Exact count of null cells. |
|  | `non_null_count` | `int` | Exact count of supported non-null cells. |
|  | `distinct_non_null_count` | `int` | Exact complete-domain cardinality. |
|  | `distinct_values` | immutable tuple | Every distinct canonical non-null value and frequency. |
|  | `column_content_sha256` | `str` | Hash of field identity/dtypes plus FID-addressed canonical cells. |
| `InpnProtectedAreasLayerAttributeProfile` | `relative_path`, `file_size`, `file_sha256`, `package_position`, `driver_name` | exact scalar lineage | Immutable package/catalog identity. |
|  | `layer_name`, `layer_position`, `feature_count` | exact scalar metadata | Exact physical layer identity/order/count. |
|  | `fid_count`, `fid_min`, `fid_max`, `fid_sequence_sha256` | exact FID evidence | Count/extrema and ordered identity hash; empty layers have null extrema. |
|  | `row_content_sha256` | `str` | Hash of each sorted FID and every ordered canonical cell. |
|  | `fields` | immutable tuple | All field profiles in physical catalog order. |
| `InpnProtectedAreasAttributeProfile` | source/archive fields | exact built-in scalars | Provider through archive SHA copied from verified extraction/catalog authority. |
|  | `source_catalog_schema_version`, `source_catalog_content_sha256` | exact scalar lineage | Binds profile to schema-2 catalog bytes/metadata identity. |
|  | `layers` | immutable tuple | All physical layers in catalog package/layer order. |
|  | six aggregate fields | exact nonnegative integers | Package/layer/field/row/null/distinct totals. |
|  | `complete_attribute_profile_content_sha256` | `str` | Schema-1 canonical hash over every portable factual field. |
| `_CanonicalCell` | `value_kind`, `canonical_value` | optional exact strings | Internal explicit null-or-canonical scalar representation used only during construction/hashing. |

No model retains a DataFrame, GeoDataFrame, Series, NumPy array, package path, geometry, mutable mapping, or mutable sequence.

## 5. Every helper and public function

| Function | Exact signature | Contract |
|---|---|---|
| `_canonical_json_sha256` | `def _canonical_json_sha256(value: object, label: str) -> str` | Serializes only canonical JSON with sorted keys, compact separators, UTF-8, preserved Unicode, and non-finite values forbidden, then returns SHA256; serialization failures become the controlled profile error. |
| `_validated_config` | `def _validated_config(config: object) -> InpnProtectedAreasSourceConfig` | Requires the exact source-config runtime class and reconstructs it through Pydantic so caller-owned or subclassed trust objects cannot cross the boundary unchanged. |
| `_prepare_inputs` | `def _prepare_inputs( extraction: object, config: object, catalog: object, ) -> tuple[ InpnProtectedAreasExtraction, InpnProtectedAreasSourceConfig, InpnProtectedAreasCatalog, ]` | Validates exact extraction/config/catalog types, source-completely revalidates extraction and catalog, rebuilds the catalog, and rejects any supplied catalog that differs from fresh physical metadata. |
| `_is_null_scalar` | `def _is_null_scalar(value: object) -> bool` | Recognizes only scalar null evidence; it accepts None and scalar pandas/NumPy missing values while rejecting array-shaped or ambiguous null results. |
| `_canonical_cell` | `def _canonical_cell( value: object, *, relative_path: str, layer_name: str, field_name: str, fid: int, ) -> _CanonicalCell` | Maps a supported non-null scalar to TEXT, BOOLEAN, INTEGER, FLOAT_HEX, or BINARY_BASE64 with exact built-in canonical text; it rejects composites, temporal objects, non-finite floats, subclasses, and unsupported mutable/arbitrary values. |
| `_canonical_fids` | `def _canonical_fids( frame: pd.DataFrame, *, relative_path: str, layer_name: str, ) -> tuple[tuple[int, int], ...]` | Requires a one-level integer FID index whose Python/NumPy integers normalize exactly to built-in integers, rejects booleans/nulls/duplicates/non-integral identifiers, and returns the original identities sorted numerically without renumbering. |
| `_validate_attribute_frame` | `def _validate_attribute_frame( frame: object, package: InpnProtectedAreasGeoPackageCatalog, layer: InpnProtectedAreasLayerCatalog, ) -> tuple[pd.DataFrame, tuple[tuple[int, int], ...]]` | Requires an exact pandas DataFrame, excludes GeoDataFrame/GeometryDtype/Shapely cells, proves exact ordered catalog columns and feature count, and delegates canonical FID validation. |
| `_cell_payload` | `def _cell_payload(cell: _CanonicalCell) -> object` | Returns the portable two-member canonical cell payload used by column and row hashes, including explicit null evidence. |
| `_profile_layer` | `def _profile_layer( package_bytes: bytes, package: InpnProtectedAreasGeoPackageCatalog, layer: InpnProtectedAreasLayerCatalog, ) -> InpnProtectedAreasLayerAttributeProfile` | Reads one verified package-byte snapshot with the exact Pyogrio attribute-only call, validates frame/FIDs, computes every complete field domain/frequency and column hash, then computes ordered FID and row-content hashes. |
| `_distinct_value_payload` | `def _distinct_value_payload( value: InpnProtectedAreasDistinctAttributeValue, ) -> dict[str, object]` | Converts one immutable distinct-value record to canonical hash payload fields. |
| `_field_profile_payload` | `def _field_profile_payload( field: InpnProtectedAreasFieldAttributeProfile, ) -> dict[str, object]` | Projects every portable field fact, including the complete ordered domain, into the canonical profile payload. |
| `_layer_profile_payload` | `def _layer_profile_payload( layer: InpnProtectedAreasLayerAttributeProfile, ) -> dict[str, object]` | Projects package, layer, FID, row, and ordered field evidence into the canonical profile payload. |
| `_profile_payload` | `def _profile_payload( profile: InpnProtectedAreasAttributeProfile, ) -> dict[str, object]` | Builds the complete path-independent source/catalog/layer/aggregate payload; cache paths, timestamps, cache-hit state, Python repr, and object identity are absent. |
| `_profile_content_sha256` | `def _profile_content_sha256(profile: InpnProtectedAreasAttributeProfile) -> str` | Hashes the complete profile payload through the module's canonical JSON algorithm. |
| `_build_profile` | `def _build_profile( extraction: InpnProtectedAreasExtraction, catalog: InpnProtectedAreasCatalog, ) -> InpnProtectedAreasAttributeProfile` | Walks catalog packages and layers in physical order, resolves their extraction records, profiles each layer from freshly verified bytes, calculates exact aggregates, and attaches the schema-1 complete profile hash. |
| `_exact_text` | `def _exact_text(value: object, label: str, *, allow_empty: bool = False) -> str` | Accepts only exact built-in strings, enforcing nonempty and edge-whitespace rules unless empty text is explicitly permitted. |
| `_exact_non_negative_int` | `def _exact_non_negative_int(value: object, label: str) -> int` | Accepts only exact built-in nonnegative integers and therefore excludes booleans and integer subclasses. |
| `_exact_sha` | `def _exact_sha(value: object, label: str) -> str` | Requires an exact lowercase 64-hex built-in string. |
| `_validate_canonical_distinct_value` | `def _validate_canonical_distinct_value( value: object, *, label: str, ) -> InpnProtectedAreasDistinctAttributeValue` | Proves the exact record class, supported value kind, canonical spelling for that kind, positive frequency, and forbids null values from the non-null domain. |
| `_validate_profile_intrinsic` | `def _validate_profile_intrinsic( profile: object, ) -> InpnProtectedAreasAttributeProfile` | Exhaustively validates exact classes/types/order/lineage/count equations/domains and recomputes every column, FID, row, layer, aggregate, and complete-profile hash before accepting supplied evidence. |
| `_build_with_postconditions` | `def _build_with_postconditions( extraction: InpnProtectedAreasExtraction, config: InpnProtectedAreasSourceConfig, catalog: InpnProtectedAreasCatalog, ) -> InpnProtectedAreasAttributeProfile` | Builds between fresh extraction/catalog checks and rejects any source or metadata change during attribute inspection. |
| `build_inpn_protected_areas_attribute_profile` | `def build_inpn_protected_areas_attribute_profile( extraction: InpnProtectedAreasExtraction, config: InpnProtectedAreasSourceConfig, catalog: InpnProtectedAreasCatalog, ) -> InpnProtectedAreasAttributeProfile` | Public source-complete builder: reconstructs trust inputs, verifies extraction and fresh catalog equality, reads all non-geometry fields, enforces postconditions, and returns intrinsic-valid immutable evidence. |
| `validate_inpn_protected_areas_attribute_profile` | `def validate_inpn_protected_areas_attribute_profile( extraction: InpnProtectedAreasExtraction, config: InpnProtectedAreasSourceConfig, catalog: InpnProtectedAreasCatalog, profile: InpnProtectedAreasAttributeProfile, ) -> None` | Public independent validator: validates supplied evidence intrinsically, rebuilds the complete profile from fresh verified package bytes, and requires exact equality so coordinated content/hash forgery cannot pass. |

## 6. Exact reader contract and side effects

For each catalog layer `_profile_layer` invokes exactly:

```python
pyogrio.read_dataframe(
    package_bytes,
    layer=layer.layer_name,
    columns=[field.name for field in layer.fields],
    read_geometry=False,
    fid_as_index=True,
    use_arrow=False,
    datetime_as_string=True,
)
```

`package_bytes` is one exact built-in immutable byte snapshot already size/SHA checked against archive-derived extraction evidence. No filesystem path is passed to Pyogrio. The known dynamic `/vsimem/pyogrio_<hex>` GPKG extension warning is suppressed only around this call; unrelated warnings propagate. The module performs read-only package/extraction checks and has no network, download, cache publication, extraction, or persistent-output side effect.

## 7. Hash algorithms and validation paths

- Canonical serialization is UTF-8 JSON, sorted mapping keys, compact separators, `ensure_ascii=False`, and `allow_nan=False`; SHA256 is lowercase hexadecimal.
- Column hashes include field name/position/source/runtime dtype and all `(FID, canonical cell)` pairs after numeric FID sort.
- FID hashes include every exact sorted physical identifier, including sparse identifiers and a deterministic empty sequence.
- Row hashes include every sorted FID plus every field's canonical cell in physical field order.
- Layer payloads bind package/layer/catalog lineage, FID and row hashes, and complete ordered field profiles.
- The complete hash binds schema, source/archive identity, source catalog schema/hash, every layer payload, and all aggregate counts.
- Intrinsic validation rejects comparison-equal subclasses, malformed canonical scalars, duplicate/out-of-order identities/domains, frequency/count disagreement, lineage disagreement, and any recomputed hash mismatch.
- Public validation performs intrinsic validation and then a complete fresh physical rebuild/equality comparison; a caller cannot authorize coordinated profile-plus-hash tampering.
- Full extraction/catalog validation runs before reading and again after all reads, closing persistent source changes. Each read itself is isolated from live-path swaps by immutable package bytes.

## 8. Public exports

The exact `__all__` exposes four immutable factual models, `InpnProtectedAreasAttributeProfileError`, `build_inpn_protected_areas_attribute_profile`, and `validate_inpn_protected_areas_attribute_profile`. Constants, `_CanonicalCell`, byte readers, frame helpers, payload builders, and intrinsic validators remain internal. `landscout.sources` re-exports the same approved seven-name boundary.

## 9. Tests and protected non-goals

`tests/unit/test_inpn_protected_areas_attributes_fr.py` contains 74 collected cases covering exact input authority, independent catalog/profile rebuilding, immutable package snapshots, exact Pyogrio arguments, FID and frame contracts, every scalar kind/null/rejection domain, deterministic hashes, TOCTOU postconditions, public exports, and zero retained geometry/frame objects. Existing source/catalog regressions remain required because this module depends on their archive and metadata authority.

This is factual EP attribute evidence only. It does not interpret protected-area categories or legal regimes; map Natura 2000 or ZNIEFF; load EP geometries or parcels; compute intersection/distance; exclude land; score; rank; or alter source URLs, cache/extraction schemas, catalog schema/hash, archive bytes, or physical metadata.

## 10. Exact complete current file content

```python
"""Source-bound attribute-only profile of verified INPN EP GeoPackages."""

from __future__ import annotations

import base64
import binascii
import json
import math
import re
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from typing import cast

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
from geopandas.array import GeometryDtype  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.sources.inpn_protected_areas_catalog_fr import (
    CATALOG_HASH_SCHEMA_VERSION,
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasGeoPackageCatalog,
    InpnProtectedAreasLayerCatalog,
    _read_verified_package_bytes,
    _suppress_pyogrio_bytes_gpkg_warning,
    build_inpn_protected_areas_catalog,
    validate_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    validate_inpn_protected_areas_extraction,
)

ATTRIBUTE_PROFILE_SCHEMA_VERSION = 1
ATTRIBUTE_VALUE_KINDS = (
    "TEXT",
    "BOOLEAN",
    "INTEGER",
    "FLOAT_HEX",
    "BINARY_BASE64",
)
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
_INTEGER_PATTERN = re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)")


class InpnProtectedAreasAttributeProfileError(ValueError):
    """Raised when exact EP attribute facts cannot be proven safely."""


@dataclass(frozen=True)
class InpnProtectedAreasDistinctAttributeValue:
    """One canonical non-null field value and its exact frequency."""

    value_kind: str
    canonical_value: str
    count: int


@dataclass(frozen=True)
class InpnProtectedAreasFieldAttributeProfile:
    """Complete factual value evidence for one physical attribute field."""

    name: str
    position: int
    source_dtype: str
    runtime_dtype: str
    null_count: int
    non_null_count: int
    distinct_non_null_count: int
    distinct_values: tuple[InpnProtectedAreasDistinctAttributeValue, ...]
    column_content_sha256: str


@dataclass(frozen=True)
class InpnProtectedAreasLayerAttributeProfile:
    """Attribute and FID evidence for one physical OGR layer."""

    relative_path: str
    file_size: int
    file_sha256: str
    package_position: int
    driver_name: str
    layer_name: str
    layer_position: int
    feature_count: int
    fid_count: int
    fid_min: int | None
    fid_max: int | None
    fid_sequence_sha256: str
    row_content_sha256: str
    fields: tuple[InpnProtectedAreasFieldAttributeProfile, ...]


@dataclass(frozen=True)
class InpnProtectedAreasAttributeProfile:
    """Portable complete attribute profile bound to one verified EP catalog."""

    attribute_profile_schema_version: int
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
    layers: tuple[InpnProtectedAreasLayerAttributeProfile, ...]
    package_count: int
    layer_count: int
    field_definition_count: int
    total_row_count: int
    total_null_count: int
    total_distinct_non_null_value_count: int
    complete_attribute_profile_content_sha256: str


@dataclass(frozen=True)
class _CanonicalCell:
    value_kind: str | None
    canonical_value: str | None


def _canonical_json_sha256(value: object, label: str) -> str:
    try:
        encoded = json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (OverflowError, TypeError, ValueError) as error:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
    if type(config) is not InpnProtectedAreasSourceConfig:
        raise InpnProtectedAreasAttributeProfileError(
            "config must be an exact InpnProtectedAreasSourceConfig"
        )
    try:
        return InpnProtectedAreasSourceConfig.model_validate(
            config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValueError) as error:
        raise InpnProtectedAreasAttributeProfileError(
            "INPN protected-areas source config is invalid"
        ) from error


def _prepare_inputs(
    extraction: object,
    config: object,
    catalog: object,
) -> tuple[
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasCatalog,
]:
    if type(extraction) is not InpnProtectedAreasExtraction:
        raise InpnProtectedAreasAttributeProfileError(
            "extraction must be an exact InpnProtectedAreasExtraction"
        )
    validated_config = _validated_config(config)
    if type(catalog) is not InpnProtectedAreasCatalog:
        raise InpnProtectedAreasAttributeProfileError(
            "catalog must be an exact InpnProtectedAreasCatalog"
        )
    try:
        fresh_extraction = validate_inpn_protected_areas_extraction(
            extraction,
            validated_config,
        )
        validate_inpn_protected_areas_catalog(
            fresh_extraction,
            validated_config,
            catalog,
        )
        fresh_catalog = build_inpn_protected_areas_catalog(
            fresh_extraction,
            validated_config,
        )
    except (InpnProtectedAreasCatalogError, InpnProtectedAreasSourceError) as error:
        raise InpnProtectedAreasAttributeProfileError(
            "INPN extraction or physical catalog failed source-complete validation"
        ) from error
    if catalog != fresh_catalog:
        raise InpnProtectedAreasAttributeProfileError(
            "supplied catalog differs from fresh physical catalog"
        )
    return fresh_extraction, validated_config, fresh_catalog


def _is_null_scalar(value: object) -> bool:
    if value is None or value is pd.NA or value is pd.NaT:
        return True
    if isinstance(value, (float, np.floating)):
        return math.isnan(float(value))
    if isinstance(value, np.datetime64):
        return bool(np.isnat(value))
    return False


def _canonical_cell(
    value: object,
    *,
    relative_path: str,
    layer_name: str,
    field_name: str,
    fid: int,
) -> _CanonicalCell:
    if _is_null_scalar(value):
        return _CanonicalCell(None, None)
    if type(value) is str:
        return _CanonicalCell("TEXT", value)
    if isinstance(value, np.str_):
        return _CanonicalCell("TEXT", str(value))
    if type(value) is bool or isinstance(value, np.bool_):
        return _CanonicalCell("BOOLEAN", "true" if bool(value) else "false")
    if type(value) is int or isinstance(value, np.integer):
        return _CanonicalCell("INTEGER", str(int(value)))
    if type(value) is float or isinstance(value, np.floating):
        finite = float(value)
        if not math.isfinite(finite):
            raise InpnProtectedAreasAttributeProfileError(
                f"package {relative_path} layer {layer_name} field {field_name} "
                f"FID {fid}: non-finite non-null numeric value"
            )
        return _CanonicalCell("FLOAT_HEX", finite.hex())
    if type(value) is bytes:
        return _CanonicalCell(
            "BINARY_BASE64",
            base64.b64encode(value).decode("ascii"),
        )
    if isinstance(value, (datetime, date, pd.Timestamp, np.datetime64)):
        raise InpnProtectedAreasAttributeProfileError(
            f"package {relative_path} layer {layer_name} field {field_name} FID {fid}: "
            "temporal value was not returned as text"
        )
    if isinstance(value, BaseGeometry):
        detail = "Shapely geometry value is forbidden"
    elif isinstance(value, bytearray):
        detail = "mutable bytearray value is forbidden"
    elif isinstance(value, (list, tuple, dict, set, frozenset)):
        detail = "composite attribute value is forbidden"
    else:
        detail = "unsupported attribute value"
    raise InpnProtectedAreasAttributeProfileError(
        f"package {relative_path} layer {layer_name} field {field_name} FID {fid}: "
        f"{detail} ({type(value).__module__}.{type(value).__qualname__})"
    )


def _canonical_fids(
    frame: pd.DataFrame,
    *,
    relative_path: str,
    layer_name: str,
) -> tuple[tuple[int, int], ...]:
    if isinstance(frame.index, pd.MultiIndex):
        raise InpnProtectedAreasAttributeProfileError(
            f"package {relative_path} layer {layer_name}: FID index must not be a MultiIndex"
        )
    result: list[tuple[int, int]] = []
    for row_position, value in enumerate(frame.index.tolist()):
        if type(value) is bool or isinstance(value, np.bool_):
            raise InpnProtectedAreasAttributeProfileError(
                f"package {relative_path} layer {layer_name}: Boolean FID at row {row_position}"
            )
        if type(value) is not int and not isinstance(value, np.integer):
            raise InpnProtectedAreasAttributeProfileError(
                f"package {relative_path} layer {layer_name}: non-integral or null FID "
                f"at row {row_position}"
            )
        result.append((int(value), row_position))
    fids = tuple(fid for fid, _ in result)
    if len(fids) != len(set(fids)):
        raise InpnProtectedAreasAttributeProfileError(
            f"package {relative_path} layer {layer_name}: duplicate FID"
        )
    return tuple(sorted(result, key=lambda item: item[0]))


def _validate_attribute_frame(
    frame: object,
    package: InpnProtectedAreasGeoPackageCatalog,
    layer: InpnProtectedAreasLayerCatalog,
) -> tuple[pd.DataFrame, tuple[tuple[int, int], ...]]:
    label = f"package {package.relative_path} layer {layer.layer_name}"
    if type(frame) is not pd.DataFrame:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label}: reader must return an exact pandas.DataFrame"
        )
    validated_frame = cast(pd.DataFrame, frame)
    expected_columns = tuple(field.name for field in layer.fields)
    actual_columns = tuple(validated_frame.columns.tolist())
    if any(type(name) is not str for name in actual_columns):
        raise InpnProtectedAreasAttributeProfileError(
            f"{label}: attribute columns must be exact strings"
        )
    if len(actual_columns) != len(set(actual_columns)):
        raise InpnProtectedAreasAttributeProfileError(
            f"{label}: duplicate attribute column"
        )
    if actual_columns != expected_columns:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label}: attribute columns differ from exact catalog order"
        )
    if len(validated_frame) != layer.feature_count:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label}: attribute row count differs from catalog feature count"
        )
    if any(isinstance(dtype, GeometryDtype) for dtype in validated_frame.dtypes):
        raise InpnProtectedAreasAttributeProfileError(
            f"{label}: geometry dtype is forbidden in attribute-only read"
        )
    return validated_frame, _canonical_fids(
        validated_frame,
        relative_path=package.relative_path,
        layer_name=layer.layer_name,
    )


def _cell_payload(cell: _CanonicalCell) -> object:
    if cell.value_kind is None:
        return None
    return [cell.value_kind, cell.canonical_value]


def _profile_layer(
    package_bytes: bytes,
    package: InpnProtectedAreasGeoPackageCatalog,
    layer: InpnProtectedAreasLayerCatalog,
) -> InpnProtectedAreasLayerAttributeProfile:
    field_names = [field.name for field in layer.fields]
    try:
        with _suppress_pyogrio_bytes_gpkg_warning():
            raw_frame = pyogrio.read_dataframe(
                package_bytes,
                layer=layer.layer_name,
                columns=field_names,
                read_geometry=False,
                fid_as_index=True,
                use_arrow=False,
                datetime_as_string=True,
            )
    except InpnProtectedAreasAttributeProfileError:
        raise
    except Exception as error:
        raise InpnProtectedAreasAttributeProfileError(
            f"package {package.relative_path} layer {layer.layer_name}: "
            "attribute-only Pyogrio read failed"
        ) from error

    frame, ordered_fids = _validate_attribute_frame(raw_frame, package, layer)
    cells_by_field: list[list[_CanonicalCell]] = [[] for _ in layer.fields]
    row_payload: list[object] = []
    for fid, row_position in ordered_fids:
        row_cells: list[object] = []
        for field_position, field in enumerate(layer.fields):
            value = frame.iloc[row_position, field_position]
            cell = _canonical_cell(
                value,
                relative_path=package.relative_path,
                layer_name=layer.layer_name,
                field_name=field.name,
                fid=fid,
            )
            cells_by_field[field_position].append(cell)
            row_cells.append([field.name, _cell_payload(cell)])
        row_payload.append([fid, row_cells])

    field_profiles: list[InpnProtectedAreasFieldAttributeProfile] = []
    for field_position, field in enumerate(layer.fields):
        cells = cells_by_field[field_position]
        frequencies: dict[tuple[str, str], int] = {}
        null_count = 0
        column_payload: list[object] = []
        for (fid, _), cell in zip(ordered_fids, cells, strict=True):
            column_payload.append([fid, _cell_payload(cell)])
            if cell.value_kind is None:
                null_count += 1
            else:
                key = (cell.value_kind, cell.canonical_value or "")
                frequencies[key] = frequencies.get(key, 0) + 1
        distinct_values = tuple(
            InpnProtectedAreasDistinctAttributeValue(kind, value, count)
            for (kind, value), count in sorted(frequencies.items())
        )
        non_null_count = len(cells) - null_count
        field_profiles.append(
            InpnProtectedAreasFieldAttributeProfile(
                name=field.name,
                position=field.position,
                source_dtype=field.source_dtype,
                runtime_dtype=str(frame.dtypes.iloc[field_position]),
                null_count=null_count,
                non_null_count=non_null_count,
                distinct_non_null_count=len(distinct_values),
                distinct_values=distinct_values,
                column_content_sha256=_canonical_json_sha256(
                    column_payload,
                    f"package {package.relative_path} layer {layer.layer_name} "
                    f"field {field.name} content",
                ),
            )
        )

    fids = [fid for fid, _ in ordered_fids]
    return InpnProtectedAreasLayerAttributeProfile(
        relative_path=package.relative_path,
        file_size=package.file_size,
        file_sha256=package.file_sha256,
        package_position=package.package_position,
        driver_name=package.driver_name,
        layer_name=layer.layer_name,
        layer_position=layer.layer_position,
        feature_count=layer.feature_count,
        fid_count=len(fids),
        fid_min=min(fids) if fids else None,
        fid_max=max(fids) if fids else None,
        fid_sequence_sha256=_canonical_json_sha256(
            fids,
            f"package {package.relative_path} layer {layer.layer_name} FIDs",
        ),
        row_content_sha256=_canonical_json_sha256(
            {
                "fields": field_names,
                "rows": row_payload,
            },
            f"package {package.relative_path} layer {layer.layer_name} rows",
        ),
        fields=tuple(field_profiles),
    )


def _distinct_value_payload(
    value: InpnProtectedAreasDistinctAttributeValue,
) -> dict[str, object]:
    return {
        "value_kind": value.value_kind,
        "canonical_value": value.canonical_value,
        "count": value.count,
    }


def _field_profile_payload(
    field: InpnProtectedAreasFieldAttributeProfile,
) -> dict[str, object]:
    return {
        "name": field.name,
        "position": field.position,
        "source_dtype": field.source_dtype,
        "runtime_dtype": field.runtime_dtype,
        "null_count": field.null_count,
        "non_null_count": field.non_null_count,
        "distinct_non_null_count": field.distinct_non_null_count,
        "distinct_values": [
            _distinct_value_payload(value) for value in field.distinct_values
        ],
        "column_content_sha256": field.column_content_sha256,
    }


def _layer_profile_payload(
    layer: InpnProtectedAreasLayerAttributeProfile,
) -> dict[str, object]:
    return {
        "relative_path": layer.relative_path,
        "file_size": layer.file_size,
        "file_sha256": layer.file_sha256,
        "package_position": layer.package_position,
        "driver_name": layer.driver_name,
        "layer_name": layer.layer_name,
        "layer_position": layer.layer_position,
        "feature_count": layer.feature_count,
        "fid_count": layer.fid_count,
        "fid_min": layer.fid_min,
        "fid_max": layer.fid_max,
        "fid_sequence_sha256": layer.fid_sequence_sha256,
        "row_content_sha256": layer.row_content_sha256,
        "fields": [_field_profile_payload(field) for field in layer.fields],
    }


def _profile_payload(
    profile: InpnProtectedAreasAttributeProfile,
) -> dict[str, object]:
    return {
        "attribute_profile_schema_version": profile.attribute_profile_schema_version,
        "provider": profile.provider,
        "authority": profile.authority,
        "program": profile.program,
        "dataset_id": profile.dataset_id,
        "dataset_name": profile.dataset_name,
        "declared_version": profile.declared_version,
        "reference_page_url": profile.reference_page_url,
        "archive_url": profile.archive_url,
        "archive_filename": profile.archive_filename,
        "archive_size": profile.archive_size,
        "archive_sha256": profile.archive_sha256,
        "source_catalog_schema_version": profile.source_catalog_schema_version,
        "source_catalog_content_sha256": profile.source_catalog_content_sha256,
        "layers": [_layer_profile_payload(layer) for layer in profile.layers],
        "package_count": profile.package_count,
        "layer_count": profile.layer_count,
        "field_definition_count": profile.field_definition_count,
        "total_row_count": profile.total_row_count,
        "total_null_count": profile.total_null_count,
        "total_distinct_non_null_value_count": (
            profile.total_distinct_non_null_value_count
        ),
    }


def _profile_content_sha256(profile: InpnProtectedAreasAttributeProfile) -> str:
    return _canonical_json_sha256(_profile_payload(profile), "attribute profile")


def _build_profile(
    extraction: InpnProtectedAreasExtraction,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasAttributeProfile:
    layers: list[InpnProtectedAreasLayerAttributeProfile] = []
    for package in catalog.packages:
        item = extraction.files[package.package_position]
        if (
            type(item) is not InpnProtectedAreasExtractedFile
            or item.relative_path != package.relative_path
            or item.file_size != package.file_size
            or item.sha256 != package.file_sha256
        ):
            raise InpnProtectedAreasAttributeProfileError(
                f"package {package.relative_path}: extraction/catalog identity differs"
            )
        try:
            package_bytes = _read_verified_package_bytes(extraction, item)
        except InpnProtectedAreasCatalogError as error:
            raise InpnProtectedAreasAttributeProfileError(
                f"package {package.relative_path}: byte identity cannot be verified"
            ) from error
        for layer in package.layers:
            layers.append(_profile_layer(package_bytes, package, layer))

    profile = InpnProtectedAreasAttributeProfile(
        attribute_profile_schema_version=ATTRIBUTE_PROFILE_SCHEMA_VERSION,
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
        layers=tuple(layers),
        package_count=catalog.package_count,
        layer_count=len(layers),
        field_definition_count=sum(len(layer.fields) for layer in layers),
        total_row_count=sum(layer.feature_count for layer in layers),
        total_null_count=sum(
            field.null_count for layer in layers for field in layer.fields
        ),
        total_distinct_non_null_value_count=sum(
            field.distinct_non_null_count for layer in layers for field in layer.fields
        ),
        complete_attribute_profile_content_sha256="",
    )
    return replace(
        profile,
        complete_attribute_profile_content_sha256=_profile_content_sha256(profile),
    )


def _exact_text(value: object, label: str, *, allow_empty: bool = False) -> str:
    if type(value) is not str or (not allow_empty and not value):
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} must be an exact built-in string"
        )
    return value


def _exact_non_negative_int(value: object, label: str) -> int:
    if type(value) is not int or value < 0:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} must be an exact non-negative integer"
        )
    return value


def _exact_sha(value: object, label: str) -> str:
    if type(value) is not str or _SHA_PATTERN.fullmatch(value) is None:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} must be a canonical SHA256"
        )
    return value


def _validate_canonical_distinct_value(
    value: object,
    *,
    label: str,
) -> InpnProtectedAreasDistinctAttributeValue:
    if type(value) is not InpnProtectedAreasDistinctAttributeValue:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} has invalid nested value type"
        )
    kind = _exact_text(value.value_kind, f"{label} value_kind")
    canonical = _exact_text(
        value.canonical_value,
        f"{label} canonical_value",
        allow_empty=True,
    )
    if kind not in ATTRIBUTE_VALUE_KINDS:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} has unsupported value kind"
        )
    if type(value.count) is not int or value.count <= 0:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} count must be an exact positive integer"
        )
    if kind == "BOOLEAN" and canonical not in {"false", "true"}:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} Boolean value is not canonical"
        )
    if kind == "INTEGER" and _INTEGER_PATTERN.fullmatch(canonical) is None:
        raise InpnProtectedAreasAttributeProfileError(
            f"{label} integer value is not canonical"
        )
    if kind == "FLOAT_HEX":
        try:
            number = float.fromhex(canonical)
        except (OverflowError, ValueError) as error:
            raise InpnProtectedAreasAttributeProfileError(
                f"{label} float value is not canonical"
            ) from error
        if not math.isfinite(number) or number.hex() != canonical:
            raise InpnProtectedAreasAttributeProfileError(
                f"{label} float value is not canonical"
            )
    if kind == "BINARY_BASE64":
        try:
            decoded = base64.b64decode(canonical, validate=True)
        except (binascii.Error, ValueError) as error:
            raise InpnProtectedAreasAttributeProfileError(
                f"{label} binary value is not canonical Base64"
            ) from error
        if base64.b64encode(decoded).decode("ascii") != canonical:
            raise InpnProtectedAreasAttributeProfileError(
                f"{label} binary value is not canonical Base64"
            )
    return value


def _validate_profile_intrinsic(
    profile: object,
) -> InpnProtectedAreasAttributeProfile:
    if type(profile) is not InpnProtectedAreasAttributeProfile:
        raise InpnProtectedAreasAttributeProfileError(
            "profile must be an exact InpnProtectedAreasAttributeProfile"
        )
    if (
        type(profile.attribute_profile_schema_version) is not int
        or profile.attribute_profile_schema_version != ATTRIBUTE_PROFILE_SCHEMA_VERSION
    ):
        raise InpnProtectedAreasAttributeProfileError(
            "attribute profile schema version is invalid"
        )
    for name in (
        "provider",
        "authority",
        "program",
        "dataset_id",
        "dataset_name",
        "declared_version",
        "reference_page_url",
        "archive_url",
        "archive_filename",
    ):
        _exact_text(getattr(profile, name), f"profile {name}")
    if type(profile.archive_size) is not int or profile.archive_size <= 0:
        raise InpnProtectedAreasAttributeProfileError("profile archive size is invalid")
    _exact_sha(profile.archive_sha256, "profile archive SHA256")
    if (
        type(profile.source_catalog_schema_version) is not int
        or profile.source_catalog_schema_version != CATALOG_HASH_SCHEMA_VERSION
    ):
        raise InpnProtectedAreasAttributeProfileError(
            "source catalog schema version is invalid"
        )
    _exact_sha(
        profile.source_catalog_content_sha256,
        "profile source catalog SHA256",
    )
    if type(profile.layers) is not tuple or not profile.layers:
        raise InpnProtectedAreasAttributeProfileError(
            "profile layers must be a non-empty exact tuple"
        )

    package_paths: dict[int, str] = {}
    layer_identities: set[tuple[str, str]] = set()
    expected_order: list[tuple[int, int]] = []
    field_count = 0
    total_rows = 0
    total_nulls = 0
    total_distinct = 0
    for layer in profile.layers:
        if type(layer) is not InpnProtectedAreasLayerAttributeProfile:
            raise InpnProtectedAreasAttributeProfileError(
                "profile layer nested type is invalid"
            )
        path = _exact_text(layer.relative_path, "profile layer package path")
        if type(layer.file_size) is not int or layer.file_size <= 0:
            raise InpnProtectedAreasAttributeProfileError(
                f"package {path}: profile file size is invalid"
            )
        _exact_sha(layer.file_sha256, f"package {path} file SHA256")
        package_position = _exact_non_negative_int(
            layer.package_position,
            f"package {path} position",
        )
        previous_path = package_paths.setdefault(package_position, path)
        if previous_path != path:
            raise InpnProtectedAreasAttributeProfileError(
                "profile package position maps to multiple paths"
            )
        if _exact_text(layer.driver_name, f"package {path} driver") != "GPKG":
            raise InpnProtectedAreasAttributeProfileError(
                f"package {path}: driver must be exact GPKG"
            )
        layer_name = _exact_text(layer.layer_name, f"package {path} layer name")
        layer_position = _exact_non_negative_int(
            layer.layer_position,
            f"package {path} layer {layer_name} position",
        )
        identity = (path, layer_name)
        if identity in layer_identities:
            raise InpnProtectedAreasAttributeProfileError(
                "profile contains a duplicate package/layer identity"
            )
        layer_identities.add(identity)
        expected_order.append((package_position, layer_position))
        feature_count = _exact_non_negative_int(
            layer.feature_count,
            f"package {path} layer {layer_name} feature count",
        )
        fid_count = _exact_non_negative_int(
            layer.fid_count,
            f"package {path} layer {layer_name} FID count",
        )
        if fid_count != feature_count:
            raise InpnProtectedAreasAttributeProfileError(
                f"package {path} layer {layer_name}: FID/feature counts differ"
            )
        if feature_count == 0:
            if layer.fid_min is not None or layer.fid_max is not None:
                raise InpnProtectedAreasAttributeProfileError(
                    f"package {path} layer {layer_name}: empty FID range must be null"
                )
        elif (
            type(layer.fid_min) is not int
            or type(layer.fid_max) is not int
            or layer.fid_min > layer.fid_max
        ):
            raise InpnProtectedAreasAttributeProfileError(
                f"package {path} layer {layer_name}: FID range is invalid"
            )
        _exact_sha(
            layer.fid_sequence_sha256,
            f"package {path} layer {layer_name} FID hash",
        )
        _exact_sha(
            layer.row_content_sha256,
            f"package {path} layer {layer_name} row hash",
        )
        if type(layer.fields) is not tuple:
            raise InpnProtectedAreasAttributeProfileError(
                f"package {path} layer {layer_name}: fields must be an exact tuple"
            )
        field_names: set[str] = set()
        for position, field in enumerate(layer.fields):
            if type(field) is not InpnProtectedAreasFieldAttributeProfile:
                raise InpnProtectedAreasAttributeProfileError(
                    f"package {path} layer {layer_name}: field nested type is invalid"
                )
            field_name = _exact_text(field.name, f"{identity} field name")
            if field_name in field_names:
                raise InpnProtectedAreasAttributeProfileError(
                    f"package {path} layer {layer_name}: duplicate field name"
                )
            field_names.add(field_name)
            if type(field.position) is not int or field.position != position:
                raise InpnProtectedAreasAttributeProfileError(
                    f"package {path} layer {layer_name} field {field_name}: "
                    "position is invalid"
                )
            _exact_text(field.source_dtype, f"field {field_name} source dtype")
            _exact_text(field.runtime_dtype, f"field {field_name} runtime dtype")
            null_count = _exact_non_negative_int(
                field.null_count,
                f"field {field_name} null count",
            )
            non_null_count = _exact_non_negative_int(
                field.non_null_count,
                f"field {field_name} non-null count",
            )
            distinct_count = _exact_non_negative_int(
                field.distinct_non_null_count,
                f"field {field_name} distinct count",
            )
            if null_count + non_null_count != feature_count:
                raise InpnProtectedAreasAttributeProfileError(
                    f"package {path} layer {layer_name} field {field_name}: "
                    "null/non-null counts differ from feature count"
                )
            if type(field.distinct_values) is not tuple:
                raise InpnProtectedAreasAttributeProfileError(
                    f"field {field_name}: distinct values must be an exact tuple"
                )
            values = tuple(
                _validate_canonical_distinct_value(
                    value,
                    label=f"field {field_name} distinct value {value_position}",
                )
                for value_position, value in enumerate(field.distinct_values)
            )
            ordering = tuple(
                (value.value_kind, value.canonical_value) for value in values
            )
            if ordering != tuple(sorted(ordering)) or len(set(ordering)) != len(
                ordering
            ):
                raise InpnProtectedAreasAttributeProfileError(
                    f"field {field_name}: distinct value domain is not canonical"
                )
            if (
                len(values) != distinct_count
                or sum(value.count for value in values) != non_null_count
            ):
                raise InpnProtectedAreasAttributeProfileError(
                    f"field {field_name}: distinct value counts are inconsistent"
                )
            _exact_sha(field.column_content_sha256, f"field {field_name} column hash")
            field_count += 1
            total_nulls += null_count
            total_distinct += distinct_count
        total_rows += feature_count

    if expected_order != sorted(expected_order) or set(package_paths) != set(
        range(len(package_paths))
    ):
        raise InpnProtectedAreasAttributeProfileError(
            "profile package/layer order is invalid"
        )
    expected_counts = (
        len(package_paths),
        len(profile.layers),
        field_count,
        total_rows,
        total_nulls,
        total_distinct,
    )
    actual_counts = (
        profile.package_count,
        profile.layer_count,
        profile.field_definition_count,
        profile.total_row_count,
        profile.total_null_count,
        profile.total_distinct_non_null_value_count,
    )
    if any(type(value) is not int or value < 0 for value in actual_counts) or (
        actual_counts != expected_counts
    ):
        raise InpnProtectedAreasAttributeProfileError(
            "attribute profile aggregate counts are invalid"
        )
    _exact_sha(
        profile.complete_attribute_profile_content_sha256,
        "complete attribute profile SHA256",
    )
    if (
        _profile_content_sha256(profile)
        != profile.complete_attribute_profile_content_sha256
    ):
        raise InpnProtectedAreasAttributeProfileError(
            "complete attribute profile SHA256 is invalid"
        )
    return profile


def _build_with_postconditions(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasAttributeProfile:
    profile = _validate_profile_intrinsic(_build_profile(extraction, catalog))
    try:
        final_extraction = validate_inpn_protected_areas_extraction(
            extraction,
            config,
        )
        final_catalog = build_inpn_protected_areas_catalog(final_extraction, config)
    except (InpnProtectedAreasCatalogError, InpnProtectedAreasSourceError) as error:
        raise InpnProtectedAreasAttributeProfileError(
            "INPN source changed during attribute profiling"
        ) from error
    if final_extraction != extraction or final_catalog != catalog:
        raise InpnProtectedAreasAttributeProfileError(
            "INPN extraction or catalog changed during attribute profiling"
        )
    return profile


def build_inpn_protected_areas_attribute_profile(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> InpnProtectedAreasAttributeProfile:
    """Build the complete non-geometry attribute profile of verified EP bytes."""

    try:
        fresh_extraction, validated_config, fresh_catalog = _prepare_inputs(
            extraction,
            config,
            catalog,
        )
        return _build_with_postconditions(
            fresh_extraction,
            validated_config,
            fresh_catalog,
        )
    except InpnProtectedAreasAttributeProfileError:
        raise
    except Exception as error:
        raise InpnProtectedAreasAttributeProfileError(
            "INPN protected-areas attribute profile cannot be built safely"
        ) from error


def validate_inpn_protected_areas_attribute_profile(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
    profile: InpnProtectedAreasAttributeProfile,
) -> None:
    """Intrinsically validate, physically rebuild, and compare one profile."""

    try:
        validated_profile = _validate_profile_intrinsic(profile)
        fresh_extraction, validated_config, fresh_catalog = _prepare_inputs(
            extraction,
            config,
            catalog,
        )
        rebuilt = _build_with_postconditions(
            fresh_extraction,
            validated_config,
            fresh_catalog,
        )
        if validated_profile != rebuilt:
            raise InpnProtectedAreasAttributeProfileError(
                "attribute profile differs from independently rebuilt physical values"
            )
    except InpnProtectedAreasAttributeProfileError:
        raise
    except Exception as error:
        raise InpnProtectedAreasAttributeProfileError(
            "INPN protected-areas attribute profile validation failed safely"
        ) from error


__all__ = [
    "InpnProtectedAreasAttributeProfile",
    "InpnProtectedAreasAttributeProfileError",
    "InpnProtectedAreasDistinctAttributeValue",
    "InpnProtectedAreasFieldAttributeProfile",
    "InpnProtectedAreasLayerAttributeProfile",
    "build_inpn_protected_areas_attribute_profile",
    "validate_inpn_protected_areas_attribute_profile",
]
```
