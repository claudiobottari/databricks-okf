---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf1c22a0f9e808d44dc636eca5c651ae8c53fada44f3db628bbf54fe804906a4
  pageDirectory: concepts
  sources:
    - when-to-use-spark-vs-ray-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - resource-management-in-combined-ray-spark-environments
    - RMICRE
  citations:
    - file: when-to-use-spark-vs-ray-databricks-on-aws.md
title: Resource Management in Combined Ray-Spark Environments
description: When combining Ray and Spark, resource conflicts can be managed by configuring CPU/memory/GPU allocation, e.g., using setup_ray_cluster to split resources between the two frameworks.
tags:
  - ray
  - spark
  - resource-management
  - databricks
timestamp: "2026-06-19T23:26:12.758Z"
---

# Resource Management in Combined Ray-Spark Environments

When Ray and Apache Spark run together on the same Databricks cluster, resource management ensures that both frameworks have sufficient memory, CPU, and/or GPU availability without contention. Although resource conflicts are rare due to task scheduling, explicit configuration can prevent resource starvation. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## When to Combine Ray and Spark

Shared-mode execution on Databricks allows running a Ray cluster within the same environment as Spark. This pattern is useful when a single application has both data-intensive stages (best handled by Spark) and computation-heavy stages (best handled by Ray). Common patterns include:

| Pattern | Description |
|---------|-------------|
| **Spark for data handling, Ray for computation** | Use Spark to manage input/output data (e.g., pass training data via `databricks.ray.data.from_spark`) and Ray to run complex computations. Save results to [MLflow](/concepts/mlflow.md) or [Unity Catalog](/concepts/unity-catalog.md). |
| **Ray inside a Spark function (advanced)** | Run Ray within Spark UDFs or Structured Streaming `foreachBatch` operations. |
| **Concurrent Spark and Ray operations (advanced)** | Run Spark queries and Ray functions simultaneously, e.g., Spark writes output while Ray processes. |

^[when-to-use-spark-vs-ray-databricks-on-aws.md]

An alternative pattern isolates the ETL stage into a separate Databricks Workflow subtask, which avoids resource sharing issues between the two engines. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## Resource Allocation Configuration

When combining Ray and Spark in a single task, configure the Ray cluster's node allocation to reserve resources for Spark. The example below uses `setup_ray_cluster` with explicit `min_worker_nodes` and `max_worker_nodes` to split cluster resources.

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

^[when-to-use-spark-vs-ray-databricks-on-aws.md]

In this example, the cluster uses autoscaling with a minimum of 4 and maximum of 6 worker nodes. The Ray cluster is fixed at 4 nodes, leaving 2 nodes (when scaling up) for Spark operations. Adjust the cluster size or the number of CPUs allocated to Ray worker nodes to prevent contention. ^[when-to-use-spark-vs-ray-databricks-on-aws.md]

## Best Practices

- **Match cluster type to workload**: For isolated ETL subtasks, use a separate cluster tuned for data processing.
- **Explicitly reserve resources**: Use `setup_ray_cluster` parameters to control how many nodes Ray consumes.
- **Monitor for conflicts**: Although rare, task scheduling can still cause contention; adjust allocation if Spark tasks are starved.

## Related Concepts

- Ray
- Apache Spark
- Databricks Workflow
- ETL
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- when-to-use-spark-vs-ray-databricks-on-aws.md

# Citations

1. [when-to-use-spark-vs-ray-databricks-on-aws.md](/references/when-to-use-spark-vs-ray-databricks-on-aws-bddbc4fb.md)
