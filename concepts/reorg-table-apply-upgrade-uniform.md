---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 653180b2be9b8ea07974c209c3402a930c526ebb32938ce638bb679250eed7ae
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reorg-table-apply-upgrade-uniform
    - RTA(U
    - REORG TABLE - UPGRADE UNIFORM
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: REORG TABLE APPLY (UPGRADE UNIFORM)
description: A Databricks SQL command used to upgrade a Delta table to a specific IcebergCompatV version, rewrite data for Iceberg compatibility, and resolve several DELTA_ICEBERG_COMPAT_VIOLATION errors.
tags:
  - sql-command
  - delta-lake
  - iceberg
  - databricks
timestamp: "2026-06-19T18:25:54.755Z"
---

Here is the wiki page for "REORG TABLE APPLY (UPGRADE UNIFORM)", based solely on the provided source material.

---

**REORG TABLE APPLY (UPGRADE UNIFORM)** is a Databricks SQL command used to rewrite a [Delta Lake](/concepts/delta-lake.md) table's data and metadata to resolve compatibility issues with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) when [Uniform](/concepts/delta-uniform.md) is enabled. It is specifically directed at [IcebergCompatV](/concepts/icebergcompatv.md) version upgrades.

## Purpose

The command is the primary recovery action when a `DELTA_ICEBERG_COMPAT_VIOLATION` error indicates that an operation, such as changing the [IcebergCompatV](/concepts/icebergcompatv.md) version of a Uniform-enabled table, requires a full table rewrite. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

Several specific error conditions within `DELTA_ICEBERG_COMPAT_VIOLATION` recommend this command:

- **`CHANGE_VERSION_NEED_REWRITE`** – Changing the table to a new `IcebergCompatV` version requires a rewrite. The recommended action is to run `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **`FILES_NOT_ICEBERG_COMPAT`** – Some files in the table are not Apache Iceberg compatible, usually due to concurrent writes. The recommended action is to re-run `REORG TABLE` `APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **`REWRITE_DATA_FAILED`** – The data rewrite process for a new IcebergCompat version failed. The recommended action is to re-run the `REORG TABLE` `APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Syntax

The command is provided in two syntactical forms in the source material:

```sql
REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'));
```

and

```sql
REORG TABLE table APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>));
```

Both forms specify the target Iceberg compatibility version within the `UPGRADE UNIFORM` clause. The command rewrites existing data files to be compatible with the new version. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Side Effects

Executing this command enables the table feature `IcebergCompatV<newVersion>`. As a result, other Databricks runtime versions that do not support that specific table feature may lose the ability to write to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Commands

A similar command, `REORG TABLE APPLY (PURGE)`, is used in a different scenario where [IcebergCompatV](/concepts/icebergcompatv.md) requires [Deletion Vectors](/concepts/deletion-vectors.md) to be completely purged from the table. The `DELETION_VECTORS_NOT_PURGED` error directs users to run `REORG TABLE APPLY (PURGE)`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Uniform](/concepts/delta-uniform.md) – The feature enabling Delta Lake tables to be read by Apache Iceberg clients.
- [IcebergCompatV](/concepts/icebergcompatv.md) – The specific version of the Iceberg compatibility specification applied to a Uniform table.
- [REORG TABLE](/concepts/reorg-table.md) – The parent command encompassing both `APPLY (UPGRADE UNIFORM)` and `APPLY (PURGE)` operations.
- [Deletion Vectors](/concepts/deletion-vectors.md) – A Delta Lake feature that must be removed before upgrading Uniform to certain IcebergCompat versions.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
