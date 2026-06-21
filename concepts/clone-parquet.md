---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9713d8025f124bb21f15e01be0add0de2d542260bb3b1a56f66bea834061438
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-parquet
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: CLONE Parquet
description: A Databricks SQL command to incrementally copy data from Parquet to Delta Lake, supporting both shallow and deep clones.
tags:
  - delta-lake
  - data-migration
  - sql
timestamp: "2026-06-19T19:32:16.368Z"
---

# CLONE Parquet

**CLONE Parquet** is a Databricks SQL command used to migrate data from a Parquet data lake to [Delta Lake](/concepts/delta-lake.md) by creating either a shallow or deep clone of the source Parquet files. It provides an incremental migration path that can copy data without disrupting the original Parquet data source. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Overview

CLONE Parquet is one of four main approaches for converting a Parquet data lake to Delta Lake. It offers flexibility through two distinct clone types—shallow and deep—each with different trade-offs regarding data duplication, file location, and write capabilities. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Shallow Clone

A shallow clone creates pointers to existing Parquet files without copying the underlying data. This approach maintains the original Parquet table in its original location and format while providing optimized access through collected file statistics. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

You can write to the table created by a shallow clone without impacting the original data source. This makes shallow clones useful for creating a Delta Lake interface over existing Parquet data while preserving the original format for legacy systems. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Deep Clone

A deep clone copies all data files from the source to a new location while converting the data to Delta Lake format. Deep clones support incremental migration by automatically detecting new files on subsequent executions of the clone logic, including backfill operations. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Syntax

The basic syntax for CLONE Parquet is:

```sql
CREATE OR REPLACE TABLE <target-table-name> [SHALLOW] CLONE parquet.`/path/to/data`;
```

The `SHALLOW` keyword is optional. Omitting it creates a deep clone by default. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Comparison with Other Migration Approaches

CLONE Parquet supports both incremental migration and backfill operations, distinguishing it from [CONVERT TO DELTA](/concepts/convert-to-delta.md), which is a one-time transformation of a Parquet directory into a Delta table. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

| Feature | CLONE Parquet | CONVERT TO DELTA | Auto Loader | Custom Spark Logic |
|---|---|---|---|---|
| Incremental | Yes | No | Yes | Varies |
| Maintains data structure | Yes | Yes | Yes | Varies |
| Backfill support | Yes | No | Yes | Varies |

^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Important Considerations

When using CLONE Parquet, note that shallow clones do not duplicate data—they maintain pointers to the original Parquet files. This means the original Parquet data remains in place and readable by Parquet-based systems, while the Delta clone provides a structured, queryable interface with optimized file statistics. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

For tables that are over-partitioned, performance may still be suboptimal even after conversion. Consider reviewing your partitioning strategy before migrating, as over-partitioned tables are a common cause of slow workloads on Delta Lake. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying format for the Databricks lakehouse
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — Alternative one-time migration approach
- Auto Loader — Incremental ingestion method for Parquet migration
- [Parquet to Delta Lake Migration](/concepts/parquet-to-delta-lake-migration.md) — Overall migration strategy guide
- Lakehouse Architecture — The data architecture enabled by Delta Lake

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
