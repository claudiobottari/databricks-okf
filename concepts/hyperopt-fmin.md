---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6535d804be21d6a6c1ce16315fba9a7dd5397cc1fe268917523f06ed5dc0719
  pageDirectory: concepts
  sources:
    - hyperopt-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-fmin
  citations:
    - file: hyperopt-concepts-databricks-on-aws.md
title: Hyperopt fmin()
description: The core function in Hyperopt used to execute hyperparameter optimization runs by iteratively generating and evaluating trials.
tags:
  - hyperparameter-tuning
  - optimization
  - Hyperopt
timestamp: "2026-06-19T19:07:54.256Z"
---

# Hyperopt `fmin()`

**Hyperopt `fmin()`** is the primary function used to execute a hyperparameter optimization run in the Hyperopt library. It iteratively generates trials (combinations of hyperparameters), evaluates them against an objective function, and searches for the configuration that minimizes (or maximizes) the objective. ^[hyperopt-concepts-databricks-on-aws.md]

## Overview

`fmin()` orchestrates the entire tuning process. The user provides an objective function, a search space, a choice of optimization algorithm (e.g., Tree of Parzen Estimators, Random Search), and the maximum number of evaluations (`max_evals`). Hyperopt then proposes new hyperparameter settings based on past results, evaluates them, and returns the best configuration found. ^[hyperopt-concepts-databricks-on-aws.md]

The function’s arguments include `fn` (the objective function), `space` (the search space), `algo` (the search algorithm), `max_evals` (the maximum number of trials), and `trials` (a trials object such as `SparkTrials` or the default `Trials`). For a full description of each argument, see the Hyperopt documentation. ^[hyperopt-concepts-databricks-on-aws.md]

## Deprecation Warning

The open-source version of Hyperopt is no longer being maintained, and Hyperopt is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for distributed hyperparameter tuning as a replacement for Hyperopt’s distributed functionality. ^[hyperopt-concepts-databricks-on-aws.md]

## Using `fmin()` with `SparkTrials`

Databricks provides the [SparkTrials](/concepts/sparktrials.md) class, which allows `fmin()` to distribute trial evaluations across Spark workers without modifying the existing Hyperopt code. When using `SparkTrials`, the driver node generates new trials, and worker nodes evaluate them in parallel. Each trial is evaluated in a Spark task. ^[hyperopt-concepts-databricks-on-aws.md]

`SparkTrials` is designed for single‑machine ML models (e.g., scikit‑learn). For distributed ML algorithms (e.g., MLlib, Horovod), the default `Trials` class should be used instead, because the model building process is already parallelized on the cluster. ^[hyperopt-concepts-databricks-on-aws.md]

## Integration with MLflow

When `fmin()` is called with `SparkTrials`, tuning results are logged as nested MLflow runs:

- **Main (parent) run:** The `fmin()` call is logged as the main run. If an active [MLflow Run](/concepts/mlflow-run.md) already exists, `SparkTrials` logs to that active run and does not end it when `fmin()` returns. If no active run exists, `SparkTrials` creates a new run, logs to it, and ends the run before `fmin()` returns. ^[hyperopt-concepts-databricks-on-aws.md]
- **Child runs:** Each hyperparameter setting tested (each trial) is logged as a child run under the main run. MLflow log records from worker code are stored under the corresponding child run. ^[hyperopt-concepts-databricks-on-aws.md]

Databricks recommends wrapping the `fmin()` call inside a `with mlflow.start_run():` statement to ensure each `fmin()` call is logged to a separate main run and to simplify logging additional tags, parameters, or metrics. When `fmin()` is called multiple times within the same active run, MLflow appends a UUID to parameter and tag names to resolve conflicts. ^[hyperopt-concepts-databricks-on-aws.md]

In the objective function, users can log directly to the child run without explicit run management — for example, calling `mlflow.log_param("param_from_worker", x)` inside the function. Parameters, metrics, tags, and artifacts can all be logged from worker code. ^[hyperopt-concepts-databricks-on-aws.md]

## Related Concepts

- [SparkTrials](/concepts/sparktrials.md)
- [Hyperopt](/concepts/hyperopt.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Optuna](/concepts/optuna.md)
- [RayTune](/concepts/raytune.md)
- Hyperparameter Optimization

## Sources

- hyperopt-concepts-databricks-on-aws.md

# Citations

1. [hyperopt-concepts-databricks-on-aws.md](/references/hyperopt-concepts-databricks-on-aws-853fbb92.md)
