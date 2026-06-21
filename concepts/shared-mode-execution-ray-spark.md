---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dea0a23fb1ed9047f3f5460e8e828fd2ed7347f205b38105aad7a3ecf600ae6b
  pageDirectory: concepts
  sources:
    - when-to-use-spark-vs-ray-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-mode-execution-ray-spark
    - SME(+S
  citations:
    - file: when-to-use-spark-vs-ray-databricks-on-aws.md
title: Shared Mode Execution (Ray + Spark)
description: Running both Ray and Spark in the same execution environment on Databricks allows teams to use Spark for data-intensive tasks and Ray for heavy computation stages within a single application.
tags:
  - databricks
  - ray
  - spark
  - architecture
timestamp: "2026-06-19T23:26:03.006Z"
---

## Shared Mode Execution (Ray + Spark)

**Shared Mode Execution** refers to running a Ray cluster within the same Databricks environment as Apache Spark, enabling both frameworks to operate in a single application. This allows users to leverage Spark for data-intensive tasks (e.g., ETL, large‑scale data processing) and switch to Ray for computation‑heavy stages (e.g., deep learning training, hyperparameter search, reinforcement learning). ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Overview

On Databricks, you can run Ray and Spark operations in the same execution environment. Having both engines available provides a powerful solution to distribute nearly any type of Python application. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

Spark excels at **data parallelism** – applying the same operation to each element of a large dataset – while Ray excels at **task parallelism** – running a set of independent tasks concurrently. Shared mode execution combines these strengths. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### When to Use Shared Mode

Use shared mode when your workflow benefits from both frameworks in a single task:

- **Spark for data handling, Ray for computation** – Use Spark to manage input and output data operations (e.g., passing training data from Spark to Ray Data via `databricks.ray.data.from_spark`) and save results to [MLflow](/concepts/mlflow.md) or [Unity Catalog](/concepts/unity-catalog.md). ^[when-to-use-spark-vs-ray-databricks-on-aws.md]
- **Ray inside Spark functions (advanced)** – Run Ray within Spark UDFs or Structured Streaming `foreachBatch` operations. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]
- **Concurrent Spark and Ray operations (advanced)** – Run Spark queries or writes while Ray tasks are still executing. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

Alternatively, you can **isolate ETL in a subtask** using Databricks Workflows: separate the extract‑transform‑load (ETL) portion into its own subtask, matching the cluster type to the workload and avoiding resource sharing issues between Ray and Spark. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Resource Management

Resource conflicts between Ray and Spark are rare due to task scheduling, but can be managed by configuring resource allocation to ensure both frameworks have sufficient memory, CPU, or GPU availability. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

The following example uses `setup_ray_cluster` to split resources: ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

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

Adjust the cluster size or the number of CPUs allocated to Ray worker nodes as needed to prevent contention. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

### Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Spark on Databricks
- Databricks Workflows
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Hyperparameter search](/concepts/hyperparameter-tuning.md)
- Deep learning training

### Sources

- when-to-use-spark-vs-ray-databricks-on-aws.md

# Citations

1. [when-to-use-spark-vs-ray-databricks-on-aws.md](/references/when-to-use-spark-vs-ray-databricks-on-aws-bddbc4fb.md)
