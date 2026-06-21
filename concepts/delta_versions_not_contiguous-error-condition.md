---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14d1cf0de64a289a60d93fb547fcb9b21d04a8f66e513af7a5606e7a0f3d6179
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_versions_not_contiguous-error-condition
    - DEC
    - DELTA_VERSIONS_NOT_CONTIGUOUS error condition
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: DELTA_VERSIONS_NOT_CONTIGUOUS error condition
description: A Delta Lake error that occurs when version numbers in the transaction log are not sequential, indicating a gap in the delta log.
tags:
  - delta-lake
  - error-messages
  - databricks
timestamp: "2026-06-18T11:57:50.459Z"
---

# DELTA_VERSIONS_NOT_CONTIGUOUS error condition

The **DELTA_VERSIONS_NOT_CONTIGUOUS** error occurs when a Delta table's transaction log is missing one or more version entries between two known versions, resulting in a non‑contiguous sequence. The Delta engine requires that the Delta log contain every version number from 0 up to the most recent version without gaps; any missing version causes this error when the engine attempts to load a version that lies beyond the gap. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Message

The full error message is:

```
DELTA_VERSIONS_NOT_CONTIGUOUS
SQLSTATE: KD00C
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Cause

The root cause is always a gap in the Delta log. Two scenarios are known to produce this condition:

- **Manual removal of files** from the Delta log directory (e.g., `_delta_log/`). If someone deletes a checkpoint file or a JSON commit file, the sequence becomes incomplete. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

- **Object store eventual consistency** (AWS S3 only). When a Delta table is deleted and quickly recreated at the same location, stale file listing caches can make the new table’s log appear non‑contiguous. This occurs because S3’s eventual consistency model may return an incomplete view of the log files for a short period. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

On Azure and other platforms only manual file removal is cited; the eventual‑consistency scenario is specific to Amazon S3. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Troubleshooting and Resolution

There is no self‑service repair for a broken Delta log. Databricks recommends contacting **Databricks support** to repair the table. The support team can reconstruct the missing commit entries or rebuild the log from the table’s current data files. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Preventive Measures

- Do **not** manually delete or move files inside the `_delta_log/` directory.
- When replacing a Delta table at the same location on AWS S3, consider using a different path or waiting for full consistency before performing operations on the new table.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open‑source storage layer that provides ACID transactions
- Delta Log — The transaction log that records every change to a Delta table
- [Delta Table](/concepts/delta-lake-table.md) — A table format built on Delta Lake
- [Delta Lake Consistency](/concepts/s3-eventual-consistency-and-delta-lake.md) — How Delta Lake maintains atomicity and isolation
- Lakehouse Architecture — The architectural pattern that combines data lake and data warehouse features

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
