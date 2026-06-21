---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4447a58436393e689d63a2a38940e1b9e59c58e21aa4b7afcab79daf28972bd2
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - cross-model-hyperparameter-optimization
    - CHO
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
      start: 7
      end: 12
title: Cross-model hyperparameter optimization
description: The technique of tuning hyperparameters across multiple distinct model types (e.g., different scikit-learn classifiers) and comparing their best configurations to select an overall best model.
tags:
  - machine-learning
  - hyperparameter-tuning
  - model-selection
timestamp: "2026-06-18T14:40:43.313Z"
---

# Cross-model hyperparameter optimization

**Cross-model hyperparameter optimization** is the practice of tuning the hyperparameters of multiple distinct model types (e.g., different scikit-learn classifiers) within a single optimization run, then selecting the best-performing model overall. This approach allows practitioners to compare both model architectures and their optimal configurations simultaneously, rather than tuning each model type in isolation.

## Overview

Rather than optimizing a single model’s hyperparameters, cross-model hyperparameter optimization defines separate search spaces for each model type and runs parallel trials across all of them. A common implementation uses [Hyperopt](/concepts/hyperopt.md) with `SparkTrials` to evaluate three or more model types, each with a unique set of hyperparameters appropriate to that model. The objective function returns a validation metric (such as accuracy or F1 score) that is comparable across models, and the best overall model is selected after all trials complete. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Methodology

1. **Define per-model hyperparameter spaces** – Each model type (e.g., random forest, logistic regression, gradient boosting) receives its own set of hyperparameters to vary.
2. **Create a combined search space** – The spaces are merged into a single hyperparameter dictionary; a categorical parameter (e.g., `model_type`) selects which space to use.
3. **Use Hyperopt’s `SparkTrials`** – `SparkTrials` distributes trials across a Spark cluster, enabling parallel evaluation of different model types and hyperparameter combinations.
4. **Log results with MLflow** – Each trial logs the model, its hyperparameters, and evaluation metrics, making it easy to compare runs and retrieve the best configuration. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

```python
# Conceptual sketch of the search space
search_space = hp.choice('model_type', [
    {
        'type': 'rf',
        'n_estimators': hp.choice('rf.n_estimators', [100, 200]),
        'max_depth': hp.choice('rf.max_depth', [5, 10, 15]),
    },
    {
        'type': 'lr',
        'C': hp.uniform('lr.C', 0.01, 10),
        'penalty': hp.choice('lr.penalty', ['l1', 'l2']),
    },
    # ... additional model types
])
```

## Benefits

- **Holistic model selection** – Avoids the bias of tuning only one architecture before comparing.
- **Resource efficiency** – Parallel trials across model types reuse the same cluster resources, reducing wall-clock time compared to sequential tuning.
- **Reproducible tracking** – [MLflow](/concepts/mlflow.md) captures all runs, making it straightforward to audit or revisit the optimization history.

## Deprecation and alternatives

The open-source version of Hyperopt is no longer being maintained, and Hyperopt is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. Databricks recommends replacing Hyperopt with:

- **[Optuna](/concepts/optuna.md)** – for single-node hyperparameter optimization.
- **[RayTune](/concepts/raytune.md)** – for distributed hyperparameter tuning, offering a similar experience to the deprecated Hyperopt distributed functionality.

Users migrating existing cross-model comparison workflows can replicate the same pattern using Optuna (with single-node `Study`) or RayTune (with distributed `Tuner`), while still logging to MLflow. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:7-12]

## Related concepts

- [Hyperopt](/concepts/hyperopt.md) — the Bayesian optimization library used in the original implementation
- [Optuna](/concepts/optuna.md) — recommended replacement for single-node hyperparameter tuning
- [RayTune](/concepts/raytune.md) — recommended replacement for distributed hyperparameter tuning
- [SparkTrials](/concepts/sparktrials.md) — Hyperopt’s distributed trial runner
- [MLflow Tracking](/concepts/mlflow-tracking.md) — experiment logging and run comparison
- [Model selection](/concepts/custom-judge-model-selection.md) — broader topic of choosing among candidate model architectures

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
2. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:7-12](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
