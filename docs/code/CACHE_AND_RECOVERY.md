# Cache and recovery behavior

## Terms

- Final archive/data path: bytes available to a verified cache hit.
- Metadata sidecar: JSON lineage/integrity record stored beside the final file.
- `.part`: temporary archive or metadata written before publication.
- `.bak`: recovery copy retained during pair replacement/rollback or after an unrecoverable double failure.
- Cache hit: returned only after current physical bytes and sidecar satisfy the adapter contract.
- Manual recovery state: any existing recovery backup/link/junction that stops automatic cache/network work.

The adapters share safety principles but not identical cache layouts, metadata schemas, expiry rules, archive formats, or extraction implementations. Every trust-bearing JSON sidecar/marker is parsed through the shared duplicate-rejecting, finite-number, strict-UTF-8 object decoder before its source-specific schema is validated.

## Cadastre

### Paths and hit/miss

The caller supplies a cache directory. The archive filename is derived from the official commune URL; metadata is `<filename>.metadata.json`. A cache hit requires a current regular archive and sidecar, matching URL/filename/size/SHA/timestamp, a valid gzip, and configured maximum age. An expired or invalid pair is a miss, but existing valid final files remain available during replacement.

### Publication sequence

1. Fail before cache/network if either `<archive>.bak` or `<metadata>.bak` exists or is a symlink, broken symlink, or junction.
2. Check the existing cache.
3. Create the parent and prepare both `.part` paths. An ordinary stale file may be removed; link/junction/directory/nonregular paths fail closed.
4. Stream exact HTTPS bytes into the archive `.part` with exclusive creation.
5. Validate gzip and compute size/SHA/result lineage.
6. Write metadata `.part` exclusively.
7. Recheck absence of recovery material, copy existing final files to `.bak`, and replace archive then metadata.
8. On success, delete obsolete backups.
9. On publication failure, remove any newly published half and restore old files. Successful rollback removes backups; rollback failure raises a controlled error and preserves remaining backup bytes.
10. Cleanup attempts both `.part` files. A cleanup error cannot replace an active rollback error; if cleanup is the sole failure it becomes `CadastreDownloadError`.

The next run after a double failure sees recovery material before cache/network and leaves it untouched.

## RTE / ODRÉ

### Paths and hit/miss

The caller supplies a cache root; each configured dataset uses `<dataset_id>.geojson` and a metadata sidecar. A hit validates age, config/dataset/source URL, metadata, physical size/SHA, recursive GeoJSON geometry/coordinate structure, export summary, and record-count agreement.

### Network and publication sequence

Recovery and `.part` checks occur before either network operation. On a miss the adapter requests current ODRÉ dataset metadata, constructs the exact export URL, streams GeoJSON, validates it, and writes the lineage sidecar. Pair publication/rollback/cleanup follows the same recovery-preserving rules as Cadastre. Therefore a manual recovery state performs zero metadata requests and zero export requests.

## IGN BD TOPO

### Download cache

The configured source cache root includes the archive filename and JSON metadata. The sidecar binds schema/config/source identity, timestamp, size, SHA/checksum, and cache status reconstruction. Cache reuse rechecks physical bytes and archive validation; pinned checksum/size/config lineage cannot be replaced by a coordinated sidecar mutation.

The pair publisher fails closed on stale `.bak`, uses safe/exclusive `.part` paths, preserves backups after publication-plus-rollback failure, and prevents cleanup from masking the primary failure. A valid cache hit also stops before DNS/HTTP.

### Extraction cache

Extraction uses a deterministic directory and marker. The marker binds archive identity, GeoPackage relative path, byte size/SHA, layer inventory, globally distinct configured logical roles, and schema. Cache reuse verifies the marker and current GeoPackage bytes. Before rebuild, a pre-existing `.bak` of any path kind stops work for manual recovery, and a `.part` path must be proven non-linked and transaction-safe. The complete Windows-compatible 7z destination inventory is validated before extraction and exact-compared with the actual extracted inventory. Publication moves the old directory to `.bak`; success removes the transaction backup, rollback restores the old tree, and a failed rollback preserves recovery material for the next fail-closed run.

## GPU

### Download cache

GPU archive cache identity includes the validated document identity and official partition/document provenance. The sidecar and physical archive must agree on exact size/SHA and ZIP validation. `.bak`, `.part`, exclusive publication, rollback, cleanup precedence, and next-run manual-recovery behavior follow the hardened pair contract, but the metadata fields are GPU-document-specific.

### Extraction cache

The extraction marker inventories every extracted regular file with path/category/size/SHA and archive identity; the enclosing extraction retains the source document through its archive object. A hit rescans the directory and exact-compares inventory. Rebuild validates the complete ZIP member set before copying, requires link/junction-safe temporary paths, extracts manually under a temporary root, writes/verifies the marker, and transactionally replaces the prior directory. A pre-existing extraction `.bak` stops the run; rollback failure preserves it. Planning spatial source validation subsequently rechecks the planning document's canonical config hash, actual physical files, and globally unique configured layer roles; an extraction cache hit alone is not the final planning-stage trust proof.

## INPN / PatriNat

### Download cache

The versioned path is under configured `.cache/landscout/inpn/protected_areas`, dataset `EP`, declared-version segment, and `EP.zip`; the sidecar is adjacent. Cache metadata schema remains `1`. A hit requires exact config identity, expected 99,835,011 bytes, expected SHA256, current physical bytes, strict timestamp/metadata, and complete ZIP validation. There is no age-based refresh for this pinned snapshot.

Download publication writes archive/metadata `.part` files, validates configured pins before publication, and uses a recovery-preserving pair transaction. Backup detection includes ordinary paths, symlinks, broken symlinks, and junctions. Unlike blindly deleting stale recovery material, the publisher raises `InpnProtectedAreasSourceError` and leaves operator-recoverable bytes untouched.

### Extraction cache

The extraction root is content-addressed below the versioned cache. Marker schema `1` binds archive SHA/size and a lexically ordered list of every regular file's canonical relative path, size, and SHA. Reuse rejects links/junctions, special files, missing/modified/renamed/extra files, malformed marker paths, order/type/hash drift, or archive mismatch. Rebuild validates all ZIP members before copying any, extracts with exclusive targets, inventories and revalidates, then publishes the directory transactionally.

## Recovery state is not a cache miss

A cache miss means the adapter may safely acquire/rebuild. A `.bak` recovery state means the previous transactional outcome requires human inspection. Treating it as an ordinary miss could overwrite the only good copy. Current adapters therefore stop before network where their recovery contract requires it.

## Security and non-goals

Path checks prevent cache publication from following attacker-controlled symlink/junction redirection. Recovery logic protects byte availability and transactional consistency; it does not certify the real-world truth of a source, interpret its business meaning, or decide parcel suitability.
