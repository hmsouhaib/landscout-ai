# LandScout glossary

## Core project terms

**BESS** — Battery Energy Storage System. LandScout is BESS-first, but current evidence/prechecks do not by themselves establish buildability, authorization, connection, access, or economic suitability.

**Muret** — Commune code 31395 and the current proving-ground geography/source set used by checked-in scan/planning profiles and persisted local validation evidence.

**parcel** — A cadastral polygon/multipolygon row identified by exact `parcel_id`; it is a spatial/source unit, not an owner/contact record.

**source-complete** — A public validation boundary that binds an object to its required configured/physical/upstream source, rather than accepting a merely self-consistent in-memory frame or result.

**lineage** — Provider/product/document/archive/layer/profile/hash/version/URL fields that describe origin. Lineage strings require validation but are not automatically physical proof.

**source lock** — Exact configured identity, version, URL, hash, schema, document, archive, or evidence reference that a validator requires before use.

**proxy** — Evidence used as an explicitly limited approximation. It must not be renamed or interpreted as the engineering/legal fact it does not establish.

**precheck** — Deterministic coded evidence outcome requiring later human/domain review; not authorization, prohibition, rejection, or a score.

**coverage** — Count/existence evidence for expected classes/features or the extent of a source package, depending on the named object.

**coverage boundary** — The configured IGN department polygon boundary used to diagnose whether a nearest-feature result may be limited by the verified package extent.

## Organizations and source systems

**Cadastre** — Official French cadastral parcel geometry source acquired as commune GeoJSON gzip.

**IGN** — Institut national de l'information géographique et forestière, source authority for BD TOPO.

**BD TOPO** — IGN topographic product providing electricity, road, and administrative-coverage geometries/attributes used as factual/proxy sources.

**RTE** — Réseau de Transport d'Électricité. Current adapter acquires configured datasets through the ODRÉ API; its data is not silently equated with IGN proxy features.

**ODRÉ** — Open Data Réseaux Énergies platform/API at the exact configured official origin.

**GPU** — Géoportail de l'Urbanisme, source for PLU document metadata, archives, written files, and spatial layers.

**PLU** — Plan local d'urbanisme. Current planning evidence includes zoning geometry, feature catalogs, written regulation text, structured evidence, and prechecks.

**CNIG** — Conseil national de l'information géolocalisée. The checked-in CNIG PLU v2017 profile supplies official feature code-pair meaning/reference evidence.

**INPN** — Inventaire national du patrimoine naturel program used in the protected-area source identity.

**PatriNat** — Source provider/portal for the pinned protected-areas reference archive, under MNHN authority and the INPN program.

**EP** — Dataset ID for the French protected-areas reference base acquired by the current environment source adapter.

## Geometry and CRS

**EPSG:4326 / WGS84** — Geographic longitude/latitude CRS used for stored normalized parcels.

**EPSG:2154 / Lambert-93** — Projected metric CRS used for mainland-France distance, area, length, width, intersection, and boundary calculations.

**VALID / INVALID** — Exact cadastral normalized geometry statuses. `VALID` permits metric use; `INVALID` preserves a source geometry defect and nulls metrics rather than repairing it.

**VALID / NULL / EMPTY / INVALID (IGN)** — Factual geometry-quality statuses used by IGN normalizers; valid rows additionally satisfy the role-specific geometry-kind contract.

**PROXY_GEOMETRY** — IGN spatial role stating a mapped feature is used as proxy geometry. It is not proof of capacity/access/legal status.

**SOURCE_COVERAGE_BOUNDARY** — IGN spatial role for the configured department polygon used only to diagnose source-package boundary effects.

**tie** — More than one feature at the exact nearest distance. Code retains all tie IDs and selects a deterministic lexical representative.

## Planning evidence

**FACT** — Source attribute/geometry/identity or computed factual spatial relation before policy meaning.

**SOURCE TEXT** — Exact written-regulation bytes/page/text/span evidence.

**STRUCTURED EVIDENCE** — Deterministic sections/headings/zone mappings/topic flags with source closure.

**CONDITIONAL_REVIEW** — Written-zoning policy outcome indicating a route has unresolved conditions/applicability requiring review; not an approval.

**CONTEXT_ONLY** — Evidence retained for context but forbidden from qualifying a policy route.

**UNKNOWN / UNKNOWN_REVIEW** — Explicit unresolved/malformed/out-of-domain evidence. It must not be coerced into a positive fallback.

**RESOLVED_OFFICIAL** — CNIG feature code pair matched exactly to official checked-in meaning/reference evidence.

**UNKNOWN_CODE_PAIR** — Observed pair not present in the official profile; official meaning fields remain true null.

**relation type** — Geometry-specific factual parcel-feature relationship such as `AREA_OVERLAP`, `LENGTH_OVERLAP`, `TOUCH_ONLY`, `INSIDE`, or `BOUNDARY_TOUCH`.

## Road terms

**general vehicle proxy** — IGN evidence compatible with the policy's general-car/light-vehicle scope after higher-priority restrictions/unknowns; not heavy/BESS/legal access.

**NOT_PROVEN** — Explicit heavy-vehicle access value carried by the road policy/application, preventing an unsupported positive claim.

**NOT_DISTANCE_PROXY** — Road class excluded from parcel distance indexing because technical/source evidence makes it unsuitable as distance proxy; not a parcel rejection.

## Cache/trust terms

**`.part`** — Temporary file/directory used to build and verify a replacement before publication.

**`.bak`** — Recovery copy/material retained during replacement/rollback or after a double failure; its presence may require manual recovery and stop network work.

**manifest/sidecar** — Strict metadata file binding physical artifact/cache bytes to source identity, size, SHA, schema, and component roles.

**lightweight envelope validation** — Result type/schema/scalar/frame/hash/semantic validation that does not reread GPU sources or reconstruct spatial intersections.

**physical revalidation** — Rehashing/rereading actual files/layers and comparing them with supplied source objects/results.
