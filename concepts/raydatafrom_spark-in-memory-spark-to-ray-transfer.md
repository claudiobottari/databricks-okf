---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93ff7188a903747493ae6b2409879ca9094150cac3249c2e911d41c746069d18
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - raydatafrom_spark-in-memory-spark-to-ray-transfer
    - R—IST
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: ray.data.from_spark() — In-Memory Spark-to-Ray Transfer
description: Transfer Spark DataFrames to Ray datasets in-memory using ray.data.from_spark(), avoiding intermediate storage writes; available on Databricks Runtime ML 15.0+ with a required cluster config.
tags:
  - ray
  - spark
  - databricks
  - data-transfer
timestamp: "2026-06-18T11:00:57.516Z"
---

# ray.data.from_spark() — In-Memory Spark-to-Ray Transfer

**`ray.data.from_spark()`** is a function in the Ray Data API that directly reads a Spark DataFrame into a distributed Ray dataset without writing data to any intermediate storage location. This enables efficient in-memory transfer between Spark and Ray within the same execution environment on Databricks. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Prerequisites

In-memory Spark-to-Ray transfers using `ray.data.from_spark()` are supported on **Databricks Runtime ML 15.0 and above**. The following cluster configuration must be set before starting the cluster: `spark.databricks.pyspark.dataFrameChunk.enabled = true`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Usage

The basic usage is straightforward. After reading a Spark DataFrame from a Delta table (or any other source), you call `ray.data.from_spark(df)` to convert it into a `ray.data.Dataset`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

source_table = "my_db.my_table"
df = spark.read.table(source_table)
ray_ds = ray.data.from_spark(df)
```

## Handling Autoscaling Clusters

**Warning:** Autoscaling Spark clusters (including those using spot instances) must set the `use_spark_chunk_api` parameter to `False` when calling `from_spark()`. Otherwise, the API call will result in cache misses because the cache on a Spark executor is lost when the executor terminates. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

## Best Practices

- Always review the [Ray cluster best practices](/concepts/ray-cluster-scaling-best-practices.md) to ensure full utilization of cluster resources.
- For data that will be consumed repeatedly, consider calling `.materialize()` on the resulting Ray dataset to persist it in the Ray distributed object store.
- When working with [Unity Catalog](/concepts/unity-catalog.md) tables, the in-memory transfer respects access controls and lineage tracking provided by the catalog. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- The `use_spark_chunk_api` parameter must be set to `False` on autoscaling clusters or clusters using spot instances to avoid data loss from cache eviction.
- This method requires the Spark DataFrame to be available in the same Python process; it does not work for transferring data from a remote Spark context without additional setup.
- The feature is only available on Databricks Runtime ML 15.0 and later. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray – The distributed computing framework underlying Ray Data
- Ray Data – The dataset abstraction for Ray
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) – The primary data structure in Apache Spark
- [Delta Lake](/concepts/delta-lake.md) – Storage layer for reliable data lakes
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance and access control
- Ray Data to Unity Catalog via write_databricks_table()|Ray Data write_databricks_table – The complementary function for writing Ray data back to Unity Catalog tables
- Combine Ray and Spark – General guidance on using both engines together

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
