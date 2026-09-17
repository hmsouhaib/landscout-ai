# Discoverable step history

Status: historical narrative/publication association **CHECKED**; active DOCS.CONTINUITY.1 remains **IN_PROGRESS**. All 99 section narratives and 101 Git publication records were reviewed. The long raw EP domain dump is retained mechanically, not reprofiled as a fresh source run. This is navigation into evidence, not independent approval or a claim that every reported run has been repeated.

Read [CURRENT_STATE](CURRENT_STATE.md) for the active ticket and next action, [provenance](CONTEXT_PROVENANCE.md) for evidence classes, and the machine-readable [STEP_LEDGER.json](STEP_LEDGER.json) for exact SHAs, publication paths/parents, validation reports, review scope and missing prompts. Do not infer chronology from the order of sections in DEV_LOG: several earlier sections were appended after later work.

The discovered history contains 101 Git publications, 99 current STEP/global-hardening headings and one additional recovery-correction step explicitly supplied in Appendix A8. STEP 0–4 implementation bytes share the initial scaffold publication; STEP 5 spans GIS and shape commits, while their log was added retrospectively. No STEP 6 heading was found; no replacement numbering is invented. Recovery branch commits are retained separately from clean-main finalization.

Only STEP 7F.1B.4 carries the supplied `APPROVED_RECORDED_IN_CONVERSATION` functional verdict. STEP 7F.1C.1 has a specifically limited supplied review and full semantic review **PENDING**. Other logs mentioning a reviewer do not provide a retained complete verdict. Historic executions are reported evidence, not newly executed audit commands.

## Step index

| Exact existing label | Purpose | Implementation publication(s) | Evidence / review state |
|---|---|---|---|
| 0 | Environment check | `18f29e30` | [DEV_LOG](../DEV_LOG.md#step-0--environment-check); UNAVAILABLE |
| 1 | Python and Git setup | `18f29e30` | [DEV_LOG](../DEV_LOG.md#step-1--python-and-git-setup); UNAVAILABLE |
| 2 | GIS dependencies | `18f29e30` | [DEV_LOG](../DEV_LOG.md#step-2--gis-dependencies); UNAVAILABLE |
| 3 | Quality tools | `18f29e30` | [DEV_LOG](../DEV_LOG.md#step-3--quality-tools); UNAVAILABLE |
| 4 | Configuration system | `18f29e30` | [DEV_LOG](../DEV_LOG.md#step-4--configuration-system); UNAVAILABLE |
| 5 | GIS geometry core | `d1330049`, `f7d72c57` | [DEV_LOG](../DEV_LOG.md#step-5--gis-geometry-core); UNAVAILABLE |
| 7A | French cadastre downloader | `b961c568` | [DEV_LOG](../DEV_LOG.md#step-7a--french-cadastre-downloader); UNAVAILABLE |
| 7A.1 | Package installation fix | `7ccc7fc3` | [DEV_LOG](../DEV_LOG.md#step-7a1--package-installation-fix); UNAVAILABLE |
| 7A.2 | Cadastre cache freshness | `be97ad00` | [DEV_LOG](../DEV_LOG.md#step-7a2--cadastre-cache-freshness); UNAVAILABLE |
| 7A.3 | Cadastre gzip integrity | `84a59d61` | [DEV_LOG](../DEV_LOG.md#step-7a3--cadastre-gzip-integrity); UNAVAILABLE |
| 7B.1 | Load French cadastral parcels | `7bc2c6bc`, `a205c66c` | [DEV_LOG](../DEV_LOG.md#step-7b1--load-french-cadastral-parcels); UNAVAILABLE |
| 7B.2 | Normalize Muret parcels | `c65a62fc` | [DEV_LOG](../DEV_LOG.md#step-7b2--normalize-muret-parcels); UNAVAILABLE |
| 7B.3 | Filter BESS parcels by area | `33d02995` | [DEV_LOG](../DEV_LOG.md#step-7b3--filter-bess-parcels-by-area); UNAVAILABLE |
| 7B.3.1 | Strengthen parcel filter validation | `2326cc4d` | [DEV_LOG](../DEV_LOG.md#step-7b31--strengthen-parcel-filter-validation); UNAVAILABLE |
| 7B.4 | Enrich BESS parcel shape metrics | `06c62673` | [DEV_LOG](../DEV_LOG.md#step-7b4--enrich-bess-parcel-shape-metrics); UNAVAILABLE |
| 7B.4.1 | Centralize parcel shape metrics | `6c9c7e99` | [DEV_LOG](../DEV_LOG.md#step-7b41--centralize-parcel-shape-metrics); UNAVAILABLE |
| 7B.5 | Profile BESS parcel shape distribution | `97fcbaa0` | [DEV_LOG](../DEV_LOG.md#step-7b5--profile-bess-parcel-shape-distribution); UNAVAILABLE |
| 7B.5.1 | Explicit VALID and ERROR profiling | `d93df2f2` | [DEV_LOG](../DEV_LOG.md#step-7b51--explicit-valid-and-error-profiling); UNAVAILABLE |
| 7B.6 | Configurable calibrated BESS shape screening | `5642b29b` | [DEV_LOG](../DEV_LOG.md#step-7b6--configurable-calibrated-bess-shape-screening); UNAVAILABLE |
| 7C.1 | RTE / ODRÉ grid source ingestion | `25160fde` | [DEV_LOG](../DEV_LOG.md#step-7c1--rte--odré-grid-source-ingestion); UNAVAILABLE |
| 7C.1.1 | Strengthen RTE / ODRÉ source integrity | `429d7a34` | [DEV_LOG](../DEV_LOG.md#step-7c11--strengthen-rte--odré-source-integrity); UNAVAILABLE |
| 7C.2 | IGN BD TOPO electricity spatial source ingestion | `d9e81305` | [DEV_LOG](../DEV_LOG.md#step-7c2--ign-bd-topo-electricity-spatial-source-ingestion); UNAVAILABLE |
| 7C.3 | Normalize IGN electricity proxy layers | `978c15ca` | [DEV_LOG](../DEV_LOG.md#step-7c3--normalize-ign-electricity-proxy-layers); UNAVAILABLE |
| 7C.3.1 | Harden IGN grid normalization lineage, geometry semantics, and numeric integrity | `d698fd80` | [DEV_LOG](../DEV_LOG.md#step-7c31--harden-ign-grid-normalization-lineage-geometry-semantics-and-numeric-integrity); UNAVAILABLE |
| 7C.3.2 | Close IGN normalization API boundary and validate lineage context | `24659ec5` | [DEV_LOG](../DEV_LOG.md#step-7c32--close-ign-normalization-api-boundary-and-validate-lineage-context); UNAVAILABLE |
| 7C.4 | Parcel-to-IGN grid proxy proximity | `c35c4558` | [DEV_LOG](../DEV_LOG.md#step-7c4--parcel-to-ign-grid-proxy-proximity); UNAVAILABLE |
| 7C.4.1 | Harden grid-proximity integrity contracts | `a0d83a20` | [DEV_LOG](../DEV_LOG.md#step-7c41--harden-grid-proximity-integrity-contracts); UNAVAILABLE |
| 7C.4.2 | Cross-validate exact-line proximity representations | `c1ec75db` | [DEV_LOG](../DEV_LOG.md#step-7c42--cross-validate-exact-line-proximity-representations); UNAVAILABLE |
| 7C.5 | Diagnose IGN grid proxy coverage boundaries | `881e8e82` | [DEV_LOG](../DEV_LOG.md#step-7c5--diagnose-ign-grid-proxy-coverage-boundaries); UNAVAILABLE |
| 7D.1 | GPU Muret urban-planning source ingestion | `2a25659c` | [DEV_LOG](../DEV_LOG.md#step-7d1--gpu-muret-urban-planning-source-ingestion); UNAVAILABLE |
| 7D.1.1 | Harden GPU source and extraction integrity | `bb5ca08c` | [DEV_LOG](../DEV_LOG.md#step-7d11--harden-gpu-source-and-extraction-integrity); UNAVAILABLE |
| 7D.2 | Normalize GPU zoning and intersect Muret parcels | `24ac4747` | [DEV_LOG](../DEV_LOG.md#step-7d2--normalize-gpu-zoning-and-intersect-muret-parcels); UNAVAILABLE |
| 7D.3 | Normalize and intersect GPU planning features | `ba22f9b0` | [DEV_LOG](../DEV_LOG.md#step-7d3--normalize-and-intersect-gpu-planning-features); UNAVAILABLE |
| 7D.3.1 | Harden GPU planning-feature identity and result contracts | `76a9bfb4` | [DEV_LOG](../DEV_LOG.md#step-7d31--harden-gpu-planning-feature-identity-and-result-contracts); UNAVAILABLE |
| 7D.4A | Extract and index the Muret PLU written regulation | `8d5b855c` | [DEV_LOG](../DEV_LOG.md#step-7d4a--extract-and-index-the-muret-plu-written-regulation); UNAVAILABLE |
| 7D.4A.1 | Generalize and harden planning-regulation indexing | `1ee5da25` | [DEV_LOG](../DEV_LOG.md#step-7d4a1--generalize-and-harden-planning-regulation-indexing); UNAVAILABLE |
| 7D.4A.2 | Seal regulation-source selection and index lineage | `0825017d` | [DEV_LOG](../DEV_LOG.md#step-7d4a2--seal-regulation-source-selection-and-index-lineage); UNAVAILABLE |
| 7D.4B | Build factual regulation structure and zone evidence | `281f7b7e` | [DEV_LOG](../DEV_LOG.md#step-7d4b--build-factual-regulation-structure-and-zone-evidence); UNAVAILABLE |
| 7D.4B.1 | Harden regulation structure and evidence fidelity | `7552c249` | [DEV_LOG](../DEV_LOG.md#step-7d4b1--harden-regulation-structure-and-evidence-fidelity); UNAVAILABLE |
| 7D.4B.2 | Finalize structure schema and deterministic edge handling | `7f3fce31` | [DEV_LOG](../DEV_LOG.md#step-7d4b2--finalize-structure-schema-and-deterministic-edge-handling); UNAVAILABLE |
| 7D.4B.3 | Finalize factual structure edge integrity | `319955bf` | [DEV_LOG](../DEV_LOG.md#step-7d4b3--finalize-factual-structure-edge-integrity); UNAVAILABLE |
| 7D.4B.4 | Reject ambiguous structural heading matches | `6a2f54a6` | [DEV_LOG](../DEV_LOG.md#step-7d4b4--reject-ambiguous-structural-heading-matches); UNAVAILABLE |
| 7D.4C | Evidence-backed BESS zoning precheck | `c268bd6d` | [DEV_LOG](../DEV_LOG.md#step-7d4c--evidence-backed-bess-zoning-precheck); UNAVAILABLE |
| 7D.4C.1 | Harden BESS zoning-policy semantics and evidence auditability | `111a3788` | [DEV_LOG](../DEV_LOG.md#step-7d4c1--harden-bess-zoning-policy-semantics-and-evidence-auditability); UNAVAILABLE |
| 7D.4C.2 | Link BESS zoning evidence into coherent decision routes | `f93522fe` | [DEV_LOG](../DEV_LOG.md#step-7d4c2--link-bess-zoning-evidence-into-coherent-decision-routes); UNAVAILABLE |
| 7D.4C.3 | Close evidence-to-route coverage and chapter identity | `d90d0acc` | [DEV_LOG](../DEV_LOG.md#step-7d4c3--close-evidence-to-route-coverage-and-chapter-identity); UNAVAILABLE |
| 7D.4C.4 | Enforce unique chapter-scoped evidence occurrences | `2ba41b44` | [DEV_LOG](../DEV_LOG.md#step-7d4c4--enforce-unique-chapter-scoped-evidence-occurrences); UNAVAILABLE |
| 7D.5A | Resolve official CNIG meanings for planning-feature codes | `266acb98` | [DEV_LOG](../DEV_LOG.md#step-7d5a--resolve-official-cnig-meanings-for-planning-feature-codes); UNAVAILABLE |
| 7D.5A.1 | Harden CNIG snapshot fidelity and public coding contracts | `1d18eea8` | [DEV_LOG](../DEV_LOG.md#step-7d5a1--harden-cnig-snapshot-fidelity-and-public-coding-contracts); UNAVAILABLE |
| 7D.5A.2 | Close normalized planning-feature input contracts | `457c4090` | [DEV_LOG](../DEV_LOG.md#step-7d5a2--close-normalized-planning-feature-input-contracts); UNAVAILABLE |
| 7D.5A.3 | Bind normalized planning facts to GPU and parcel identity | `8ccbfde2` | [DEV_LOG](../DEV_LOG.md#step-7d5a3--bind-normalized-planning-facts-to-gpu-and-parcel-identity); UNAVAILABLE |
| 7D.5A.4 | Prove GPU-source and parcel-feature relation completeness | `7f87bbe8` | [DEV_LOG](../DEV_LOG.md#step-7d5a4--prove-gpu-source-and-parcel-feature-relation-completeness); UNAVAILABLE |
| 7D.5A.5 | Finalize deterministic relation schemas and GPU validation boundaries | `893d912f` | [DEV_LOG](../DEV_LOG.md#step-7d5a5--finalize-deterministic-relation-schemas-and-gpu-validation-boundaries); UNAVAILABLE |
| 7D.5B.1 | Define a strict BESS policy for official CNIG feature codes | `8e52b0b3` | [DEV_LOG](../DEV_LOG.md#step-7d5b1--define-a-strict-bess-policy-for-official-cnig-feature-codes); UNAVAILABLE |
| 7D.5B.1.1 | Harden BESS CNIG policy snapshot and persisted artifacts | `da673db9` | [DEV_LOG](../DEV_LOG.md#step-7d5b11--harden-bess-cnig-policy-snapshot-and-persisted-artifacts); UNAVAILABLE |
| 7D.5B.1.2 | Finalize BESS CNIG policy hash and artifact integrity | `bc96c141` | [DEV_LOG](../DEV_LOG.md#step-7d5b12--finalize-bess-cnig-policy-hash-and-artifact-integrity); UNAVAILABLE |
| 7D.5B.2A | Apply BESS CNIG policy to features and relations | `cd8abcd6` | [DEV_LOG](../DEV_LOG.md#step-7d5b2a--apply-bess-cnig-policy-to-features-and-relations); UNAVAILABLE |
| 7D.5B.2A.1 | Finalize feature-policy application integrity | `b7cb0a10` | [DEV_LOG](../DEV_LOG.md#step-7d5b2a1--finalize-feature-policy-application-integrity); UNAVAILABLE |
| 7D.5B.2B | Aggregate BESS CNIG feature evidence to parcels | `4b4c08c8` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b--aggregate-bess-cnig-feature-evidence-to-parcels); UNAVAILABLE |
| 7D.5B.2B.1 | Seal intrinsic parcel-aggregation contracts | `74cde046` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b1--seal-intrinsic-parcel-aggregation-contracts); UNAVAILABLE |
| 7D.5B.2B.2 | Seal relation identity and global policy mapping | `c50c37c7` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b2--seal-relation-identity-and-global-policy-mapping); UNAVAILABLE |
| 7D.5B.2B.3 | Seal feature catalogs and factual relation semantics | `0502f435` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b3--seal-feature-catalogs-and-factual-relation-semantics); UNAVAILABLE |
| 7D.5B.2B.4 | Seal local source lineage and canonical schemas | `ed8b54df` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b4--seal-local-source-lineage-and-canonical-schemas); UNAVAILABLE |
| 7D.5B.2B.5 | Bind artifacts to exact upstream results | `c0e48bda` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b5--bind-artifacts-to-exact-upstream-results); UNAVAILABLE |
| 7D.5B.2B.5.1 | Finalize upstream envelopes and portable filenames | `6de0b7f6` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b51--finalize-upstream-envelopes-and-portable-filenames); UNAVAILABLE |
| 7D.5B.2B.5.2 | Close empty envelopes and Windows device names | `eb7af494` | [DEV_LOG](../DEV_LOG.md#step-7d5b2b52--close-empty-envelopes-and-windows-device-names); UNAVAILABLE |
| 7E.1A | Add factual IGN BD TOPO road-layer loading | `20cea426` | [DEV_LOG](../DEV_LOG.md#step-7e1a--add-factual-ign-bd-topo-road-layer-loading); UNAVAILABLE |
| 7E.1B | Normalize factual IGN road access attributes | `cd1861ea` | [DEV_LOG](../DEV_LOG.md#step-7e1b--normalize-factual-ign-road-access-attributes); UNAVAILABLE |
| GLOBAL HARDENING — Close source-integrity and adversarial validation gaps | GLOBAL HARDENING — Close source-integrity and adversarial validation gaps | `9e800227` | [DEV_LOG](../DEV_LOG.md#global-hardening--close-source-integrity-and-adversarial-validation-gaps); UNAVAILABLE |
| GLOBAL HARDENING REVIEW CORRECTION - Source-boundary and adversarial contracts | GLOBAL HARDENING REVIEW CORRECTION - Source-boundary and adversarial contracts | `8c3bdf6a` | [DEV_LOG](../DEV_LOG.md#global-hardening-review-correction---source-boundary-and-adversarial-contracts); UNAVAILABLE |
| GLOBAL HARDENING REVIEW CORRECTION.1 - Config-bound IGN non-electric roles | GLOBAL HARDENING REVIEW CORRECTION.1 - Config-bound IGN non-electric roles | `9d74fbb4` | [DEV_LOG](../DEV_LOG.md#global-hardening-review-correction1---config-bound-ign-non-electric-roles); UNAVAILABLE |
| 7E.2A | Compile official IGN general-vehicle proxy policy | `00adf397` | [DEV_LOG](../DEV_LOG.md#step-7e2a--compile-official-ign-general-vehicle-proxy-policy); review UNAVAILABLE; SUPERSEDED_BEFORE_APPLICATION by 7E.2A.1 |
| 7E.2A.1 | Correct IGN road proxy policy source semantics and evidence lineage | `12ec9e8f` | [DEV_LOG](../DEV_LOG.md#step-7e2a1--correct-ign-road-proxy-policy-source-semantics-and-evidence-lineage); UNAVAILABLE |
| 7E.2B | Apply IGN road vehicle proxy policy | `d26bb10b` | [DEV_LOG](../DEV_LOG.md#step-7e2b--apply-ign-road-vehicle-proxy-policy); UNAVAILABLE |
| 7E.3A | Compute parcel-to-road proximity by proxy class | `b230eb84` | [DEV_LOG](../DEV_LOG.md#step-7e3a--compute-parcel-to-road-proximity-by-proxy-class); UNAVAILABLE |
| 7E.3B | Diagnose parcel-road proximity against source-package boundary | `37a81560` | [DEV_LOG](../DEV_LOG.md#step-7e3b--diagnose-parcel-road-proximity-against-source-package-boundary); UNAVAILABLE |
| 7F.1A | Acquire PatriNat / INPN protected-areas reference archive | `bdcbb1fe` | [DEV_LOG](../DEV_LOG.md#step-7f1a--acquire-patrinat--inpn-protected-areas-reference-archive); UNAVAILABLE |
| 7F.1A.1 | Close DNS-resolved redirect network-safety gap | `463cb10b` | [DEV_LOG](../DEV_LOG.md#step-7f1a1--close-dns-resolved-redirect-network-safety-gap); UNAVAILABLE |
| 7F.1A.2 | Close repository trust-boundary review findings | `0078b4d7` | [DEV_LOG](../DEV_LOG.md#step-7f1a2--close-repository-trust-boundary-review-findings); UNAVAILABLE |
| 7F.1A.2.1 | Complete source cache-recovery safety parity | `16de8c0e` | [DEV_LOG](../DEV_LOG.md#step-7f1a21--complete-source-cache-recovery-safety-parity); UNAVAILABLE |
| 7F.1A.3 | Build complete living code documentation | `712921ae` | [DEV_LOG](../DEV_LOG.md#step-7f1a3--build-complete-living-code-documentation); UNAVAILABLE |
| 7F.1A.3.1 | Rebuild documentation fidelity from source semantics | `10cd448e` | [DEV_LOG](../DEV_LOG.md#step-7f1a31--rebuild-documentation-fidelity-from-source-semantics); UNAVAILABLE |
| 7F.1A.3.2 | Correct qualified-reference ownership and semantic documentation | `6c4d7ac2` | [DEV_LOG](../DEV_LOG.md#step-7f1a32--correct-qualified-reference-ownership-and-semantic-documentation); UNAVAILABLE |
| 7F.1A.4 | Close end-to-end source authority and planning-completeness gaps | `b19a21ea` | [DEV_LOG](../DEV_LOG.md#step-7f1a4--close-end-to-end-source-authority-and-planning-completeness-gaps); UNAVAILABLE |
| 7F.1A.4.1 | Make trust-bearing configuration deeply immutable | `b5c2fb9d` | [DEV_LOG](../DEV_LOG.md#step-7f1a41--make-trust-bearing-configuration-deeply-immutable); UNAVAILABLE |
| 7F.1A.4.2 | Reject mutable/non-canonical leaves in immutable integrity mappings | `c76386ef` | [DEV_LOG](../DEV_LOG.md#step-7f1a42--reject-mutablenon-canonical-leaves-in-immutable-integrity-mappings); UNAVAILABLE |
| 7F.1A.4.2.1 | Synchronize canonical living documentation | `6c20cb4b` | [DEV_LOG](../DEV_LOG.md#step-7f1a421--synchronize-canonical-living-documentation); UNAVAILABLE |
| 7F.1A.4.2.2 | Remove final canonical companion contradictions | `6ed496e8` | [DEV_LOG](../DEV_LOG.md#step-7f1a422--remove-final-canonical-companion-contradictions); UNAVAILABLE |
| 7F.1B.1 | Build exact INPN EP GeoPackage metadata catalog | `0ae05234` | [DEV_LOG](../DEV_LOG.md#step-7f1b1--build-exact-inpn-ep-geopackage-metadata-catalog); UNAVAILABLE |
| 7F.1B.1.1 | Bind INPN catalog to archive and package byte snapshots | `090626e8` | [DEV_LOG](../DEV_LOG.md#step-7f1b11--bind-inpn-catalog-to-archive-and-package-byte-snapshots); UNAVAILABLE |
| 7F.1B.1.2 | Close final INPN archive postconditions and evidence gaps | `26824f14`, `f20687f1`, `dcf071f9`, `40e9493e` | [DEV_LOG](../DEV_LOG.md#step-7f1b12--close-final-inpn-archive-postconditions-and-evidence-gaps); UNAVAILABLE |
| 7F.1B.1.2.1 | Cached-download archive return postcondition recovery correction | `f20687f1` | [Supplied ticket](tickets/DOCS.CONTINUITY.1.txt); UNAVAILABLE |
| 7F.1B.2 | Build exact INPN EP attribute-value profile | `77d0e938` | [DEV_LOG](../DEV_LOG.md#step-7f1b2--build-exact-inpn-ep-attribute-value-profile); UNAVAILABLE |
| 7F.1B.2.1 | Close intrinsic attribute-profile structure gaps | `3ecb918d` | [DEV_LOG](../DEV_LOG.md#step-7f1b21--close-intrinsic-attribute-profile-structure-gaps); UNAVAILABLE |
| 7F.1B.2.2 | Align INPN package-path canonicality and FID evidence | `abcba8e5` | [DEV_LOG](../DEV_LOG.md#step-7f1b22--align-inpn-package-path-canonicality-and-fid-evidence); UNAVAILABLE |
| 7F.1B.3 | Build exact INPN EP geometry-quality profile | `57edf936` | [DEV_LOG](../DEV_LOG.md#step-7f1b3--build-exact-inpn-ep-geometry-quality-profile); UNAVAILABLE |
| 7F.1B.3.1 | Close GeoPackage geometry-type contracts | `a2ebe526` | [DEV_LOG](../DEV_LOG.md#step-7f1b31--close-geopackage-geometry-type-contracts); UNAVAILABLE |
| 7F.1B.3.2 | Correct collection subtype assignability | `9f696c2d` | [DEV_LOG](../DEV_LOG.md#step-7f1b32--correct-collection-subtype-assignability); UNAVAILABLE |
| 7F.1B.4 | Assemble aligned INPN EP source evidence | `ca0ec73d` | [DEV_LOG](../DEV_LOG.md#step-7f1b4--assemble-aligned-inpn-ep-source-evidence); APPROVED_RECORDED_IN_CONVERSATION |
| 7F.1C.1 | Establish source-locked EP category meaning (research draft) | `aa4ebc70` | [DEV_LOG](../DEV_LOG.md#step-7f1c1--establish-source-locked-ep-category-meaning-research-draft); PARTIAL_REVIEW_RECORDED_IN_CONVERSATION |
| DOCS.CONTINUITY.1 | Audit the entire code reference and establish durable evidence-linked continuity | Not published | [Supplied ticket](tickets/DOCS.CONTINUITY.1.txt); PENDING |

## Missing and superseded material

The ledger retains unavailable original prompts/review receipts as null, not guessed transcripts. `git_publications` inventories ancillary documentation/recovery publications as well as implementation commits. Parent pointers are Git ancestry, not automatically functional dependencies or approval. Correction/dependency relationships require explicit evidence before being promoted from related numbering.

See [DEC-005](DECISIONS.md#dec-005--geometrycollection-subtype-correction-active-supersedes-earlier-restrictive-instruction) for the preserved GEOMETRYCOLLECTION correction and [history gaps](BACKLOG_AND_GAPS.md#historical-material-unavailable-in-the-versioned-record). Do not start the next functional step from this index.
