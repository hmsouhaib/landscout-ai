# `src/landscout/sources/__init__.py`

## File identity

- Repository path: `src/landscout/sources/__init__.py`
- File type: Python source
- Layer: source adapter
- Domain: project
- Responsibility: Re-exports the supported external-source adapter API.
- Source SHA256: `b263dbbbf4fc65bd4c4c92fb525885d4efbc484ff7c71b335e77740d882b29f7`

## 1. Purpose

Re-exports the supported external-source adapter API.

## 2. Position in LandScout architecture

This file belongs to the **source adapter** layer and the **project** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `None.`

### Internal LandScout imports

- `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "CadastreDownload",
    "CadastreDownloadError",
    "GpuArchiveDownload",
    "GpuArchiveError",
    "GpuConfigError",
    "GpuDiscoveryError",
    "GpuDocumentMetadata",
    "GpuDownloadError",
    "GpuError",
    "GpuExtractedFile",
    "GpuExtraction",
    "GpuInspectedLayer",
    "GpuLayerSummary",
    "GpuPlanningDocument",
    "GpuSourceConfig",
    "GpuSpatialInspectionError",
    "GpuSpatialLayerReference",
    "GpuSpatialSourceFileIntegrity",
    "GpuValidatedSpatialLayerSource",
    "GpuWrittenFile",
    "IgnBdTopoArchiveError",
    "IgnBdTopoArchiveIntegrity",
    "IgnBdTopoCoverageConfig",
    "IgnBdTopoCoverageLayerSummary",
    "IgnBdTopoDepartmentCoverage",
    "IgnBdTopoDepartmentLayerConfig",
    "IgnBdTopoDownload",
    "IgnBdTopoDownloadError",
    "IgnBdTopoElectricityData",
    "IgnBdTopoError",
    "IgnBdTopoExtraction",
    "IgnBdTopoLayerError",
    "IgnBdTopoLayerSelection",
    "IgnBdTopoLayerSummary",
    "IgnBdTopoLoadedLayer",
    "IgnBdTopoLogicalLayerConfig",
    "IgnBdTopoLogicalLayersConfig",
    "IgnBdTopoRoadData",
    "IgnBdTopoSourceConfig",
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasSourceConfig",
    "InpnProtectedAreasSourceError",
    "RteDatasetConfig",
    "RteOdreDatasetMetadata",
    "RteOdreDownload",
    "RteOdreDownloadError",
    "RteOdreExportSummary",
    "RteOdreSourceConfig",
    "build_cadastre_parcelles_url",
    "build_gpu_document_list_url",
    "build_gpu_partition",
    "build_gpu_partition_download_url",
    "build_rte_odre_export_url",
    "build_rte_odre_metadata_url",
    "discover_current_gpu_document",
    "discover_gpu_spatial_layers",
    "discover_ign_bdtopo_geopackage",
    "discover_ign_bdtopo_layers",
    "download_cadastre_parcelles",
    "download_gpu_document",
    "download_ign_bdtopo_archive",
    "download_inpn_protected_areas_archive",
    "download_rte_odre_dataset",
    "extract_gpu_document",
    "extract_ign_bdtopo_archive",
    "extract_inpn_protected_areas_archive",
    "fetch_rte_odre_dataset_metadata",
    "ingest_gpu_planning_document",
    "inspect_gpu_planning_document",
    "list_ign_bdtopo_layers",
    "load_gpu_source_config",
    "load_ign_bdtopo_department_coverage",
    "load_ign_bdtopo_electricity",
    "load_ign_bdtopo_layer",
    "load_ign_bdtopo_roads",
    "load_ign_bdtopo_source_config",
    "load_inpn_protected_areas_source_config",
    "load_rte_odre_source_config",
    "revalidate_gpu_spatial_layer_source",
    "revalidate_gpu_spatial_layer_sources",
    "validate_gpu_archive",
    "validate_ign_bdtopo_archive",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

No function or method is declared.

## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `CadastreDownload` | public re-export imported from its declaring module | `landscout.sources.cadastre_fr.CadastreDownload` | yes |
| `CadastreDownloadError` | public re-export imported from its declaring module | `landscout.sources.cadastre_fr.CadastreDownloadError` | yes |
| `GpuArchiveDownload` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuArchiveDownload` | yes |
| `GpuArchiveError` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuArchiveError` | yes |
| `GpuConfigError` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuConfigError` | yes |
| `GpuDiscoveryError` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuDiscoveryError` | yes |
| `GpuDocumentMetadata` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuDocumentMetadata` | yes |
| `GpuDownloadError` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuDownloadError` | yes |
| `GpuError` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuError` | yes |
| `GpuExtractedFile` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuExtractedFile` | yes |
| `GpuExtraction` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuExtraction` | yes |
| `GpuInspectedLayer` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuInspectedLayer` | yes |
| `GpuLayerSummary` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuLayerSummary` | yes |
| `GpuPlanningDocument` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuPlanningDocument` | yes |
| `GpuSourceConfig` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuSourceConfig` | yes |
| `GpuSpatialInspectionError` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuSpatialInspectionError` | yes |
| `GpuSpatialLayerReference` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuSpatialLayerReference` | yes |
| `GpuSpatialSourceFileIntegrity` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuSpatialSourceFileIntegrity` | yes |
| `GpuValidatedSpatialLayerSource` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuValidatedSpatialLayerSource` | yes |
| `GpuWrittenFile` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.GpuWrittenFile` | yes |
| `IgnBdTopoArchiveError` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` | yes |
| `IgnBdTopoArchiveIntegrity` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveIntegrity` | yes |
| `IgnBdTopoCoverageConfig` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoCoverageConfig` | yes |
| `IgnBdTopoCoverageLayerSummary` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoCoverageLayerSummary` | yes |
| `IgnBdTopoDepartmentCoverage` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDepartmentCoverage` | yes |
| `IgnBdTopoDepartmentLayerConfig` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDepartmentLayerConfig` | yes |
| `IgnBdTopoDownload` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownload` | yes |
| `IgnBdTopoDownloadError` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` | yes |
| `IgnBdTopoElectricityData` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoElectricityData` | yes |
| `IgnBdTopoError` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoError` | yes |
| `IgnBdTopoExtraction` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoExtraction` | yes |
| `IgnBdTopoLayerError` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` | yes |
| `IgnBdTopoLayerSelection` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSelection` | yes |
| `IgnBdTopoLayerSummary` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSummary` | yes |
| `IgnBdTopoLoadedLayer` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLoadedLayer` | yes |
| `IgnBdTopoLogicalLayerConfig` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLogicalLayerConfig` | yes |
| `IgnBdTopoLogicalLayersConfig` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLogicalLayersConfig` | yes |
| `IgnBdTopoRoadData` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` | yes |
| `IgnBdTopoSourceConfig` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig` | yes |
| `InpnProtectedAreasDownload` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasDownload` | yes |
| `InpnProtectedAreasExtractedFile` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtractedFile` | yes |
| `InpnProtectedAreasExtraction` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtraction` | yes |
| `InpnProtectedAreasSourceConfig` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig` | yes |
| `InpnProtectedAreasSourceError` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` | yes |
| `RteDatasetConfig` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.RteDatasetConfig` | yes |
| `RteOdreDatasetMetadata` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.RteOdreDatasetMetadata` | yes |
| `RteOdreDownload` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.RteOdreDownload` | yes |
| `RteOdreDownloadError` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.RteOdreDownloadError` | yes |
| `RteOdreExportSummary` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.RteOdreExportSummary` | yes |
| `RteOdreSourceConfig` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.RteOdreSourceConfig` | yes |
| `build_cadastre_parcelles_url` | public re-export imported from its declaring module | `landscout.sources.cadastre_fr.build_cadastre_parcelles_url` | yes |
| `build_gpu_document_list_url` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.build_gpu_document_list_url` | yes |
| `build_gpu_partition` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.build_gpu_partition` | yes |
| `build_gpu_partition_download_url` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.build_gpu_partition_download_url` | yes |
| `build_rte_odre_export_url` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.build_rte_odre_export_url` | yes |
| `build_rte_odre_metadata_url` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.build_rte_odre_metadata_url` | yes |
| `discover_current_gpu_document` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.discover_current_gpu_document` | yes |
| `discover_gpu_spatial_layers` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` | yes |
| `discover_ign_bdtopo_geopackage` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_geopackage` | yes |
| `discover_ign_bdtopo_layers` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_layers` | yes |
| `download_cadastre_parcelles` | public re-export imported from its declaring module | `landscout.sources.cadastre_fr.download_cadastre_parcelles` | yes |
| `download_gpu_document` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.download_gpu_document` | yes |
| `download_ign_bdtopo_archive` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` | yes |
| `download_inpn_protected_areas_archive` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.download_inpn_protected_areas_archive` | yes |
| `download_rte_odre_dataset` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` | yes |
| `extract_gpu_document` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.extract_gpu_document` | yes |
| `extract_ign_bdtopo_archive` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` | yes |
| `extract_inpn_protected_areas_archive` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` | yes |
| `fetch_rte_odre_dataset_metadata` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.fetch_rte_odre_dataset_metadata` | yes |
| `ingest_gpu_planning_document` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.ingest_gpu_planning_document` | yes |
| `inspect_gpu_planning_document` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.inspect_gpu_planning_document` | yes |
| `list_ign_bdtopo_layers` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.list_ign_bdtopo_layers` | yes |
| `load_gpu_source_config` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.load_gpu_source_config` | yes |
| `load_ign_bdtopo_department_coverage` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` | yes |
| `load_ign_bdtopo_electricity` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_electricity` | yes |
| `load_ign_bdtopo_layer` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_layer` | yes |
| `load_ign_bdtopo_roads` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` | yes |
| `load_ign_bdtopo_source_config` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config` | yes |
| `load_inpn_protected_areas_source_config` | public re-export imported from its declaring module | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` | yes |
| `load_rte_odre_source_config` | public re-export imported from its declaring module | `landscout.sources.rte_odre_fr.load_rte_odre_source_config` | yes |
| `revalidate_gpu_spatial_layer_source` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_source` | yes |
| `revalidate_gpu_spatial_layer_sources` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_sources` | yes |
| `validate_gpu_archive` | public re-export imported from its declaring module | `landscout.sources.gpu_fr.validate_gpu_archive` | yes |
| `validate_ign_bdtopo_archive` | public re-export imported from its declaring module | `landscout.sources.ign_bdtopo_fr.validate_ign_bdtopo_archive` | yes |

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the project flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
