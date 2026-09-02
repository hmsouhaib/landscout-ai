# `src/landscout/sources/__init__.py`

## File identity

- Repository path: `src/landscout/sources/__init__.py`
- File type: Python source
- Layer: source adapter
- Domain: official source acquisition and physical authority
- Responsibility: Re-exports approved source-bound adapter APIs, including Cadastre authority and INPN extraction/catalog trust boundaries, without presenting raw-path helpers as equivalent trust roots.
- Source SHA256: `113c9fcf94d926f244f795844e115a42398e2ffcb15b3ed380583831fd234987`

## 1. STEP 7F.1B.1 contract delta

- Publishes the source-complete INPN extraction validator and the immutable catalog models, controlled error, builder, and independent validator.
- Low-level path/metadata helpers remain internal; no environmental semantic API is exported.

## 2. Purpose and architectural position

Re-exports approved source-bound adapter APIs, including Cadastre authority and INPN extraction/catalog trust boundaries, without presenting raw-path helpers as equivalent trust roots.

The file belongs to the **source adapter** layer and **official source acquisition and physical authority** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- None.

### Third-party packages

- None.

### Internal LandScout imports

- `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
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
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- `from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    InpnProtectedAreasFieldCatalog,
    InpnProtectedAreasGeoPackageCatalog,
    InpnProtectedAreasLayerCatalog,
    build_inpn_protected_areas_catalog,
    validate_inpn_protected_areas_catalog,
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
    validate_inpn_protected_areas_extraction,
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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
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
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
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
    "validate_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_extraction",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `CadastreDownload`
  - `CadastreDownloadError`
  - `CadastreLoadError`
  - `CadastreParcelSource`
  - `EmptyCadastreDatasetError`
  - `GpuArchiveDownload`
  - `GpuArchiveError`
  - `GpuConfigError`
  - `GpuDiscoveryError`
  - `GpuDocumentMetadata`
  - `GpuDownloadError`
  - `GpuError`
  - `GpuExtractedFile`
  - `GpuExtraction`
  - `GpuInspectedLayer`
  - `GpuLayerSummary`
  - `GpuPlanningDocument`
  - `GpuSourceConfig`
  - `GpuSpatialInspectionError`
  - `GpuSpatialLayerReference`
  - `GpuSpatialSourceFileIntegrity`
  - `GpuValidatedSpatialLayerSource`
  - `GpuWrittenFile`
  - `IgnBdTopoArchiveError`
  - `IgnBdTopoArchiveIntegrity`
  - `IgnBdTopoCoverageConfig`
  - `IgnBdTopoCoverageLayerSummary`
  - `IgnBdTopoDepartmentCoverage`
  - `IgnBdTopoDepartmentLayerConfig`
  - `IgnBdTopoDownload`
  - `IgnBdTopoDownloadError`
  - `IgnBdTopoElectricityData`
  - `IgnBdTopoError`
  - `IgnBdTopoExtraction`
  - `IgnBdTopoLayerError`
  - `IgnBdTopoLayerSelection`
  - `IgnBdTopoLayerSummary`
  - `IgnBdTopoLoadedLayer`
  - `IgnBdTopoLogicalLayerConfig`
  - `IgnBdTopoLogicalLayersConfig`
  - `IgnBdTopoRoadData`
  - `IgnBdTopoSourceConfig`
  - `InpnProtectedAreasCatalog`
  - `InpnProtectedAreasCatalogError`
  - `InpnProtectedAreasDownload`
  - `InpnProtectedAreasExtractedFile`
  - `InpnProtectedAreasExtraction`
  - `InpnProtectedAreasFieldCatalog`
  - `InpnProtectedAreasGeoPackageCatalog`
  - `InpnProtectedAreasLayerCatalog`
  - `InpnProtectedAreasSourceConfig`
  - `InpnProtectedAreasSourceError`
  - `MissingGeometryColumnError`
  - `RteDatasetConfig`
  - `RteOdreDatasetMetadata`
  - `RteOdreDownload`
  - `RteOdreDownloadError`
  - `RteOdreExportSummary`
  - `RteOdreSourceConfig`
  - `UnsupportedGeometryTypeError`
  - `build_cadastre_parcelles_url`
  - `build_gpu_document_list_url`
  - `build_gpu_partition`
  - `build_gpu_partition_download_url`
  - `build_inpn_protected_areas_catalog`
  - `build_rte_odre_export_url`
  - `build_rte_odre_metadata_url`
  - `discover_current_gpu_document`
  - `discover_gpu_spatial_layers`
  - `discover_ign_bdtopo_geopackage`
  - `discover_ign_bdtopo_layers`
  - `download_cadastre_parcelles`
  - `download_gpu_document`
  - `download_ign_bdtopo_archive`
  - `download_inpn_protected_areas_archive`
  - `download_rte_odre_dataset`
  - `extract_gpu_document`
  - `extract_ign_bdtopo_archive`
  - `extract_inpn_protected_areas_archive`
  - `fetch_rte_odre_dataset_metadata`
  - `ingest_gpu_planning_document`
  - `inspect_gpu_planning_document`
  - `list_ign_bdtopo_layers`
  - `load_cadastre_parcels`
  - `load_gpu_source_config`
  - `load_ign_bdtopo_department_coverage`
  - `load_ign_bdtopo_electricity`
  - `load_ign_bdtopo_roads`
  - `load_ign_bdtopo_source_config`
  - `load_inpn_protected_areas_source_config`
  - `load_rte_odre_source_config`
  - `revalidate_cadastre_parcel_source`
  - `revalidate_gpu_spatial_layer_source`
  - `revalidate_gpu_spatial_layer_sources`
  - `validate_gpu_archive`
  - `validate_ign_bdtopo_archive`
  - `validate_inpn_protected_areas_catalog`
  - `validate_inpn_protected_areas_extraction`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

No function or method is declared.

## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
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
| `InpnProtectedAreasCatalog` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasCatalog` |
| `InpnProtectedAreasCatalogError` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasCatalogError` |
| `InpnProtectedAreasDownload` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasDownload` |
| `InpnProtectedAreasExtractedFile` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtractedFile` |
| `InpnProtectedAreasExtraction` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtraction` |
| `InpnProtectedAreasFieldCatalog` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasFieldCatalog` |
| `InpnProtectedAreasGeoPackageCatalog` | `landscout.sources.inpn_protected_areas_catalog_fr.InpnProtectedAreasGeoPackageCatalog` |
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
| `validate_inpn_protected_areas_catalog` | `landscout.sources.inpn_protected_areas_catalog_fr.validate_inpn_protected_areas_catalog` |
| `validate_inpn_protected_areas_extraction` | `landscout.sources.inpn_protected_areas_fr.validate_inpn_protected_areas_extraction` |

## 9. Trust, provenance, side effects, and business boundary

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

This byte-bound snapshot is the complete current repository file.

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
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
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
    "validate_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_extraction",
]
```
