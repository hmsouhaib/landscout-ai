# `src/landscout/stages/__init__.py`

## File identity

- Repository path: `src/landscout/stages/__init__.py`
- File type: Python source
- Primary responsibility: Defines the import/export surface for `src/landscout/stages`.
- Layer / domain: `stage` / `project`
- Public or internal role: Public package export surface.
- Source SHA256: `486c673828a9bdc77ca594316d86e3ab8b026cda42dec33326dc8f6dc12f28d5`

## 1. Purpose

Defines the import/export surface for `src/landscout/stages`.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `project` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- None.

### Third-party

- None.

### Internal LandScout

- `from landscout.stages.aggregate_bess_planning_feature_policy import ( BessPlanningFeatureParcelAggregationArtifactManifest, BessPlanningFeatureParcelAggregationError, BessPlanningFeatureParcelAggregationResult, aggregate_bess_planning_feature_policy_to_parcels, load_bess_planning_feature_parcel_agg…` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_bess_planning_feature_policy import ( BessPlanningFeatureApplicationArtifactManifest, BessPlanningFeatureApplicationError, BessPlanningFeatureApplicationResult, apply_bess_planning_feature_policy, load_bess_planning_feature_application_artifacts, validate_bess_planning_f…` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_road_vehicle_proxy_policy import ( IgnRoadVehicleProxyApplicationError, IgnRoadVehicleProxyApplicationResult, apply_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.assess_grid_coverage import ( BoundaryDistanceProfile, CoverageStatusCounts, GridCoverageAssessmentError, GridCoverageAssessmentResult, GridCoverageProfile, VoltageCoverageStatusProfile, assess_grid_coverage, profile_grid_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.assess_road_proximity_coverage import ( RoadProximityCoverageAssessmentResult, RoadProximityCoverageError, assess_road_proximity_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.bess_planning_feature_policy import ( BessPlanningFeaturePolicyArtifactManifest, BessPlanningFeaturePolicyConfig, BessPlanningFeaturePolicyError, BessPlanningFeaturePolicyResult, compile_bess_planning_feature_policy, load_bess_planning_feature_policy_artifacts, load_bess_plann…` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_grid_proximity import ( DistanceProfile, GridProximityError, GridProximityProfile, GridProximityResult, VoltageLevelCoverage, VoltageLevelDistanceProfile, enrich_parcel_grid_proximity, profile_grid_proximity, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_planning_features import ( ParcelPlanningFeaturesResult, PlanningFeatureInputValidation, PlanningFeaturesError, intersect_parcels_with_gpu_planning_features, validate_normalized_planning_feature_inputs, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_planning_zoning import ( intersect_parcels_with_gpu_zoning, validate_normalized_planning_zoning_inputs, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_road_proximity import ( ParcelRoadProximityResult, RoadProximityError, RoadProxyClassCoverage, enrich_parcel_road_proximity, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_shape import ShapeEnrichmentError, enrich_parcel_shapes` — required by the implementation paths and symbols documented below.
- `from landscout.stages.filter_parcels import ( ParcelFilterError, filter_parcels_by_area, filter_parcels_by_shape, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.index_planning_regulation import ( PlanningRegulationIndex, PlanningRegulationIndexError, PlanningRegulationSearchResult, index_planning_regulation, search_planning_regulation, validate_planning_regulation_index, validate_planning_regulation_search_result, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.interpret_bess_zoning import ( BessZoningPolicyConfig, BessZoningPrecheckError, BessZoningPrecheckResult, interpret_bess_zoning, load_bess_zoning_policy_config, validate_bess_zoning_precheck, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_access_ign import ( IgnRoadNormalizationError, NormalizedIgnRoadData, normalize_ign_roads, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_cadastre import ( CadastreNormalizationError, normalize_cadastre_parcels, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import ( IgnGridNormalizationError, IgnVoltageNormalization, NormalizedIgnElectricityData, normalize_ign_electricity, parse_ign_voltage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.profile_shape import ( ShapeDistributionProfile, ShapeProfileError, profile_shape_distribution, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( CnigFeatureCodeProfile, PlanningFeatureCodeError, PlanningFeatureCodeResult, load_cnig_feature_code_profile, resolve_planning_feature_codes, validate_planning_feature_code_result, validate_planning_feature_code_result_envelope, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( IgnRoadVehicleProxyPolicy, IgnRoadVehicleProxyPolicyError, load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.structure_planning_regulation import ( PlanningRegulationStructureConfig, PlanningRegulationStructureError, PlanningRegulationStructureResult, load_planning_regulation_structure_config, planning_regulation_section_page_fragments, structure_planning_regulation, validate_plannin…` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

No function or method is declared in this file.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `project` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- This project file does not implement a business algorithm.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
