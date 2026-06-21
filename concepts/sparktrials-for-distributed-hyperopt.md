---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19c31cce8643d49466ab0b5e3694f03d4e8e4b757032e5ccabc76710643caaee
  pageDirectory: concepts
  sources:
    - parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparktrials-for-distributed-hyperopt
    - SFDH
  citations:
    - file: parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
title: SparkTrials for Distributed Hyperopt
description: A Trials subclass for Hyperopt that distributes hyperparameter tuning trials across a Spark cluster, accepting parallelism and timeout parameters for concurrent model fitting.
tags:
  - hyperopt
  - apache-spark
  - distributed-computing
  - hyperparameter-tuning
timestamp: "2026-06-19T19:53:59.051Z"
---

# SparkTrials for Distributed Hyperopt

**SparkTrials** is a Hyperopt [`Trials`](https://github.com/hyperopt/hyperopt/wiki/FMin) subclass that parallelizes hyperparameter tuning across an Apache Spark cluster. It enables single-machine Hyperopt workflows to scale by evaluating multiple hyperparameter configurations concurrently on Spark workers, while MLflow automatically tracks every trial.

> **Note:** The open-source version of Hyperopt is no longer being maintained. Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for a similar distributed hyperparameter tuning experience on Databricks. SparkTrials is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

---

## Overview

Hyperopt `fmin()` uses a `Trials` object to record and manage evaluations of the objective function. `SparkTrials` extends this by distributing each trial as a Spark task, allowing multiple hyperparameter combinations to be tested concurrently. This is particularly useful when the objective function is computationally expensive — such as training a deep learning model or running cross-validation on a large dataset — because the wall-clock time of tuning can be significantly reduced. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

---

## Usage

To enable distributed tuning, pass a `SparkTrials` instance as the `trials` argument to `fmin()`:

```python
from hyperopt import SparkTrials

spark_trials = SparkTrials()

argmin = fmin(
    fn=objective,
    space=search_space,
    algo=algo,
    max_evals=16,
    trials=spark_trials
)
```

^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

When using `SparkTrials`, the objective function is serialized and sent to Spark executors, so it must be self-contained (e.g., import all necessary libraries and load datasets inside the function or use Spark broadcast variables).

---

## Parameters

`SparkTrials` accepts two optional parameters:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `parallelism` | Maximum number of models to fit and evaluate concurrently. | Number of available Spark task slots in the cluster. |
| `timeout` | Maximum time (in seconds) that `fmin()` can run. | `None` (no maximum). |

^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

Setting `parallelism` appropriately can trade off between exploration speed and resource usage. A high parallelism value may cause `fmin()` to converge less adaptively because it evaluates many points at once before receiving feedback. The `timeout` parameter is useful for controlling job cost and ensuring the tuning finishes within a deadline.

---

## Automated MLflow Tracking

When `SparkTrials` is used inside an [MLflow Run](/concepts/mlflow-run.md), each trial is automatically logged as a child run under the parent [MLflow Run](/concepts/mlflow-run.md). This enables detailed tracking of hyperparameters, metrics, and artifacts for every evaluated configuration. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

To enable automatic tracking, wrap the `fmin()` call in an `mlflow.start_run()` context:

```python
with mlflow.start_run():
    argmin = fmin(
        fn=objective,
        space=search_space,
        algo=algo,
        max_evals=16,
        trials=SparkTrials()
    )
```

^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

After the run completes, you can use the MLflow UI to compare trials, plot hyperparameter effects, and identify the best configuration.

---

## Performance Considerations

Distributed tuning with `SparkTrials` introduces overhead for serializing the objective function and starting Spark tasks. For simple, fast objective functions (e.g., training a small model on a small dataset), the overhead may *increase* total tuning time compared to single-machine tuning. `SparkTrials` is most beneficial when the objective function takes non-trivial time to evaluate — for example, fitting a large model or performing cross-validation on a large dataset. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

---

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — The foundational hyperparameter optimization library (deprecated)
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment logging for machine learning workflows
- [Optuna](/concepts/optuna.md) — Recommended replacement for single-node optimization
- [RayTune](/concepts/raytune.md) — Recommended replacement for distributed hyperparameter tuning
- [Distributed Hyperparameter Tuning](/concepts/raytune.md) — General strategies for scaling hyperparameter search
- fmin — The core function for running Hyperopt optimization
- [Tree of Parzen Estimators (TPE)](/concepts/hyperopt-tree-of-parzen-estimators-tpe-algorithm.md) — Bayesian search algorithm often used with Hyperopt

---

## Sources

- parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md](/references/parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws-b91f741c.md)
