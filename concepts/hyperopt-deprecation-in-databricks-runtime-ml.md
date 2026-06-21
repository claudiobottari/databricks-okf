---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5006a19d96d1789475f7f01b82fd588d702a73704d4c2bf25c363720e9edcce8
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-deprecation-in-databricks-runtime-ml
    - HDIDRM
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Hyperopt deprecation in Databricks Runtime ML
description: Hyperopt is excluded from Databricks Runtime for Machine Learning starting from version 16.4 LTS ML, marking its phased removal from the Databricks ML ecosystem.
tags:
  - databricks
  - deprecation
  - mlops
timestamp: "2026-06-19T09:19:22.264Z"
---

# Hyperopt Deprecation in Databricks Runtime ML

**Hyperopt deprecation in Databricks Runtime ML** refers to the removal of the open-source [Hyperopt](https://github.com/hyperopt/hyperopt) library from Databricks Runtime for Machine Learning, effective after version 16.4 LTS ML. Users of hyperparameter tuning workflows must migrate to alternative optimization frameworks.

## Overview

The open-source version of Hyperopt is no longer being maintained by its community maintainers. As a result, Hyperopt is not included in Databricks Runtime for Machine Learning versions after 16.4 LTS ML. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Recommended Alternatives

Databricks recommends the following migration paths depending on workload type: ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

| Alternative | Use Case |
|-------------|----------|
| [Optuna](/concepts/optuna.md) | Single-node hyperparameter optimization |
| [RayTune](/concepts/raytune.md) | Distributed hyperparameter tuning (closest experience to deprecated Hyperopt + SparkTrials) |

### Optuna

Optuna is recommended for [single-node optimization](/concepts/optuna-for-single-node-optimization-on-databricks.md) workflows where the model training fits within a single machine. It provides an efficient, define-by-run API for hyperparameter search.

### RayTune

RayTune offers a distributed tuning experience similar to the deprecated `Hyperopt` with `SparkTrials`. For guidance on using RayTune on Databricks, see [Ray on Databricks](/concepts/ray-on-databricks.md). ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Migration Guidance

Existing code using Hyperopt should be migrated to Optuna or RayTune. The notebook example "[Compare models using scikit-learn, Hyperopt, and MLflow](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-model-selection)" previously demonstrated using Hyperopt with `SparkTrials` to compare three model types—this workflow should now be implemented using the recommended alternatives. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Related Concepts

- [Hyperparameter tuning on Databricks](/concepts/hyperparameter-tuning-on-databricks.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [SparkTrials](/concepts/sparktrials.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- Model Selection

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
