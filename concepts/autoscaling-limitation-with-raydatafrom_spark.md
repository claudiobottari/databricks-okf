---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5ee42ea382c75dd7c9a15b8e48d9d1f818026f735142dcd95abf233f3d6a1ec
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autoscaling-limitation-with-raydatafrom_spark
    - ALWR
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Autoscaling Limitation with ray.data.from_spark()
description: Autoscaling Spark clusters (including spot instances) must set use_spark_chunk_api=False when using ray.data.from_spark() to avoid cache misses caused by executor termination.
tags:
  - ray
  - spark
  - autoscaling
  - limitations
timestamp: "2026-06-18T11:01:23.719Z"
---

# Autoscaling Limitation with `ray.data.from_spark()`

When using `ray.data.from_spark()` to create a distributed Ray dataset from a Spark DataFrame, autoscaling Spark clusters — including those using spot instances — must set the `use_spark_chunk_api` parameter to `False`. Failure to do so results in cache misses because the cache on a Spark executor is lost when the executor terminates during autoscaling events. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Background

The `ray.data.from_spark()` function enables in-memory transfer of Spark DataFrames to Ray datasets without writing data to disk. This feature is available on Databricks Runtime ML 15.0 and above. To enable it, you must set the Spark cluster configuration `spark.databricks.pyspark.dataFrameChunk.enabled` to `true` before starting your cluster. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## The Autoscaling Problem

Autoscaling Spark clusters dynamically add and remove executor nodes based on workload demands. When an executor is terminated during a scale-in event, any cached data chunks stored on that executor are lost. The `from_spark()` function's default chunk API relies on these caches, so subsequent attempts to read the lost chunks result in cache misses and API failures. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

This limitation applies to:
- Autoscaling Spark clusters
- Clusters using spot (preemptible) instances, which can be terminated at any time

## Workaround

To use `ray.data.from_spark()` with autoscaling or spot-instance clusters, set the `use_spark_chunk_api` parameter to `False`: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

When `use_spark_chunk_api=False`, the function uses an alternative data transfer mechanism that does not depend on executor-local caches, making it resilient to executor termination during autoscaling. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray and Spark Integration](/concepts/ray-and-spark-integration-on-databricks.md) — Overview of combining Ray and Spark on Databricks
- Ray Data — The Ray dataset abstraction for distributed data
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) — The primary Spark data abstraction
- Autoscaling Clusters — Databricks cluster autoscaling behavior
- Spot Instances — Preemptible cloud instances used for cost savings

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
