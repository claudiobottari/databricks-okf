---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d3baa3bc6a599be3d6bdfc357f6ae7ddfb443c5181d78cc66461d57b1b7f2ec
  pageDirectory: concepts
  sources:
    - parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-mlflow-integration
    - Hyperopt Integration
  citations:
    - file: parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
title: Hyperopt-MLflow Integration
description: Automated MLflow tracking of Hyperopt tuning trials on Databricks, enabled by calling mlflow.start_run() before fmin() to log all trials as MLflow runs.
tags:
  - hyperopt
  - mlflow
  - experiment-tracking
timestamp: "2026-06-19T19:54:25.152Z"
---

Here is the wiki page for "Hyperopt-MLflow Integration".

---

## Hyperopt-MLflow Integration

**Hyperopt-MLflow Integration** refers to the automatic tracking of hyperparameter tuning trials when using [Hyperopt](/concepts/hyperopt.md) with a distributed Apache Spark backend on Databricks. When using [SparkTrials](/concepts/sparktrials.md), each trial's hyperparameters and resulting metrics are automatically logged as an [MLflow](/concepts/mlflow.md) run, providing a centralized view of the tuning experiment.

### Overview

When you parallelize a Hyperopt tuning workflow using `SparkTrials` with `fmin()`, MLflow automatically logs every function evaluation as a separate [MLflow Run](/concepts/mlflow-run.md). This is enabled by default — no explicit MLflow logging calls are needed inside the objective function to capture the trial results. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

To use automated MLflow tracking, call `mlflow.start_run()` before invoking `fmin()`. This groups all trials under a single parent experiment run for cleaner organization in the MLflow UI. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

### How It Works

The integration requires two components:

1. **SparkTrials**: A Trials implementation from Hyperopt that evaluates the objective function on Spark workers concurrently.
2. **MLflow tracking**: Automatically captures each trial's parameters, metrics, and artifacts.

The following code demonstrates the integration:

```python
from hyperopt import fmin, tpe, hp, SparkTrials, STATUS_OK
import mlflow

# Define the objective function
def objective(C):
    clf = SVC(C=C)
    accuracy = cross_val_score(clf, X, y).mean()
    return {'loss': -accuracy, 'status': STATUS_OK}

# Define the search space
search_space = hp.lognormal('C', 0, 1.0)

# Run distributed tuning with automatic MLflow tracking
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

^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

### Viewing Results

After running the tuning workflow, you can view the results in the MLflow UI:

1. Click the **Experiment** icon in the notebook context bar (upper right).
2. Select the resulting runs and click **Compare**.
3. Use the Scatter Plot to visualize relationships — for example, setting the hyperparameter on the X‑axis and the loss on the Y‑axis to examine sensitivity.

^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

### Advantages

- **No manual logging**: Each trial is automatically recorded without additional instrumentation of the objective function.
- **Centralized tracking**: All trials are visible in the MLflow experiment UI alongside other MLflow runs.
- **Debugging and analysis**: You can compare trials, inspect hyperparameter values, and analyze performance trends directly in the MLflow UI.

### Deprecation Notice

The open-source version of Hyperopt is no longer being maintained. In Databricks Runtime for Machine Learning, Hyperopt is not included after version 16.4 LTS ML. Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for distributed hyperparameter tuning functionality similar to Hyperopt's. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

### Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — The hyperparameter optimization library.
- [SparkTrials](/concepts/sparktrials.md) — The Trials implementation for distributed evaluation.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The experiment tracking component that logs trials.
- [Optuna](/concepts/optuna.md) — Recommended alternative for single-node optimization.
- [RayTune](/concepts/raytune.md) — Recommended alternative for distributed tuning on Databricks.

### Sources

- parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md](/references/parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws-b91f741c.md)
