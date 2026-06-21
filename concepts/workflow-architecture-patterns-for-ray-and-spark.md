---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4abbc2c9a3f5c2aa8391916febd73bb84a281289153ab2ab82c3e222c47d788
  pageDirectory: concepts
  sources:
    - when-to-use-spark-vs-ray-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workflow-architecture-patterns-for-ray-and-spark
    - Spark and Workflow Architecture Patterns for Ray
    - WAPFRAS
  citations:
    - file: when-to-use-spark-vs-ray-databricks-on-aws.md
title: Workflow Architecture Patterns for Ray and Spark
description: Recommended patterns for integrating Ray and Spark pipelines include isolating ETL in a subtask, using Spark for data handling with Ray for computation, running Ray inside Spark functions (UDFs/foreachBatch), and concurrent Spark/Ray operations.
tags:
  - databricks
  - architecture
  - ray
  - spark
timestamp: "2026-06-19T23:25:59.876Z"
---

# Workflow Architecture Patterns for Ray and Spark

**Workflow Architecture Patterns for Ray and Spark** describe recommended approaches for integrating Ray and Apache Spark pipelines within the same workflow on Databricks. These patterns enable teams to leverage the strengths of both frameworks—Spark for data parallelism and Ray for task parallelism—in a single execution environment. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## Overview

Databricks allows you to run Ray and Spark operations in the same execution environment, providing a powerful solution for distributing nearly any type of Python application. The key architectural decision is how to structure the workflow to match each framework's strengths: Spark excels at [data parallelism](/concepts/data-parallelism-spark.md) (applying the same operation to each element of a large dataset), while Ray excels at [task parallelism](/concepts/task-parallelism-ray.md) (running a set of independent tasks concurrently). ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## Pattern 1: Isolate ETL in a Subtask

The first recommended pattern is to isolate the main data extract-transform-load (ETL) portion into its own subtask within a Databricks Workflow. This approach lets you match the cluster type to the type of ETL workload and avoids resource sharing issues between Ray and Spark. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## Pattern 2: Combine Ray and Spark in a Single Task

For workflows that require both frameworks within a single task, Databricks recommends one of the following sub-patterns: ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Spark for Data Handling, Ray for Computation

Use Spark to manage input and output data operations while Ray handles the computational workload. For example, use `databricks.ray.data.from_spark` to pass training data from Spark to Ray Data. Save the output model to [MLflow](/concepts/mlflow.md) or a data set to [Unity Catalog](/concepts/unity-catalog.md) tables. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Ray Inside a Spark Function (Advanced)

Run Ray within Spark functions like UDFs or [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) `foreachBatch` operations. This pattern is considered advanced and should be used when tight integration between the two frameworks is required within a single operation. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Concurrent Spark and Ray Operations (Advanced)

Run Spark operations alongside Ray functions. For example, use Spark to query data within Ray tasks or to write output data while Ray is still running. This pattern enables maximum parallelism between the two frameworks. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## Resource Management

Resource conflicts between Ray and Spark are rare due to task scheduling, but they can be managed by configuring resource allocation to ensure that both frameworks have sufficient memory, CPU, and/or GPU availability. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

The following example shows how to use setup configuration arguments when starting your Ray cluster to split resources between Ray and Spark. Adjust the cluster size or the number of CPUs allocated to Ray worker nodes as needed to prevent contention: ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

```python
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

# For a Databricks cluster configured with autoscaling enabled,
# the minimum worker nodes of 4 and maximum of 6 nodes.
# 2 Spark-only nodes will launch when needed.
# The Ray cluster will have 4 nodes allocated for its use.
setup_ray_cluster(
  min_worker_nodes=4,
  max_worker_nodes=4,
)

# Pass any custom Ray configuration with ray.init
ray.init()
```

## When to Use Each Pattern

- **Isolate ETL in a subtask**: Use when you want to match cluster types to workload types and avoid resource sharing issues between Ray and Spark. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]
- **Spark for data handling, Ray for computation**: Use for most combined workloads where Spark handles data-intensive operations and Ray handles computation-intensive operations. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]
- **Ray inside a Spark function**: Use for advanced scenarios requiring tight integration within a single operation. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]
- **Concurrent Spark and Ray operations**: Use for advanced scenarios requiring maximum parallelism between the two frameworks. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## Related Concepts

- When to Use Spark vs Ray
- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Apache Spark on Databricks
- Databricks Workflows
- Distributed Computing Patterns
- [Data Parallelism](/concepts/data-parallelism-spark.md)
- Task Parallelism

## Sources

- when-to-use-spark-vs-ray-databricks-on-aws.md

# Citations

1. [when-to-use-spark-vs-ray-databricks-on-aws.md](/references/when-to-use-spark-vs-ray-databricks-on-aws-bddbc4fb.md)
