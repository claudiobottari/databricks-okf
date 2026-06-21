---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c002972f15e5606a98bcfdd98fdf05f936f7a887c961f6378b89fe6fdce7867
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-uuid-name-conflict-resolution
    - MUNCR
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: MLflow UUID Name Conflict Resolution
description: "MLflow's behavior when fit() is called multiple times within the same active run: it appends a UUID to parameter and tag names to resolve conflicts."
tags:
  - mlflow
  - machine-learning
  - experiment-tracking
timestamp: "2026-06-18T14:26:37.325Z"
---

# MLflow UUID Name Conflict Resolution

**MLflow UUID Name Conflict Resolution** is a mechanism that automatically resolves naming conflicts for parameters and tags when multiple MLflow runs are logged within the same active [MLflow Run](/concepts/mlflow-run.md) context. When duplication occurs, MLflow appends a UUID to the conflicting names to ensure uniqueness. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Overview

In MLflow, when multiple calls to `fit()` are made within the same active [MLflow Run](/concepts/mlflow-run.md) — such as with [CrossValidator](/concepts/crossvalidator.md) or [TrainValidationSplit](/concepts/trainvalidationsplit.md) from [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — parameters and tags may collide if the same names are reused across different sub-runs. MLflow resolves these name conflicts automatically by appending a UUID to parameter and tag names that have conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

This behavior is particularly relevant when using [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md), where `CrossValidator` or `TrainValidationSplit` log hyperparameters and evaluation metrics as nested runs under a parent run.

## When Conflicts Occur

Name conflicts can occur under the following conditions:

- Multiple calls to `fit()` are made within the same active [MLflow Run](/concepts/mlflow-run.md).
- The same parameter or tag names are used across different evaluations or model configurations.
- [Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md) is enabled, and tuning results are logged as nested child runs under a single parent run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Resolution Mechanism

When a name conflict is detected, MLflow modifies the conflicting name by appending a UUID. For example, a parameter named `maxDepth` that conflicts across two sub-runs might become `maxDepth_<uuid>` in the second run's metadata. This ensures that all logged parameters and tags remain unique and traceable. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Example Scenario

Consider a notebook where `CrossValidator.fit()` is called multiple times within the same `with mlflow.start_run():` block:

```python
with mlflow.start_run():
    model1 = crossval.fit(training_data)
    model2 = crossval.fit(validation_data)
```

Both calls log hyperparameters like `maxDepth` and `numTrees`. Without conflict resolution, these names would collide. MLflow resolves this by adding a UUID suffix to the second set of parameters, preserving all logged information without data loss. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Best Practices

While MLflow automatically handles name conflicts, following best practices can reduce confusion:

- **Wrap each `fit()` call in its own active run.** Use `with mlflow.start_run():` for each individual tuning operation to avoid conflicts entirely. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Use descriptive run names.** When starting a new run, provide a `run_name` parameter to make runs easier to identify in the MLflow UI.
- **Review nested run structure.** Understand that `CrossValidator` and `TrainValidationSplit` create nested runs (child runs under a parent run), which may produce UUID-suffixed names when `fit()` is called multiple times.

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core MLflow component for logging parameters, metrics, and artifacts
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — The Spark library for machine learning that integrates with MLflow
- [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md) — Automated tracking of MLlib tuning operations
- [CrossValidator](/concepts/crossvalidator.md) — MLlib tool for hyperparameter tuning via cross-validation
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) — MLlib tool for hyperparameter tuning via train-validation splitting
- [Databricks Autologging](/concepts/databricks-autologging.md) — A broader automatic logging feature that includes MLflow integration

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
