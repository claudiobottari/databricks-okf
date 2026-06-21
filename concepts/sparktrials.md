---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 966bf16548593dec9ad246a351f608feaf18ea1f7224b792800affd134155219
  pageDirectory: concepts
  sources:
    - hyperopt-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparktrials
    - Hyperopt SparkTrials
  citations:
    - file: hyperopt-concepts-databricks-on-aws.md
    - file: parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: SparkTrials
description: A Databricks API that distributes Hyperopt hyperparameter tuning trials across Spark workers for parallel execution.
tags:
  - distributed-computing
  - Spark
  - Hyperopt
  - parallelization
timestamp: "2026-06-19T19:08:33.375Z"
---

# SparkTrials

**SparkTrials** is a Hyperopt API, developed by Databricks, that enables distributed hyperparameter tuning across a Spark cluster by parallelizing trial evaluations on worker nodes. It scales single‑machine hyperparameter tuning to a cluster without requiring changes to existing Hyperopt code. ^[hyperopt-concepts-databricks-on-aws.md]

## Overview

SparkTrials accelerates tuning by distributing trial evaluations to Spark workers. In Hyperopt, a trial typically corresponds to fitting one model with one set of hyperparameters. With SparkTrials, the driver node generates new trials, and worker nodes evaluate them. Each trial is launched as a Spark job with a single task; if the cluster runs multiple tasks per worker, multiple trials may be evaluated simultaneously on that worker. ^[hyperopt-concepts-databricks-on-aws.md]

SparkTrials is designed for single‑machine ML models such as scikit-learn estimators. For models built with distributed ML algorithms (e.g., MLlib or Horovod), the model‑building process is already parallelized on the cluster, so the default Hyperopt class `Trials` should be used instead. ^[hyperopt-concepts-databricks-on-aws.md]

## Arguments

SparkTrials accepts two optional arguments: ^[hyperopt-concepts-databricks-on-aws.md]

- **`parallelism`**: The maximum number of trials to evaluate concurrently. A higher number allows scaling out the testing of more hyperparameter settings. Because Hyperopt proposes new trials based on past results, there is a trade‑off between parallelism and adaptivity: for a fixed `max_evals`, greater parallelism speeds up computation, but lower parallelism may yield better results as each iteration sees more past results. Default: number of Spark executors available. Maximum: 128. If the value exceeds the number of concurrent tasks allowed by the cluster configuration, SparkTrials reduces parallelism to that value. ^[hyperopt-concepts-databricks-on-aws.md]
- **`timeout`**: The maximum number of seconds an `fmin()` call can take. When exceeded, all runs are terminated and `fmin()` exits; information about completed runs is preserved. ^[hyperopt-concepts-databricks-on-aws.md]

## SparkTrials and MLflow

Databricks Runtime ML supports logging to [MLflow](/concepts/mlflow.md) from workers. SparkTrials logs tuning results as nested MLflow runs: ^[hyperopt-concepts-databricks-on-aws.md]

- **Main (parent) run**: The call to `fmin()` is logged as the main run. If there is already an active [MLflow Run](/concepts/mlflow-run.md), SparkTrials logs to it and does not end the run when `fmin()` returns. If there is no active run, SparkTrials creates a new one, logs to it, and ends it before `fmin()` returns. ^[hyperopt-concepts-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting evaluated (a “trial”) is logged as a child run under the main run. MLflow log records from workers are stored under the corresponding child runs. ^[hyperopt-concepts-databricks-on-aws.md]

When calling `fmin()` inside a `with mlflow.start_run():` block, each call is logged to a separate main run, making it easier to log extra tags, parameters, or metrics. If `fmin()` is called multiple times within the same active run, MLflow appends a UUID to resolve name conflicts. ^[hyperopt-concepts-databricks-on-aws.md]

Logging from workers does not require explicit run management in the objective function; simply call `mlflow.log_param("param_from_worker", x)` inside the function to log to the child run. ^[hyperopt-concepts-databricks-on-aws.md]

## Example

The following example demonstrates distributed hyperparameter tuning of a scikit‑learn SVM classifier on the Iris dataset: ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from hyperopt import fmin, tpe, hp, SparkTrials, STATUS_OK
import mlflow

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define objective function
def objective(C):
    clf = SVC(C=C)
    accuracy = cross_val_score(clf, X, y).mean()
    return {'loss': -accuracy, 'status': STATUS_OK}

# Define search space
search_space = hp.lognormal('C', 0, 1.0)

# Create SparkTrials and run distributed tuning
spark_trials = SparkTrials()
with mlflow.start_run():
    argmin = fmin(
        fn=objective,
        space=search_space,
        algo=tpe.suggest,
        max_evals=16,
        trials=spark_trials
    )
```

After the run, the best value for `C` is available in `argmin`. The MLflow UI shows a parent run for the whole `fmin()` call and a child run for each trial. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Status

The open‑source version of [Hyperopt](/concepts/hyperopt.md) is no longer being maintained. Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using [Optuna](/concepts/optuna.md) for single‑node optimization or [RayTune](/concepts/raytune.md) as a replacement for the deprecated distributed Hyperopt workflow. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md, hyperopt-concepts-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — The open‑source hyperparameter tuning framework.
- fmin() — The Hyperopt function for executing tuning runs.
- [MLflow](/concepts/mlflow.md) — Platform for logging and tracking experiments.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — Supports MLflow logging from workers.
- [Optuna](/concepts/optuna.md) — Recommended alternative for single‑node optimization.
- [RayTune](/concepts/raytune.md) — Recommended alternative for distributed hyperparameter tuning.
- scikit-learn — Example of a single‑machine ML model compatible with SparkTrials.

## Sources

- hyperopt-concepts-databricks-on-aws.md
- parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [hyperopt-concepts-databricks-on-aws.md](/references/hyperopt-concepts-databricks-on-aws-853fbb92.md)
2. [parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md](/references/parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws-b91f741c.md)
3. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
