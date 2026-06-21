---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0298818c19dfd4e9f3c123c24ec228ac218cc083019f9df21af8f7c6be325d94
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-core-mlflow-integration
    - RCMI
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: Ray Core MLflow Integration
description: Patterns for integrating MLflow tracking with Ray Core distributed applications, including driver-process logging and child-run approaches.
tags:
  - ray
  - mlflow
  - distributed-computing
timestamp: "2026-06-19T19:10:59.235Z"
---

# Ray Core MLflow Integration

**Ray Core MLflow Integration** describes the patterns and best practices for combining Ray Core, the foundational distributed computing framework, with [MLflow](/concepts/mlflow.md), the open-source AI engineering platform, to track models, metrics, parameters, and metadata generated during distributed training workloads. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Overview

MLflow enables teams to debug, evaluate, monitor, and optimize AI applications while controlling costs and managing access to models and data. Combining Ray with MLflow allows you to distribute workloads with Ray and track the resulting artifacts with MLflow. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Logging from the Ray Driver Process

The recommended approach for integrating Ray Core with MLflow is to log models and metrics from the **driver process** rather than from worker nodes. This avoids the complexity of passing stateful references to remote workers. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Why Not Log from Workers

The following code fails because the MLflow Tracking Server is not initialized using the `MLflow Client` from within worker nodes: ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
import mlflow

@ray.remote
def example_logging_task(x):
    # ...
    # This method will fail
    mlflow.log_metric("x", x)
    return x

with mlflow.start_run() as run:
    ray.get([example_logging_task.remote(x) for x in range(10)])
```

### Returning Metrics to the Driver

Instead, return metrics to the driver node and log them there. Metrics and metadata are generally small enough to transfer back without causing memory issues. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
import mlflow

@ray.remote
def example_logging_task(x):
    # ...
    return x

with mlflow.start_run() as run:
    results = ray.get([example_logging_task.remote(x) for x in range(10)])
    for x in results:
        mlflow.log_metric("x", x)
```

### Handling Large Artifacts

For tasks that require saving large artifacts (such as large Pandas tables, images, plots, or models), Databricks recommends persisting the artifact as a file. Then, either reload the artifact within the driver context or directly log the object with MLflow by specifying the path to the saved file. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
import mlflow

@ray.remote
def example_logging_task(x):
    # ...
    # Create a large object that needs to be stored
    with open("/dbfs/myLargeFilePath.txt", "w") as f:
        f.write(myLargeObject)
    return x

with mlflow.start_run() as run:
    results = ray.get([example_logging_task.remote(x) for x in range(10)])
    for x in results:
        mlflow.log_metric("x", x)
        # Directly log the saved file by specifying the path
        mlflow.log_artifact("/dbfs/myLargeFilePath.txt")
```

## Logging Ray Tasks as MLflow Child Runs

You can integrate Ray Core with MLflow by using **child runs** to establish a hierarchical relationship between the parent process and distributed tasks. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Implementation Steps

1. **Create a parent run**: Initialize a parent run in the driver process. This run acts as a hierarchical container for all subsequent child runs.
2. **Create child runs**: Within each Ray task, initiate a child run under the parent run. Each child run can independently log its own metrics.

To implement this approach, ensure that each Ray task receives the necessary client credentials and the parent `run_id`. This setup establishes the hierarchical parent-child relationship between runs. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
from mlflow.utils.databricks_utils import get_databricks_env_vars

mlflow_db_creds = get_databricks_env_vars("databricks")
username = ""  # Username path
experiment_name = f"/Users/{username}/mlflow_test"
mlflow.set_experiment(experiment_name)

@ray.remote
def ray_task(x, run_id):
    import os
    # Set the MLflow credentials within the Ray task
    os.environ.update(mlflow_db_creds)
    # Set the active MLflow experiment within each Ray task
    mlflow.set_experiment(experiment_name)
    # Create nested child runs associated with the parent run_id
    with mlflow.start_run(run_id=run_id, nested=True):
        # Log metrics to the child run within the Ray task
        mlflow.log_metric("x", x)
    return x

# Start parent run on the main driver process
with mlflow.start_run() as run:
    # Pass the parent run's run_id to each Ray task
    results = ray.get([ray_task.remote(x, run.info.run_id) for x in range(10)])
```

## Related Concepts

- Ray Train MLflow Integration — Logging distributed training models to MLflow
- [Ray Tune MLflow Integration](/concepts/ray-tune-mlflow-integration.md) — Tracking hyperparameter tuning experiments with MLflow
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for MLflow runs
- Distributed Computing with Ray — General-purpose distributed applications
- [Databricks MLflow Tracking](/concepts/databricks-mlflow-tracking-integration.md) — Platform-specific MLflow configuration

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
