---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91798edaea59a6d5af303581137c241203396809a95fcf2b3cb58786d53ece93
  pageDirectory: concepts
  sources:
    - when-to-use-spark-vs-ray-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ray-spark-integration
    - DRI
  citations:
    - file: when-to-use-spark-vs-ray-databricks-on-aws.md
title: Databricks Ray-Spark Integration
description: Databricks provides native integration for running Ray and Spark in the same environment, including utilities like databricks.ray.data.from_spark for seamless data passing between the frameworks.
tags:
  - databricks
  - ray
  - spark
  - integration
timestamp: "2026-06-19T23:26:34.873Z"
---

Here is the wiki page for "Databricks Ray-Spark Integration", based solely on the provided source material.

## Databricks Ray-Spark Integration

**Databricks Ray-Spark Integration** refers to the ability to run both Ray and Apache Spark operations within the same execution environment on the Databricks platform. This integration provides a powerful solution for distributing nearly any type of Python application by leveraging the strengths of each framework for specific tasks.^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Framework Characteristics

The two frameworks have distinct advantages for different task types:

- **Ray** excels at **task parallelism** — running a set of independent tasks concurrently. It is designed for computation-focused workloads where Spark is less optimized, such as [Reinforcement Learning|reinforcement learning](/concepts/trl-transformer-reinforcement-learning.md), Hierarchical Time Series Forecasting|hierarchical time series forecasting, Simulation Modeling|simulation modeling, Hyperparameter Search|hyperparameter search, Deep Learning Training|deep learning training, and High Performance Computing (HPC)|high-performance computing (HPC).^[when-to-use-spark-vs-ray-databricks-on-aws.md]
- **Spark** excels at **data parallelism** — applying the same operation to each element of a large dataset. It is optimized for large-scale data processing tasks like table joins, filtering, and aggregation, making it ideal for Extract-Transform-Load (ETL)|ETL, analytics reporting, feature engineering, and data preprocessing. Spark's MLlib and SparkML libraries are optimized for large-scale machine learning algorithms and statistical modeling.^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### When to Use Both Frameworks

Shared mode execution allows running a Ray cluster within the same environment as Spark, enabling both frameworks to be used in a single application. A common pattern is to use Spark for data-intensive tasks (like efficient data retrieval) and switch to Ray for stages that require heavy computation.^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Workflow Architecture Patterns

The following are recommended patterns for integrating Spark and Ray pipelines within the same workflow:

- **Isolate ETL in a subtask**: The main ETL portion can be isolated into its own subtask within a Databricks Workflow. This allows matching the cluster type to the ETL workload and avoids resource sharing issues between Ray and Spark.^[when-to-use-spark-vs-ray-databricks-on-aws.md]
- **Combine Ray and Spark in a single task**: Databricks recommends one of three patterns:
    1. **Spark for data handling, Ray for computation**: Use Spark to manage input and output data operations (e.g., pass training data from Spark to Ray Data using `databricks.ray.data.from_spark`, then save output to [MLflow](/concepts/mlflow.md) or [Unity Catalog](/concepts/unity-catalog.md)).
    2. **Ray inside a Spark function (advanced)**: Run Ray within Spark functions like UDFs or Structured Streaming `foreachBatch` operations.
    3. **Concurrent Spark and Ray operations (advanced)**: Run Spark operations alongside Ray functions (e.g., using Spark to query data within Ray tasks or to write output data while Ray is still running).^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Resource Management

Resource conflicts are rare due to task scheduling but can be managed by configuring resource allocation to ensure both frameworks have sufficient memory, CPU, and/or GPU availability. The following example demonstrates using setup configuration arguments when starting a Ray cluster to split resources between Ray and Spark:^[when-to-use-spark-vs-ray-databricks-on-aws.md]

```python
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

# For a Databricks cluster configured with autoscaling enabled,
# The minimum worker nodes of 4 and maximum of 6 nodes.
# 2 Spark-only nodes will launch when needed.
# The Ray cluster will have 4 nodes allocated for its use.
setup_ray_cluster(
  min_worker_nodes=4,
  max_worker_nodes=4,
)
# Pass any custom Ray configuration with ray.init
ray.init()
```

### Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Spark on Databricks
- Ray Data Integration
- Connect Spark and Ray
- Databricks Workflows

### Sources

- when-to-use-spark-vs-ray-databricks-on-aws.md

# Citations

1. [when-to-use-spark-vs-ray-databricks-on-aws.md](/references/when-to-use-spark-vs-ray-databricks-on-aws-bddbc4fb.md)
