# File index

Each tracked file outside `docs/code/**` has exactly one SHA-bound companion. The role column is curated from the actual implementation/file consumer, not inferred from the basename alone.

## Project/root metadata

| Repository file | Actual role | Companion |
|---|---|---|
| `.env.example` | Declares the example environment-variable surface for local LandScout configuration without storing secrets. | [files/.env.example.md](files/.env.example.md) |
| `.gitignore` | Defines repository paths and generated artifacts that Git must not track. | [files/.gitignore.md](files/.gitignore.md) |
| `.python-version` | Pins the uv/Python interpreter version used by the project. | [files/.python-version.md](files/.python-version.md) |
| `README.md` | Introduces LandScout's current evidence-first BESS scope and links to the detailed technical reference. | [files/README.md.md](files/README.md.md) |
| `data/cache/.gitkeep` | Keeps an otherwise generated/empty directory present in Git without adding runtime data. | [files/data/cache/.gitkeep.md](files/data/cache/.gitkeep.md) |
| `data/processed/.gitkeep` | Keeps an otherwise generated/empty directory present in Git without adding runtime data. | [files/data/processed/.gitkeep.md](files/data/processed/.gitkeep.md) |
| `data/raw/.gitkeep` | Keeps an otherwise generated/empty directory present in Git without adding runtime data. | [files/data/raw/.gitkeep.md](files/data/raw/.gitkeep.md) |
| `outputs/.gitkeep` | Keeps an otherwise generated/empty directory present in Git without adding runtime data. | [files/outputs/.gitkeep.md](files/outputs/.gitkeep.md) |
| `pyproject.toml` | Defines project/dependency/tool configuration and excludes `docs/code/files` from Ruff so byte-exact companion source snapshots are not reformatted. | [files/pyproject.toml.md](files/pyproject.toml.md) |
| `src/landscout/__init__.py` | Defines the package version exposed as `landscout.__version__`, which package tests bind exactly to `project.version`. | [files/src/landscout/__init__.py.md](files/src/landscout/__init__.py.md) |
| `src/landscout/config.py` | Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration. | [files/src/landscout/config.py.md](files/src/landscout/config.py.md) |
| `uv.lock` | Locks the resolved Python dependency graph used by uv; it is dependency evidence, not business logic. | [files/uv.lock.md](files/uv.lock.md) |

## Checked-in configuration

| Repository file | Actual role | Companion |
|---|---|---|
| `configs/access/ign_bdtopo_vehicle_proxy_policy.yaml` | Defines the approved versioned IGN general-car/light-vehicle evidence policy, source references, vocabularies, outcomes, and exact precedence. | [files/configs/access/ign_bdtopo_vehicle_proxy_policy.yaml.md](files/configs/access/ign_bdtopo_vehicle_proxy_policy.yaml.md) |
| `configs/planning/cnig_plu_2017_feature_codes.yaml` | Defines the approved CNIG PLU v2017 official planning-feature code pairs, labels, references, and profile identity. | [files/configs/planning/cnig_plu_2017_feature_codes.yaml.md](files/configs/planning/cnig_plu_2017_feature_codes.yaml.md) |
| `configs/planning/muret_bess_cnig_feature_policy.yaml` | Defines the Muret BESS precheck policy over official CNIG feature-code meaning only. | [files/configs/planning/muret_bess_cnig_feature_policy.yaml.md](files/configs/planning/muret_bess_cnig_feature_policy.yaml.md) |
| `configs/planning/muret_bess_zoning_policy.yaml` | Defines the source-locked Muret written-zoning evidence occurrences, routes, chapter decisions, and applicability notes. | [files/configs/planning/muret_bess_zoning_policy.yaml.md](files/configs/planning/muret_bess_zoning_policy.yaml.md) |
| `configs/planning/muret_plu_structure.yaml` | Defines deterministic Muret regulation layout, heading grammar, zone aliases, and topic-evidence terms. | [files/configs/planning/muret_plu_structure.yaml.md](files/configs/planning/muret_plu_structure.yaml.md) |
| `configs/profiles/bess_default_fr.yaml` | Defines the default French BESS parcel-area and shape-screening profile consumed by scan configuration. | [files/configs/profiles/bess_default_fr.yaml.md](files/configs/profiles/bess_default_fr.yaml.md) |
| `configs/scans/bess_muret.yaml` | Defines the Muret scan identity, AOI, profile reference, and output root. | [files/configs/scans/bess_muret.yaml.md](files/configs/scans/bess_muret.yaml.md) |
| `configs/sources/gpu_fr.yaml` | Pins the official GPU API/cache/pilot identity and logical spatial-layer discovery rules. | [files/configs/sources/gpu_fr.yaml.md](files/configs/sources/gpu_fr.yaml.md) |
| `configs/sources/ign_bdtopo_fr.yaml` | Pins the IGN BD TOPO D031 archive identity, checksum/size, cache, logical layers, access, and coverage selection. | [files/configs/sources/ign_bdtopo_fr.yaml.md](files/configs/sources/ign_bdtopo_fr.yaml.md) |
| `configs/sources/inpn_protected_areas_fr.yaml` | Pins the PatriNat/MNHN/INPN EP 07/2026 archive identity, size, SHA256, URLs, and cache root. | [files/configs/sources/inpn_protected_areas_fr.yaml.md](files/configs/sources/inpn_protected_areas_fr.yaml.md) |
| `configs/sources/rte_odre_fr.yaml` | Pins the official ODRÉ API/cache identity and exact RTE dataset IDs/formats. | [files/configs/sources/rte_odre_fr.yaml.md](files/configs/sources/rte_odre_fr.yaml.md) |

## Internal common contracts

| Repository file | Actual role | Companion |
|---|---|---|
| `src/landscout/common/__init__.py` | Marks the internal common-contract package; it declares no package export list. | [files/src/landscout/common/__init__.py.md](files/src/landscout/common/__init__.py.md) |
| `src/landscout/common/artifact_paths.py` | Validates portable local Parquet artifact basenames across POSIX and Windows rules. | [files/src/landscout/common/artifact_paths.py.md](files/src/landscout/common/artifact_paths.py.md) |
| `src/landscout/common/bess_application_contract.py` | Enforces intrinsic BESS planning feature-catalog and factual-relation contracts shared by application and aggregation stages. | [files/src/landscout/common/bess_application_contract.py.md](files/src/landscout/common/bess_application_contract.py.md) |
| `src/landscout/common/cadastre_contract.py` | Validates the canonical normalized Cadastre prefix, identity, 2D geometry/status facts, and recomputed EPSG:2154 parcel areas. | [files/src/landscout/common/cadastre_contract.py.md](files/src/landscout/common/cadastre_contract.py.md) |
| `src/landscout/common/frame_integrity.py` | Builds deterministic structural signatures for Pandas and GeoPandas frames. | [files/src/landscout/common/frame_integrity.py.md](files/src/landscout/common/frame_integrity.py.md) |
| `src/landscout/common/immutable_mapping.py` | Provides recursively immutable mappings, strict canonical-JSON integrity freezing, and copy/deep-copy-safe immutable identity. | [files/src/landscout/common/immutable_mapping.py.md](files/src/landscout/common/immutable_mapping.py.md) |
| `src/landscout/common/planning_feature_contract.py` | Validates stored factual planning relation semantics without rereading GPU geometry. | [files/src/landscout/common/planning_feature_contract.py.md](files/src/landscout/common/planning_feature_contract.py.md) |
| `src/landscout/common/planning_feature_schema.py` | Centralizes ordered normalized, CNIG-coded, and BESS-application feature/relation schemas and dtypes. | [files/src/landscout/common/planning_feature_schema.py.md](files/src/landscout/common/planning_feature_schema.py.md) |
| `src/landscout/common/planning_overlay.py` | Defines the technical floating-point tolerance used by factual planning overlay checks. | [files/src/landscout/common/planning_overlay.py.md](files/src/landscout/common/planning_overlay.py.md) |
| `src/landscout/common/planning_text.py` | Normalizes planning text for deterministic matching while retaining mappings back to raw source spans. | [files/src/landscout/common/planning_text.py.md](files/src/landscout/common/planning_text.py.md) |
| `src/landscout/common/safe_http.py` | Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects. | [files/src/landscout/common/safe_http.py.md](files/src/landscout/common/safe_http.py.md) |
| `src/landscout/common/strict_json.py` | Decodes trust-bearing JSON with strict UTF-8, duplicate-key, finite-number, overflow, and object-root enforcement. | [files/src/landscout/common/strict_json.py.md](files/src/landscout/common/strict_json.py.md) |
| `src/landscout/common/strict_yaml.py` | Decodes trust-bearing YAML with a SafeLoader subclass that rejects duplicate mapping keys at every depth. | [files/src/landscout/common/strict_yaml.py.md](files/src/landscout/common/strict_yaml.py.md) |

## Geo/GIS

| Repository file | Actual role | Companion |
|---|---|---|
| `src/landscout/geo/__init__.py` | Re-exports the supported CRS and geometry API from landscout.geo. | [files/src/landscout/geo/__init__.py.md](files/src/landscout/geo/__init__.py.md) |
| `src/landscout/geo/crs.py` | Exposes canonical storage and metric CRS constants. | [files/src/landscout/geo/crs.py.md](files/src/landscout/geo/crs.py.md) |
| `src/landscout/geo/geometry.py` | Validates parcel geometry and computes metric shape measurements on calculation-only Lambert-93 copies. | [files/src/landscout/geo/geometry.py.md](files/src/landscout/geo/geometry.py.md) |

## Source adapters

| Repository file | Actual role | Companion |
|---|---|---|
| `src/landscout/sources/__init__.py` | Re-exports approved source-bound adapter APIs, including Cadastre authority and INPN extraction/catalog trust boundaries, without presenting raw-path helpers as equivalent trust roots. | [files/src/landscout/sources/__init__.py.md](files/src/landscout/sources/__init__.py.md) |
| `src/landscout/sources/cadastre_fr.py` | Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks. | [files/src/landscout/sources/cadastre_fr.py.md](files/src/landscout/sources/cadastre_fr.py.md) |
| `src/landscout/sources/cadastre_loader_fr.py` | Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data. | [files/src/landscout/sources/cadastre_loader_fr.py.md](files/src/landscout/sources/cadastre_loader_fr.py.md) |
| `src/landscout/sources/gpu_fr.py` | Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance. | [files/src/landscout/sources/gpu_fr.py.md](files/src/landscout/sources/gpu_fr.py.md) |
| `src/landscout/sources/ign_bdtopo_fr.py` | Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data. | [files/src/landscout/sources/ign_bdtopo_fr.py.md](files/src/landscout/sources/ign_bdtopo_fr.py.md) |
| `src/landscout/sources/inpn_protected_areas_catalog_fr.py` | Builds and independently validates the schema-2 metadata-only INPN catalog from immutable package bytes with exact GPKG driver evidence and narrow known-warning handling. | [files/src/landscout/sources/inpn_protected_areas_catalog_fr.py.md](files/src/landscout/sources/inpn_protected_areas_catalog_fr.py.md) |
| `src/landscout/sources/inpn_protected_areas_fr.py` | Acquires the pinned PatriNat/INPN EP archive with controlled ZIP opening and binds extraction returns to archive-derived inventory plus final archive-path postconditions. | [files/src/landscout/sources/inpn_protected_areas_fr.py.md](files/src/landscout/sources/inpn_protected_areas_fr.py.md) |
| `src/landscout/sources/rte_odre_fr.py` | Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation. | [files/src/landscout/sources/rte_odre_fr.py.md](files/src/landscout/sources/rte_odre_fr.py.md) |

## Stages

| Repository file | Actual role | Companion |
|---|---|---|
| `src/landscout/stages/__init__.py` | Re-exports stable stage result, error, loader, validator, and transformation APIs, including factual zoning result/error contracts. | [files/src/landscout/stages/__init__.py.md](files/src/landscout/stages/__init__.py.md) |
| `src/landscout/stages/aggregate_bess_planning_feature_policy.py` | Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries. | [files/src/landscout/stages/aggregate_bess_planning_feature_policy.py.md](files/src/landscout/stages/aggregate_bess_planning_feature_policy.py.md) |
| `src/landscout/stages/apply_bess_planning_feature_policy.py` | Applies exact coded-result and policy-result evidence to planning feature catalogs and relations. | [files/src/landscout/stages/apply_bess_planning_feature_policy.py.md](files/src/landscout/stages/apply_bess_planning_feature_policy.py.md) |
| `src/landscout/stages/apply_road_vehicle_proxy_policy.py` | Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation. | [files/src/landscout/stages/apply_road_vehicle_proxy_policy.py.md](files/src/landscout/stages/apply_road_vehicle_proxy_policy.py.md) |
| `src/landscout/stages/assess_grid_coverage.py` | Diagnoses grid proxy distances against the configured IGN source-package boundary. | [files/src/landscout/stages/assess_grid_coverage.py.md](files/src/landscout/stages/assess_grid_coverage.py.md) |
| `src/landscout/stages/assess_road_proximity_coverage.py` | Diagnoses road proxy proximity against the verified IGN department coverage boundary. | [files/src/landscout/stages/assess_road_proximity_coverage.py.md](files/src/landscout/stages/assess_road_proximity_coverage.py.md) |
| `src/landscout/stages/bess_planning_feature_policy.py` | Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings. | [files/src/landscout/stages/bess_planning_feature_policy.py.md](files/src/landscout/stages/bess_planning_feature_policy.py.md) |
| `src/landscout/stages/enrich_grid_proximity.py` | Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data. | [files/src/landscout/stages/enrich_grid_proximity.py.md](files/src/landscout/stages/enrich_grid_proximity.py.md) |
| `src/landscout/stages/enrich_planning_features.py` | Normalizes GPU planning feature catalogs and constructs validated factual parcel-feature relations. | [files/src/landscout/stages/enrich_planning_features.py.md](files/src/landscout/stages/enrich_planning_features.py.md) |
| `src/landscout/stages/enrich_planning_zoning.py` | Intersects parcels with verified GPU zoning and source-completely reconstructs every required factual parcel-summary column. | [files/src/landscout/stages/enrich_planning_zoning.py.md](files/src/landscout/stages/enrich_planning_zoning.py.md) |
| `src/landscout/stages/enrich_road_proximity.py` | Computes per-class parcel-to-road proxy proximity using source-bound policy application results. | [files/src/landscout/stages/enrich_road_proximity.py.md](files/src/landscout/stages/enrich_road_proximity.py.md) |
| `src/landscout/stages/enrich_shape.py` | Adds parcel shape metrics and diagnostics for valid cadastral geometries. | [files/src/landscout/stages/enrich_shape.py.md](files/src/landscout/stages/enrich_shape.py.md) |
| `src/landscout/stages/filter_parcels.py` | Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking. | [files/src/landscout/stages/filter_parcels.py.md](files/src/landscout/stages/filter_parcels.py.md) |
| `src/landscout/stages/index_planning_regulation.py` | Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index. | [files/src/landscout/stages/index_planning_regulation.py.md](files/src/landscout/stages/index_planning_regulation.py.md) |
| `src/landscout/stages/interpret_bess_zoning.py` | Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure. | [files/src/landscout/stages/interpret_bess_zoning.py.md](files/src/landscout/stages/interpret_bess_zoning.py.md) |
| `src/landscout/stages/normalize_access_ign.py` | Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability. | [files/src/landscout/stages/normalize_access_ign.py.md](files/src/landscout/stages/normalize_access_ign.py.md) |
| `src/landscout/stages/normalize_cadastre.py` | Source-completely normalizes a fresh physical `CadastreParcelSource` into the stable canonical parcel schema. | [files/src/landscout/stages/normalize_cadastre.py.md](files/src/landscout/stages/normalize_cadastre.py.md) |
| `src/landscout/stages/normalize_grid_ign.py` | Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs. | [files/src/landscout/stages/normalize_grid_ign.py.md](files/src/landscout/stages/normalize_grid_ign.py.md) |
| `src/landscout/stages/planning_overlay.py` | Preserves the historical stage import path by re-exporting the shared common-layer technical overlay tolerance constants and function without adding behavior. | [files/src/landscout/stages/planning_overlay.py.md](files/src/landscout/stages/planning_overlay.py.md) |
| `src/landscout/stages/profile_shape.py` | Profiles shape metrics and scenario evidence without making parcel suitability decisions. | [files/src/landscout/stages/profile_shape.py.md](files/src/landscout/stages/profile_shape.py.md) |
| `src/landscout/stages/resolve_planning_feature_codes.py` | Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary. | [files/src/landscout/stages/resolve_planning_feature_codes.py.md](files/src/landscout/stages/resolve_planning_feature_codes.py.md) |
| `src/landscout/stages/road_vehicle_proxy_policy.py` | Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy. | [files/src/landscout/stages/road_vehicle_proxy_policy.py.md](files/src/landscout/stages/road_vehicle_proxy_policy.py.md) |
| `src/landscout/stages/structure_planning_regulation.py` | Partitions indexed regulation into source-bound sections while failing closed on applicable body-page extraction errors. | [files/src/landscout/stages/structure_planning_regulation.py.md](files/src/landscout/stages/structure_planning_regulation.py.md) |

## Tests

| Repository file | Actual role | Companion |
|---|---|---|
| `tests/integration/test_gpu_planning_end_to_end.py` | Exercises the complete synthetic physical GPU archive-to-zoning/PDF/structure/policy/result chain without bypassing zoning validation. | [files/tests/integration/test_gpu_planning_end_to_end.py.md](files/tests/integration/test_gpu_planning_end_to_end.py.md) |
| `tests/unit/test_aggregate_bess_planning_feature_policy.py` | Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file. | [files/tests/unit/test_aggregate_bess_planning_feature_policy.py.md](files/tests/unit/test_aggregate_bess_planning_feature_policy.py.md) |
| `tests/unit/test_apply_bess_planning_feature_policy.py` | Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file. | [files/tests/unit/test_apply_bess_planning_feature_policy.py.md](files/tests/unit/test_apply_bess_planning_feature_policy.py.md) |
| `tests/unit/test_apply_road_vehicle_proxy_policy.py` | Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file. | [files/tests/unit/test_apply_road_vehicle_proxy_policy.py.md](files/tests/unit/test_apply_road_vehicle_proxy_policy.py.md) |
| `tests/unit/test_assess_grid_coverage.py` | Provides complete unit and regression coverage for the `assess_grid_coverage` contracts exercised in this file. | [files/tests/unit/test_assess_grid_coverage.py.md](files/tests/unit/test_assess_grid_coverage.py.md) |
| `tests/unit/test_assess_road_proximity_coverage.py` | Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file. | [files/tests/unit/test_assess_road_proximity_coverage.py.md](files/tests/unit/test_assess_road_proximity_coverage.py.md) |
| `tests/unit/test_bess_planning_feature_policy.py` | Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file. | [files/tests/unit/test_bess_planning_feature_policy.py.md](files/tests/unit/test_bess_planning_feature_policy.py.md) |
| `tests/unit/test_cadastre_fr.py` | Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file. | [files/tests/unit/test_cadastre_fr.py.md](files/tests/unit/test_cadastre_fr.py.md) |
| `tests/unit/test_cadastre_loader_fr.py` | Provides complete unit and regression coverage for the `cadastre_loader_fr` contracts exercised in this file. | [files/tests/unit/test_cadastre_loader_fr.py.md](files/tests/unit/test_cadastre_loader_fr.py.md) |
| `tests/unit/test_config.py` | Provides complete unit and regression coverage for the `config` contracts exercised in this file. | [files/tests/unit/test_config.py.md](files/tests/unit/test_config.py.md) |
| `tests/unit/test_deep_immutability.py` | Proves deep configuration/policy immutability, canonical artifact-JSON leaf rejection, alias isolation, safe immutable/Pydantic deep copy, and stable canonical hashes. | [files/tests/unit/test_deep_immutability.py.md](files/tests/unit/test_deep_immutability.py.md) |
| `tests/unit/test_crs.py` | Provides complete unit and regression coverage for the `crs` contracts exercised in this file. | [files/tests/unit/test_crs.py.md](files/tests/unit/test_crs.py.md) |
| `tests/unit/test_enrich_grid_proximity.py` | Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file. | [files/tests/unit/test_enrich_grid_proximity.py.md](files/tests/unit/test_enrich_grid_proximity.py.md) |
| `tests/unit/test_enrich_planning_features.py` | Provides complete unit and regression coverage for the `enrich_planning_features` contracts exercised in this file. | [files/tests/unit/test_enrich_planning_features.py.md](files/tests/unit/test_enrich_planning_features.py.md) |
| `tests/unit/test_enrich_planning_zoning.py` | Provides complete unit and regression coverage for the `enrich_planning_zoning` contracts exercised in this file. | [files/tests/unit/test_enrich_planning_zoning.py.md](files/tests/unit/test_enrich_planning_zoning.py.md) |
| `tests/unit/test_enrich_road_proximity.py` | Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file. | [files/tests/unit/test_enrich_road_proximity.py.md](files/tests/unit/test_enrich_road_proximity.py.md) |
| `tests/unit/test_enrich_shape.py` | Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file. | [files/tests/unit/test_enrich_shape.py.md](files/tests/unit/test_enrich_shape.py.md) |
| `tests/unit/test_filter_parcels.py` | Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file. | [files/tests/unit/test_filter_parcels.py.md](files/tests/unit/test_filter_parcels.py.md) |
| `tests/unit/test_filter_shape.py` | Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file. | [files/tests/unit/test_filter_shape.py.md](files/tests/unit/test_filter_shape.py.md) |
| `tests/unit/test_geometry.py` | Provides complete unit and regression coverage for the `geometry` contracts exercised in this file. | [files/tests/unit/test_geometry.py.md](files/tests/unit/test_geometry.py.md) |
| `tests/unit/test_gpu_fr.py` | Provides complete unit and regression coverage for the `gpu_fr` contracts exercised in this file. | [files/tests/unit/test_gpu_fr.py.md](files/tests/unit/test_gpu_fr.py.md) |
| `tests/unit/test_ign_bdtopo_fr.py` | Provides complete unit and regression coverage for the `ign_bdtopo_fr` contracts exercised in this file. | [files/tests/unit/test_ign_bdtopo_fr.py.md](files/tests/unit/test_ign_bdtopo_fr.py.md) |
| `tests/unit/test_index_planning_regulation.py` | Provides complete unit and regression coverage for the `index_planning_regulation` contracts exercised in this file. | [files/tests/unit/test_index_planning_regulation.py.md](files/tests/unit/test_index_planning_regulation.py.md) |
| `tests/unit/test_inpn_protected_areas_catalog_fr.py` | Proves immutable package-byte metadata inspection, narrow Pyogrio warning filtering, exact GPKG driver/schema-2 hashing, canonical runtime types, and independent rebuild. | [files/tests/unit/test_inpn_protected_areas_catalog_fr.py.md](files/tests/unit/test_inpn_protected_areas_catalog_fr.py.md) |
| `tests/unit/test_inpn_protected_areas_fr.py` | Proves controlled ZIP errors, canonical download lineage, archive-derived inventories, return-boundary archive postconditions, effective swap attacks, four-way extraction equality, and offline rebuild. | [files/tests/unit/test_inpn_protected_areas_fr.py.md](files/tests/unit/test_inpn_protected_areas_fr.py.md) |
| `tests/unit/test_interpret_bess_zoning.py` | Provides complete unit and regression coverage for the `interpret_bess_zoning` contracts exercised in this file. | [files/tests/unit/test_interpret_bess_zoning.py.md](files/tests/unit/test_interpret_bess_zoning.py.md) |
| `tests/unit/test_normalize_access_ign.py` | Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file. | [files/tests/unit/test_normalize_access_ign.py.md](files/tests/unit/test_normalize_access_ign.py.md) |
| `tests/unit/test_normalize_cadastre.py` | Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file. | [files/tests/unit/test_normalize_cadastre.py.md](files/tests/unit/test_normalize_cadastre.py.md) |
| `tests/unit/test_normalize_grid_ign.py` | Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file. | [files/tests/unit/test_normalize_grid_ign.py.md](files/tests/unit/test_normalize_grid_ign.py.md) |
| `tests/unit/test_package.py` | Verifies exact package exports and equality between `landscout.__version__` and `project.version`. | [files/tests/unit/test_package.py.md](files/tests/unit/test_package.py.md) |
| `tests/unit/test_profile_shape.py` | Provides complete unit and regression coverage for the `profile_shape` contracts exercised in this file. | [files/tests/unit/test_profile_shape.py.md](files/tests/unit/test_profile_shape.py.md) |
| `tests/unit/test_resolve_planning_feature_codes.py` | Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file. | [files/tests/unit/test_resolve_planning_feature_codes.py.md](files/tests/unit/test_resolve_planning_feature_codes.py.md) |
| `tests/unit/test_road_vehicle_proxy_policy.py` | Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file. | [files/tests/unit/test_road_vehicle_proxy_policy.py.md](files/tests/unit/test_road_vehicle_proxy_policy.py.md) |
| `tests/unit/test_rte_odre_fr.py` | Provides complete unit and regression coverage for the `rte_odre_fr` contracts exercised in this file. | [files/tests/unit/test_rte_odre_fr.py.md](files/tests/unit/test_rte_odre_fr.py.md) |
| `tests/unit/test_safe_http.py` | Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file. | [files/tests/unit/test_safe_http.py.md](files/tests/unit/test_safe_http.py.md) |
| `tests/unit/test_strict_serialization.py` | Proves the shared strict YAML/JSON duplicate, UTF-8, finite-number, overflow, and object-root contracts. | [files/tests/unit/test_strict_serialization.py.md](files/tests/unit/test_strict_serialization.py.md) |
| `tests/unit/test_structure_planning_regulation.py` | Provides complete unit and regression coverage for the `structure_planning_regulation` contracts exercised in this file. | [files/tests/unit/test_structure_planning_regulation.py.md](files/tests/unit/test_structure_planning_regulation.py.md) |

## Engineering history

| Repository file | Actual role | Companion |
|---|---|---|
| `docs/DEV_LOG.md` | Preserves chronological implementation and validation evidence; current source and tests remain authoritative. | [files/docs/DEV_LOG.md.md](files/docs/DEV_LOG.md.md) |
