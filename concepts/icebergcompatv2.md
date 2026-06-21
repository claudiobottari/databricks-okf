---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9eed2b3266b1bf066e7ea9cd9ac422a4f47ca489abf1dc8b7d143f2e4d02b551
  pageDirectory: concepts
  sources:
    - read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv2
    - IcebergCompatV1 and V2
    - Iceberg-Spark
  citations:
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
title: IcebergCompatV2
description: A Delta Lake write protocol feature that enables Iceberg read compatibility on Delta Lake tables, requiring column mapping and Databricks Runtime 14.3 LTS or above.
tags:
  - delta-lake
  - iceberg
  - protocol-features
timestamp: "2026-06-19T20:11:15.436Z"
---

# IcebergCompatV2

**IcebergCompatV2** is a Delta Lake write protocol feature that enables tables to generate Iceberg-compatible metadata automatically, allowing Apache Iceberg clients to read Delta Lake tables. It was previously part of the Delta Lake Universal Format (UniForm) feature and supersedes the legacy `IcebergCompatV1` implementation. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Overview

IcebergCompatV2 configures Delta Lake tables to automatically generate Iceberg metadata asynchronously alongside normal Delta Lake write operations, without rewriting existing data files. This enables a single copy of Parquet data files to be read by both Delta Lake and Apache Iceberg clients. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Requirements

To enable IcebergCompatV2, the following conditions must be met:

- The [Delta Lake Table](/concepts/delta-lake-table.md) must be registered to [Unity Catalog](/concepts/unity-catalog.md). Both managed and external tables are supported.
- The table must have [Delta Lake Column Mapping](/concepts/delta-table-column-mapping.md) enabled.
- The table must have a `minReaderVersion` >= 2 and `minWriterVersion` >= 7.
- Writes to the table must use Databricks Runtime 14.3 LTS or above.

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Enabling IcebergCompatV2

IcebergCompatV2 is enabled by setting two table properties:

```sql
'delta.enableIcebergCompatV2' = 'true'
'delta.universalFormat.enabledFormats' = 'iceberg'
```

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

### During Table Creation

Column mapping is automatically enabled when Iceberg reads are enabled during table creation:

```sql
CREATE TABLE T(c1 INT) TBLPROPERTIES(
  'delta.columnMapping.mode' = 'id',
  'delta.enableIcebergCompatV2' = 'true',
  'delta.universalFormat.enabledFormats' = 'iceberg'
);
```

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

### On Existing Tables

In Databricks Runtime 15.4 LTS and above, IcebergCompatV2 can be enabled on existing tables:

```sql
ALTER TABLE table_name SET TBLPROPERTIES(
  'delta.columnMapping.mode' = 'name',
  'delta.enableIcebergCompatV2' = 'true',
  'delta.universalFormat.enabledFormats' = 'iceberg'
);
```

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

### Using REORG

The `REORG` command can upgrade existing tables to IcebergCompatV2, which is necessary when the table has [Deletion Vectors](/concepts/deletion-vectors.md) enabled or when upgrading from the legacy `IcebergCompatV1`:

```sql
REORG TABLE table_name APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2));
```

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## How It Works

When IcebergCompatV2 is enabled, each Delta Lake write transaction triggers asynchronous Iceberg metadata generation on the same compute resource. The system groups multiple Delta Lake commits into a single Iceberg metadata commit for tables with frequent writes, preventing cascading latency. Only one metadata generation process runs concurrently per compute resource. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Delta and Iceberg Version Mapping

[Delta Lake Table](/concepts/delta-lake-table.md) versions generally do not align with Iceberg table versions by commit timestamp or version ID. The corresponding table properties can be reviewed using `DESCRIBE EXTENDED` or Catalog Explorer to track version correspondence. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Limitations

- IcebergCompatV2 does not work on tables with [Deletion Vectors](/concepts/deletion-vectors.md) enabled when targeting Iceberg v2 clients. (Apache Iceberg v3 does support deletion vectors.)
- The Delta table must be accessed by name (not path) to automatically trigger Iceberg metadata generation.
- Cannot be enabled on materialized views or Streaming Tables.
- Tables with Iceberg reads enabled do not support `VOID` types.
- Iceberg client support is read-only; writes from Iceberg clients are not supported.
- Tables use Zstandard compression instead of Snappy for underlying Parquet data files.

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Universal Format (UniForm)](/concepts/delta-lake-universal-format-uniform.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Delta Lake Column Mapping](/concepts/delta-table-column-mapping.md)
- [Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md)
- [OpenSharing](/concepts/opensharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md

# Citations

1. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
