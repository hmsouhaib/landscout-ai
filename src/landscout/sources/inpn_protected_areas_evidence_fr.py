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
