---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65d8d1a5269e01529028087cf89b99065a4f619174b0373b751534884570daf7
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-credential-propagation
    - DMCP
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: Databricks MLflow Credential Propagation
description: Method for passing Databricks MLflow tracking credentials to remote Ray workers using get_databricks_env_vars and environment variable updates.
tags:
  - databricks
  - mlflow
  - ray
  - authentication
timestamp: "2026-06-19T19:11:12.698Z"
---

# Databricks MLflow Credential Propagation

**Databricks MLflow Credential Propagation** refers to the mechanism by which MLflow authentication credentials are securely passed from a driver process to remote worker processes, such as those running in Ray Core tasks or [Ray Tune](/concepts/ray-tune.md) trials. This enables distributed workloads to log metrics, parameters, and models to the same MLflow tracking server without authentication failures.

## Overview

When running distributed workloads with Ray on Databricks, worker processes execute on remote nodes that do not automatically inherit the MLflow authentication context from the driver process. Without explicit credential propagation, attempts to call MLflow logging functions (such as `mlflow.log_metric()`) from within Ray tasks will fail because the MLflow Tracking Server is not initialized with the proper client credentials on the worker nodes. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Credential Retrieval

The `mlflow.utils.databricks_utils` module provides the `get_databricks_env_vars()` function, which retrieves the necessary environment variables for MLflow authentication within a Databricks workspace. This function returns a dictionary of environment variables that must be set on each worker process before MLflow operations can be performed. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
from mlflow.utils.databricks_utils import get_databricks_env_vars

mlflow_db_creds = get_databricks_env_vars("databricks")
```

## Propagation Pattern

The standard pattern for credential propagation involves three steps:

1. **Retrieve credentials** on the driver process using `get_databricks_env_vars()`.
2. **Pass credentials** to each remote task, typically as part of the task's configuration or by updating environment variables within the task.
3. **Apply credentials** inside each remote task by updating the process environment variables before any MLflow calls.

^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Example with Ray Core

The following example demonstrates credential propagation for Ray Core tasks:

```python
from mlflow.utils.databricks_utils import get_databricks_env_vars

mlflow_db_creds = get_databricks_env_vars("databricks")
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
        mlflow.log_metric("x", x)
    return x

with mlflow.start_run() as run:
    results = ray.get([ray_task.remote(x, run.info.run_id) for x in range(10)])
```

^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Example with Ray Tune

The same pattern applies to [Ray Tune](/concepts/ray-tune.md) hyperparameter tuning tasks:

```python
import os
import mlflow
from mlflow.utils.databricks_utils import get_databricks_env_vars

mlflow_db_creds = get_databricks_env_vars("databricks")
EXPERIMENT_NAME = "/Users/<WORKSPACE_USERNAME>/setup_mlflow_example"
mlflow.set_experiment(EXPERIMENT_NAME)

def train_function_mlflow(config, run_id):
    os.environ.update(mlflow_db_creds)
    mlflow.set_experiment(EXPERIMENT_NAME)
    with mlflow.start_run(run_id=run_id, nested=True):
        # Training logic with MLflow logging
        ...
```

^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Key Considerations

- **Environment variable scope**: Credentials must be applied within each remote task's process environment using `os.environ.update()`. Simply passing the credentials as function arguments is insufficient for MLflow's internal authentication mechanism. ^[integrate-mlflow-and-ray-databricks-on-aws.md]
- **Experiment setting**: After propagating credentials, each remote task should also call `mlflow.set_experiment()` to ensure the correct experiment context is established. ^[integrate-mlflow-and-ray-databricks-on-aws.md]
- **Child runs**: Credential propagation is commonly combined with the [MLflow Child Runs](/concepts/mlflow-child-run-pattern.md) pattern, where remote tasks log metrics to nested runs under a parent run created on the driver process. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core MLflow component for logging metrics, parameters, and artifacts.
- [MLflow Child Runs](/concepts/mlflow-child-run-pattern.md) — Hierarchical run structure used with credential propagation.
- Ray Core Integration with MLflow — General patterns for combining Ray and MLflow.
- Ray Tune Integration with MLflow — Hyperparameter tuning with MLflow tracking.
- Databricks Authentication for MLflow — Workspace-level authentication mechanisms.

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
