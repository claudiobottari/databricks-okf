---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf605ee941ce932be4ee0b5acdd563f68627eae29f85fe819f15faaba2abb367
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversion-caveats-and-file-visibility
    - File Visibility and Conversion Caveats
    - CCAFV
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Conversion Caveats and File Visibility
description: Post-conversion, untracked Parquet files become invisible to Delta Lake and can be deleted by VACUUM; writes must go through Delta Lake; multiple external tables sharing the same directory face access issues.
tags:
  - migration
  - delta-lake
  - parquet
timestamp: "2026-06-18T14:44:44.748Z"
---

# Conversion Caveats and File Visibility

**Conversion Caveats and File Visibility** refers to important considerations when using the `CONVERT TO DELTA` command to transform an existing Parquet or Iceberg table into a Delta table. Understanding these caveats helps prevent data loss, access issues, and metadata inconsistencies during and after the conversion process.

## Overview

The `CONVERT TO DELTA` command creates a Delta Lake transaction log from the files in a directory, making the data available as a Delta table. However, this operation introduces several constraints related to file visibility, concurrent access, and metadata management that users must account for.^[convert-to-delta-databricks-on-aws.md]

## Caveats

### Files Not Tracked by Delta Lake Become Invisible

Any file that is not tracked by the Delta Lake transaction log is invisible to Delta operations and can be deleted when `VACUUM` is run. To avoid unintended data loss, you should:

- Avoid updating or appending data files **during** the conversion process. During conversion, the Delta log is being created and any concurrent writes may produce files that are not recorded.
- After the table is converted, ensure **all writes go through Delta Lake**. Writing directly to the underlying directory will create files that Delta Lake does not track, making them invisible and eligible for deletion by `VACUUM`.^[convert-to-delta-databricks-on-aws.md]

### Multiple External Tables Sharing the Same Directory

It is possible that multiple external tables (e.g., in the Hive [Metastore](/concepts/metastore.md)) share the same underlying Parquet directory. If you run `CONVERT TO DELTA` on one of these external tables, the directory is converted from Parquet to Delta Lake. The other external tables will then be unable to access the data because their underlying directory is no longer in Parquet format. To restore access, you must run `CONVERT TO DELTA` on those external tables as well.^[convert-to-delta-databricks-on-aws.md]

### Metadata Consistency Checks

`CONVERT TO DELTA` populates the catalog information (such as schema and table properties) into the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and the existing Delta metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` error is thrown. To overwrite the existing Delta metadata in such cases, set the SQL configuration:

```
spark.databricks.delta.convert.metadataCheck.enabled = false
```

This is applicable when using Databricks Runtime.^[convert-to-delta-databricks-on-aws.md]

### Partitioning Requirements

When converting a table by path, the `PARTITIONED BY` clause is **required** for partitioned data. When converting a table by qualified table name (e.g., `database_name.table_name`), the partition specification is loaded from the [Metastore](/concepts/metastore.md) and the clause is optional. In either case, the conversion aborts with an error if the directory structure does not match the provided or loaded partitioning specification.^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – The full command syntax and parameters.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage layer for Delta tables.
- VACUUM – The operation that deletes files not tracked by the Delta log.
- [Liquid Clustering](/concepts/liquid-clustering.md) – Recommended post-conversion reorganization for better performance.
- External Tables – Tables that reference data stored outside the [Metastore](/concepts/metastore.md) location.
- [Delta transaction log](/concepts/delta-transaction-log.md) – The foundational metadata layer for Delta tables.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
