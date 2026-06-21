---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec4fc40718281aa30f6b3810827d795c26871e1b7dff17a6be526bc77acd0daa
  pageDirectory: concepts
  sources:
    - read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-universal-format-uniform
    - DLUF(
    - Universal Format (UniForm)
  citations:
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
title: Delta Lake Universal Format (UniForm)
description: A Databricks feature that enables Delta Lake tables to be read by Apache Iceberg clients by automatically generating Iceberg metadata asynchronously without rewriting data.
tags:
  - delta-lake
  - iceberg
  - databricks
  - interoperability
timestamp: "2026-06-19T20:11:41.823Z"
---

# Delta Lake Universal Format (UniForm)

**Delta Lake Universal Format (UniForm)** is a feature of Delta Lake on Databricks that enables Apache Iceberg clients to read Delta Lake tables. The feature was formerly called "UniForm" and is now referred to as "Iceberg reads." ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## How It Works

Both [Delta Lake](/concepts/delta-lake.md) and [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) consist of Parquet data files and a metadata layer. UniForm configures tables to automatically generate Iceberg metadata asynchronously, without rewriting data, so that Iceberg clients can read Delta Lake tables written by Databricks. A single copy of the data files serves multiple formats. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

When Iceberg reads are enabled, the write protocol feature `IcebergCompatV2` is added to the table. This feature depends on [Delta Lake Column Mapping](/concepts/delta-table-column-mapping.md), which cannot be dropped once enabled. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Requirements

To enable Iceberg reads, the following requirements must be met: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

- The [Delta Lake Table](/concepts/delta-lake-table.md) must be registered to [Unity Catalog](/concepts/unity-catalog.md). Both managed and external tables are supported.
- The table must have column mapping enabled.
- The [Delta Lake Table](/concepts/delta-lake-table.md) must have a `minReaderVersion` >= 2 and `minWriterVersion` >= 7.
- Writes to the table must use Databricks Runtime 14.3 LTS or above.

## Enabling Iceberg Reads

### During Table Creation

Column mapping is enabled automatically when Iceberg reads are enabled during table creation: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

```sql
CREATE TABLE T(c1 INT) TBLPROPERTIES(
  'delta.columnMapping.mode' = 'id',
  'delta.enableIcebergCompatV2' = 'true',
  'delta.universalFormat.enabledFormats' = 'iceberg'
);
```

### On an Existing Table

In Databricks Runtime 15.4 LTS and above, you can enable Iceberg reads on an existing table using `ALTER TABLE`: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

```sql
ALTER TABLE table_name SET TBLPROPERTIES(
  'delta.columnMapping.mode' = 'name',
  'delta.enableIcebergCompatV2' = 'true',
  'delta.universalFormat.enabledFormats' = 'iceberg'
);
```

### Using `REORG`

Use `REORG` to enable Iceberg reads when your table has deletion vectors enabled, or if you previously enabled the `IcebergCompatV1` version of UniForm: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

```sql
REORG TABLE table_name APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2));
```

## Metadata Generation

Databricks triggers metadata generation asynchronously after a Delta Lake write transaction completes. Delta Lake ensures that only one metadata generation process is in progress on a given compute resource. Tables with frequent commits might group multiple Delta Lake commits into a single commit to Iceberg metadata. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

### Manual Trigger

You can manually trigger Iceberg metadata generation for the latest version of the [Delta Lake Table](/concepts/delta-lake-table.md) using `MSCK REPAIR TABLE`: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

```sql
MSCK REPAIR TABLE <table-name> SYNC METADATA
```

This is helpful when a cluster terminates before automatic metadata generation succeeds, or when a client that does not support UniForm writes to the table.

## Delta and Iceberg Table Versions

[Delta Lake Table](/concepts/delta-lake-table.md) versions do not generally align with Iceberg versions by commit timestamp or version ID. To verify which [Delta Lake Table](/concepts/delta-lake-table.md) version a given Iceberg version corresponds to, review the `Delta Uniform Iceberg` section returned by `DESCRIBE EXTENDED`. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Limitations

The following limitations apply to all tables with Iceberg reads enabled: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

- Iceberg v2 reads do not work on tables with deletion vectors enabled (though Apache Iceberg v3 supports deletion vectors).
- The Delta table must be accessed by name (not path) to automatically trigger Iceberg metadata generation.
- Iceberg reads cannot be enabled on [Materialized Views](/concepts/materialized-views-in-databricks.md) or Streaming Tables.
- Tables with Iceberg reads enabled do not support `VOID` types.
- Iceberg client support is read-only; writes are not supported.
- Data files use Zstandard compression instead of Snappy.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Lake Column Mapping](/concepts/delta-table-column-mapping.md)
- [OpenSharing](/concepts/opensharing.md)
- [Deletion Vectors](/concepts/deletion-vectors.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)

## Sources

- read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md

# Citations

1. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
