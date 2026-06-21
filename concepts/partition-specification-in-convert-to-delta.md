---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7dcf52bf0412e3aa7c5523e256e258e708cf1227e3ece165a90bd3b62dd97971
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-specification-in-convert-to-delta
    - PSICTD
  citations:
    - file: convert-to-delta-databricks-on-aws.md
    - file: convert-to-databricks-on-aws.md
title: Partition Specification in CONVERT TO DELTA
description: The requirement and behavior of the PARTITIONED BY clause when converting partitioned Parquet tables to Delta Lake, including validation against actual directory structure.
tags:
  - delta-lake
  - partitioning
  - sql-command
timestamp: "2026-06-19T09:24:36.126Z"
---

# Partition Specification in CONVERT TO DELTA

**Partition Specification in CONVERT TO DELTA** refers to how the `PARTITIONED BY` clause is used when converting existing Apache Parquet or Iceberg tables to [Delta Lake](/concepts/delta-lake.md) format using the `CONVERT TO DELTA` SQL command. The partition specification ensures that the directory structure of the source data matches the expected partitioning scheme during the conversion process.^[convert-to-delta-databricks-on-aws.md]

## Syntax

The `PARTITIONED BY` clause is included in the `CONVERT TO DELTA` statement for partitioned data sources:

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Behavior by Source Type

The requirement for specifying partitions depends on how the table name is provided:

### Path-Based Conversion

When `table_name` is a path to a Parquet file directory (e.g., `parquet.\`s3://my-bucket/path/to/table\``), the `PARTITIONED BY` clause is **required** for partitioned data. The conversion process aborts and throws an exception if the directory structure does not conform to the provided partition specification.^[convert-to-delta-databricks-on-aws.md]

### Metastore-Registered Tables

When `table_name` is a qualified table identifier (e.g., `database_name.table_name`), the `PARTITIONED BY` clause is **optional**. In this case, partition information is loaded from the [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) or [Hive metastore](/concepts/built-in-hive-metastore.md). The conversion still validates that the directory structure matches the stored partition specification and aborts if there is a mismatch.^[convert-to-delta-databricks-on-aws.md]

### Iceberg Tables

For Apache Iceberg tables, you do **not** need to provide partitioning information. The converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. Note that Iceberg conversion only supports paths, as converting managed Iceberg tables is not supported.^[convert-to-delta-databricks-on-aws.md]

## Version-Specific Behavior

In Databricks Runtime 11.1 and below, `PARTITIONED BY` is a **required** argument for all partitioned data, regardless of whether the table is registered in the [Metastore](/concepts/metastore.md).^[convert-to-delta-databricks-on-aws.md]

## Examples

The following examples illustrate partition specification for different scenarios:

```sql
-- Parquet table registered in [[metastore|Metastore]] (partition info loaded automatically)
CONVERT TO DELTA database_name.table_name;

-- Partitioned Parquet table by path (PARTITIONED BY is required)
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table`
  PARTITIONED BY (date DATE);

-- Iceberg table (partition info loaded from Iceberg manifest)
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

## Validation and Error Handling

The conversion process validates that the directory structure of the source data matches the partition specification. If the directory structure does not conform, the command aborts and throws an exception. This validation ensures that the converted Delta table accurately represents the underlying data organization.^[convert-to-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The full SQL command for converting Parquet and Iceberg tables to Delta Lake
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that enables ACID transactions and scalable metadata handling
- Partitioned Tables — Tables organized by partition columns for query performance
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended post-conversion reorganization for data layout and statistics
- VACUUM — Command to clean up files not tracked by Delta Lake after conversion
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — Centralized metadata repository for table registration

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
2. convert-to-databricks-on-aws.md
