---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 174038c54bdb12dec3cc90c1dc53f658a2511fda26aa3d979c332b69513b2544
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-managed-tables
    - UCMT
    - Unity Catalog Managed Storage
    - Unity Catalog Managed Table
    - Unity Catalog Managed Volumes
    - Unity Catalog managed storage
    - Unity Catalog managed table
    - Managed Table
    - Managed Table|managed tables
    - Managed table
    - Unity Catalog managed tables in Databricks for Delta Lake and Apache Iceberg
    - managed table
  citations:
    - file: managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
    - file: best-practices-delta-lake-databricks-on-aws.md
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: Unity Catalog Managed Tables
description: Databricks recommendation to use Unity Catalog managed tables for Delta Lake workloads, with automatic optimization and governance.
tags:
  - databricks
  - governance
  - table-management
timestamp: "2026-06-19T17:39:58.094Z"
---

# Unity Catalog Managed Tables

A **Unity Catalog managed table** is a table where [Unity Catalog](/concepts/unity-catalog.md) controls both governance (access control, auditing, lineage) and the underlying file storage lifecycle — including file optimization, organization, and deletion. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

Managed tables always use the [Delta Lake](/concepts/delta-lake.md) or [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) format. When you drop a managed table, Unity Catalog deletes the underlying data files. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Overview

Every securable object registered in Unity Catalog is centrally governed — Unity Catalog manages the object's metadata, controlling access, auditing, and lineage. For data assets like tables, Unity Catalog can additionally control the storage location and lifecycle of the underlying data files in your cloud account. This distinction separates **managed** from [Unity Catalog External Tables|external data assets](/concepts/unity-catalog-external-table-conversion.md). ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

When you register a managed table, you retain full ownership of your data. The data files always remain in your cloud account. Unity Catalog determines where within your account they are stored, but does not transfer them to Databricks or own them. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Storage Location

Unity Catalog stores managed tables in the managed storage location defined on the containing schema, catalog, or [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md). ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Comparison with External Tables

| Aspect | Managed Table | External Table |
|--------|---------------|----------------|
| Storage location | Determined by Unity Catalog | Specified by the user |
| Data lifecycle | Controlled by Unity Catalog | Controlled by the user or external system |
| When dropped | Underlying data files are deleted | Metadata is removed; data files remain |
| Supported formats | Delta, Apache Iceberg | Delta, CSV, JSON, Avro, Parquet, ORC |

Both managed and external tables support read, write, and create access from external engines via open APIs, including the Unity REST API and the Iceberg REST Catalog (IRC). This means that managed tables do not cause vendor lock-in — any engine that supports these APIs can access managed tables. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Best Practices

Databricks recommends using Unity Catalog managed tables for most workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

When combined with managed tables, Databricks recommends:

- Using [predictive optimization](/concepts/delta-lake-predictive-optimization.md), which automatically runs `OPTIMIZE` and `VACUUM` commands on Unity Catalog managed tables. ^[best-practices-delta-lake-databricks-on-aws.md]
- Using [Liquid Clustering](/concepts/liquid-clustering.md) for table organization. ^[best-practices-delta-lake-databricks-on-aws.md]
- When deleting and recreating a table in the same location, always using a `CREATE OR REPLACE TABLE` statement. ^[best-practices-delta-lake-databricks-on-aws.md]

## Migration from Hive [Metastore](/concepts/metastore.md)

You can upgrade Hive managed tables to Unity Catalog managed tables using either:

- **`CREATE TABLE CLONE`**: Deep clone a managed Delta table from the Hive [Metastore](/concepts/metastore.md) to a managed table in Unity Catalog. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **`CREATE TABLE AS SELECT`**: Create a new managed table in Unity Catalog by querying the Hive table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

Managed tables are the preferred way to create tables in Unity Catalog. Unity Catalog fully manages their lifecycle, file layout, and storage, and optimizes their performance automatically. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Retention of Existing Data Layout

When using [Low Shuffle Merge](/concepts/low-shuffle-merge.md) on managed tables, the optimization preserves existing data layout optimizations such as liquid clustering on unmodified data. ^[best-practices-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog External Tables](/concepts/unity-catalog-external-table-conversion.md)
- Unity Catalog Managed Volumes
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md)
- Predictive Optimization
- [Liquid Clustering](/concepts/liquid-clustering.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg on Databricks](/concepts/uniform-apache-iceberg-format-in-databricks.md)
- Upgrade Hive Tables to Unity Catalog

## Sources

- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
- best-practices-delta-lake-databricks-on-aws.md
- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md](/references/managed-versus-external-assets-in-unity-catalog-databricks-on-aws-581e1fb1.md)
2. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
3. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
