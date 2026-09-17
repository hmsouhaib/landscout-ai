# `src/landscout/sources/inpn_protected_areas_evidence_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_evidence_fr.py`
- Layer/domain: source-bound factual INPN EP evidence assembly
- Source SHA256: `55762f6a3ae7b51c5d3550e32d69b424aa300a2eac508c5b492e8a502b641bd6`
- New bundle schema: `1`; existing catalog schema `2`, attribute schema `1`, and geometry schema `1` are unchanged.

## 1. Responsibility and boundary

This module retains the already-built catalog and two immutable profiles in one source-complete evidence bundle and proves their exact physical FID-domain alignment. It does not join raw attribute cells to geometries or introduce a third reader. Public entry points always reuse both existing public physical profile validators and a final extraction postcondition. Private intrinsic/alignment helpers prove only internal structure, never source authority.

The approved attribute reader remains Pyogrio with `read_geometry=False` and the exact existing field/FID options. The approved geometry reader remains immutable package bytes deserialized into query-only SQLite, selecting only physical FID plus geometry BLOB. Measured geometry does not pass through Pyogrio. No category interpretation, Natura 2000/ZNIEFF mapping, CRS repair/reprojection, geometry normalization, parcel relation, exclusion, score, ranking, or legal/BESS decision is added. Matching FIDs do not resolve `EP/sig_tadl.gpkg`'s recorded CRS/coordinate observation.

## 2. Imports and qualified ownership

| Binding | Owner and role |
|---|---|
| `annotations` | `__future__`; deferred annotations only. |
| `json`, `re`, `sha256` | Standard-library JSON serializer, lowercase digest grammar, and `hashlib.sha256`. |
| `asdict`, `dataclass`, `fields`, `replace` | `dataclasses`; alignment-only payloads, frozen records, exact field-type checks, and immutable digest completion. |
| `InpnProtectedAreasAttributeProfile`, `InpnProtectedAreasAttributeProfileError`, `validate_inpn_protected_areas_attribute_profile` | `landscout.sources.inpn_protected_areas_attributes_fr`; retained attribute model, controlled error, and mandatory physical profile validator. |
| `_validate_attributes_intrinsic` | Alias of **attribute module** `_validate_profile_intrinsic`, not a geometry or evidence-owned implementation; cheap nested attribute structure/hash checks only. |
| `InpnProtectedAreasCatalog`, `InpnProtectedAreasCatalogError`, `_validate_catalog_intrinsic` | `landscout.sources.inpn_protected_areas_catalog_fr`; metadata evidence/error and private intrinsic catalog checks. Physical catalog validation occurs inside the public profile validators. |
| `InpnProtectedAreasExtraction`, `InpnProtectedAreasSourceConfig`, `InpnProtectedAreasSourceError`, `validate_inpn_protected_areas_extraction` | `landscout.sources.inpn_protected_areas_fr`; extraction/config authority, source error, and final physical extraction validation. |
| `InpnProtectedAreasGeometryProfile`, `InpnProtectedAreasGeometryProfileError`, `validate_inpn_protected_areas_geometry_profile` | `landscout.sources.inpn_protected_areas_geometry_fr`; retained geometry model/error and mandatory independent physical geometry rebuild. |
| `_validate_geometries_intrinsic` | Alias of **geometry module** `_validate_profile_intrinsic`, distinct from the similarly named attribute helper; private structure/hash checks only. |

## 3. Constants and exports

`EVIDENCE_BUNDLE_SCHEMA_VERSION` is 1 and is not included in `__all__`; `_SHA_PATTERN` requires exactly 64 lowercase hexadecimal characters through `fullmatch`. `_SOURCE_FIELDS` contains the eleven portable source/archive lineage fields, and `_PACKAGE_FIELDS` contains the five repeated package facts checked against the catalog. `_UPSTREAM_ERRORS` is exactly the four source/catalog/attribute/geometry controlled error classes. These tuples are comparison declarations, not serialized schemas. The only five public exports are the two new records, the controlled error, and the source-complete builder/validator; no structural helper or raw reader is exported.

```python
EVIDENCE_BUNDLE_SCHEMA_VERSION = 1

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

_PACKAGE_FIELDS = (
    "relative_path",
    "package_position",
    "file_size",
    "file_sha256",
    "driver_name",
)

_UPSTREAM_ERRORS = (
    InpnProtectedAreasSourceError,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasAttributeProfileError,
    InpnProtectedAreasGeometryProfileError,
)

__all__ = [
    "InpnProtectedAreasEvidenceBundle",
    "InpnProtectedAreasEvidenceError",
    "InpnProtectedAreasLayerAlignment",
    "build_inpn_protected_areas_evidence_bundle",
    "validate_inpn_protected_areas_evidence_bundle",
]
```

## 4. Exact records and field meanings

`InpnProtectedAreasEvidenceError(ValueError)` adds no fields and is the controlled boundary for malformed objects, noncanonical hashes, contradictory alignment, and failed physical source trust. Both dataclasses use `@dataclass(frozen=True)` and every field is required; only the two optional FID extrema permit None. Exact recursive validation plus existing immutable upstream records prevents mutable or subclass/coercible leaves from becoming accepted evidence; direct dataclass construction alone is not an independently validated source boundary.

### `InpnProtectedAreasLayerAlignment`

| Exact field annotation | Meaning |
|---|---|
| `relative_path: str` | Exact canonical portable `.gpkg` path relative to the verified extraction. Together with `layer_name`, identifies the physical layer; never an absolute filesystem path. |
| `package_position: int` | Exact zero-based catalog package position, retaining canonical package order. |
| `file_sha256: str` | Exact archive-derived package-byte SHA256 shared by catalog and both profiles; size and driver are cross-checked through retained upstream records. |
| `layer_name: str` | Exact catalog physical layer name; the same name in another package is a different key. |
| `layer_position: int` | Exact zero-based physical layer position within its catalog package. |
| `feature_count: int` | Exact catalog feature count, equal to both profile feature counts and both FID counts. |
| `fid_count: int` | Shared exact nonnegative physical FID count. The FID values themselves have no positivity, starting-value, or contiguity requirement. |
| `fid_min: int \| None` | Shared exact integer minimum, or exact `None` for an empty FID domain. |
| `fid_max: int \| None` | Shared exact integer maximum, or exact `None` for an empty FID domain. |
| `fid_sequence_sha256: str` | Shared SHA256 of the canonical sorted physical integer-FID JSON sequence; equal count/extrema alone do not establish this commitment. |

### `InpnProtectedAreasEvidenceBundle`

| Exact field annotation | Meaning |
|---|---|
| `evidence_bundle_schema_version: int` | Exact built-in integer `1`; distinct from unchanged upstream catalog schema 2 and profile schemas 1. |
| `catalog: InpnProtectedAreasCatalog` | Exact retained immutable `InpnProtectedAreasCatalog`, including all source/package/layer/field metadata; both public profile validators prove its physical authority. |
| `attributes: InpnProtectedAreasAttributeProfile` | Exact retained immutable `InpnProtectedAreasAttributeProfile`, physically rebuilt by its public validator, with all existing domains and hashes unchanged. |
| `geometries: InpnProtectedAreasGeometryProfile` | Exact retained immutable `InpnProtectedAreasGeometryProfile`, physically rebuilt by its public validator, retaining technical geometry facts and toolchain identity unchanged. |
| `layer_alignments: tuple[InpnProtectedAreasLayerAlignment, ...]` | Exact tuple containing every `InpnProtectedAreasLayerAlignment` in catalog package/layer order, with no omission, duplication, sorting repair, or semantic selection. |
| `complete_evidence_bundle_content_sha256: str` | Canonical lowercase SHA256 over `_bundle_payload`; does not include itself or duplicate expanded upstream domains. |

## 5. Alignment and physical validation order

The full `(relative_path, layer_name)` identity and unchanged catalog package/layer positions disambiguate identically named layers in different files. Intrinsic upstream checks preserve canonical path grammar, package grouping and order, identity uniqueness, exact scalar/tuple domains, FID range relationships, and complete-hash closure. Cross-profile checks add equality rather than replacing those contracts. Every catalog layer must produce one alignment; no missing or extra layer is tolerated.

The attribute profiler accepts Python/NumPy integral FIDs and converts them to exact built-in integers; the geometry reader requires SQLite FIDs already to be exact built-in integers. Both sort numerically and hash a JSON integer sequence with the same canonical options. Count and extrema are necessary but insufficient: `[1, 2, 4]` versus `[1, 3, 4]` is rejected by sequence SHA. Sparse and negative FIDs remain valid; empty FID ranges retain exact `None` extrema and the existing deterministic empty-sequence hash. No contiguity or business-identifier substitution is introduced.

Public order is exact types/config reconstruction -> public attribute physical validator -> public geometry physical validator -> structural alignment -> bundle hash -> final extraction equality. The independent validator adds intrinsic bundle preflight, then runs that same public source-complete builder and compares the full result. Neither `_align_layers` nor `_validate_bundle_intrinsic` is an approved alternate physical validator.

## 6. Every function and failure contract

### `_require_exact_type`

```python
def _require_exact_type(value: object, expected: type[object], label: str) -> None:
```

Rejects any value whose exact runtime class differs from `expected`, including subclasses; `label` supplies the controlled error context. It returns `None` and performs no coercion.

### `_validated_config`

```python
def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
```

Requires the exact source-config class, dumps canonical Python values, and reconstructs with `InpnProtectedAreasSourceConfig.model_validate`. This preserves source-lock and deep-immutability validation rather than treating a frozen supplied object as self-authenticating. Attribute/type/value failures are chained into the bundle error.

### `_align_layers`

```python
def _align_layers(
    catalog: InpnProtectedAreasCatalog,
    attributes: InpnProtectedAreasAttributeProfile,
    geometries: InpnProtectedAreasGeometryProfile,
) -> tuple[InpnProtectedAreasLayerAlignment, ...]:
```

Private structure-only alignment, not physical source validation. First invokes the catalog-owned intrinsic validator and the separately owned attribute/geometry intrinsic validators, translating their controlled failures with a cause. It compares the eleven `_SOURCE_FIELDS`; catalog schema/hash/package/layer counts; catalog total features against attribute total rows and geometry rows; and catalog field count against the attribute field-definition count. It flattens the catalog in its existing package/layer order and requires both profile lengths to match. Strict positional zip checks each repeated `_PACKAGE_FIELDS` tuple plus layer name/position, then each profile feature/FID count against catalog feature count, both FID extrema, and both FID sequence hashes. The ten-field output is copied from these already-equal facts and returned as an exact tuple. Source-level failures identify the profile; layer failures retain package/layer context. It never sorts, renumbers, filters, repairs, or reads a physical source.

### `_bundle_payload`

```python
def _bundle_payload(bundle: InpnProtectedAreasEvidenceBundle) -> dict[str, object]:
```

Constructs the exact compact schema-1 payload below. `asdict` applies only to each ten-field alignment, never to a complete upstream profile. The internal dictionary/list representation is ephemeral hashing input, not retained mutable trust data. Upstream schema/complete-hash pairs transitively commit all their evidence and the geometry toolchain.

### `_bundle_content_sha256`

```python
def _bundle_content_sha256(bundle: InpnProtectedAreasEvidenceBundle) -> str:
```

Serializes `_bundle_payload` with sorted JSON keys, compact comma/colon separators, Unicode preserved, and non-finite numbers forbidden, then UTF-8 encodes and SHA256 hashes the result. Overflow/type/value/Unicode failures become a chained controlled error. Python repr, class names, addresses, operational paths, times, and cache-hit state do not enter this payload.

### `_validate_bundle_intrinsic`

```python
def _validate_bundle_intrinsic(
    bundle: object,
) -> InpnProtectedAreasEvidenceBundle:
```

Requires the exact bundle class and exact integer schema 1, then obtains expected structural alignment through `_align_layers` (including every upstream intrinsic validator). Requires an exact complete tuple, exact alignment class, and for every dataclass field the same exact runtime type as the expected aligned value; this rejects Boolean-for-integer and string subclasses even when Python equality would pass. It exact-compares every alignment value, validates lowercase digest syntax, and recomputes complete bundle hash closure. It returns the supplied object, not a trusted physical reconstruction. No source or reader is opened here.

### `build_inpn_protected_areas_evidence_bundle`

```python
def build_inpn_protected_areas_evidence_bundle(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
    attributes: InpnProtectedAreasAttributeProfile,
    geometries: InpnProtectedAreasGeometryProfile,
) -> InpnProtectedAreasEvidenceBundle:
```

Source-complete builder. Checks exact extraction/catalog/profile classes and reconstructs config. Calls `validate_inpn_protected_areas_attribute_profile` once, followed by `validate_inpn_protected_areas_geometry_profile` once, each with the same extraction, validated config, and supplied catalog; these public owners perform existing physical extraction/catalog/profile reconstruction. Only after both succeed does it align, create the frozen bundle retaining those proven upstream objects, and fill its digest using `dataclasses.replace`. Finally, `validate_inpn_protected_areas_extraction` must return evidence exactly equal to the supplied extraction. Thus persistent source mutation after profile reads prevents return. Existing bundle errors propagate; lower controlled source/catalog/profile errors are chained with their useful original context; other exceptions become a safe controlled bundle error. No third reader, download, or direct filesystem/SQL access is added.

### `validate_inpn_protected_areas_evidence_bundle`

```python
def validate_inpn_protected_areas_evidence_bundle(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    bundle: InpnProtectedAreasEvidenceBundle,
) -> None:
```

Independent public validation. Checks exact extraction and reconstructs config, validates intrinsic nested structure/alignment/hash closure, then calls the public bundle builder with the retained catalog/profiles. The builder repeats both public physical profile validators once each and final extraction validation. The supplied complete bundle must exactly equal that rebuilt result. A coordinated nested/profile/bundle rehash therefore cannot override physical source evidence. Success returns `None`. Own controlled errors propagate; lower controlled errors and unexpected exceptions are safely chained into `InpnProtectedAreasEvidenceError`.

## 7. Exact bundle hash payload and compatibility

The complete payload is deliberately small: the bundle schema, each upstream schema and complete SHA256, and full ordered alignment records. Its exact shape is implemented here:

```python
def _bundle_payload(bundle: InpnProtectedAreasEvidenceBundle) -> dict[str, object]:
    """Bind upstream schema/hash commitments, not duplicated large value domains."""
    return {
        "evidence_bundle_schema_version": bundle.evidence_bundle_schema_version,
        "catalog": {
            "catalog_schema_version": bundle.catalog.catalog_schema_version,
            "complete_catalog_content_sha256": (
                bundle.catalog.complete_catalog_content_sha256
            ),
        },
        "attributes": {
            "attribute_profile_schema_version": (
                bundle.attributes.attribute_profile_schema_version
            ),
            "complete_attribute_profile_content_sha256": (
                bundle.attributes.complete_attribute_profile_content_sha256
            ),
        },
        "geometries": {
            "geometry_profile_schema_version": (
                bundle.geometries.geometry_profile_schema_version
            ),
            "complete_geometry_profile_content_sha256": (
                bundle.geometries.complete_geometry_profile_content_sha256
            ),
        },
        "layer_alignments": [asdict(item) for item in bundle.layer_alignments],
    }
```

Serialization is `json.dumps(..., sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")`, followed by `sha256(...).hexdigest()`. The complete bundle digest itself is excluded. Every ordered alignment has all ten documented fields. No upstream attribute domain or geometry domain is expanded again; its original complete hash remains the transitive commitment. Geometry profile identity includes its toolchain and encoding contract, so the new complete bundle hash inherits that dependence. The original catalog/profile fields, hash payloads, schemas, and verified EP archive bytes are unchanged. Portable relative paths are intentionally retained; absolute filesystem paths, cache-hit flags, timestamps, runtime duration, object identity, connections, raw BLOBs, and geometries are not part of the new records or hash.

## 8. Tests, side effects, and change impact

The paired [evidence-bundle test companion](../../../tests/unit/test_inpn_protected_areas_evidence_fr.py.md) distinguishes pure structural mismatch fixtures from real temporary ZIP/GeoPackage public-chain proofs. Coverage includes canonical keys/order/FIDs, identity and nested types, compact hashes, immediate mutation failures, coherent forgeries, public-validator call counts, physical postconditions, reader ownership, and public exports. Real EP evidence and executed counts belong to `docs/DEV_LOG.md`, not inferred from this contract.

The new module opens no file, network connection, dataframe reader, or SQLite connection itself. The public upstream validators intentionally perform the existing approved physical reads; the final extraction validator rehashes and validates existing archive/extraction state. No artifact is published and no source cache schema/layout changes. Future changes must preserve the distinction between cheap intrinsic closure and physical authority, retain complete alignment order, and make an explicit schema decision before altering the canonical bundle payload.

## 9. Exact complete current file content

```python
"""Source-bound alignment of existing INPN EP catalog and profile evidence."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, fields, replace
from hashlib import sha256

from landscout.sources.inpn_protected_areas_attributes_fr import (
    InpnProtectedAreasAttributeProfile,
    InpnProtectedAreasAttributeProfileError,
    validate_inpn_protected_areas_attribute_profile,
)
from landscout.sources.inpn_protected_areas_attributes_fr import (
    _validate_profile_intrinsic as _validate_attributes_intrinsic,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    _validate_catalog_intrinsic,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    validate_inpn_protected_areas_extraction,
)
from landscout.sources.inpn_protected_areas_geometry_fr import (
    InpnProtectedAreasGeometryProfile,
    InpnProtectedAreasGeometryProfileError,
    validate_inpn_protected_areas_geometry_profile,
)
from landscout.sources.inpn_protected_areas_geometry_fr import (
    _validate_profile_intrinsic as _validate_geometries_intrinsic,
)

EVIDENCE_BUNDLE_SCHEMA_VERSION = 1
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
_PACKAGE_FIELDS = (
    "relative_path",
    "package_position",
    "file_size",
    "file_sha256",
    "driver_name",
)
_UPSTREAM_ERRORS = (
    InpnProtectedAreasSourceError,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasAttributeProfileError,
    InpnProtectedAreasGeometryProfileError,
)


class InpnProtectedAreasEvidenceError(ValueError):
    """Raised when physical source trust or exact profile alignment fails."""


@dataclass(frozen=True)
class InpnProtectedAreasLayerAlignment:
    """One ordered physical layer and its shared canonical FID commitment."""

    relative_path: str
    package_position: int
    file_sha256: str
    layer_name: str
    layer_position: int
    feature_count: int
    fid_count: int
    fid_min: int | None
    fid_max: int | None
    fid_sequence_sha256: str


@dataclass(frozen=True)
class InpnProtectedAreasEvidenceBundle:
    """Immutable aligned profiles, not joined features or environmental policy."""

    evidence_bundle_schema_version: int
    catalog: InpnProtectedAreasCatalog
    attributes: InpnProtectedAreasAttributeProfile
    geometries: InpnProtectedAreasGeometryProfile
    layer_alignments: tuple[InpnProtectedAreasLayerAlignment, ...]
    complete_evidence_bundle_content_sha256: str


def _require_exact_type(value: object, expected: type[object], label: str) -> None:
    if type(value) is not expected:
        raise InpnProtectedAreasEvidenceError(
            f"{label} must be an exact {expected.__name__}"
        )


def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
    """Reconstruct supplied configuration without relaxing its source locks."""
    if type(config) is not InpnProtectedAreasSourceConfig:
        raise InpnProtectedAreasEvidenceError(
            "config must be an exact InpnProtectedAreasSourceConfig"
        )
    try:
        return InpnProtectedAreasSourceConfig.model_validate(
            config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValueError) as error:
        raise InpnProtectedAreasEvidenceError(
            f"INPN evidence source config is invalid: {error}"
        ) from error


def _align_layers(
    catalog: InpnProtectedAreasCatalog,
    attributes: InpnProtectedAreasAttributeProfile,
    geometries: InpnProtectedAreasGeometryProfile,
) -> tuple[InpnProtectedAreasLayerAlignment, ...]:
    """Check canonical structure and alignment only; this does not prove source trust."""
    try:
        _validate_catalog_intrinsic(catalog)
        _validate_attributes_intrinsic(attributes)
        _validate_geometries_intrinsic(geometries)
    except _UPSTREAM_ERRORS as error:
        raise InpnProtectedAreasEvidenceError(
            f"INPN profile structure cannot align: {error}"
        ) from error

    source_identity = tuple(getattr(catalog, name) for name in _SOURCE_FIELDS)
    catalog_identity = (
        catalog.catalog_schema_version,
        catalog.complete_catalog_content_sha256,
        catalog.package_count,
        catalog.layer_count,
    )
    for label, profile in (("attributes", attributes), ("geometries", geometries)):
        if tuple(getattr(profile, name) for name in _SOURCE_FIELDS) != source_identity:
            raise InpnProtectedAreasEvidenceError(
                f"{label}: source/archive identity differs from catalog"
            )
        if (
            profile.source_catalog_schema_version,
            profile.source_catalog_content_sha256,
            profile.package_count,
            profile.layer_count,
        ) != catalog_identity:
            raise InpnProtectedAreasEvidenceError(
                f"{label}: catalog identity or package/layer inventory differs"
            )
    if (
        attributes.total_row_count != catalog.total_feature_count
        or geometries.geometry_row_count != catalog.total_feature_count
        or attributes.field_definition_count != catalog.field_count
    ):
        raise InpnProtectedAreasEvidenceError("catalog/profile aggregate counts differ")

    catalog_layers = tuple(
        (package, layer) for package in catalog.packages for layer in package.layers
    )
    if len(attributes.layers) != len(catalog_layers) or len(geometries.layers) != len(
        catalog_layers
    ):
        raise InpnProtectedAreasEvidenceError(
            "catalog/profile layer inventories differ"
        )
    alignments: list[InpnProtectedAreasLayerAlignment] = []
    for (package, layer), attribute, geometry in zip(
        catalog_layers, attributes.layers, geometries.layers, strict=True
    ):
        label = f"package {package.relative_path} layer {layer.layer_name}"
        package_identity = tuple(getattr(package, name) for name in _PACKAGE_FIELDS)
        for kind, profile_layer in (("attribute", attribute), ("geometry", geometry)):
            if tuple(
                getattr(profile_layer, name) for name in _PACKAGE_FIELDS
            ) != package_identity or (
                profile_layer.layer_name,
                profile_layer.layer_position,
            ) != (layer.layer_name, layer.layer_position):
                raise InpnProtectedAreasEvidenceError(
                    f"{label}: {kind} package/layer identity or order differs"
                )
            if (
                profile_layer.feature_count != layer.feature_count
                or profile_layer.fid_count != layer.feature_count
            ):
                raise InpnProtectedAreasEvidenceError(
                    f"{label}: {kind} feature/FID counts differ from catalog"
                )
        if (attribute.fid_min, attribute.fid_max) != (
            geometry.fid_min,
            geometry.fid_max,
        ):
            raise InpnProtectedAreasEvidenceError(f"{label}: FID extrema differ")
        if attribute.fid_sequence_sha256 != geometry.fid_sequence_sha256:
            raise InpnProtectedAreasEvidenceError(
                f"{label}: canonical FID sequence SHA256 differs"
            )
        alignments.append(
            InpnProtectedAreasLayerAlignment(
                relative_path=package.relative_path,
                package_position=package.package_position,
                file_sha256=package.file_sha256,
                layer_name=layer.layer_name,
                layer_position=layer.layer_position,
                feature_count=layer.feature_count,
                fid_count=attribute.fid_count,
                fid_min=attribute.fid_min,
                fid_max=attribute.fid_max,
                fid_sequence_sha256=attribute.fid_sequence_sha256,
            )
        )
    return tuple(alignments)


def _bundle_payload(bundle: InpnProtectedAreasEvidenceBundle) -> dict[str, object]:
    """Bind upstream schema/hash commitments, not duplicated large value domains."""
    return {
        "evidence_bundle_schema_version": bundle.evidence_bundle_schema_version,
        "catalog": {
            "catalog_schema_version": bundle.catalog.catalog_schema_version,
            "complete_catalog_content_sha256": (
                bundle.catalog.complete_catalog_content_sha256
            ),
        },
        "attributes": {
            "attribute_profile_schema_version": (
                bundle.attributes.attribute_profile_schema_version
            ),
            "complete_attribute_profile_content_sha256": (
                bundle.attributes.complete_attribute_profile_content_sha256
            ),
        },
        "geometries": {
            "geometry_profile_schema_version": (
                bundle.geometries.geometry_profile_schema_version
            ),
            "complete_geometry_profile_content_sha256": (
                bundle.geometries.complete_geometry_profile_content_sha256
            ),
        },
        "layer_alignments": [asdict(item) for item in bundle.layer_alignments],
    }


def _bundle_content_sha256(bundle: InpnProtectedAreasEvidenceBundle) -> str:
    try:
        encoded = json.dumps(
            _bundle_payload(bundle),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (OverflowError, TypeError, ValueError, UnicodeError) as error:
        raise InpnProtectedAreasEvidenceError(
            "INPN evidence bundle payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _validate_bundle_intrinsic(
    bundle: object,
) -> InpnProtectedAreasEvidenceBundle:
    """Validate exact structure/alignment/hash closure, never physical source trust."""
    if type(bundle) is not InpnProtectedAreasEvidenceBundle:
        raise InpnProtectedAreasEvidenceError(
            "bundle must be an exact InpnProtectedAreasEvidenceBundle"
        )
    if (
        type(bundle.evidence_bundle_schema_version) is not int
        or bundle.evidence_bundle_schema_version != EVIDENCE_BUNDLE_SCHEMA_VERSION
    ):
        raise InpnProtectedAreasEvidenceError("invalid evidence bundle schema version")
    expected = _align_layers(bundle.catalog, bundle.attributes, bundle.geometries)
    if type(bundle.layer_alignments) is not tuple or len(
        bundle.layer_alignments
    ) != len(expected):
        raise InpnProtectedAreasEvidenceError("exact complete alignment tuple required")
    for actual, aligned in zip(bundle.layer_alignments, expected, strict=True):
        _require_exact_type(actual, InpnProtectedAreasLayerAlignment, "alignment")
        for field in fields(InpnProtectedAreasLayerAlignment):
            if type(getattr(actual, field.name)) is not type(
                getattr(aligned, field.name)
            ):
                raise InpnProtectedAreasEvidenceError(
                    f"package {aligned.relative_path} layer {aligned.layer_name}: "
                    f"alignment {field.name} has a noncanonical runtime type"
                )
        if actual != aligned:
            raise InpnProtectedAreasEvidenceError(
                f"package {aligned.relative_path} layer {aligned.layer_name}: "
                "alignment differs from retained profiles"
            )
    digest = bundle.complete_evidence_bundle_content_sha256
    if type(digest) is not str or _SHA_PATTERN.fullmatch(digest) is None:
        raise InpnProtectedAreasEvidenceError(
            "canonical evidence bundle SHA256 required"
        )
    if digest != _bundle_content_sha256(bundle):
        raise InpnProtectedAreasEvidenceError("complete evidence bundle SHA256 differs")
    return bundle


def build_inpn_protected_areas_evidence_bundle(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
    attributes: InpnProtectedAreasAttributeProfile,
    geometries: InpnProtectedAreasGeometryProfile,
) -> InpnProtectedAreasEvidenceBundle:
    """Physically validate both profiles once, align them, and recheck extraction."""
    try:
        _require_exact_type(extraction, InpnProtectedAreasExtraction, "extraction")
        validated_config = _validated_config(config)
        _require_exact_type(catalog, InpnProtectedAreasCatalog, "catalog")
        _require_exact_type(
            attributes, InpnProtectedAreasAttributeProfile, "attributes"
        )
        _require_exact_type(geometries, InpnProtectedAreasGeometryProfile, "geometries")
        validate_inpn_protected_areas_attribute_profile(
            extraction, validated_config, catalog, attributes
        )
        validate_inpn_protected_areas_geometry_profile(
            extraction, validated_config, catalog, geometries
        )
        alignments = _align_layers(catalog, attributes, geometries)
        bundle = InpnProtectedAreasEvidenceBundle(
            evidence_bundle_schema_version=EVIDENCE_BUNDLE_SCHEMA_VERSION,
            catalog=catalog,
            attributes=attributes,
            geometries=geometries,
            layer_alignments=alignments,
            complete_evidence_bundle_content_sha256="",
        )
        bundle = replace(
            bundle,
            complete_evidence_bundle_content_sha256=_bundle_content_sha256(bundle),
        )
        final_extraction = validate_inpn_protected_areas_extraction(
            extraction, validated_config
        )
        if final_extraction != extraction:
            raise InpnProtectedAreasEvidenceError(
                "INPN extraction changed during evidence assembly"
            )
        return bundle
    except InpnProtectedAreasEvidenceError:
        raise
    except _UPSTREAM_ERRORS as error:
        raise InpnProtectedAreasEvidenceError(
            f"INPN evidence failed physical source/profile validation: {error}"
        ) from error
    except Exception as error:
        raise InpnProtectedAreasEvidenceError(
            "INPN evidence bundle cannot be assembled safely"
        ) from error


def validate_inpn_protected_areas_evidence_bundle(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    bundle: InpnProtectedAreasEvidenceBundle,
) -> None:
    """Check intrinsic closure, independently revalidate physical profiles, and compare."""
    try:
        _require_exact_type(extraction, InpnProtectedAreasExtraction, "extraction")
        validated_config = _validated_config(config)
        supplied = _validate_bundle_intrinsic(bundle)
        rebuilt = build_inpn_protected_areas_evidence_bundle(
            extraction,
            validated_config,
            supplied.catalog,
            supplied.attributes,
            supplied.geometries,
        )
        if supplied != rebuilt:
            raise InpnProtectedAreasEvidenceError(
                "bundle differs from independently rebuilt aligned source evidence"
            )
    except InpnProtectedAreasEvidenceError:
        raise
    except _UPSTREAM_ERRORS as error:
        raise InpnProtectedAreasEvidenceError(
            f"INPN evidence profile validation failed: {error}"
        ) from error
    except Exception as error:
        raise InpnProtectedAreasEvidenceError(
            "INPN evidence bundle validation failed safely"
        ) from error


__all__ = [
    "InpnProtectedAreasEvidenceBundle",
    "InpnProtectedAreasEvidenceError",
    "InpnProtectedAreasLayerAlignment",
    "build_inpn_protected_areas_evidence_bundle",
    "validate_inpn_protected_areas_evidence_bundle",
]
```
