---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c8e7b9e6d7a81cb99e4c2e56e891119fafcf478d8c0c2232d678abe955b80667
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-child-run-pattern
    - MCRP
    - MLflow Child Runs
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: MLflow Child Run Pattern
description: A hierarchical logging approach where a parent run is created in the driver process and each Ray task logs metrics to a nested child run under that parent.
tags:
  - mlflow
  - ray
  - logging
timestamp: "2026-06-19T19:11:28.169Z"
---

# MLflow Child Run Pattern

The **MLflow Child Run Pattern** is a hierarchical logging strategy that organizes related MLflow runs under a parent run, creating a tree-like structure for experiment tracking. This pattern is particularly useful when distributing computational work across multiple nodes or workers while maintaining coherent experiment organization.

## Overview

In distributed computing scenarios, when tasks run on remote workers, the MLflow Tracking Server may not be properly initialized to log metrics directly. The child run pattern addresses this by creating a parent run on the driver process and spawning nested child runs within each worker task. Each child run can independently log its own metrics, parameters, and artifacts while remaining associated with the parent run. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Implementation

### Core Pattern

The basic implementation involves three steps:

1. **Create a parent run** on the driver process
2. **Pass the parent `run_id`** to each worker task
3. **Create child runs** within each task using `nested=True`

```python
with mlflow.start_run() as parent_run:
    # Pass parent run_id to remote tasks
    results = ray.get([
        ray_task.remote(x, parent_run.info.run_id) 
        for x in range(10)
    ])
```

Within each task, the child run is created by passing the parent `run_id`:

```python
@ray.remote
def ray_task(x, run_id):
    with mlflow.start_run(run_id=run_id, nested=True):
        mlflow.log_metric("x", x)
    return x
```

^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Authentication and Credentials

For child runs in remote workers to function properly, each task must receive the necessary MLflow client credentials and the parent `run_id`. The credentials can be retrieved and passed using environment variables:

```python
from mlflow.utils.databricks_utils import get_databricks_env_vars
mlflow_db_creds = get_databricks_env_vars("databricks")
```

These credentials must be set within each remote task before creating child runs. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Use Cases

The child run pattern is used in several distributed computing frameworks:

- **Ray Core** — General-purpose distributed applications where tasks run across multiple nodes
- **[Ray Train](/concepts/ray-train-resource-allocation.md)** — Distributed model training with multiple workers
- **[Ray Tune](/concepts/ray-tune.md)** — Distributed hyperparameter tuning with multiple trials
- **[Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)** — Multi-GPU training where each GPU runs a separate training process

For each use case, the pattern maintains a clear hierarchy of experiment results, with the parent run serving as the main container and child runs representing individual tasks or trials. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Alternative: Direct Logging from Driver

When tasks return small artifacts (metrics, small data structures), it is often simpler and more reliable to log directly from the driver process rather than using child runs. This avoids the complexity of passing stateful references to remote workers:

```python
with mlflow.start_run() as run:
    results = ray.get([
        example_logging_task.remote(x) 
        for x in range(10)
    ])
    for x in results:
        mlflow.log_metric("x", x)
```

For large artifacts, Databricks recommends persisting artifacts as files and then logging them from the driver by specifying the file path. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — Core logging functionality for experiments
- Ray Distributed Computing — Framework for parallel task execution
- Experiment Organization — Best practices for structuring MLflow experiments
- [Nested Runs](/concepts/nested-mlflow-runs-for-tuning.md) — MLflow's built-in support for run hierarchies

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
