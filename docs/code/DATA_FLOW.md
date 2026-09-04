# LandScout data flow

This document shows the implemented high-level object flow. Exact parameters, frame columns, hashes, and guards are in the source-file companions.

## Cadastre

```text
commune code + cache root
  -> download_cadastre_parcelles
  -> CadastreDownload
  -> load_cadastre_parcels
  -> CadastreParcelSource(download, parcels)
  -> normalize_cadastre_parcels
  -> normalized parcel GeoDataFrame
  -> filter_parcels_by_area
  -> enrich_parcel_shapes
  -> filter_parcels_by_shape / profile_shape_distribution
```

`download_cadastre_parcelles` constructs the exact official commune archive URL, safely streams gzip bytes, and publishes a strict byte/hash/timestamp sidecar transactionally. `load_cadastre_parcels` returns a source-bound object that retains both the verified download and parsed parcels. Normalization validates the official download identity, rereads the physical gzip, exact-compares the supplied frame with that fresh read, and normalizes the fresh frame. It preserves WGS84 geometry, classifies `geometry_status`, and uses EPSG:2154 only to calculate `area_m2`. Area and shape filters validate the canonical parcel contract and create explicit screening results rather than a ranking.

## Grid

```text
IgnBdTopoSourceConfig
  -> download_ign_bdtopo_archive
  -> IgnBdTopoDownload
  -> extract_ign_bdtopo_archive
  -> IgnBdTopoExtraction
  -> load_ign_bdtopo_electricity
  -> IgnBdTopoElectricityData
  -> normalize_ign_electricity(source, config)
  -> NormalizedIgnElectricityData
  -> enrich_parcel_grid_proximity(parcels, source, config)
  -> GridProximityResult
  -> assess_grid_coverage(parcels, source, config)
  -> GridCoverageAssessmentResult
```

The public proximity function normalizes the verified source exactly once; callers cannot nominate arbitrary normalized line/post frames. IGN revalidation reproduces globally distinct roles from immutable config, reloads the physical layers, and the normalizer derives its output only from the fresh result. The result contains an unchanged parcel copy plus nearest line/post and exact-voltage evidence. Coverage assessment owns one proximity call and one freshly configured department-coverage load from the same extraction, then adds boundary diagnostics. Profiles summarize existing rows without changing them.

## Road

```text
IgnBdTopoExtraction + IgnBdTopoSourceConfig
  -> load_ign_bdtopo_roads
  -> IgnBdTopoRoadData
  -> normalize_ign_roads(source, config)
  -> NormalizedIgnRoadData
  -> load_ign_road_vehicle_proxy_policy
  -> IgnRoadVehicleProxyPolicy
  -> apply_ign_road_vehicle_proxy_policy
  -> IgnRoadVehicleProxyApplicationResult
  -> enrich_parcel_road_proximity
  -> ParcelRoadProximityResult
  -> assess_road_proximity_coverage
  -> RoadProximityCoverageAssessmentResult
```

Normalization revalidates configured role and download/extraction lineage, uses the freshly reread road object, and copies raw IGN access/restriction attributes without semantic coercion. Policy application reloads checked-in bytes, classifies each row under exact precedence, and preserves every normalized fact. Proximity builds a separate STRtree for each distance-eligible policy class, retains deterministic ties, and never indexes `NOT_DISTANCE_PROXY`. Coverage diagnosis compares those distances with a freshly loaded configured department boundary and the full parcel-to-boundary margin.

## Planning — spatial facts

```text
GpuSourceConfig
  -> discover_current_gpu_document
  -> GpuDocumentMetadata
  -> download_gpu_document
  -> GpuArchiveDownload
  -> extract_gpu_document
  -> GpuExtraction
  -> discover/inspect/ingest_gpu_planning_document
  -> GpuPlanningDocument(source_config, source_config_sha256, ...)
```

From `GpuPlanningDocument`, zoning and feature flows remain separate:

```text
parcels + planning document
  -> intersect_parcels_with_gpu_zoning
  -> ParcelZoningResult

parcels + planning document
  -> intersect_parcels_with_gpu_planning_features
  -> ParcelPlanningFeaturesResult
```

The planning document retains a canonical hash of the exact immutable GPU config. Every later physical revalidator verifies that identity, extraction inventory, and globally unique logical-role selection. Both stages source-completely validate normalized inputs by rebuilding from physical GPU layers. Zoning requires and reconstructs every column in the exact `PARCEL_ZONING_OUTPUT_COLUMNS` summary contract. Feature enrichment produces canonical surface/line/point catalogs and factual relation types/metrics.

## Planning — written regulation

```text
GpuPlanningDocument
  -> index_planning_regulation
  -> PlanningRegulationIndex
  -> structure_planning_regulation
  -> PlanningRegulationStructureResult
  -> interpret_bess_zoning
  -> BessZoningPrecheckResult
```

The index binds the selected written PDF bytes and page/text records. Structure configuration maps only deterministic headings, source spans, sections, zone aliases, and topic evidence; an `ERROR` on an applicable body page fails closed while a blank successfully extracted page remains valid. For every configured zone chapter, policy validation requires exactly one child article for every configured required article number and requires the same chapter-scoped sections in `reviewed_section_ids`. The written-zoning policy links exact source excerpts into routes and parcel prechecks. Raw source text, structured evidence, policy interpretation, and parcel result are different frames/envelopes.

## Planning — official CNIG feature meaning

```text
ParcelPlanningFeaturesResult + CNIG profile
  -> resolve_planning_feature_codes
  -> PlanningFeatureCodeResult
  + checked-in BESS CNIG policy
  -> compile_bess_planning_feature_policy
  -> BessPlanningFeaturePolicyResult
  -> apply_bess_planning_feature_policy
  -> BessPlanningFeatureApplicationResult
  -> aggregate_bess_planning_feature_policy_to_parcels
  -> BessPlanningFeatureParcelAggregationResult
```

The coded result preserves factual prefixes and appends official CNIG meaning/status. The policy result is compiled from official meaning pairs, not feature text. Application loaders require exact upstream coded and policy results and rebuild expected frames. Aggregation binds source parcel geometry and the exact application result; it does not combine planning with grid, road, or environment.

## Environment

```text
InpnProtectedAreasSourceConfig
  -> download_inpn_protected_areas_archive
  -> InpnProtectedAreasDownload
  -> immutable verified archive bytes
  -> archive-derived regular-member inventory
  -> extract_inpn_protected_areas_archive
  -> marker + physical + caller inventory equality
  -> archive path postcondition against initial immutable snapshot
  -> archive-bound InpnProtectedAreasExtraction
  -> validate_inpn_protected_areas_extraction
  -> immutable verified package bytes
  -> exact GPKG driver evidence
  -> build_inpn_protected_areas_catalog
  -> schema-2 InpnProtectedAreasCatalog(package/layer/field metadata)
  -> validate_inpn_protected_areas_catalog
  -> build_inpn_protected_areas_attribute_profile
  -> schema-1 InpnProtectedAreasAttributeProfile(complete non-geometry domains)
  -> validate_inpn_protected_areas_attribute_profile
  -> category semantics NOT IMPLEMENTED
  -> geometry loading NOT IMPLEMENTED
  -> parcel relation NOT IMPLEMENTED
  -> environmental policy NOT IMPLEMENTED
  -> score NOT IMPLEMENTED
```

The flow currently stops at a portable, source-bound schema-1 attribute profile. Archive member validation, archive-derived inventory, and extraction streaming share one verified archive snapshot; archive/marker/physical/caller inventories must match, and every successful source return rechecks the live archive path against the initial snapshot. Extraction, catalog, and profile intrinsic validation use the same authoritative Windows-compatible relative-package-path grammar. Accepted portable `relative_path: str` values are preserved exactly; whitespace is rejected rather than trimmed, no profile retains an absolute filesystem `Path`, and catalog/profile boundaries translate lower-layer path failures with chained causes. Each package is read once per catalog/profile build and all OGR calls use exact verified bytes; exact `GPKG` driver identity is hash-bound. Attribute reads request no geometry and preserve every integer FID, exact scalar value/frequency, null, source/runtime dtype, field order, and content hash. Only the expected byte-backed `/vsimem` extension warning is locally suppressed. Intrinsic profile validation proves canonical package grouping, contiguous layer/field structure, collision-free identities, inclusive FID-range capacity, component-SHA syntax, recomputable empty hashes, aggregates, and complete-hash closure; non-empty component hashes remain physical evidence. The public validator exact-compares all catalog-bound profile facts with a fresh catalog before attribute reads, then rebuilds and exact-compares every profile value. Catalog/profile canonical payloads and schema versions remain unchanged. No EP geometry is materialized, and there is no category semantics, parcel overlay, exclusion, or score. EP is not the separately published Natura 2000 archive and is not the separately published ZNIEFF archive.

## Result preservation pattern

Spatial stages generally create calculation-only copies for reprojection/force-2D/metrics, then return stored geometry under the documented source CRS. Result validators compare row order, index, dtype, active geometry, CRS, WKB, scalar lineage, and hashes in proportion to their contract. High-level artifact loaders verify physical bytes first and then compare deterministic source-bound rebuilds.
