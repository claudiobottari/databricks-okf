---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a0f34e6ffdf4b64b52cde61d99378b9c7357e8dd326175385048a3aa7a83b2b
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-delta-log-tampering
    - MDLT
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Manual Delta log tampering
description: Manually deleting or removing files from the Delta transaction log directory can corrupt the table by creating version gaps.
tags:
  - delta-lake
  - operations
  - best-practices
timestamp: "2026-06-18T15:25:33.817Z"
---

# Manual Delta log tampering

**Manual Delta log tampering** refers to the unauthorized or accidental removal, modification, or deletion of files from the Delta transaction log directory (`_delta_log/`), which causes the Delta Lake protocol to detect non-contiguous version sequences and fail with a `DELTA_VERSIONS_NOT_CONTIGUOUS` error. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Condition

When Delta Lake encounters a gap in the commit log between two consecutive versions, it raises the `DELTA_VERSIONS_NOT_CONTIGUOUS` error. The full error includes a list of available versions, the start and end versions of the detected gap, and the version the reader was attempting to load. The SQLSTATE for this error is `KD00C`. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Common Causes

### Manual File Removal

The most common cause is when files have been manually removed from the Delta log directory. Delta Lake relies on an ordered, contiguous sequence of JSON commit files (e.g., `00000000000000000001.json`, `00000000000000000002.json`) in the `_delta_log/` folder. If any intermediate file is deleted, Delta Lake cannot reconstruct the table state at that version and raises the error. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### S3 Eventual Consistency (AWS only)

On AWS, S3 eventual consistency can cause this error pattern when a table is deleted and recreated at the same S3 path. During the window of inconsistency, readers may see stale or incomplete versions of the Delta log, creating a perceived gap. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Recovery

Delta Lake does not provide a built-in repair command to recover from log gaps. To repair the table, contact Databricks Support or your cloud provider's support team for assistance. Support engineers can reconstruct the missing commit files or recommend alternative recovery strategies. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

To prevent manual log tampering:

- Avoid direct filesystem operations on the `_delta_log/` directory.
- Use Delta Lake APIs (Spark SQL, DeltaTable API, or Delta Sharing) for all table modifications.
- Implement [Delta Lake table access controls](/concepts/table-access-control-tacl.md) to restrict who can modify table metadata.
- Monitor the Delta log directory for unexpected file deletions using cloud storage audit logs.
- On AWS, use S3 strong consistency features to reduce the risk of consistency-related version gaps.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The ordered record of all changes to a Delta table.
- [Delta Lake versioning](/concepts/delta-table-versioning.md) — How Delta Lake tracks table states through contiguous commit versions.
- DELTA_VERSIONS_NOT_CONTIGUOUS error|DELTA_VERSIONS_NOT_CONTIGUOUS — The specific error class for this condition.
- [Delta Lake table repair](/concepts/delta-table-repair.md) — Procedures for recovering from corrupted Delta logs.
- [Delta Lake best practices](/concepts/delta-lake-general-best-practices.md) — Guidelines for maintaining Delta table integrity.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
