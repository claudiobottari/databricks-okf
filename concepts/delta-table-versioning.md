---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4732298fd636a0d12bdb99c72652e4d736e23aeb06c86892a9e6c66e4b57442
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-table-versioning
    - DTV
    - Delta Lake Versioning
    - Delta Lake versioning
    - DeltaLog Versioning
    - Table Versioning
    - table versioning
    - Delta Lake version
    - Feature Table Versioning
    - Immutable Versioning
    - S3 Versioning
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta table versioning
description: The mechanism by which Delta Lake maintains sequential, atomic versions of a table through ordered commits in the transaction log.
tags:
  - delta-lake
  - versioning
timestamp: "2026-06-19T18:29:05.358Z"
---

# Delta Table Versioning

**Delta table versioning** is a core feature of the [Delta Lake](/concepts/delta-lake.md) storage format that enables time travel, audit history, and transactional consistency through an ordered sequence of table versions. Each write, update, delete, or merge operation on a Delta table creates a new version, allowing users to query, roll back, or inspect the table at any point in its history. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## How Versioning Works

Delta Lake maintains table versions through a transaction log (the `_delta_log` directory) stored alongside the table data. Each operation that modifies the table appends a new JSON or Parquet file to the log, incrementing the version number. The log files are numbered sequentially (e.g., `00000000000000000001.json`, `00000000000000000002.json`) and record which data files are part of that version. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

When reading a Delta table, the engine reads the latest version from the log to determine which data files constitute the current table state. Users can also specify a particular version or timestamp to read the table at a specific point in history, enabling [time travel](/concepts/delta-lake-time-travel.md) queries. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Version Contiguity Requirement

For Delta Lake to function correctly, the version log must be contiguous – every version between the first and the latest must have a corresponding log entry. If a gap exists in the sequence of version numbers, Delta Lake cannot reconstruct the table state correctly and raises an error. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## DELTA_VERSIONS_NOT_CONTIGUOUS Error

The `DELTA_VERSIONS_NOT_CONTIGUOUS` error occurs when Delta Lake detects a gap in the delta log between two versions. The error message identifies the specific range of missing versions and which version the system was attempting to load. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Causes

The error can arise from two primary causes: ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

**Manual file removal**: Files from the Delta log (`_delta_log` directory) have been manually deleted, either by a user or an automated process. This is the most common cause on all platforms. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

**S3 eventual consistency**: On AWS, if a table is deleted and quickly recreated at the same location, S3's eventual consistency model may cause old log files to appear alongside new ones, creating gaps or conflicts in the version history. This applies only to AWS deployments. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Resolution

To resolve a `DELTA_VERSIONS_NOT_CONTIGUOUS` error, users must contact Databricks support to repair the table. The repair process restores the contiguous version history by reconciling the log files. There is no user-facing tool to directly fix this condition. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Best Practices to Avoid Versioning Issues

- Never manually delete files from the `_delta_log` directory. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- When deleting and recreating a table on AWS, wait for S3 eventual consistency to settle before writing to the same location. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- Use Delta Lake's built-in VACUUM and OPTIMIZE commands rather than manual file manipulation. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Lake architecture
- [Time travel](/concepts/delta-lake-time-travel.md)
- [Transaction log](/concepts/delta-transaction-log.md)
- Delta Lake VACUUM
- [Delta Lake OPTIMIZE](/concepts/delta-lake-optimized-writes.md)
- [S3 eventual consistency](/concepts/s3-eventually-consistent-model.md)
- [Table repair](/concepts/delta-table-repair.md)

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
