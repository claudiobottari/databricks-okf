---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e9090ac0cf5799edf959e429a212bfbb788fb4dc3e993c186bbddd1ee7b31a6
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - reorg-table-command
    - RTC
    - REORG Command
    - REORG command
  citations:
    - file: reorg-table-databricks-on-aws.md
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: REORG TABLE command
description: A Databricks SQL command used to resolve IcebergCompat violations by rewriting data, upgrading uniform format, purging deletion vectors, or enabling IcebergCompat versions.
tags:
  - delta-lake
  - databricks
  - sql-commands
  - table-maintenance
timestamp: "2026-06-19T15:05:46.310Z"
---

# REORG TABLE Command

The **`REORG TABLE` command** is a Delta Lake SQL statement used to reorganize a Delta table by rewriting data files for specific maintenance purposes, such as purging soft-deleted data, upgrading table format compatibility, or performing checkpointing to improve metadata management. It is available in Databricks SQL and Databricks Runtime 11.3 LTS and above. ^[reorg-table-databricks-on-aws.md]

## Syntax

```
REORG [ TABLE ] table_name { [ WHERE predicate ] APPLY ( PURGE ) |
                             APPLY ( UPGRADE UNIFORM ( ICEBERG_COMPAT_VERSION = version ) |
                                     CHECKPOINT ) }
```

In Databricks Runtime versions before 15.4, `TABLE` is a mandatory keyword. ^[reorg-table-databricks-on-aws.md]

## Parameters

- **`table_name`** — Identifies an existing Delta table. The name must not include a temporal specification or options specification. ^[reorg-table-databricks-on-aws.md]

- **`WHERE predicate`** — For `APPLY (PURGE)`, reorganizes only the files that match the given partition predicate. Only filters involving partition key attributes are supported. ^[reorg-table-databricks-on-aws.md]

- **`APPLY (PURGE)`** — Rewrites files that contain soft-deleted data, such as column data removed by `ALTER TABLE DROP COLUMN`. This purges metadata-only deletes by forcing a data rewrite. After running `APPLY (PURGE)`, the soft-deleted data may still exist in the old files; you can run the VACUUM command to physically delete them. ^[reorg-table-databricks-on-aws.md]

- **`APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION = version))`** — Available in Databricks Runtime 14.3 and above. Rewrites table files to upgrade the table to a specified [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) compatibility version. The `version` parameter must be either `1` or `2`. This operation may rewrite all files, unlike `PURGE` which only rewrites files with soft-deleted data. ^[reorg-table-databricks-on-aws.md]

- **`APPLY (CHECKPOINT)`** — Available in Databricks Runtime 16.3 and above. Performs Delta checkpointing on the table's latest Delta version. This requires the table to have checkpoint V2 enabled to prevent corruption caused by race conditions. ^[reorg-table-databricks-on-aws.md]

## Behavior and Idempotency

`REORG TABLE` is **idempotent** — if it is run twice on the same dataset, the second run has no effect. ^[reorg-table-databricks-on-aws.md]

- `APPLY (PURGE)` only rewrites files that contain soft-deleted data. ^[reorg-table-databricks-on-aws.md]
- `APPLY (UPGRADE)` may rewrite all files. ^[reorg-table-databricks-on-aws.md]

## Error Handling

`REORG TABLE` is referenced in several error conditions related to the DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION error class. For example, when upgrading the Iceberg compatibility version, if some files are not Iceberg-compatible (often due to concurrent writes), the error suggests running `REORG TABLE APPLY (UPGRADE UNIFORM ...)` again. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

Similarly, when Deletion Vectors need to be purged before enabling an Iceberg compat version, the error message directs the user to run `REORG TABLE APPLY (PURGE)`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Examples

```sql
-- Purge soft-deleted data from all files
REORG TABLE events APPLY (PURGE);

-- Purge soft-deleted data from a specific partition
REORG TABLE events WHERE date >= '2022-01-01' APPLY (PURGE);

-- Purge soft-deleted data from recent partitions
REORG TABLE events
  WHERE date >= current_timestamp() - INTERVAL '1' DAY
  APPLY (PURGE);

-- Upgrade table to Iceberg compatibility version 2
REORG TABLE events APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2));

-- Perform checkpointing on the latest Delta version
REORG TABLE events APPLY (CHECKPOINT);
```

^[reorg-table-databricks-on-aws.md]

## Related Concepts

- VACUUM — Physically deletes old files after purging soft-deleted data with `REORG TABLE APPLY (PURGE)`.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION — Error class that may recommend running `REORG TABLE` to resolve incompatibilities.
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The feature that `REORG TABLE APPLY (UPGRADE UNIFORM ...)` enables.
- [Deletion Vectors](/concepts/deletion-vectors.md) — Feature that must be purged or disabled before certain Iceberg compat upgrades.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format managed by `REORG TABLE`.
- ALTER TABLE DROP COLUMN — Operation that creates soft-deleted data that `REORG TABLE PURGE` removes.

## Sources

- reorg-table-databricks-on-aws.md
- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md](/references/reorg-table-databricks-on-aws-58d61683.md)
2. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
