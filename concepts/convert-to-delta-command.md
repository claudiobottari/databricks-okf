---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fbfadbb6fca8d1ee1d5a63202fda7a8043589245283dc96ee09c7e1fdf1ca54e
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - convert-to-delta-command
    - CTDC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: CONVERT TO DELTA Command
description: A SQL command that converts existing Apache Parquet or Iceberg tables to Delta tables in-place by creating a Delta Lake transaction log.
tags:
  - delta-lake
  - sql-command
  - table-conversion
timestamp: "2026-06-19T17:52:31.165Z"
---

```markdown
---
title: CONVERT TO DELTA Command
summary: A Databricks SQL command that converts existing Apache Parquet or Iceberg tables to Delta Lake format in-place by creating a Delta Lake transaction log and inferring the schema.
sources:
  - convert-to-delta-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:44:31.131Z"
updatedAt: "2026-06-19T16:00:00.000Z"
tags:
  - delta-lake
  - sql-command
  - data-migration
aliases:
  - convert-to-delta-command
  - CTDC
confidence: 1.0
provenanceState: extracted
inferredParagraphs: 0
---

# CONVERT TO DELTA Command

The **CONVERT TO DELTA** command converts an existing Apache Parquet table to a [[Delta Lake]] table in-place. It lists all files in the directory, creates a Delta Lake transaction log that tracks these files, and automatically infers the data schema by reading the footers of all Parquet files. The conversion process collects statistics to improve query performance on the converted Delta table. If you provide a table name, the [[metastore|Metastore]] is also updated to reflect that the table is now a Delta table. ^[convert-to-delta-databricks-on-aws.md]

This command also supports converting Apache Iceberg tables whose underlying file format is Parquet. In this case, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. ^[convert-to-delta-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

- **table_name**: Either an optionally qualified table identifier or a path to a `parquet` or `iceberg` file directory. The name must not include a temporal specification or options specification. For Iceberg tables, you can only use paths, as converting managed Iceberg tables is not supported. ^[convert-to-delta-databricks-on-aws.md]

- **NO STATISTICS**: Bypasses statistics collection during the conversion process to finish conversion faster. After the table is converted to Delta Lake, Databricks recommends using [[liquid clustering]] to reorganize the data layout and generate statistics. ^[convert-to-delta-databricks-on-aws.md]

- **PARTITIONED BY**: Partitions the created table by the specified columns. When `table_name` is a path, `PARTITIONED BY` is required for partitioned data. When `table_name` is a qualified table identifier, `PARTITIONED BY` is optional and the partition specification is loaded from the [[metastore|Metastore]]. In either approach, the conversion process aborts and throws an exception if the directory structure does not conform to the provided or loaded `PARTITIONED BY` specification. In Databricks Runtime 11.1 and below, `PARTITIONED BY` is a required argument for all partitioned data. ^[convert-to-delta-databricks-on-aws.md]

## Examples

```sql
-- Convert a Parquet table registered in the [Metastore](/concepts/metastore.md)
CONVERT TO DELTA database_name.table_name;

-- Convert a partitioned Parquet table by path
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table` PARTITIONED BY (date DATE);

-- Convert an Iceberg table (uses Iceberg manifest for metadata)
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

## Caveats

Any file not tracked by Delta Lake is invisible and can be deleted when you run `VACUUM`. You should avoid updating or appending data files during the conversion process. After the table is converted, make sure all writes go through Delta Lake. ^[convert-to-delta-databricks-on-aws.md]

It is possible that multiple external tables share the same underlying Parquet directory. If you run `CONVERT` on one external table, you will not be able to access the other external tables because their underlying directory has been converted from Parquet to Delta Lake. To query or write to these external tables again, you must run `CONVERT` on them as well. ^[convert-to-delta-databricks-on-aws.md]

`CONVERT` populates catalog information, such as schema and table properties, to the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. While using Databricks Runtime, if you want `CONVERT` to overwrite the existing metadata in the Delta Lake transaction log, set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to false. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] — The underlying format in the Databricks lakehouse
- [[VACUUM Command (Databricks)|VACUUM Command]] — Removes files not tracked by Delta Lake
- [[Liquid Clustering]] — Reorganizes data layout and generates statistics after conversion
- [[Parquet to Delta Lake Migration]] — Broader migration strategies and considerations

## Sources

- convert-to-delta-databricks-on-aws.md
```

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
