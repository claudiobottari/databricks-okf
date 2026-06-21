---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e28549597e531d0f8497963ff83c334073c73af79b8f3ded7aa5b2ae9884045d
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - uniform-delta-uniform
    - Uniform (UniForm)
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Uniform (Delta-Uniform)
description: A Databricks feature that makes Delta Lake tables readable by Apache Iceberg clients by storing Iceberg metadata alongside Delta metadata.
tags:
  - databricks
  - delta-lake
  - apache-iceberg
  - interoperability
timestamp: "2026-06-18T15:21:08.520Z"
---

**Note:** The provided source material does not contain a page titled "Uniform (Delta-Uniform)". The closest match is a page about the `DELTA_ICEBERG_COMPAT_VIOLATION` error condition, which is part of the **Uniform** feature in Databricks.

The following page is written based solely on the provided source. I have chosen the title "Delta-Uniform: DELTA_ICEBERG_COMPAT_VIOLATION" to reflect the actual content, as the requested title is not present in the source.

---

## Delta-Uniform: DELTA_ICEBERG_COMPAT_VIOLATION

**Delta-Uniform** refers to the [Delta Lake](/concepts/delta-lake.md) feature that enables [Delta Lake](/concepts/delta-lake.md) tables to be read by [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) readers. The official term used in the Databricks documentation is **Uniform**. The `DELTA_ICEBERG_COMPAT_VIOLATION` error class covers a set of errors that occur when a user attempts to enable or upgrade the Uniform / IcebergCompatV compatibility layer on a Delta table and the table's state is incompatible with the requested version. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Class: DELTA_ICEBERG_COMPAT_VIOLATION

The `DELTA_ICEBERG_COMPAT_VIOLATION` error condition is raised when the validation of `IcebergCompatV<version>` fails. Each sub-error has a specific message and recommended resolution. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Sub-Errors

| Error | SQLSTATE | Cause and Resolution |
|-------|----------|----------------------|
| CHANGE_VERSION_NEED_REWRITE | KD00E | The user is attempting to change to a newer IcebergCompat version. The table must be rewritten using the `REORG TABLE APPLY (UPGRADE UNIFORM ...)` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| COMPAT_VERSION_NOT_SUPPORTED | KD00E | The requested `IcebergCompatVersion = <version>` is not supported. Supported versions are between 1 and `<maxVersion>`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| CONFIG_NOT_ENABLED | KD00E | `IcebergCompatV<version>` is not enabled in the current environment. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| DELETION_VECTORS_NOT_PURGED | KD00E | `IcebergCompatV<version>` requires [Deletion Vectors](/concepts/deletion-vectors.md) to be completely purged from the table. Run the `REORG TABLE APPLY (PURGE)` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| DELETION_VECTORS_SHOULD_BE_DISABLED | KD00E | `IcebergCompatV<version>` requires Deletion Vectors to be disabled on the table first. Then run `REORG PURGE` to purge the Deletion Vectors. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| DISABLING_REQUIRED_TABLE_FEATURE | KD00E | `IcebergCompatV<version>` requires a table feature (`<feature>`) to be supported and enabled. You cannot drop the feature from the table. Instead, disable `IcebergCompatV<version>` first. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| FILES_NOT_ICEBERG_COMPAT | KD00E | Some files are not Apache Iceberg compatible, likely due to concurrent writes. Run `REORG TABLE APPLY (UPGRADE UNIFORM)` again. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| INCOMPATIBLE_TABLE_FEATURE | KD00E | `IcebergCompatV<version>` is incompatible with a specific table feature. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| MISSING_REQUIRED_TABLE_FEATURE | KD00E | `IcebergCompatV<version>` requires a table feature (`<feature>`) to be supported and enabled. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| REPLACE_TABLE_CHANGE_PARTITION_NAMES | KD00E | `IcebergCompatV<version>` does not support replacing partitioned tables with a differently-named partition spec. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| REQUIRE_MANAGED_TABLE | KD00E | The feature can only be enabled on [Managed Tables](/concepts/managed-tables-in-databricks.md). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| REWRITE_DATA_FAILED | KD00E | Data rewriting failed. Run the `REORG TABLE APPLY (UPGRADE UNIFORM)` command again. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| SCHEMA_COMPATIBILITY_CHECK_FAILED | KD00E | Apache Iceberg schema compatibility check failed during table creation or conversion. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| UNSUPPORTED_DATA_TYPE | KD00E | `IcebergCompatV<version>` does not support the specified data type in the schema. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| UNSUPPORTED_PARTITION_DATA_TYPE | KD00E | `IcebergCompatV<version>` does not support the partition data type. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| UNSUPPORTED_TYPE_WIDENING | KD00E | `IcebergCompatV<version>` is incompatible with a type change applied to the field. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| VERSION_MUTUAL_EXCLUSIVE | KD00E | Only one `IcebergCompat` version can be enabled. Explicitly disable all other versions. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |
| WRONG_REQUIRED_TABLE_PROPERTY | KD00E | `IcebergCompatV<version>` requires a specific table property value. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md] |

## Prerequisites

To enable `IcebergCompatV<version>` (Uniform), the table must be a [Managed Table](/concepts/unity-catalog-managed-tables.md). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- Uniform (IcebergCompatV)
- [Deletion Vectors](/concepts/deletion-vectors.md)
- [REORG TABLE](/concepts/reorg-table.md)
- [SQLSTATE KD00E](/concepts/sqlstate-kd00e.md)

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
