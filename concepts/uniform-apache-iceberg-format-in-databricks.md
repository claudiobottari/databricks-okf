---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0878f73909b06f744726d2e31f179fc9153226eb1b75a0427f6055f04b4c8ce
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - uniform-apache-iceberg-format-in-databricks
    - U(IFID
    - Apache Iceberg on Databricks
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Uniform (Apache Iceberg) format in Databricks
description: A Databricks feature that makes Delta Lake tables readable as Apache Iceberg tables; enabling it requires all files to be Iceberg-compatible and triggers the DELTA_ICEBERG_COMPAT_VIOLATION if files lack compatibility tags.
tags:
  - delta-lake
  - iceberg
  - uniform
  - databricks
timestamp: "2026-06-19T18:25:54.364Z"
---

# Uniform (Apache Iceberg) Format in Databricks

**Uniform (Apache Iceberg) format** is a table format feature in Databricks that enables Apache Iceberg compatibility for Delta Lake tables. When enabled, the table maintains both Delta and Iceberg metadata simultaneously, allowing Iceberg-compatible engines to read the table while Delta Lake engines continue to write to it.

## Overview

Uniform (Apache Iceberg) format is implemented through the `IcebergCompatV` feature, where `V` represents a version number. This feature ensures that all files in the table are Apache Iceberg compatible, enabling interoperability between Delta Lake and Apache Iceberg ecosystems. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## IcebergCompat Versions

The `IcebergCompatVersion` setting supports versions between 1 and a maximum version (`<maxVersion>`) supported by the Databricks runtime. Only one IcebergCompat version can be enabled at a time — all other versions must be explicitly disabled. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Enabling Uniform Format

### Upgrading an Existing Table

To enable or upgrade Uniform (Apache Iceberg) format on an existing table, use the `REORG TABLE APPLY (UPGRADE UNIFORM)` command:

```sql
REORG TABLE <table_name> APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <version>'));
```

This command enables the specified IcebergCompat table feature. Note that other Databricks runtime versions without support for that specific table feature may not be able to write to the table after upgrading. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Prerequisites

Uniform format can only be enabled on **managed tables**. It is not supported on external or unmanaged tables. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Requirements and Constraints

### Deletion Vectors

IcebergCompatV requires Deletion Vectors to be completely purged from the table. If Deletion Vectors are still enabled, you must first disable them and then run `REORG PURGE` to remove existing Deletion Vectors:

```sql
REORG TABLE <table_name> APPLY (PURGE);
```

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Required Table Features

IcebergCompatV requires certain table features to be supported and enabled. You cannot drop these required features from the table without first disabling IcebergCompatV. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Schema Compatibility

The schema must be compatible with Apache Iceberg. This means:

- All data types in the schema must be supported by IcebergCompatV
- Partition column data types must also be supported
- Type widening changes (changing a field from one type to another) are incompatible with IcebergCompatV
- Replacing partitioned tables with a differently-named partition spec is not supported (due to Iceberg-Spark 1.1.0 limitations)

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Table Properties

IcebergCompatV requires specific table properties to be set to specific values. If a required property is set to an incorrect value, the feature cannot be enabled. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## File Compatibility

All files in the table must be Apache Iceberg compatible when enabling Uniform format. If concurrent writes have added files that are not Iceberg compatible, you may need to run the upgrade command again. The system checks for `<addFilesCount>` files in the current table version and `<addFilesWithoutTag>` files that are not compatible. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Conditions

The `DELTA_ICEBERG_COMPAT_VIOLATION` error class covers various validation failures:

| Error Subtype | Description |
|---------------|-------------|
| `CHANGE_VERSION_NEED_REWRITE` | Changing to a new IcebergCompat version requires rewriting the table |
| `COMPAT_VERSION_NOT_SUPPORTED` | The specified version is not supported |
| `CONFIG_NOT_ENABLED` | IcebergCompatV is not enabled in the environment |
| `DELETION_VECTORS_NOT_PURGED` | Deletion Vectors must be purged first |
| `DISABLING_REQUIRED_TABLE_FEATURE` | Cannot drop required table features |
| `FILES_NOT_ICEBERG_COMPAT` | Some files are not Iceberg compatible |
| `UNSUPPORTED_DATA_TYPE` | Schema contains unsupported data types |
| `VERSION_MUTUAL_EXCLUSIVE` | Only one IcebergCompat version can be enabled |
| `WRONG_REQUIRED_TABLE_PROPERTY` | Required table property is set incorrectly |

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The base table format that Uniform extends
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that Uniform provides compatibility with
- [REORG command](/concepts/reorg-table-command.md) — The SQL command used to upgrade tables to Uniform format
- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta Lake feature that must be purged before enabling IcebergCompat
- [Managed Tables](/concepts/managed-tables-in-databricks.md) — The only table type that supports Uniform format
- Table Properties in Delta Lake — Configuration properties that may conflict with Uniform requirements

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
