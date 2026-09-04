# `src/landscout/sources/__init__.py`

## File identity

- Repository path: `src/landscout/sources/__init__.py`
- File type: Python package exports
- Layer/domain: official source adapters and source-bound factual authorities
- Responsibility: Re-exports approved source APIs while keeping raw-path, byte-reader, frame, and intrinsic-validation helpers internal.
- Source SHA256: `b323e00e7aff36e8580dba05b8907dc9b5d7d8f1635e223b54d97d4ef170fbcf`

## 1. STEP 7F.1B.2 contract delta

The package now publishes the four immutable INPN EP attribute-profile records, the controlled profile error, the source-complete builder, and the independent validator. It does not export `_read_verified_package_bytes`, `_suppress_pyogrio_bytes_gpkg_warning`, scalar canonicalizers, frame readers, payload/hash helpers, or an environmental semantic API.

## 2. Imports and ownership

There are no standard-library or third-party imports and no executable behavior beyond imports and the `__all__` assignment. Every binding is qualified in the exact source snapshot. The INPN ownership chain is intentionally split among `inpn_protected_areas_fr` (download/extraction), `inpn_protected_areas_catalog_fr` (physical metadata), and `inpn_protected_areas_attributes_fr` (attribute-only values); Cadastre, GPU, IGN, and RTE exports remain unchanged.

## 3. Exact public exports

| Export | Qualified origin |
|---|---|
| `CadastreDownload` | `landscout.sources.cadastre_fr.CadastreDownload` |
| `CadastreDownloadError` | `landscout.sources.cadastre_fr.CadastreDownloadError` |
| `CadastreLoadError` | `landscout.sources.cadastre_loader_fr.CadastreLoadError` |
| `CadastreParcelSource` | `landscout.sources.cadastre_loader_fr.CadastreParcelSource` |
| `EmptyCadastreDatasetError` | `landscout.sources.cadastre_loader_fr.EmptyCadastreDatasetError` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `GpuConfigError` | `landscout.sources.gpu_fr.GpuConfigError` |
| `GpuDiscoveryError` | `landscout.sources.gpu_fr.GpuDiscoveryError` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |
| `GpuError` | `landscout.sources.gpu_fr.GpuError` |
| `GpuExtractedFile` | `landscout.sources.gpu_fr.GpuExtractedFile` |
| `GpuExtraction` | `landscout.sources.gpu_fr.GpuExtraction` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |
| `GpuLayerSummary` | `landscout.sources.gpu_fr.GpuLayerSummary` |
| `GpuPlanningDocument` | `landscout.sources.gpu_fr.GpuPlanningDocument` |
| `GpuSourceConfig` | `landscout.sources.gpu_fr.GpuSourceConfig` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `GpuSpatialSourceFileIntegrity` | `landscout.sources.gpu_fr.GpuSpatialSourceFileIntegrity` |
| `GpuValidatedSpatialLayerSource` | `landscout.sources.gpu_fr.GpuValidatedSpatialLayerSource` |
| `GpuWrittenFile` | `landscout.sources.gpu_fr.GpuWrittenFile` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `IgnBdTopoArchiveIntegrity` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveIntegrity` |
| `IgnBdTopoCoverageConfig` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoCoverageConfig` |
| `IgnBdTopoCoverageLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoCoverageLayerSummary` |
| `IgnBdTopoDepartmentCoverage` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDepartmentCoverage` |
| `IgnBdTopoDepartmentLayerConfig` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDepartmentLayerConfig` |
| `IgnBdTopoDownload` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownload` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |
| `IgnBdTopoElectricityData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoElectricityData` |
| `IgnBdTopoError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoError` |
| `IgnBdTopoExtraction` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoExtraction` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `IgnBdTopoLayerSelection` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSelection` |
| `IgnBdTopoLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSummary` |
| `IgnBdTopoLoadedLayer` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLoadedLayer` |
| `IgnBdTopoLogicalLayerConfig` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLogicalLayerConfig` |
| `IgnBdTopoLogicalLayersConfig` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLogicalLayersConfig` |
| `IgnBdTopoRoadData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` |
| `IgnBdTopoSourceConfig` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig` |
| `InpnProtectedAreasAttributeProfile` | `landscout.sources.inpn_protected_areas_attributes_fr.InpnProtectedAreasAttributeProfile` |
| `InpnProtectedAreasAttributeProfileError` | `landscout.sources.inpn_protected_areas_attributes_fr.InpnProtectedAreasAttributeProfileError` |
| `InpnProtectedAreasCatalog` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasCatalog` |
| `InpnProtectedAreasCatalogError` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasCatalogError` |
| `InpnProtectedAreasDistinctAttributeValue` | `landscout.sources.inpn_protected_areas_attributes_fr.InpnProtectedAreasDistinctAttributeValue` |
| `InpnProtectedAreasDownload` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasDownload` |
| `InpnProtectedAreasExtractedFile` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtractedFile` |
| `InpnProtectedAreasExtraction` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtraction` |
| `InpnProtectedAreasFieldAttributeProfile` | `landscout.sources.inpn_protected_areas_attributes_fr.InpnProtectedAreasFieldAttributeProfile` |
| `InpnProtectedAreasFieldCatalog` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasFieldCatalog` |
| `InpnProtectedAreasGeoPackageCatalog` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasGeoPackageCatalog` |
| `InpnProtectedAreasLayerAttributeProfile` | `landscout.sources.inpn_protected_areas_attributes_fr.InpnProtectedAreasLayerAttributeProfile` |
| `InpnProtectedAreasLayerCatalog` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasLayerCatalog` |
| `InpnProtectedAreasSourceConfig` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `MissingGeometryColumnError` | `landscout.sources.cadastre_loader_fr.MissingGeometryColumnError` |
| `RteDatasetConfig` | `landscout.sources.rte_odre_fr.RteDatasetConfig` |
| `RteOdreDatasetMetadata` | `landscout.sources.rte_odre_fr.RteOdreDatasetMetadata` |
| `RteOdreDownload` | `landscout.sources.rte_odre_fr.RteOdreDownload` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
| `RteOdreExportSummary` | `landscout.sources.rte_odre_fr.RteOdreExportSummary` |
| `RteOdreSourceConfig` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig` |
| `UnsupportedGeometryTypeError` | `landscout.sources.cadastre_loader_fr.UnsupportedGeometryTypeError` |
| `build_cadastre_parcelles_url` | `landscout.sources.cadastre_fr.build_cadastre_parcelles_url` |
| `build_gpu_document_list_url` | `landscout.sources.gpu_fr.build_gpu_document_list_url` |
| `build_gpu_partition` | `landscout.sources.gpu_fr.build_gpu_partition` |
| `build_gpu_partition_download_url` | `landscout.sources.gpu_fr.build_gpu_partition_download_url` |
| `build_inpn_protected_areas_attribute_profile` | `landscout.sources.inpn_protected_areas_attributes_fr.build_inpn_protected_areas_attribute_profile` |
| `build_inpn_protected_areas_catalog` | `landscout.sources.inpn_protected_areas_catalog_fr.build_inpn_protected_areas_catalog` |
| `build_rte_odre_export_url` | `landscout.sources.rte_odre_fr.build_rte_odre_export_url` |
| `build_rte_odre_metadata_url` | `landscout.sources.rte_odre_fr.build_rte_odre_metadata_url` |
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `discover_gpu_spatial_layers` | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` |
| `discover_ign_bdtopo_geopackage` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_geopackage` |
| `discover_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_layers` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `download_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.download_ign_bdtopo_archive` |
| `download_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.download_inpn_protected_areas_archive` |
| `download_rte_odre_dataset` | `landscout.sources.rte_odre_fr.download_rte_odre_dataset` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `extract_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.extract_ign_bdtopo_archive` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `fetch_rte_odre_dataset_metadata` | `landscout.sources.rte_odre_fr.fetch_rte_odre_dataset_metadata` |
| `ingest_gpu_planning_document` | `landscout.sources.gpu_fr.ingest_gpu_planning_document` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |
| `list_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.list_ign_bdtopo_layers` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `load_ign_bdtopo_electricity` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_electricity` |
| `load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `load_ign_bdtopo_source_config` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config` |
| `load_inpn_protected_areas_source_config` | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` |
| `load_rte_odre_source_config` | `landscout.sources.rte_odre_fr.load_rte_odre_source_config` |
| `revalidate_cadastre_parcel_source` | `landscout.sources.cadastre_loader_fr.revalidate_cadastre_parcel_source` |
| `revalidate_gpu_spatial_layer_source` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_source` |
| `revalidate_gpu_spatial_layer_sources` | `landscout.sources.gpu_fr.revalidate_gpu_spatial_layer_sources` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |
| `validate_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.validate_ign_bdtopo_archive` |
| `validate_inpn_protected_areas_attribute_profile` | `landscout.sources.inpn_protected_areas_attributes_fr.validate_inpn_protected_areas_attribute_profile` |
| `validate_inpn_protected_areas_catalog` | `landscout.sources.inpn_protected_areas_catalog_fr.validate_inpn_protected_areas_catalog` |
| `validate_inpn_protected_areas_extraction` | `landscout.sources.inpn_protected_areas_fr.validate_inpn_protected_areas_extraction` |

## 4. Validation, side effects, and boundary

This module performs no validation, network, filesystem, hashing, CRS, geometry, or mutation work itself; those contracts belong to each qualified implementation. Re-exporting the attribute profile does not interpret EP categories/legal regimes, map Natura 2000/ZNIEFF, load geometry/parcels, intersect, exclude, score, or rank.

Any import/export change requires package-ownership tests, companion SHA/snapshot synchronization, source/catalog/attribute focused suites, and the full repository gates.

## 5. Exact complete current file content

```python
from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)
from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)
from landscout.sources.gpu_fr import (
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
)
from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)
from landscout.sources.inpn_protected_areas_attributes_fr import (
    InpnProtectedAreasAttributeProfile,
    InpnProtectedAreasAttributeProfileError,
    InpnProtectedAreasDistinctAttributeValue,
    InpnProtectedAreasFieldAttributeProfile,
    InpnProtectedAreasLayerAttributeProfile,
    build_inpn_protected_areas_attribute_profile,
    validate_inpn_protected_areas_attribute_profile,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasFieldCatalog,
    InpnProtectedAreasGeoPackageCatalog,
    InpnProtectedAreasLayerCatalog,
    build_inpn_protected_areas_catalog,
    validate_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
    validate_inpn_protected_areas_extraction,
)
from landscout.sources.rte_odre_fr import (
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
)

__all__ = [
    "CadastreDownload",
    "CadastreDownloadError",
    "CadastreLoadError",
    "CadastreParcelSource",
    "EmptyCadastreDatasetError",
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
    "InpnProtectedAreasAttributeProfile",
    "InpnProtectedAreasAttributeProfileError",
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasDistinctAttributeValue",
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasFieldAttributeProfile",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
    "InpnProtectedAreasLayerAttributeProfile",
    "InpnProtectedAreasLayerCatalog",
    "InpnProtectedAreasSourceConfig",
    "InpnProtectedAreasSourceError",
    "MissingGeometryColumnError",
    "RteDatasetConfig",
    "RteOdreDatasetMetadata",
    "RteOdreDownload",
    "RteOdreDownloadError",
    "RteOdreExportSummary",
    "RteOdreSourceConfig",
    "UnsupportedGeometryTypeError",
    "build_cadastre_parcelles_url",
    "build_gpu_document_list_url",
    "build_gpu_partition",
    "build_gpu_partition_download_url",
    "build_inpn_protected_areas_attribute_profile",
    "build_inpn_protected_areas_catalog",
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
    "load_cadastre_parcels",
    "load_gpu_source_config",
    "load_ign_bdtopo_department_coverage",
    "load_ign_bdtopo_electricity",
    "load_ign_bdtopo_roads",
    "load_ign_bdtopo_source_config",
    "load_inpn_protected_areas_source_config",
    "load_rte_odre_source_config",
    "revalidate_cadastre_parcel_source",
    "revalidate_gpu_spatial_layer_source",
    "revalidate_gpu_spatial_layer_sources",
    "validate_gpu_archive",
    "validate_ign_bdtopo_archive",
    "validate_inpn_protected_areas_attribute_profile",
    "validate_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_extraction",
]
```
