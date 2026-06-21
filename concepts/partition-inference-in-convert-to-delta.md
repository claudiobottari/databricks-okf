---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d52608102dd65da59e619cf9306ac37ba36ff9e86ba288cefeb05dfae56ec64f
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-inference-in-convert-to-delta
    - PIICTD
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Partition Inference in CONVERT TO DELTA
description: CONVERT TO DELTA automatically infers partitioning information for Hive metastore tables but requires explicit partitioning for Unity Catalog external tables.
tags:
  - partitioning
  - delta-lake
  - hive-metastore
timestamp: "2026-06-19T17:52:59.609Z"
---

```markdown
---
title: Partition inference in CONVERT TO DELTA
summary: CONVERT TO DELTA automatically infers partitioning for Hive [[metastore|Metastore]] tables but requires explicit partition specification for Unity Catalog external tables.
sources:
  - convert-to-delta-lake-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:26:40.491Z"
updatedAt: "2026-06-19T14:26:40.491Z"
tags:
  - partitioning
  - delta-lake
  - unity-catalog
aliases:
  - partition-inference-in-convert-to-delta
  - PIICTD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Partition inference in CONVERT TO DELTA

**Partition inference in CONVERT TO DELTA** refers to the ability of the `CONVERT TO DELTA` command to automatically determine the partition columns of a source Parquet or Iceberg table and apply them to the resulting Delta table. The behavior differs depending on whether the table is registered in the Hive [[metastore|Metastore]] or managed by Unity Catalog.

## Automatic inference for Hive [[metastore|Metastore]] tables

For Databricks Runtime 11.3 LTS and above, when you run `CONVERT TO DELTA` on a Parquet or Iceberg table that is registered in the Hive [[metastore|Metastore]], the command automatically infers the partitioning information from the source table. You do not need to specify the partition columns manually. ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA my_hive_table;
```

The inferred partition columns are written into the Delta transaction log, allowing Delta Lake to recognise the existing directory structure.

## Manual specification for Unity Catalog external tables

Unity Catalog tables registered as external tables do not support automatic partition inference. When converting a Unity Catalog external Parquet or Iceberg table, you must explicitly provide the partition columns if the table is partitioned. ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog.schema.table_name PARTITIONED BY (date_updated DATE);
```

If you omit the `PARTITIONED BY` clause and the table is partitioned, the command may fail or produce incorrect results. This requirement applies to both Parquet and Iceberg [[external-tables-in-unity-catalog|External Tables in Unity Catalog]].

## Limitations

- **Iceberg partition evolution**: Converting Iceberg tables that have undergone partition evolution is not supported. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Iceberg truncated columns**: When converting Iceberg tables with partitions defined on truncated columns:
  - In Databricks Runtime 12.2 LTS and below, only `string` truncated columns are supported.
  - In Databricks Runtime 13.3 LTS and above, truncated columns of types `string`, `long`, or `int` are supported.
  - Databricks does not support truncated columns of type `decimal`. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Iceberg [[metastore|Metastore]] tables**: Converting Iceberg [[metastore|Metastore]] tables (as opposed to file directories) is not supported. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related concepts

- [[CONVERT TO DELTA]] – The broader SQL command for one-time conversion to Delta Lake.
- [[Delta Lake Partitioning Constraints|Delta Lake partitioning]] – How partition columns affect storage layout and query performance.
- Unity Catalog external tables – Tables whose data resides in cloud storage managed by Unity Catalog.
- [[Built-in Hive Metastore|Hive metastore]] – Legacy [[metastore|Metastore]] that stores table metadata, including partition information.

## Sources

- convert-to-delta-lake-databricks-on-aws.md
```

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
