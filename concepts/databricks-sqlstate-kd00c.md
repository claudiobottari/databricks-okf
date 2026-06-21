---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4542e536d5151c657ec6e6b5290534ca20ceaaf226f850d4b95a2ed87b872fb
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sqlstate-kd00c
    - DSK
    - Databricks SQL States
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Databricks SQLSTATE KD00C
description: The SQLSTATE class KD00C that categorizes datasource-specific errors within Databricks, including the DELTA_VERSIONS_NOT_CONTIGUOUS error.
tags:
  - databricks
  - error-messages
  - sql
timestamp: "2026-06-18T15:25:47.854Z"
---

# Databricks SQLSTATE KD00C

**SQLSTATE KD00C** is a Databricks-specific error condition associated with the `DELTA_VERSIONS_NOT_CONTIGUOUS` error class. This error occurs when Delta Lake detects a gap in the Delta transaction log, meaning that the versions of a Delta table are not in a contiguous sequence. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Message

The error message typically appears as:

```
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Causes

The `DELTA_VERSIONS_NOT_CONTIGUOUS` error can be caused by the following scenarios:

### File Removal
Files have been manually removed from the Delta log directory (`_delta_log`). This disrupts the sequential version numbering that Delta Lake relies on for transaction management. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### AWS S3 Eventual Consistency
On AWS, this error can occur due to Amazon S3's eventual consistency model when a Delta table is deleted and then recreated at the same storage location. The inconsistency can cause the Delta log to reference versions that no longer exist or are out of order. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

In all cases, the recommended resolution is to contact Databricks support to repair the table. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

| Cloud | Cause | Action |
|-------|-------|--------|
| AWS | Manual file removal or S3 eventual consistency | Contact Databricks support |
| Azure | Manual file removal | Contact Databricks support |
| Generic | Manual file removal | Contact Databricks support |

## SQLSTATE Classification

KD00C belongs to **Class KD** in Databricks' SQLSTATE classification, which covers datasource-specific errors. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that manages Delta tables and their transaction logs
- [Delta transaction log](/concepts/delta-transaction-log.md) – The `_delta_log` directory containing versioned JSON files
- Delta Table Maintenance – Regular operations to keep Delta tables healthy
- SQLSTATE Error Codes – The complete list of Databricks SQLSTATE error codes
- [Delta Log Repair](/concepts/delta-table-repair.md) – The process of fixing a corrupted or inconsistent Delta log
- [S3 Eventual Consistency](/concepts/s3-eventually-consistent-model.md) – The AWS storage consistency model that can trigger this error

## Best Practices

To prevent the DELTA_VERSIONS_NOT_CONTIGUOUS error:

- **Avoid manual file operations** on the `_delta_log` directory. All Delta table operations should go through the Delta Lake API. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- **Use proper table lifecycle management** rather than deleting and recreating tables at the same path. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- **Enable Delta table retention** settings such as `delta.logRetentionDuration` to allow time for recovery before old log files are cleaned up.

> **Note**: The source material does not provide specific instructions for repairing the table manually. Users should rely on Databricks support for accurate repair procedures.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
