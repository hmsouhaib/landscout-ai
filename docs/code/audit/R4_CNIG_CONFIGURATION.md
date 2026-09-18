# DOCS.CONTINUITY.1.R4 — CNIG configuration fidelity

Status: bounded two-row implementation complete; validation/publication gates
recorded below. Global audit **PARTIAL**; independent R4 review **PENDING**.
No application/config/test change or official/legal certification.

## Authority, readiness and prior review

Authority: [exact R4 ticket](../../project/tickets/DOCS.CONTINUITY.1.R4.txt),
attachment `fda3e856-7f31-46b9-bab9-4ef9fe9ed8e2/pasted-text.txt`.
Archived raw bytes and attachment SHA256:
`10aa74b8ee29811641597ebbdac15d4d8eef3833e55aff8c874099c2ae80a23a`.
Section 1 is the supplied ChatGPT read-only reviewer statement, not a fresh
Codex execution or an unavailable signed document.

Starting root `C:/souhaib/landscout-ai`, clean branch
`recovery/docs-continuity-1-partial`; HEAD, local tracking recovery and actual
remote recovery all `e89f7f176f7bc3369977055aceb6423b882d3429`.
Local/actual remote main `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`.
No unmerged index entries or operation markers. Sandbox ls-remote could not
connect to GitHub. Native explicit-root Git reproduced the known ownership
mismatch; only then the authorized command-scoped
`-c safe.directory=C:/souhaib/landscout-ai` remote query succeeded. No fetch,
persistent trust/ACL/security/dependency changes, reset or history rewrite.

R4 section 1 approves R3.1 at the starting SHA, parent
`aad641420c0b0d2c8c503815854ae9c17f4d09f4`, within planning documentary-fidelity
correction only. It checked seven-path publication/diffs, corrected anchors and
owner mapping, and fixture/call-order/scope notices against source/test evidence.
It did not freshly execute 183 tests, the full INDEX checker, all 206 mappings,
complete snapshot recalculation, visual rendering, A-003 or official GPU/EP data.
[CURRENT_STATE](../../project/CURRENT_STATE.md) records that successor approval;
unchanged [R3](R3_PLANNING_FEATURES.md) and [R3.1](R3_1_PLANNING_FIDELITY.md)
receipts preserve history. Receipt of a verdict adds no closure count.

## Actual ownership and exact progress

Parsed the original [matrix](recovery_file_matrix_2026-09-17.json) and all six
existing review fragments by exact path. For these two paths the matrix names
[planning.json](reviews/planning.json), and only that fragment contains an
explicit file row. Its old `transferred_to: inpn_roads extension` note was an
unmaterialized transfer intention: the extension contains only the four other
planning-feature rows from R3. No new extension record, duplicate closure or
global-ledger rewrite is appropriate. Both previous records/evidence are retained
under r4_prior_evidence; only these two operational records change.

| Original path | Starting status/read_complete | Final status/read_complete | Symbols |
|---|---|---|---:|
| configs/planning/cnig_plu_2017_feature_codes.yaml | NOT_READ / false | CHECKED / true | 0 |
| docs/code/files/configs/planning/cnig_plu_2017_feature_codes.yaml.md | NOT_READ / false | CORRECTED / true | 0 |

Starting YAML SHA256:
`77407429fd414eece8f6b20ca4da587aac76ab6b0b93e02f148622ab85ee253e`.
Starting companion SHA256:
`91a88465643f319a5d55da18ebc5d6e6155e031fb3e8e9581204dfc5d3b94244`.
Final companion SHA256:
`57ba6adf300e215302bf21ef1130ae79824b0215294422fc3ee58eb9c382c005`.

Deduplicated original-scope arithmetic: 71 + 2 = **73/245 files**;
**1,594/4,769 symbols** unchanged; **172 files / 3,175 symbols** pending.
File totals CHECKED 27, CORRECTED 46, READ 141, NOT_READ 31; symbol totals
CHECKED 1,593, CORRECTED 1, READ 2,078, NOT_READ 1,097. The larger current Git
candidate and new ticket/receipt are not the original denominator. No resolver,
test or other companion row is promoted by dependency reading.

## Source-derived reading and corrections

Read the entire 94-line YAML and entire prior 637-line companion, including
all generic leaf rows, model/consumer sections, readable snapshot and base64
payload; exact repeated snapshots are compared mechanically as well.
Read AGENTS, working rules, current state, relevant step/decision/backlog records,
resume route, technical architecture/data flow/planning pipeline, current audit
and R3/R3.1 receipts before editing.

Exact implementation/dependency reading (line numbers in unchanged starting files):

- `src/landscout/stages/resolve_planning_feature_codes.py` 1–1177: complete
  source read to trace the configuration; field models/text checks 51–239,
  loader 242–259, supplied-profile reconstruction 292–307, dictionary/result
  validation 334–529, lookup/propagation 550–647, canonical result hash payloads
  650–885, builder 888–968, intrinsic/public validators and resolver 971–1177.
  This is not a full per-symbol audit/closure of that separate source unit.
- `src/landscout/common/strict_yaml.py` 1–60: entire decoder, including merge
  flattening, duplicate/unhashable-key checks, UTF-8 and controlled exceptions.
- `tests/unit/test_resolve_planning_feature_codes.py` 1–338, 523–925,
  1593–1854, 2101–2295: imports, hash/record/profile helpers, synthetic physical
  inventory/GPKG/manifest helpers, test-local wrappers, relevant configuration,
  selection, reconstruction, preservation, schema and intrinsic-meaning tests.
  Extra lines 2296–2305 were displayed as context only; no complete audit of
  the remaining test file or automatic status promotion.
- `tests/unit/test_deep_immutability.py` imports/constants 1–75; loaded-family
  factory and recursive field traversal 300–354; AOI sequence/structure mapping
  mutation tests 356–424; alias/hash tests 434–482. Adjacent artifact fixture
  context was read, not audited as a new unit. CNIG graph/hash checks are not
  a dedicated CNIG alias or immediate sequence-mutation regression.
- `tests/unit/test_strict_serialization.py` 1–23: nested YAML duplicate and
  safe-loader behavior; no attribution of strict-JSON nonfinite tests to YAML.
- `src/landscout/stages/bess_planning_feature_policy.py` 542–700, 1007–1070:
  source locks, dictionary/policy exact-pair completeness/meaning comparison,
  policy-table fields, source-complete delegation and compiler. No policy YAML
  inventory review or business-rule interpretation.
- Reference search located stage reexports and profile consumers in application/
  aggregation, not a claim to have audited those modules. DEV_LOG 4057–4156
  was read for reported 7D.5A/7D.5A.1 endpoint inspection and v2 display correction,
  not as a newly executed official-source check.

The [replacement companion](../files/configs/planning/cnig_plu_2017_feature_codes.yaml.md)
explains all 8 root fields, 2 nested URL fields, 7 record fields and 92 leaves;
all 12 exact records; 24 legal/annex cells (22 text, 2 null); and 14 URL occurrences
(2 root + 12 record, 2 distinct family endpoints). It preserves literal codes,
case/accents/punctuation, endpoint association and meaningful record order.

Concrete corrections: remove generic validator prose and unrelated road/scan/CRS
boilerplate; correct the former “Hashing: none” assertion (records are hashed
during validation, raw YAML bytes are not); distinguish date parsing from strict
string fields and frozen/tuple models from model-wide strict mode; explain
required nullable references, true null versus text, literal 00/no fallback,
canonical official text versus raw LIBELLE/A-003, exact runtime API and separate
intrinsic/physical boundaries. The old companion was already schema 2 with 12
records; no nonexistent schema-1/six-row defect is claimed.

Historical table-inspection and approved-display wording in DEV_LOG is retained
as reported provenance. No external table/PDF/current law was read in R4; a
retained external-table byte capture and full original review receipt are not
established by the read evidence. Model/hash acceptance is internal consistency,
not independent current legal verification or complete nomenclature coverage.

### Existing tests: bounded claims only

The companion links actual test definitions with literal setup/assertion limits.
The no-fallback test removes PRESCRIPTION 07/04 and INFORMATION 99/00 and checks
unknown retention; it does not create a competing same-code other-family record
or check every null meaning field. The malformed-profile-code parametrization
attacks type_code only. Endpoint mutation changes both root and record fields,
so nested errors need not isolate one guard. Duplicate YAML fails before the
unsupported schema; duplicate/order validators precede record-hash comparison.
The test _records_hash sorts fixture records, whereas production preserves order.
In-memory profile rejection precedes resolver physical validation, but fixtures
already performed synthetic local IO. Immutable graph/hash tests include CNIG;
dedicated alias/immediate sequence-operation cases use other model families.
Missing direct cases are limitations, not automatic production findings.
No pytest was run; no historical pass count is presented as a fresh R4 execution.

## Actual offline load and three hashes

Existing `.venv/Scripts/python.exe -B -X utf8 -` loaded this path through the
existing loader **once**; existing _records_sha256/_profile_sha256 helpers were
used. Native exit 0; load call 0.005550700001549558 seconds (not a benchmark).
Observed count 12, INFORMATION 4/PRESCRIPTION 8. Root runtime types:
schema_version int; profile/standard_model/official_text_normalization/
canonical_records_sha256 str; official_sources OfficialSourceUrls;
retrieval_date date; records tuple. Both endpoint fields are str. All record
fields are str except legal_reference/regulation_or_annex_reference, each with
str and NoneType values.

- YAML Git-content SHA256:
  `77407429fd414eece8f6b20ca4da587aac76ab6b0b93e02f148622ab85ee253e`.
- Ordered seven-field record payloads, UTF-8 canonical JSON SHA256:
  `5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c`.
- Complete JSON-mode profile including metadata, date and records SHA256:
  `5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee`.

A process-local audit hook rejected socket events except local gethostname and
socket construction; only `socket.gethostname` occurred during dependency import.
Zero DNS/HTTP/network requests; no persistent source/config/artifact write.
An initial overly broad hook blocked local gethostname in Pandas/platform import
before the loader was called (exit 1). Allowing that local introspection yielded
the single actual load above; no loader failure was hidden, no dependency changed.
An initial JSON-transport read of the very long old companion was truncated;
it was discarded and reread without JSON escaping before applying any edit.

<a id="r4-application-finding"></a>

## A-004 — optional reference model/result mismatch, OPEN

Source evidence: record optional-text checks at 120–123/160–165 accept any
nonempty canonical text; result guard at 360–368 rejects the three exact strings
None/nan/<NA>. After the single successful load, this bounded no-I/O check ran:

```python
r = profile.records[3].model_dump(mode="python")
r["legal_reference"] = "None"
accepted = CnigFeatureCodeRecord.model_validate(r)
# accepted.legal_reference == "None" (str)
_validate_nullable_official_value(accepted.legal_reference, "legal reference")
# PlanningFeatureCodeError: legal reference contains a literal null replacement
```

Here profile denotes the already loaded checked-in object; only its separate
dump was mutated. Existing helper/model names are imported from the resolver
module. The controlled expected exception was caught/printed, process exit 0.
This is **record-model versus intrinsic helper** evidence, not a full rehashed
profile, public resolver, official GPU row or legal assertion. The same source
guard covers nan/<NA>, not separately executed. Current YAML uses real nulls.
The narrow [backlog addition](../../project/BACKLOG_AND_GAPS.md#application-findings)
preserves the discrepancy for separate review/corrective authority. A-001/A-002/
A-003 and all earlier test-evidence limits remain OPEN; no raw-label repair.

## Preservation, mechanics and rendering

Pre-staging scoped check **PASS**, process exit 0: all **106 original protected
paths** match recorded original Git blobs, index SHA and raw-checkout SHA;
all **279 out-of-scope starting paths** match their starting Git/raw bases out
of 284 starting tracked paths. The only raw/Git differences remain the recorded
Muret written-zoning YAML and old resume ticket EOL exceptions, byte-verified
without rewriting. No code/config/test/dependency/tool/cache/source/artifact or
old receipt/archive/global ledger changed. Exactly seven documentation paths
are in scope, including the justified A-004-only backlog line.

Strict fragment JSON passed; exactly the two intended file records changed,
all other rows and top-level fragment data remain equal. Reconciled file totals
and next NOT_READ identity agree with the original matrix plus existing R3 and
these two R4 operational records, without merging coverage.json. Source and
companion owner fingerprints match actual bytes. New and old complete YAML
fences and old base64 payload each reproduce all **4,934** exact Git bytes.
All **92 leaves / 12 × 7 record values**, endpoint associations and actual public
signatures match the source. **9 explicit IDs are unique** (8 companion + 1
receipt), **85 local links** resolve to existing intended owners/anchors, and
**69 table lines**, fences and delimiters pass scoped static checks.
The verification used existing auditor Markdown/index helpers plus read-only
stdin comparisons, not another checked-in checker or a full auditor invocation.

New worktree `git diff --check` exit 0. Cumulative main-to-worktree comparison
exits 2 with stdout/stderr identical to main-to-start: exactly **13 inherited**
observations, twelve cold-start Markdown hard breaks (29, 32, 39, 42, 47, 50,
53, 56, 59, 73, 97, 102) and the original continuity ticket's final blank line
(1036). No archive rewrite or suppression. Staged checks are recorded below.

Unchanged resolver SHA256:
`cdb463f06cea6f58881681bca7e95e80b0770e69f4cdf3cc373329eca7bc0235`.
Unchanged resolver-test SHA256:
`f089c7cf174ecf5fa745d5909f817884a6c9df6d52f0e53f8702a639106e574c`.
Unchanged strict-YAML SHA256:
`2affe2cb67de83b4c493d6df1567d4f6809464a86fd47b57fcff48da99a9acc5`.

Rendering discovery rerun: pandoc/markdown/marked/node absent from PATH; existing
Python environment has no markdown/markdown_it/mistune/docutils. The earlier
VS Code-extension observation is historical, not a newly exercised renderer.
No visual rendering performed, no dependency installed or content uploaded;
visual acceptance remains pending. Static checks are not a visual pass.

## Staged INDEX auditor and publication boundary

The seven explicit paths were staged and independently checked as INDEX bytes:
the same 106/279 protection comparisons, two-row scope, snapshot/field values,
9 IDs, 85 links and 69 table lines passed, process exit 0. New working and staged
`git diff --check` both exited 0. The unchanged auditor ran **once**:

```text
.venv\Scripts\python.exe -B -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r4-candidate.stdout.txt
```

**Process exit 1**, `completed=true`, **10,266 findings**: completed PARTIAL
check, not exit 2, interruption or a claim of a clean global audit.
Candidate manifest SHA256:
`7df2d931050fd92e27d3d561acb1c9229a8d87c9043d6e6414fbec75b1b1597e`.
**286 files, 283 unique blobs, 29,087,633 per-path content bytes**;
94 Python files / 94 AST parses / 4,863 enumerated symbols; original global
coverage remains 245 files / 4,769 symbols. Five Git processes, non-shallow
history, unchanged index postcondition. Tool wall time 2.3090175 s includes
launcher/output overhead, not a benchmark. Phase seconds: index 0.226413,
coverage-input 0.010852, Python 0.836676, checkout-Markdown 0.285141,
coverage 0.129397, references 0.139073, history 0.115510,
index-postcondition 0.037370.

Findings grouped from the actual sorted stdout: **5,034 coverage/staleness**,
**216 mechanical**, **5,016 pending recorded acceptance**. Compared with the
retained R3.1 stdout, the YAML's ambiguous line-ending-basis diagnostic disappears;
the changed companion gains a stale fingerprint in the intentionally unmerged
original global ledger; the inventory line gains this exact ticket archive.
All other lines are unchanged. No new bad link/qualified-reference diagnostic
was introduced. Existing global findings, including the earlier literal-domain
scanner findings, remain reported; no checker change or suppression.

Detailed stdout remains outside Git, PowerShell UTF-16:
`C:\souhaib\r4-candidate.stdout.txt`, **2,315,636 bytes**, SHA256
`5678a84694564d1d52c1211050cc3bbb7cbb5b140830e2f51f8c71e4f9c71f0f`.
Exact sorted path/mode/blob entries are retained outside Git in
`C:\souhaib\r4-candidate.manifest.json` (PowerShell UTF-16); their compact
ASCII-safe JSON serialization without terminal newline reproduces the manifest
digest above. The verbose progress display was truncated by the tool output
budget, but its terminal metrics and process exit were returned; stdout is
complete and independently counted, not inferred from partial progress.

**Only this receipt is completed after that full run.** Its later bytes are not
retroactively in the checked candidate. Final scoped checks separately cover
that precise one-path manifest delta, this receipt's links/fences, the seven-path
publication scope, all protected/out-of-scope bytes and current owner/snapshot
bindings. No second full auditor or application/test run. Cumulative whitespace
remains the same thirteen inherited observations; the new staged delta is clean.

## Stop and next queue item

Publish recovery only with `docs: audit CNIG feature code configuration reference`,
verify clean tree/local-tracking-actual recovery equality and unchanged actual
main, then stop for independent R4 review. No self-approval or next unit.
The next actual preserved NOT_READ path is
`configs/planning/muret_bess_cnig_feature_policy.yaml`; identified, not started.
Global audit, visual/cold-start acceptance, final full-suite validation, original
application findings and EP semantic review remain pending.
