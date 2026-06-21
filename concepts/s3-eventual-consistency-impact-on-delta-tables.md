---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 873b47f98b8d78f0bdbea2b3fdca10cae58eebe7b99b12c810ad585667b2f804
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - s3-eventual-consistency-impact-on-delta-tables
    - SECIODT
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: S3 Eventual Consistency Impact on Delta Tables
description: A cause specific to AWS S3 where eventual consistency can lead to a non-contiguous delta log when a table is deleted and recreated at the same location.
tags:
  - aws-s3
  - consistency
  - delta-lake
  - databricks
timestamp: "2026-06-19T15:10:41.988Z"
---

# S3 Eventual Consistency Impact on Delta Tables

**S3 Eventual Consistency Impact on Delta Tables** refers to a known issue where Amazon S3's eventual consistency model can cause the `DELTA_VERSIONS_NOT_CONTIGUOUS` error when Delta tables are deleted and recreated at the same S3 location. This condition disrupts Delta Lake's transaction log, which relies on contiguous, ordered version files to maintain table integrity.

## Error Condition

The `DELTA_VERSIONS_NOT_CONTIGUOUS` error occurs when Delta Lake detects a gap in the delta log between versions `<startVersion>` and `<endVersion>` while attempting to load a specific version `<versionToLoad>`. The error message reports that versions (`<versionList>`) are not contiguous. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

This error is classified under SQLSTATE KD00C, which falls within the datasource-specific error class (Class KD) in Databricks error handling. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## S3-Specific Cause

On AWS, this error condition can be triggered by S3 eventual consistency when a table is deleted and recreated at the same S3 location. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

The mechanism works as follows:

1. A Delta table is deleted from an S3 location, removing the delta log files (version files).
2. A new Delta table is created at the same S3 location, generating new version files starting from version 0.
3. Due to S3's eventual consistency model, some old version files from the deleted table may still be visible during a subsequent read operation.
4. Delta Lake encounters both old and new version files, creating a gap or discontinuity in the version sequence, which triggers the error.

## Resolution

To resolve this error on AWS, contact Databricks Support to repair the table. Databricks support can restore the table to a consistent state by reconciling the delta log. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

To prevent this error, avoid deleting and recreating Delta tables at the same S3 location. Instead, use a different S3 path for each new table, or use Delta Lake operations like `OVERWRITE` or `REPLACE TABLE` which handle the table lifecycle within Delta Lake's transaction protocol rather than relying on raw S3 operations. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Other Causes

The `DELTA_VERSIONS_NOT_CONTIGUOUS` error can also occur when files have been manually removed from the Delta log, regardless of cloud provider. This applies to AWS, Azure, and generic scenarios. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Azure and Generic Behavior

On Azure, the error is attributed only to manual file removal from the delta log. The generic cause description likewise only mentions manual file removal. The S3 eventual consistency trigger is specific to AWS. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The mechanism that tracks all changes to a Delta table.
- [S3 Consistency Model](/concepts/s3-eventually-consistent-model.md) – Amazon S3's read-after-write and eventual consistency guarantees.
- DELTA_VERSIONS_NOT_CONTIGUOUS error|DELTA_VERSIONS_NOT_CONTIGUOUS – The error condition itself.
- [Delta Table Repair](/concepts/delta-table-repair.md) – Procedures for fixing corrupted Delta tables.
- [Delta Lake on AWS](/concepts/delta-lake.md) – Deployment considerations for Delta Lake on Amazon S3.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
