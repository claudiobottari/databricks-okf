---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8995fe744a7cd45ad9aa4c91b990eaf3aee40624d3d0925568b15f3cc7ba27f8
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - in-memory-spark-to-ray-data-transfer-on-databricks
    - ISDTOD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: In-memory Spark-to-Ray Data Transfer on Databricks
description: Using ray.data.from_spark() to transfer Spark DataFrames to Ray datasets in-memory without writing to disk, available on Databricks Runtime ML 15.0+
tags:
  - ray
  - spark
  - data-transfer
  - databricks
timestamp: "2026-06-19T09:17:09.539Z"
---

# In-memory Spark-to-Ray Data Transfer on Databricks

**In-memory Spark-to-Ray Data Transfer on Databricks** refers to the ability to directly convert a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) into a distributed Ray Dataset without writing data to disk or an external storage location. This capability enables seamless data exchange between the two distributed computing engines within the same execution environment.

## Overview

Databricks supports running Ray and Spark operations in the same execution environment, allowing users to leverage the strengths of both distributed computing engines. The integration is supported by [Delta Lake](/concepts/delta-lake.md) and [Unity Catalog](/concepts/unity-catalog.md), which provide robust data management, secure access, and lineage tracking. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

In-memory Spark-to-Ray data transfer is available on **Databricks Runtime ML 15.0 and above**. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Enabling the Feature

To use in-memory Spark-to-Ray data transfer, you must set the following Spark cluster configuration **before starting your cluster**: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```
spark.databricks.pyspark.dataFrameChunk.enabled = true
```

## Usage

Once the configuration is set, you can create a distributed Ray dataset directly from a Spark DataFrame using the `ray.data.from_spark()` function: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

source_table = "my_db.my_table"

# Read a Spark DataFrame from a Delta table in Unity Catalog
df = spark.read.table(source_table)

# Convert to Ray dataset in-memory
ray_ds = ray.data.from_spark(df)
```

This approach reads the Spark DataFrame directly from Ray without needing to write the data to any intermediate location. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Autoscaling Considerations

When using autoscaling Spark clusters (including those using spot instances), you must set the `use_spark_chunk_api` parameter to `False` when calling `from_spark()`. This is necessary because the cache on a Spark executor is lost when the executor terminates, which would otherwise result in cache misses. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

## Best Practices

- Always follow the [Ray cluster best practice guide](/concepts/ray-cluster-scaling-best-practices.md) to ensure the cluster is fully utilized. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Ensure that the `num_cpus_worker_node` configuration matches the number of CPU cores on the Spark worker node, and similarly set `num_gpus_worker_node` to match the number of GPUs per Spark worker node. In this configuration, each Spark worker node launches one Ray worker node that fully utilizes the resources of the Spark worker node. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md) — Overview of running Ray workloads on Databricks
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) — The source data structure for in-memory transfer
- Ray Dataset — The target distributed dataset format
- [Write Ray Data to Spark](/concepts/writing-ray-data-to-unity-catalog.md) — The reverse operation for transferring data from Ray back to Spark
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime version that supports this feature
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and lineage for Ray-Spark integration

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
