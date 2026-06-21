---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c155e41bd872c1f9e7e8bfb6d9d053f07b1176531b17b5b0ba46421127584193
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-log-file-removal
    - DLFR
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta Log File Removal
description: Manual deletion of transaction log files from the Delta log directory, a primary cause of the non-contiguous version error across all cloud platforms.
tags:
  - delta-lake
  - operations
  - data-loss
timestamp: "2026-06-19T15:09:47.410Z"
---

# Delta Log File Removal

**Delta log file removal** refers to the manual deletion of transaction log files from a [Delta Lake](/concepts/delta-lake.md) table's `_delta_log` directory. This action corrupts the table by creating gaps in the version history, leading to query failures and data inaccessibility. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Overview

Delta Lake maintains a transaction log in the `_delta_log` directory that records every change made to a table. Each change corresponds to a sequentially numbered JSON file (e.g., `00000000000000000001.json`). When these files are manually removed, the version sequence becomes non-contiguous, and Delta Lake cannot reconstruct the table state at certain versions. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Condition

When a gap in the delta log is detected, Delta Lake raises the `DELTA_VERSIONS_NOT_CONTIGUOUS` error condition (SQLSTATE: KD00C). The error message identifies the specific gap:

```
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Common Causes

### Manual File Deletion

The most common cause is when users or automated processes manually delete files from the `_delta_log` directory. This can happen during cleanup operations, storage management, or accidental deletion. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### S3 Eventual Consistency (AWS Only)

On AWS, the error can also occur due to [S3 eventual consistency](/concepts/s3-eventually-consistent-model.md) when a table is deleted and recreated at the same storage location. The eventual consistency model may cause the new table's log files to appear before all old log files have been fully removed, creating apparent gaps. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Impact

- **Query failures**: Queries that attempt to read the affected version or any version that depends on the missing log entries will fail.
- **Time travel breaks**: [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) becomes unreliable or impossible for versions that fall within the gap.
- **Table corruption**: The table may become partially or fully unreadable depending on the extent of the log removal.

## Resolution

Databricks support must be contacted to repair the table. There is no self-service mechanism to fix a non-contiguous delta log. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

- **Never manually delete files** from the `_delta_log` directory. Use Delta Lake's built-in VACUUM command for safe log cleanup, which respects version contiguity.
- **Avoid deleting and recreating tables** at the same S3 location. Use a different path or ensure complete cleanup before recreation.
- **Implement access controls** on the `_delta_log` directory to prevent accidental deletion by users or automated processes.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The core logging mechanism that Delta Lake uses to track table changes.
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) — The ability to query previous versions of a Delta table, which depends on a contiguous log.
- VACUUM — The safe way to clean up old Delta Lake files without breaking version contiguity.
- DELTA_VERSIONS_NOT_CONTIGUOUS error|DELTA_VERSIONS_NOT_CONTIGUOUS — The specific error condition raised when log gaps are detected.
- [S3 Eventual Consistency](/concepts/s3-eventually-consistent-model.md) — AWS-specific behavior that can cause this error under certain conditions.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
