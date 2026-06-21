---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78bbeeb8ab43955f0537c8b69cf0538e685afc228b64de0bef706969f0c1fa12
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-disk-cache
    - DDC
    - Disk Cache
    - Disk cache
    - disk cache
  citations:
    - file: cache-select-databricks-on-aws.md
title: Databricks Disk Cache
description: Local caching layer on Databricks compute nodes that accelerates data access by storing frequently read data files in SSD-based local storage.
tags:
  - databricks
  - caching
  - optimization
  - storage
timestamp: "2026-06-19T17:43:35.455Z"
---

Here is the wiki page for **Databricks Disk Cache**, based solely on the provided source material.

---

# Databricks Disk Cache

**Databricks Disk Cache** is a local caching mechanism that stores data from remote storage on the local SSDs or instance storage attached to cluster worker nodes. It accelerates data reads by allowing subsequent queries to access cached copies locally rather than fetching data over the network from cloud storage. ^[cache-select-databricks-on-aws.md]

## How It Works

When a query reads data from a remote source such as a [Delta Lake](/concepts/delta-lake.md) table or Parquet files stored in cloud object storage, the disk cache checks whether a local copy of the data exists on the worker node. If not, the data is fetched from remote storage, cached locally, and served to the query. If a cached copy exists, the query reads directly from the local disk, bypassing the network round trip. ^[cache-select-databricks-on-aws.md]

The cache is maintained on a per-node basis—each worker node caches only the data it has accessed. The cache is automatically invalidated when the underlying data changes, ensuring queries always return fresh results. ^[cache-select-databricks-on-aws.md]

## CACHE SELECT Statement

The `CACHE SELECT` SQL statement provides explicit control over the disk cache. It caches the data accessed by a simple `SELECT` query, allowing users to specify which columns and rows to cache. This enables subsequent queries to avoid scanning the original files as much as possible. ^[cache-select-databricks-on-aws.md]

### Syntax

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

The `CACHE SELECT` construct is applicable only to [Delta Lake](/concepts/delta-lake.md) tables and Parquet tables. Views are also supported, but the expanded queries must remain simple queries as described above. ^[cache-select-databricks-on-aws.md]

## Benefits

- **Reduced query latency**: Frequently accessed data is served from local SSDs rather than fetched over the network from cloud storage. ^[cache-select-databricks-on-aws.md]
- **Lower cloud storage costs**: Repeated reads of the same data do not incur additional egress or read request charges from cloud storage. ^[cache-select-databricks-on-aws.md]
- **Improved cluster utilization**: Workers spend less time waiting for I/O and more time processing data. ^[cache-select-databricks-on-aws.md]

## Best Practices

- Use `CACHE SELECT` to pre-cache data that is accessed repeatedly by multiple queries, such as dimension tables or lookup tables. ^[cache-select-databricks-on-aws.md]
- Cache only the columns and rows you actually need to minimize local storage usage. ^[cache-select-databricks-on-aws.md]
- Monitor disk usage on worker nodes to ensure the cache does not consume all available local storage. ^[cache-select-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage format that works with the disk cache
- Databricks SQL — The query engine that leverages the disk cache
- Auto Optimize — Another optimization feature for Delta Lake
- Photon — The vectorized query engine that works alongside the disk cache
- [CACHE SELECT](/concepts/cache-select.md) — The SQL statement that explicitly controls the disk cache

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
