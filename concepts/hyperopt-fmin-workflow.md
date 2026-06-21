---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7bd5e555f51c9cbf505010eb826005c379042452dfd5c81b7e6194e299123288
  pageDirectory: concepts
  sources:
    - parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-fmin-workflow
    - HFW
  citations:
    - file: parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
title: Hyperopt fmin() Workflow
description: "The standard Hyperopt optimization workflow: define an objective function, define a search space, select a search algorithm, and run fmin() to find optimal hyperparameters."
tags:
  - hyperparameter-tuning
  - hyperopt
  - workflow
timestamp: "2026-06-19T19:54:01.565Z"
---

# Hyperopt fmin() Workflow

The **Hyperopt fmin() Workflow** is a structured approach to hyperparameter optimization that uses the `fmin()` function from the Hyperopt library. This workflow enables both single-machine and distributed hyperparameter tuning, with automatic MLflow tracking for experiment management.

## Overview

Hyperopt is a Python library for hyperparameter optimization that provides algorithms for search over a defined space of hyperparameters. The core function `fmin()` minimizes an objective function by iteratively evaluating hyperparameter configurations. The workflow consists of four main steps: defining the objective function, defining the search space, selecting a search algorithm, and running the tuning algorithm with `fmin()`. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

> **Note**: The open-source version of Hyperopt is no longer being maintained. Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for distributed hyperparameter tuning. Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Steps in the Hyperopt fmin() Workflow

### 1. Define a Function to Minimize

The objective function contains the core logic for model training and evaluation. It must return a dictionary with a `'loss'` key (the value to minimize) and a `'status'` key. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

```python
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from hyperopt import STATUS_OK

def objective(C):
    clf = SVC(C=C)
    accuracy = cross_val_score(clf, X, y).mean()
    return {'loss': -accuracy, 'status': STATUS_OK}
```

Since Hyperopt minimizes the loss, a higher accuracy (better model) requires returning the negative accuracy. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

### 2. Define the Search Space

The search space specifies the range and distribution of hyperparameters to explore. Hyperopt provides parameter expressions like `hp.lognormal`, `hp.choice`, and `hp.uniform`. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

```python
from hyperopt import hp

search_space = hp.lognormal('C', 0, 1.0)
```

### 3. Select a Search Algorithm

Two main algorithms are available in Hyperopt:

- **`hyperopt.tpe.suggest`**: Tree of Parzen Estimators (TPE), a Bayesian approach that adaptively selects hyperparameter settings based on past results.
- **`hyperopt.rand.suggest`**: Random search, a non-adaptive approach that samples uniformly over the search space. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

### 4. Run the Tuning Algorithm with fmin()

The `fmin()` function executes the optimization. The `max_evals` parameter sets the maximum number of hyperparameter configurations to evaluate. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

```python
from hyperopt import fmin, tpe

argmin = fmin(
    fn=objective,
    space=search_space,
    algo=tpe.suggest,
    max_evals=16
)
```

## Distributed Tuning with SparkTrials

To parallelize hyperparameter tuning across a Spark cluster, replace the standard `Trials` class with `SparkTrials`. This distributes model fitting and evaluation across Spark workers. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

`SparkTrials` accepts two optional arguments:

- **`parallelism`**: Number of models to fit and evaluate concurrently. Defaults to the number of available Spark task slots.
- **`timeout`**: Maximum time (in seconds) that `fmin()` can run. Default is no limit. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

```python
from hyperopt import SparkTrials

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

For complex objective functions where computation time dominates, distributed tuning with `SparkTrials` can be significantly faster than single-machine tuning. For simple objective functions that run quickly, the overhead of Spark job scheduling may make distributed tuning slower. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## MLflow Integration

Automated [MLflow](/concepts/mlflow.md) tracking is enabled by default when using Hyperopt with SparkTrials. To use it, call `mlflow.start_run()` before calling `fmin()`. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

The MLflow experiment associated with the notebook automatically tracks:
- All runs with their hyperparameter configurations
- Loss values for each trial
- The best configuration found

Results can be visualized in the MLflow UI by selecting runs and using the Compare view with scatter plots. For example, plotting `C` on the X-axis and loss on the Y-axis shows the effect of the hyperparameter on model performance. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Related Concepts

- Hyperparameter Optimization
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Optuna](/concepts/optuna.md)
- [RayTune](/concepts/raytune.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md](/references/parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws-b91f741c.md)
