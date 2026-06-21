---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a789206f57e217adaade0c3e56e89b161c11dcdcf02f06d4e9dba3dd7267c75f
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - optuna-as-hyperopt-replacement-on-databricks
    - OAHROD
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Optuna as Hyperopt replacement on Databricks
description: Databricks recommends Optuna for single-node hyperparameter optimization as a replacement for Hyperopt
tags:
  - databricks
  - hyperparameter-tuning
  - optuna
timestamp: "2026-06-19T17:47:49.287Z"
---

# Optuna as Hyperopt Replacement on Databricks

**Optuna** is the recommended replacement for [Hyperopt](/concepts/hyperopt.md) for single-node hyperparameter optimization on Databricks. Hyperopt is no longer maintained as an open-source project and is removed from [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) starting with version 16.4 LTS ML. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Recommendation

Databricks recommends using Optuna for single-node hyperparameter tuning workflows. For distributed hyperparameter tuning—functionality previously provided by Hyperopt with `SparkTrials`—the platform recommends [RayTune](/concepts/raytune.md) instead, which offers a similar distributed experience. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Context

Hyperopt was previously used to tune hyperparameters across multiple model types and evaluate performance with different hyperparameter sets. Users migrating away from Hyperopt should move their single-node tuning workflows to [Optuna](/concepts/optuna.md) and their distributed tuning workflows to RayTune. This separation ensures continued support and access to maintained libraries. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- Single-Node Optimization
- [Distributed Hyperparameter Tuning](/concepts/raytune.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [SparkTrials](/concepts/sparktrials.md)

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
