---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c91fba310ed30c490cf49820d76a942ca4264b790f5c80590aacee84a79c587
  pageDirectory: concepts
  sources:
    - model-training-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-training-with-mllib
    - DMTWM
  citations:
    - file: model-training-examples-databricks-on-aws.md
title: Databricks model training with MLlib
description: Using Apache Spark MLlib on Databricks for binary classification, decision trees, GBT regression, structured streaming, and custom transformers.
tags:
  - machine-learning
  - spark
  - mllib
  - databricks
timestamp: "2026-06-19T19:45:00.327Z"
---

# Databricks Model Training with MLlib

**Databricks model training with MLlib** refers to building and training machine learning models using Apache Spark's MLlib library within the Databricks environment. MLlib provides scalable machine learning algorithms that can process large datasets distributed across a cluster, making it suitable for big data workloads. ^[model-training-examples-databricks-on-aws.md]

## Overview

MLlib is Spark's built-in machine learning library that offers a wide range of algorithms and utilities for classification, regression, clustering, collaborative filtering, and feature transformation. On Databricks, MLlib models can be trained using Python, PySpark, or Scala, and can be integrated with other Databricks features such as [Unity Catalog](/concepts/unity-catalog.md) and [MLflow](/concepts/mlflow.md) for experiment tracking and model management. ^[model-training-examples-databricks-on-aws.md]

## Available Examples

Databricks provides example notebooks demonstrating various MLlib capabilities: ^[model-training-examples-databricks-on-aws.md]

| Feature | Description |
|---------|-------------|
| Binary classification | Training classifiers on large datasets |
| Decision trees | Tree-based models for classification and regression |
| GBT regression | Gradient-boosted tree regression models |
| Structured Streaming | Real-time model training on streaming data |
| Custom transformer | Building custom feature transformers using MLlib pipelines |

## Key Capabilities

MLlib on Databricks supports a variety of model types and workflows: ^[model-training-examples-databricks-on-aws.md]

- **Binary classification** — Algorithms such as logistic regression, decision trees, random forests, and gradient-boosted trees for two-class problems.
- **Regression** — Linear regression, decision tree regression, and gradient-boosted tree regression.
- **Decision trees** — Both classification and regression trees that handle categorical features and scale to large datasets.
- **GBT regression** — Gradient-boosted tree ensembles for regression tasks, offering high predictive accuracy.
- **Structured Streaming** — MLlib models can be trained and applied on streaming data using Spark Structured Streaming.
- **Custom transformers** — Users can implement custom feature transformers by extending MLlib's `Transformer` class for use in ML pipelines.

## Integration with Databricks Ecosystem

MLlib models on Databricks can be combined with other tools in the platform: ^[model-training-examples-databricks-on-aws.md]

- **[Unity Catalog](/concepts/unity-catalog.md)** — Store and manage MLlib models alongside other data assets with fine-grained access control.
- **[MLflow](/concepts/mlflow.md)** — Track MLlib training runs, log parameters and metrics, and register models in the MLflow Model Registry.
- **AutoML** — For automated model selection and hyperparameter tuning, Databricks AutoML can prepare datasets and run trials using libraries including MLlib.

## Comparison with Other Libraries

While MLlib is optimized for distributed training on large datasets, Databricks also supports other machine learning libraries for different use cases: ^[model-training-examples-databricks-on-aws.md]

- **scikit-learn** — Better suited for single-node workloads and smaller datasets, with a broader range of algorithms and more mature feature engineering capabilities.
- **[XGBoost](/concepts/xgboostspark-module.md)** — Provides high-performance gradient boosting with support for both single-node and distributed training on Databricks.
- **[Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)** — For MLlib models, Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for distributed hyperparameter tuning, as the open-source [Hyperopt](/concepts/hyperopt.md) library is no longer maintained and is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. ^[model-training-examples-databricks-on-aws.md]

## Getting Started

To train an MLlib model on Databricks: ^[model-training-examples-databricks-on-aws.md]

1. Create or open a Databricks notebook.
2. Load your data into a Spark DataFrame.
3. Use MLlib's `Pipeline` API to define feature transformers and estimators.
4. Fit the model using the `fit()` method on the training data.
5. Evaluate model performance using MLlib's evaluation metrics.
6. Log the model and training metrics using MLflow for reproducibility.

## Related Concepts

- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — The underlying distributed machine learning library
- [ML Pipelines](/concepts/mllib-pipelines-api.md) — MLlib's API for chaining transformers and estimators
- Feature Engineering with Spark — Preparing features at scale
- Model Evaluation on Databricks — Assessing model performance
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling model training across clusters

## Sources

- model-training-examples-databricks-on-aws.md

# Citations

1. [model-training-examples-databricks-on-aws.md](/references/model-training-examples-databricks-on-aws-47a05943.md)
