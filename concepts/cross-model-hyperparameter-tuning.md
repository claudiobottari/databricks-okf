---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4e8f5013275a9b8d43414e72aae8f1a7c73bf0ef1cc841dbe7df8dfca0c6c1c
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-model-hyperparameter-tuning
    - CHT
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Cross-Model Hyperparameter Tuning
description: A workflow that tunes hyperparameters for multiple distinct model types simultaneously and selects the best overall model, rather than tuning a single model type.
tags:
  - machine-learning
  - model-selection
  - workflow
timestamp: "2026-06-18T11:03:53.859Z"
---

# Cross-Model Hyperparameter Tuning

**Cross-Model Hyperparameter Tuning** refers to the process of tuning the hyperparameters of multiple distinct model architectures (e.g., different scikit-learn estimators) in a single unified experiment, with the goal of identifying the best-performing model overall. This approach systematically compares model families by searching their respective hyperparameter spaces and evaluating them against a common metric.

## Motivation and Workflow

In practice, data scientists often need to determine not only the best hyperparameters within a given model family, but also which model type (such as a linear model, tree-based ensemble, or kernel method) is most suitable for the problem. Cross-model hyperparameter tuning addresses this by embedding model selection directly into the tuning pipeline.^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

A typical workflow involves defining separate hyperparameter search spaces for each candidate model type, running a unified optimization process, and then comparing the results to pick the overall best model. The tuning process may use either single-node or distributed execution depending on the scale of the search.

## Implementing with Hyperopt and MLflow

A common Databricks implementation uses [Hyperopt](/concepts/hyperopt.md) combined with [MLflow](/concepts/mlflow.md) to orchestrate the search and track results. Hyperopt’s `SparkTrials` distributes the evaluation of hyperparameter configurations across a Spark cluster, and MLflow logs every trial’s parameters and metrics for easy comparison.^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

The following steps are typical in such a notebook:

1. **Define search spaces** for each model type (e.g., for a random forest, decision tree, and logistic regression), each with its own set of hyperparameters.
2. **Configure `SparkTrials`** to control the parallelism and maximum number of evaluations.
3. **Run Hyperopt’s `fmin`** with an objective function that trains a model of the specified type and returns a loss metric.
4. **Use MLflow** to log parameters and metrics for every trial.
5. **Analyze the results** to select the best model overall.

The source notebook demonstrates exactly this approach, comparing three model types and evaluating performance with a different set of hyperparameters appropriate to each.^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Deprecation of Hyperopt and Recommended Alternatives

The open-source version of Hyperopt is no longer being maintained, and it is not included in Databricks Runtime for Machine Learning starting with version 16.4 LTS ML. Databricks recommends using the following alternatives:^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

- **[Optuna](/concepts/optuna.md)** for single-node hyperparameter optimization.
- **[RayTune](/concepts/raytune.md)** for distributed hyperparameter tuning, which provides a similar experience to the deprecated Hyperopt distributed functionality.

For users migrating from Hyperopt to RayTune on Databricks, see the guide on Ray with MLflow.

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General strategies for optimizing model hyperparameters
- [Optuna](/concepts/optuna.md) – Recommended single-node alternative to Hyperopt
- [RayTune](/concepts/raytune.md) – Recommended distributed alternative to Hyperopt
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging and comparing tuning experiments
- [SparkTrials](/concepts/sparktrials.md) – Hyperopt’s distributed execution mode (deprecated)

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
