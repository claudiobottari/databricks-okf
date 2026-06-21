---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12e4251950f0d69c20f8725b9e549405362f50edf265bb891a6c2926f7c80ed5
  pageDirectory: concepts
  sources:
    - hyperopt-concepts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - active-mlflow-run-management-with-hyperopt
    - AMRMWH
  citations:
    - file: hyperopt-concepts-databricks-on-aws.md
title: Active MLflow run management with Hyperopt
description: Databricks recommends wrapping fmin() calls in an active MLflow run to ensure each call is logged to a separate main run and avoid name conflicts.
tags:
  - MLflow
  - best-practices
  - experiment-tracking
  - Hyperopt
timestamp: "2026-06-19T19:08:16.488Z"
---

# Active [MLflow Run](/concepts/mlflow-run.md) management with Hyperopt

**Active [MLflow Run](/concepts/mlflow-run.md) management with Hyperopt** refers to the practice of wrapping calls to Hyperopt's `fmin()` function inside an explicit `mlflow.start_run()` context manager to ensure clean separation of tuning runs and reliable logging of hyperparameter optimization results.

## Overview

When using [SparkTrials](/concepts/sparktrials.md) to distribute Hyperopt tuning across a Spark cluster, the system automatically logs results as nested MLflow runs. The main call to `fmin()` becomes the parent run, and each hyperparameter setting tested (a "trial") is logged as a child run under that parent. MLflow log records from worker nodes are also stored under the corresponding child runs. ^[hyperopt-concepts-databricks-on-aws.md]

## Recommended pattern

Databricks recommends active [MLflow Run](/concepts/mlflow-run.md) management when calling `fmin()`. This means wrapping the call inside a `with mlflow.start_run():` statement. ^[hyperopt-concepts-databricks-on-aws.md]

```python
import mlflow
from hyperopt import fmin, tpe, hp, SparkTrials

def objective(params):
    # ... model training logic ...
    return {"loss": loss_value}

with mlflow.start_run():
    best = fmin(
        fn=objective,
        space=search_space,
        algo=tpe.suggest,
        max_evals=100,
        trials=SparkTrials(parallelism=4)
    )
```

This pattern ensures that each `fmin()` call is logged to a separate MLflow main run, and makes it easier to log extra tags, parameters, or metrics to that run. ^[hyperopt-concepts-databricks-on-aws.md]

## Behavior with and without an active run

`SparkTrials` handles [MLflow Run](/concepts/mlflow-run.md) management differently depending on whether an active run exists when `fmin()` is called: ^[hyperopt-concepts-databricks-on-aws.md]

- **If there is an active run**: `SparkTrials` logs to this active run and does not end the run when `fmin()` returns. This is the scenario enabled by the `with mlflow.start_run():` pattern.
- **If there is no active run**: `SparkTrials` creates a new run, logs to it, and ends the run before `fmin()` returns.

## Multiple calls within the same run

When you call `fmin()` multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), MLflow logs those calls to the same main run. To resolve name conflicts for logged parameters and tags, MLflow appends a UUID to names with conflicts. ^[hyperopt-concepts-databricks-on-aws.md]

## Logging from workers

When logging from worker nodes, you do not need to manage runs explicitly in the objective function. You can call `mlflow.log_param("param_from_worker", x)` directly in the objective function to log a parameter to the child run. Parameters, metrics, tags, and artifacts can all be logged from within the objective function. ^[hyperopt-concepts-databricks-on-aws.md]

## Related concepts

- [Hyperopt fmin()](/concepts/hyperopt-fmin.md) — The core function for executing hyperparameter optimization
- [SparkTrials](/concepts/sparktrials.md) — Databricks API for distributing Hyperopt trials across Spark workers
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The logging system that records hyperparameter tuning results
- [Hyperopt on Databricks](/concepts/hyperopt-deprecation-on-databricks.md) — Overview of hyperparameter tuning with Hyperopt

## Sources

- hyperopt-concepts-databricks-on-aws.md

# Citations

1. [hyperopt-concepts-databricks-on-aws.md](/references/hyperopt-concepts-databricks-on-aws-853fbb92.md)
