---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11fefc388989c3f262808800b8476f757942bbebc348eee7fbe10070bcaf88b7
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-repair
    - DTR
    - Delta Lake table repair
    - Delta Log Repair
    - Delta Table Upgrade
    - Table Repair
    - Table repair
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta Table Repair
description: The recommended remediation for a non-contiguous Delta log, requiring contacting Databricks support to repair the table.
tags:
  - delta-lake
  - operations
  - recovery
  - databricks
timestamp: "2026-06-19T15:09:48.565Z"
---

# Delta Table Repair

**Delta Table Repair** refers to the process of restoring a [Delta Lake](/concepts/delta-lake.md) table whose transaction log (the Delta log) has become non‑contiguous, typically due to manual deletion of log files or cloud‑storage consistency issues. A table in this state cannot be read or written until the log is repaired.

## Cause

The `DELTA_VERSIONS_NOT_CONTIGUOUS` error occurs when the Delta log has a gap between two consecutive versions. The error message identifies the range of missing versions (`<startVersion>` to `<endVersion>`) and the version the system was attempting to load. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

Common causes include:

- **Manual removal of Delta log files** from the storage location (e.g., deleting `.json` files in the `_delta_log` directory). This is the primary cause across all cloud environments. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- **S3 eventual consistency** (AWS only) when a table is deleted and recreated at the same storage location. After deletion, the underlying log files may not be immediately visible, leading to a perceived gap. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

Databricks does not expose a public repair command for non‑contiguous logs. To repair the table, users must contact Databricks support and request assistance. Support can analyze the log structure and restore contiguity, for example by rebuilding missing metadata or compacting the log. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

Users should not attempt to manually edit or re‑create log files, as this can further corrupt the table. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

To avoid the need for table repair:

- Never manually delete files from the `_delta_log` directory.
- When using AWS S3, avoid deleting and recreating a Delta table at the same path. Instead, use `DROP TABLE` and then `CREATE TABLE` with a different location, or overwrite the table data using [Delta Lake`s `OVERWRITE` semantics](/concepts/delta-lake-dml-statements.md).

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open‑source storage layer that provides ACID transactions on data lakes.
- Delta Log — The transaction log that records all changes to a Delta table.
- [S3 Eventual Consistency](/concepts/s3-eventually-consistent-model.md) — A characteristic of AWS S3 that can cause temporary inconsistencies after object deletions.
- [Delta table versioning](/concepts/delta-table-versioning.md) — How Delta Lake maintains table snapshots through sequential version numbers.
- DELTA_VERSIONS_NOT_CONTIGUOUS error|Error Condition: DELTA_VERSIONS_NOT_CONTIGUOUS — The specific error raised when a log gap is detected.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
