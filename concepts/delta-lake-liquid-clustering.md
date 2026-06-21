---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64b3be84714e50f7866ea1d25876d558e0d77aba47cfb6bf4856ad22ec6b1f02
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
    - tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-liquid-clustering
    - DLLC
    - Delta Lake Clustering
    - Table clustering
  citations:
    - file: tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Delta Lake Liquid Clustering
description: A data organization technique in Delta Lake where data is clustered by specified columns, and operations like certain commands may only reference those clustering columns.
tags:
  - databricks
  - delta-lake
  - clustering
  - data-optimization
timestamp: "2026-06-18T15:24:38.542Z"
---

# Delta Lake Liquid Clustering

**Delta Lake Liquid Clustering** is a data layout optimization technique for [Delta Lake](/concepts/delta-lake.md) tables that colocates related data to improve read query performance. It replaces traditional partitioning and [Z-ordering](/concepts/z-ordering-delta-lake.md) as the recommended approach for data clustering on Databricks. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

## Overview

Liquid clustering reorganizes data within a table so that rows with similar values in specified columns are stored together physically. This colocation reduces the amount of data that queries need to scan, leading to faster read performance, especially for selective queries on the clustering columns. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

## Enabling Liquid Clustering

To enable liquid clustering on an existing table, use the `ALTER TABLE` command with the `CLUSTER BY` clause, specifying one or more columns to cluster by. After enabling clustering, run `OPTIMIZE FULL` to apply the clustering layout to all existing data in the table. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

```sql
ALTER TABLE workspace.default.people_10k CLUSTER BY (firstName);
OPTIMIZE FULL workspace.default.people_10k;
```

The `CLUSTER BY` clause accepts one or more column names. Liquid clustering works well with high-cardinality columns, such as `firstName` in the example above. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

## Relationship to OPTIMIZE

Liquid clustering is applied through the OPTIMIZE command. While the standard `OPTIMIZE` operation combines small files into larger ones to improve read performance, `OPTIMIZE FULL` additionally applies the liquid clustering layout to all data in the table. For ongoing maintenance, subsequent `OPTIMIZE` operations incrementally maintain the clustering layout as new data is written. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

## Benefits

- **Improved read performance**: Queries that filter on clustering columns scan fewer files because related data is colocated. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]
- **Flexible clustering keys**: Unlike partitioning, liquid clustering supports high-cardinality columns and multiple clustering keys without creating an excessive number of directories. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]
- **Incremental maintenance**: As new data is written, subsequent `OPTIMIZE` operations maintain the clustering layout without requiring a full rewrite. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

## Limitations

Liquid clustering has certain constraints on which commands and predicates are supported. For example, some commands that reference non-clustering columns may not be supported on liquid-clustered tables. See the DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error class|DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error condition for details on unsupported operations. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides the foundation for tables on Databricks
- OPTIMIZE — The command used to compact files and apply clustering
- [Z-ordering](/concepts/z-ordering-delta-lake.md) — An earlier clustering technique that liquid clustering replaces
- [Table partitioning](/concepts/delta-table-partitioning-mismatch.md) — A traditional data organization method with different trade-offs
- DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error class|DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error condition — Error conditions for unsupported operations on liquid-clustered tables

## Sources

- tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md](/references/tutorial-create-and-manage-delta-lake-tables-databricks-on-aws-481179d7.md)
2. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
