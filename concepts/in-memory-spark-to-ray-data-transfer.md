---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 428720ff42fb5af525e14ed5430773a0301963b8a067de9aa62d9ccb2ccf9385
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - in-memory-spark-to-ray-data-transfer
    - ISTRDT
    - In-memory Spark to Ray Transfer
    - in-memory-spark-to-ray-data-transfer-on-databricks
    - ISDTOD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
      start: 7
      end: 7
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
      start: 9
      end: 9
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
      start: 11
      end: 11
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
      start: 19
      end: 19
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
      start: 21
      end: 27
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
      start: 30
      end: 31
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
      start: 33
      end: 33
title: In-memory Spark to Ray Data Transfer
description: Using ray.data.from_spark() to efficiently transfer Spark DataFrames to Ray datasets without writing to disk, available on Databricks Runtime ML 15.0+.
tags:
  - databricks
  - ray
  - spark
  - data-transfer
timestamp: "2026-06-19T17:46:39.106Z"
---

```markdown
---
title: In-Memory Spark to Ray Data Transfer
summary: Using ray.data.from_spark() to directly transfer Spark DataFrames to Ray datasets in-memory without writing data to disk, available on Databricks Runtime ML 15.0+.
sources:
  - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:39:05.027Z"
updatedAt: "2026-06-19T14:17:23.541Z"
tags:
  - ray
  - spark
  - data-transfer
  - performance
aliases:
  - in-memory-spark-to-ray-data-transfer
  - ISTRDT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# In-Memory Spark to Ray Data Transfer

**In-Memory Spark to Ray Data Transfer** refers to the ability to directly convert a Spark DataFrame into a distributed Ray dataset without writing the data to disk or any intermediate storage location. This capability enables seamless data exchange between Apache Spark and Ray within the same execution environment on Databricks.

## Overview

Databricks supports running Ray and Spark operations in the same execution environment to leverage the strengths of both distributed computing engines. The in-memory transfer from Spark to Ray is a key integration pattern that eliminates the need for intermediate storage, reducing latency and simplifying workflows. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

This integration is supported by [[Delta Lake]] and [[Unity Catalog]], which provide robust data management, secure access, and lineage tracking across both frameworks. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Prerequisites

In-memory Spark to Ray transfers are available on **Databricks Runtime ML 15.0 and above**. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:7-7]

To enable this feature, you must set the following Spark cluster configuration **before starting your cluster**: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:9-9]

```
spark.databricks.pyspark.dataFrameChunk.enabled = true
^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:11-11]

## Usage

The primary API for in-memory transfer is `ray.data.from_spark()`, which directly reads a Spark DataFrame from Ray without writing data to any location. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:19-19]

```python
import ray

source_table = "my_db.my_table"

# Read a Spark DataFrame from a Delta table in Unity Catalog
df = spark.read.table(source_table)

# Convert to a Ray dataset in-memory
ray_ds = ray.data.from_spark(df)
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:21-27]

## Autoscaling Considerations

**Warning:** Autoscaling Spark clusters (including those using spot instances) must set the `use_spark_chunk_api` parameter to `False` when using the `from_spark()` function. Otherwise, the API call will result in cache misses because the cache on a Spark executor is lost when the executor terminates. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:30-31]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:33-33]

## Related Concepts

- [Combine Ray and Spark in the same environment on Databricks](/concepts/ray-spark-integration-on-databricks.md) — The broader integration framework for running both engines together.
- [Write Ray Data to Spark](/concepts/writing-ray-data-to-unity-catalog.md) — The reverse operation for transferring data from Ray back to Spark.
- Ray Data API — The Ray dataset abstraction used for distributed data processing.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports data exchange between Spark and Ray.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing data access and lineage.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
```

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
2. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:7-7](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
3. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:9-9](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
4. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:11-11](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
5. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:19-19](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
6. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:21-27](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
7. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:30-31](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
8. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md:33-33](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
