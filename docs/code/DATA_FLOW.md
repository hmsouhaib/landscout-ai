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
  -> extract_inpn_protected_areas_archive
  -> InpnProtectedAreasExtraction(files inventory)
  -> validate_inpn_protected_areas_extraction
  -> build_inpn_protected_areas_catalog
  -> InpnProtectedAreasCatalog(package/layer/field metadata)
  -> validate_inpn_protected_areas_catalog
```

The flow currently stops at a portable, source-bound metadata catalog. The extraction validator rebuilds the complete current physical inventory; the builder uses metadata-only OGR calls between pre/post extraction validation; and the independent validator rebuilds and exact-compares every catalog value. No feature row or geometry is materialized, and there is no category semantics, Natura 2000/ZNIEFF interpretation, parcel overlay, exclusion, or score.

## Result preservation pattern

Spatial stages generally create calculation-only copies for reprojection/force-2D/metrics, then return stored geometry under the documented source CRS. Result validators compare row order, index, dtype, active geometry, CRS, WKB, scalar lineage, and hashes in proportion to their contract. High-level artifact loaders verify physical bytes first and then compare deterministic source-bound rebuilds.
