---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e4e3d41ea209c8db6ae8af2352f247bb7d4053e589deb6108c52ed23c4c262a
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-log-non-contiguity-due-to-s3-eventual-consistency
    - DLNDTSEC
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta log non-contiguity due to S3 eventual consistency
description: On AWS, eventual consistency of S3 when a Delta table is deleted and recreated at the same location can cause non-contiguous version gaps.
tags:
  - aws
  - delta-lake
  - s3
  - consistency
timestamp: "2026-06-18T11:57:49.356Z"
---

# Delta Log Non-Contiguity Due to S3 Eventual Consistency

**Delta log non-contiguity due to S3 eventual consistency** is a specific error condition in [Delta Lake](/concepts/delta-lake.md) where the transaction log contains a gap between versions, caused by the eventually consistent behavior of Amazon S3 when a Delta table is deleted and recreated at the same storage location.

## Error Condition

The error manifests as the `DELTA_VERSIONS_NOT_CONTIGUOUS` error class (SQLSTATE: KD00C) with the following message:

```
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Cause on AWS

On AWS, this error can occur due to S3 eventual consistency when a Delta table is deleted and recreated at the same location. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

The scenario typically unfolds as follows:

1. A Delta table exists at a specific S3 path with a transaction log containing versions 0 through N.
2. The table is deleted, removing the Delta log files.
3. A new Delta table is created at the same S3 path, starting a new transaction log from version 0.
4. Due to S3's eventual consistency model, some read operations may still see the old log files alongside the new ones, or may see a mix of old and new versions, creating the appearance of a gap or discontinuity in the version sequence.

This is distinct from the Azure and generic causes, where the error is attributed solely to manual removal of files from the Delta log. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Other Causes

The error can also occur when files have been manually removed from the Delta log, regardless of the cloud provider. This is the only recognized cause on Azure and in generic environments. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, contact Databricks support to repair the table. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

To prevent this error when working with Delta tables on S3:

- Avoid deleting and recreating tables at the same S3 location. Instead, use a different path for the new table.
- If you must reuse a location, ensure that all previous table data and log files have been fully deleted and that S3 consistency has been achieved before creating the new table.
- Consider using [Delta Lake table cloning](/concepts/delta-table-cloning.md) or [table versioning](/concepts/delta-table-versioning.md) practices to manage table lifecycle without reusing paths.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The foundation of Delta Lake's ACID transactions
- [Amazon S3 Consistency Model](/concepts/s3-eventually-consistent-model.md) — The underlying cause of this error on AWS
- [Delta Lake Error Conditions](/concepts/delta-error-sub-conditions.md) — Other error classes related to Delta Lake operations
- [Delta Table Repair](/concepts/delta-table-repair.md) — The process of fixing corrupted Delta tables

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
