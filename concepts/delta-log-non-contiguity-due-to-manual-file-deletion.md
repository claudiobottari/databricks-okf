---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eba1215fe53131763c1304b5dfec15bfa10b5ea771e5e47a6d45723256ea99d9
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-log-non-contiguity-due-to-manual-file-deletion
    - DLNDTMFD
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta log non-contiguity due to manual file deletion
description: Manually removing files from the Delta transaction log can create gaps in version numbering, triggering the non-contiguous error.
tags:
  - delta-lake
  - operations
  - error-causes
timestamp: "2026-06-18T11:58:10.812Z"
---

# Delta Log Non-Contiguity Due to Manual File Deletion

**Delta log non-contiguity due to manual file deletion** is an error condition that occurs when the Delta transaction log has gaps in its version sequence, typically caused by files being manually removed from the Delta log directory.

## Error Condition

When Delta Lake attempts to load a specific table version and detects that the Delta log versions are not contiguous, it raises the `DELTA_VERSIONS_NOT_CONTIGUOUS` error (SQLSTATE: KD00C). The error message indicates that a gap was detected between two versions (`<startVersion>` and `<endVersion>`) while trying to load a specific version (`<versionToLoad>`). ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Causes

### Manual File Deletion (Primary Cause)

The most common cause of this error is the manual removal of files from the Delta log directory. Delta Lake maintains a transaction log as a series of sequential JSON files (e.g., `00000000000000000001.json`, `00000000000000000002.json`). If any of these files are deleted outside of Delta Lake's control, the version sequence becomes non-contiguous. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### S3 Eventual Consistency (AWS Only)

On AWS, this error can also occur due to [Amazon S3 eventual consistency](/concepts/s3-eventual-consistency-and-delta-lake.md) when a table is deleted and recreated at the same location. The eventual consistency model may cause older version files to appear while newer ones are not yet visible, creating the appearance of a gap. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Affected Platforms

The error can occur on all platforms, though the contributing factors vary:

| Platform | Causes |
|----------|--------|
| AWS | Manual file deletion, S3 eventual consistency with table recreation |
| Azure | Manual file deletion only |
| Generic (self-hosted) | Manual file deletion only |

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

To resolve a non-contiguous Delta log, you must contact Databricks support to repair the table. The repair process restores the missing transaction log entries or rebuilds the log structure to create a consistent version sequence. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Prevention

- **Never manually delete files** from the Delta log directory (`_delta_log/`).
- Use Delta Lake's built-in maintenance operations (e.g., `VACUUM`, `OPTIMIZE`) instead of direct file manipulation.
- On AWS, avoid deleting and recreating tables at the same location; use a different table name or location when recreating.
- Implement access controls to prevent accidental or unauthorized deletion of Delta log files.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The structured log that maintains version history
- [Delta table versioning](/concepts/delta-table-versioning.md) — How Delta Lake tracks table versions
- Delta Lake VACUUM — The safe method for cleaning up old data files
- [Delta Lake OPTIMIZE](/concepts/delta-lake-optimized-writes.md) — The safe method for compacting files
- [S3 Consistency Model](/concepts/s3-eventually-consistent-model.md) — AWS-specific consistency behavior that can affect Delta operations

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
