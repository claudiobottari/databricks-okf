---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64d557ebcbb47b8d3082a0c5af61322bfc33588da741dfe5a522f6a46ea24186
  pageDirectory: concepts
  sources:
    - hyperopt-concepts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparktrials-parallelism-configuration
    - SPC
  citations:
    - file: hyperopt-concepts-databricks-on-aws.md
title: SparkTrials parallelism configuration
description: "SparkTrials accepts a parallelism parameter (default: number of Spark executors, max: 128) and a timeout parameter to control distributed tuning execution."
tags:
  - configuration
  - distributed-computing
  - SparkTrials
timestamp: "2026-06-19T19:08:06.147Z"
---

# SparkTrials Parallelism Configuration

`SparkTrials` is a Databricks-developed API that distributes Hyperopt hyperparameter tuning across Spark workers. It accelerates single‑machine tuning without requiring changes to existing Hyperopt code.^[hyperopt-concepts-databricks-on-aws.md]

The `parallelism` argument controls the maximum number of trials that can be evaluated concurrently. A higher value scales out the testing of more hyperparameter settings; however, because Hyperopt proposes new trials based on past results, there is a trade‑off between parallelism and adaptivity. For a fixed `max_evals`, greater parallelism speeds up calculations, but lower parallelism may lead to better results because each iteration has access to more past results.^[hyperopt-concepts-databricks-on-aws.md]

**Default value:** The number of Spark executors available in the cluster.  
**Maximum value:** 128. If the configured `parallelism` exceeds the number of concurrent tasks allowed by the cluster, `SparkTrials` automatically reduces parallelism to that lower limit.^[hyperopt-concepts-databricks-on-aws.md]

The `parallelism` argument is passed when constructing a `SparkTrials` instance. The optional `timeout` argument sets a maximum number of seconds for the `fmin()` call; when exceeded, all runs are terminated and `fmin()` exits, preserving results from completed trials.^[hyperopt-concepts-databricks-on-aws.md]

## Implementation Model

With `SparkTrials`, the driver node generates new trials, and worker nodes evaluate them. Each trial corresponds to one Spark job with a single task, evaluated on a worker machine. If the cluster is configured to run multiple tasks per worker, multiple trials may be evaluated simultaneously on that worker.^[hyperopt-concepts-databricks-on-aws.md]

`SparkTrials` is designed for single‑machine ML models such as scikit‑learn. For models built with distributed ML algorithms (e.g., MLlib, Horovod), use the default Hyperopt `Trials` class instead.^[hyperopt-concepts-databricks-on-aws.md]

## Relationship with MLflow

`SparkTrials` logs tuning results as nested MLflow runs:
- The call to `fmin()` is logged as the main (parent) run. If an active run exists, `SparkTrials` logs to it and does not end it; otherwise it creates a new run and ends it before returning.
- Each hyperparameter setting tested (a trial) is logged as a child run under the main run. MLflow log records from workers are stored under the corresponding child runs.^[hyperopt-concepts-databricks-on-aws.md]

When calling `fmin()`, wrap it inside `with mlflow.start_run():` to ensure each `fmin()` call is logged to a separate main run and to allow extra tags or metrics. In the objective function, use `mlflow.log_param()` etc. directly; you do not need to manage runs explicitly.^[hyperopt-concepts-databricks-on-aws.md]

## Related Concepts

- [Hyperopt fmin()](/concepts/hyperopt-fmin.md) – The core function for hyperparameter optimization.
- SparkTrials and MLflow – Nested run logging detail.
- [Distributed Hyperparameter Tuning](/concepts/raytune-for-distributed-hyperparameter-tuning-on-databricks.md) – General strategies for scaling tuning.
- [Optuna](/concepts/optuna.md) – Alternative for single‑node optimization (Hyperopt deprecated after 16.4 LTS ML).
- [RayTune](/concepts/raytune.md) – Alternative for distributed tuning.

## Sources

- hyperopt-concepts-databricks-on-aws.md

# Citations

1. [hyperopt-concepts-databricks-on-aws.md](/references/hyperopt-concepts-databricks-on-aws-853fbb92.md)
