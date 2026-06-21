---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19d8630690ee94658d75daba45e7aee029cc365f64613c06753dc426829387b8
  pageDirectory: concepts
  sources:
    - model-training-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-training-with-xgboost
    - DMTWX
  citations:
    - file: model-training-examples-databricks-on-aws.md
title: Databricks model training with XGBoost
description: Training XGBoost models on Databricks using Python, PySpark, and Scala, supporting both single-node and distributed workloads.
tags:
  - machine-learning
  - xgboost
  - databricks
  - distributed-training
timestamp: "2026-06-19T19:44:59.420Z"
---

# Databricks model training with XGBoost

**Databricks model training with XGBoost** covers the supported APIs, workload types, and integration with other Databricks features for building gradient-boosted tree models using the XGBoost library. The platform provides ready-to-run examples and automated training capabilities that leverage XGBoost alongside other popular open-source libraries. ^[model-training-examples-databricks-on-aws.md]

## Supported APIs and workload types

Databricks provides XGBoost training examples written in three APIs: **Python**, **PySpark**, and **Scala**. These examples demonstrate both single-node workloads and distributed training, allowing users to scale XGBoost training from a single machine to a cluster across multiple nodes. ^[model-training-examples-databricks-on-aws.md]

## Integration with AutoML

Databricks AutoML uses XGBoost (along with scikit‑learn and other libraries) to automatically prepare datasets, perform a set of trials, and create Python notebooks with the source code for each trial run. This enables you to quickly generate baseline XGBoost models without writing manual training code. ^[model-training-examples-databricks-on-aws.md]

## Example workflows that include XGBoost

An end‑to‑end classification example using scikit-learn includes XGBoost as one of the models in the workflow. This example runs on Unity Catalog, logs runs with [MLflow](/concepts/mlflow.md), and performs automated hyperparameter tuning using [Hyperopt](/concepts/hyperopt.md) and MLflow. It demonstrates how XGBoost can be integrated into a broader machine learning pipeline on Databricks. ^[model-training-examples-databricks-on-aws.md]

## Hyperparameter tuning for XGBoost

For tuning XGBoost models, Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for distributed hyperparameter tuning. The open‑source version of Hyperopt is deprecated and is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. ^[model-training-examples-databricks-on-aws.md]

## Related concepts

- [Distributed training with XGBoost](/concepts/distributed-training-with-xgboostspark.md)
- [PySpark XGBoost integration](/concepts/xgboost-with-mllib-integration.md)
- [Databricks AutoML](/concepts/databricks-automl.md)
- MLflow tracking for XGBoost
- [Hyperparameter tuning on Databricks](/concepts/hyperparameter-tuning-on-databricks.md)

## Sources

- model-training-examples-databricks-on-aws.md

# Citations

1. [model-training-examples-databricks-on-aws.md](/references/model-training-examples-databricks-on-aws-47a05943.md)
