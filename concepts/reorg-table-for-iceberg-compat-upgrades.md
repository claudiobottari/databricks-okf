---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f1f9cfdc6772dedce75cb564dd169f1eaca3cc7943b9874ccc73a81a00324b7
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reorg-table-for-iceberg-compat-upgrades
    - RTFICU
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: REORG TABLE for Iceberg compat upgrades
description: The command pattern REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <version>')) used to rewrite a Delta table and enable a new IcebergCompat version, including PURGE sub-commands for deletion vectors.
tags:
  - delta-lake
  - iceberg-compatibility
  - administration
timestamp: "2026-06-19T10:06:54.996Z"
---

# REORG TABLE for Iceberg Compat Upgrades

**REORG TABLE** is a Databricks command used to resolve compatibility issues when upgrading or enabling the [IcebergCompatV](/concepts/icebergcompatv.md) feature on Delta tables. When a table is configured for Unified Apache Iceberg with a specific `IcebergCompat` version, certain conditions must be met—such as purging deletion vectors or rewriting data—before the upgrade can complete. The `REORG TABLE APPLY (UPGRADE UNIFORM)` command handles these preconditions. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Purpose

The `REORG TABLE` command is primarily triggered by DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION error conditions that arise when changing the `IcebergCompatV` version on a table. Each error sub‑condition describes what must be fixed and, in most cases, points the user to a specific `REORG` sub‑command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Common REORG Commands

### CHANGE\_VERSION\_NEED\_REWRITE[​](#change_version_need_rewrite "Direct link to CHANGE_VERSION_NEED_REWRITE")

```sql
REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))
```

Switching to a newer `IcebergCompatV` version requires rewriting the table so that all existing data files are made compatible with the new version. After the command completes, the table supports the new `IcebergCompatV` version, and other Databricks runtime versions that do not support that version may not be able to write to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DELETION\_VECTORS\_NOT\_PURGED[​](#deletion_vectors_not_purged "Direct link to DELETION_VECTORS_NOT_PURGED")

```sql
REORG TABLE APPLY (PURGE)
```

`IcebergCompatV` requires [Deletion Vectors](/concepts/deletion-vectors.md) to be completely purged from the table. This command removes all deletion vector‑related metadata so that the table can be upgraded. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DELETION\_VECTORS\_SHOULD\_BE\_DISABLED[​](#deletion_vectors_should_be_disabled "Direct link to DELETION_VECTORS_SHOULD_BE_DISABLED")

```sql
REORG PURGE
```

If deletion vectors are still enabled on the table, the upgrade requires them to be disabled first, then purged with the `REORG PURGE` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### FILES\_NOT\_ICEBERG\_COMPAT[​](#files_not_iceberg_compat "Direct link to FILES_NOT_ICEBERG_COMPAT")

```sql
REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION = <version>))
```

When some files in the table are not Apache Iceberg compatible (usually as a result of concurrent writes), this command must be run again to complete the upgrade. The error message reports the number of non‑compatible files found at the current table version. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### REWRITE\_DATA\_FAILED[​](#rewrite_data_failed "Direct link to REWRITE_DATA_FAILED")

```sql
REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION = <version>))
```

If the data rewriting step itself failed, the same `REORG TABLE` command should be re‑executed. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION – The parent error class that reports these conditions.
- [IcebergCompatV](/concepts/icebergcompatv.md) – The versioned compatibility layer for Iceberg.
- [Deletion Vectors](/concepts/deletion-vectors.md) – A Delta feature that must be purged before upgrading.
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The format that `IcebergCompatV` enables.
- [REORG TABLE](/concepts/reorg-table.md) (general purpose) – The broader command used for table maintenance.
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) – The set of features that must be enabled or disabled for version upgrades.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
