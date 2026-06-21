---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2737bf5fd473d1fb33e55d874a76542b4887e2c1d3f8f6102abdca1c53442bec
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-table-conversion-caveats
    - ETCC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: External Table Conversion Caveats
description: Risks and limitations when converting external tables, including shared directory visibility issues and data integrity concerns during the conversion process.
tags:
  - delta-lake
  - external-tables
  - data-integrity
timestamp: "2026-06-19T17:52:48.659Z"
---

# External Table Conversion Caveats

**External Table Conversion Caveats** refers to the set of behaviors and restrictions that apply when using the `CONVERT TO DELTA` command on a table that is registered as an external (non-managed) External Table in the [Metastore](/concepts/metastore.md). The command converts the underlying data directory from Apache Parquet (or Iceberg) to [Delta Lake](/concepts/delta-lake.md) in-place, which can cause side effects for other tables or processes that share the same storage location.

## Sharing the Same Underlying Directory

It is possible that multiple external tables reference the same Parquet directory. If you run `CONVERT TO DELTA` on one of those external tables, the directory becomes a Delta Lake directory. The other external tables that point to the same location become inaccessible because their underlying format is no longer Parquet. To query or write to those tables again, you must also run `CONVERT TO DELTA` on each of them. ^[convert-to-delta-databricks-on-aws.md]

## Metadata Mismatch Between Catalog and Delta Transaction Log

`CONVERT TO DELTA` populates the [Metastore](/concepts/metastore.md) catalog information—such as schema and table properties—into the Delta Lake transaction log. If the underlying directory has already been converted to Delta and its metadata differs from the catalog metadata, the command throws a `convertMetastoreMetadataMismatchException`. ^[convert-to-delta-databricks-on-aws.md]

To override this check and overwrite the existing metadata in the Delta transaction log, you can set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false`. This option is available in Databricks Runtime. ^[convert-to-delta-databricks-on-aws.md]

## File Visibility and Vacuum

Any file present in the underlying directory that is not tracked by the Delta Lake transaction log becomes invisible to queries. These orphaned files can be deleted when you run `VACUUM`. To avoid data loss, you should not update or append data files during the conversion process. After the table is converted, all writes must go through Delta Lake operations; direct file manipulation outside of Delta can lead to data inconsistency. ^[convert-to-delta-databricks-on-aws.md]

## Partitioning Considerations

When the `table_name` is a path (rather than a qualified table name), the `PARTITIONED BY` clause is required for partitioned data. For qualified table identifiers registered in the [Metastore](/concepts/metastore.md), the partition specification is loaded from the [Metastore](/concepts/metastore.md) automatically. In both cases, the conversion aborts if the directory structure does not conform to the provided or loaded partition specification. ^[convert-to-delta-databricks-on-aws.md]

## Statistics Collection

By default, `CONVERT TO DELTA` collects statistics from Parquet file footers to improve query performance. You can bypass statistics collection by specifying the `NO STATISTICS` option, which speeds up the conversion. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics explicitly. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – Full syntax and parameters.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format after conversion.
- External Table – Tables whose data resides outside the [Metastore](/concepts/metastore.md) location.
- [Metastore](/concepts/metastore.md) – The catalog that stores table metadata.
- VACUUM – Cleanup operation that can delete untracked files.
- [Liquid Clustering](/concepts/liquid-clustering.md) – Recommended post-conversion data organization.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
