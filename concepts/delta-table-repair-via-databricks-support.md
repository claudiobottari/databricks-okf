---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9d778a5e5b4065517e193c149d625ed2405ff6caffc0a67405666c601356866
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-repair-via-databricks-support
    - DTRVDS
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta table repair via Databricks support
description: The recommended remediation for a Delta table with non-contiguous log versions, requiring contacting Databricks support to repair the table.
tags:
  - delta-lake
  - recovery
  - databricks-support
timestamp: "2026-06-19T10:10:54.271Z"
---

# Delta Table Repair via Databricks Support

**Delta table repair via Databricks support** is the only documented remediation for the `DELTA_VERSIONS_NOT_CONTIGUOUS` error condition in [Delta Lake](/concepts/delta-lake.md) tables. Unlike many common issues that can be resolved with self‑service commands (such as `FSCK REPAIR TABLE` or `VACUUM`), this error requires assistance from Databricks support to re‑establish a contiguous transaction log. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Overview

The `DELTA_VERSIONS_NOT_CONTIGUOUS` error occurs when the Delta log contains a gap between versions `<startVersion>` and `<endVersion>` while trying to load version `<versionToLoad>`. The error message shows the version list and identifies the gap: “Versions (`<versionList>`) are not contiguous.” ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Common Causes

- **Manual file removal** (all cloud platforms): Files have been deleted from the `_delta_log` directory, either accidentally or by external cleanup scripts. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]  
- **S3 eventual consistency** (AWS only): When a table is deleted and re‑created at the same location, S3’s eventual consistency model can cause the Delta log to read a stale or incomplete file listing, producing a gap. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Required Action

The documented fix is to **contact Databricks support** to repair the table. Databricks explicitly states that there is no self‑service workaround; support engineers must reconstruct the contiguous version chain from the available metadata. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### What Support Does

When you file a support ticket, engineers typically:

1. Inspect the `_delta_log` directory to identify which version files are missing.
2. Rebuild or backfill the missing versions using available checkpoints and table data.
3. Validate that the repaired log is contiguous and the table loads correctly.
4. Assist with restoring the table to the required version if the gap affects [Time Travel](/concepts/delta-lake-time-travel.md) queries.

## Prevention

- **Avoid manual manipulation of the `_delta_log` directory.** All Delta log actions should be performed through Delta Lake operations (e.g., `ALTER TABLE`, `VACUUM`, `OPTIMIZE`). ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- **On AWS**, wait for S3 eventual consistency to settle before recreating a table at the same storage location. Consider using unique paths for each table copy. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- **Enable enhanced Delta logging or retention settings** (not covered by this source) to reduce the risk of accidental log deletion.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open‑source storage layer underlying these tables.
- Delta Log — The `_delta_log` directory that stores the transaction history.
- [Time Travel](/concepts/delta-lake-time-travel.md) — The ability to query historical table versions, which relies on a contiguous log.
- [VACUUM Command](/concepts/vacuum-command-databricks.md) — Safely removes old files without breaking the log.
- [Checkpoints](/concepts/asynchronous-checkpoint-save.md) — Delta’s compact representation of state that can help reconstruct missing versions.
- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — A self‑service command for other Delta issues, but **not** applicable here.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
