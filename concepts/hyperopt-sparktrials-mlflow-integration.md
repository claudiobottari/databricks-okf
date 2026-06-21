---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03ad09b26e381a1b89c1b85a331677959044333d8471363b758824a4db5d98f7
  pageDirectory: concepts
  sources:
    - hyperopt-concepts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-sparktrials-mlflow-integration
    - HSMI
  citations:
    - file: hyperopt-concepts-databricks-on-aws.md
title: Hyperopt SparkTrials MLflow integration
description: SparkTrials logs tuning results as nested MLflow runs, with fmin() calls as parent runs and individual trials as child runs.
tags:
  - MLflow
  - experiment-tracking
  - Hyperopt
  - logging
timestamp: "2026-06-19T19:07:59.534Z"
---

# Hyperopt SparkTrials MLflow Integration

The **Hyperopt SparkTrials MLflow integration** describes how [SparkTrials](/concepts/sparktrials.md)—a Databricks-developed API for distributing [Hyperopt](/concepts/hyperopt.md) hyperparameter tuning—automatically logs tuning results to [MLflow](/concepts/mlflow.md) and enables custom logging from worker nodes. This integration helps track and compare hyperparameter experiments within the MLflow experiment framework. ^[hyperopt-concepts-databricks-on-aws.md]

## [MLflow Run](/concepts/mlflow-run.md) Hierarchy

When using `SparkTrials`, MLflow logging is structured as a hierarchy of runs:

- **Main (parent) run**: The call to `fmin()` is logged as the main run. If an active [MLflow Run](/concepts/mlflow-run.md) already exists, `SparkTrials` logs to that active run and does **not** end the run when `fmin()` returns. If no active run exists, `SparkTrials` creates a new run, logs to it, and ends the run before `fmin()` returns. ^[hyperopt-concepts-databricks-on-aws.md]

- **Child runs**: Each individual hyperparameter setting tested (a “trial”) is logged as a child run under the main run. Any MLflow log records from worker processes are also stored under the corresponding child runs. ^[hyperopt-concepts-databricks-on-aws.md]

## Active Run Management

Databricks recommends active [MLflow Run](/concepts/mlflow-run.md) management when calling `fmin()`. Specifically, wrap the call to `fmin()` inside a `with mlflow.start_run():` statement. This practice ensures that each `fmin()` call is logged to a separate MLflow main run, and it makes it easier to log extra tags, parameters, or metrics to that run. ^[hyperopt-concepts-databricks-on-aws.md]

> **Multiple calls within the same run**: When you call `fmin()` multiple times inside the same active [MLflow Run](/concepts/mlflow-run.md), MLflow logs those calls to the same main run. To resolve name conflicts for logged parameters and tags, MLflow appends a UUID to names that collide. ^[hyperopt-concepts-databricks-on-aws.md]

## Logging from Workers

Databricks Runtime ML supports logging to MLflow directly from worker nodes. You can add custom logging code inside the objective function passed to Hyperopt without explicitly managing runs in that function. For example, calling `mlflow.log_param("param_from_worker", x)` in the objective function logs a parameter to the child run associated with that trial. You can similarly log metrics, tags, and artifacts. ^[hyperopt-concepts-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) – The open-source hyperparameter optimization framework used together with SparkTrials.
- [SparkTrials](/concepts/sparktrials.md) – The Databricks class that distributes Hyperopt trials across a Spark cluster.
- fmin() – The core Hyperopt function for executing a tuning run.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The component that records experiment metadata.
- [Distributed Hyperparameter Tuning](/concepts/raytune-for-distributed-hyperparameter-tuning-on-databricks.md) – Broader topic of scaling hyperparameter search.

## Sources

- hyperopt-concepts-databricks-on-aws.md

# Citations

1. [hyperopt-concepts-databricks-on-aws.md](/references/hyperopt-concepts-databricks-on-aws-853fbb92.md)
