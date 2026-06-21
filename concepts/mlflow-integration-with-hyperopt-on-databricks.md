---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cdb202a923e72574de62c87d5a088272b18404248e2abdb9ef3132963775f04e
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-with-hyperopt-on-databricks
    - MIWHOD
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
      start: 25
      end: 27
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
      start: 18
      end: 23
title: MLflow integration with Hyperopt on Databricks
description: Using MLflow to track and compare hyperparameter tuning experiments across different model types in Databricks
tags:
  - databricks
  - mlflow
  - hyperparameter-tuning
  - experiment-tracking
timestamp: "2026-06-19T17:48:00.451Z"
---

# MLflow Integration with Hyperopt on Databricks

**MLflow integration with Hyperopt on Databricks** refers to the use of [Hyperopt](https://github.com/hyperopt/hyperopt) together with [MLflow](/wiki/mlflow) to perform hyperparameter tuning and model comparison within the Databricks environment. The integration is demonstrated in the official notebook *Compare models using scikit-learn, Hyperopt, and MLflow*, which uses Hyperopt with `SparkTrials` to compare three model types and evaluate performance across different hyperparameter sets, logging results to MLflow. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:25-27]

## Deprecation Status

The open-source version of Hyperopt is no longer being maintained. As of **Databricks Runtime for Machine Learning 16.4 LTS ML and later**, Hyperopt is **no longer included** in the runtime. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:18-23]

Databricks recommends migrating to the following alternatives:

- **[Optuna](/concepts/optuna.md)** – for single‑node hyperparameter optimization.
- **[RayTune](/concepts/raytune.md)** – for distributed hyperparameter tuning, offering a similar experience to the deprecated Hyperopt distributed functionality (e.g., `SparkTrials`).

^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:18-23]

## Use in Existing Workflows

Users who still have access to older Databricks Runtime ML versions (≤ 16.4 LTS ML) can run the *Compare models using scikit-learn, Hyperopt, and MLflow* notebook to see how MLflow tracks experiments across multiple model types and hyperparameter sets. The notebook uses `SparkTrials` to distribute evaluation across a Spark cluster. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:25-27]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) – the underlying optimization library (deprecated).
- [MLflow](/concepts/mlflow.md) – experiment tracking and model registry used to log results.
- [SparkTrials](/concepts/sparktrials.md) – Hyperopt’s distributed trial runner on Apache Spark.
- [Optuna](/concepts/optuna.md) – recommended replacement for single‑node tuning.
- RayTune on Databricks – recommended replacement for distributed tuning.
- [Hyperparameter tuning on Databricks](/concepts/hyperparameter-tuning-on-databricks.md) – general guidance for tuning workflows.

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:25-27](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
2. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md:18-23](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
