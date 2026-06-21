---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b3b37b1b985e0abfdc45586460df40edf58a48fbc54311cf6ac295d70f64cc28
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-tune-mlflow-integration
    - RTMI
    - Ray Train MLflow Integration
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: Ray Tune MLflow Integration
description: Integration of Ray Tune distributed hyperparameter tuning with MLflow experiment tracking using child runs and the MLflowLoggerCallback.
tags:
  - ray
  - mlflow
  - hyperparameter-tuning
timestamp: "2026-06-19T19:11:13.236Z"
---

# Ray Tune MLflow Integration

**Ray Tune MLflow Integration** refers to the combination of [Ray Tune](/concepts/ray-tune.md), a distributed hyperparameter tuning library, with [MLflow](/concepts/mlflow.md), an open source AI engineering platform for tracking experiments, metrics, and models. This integration allows you to efficiently track and log hyperparameter tuning experiments within Databricks, leveraging MLflow's experiment-tracking capabilities to record metrics and results directly from Ray tasks. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Overview

Integrating Ray Tune with MLflow enables teams to distribute hyperparameter tuning workloads across multiple nodes while maintaining comprehensive experiment tracking. MLflow records metrics, parameters, and metadata generated during training, providing a centralized repository for all tuning results. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Child-Run Approach for Logging

Similar to logging from Ray Core tasks, Ray Tune applications can use a child-run approach to log metrics from each trial or tuning iteration. This approach maintains a clear hierarchy of experiment results. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Implementation Steps

1. **Create a parent run**: Initialize a parent run in the driver process. This run serves as the main container for all subsequent child runs.
2. **Log child runs**: Each Ray Tune task creates a child run under the parent run, maintaining a clear hierarchy of experiment results.

^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Authentication and Setup

To authenticate and log from Ray Tune tasks using MLflow, you must retrieve Databricks environment variables and pass the parent `run_id` to each Ray Tune task. The following example demonstrates this pattern: ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
import os
import tempfile
import time
import mlflow
from mlflow.utils.databricks_utils import get_databricks_env_vars
from ray import train, tune
from ray.air.integrations.mlflow import MLflowLoggerCallback, setup_mlflow

mlflow_db_creds = get_databricks_env_vars("databricks")
EXPERIMENT_NAME = "/Users/<WORKSPACE_USERNAME>/setup_mlflow_example"
mlflow.set_experiment(EXPERIMENT_NAME)

def evaluation_fn(step, width, height):
   return (0.1 + width * step / 100) ** (-1) + height * 0.1

def train_function_mlflow(config, run_id):
   os.environ.update(mlflow_db_creds)
   mlflow.set_experiment(EXPERIMENT_NAME)
   # Hyperparameters
   width = config["width"]
   height = config["height"]
   with mlflow.start_run(run_id=run_id, nested=True):
       for step in range(config.get("steps", 100)):
           # Iterative training function - can be any arbitrary training procedure
           intermediate_score = evaluation_fn(step, width, height)
           # Log the metrics to MLflow
           mlflow.log_metrics({"iterations": step, "mean_loss": intermediate_score})
           # Feed the score back to Tune.
           train.report({"iterations": step, "mean_loss": intermediate_score})
           time.sleep(0.1)

def tune_with_setup(run_id, finish_fast=True):
   os.environ.update(mlflow_db_creds)
   # Set the experiment or create a new one if it does not exist.
   mlflow.set_experiment(experiment_name=EXPERIMENT_NAME)
   tuner = tune.Tuner(
       tune.with_parameter(train_function_mlflow, run_id),
       tune_config=tune.TuneConfig(num_samples=5),
       run_config=train.RunConfig(
           name="mlflow",
       ),
       param_space={
           "width": tune.randint(10, 100),
           "height": tune.randint(0, 100),
           "steps": 20 if finish_fast else 100,
       },
   )
   results = tuner.fit()

with mlflow.start_run() as run:
   mlflow_tracking_uri = mlflow.get_tracking_uri()
   tune_with_setup(run.info.run_id)
```

## Key Components

### Parent Run

The parent run is initialized in the driver process and acts as a hierarchical container for all subsequent child runs. It provides the `run_id` that each Ray Tune task uses to create nested child runs. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Child Runs

Each Ray Tune task creates a child run under the parent run using `mlflow.start_run(run_id=run_id, nested=True)`. Each child run can independently log its own metrics, maintaining a clear hierarchy of experiment results. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

### Credential Passing

To enable child runs to log to MLflow, each Ray Tune task must receive the necessary client credentials and the parent `run_id`. The `get_databricks_env_vars()` function retrieves the required environment variables, which are then set within each Ray task. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Best Practices

- **Log from the driver process**: When possible, log MLflow models from the driver process rather than from worker nodes to avoid complexity with passing stateful references. ^[integrate-mlflow-and-ray-databricks-on-aws.md]
- **Return metrics to the driver**: Metrics and metadata are generally small enough to transfer back to the driver without causing memory issues. ^[integrate-mlflow-and-ray-databricks-on-aws.md]
- **Use child runs for distributed tasks**: The child-run approach maintains a clear hierarchy of experiment results, making it easier to track and compare individual trials. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Related Concepts

- [Ray Tune](/concepts/ray-tune.md) — Distributed hyperparameter tuning library
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for MLflow runs and evaluations
- [Ray Core MLflow Integration](/concepts/ray-core-mlflow-integration.md) — Logging from general-purpose distributed applications
- Ray Train MLflow Integration — Logging from distributed model training
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The component responsible for logging parameters, metrics, and artifacts
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The process of optimizing model hyperparameters

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
