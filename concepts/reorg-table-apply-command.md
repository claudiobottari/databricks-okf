---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66c0b4cc42f78c6264c70df8c5a526964a5451bb1dc2491243dfc3fbc1e42028
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reorg-table-apply-command
    - RTAC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: REORG TABLE APPLY command
description: A Databricks SQL command used to resolve IcebergCompatV violations by rewriting, purging deletion vectors, or upgrading the Uniform format version on Delta tables.
tags:
  - delta-lake
  - databricks
  - sql-commands
  - table-maintenance
timestamp: "2026-06-18T11:54:01.111Z"
---

---
title: REORG TABLE APPLY command
summary: The `REORG TABLE APPLY` command resolves `DELTA_ICEBERG_COMPAT_VIOLATION` errors by purging Deletion Vectors or upgrading the Uniform Iceberg compatibility version of a Delta table.
sources:
  - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - databricks
  - sql
  - delta-lake
  - iceberg
aliases:
  - reorg-table-apply-command
  - REORGTAC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# REORG TABLE APPLY command

The **`REORG TABLE APPLY`** command is a maintenance operation on Delta tables in Databricks that resolves specific `DELTA_ICEBERG_COMPAT_VIOLATION` errors. It has two primary uses: purging [Deletion Vectors](/concepts/deletion-vectors.md) from a table, and upgrading the table's [Uniform](/concepts/delta-uniform.md) compatibility with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Syntax

```
REORG TABLE [table_name] APPLY (PURGE)
REORG TABLE [table_name] APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <version>'))
```

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Use Cases

### Purging Deletion Vectors

When the error `DELETION_VECTORS_NOT_PURGED` occurs — indicating that IcebergCompatV`<version>` requires all Deletion Vectors to be purged — run the `REORG TABLE APPLY (PURGE)` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

If Deletion Vectors need to be disabled first (error `DELETION_VECTORS_SHOULD_BE_DISABLED`), disable them on the table and then run the `REORG PURGE` command (the source uses `REORG PURGE` without `APPLY` in that context, but the underlying operation is the same purge action). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Upgrading Uniform Iceberg Compatibility

When changing the IcebergCompat version of a table (error `CHANGE_VERSION_NEED_REWRITE`), run: ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

```sql
REORG TABLE <table_name> APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'));
```

This rewrites the table to enable the new IcebergCompatV`<newVersion>` feature. Note that after the upgrade, other Databricks runtime versions that do not support that table feature may not be able to write to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Retrying After Incomplete Upgrade

If the `FILES_NOT_ICEBERG_COMPAT` error occurs — meaning some files were not made Iceberg compatible due to concurrent writes — or if `REWRITE_DATA_FAILED` is raised, run the same `REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` command again. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Errors Handled

| Error Condition | Recommended Action |
|----------------|-------------------|
| `CHANGE_VERSION_NEED_REWRITE` | Run `REORG TABLE APPLY (UPGRADE UNIFORM (...))` with the new version. |
| `DELETION_VECTORS_NOT_PURGED` | Run `REORG TABLE APPLY (PURGE)`. |
| `DELETION_VECTORS_SHOULD_BE_DISABLED` | Disable Deletion Vectors, then run `REORG PURGE`. |
| `FILES_NOT_ICEBERG_COMPAT` | Re-run the same `UPGRADE UNIFORM` command. |
| `REWRITE_DATA_FAILED` | Re-run the same `UPGRADE UNIFORM` command. |

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ICEBERG_COMPAT_VIOLATION error class — The parent error class addressed by this command
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The Delta-to-Iceberg compatibility layer
- [Deletion Vectors](/concepts/deletion-vectors.md) — Delta table features that must be purged for Iceberg compatibility
- [IcebergCompatV2](/concepts/icebergcompatv2.md) — A specific version of Iceberg compatibility
- Delta table maintenance commands — Other maintenance operations like `OPTIMIZE`, `VACUUM`, `REORG`

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
