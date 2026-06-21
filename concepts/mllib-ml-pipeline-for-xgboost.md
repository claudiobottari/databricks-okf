---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57ac02c044190f2f2e4385fefc3422999b4700e189d95ad4c4757c26eb1da0c1
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mllib-ml-pipeline-for-xgboost
    - MMPFX
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: MLlib ML Pipeline for XGBoost
description: Embedding XGBoost models into MLlib ML pipelines to enable distributed model training workflows
tags:
  - machine-learning
  - pipeline
  - xgboost
  - spark-mllib
timestamp: "2026-06-18T12:04:45.373Z"
---

#MLlib ML Pipeline for XGBoost

The **MLlib ML Pipeline for XGBoost** is an integration that allows XGBoost models to be used as standard components in Apache Spark MLlib pipelines. This enables data scientists and engineers to leverage XGBoost's high-performance gradient boosting within the familiar pipeline workflow for tasks such as feature transformation, model training, tuning, and evaluation. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Overview

MLlib's [ML Pipelines](/concepts/mllib-pipelines-api.md) provide a uniform API for building and evaluating machine learning workflows. By embedding XGBoost into this API, users can combine XGBoost estimators and transformers with other pipeline stages. This integration supports both classification and regression tasks and works with Scala on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Example Notebooks

Two example notebooks are provided to demonstrate the integration:

- **XGBoost classification with ML pipeline** — shows how to embed an XGBoost model into an MLlib ML pipeline for classification. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- **XGBoost regression with cross-validation** — demonstrates how to use MLlib cross-validation to tune an XGBoost regression model within a pipeline. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

These notebooks are available in the Databricks documentation and can be run directly in a Databricks workspace.

## Benefits of Using XGBoost in an ML Pipeline

- **Unified workflow** – Combine XGBoost with Spark feature transformers, indexers, and evaluators in a single [Pipeline](/concepts/mllib-pipelines-api.md) object.
- **Hyperparameter tuning** – Use MLlib's [CrossValidator](/concepts/crossvalidator.md) and [TrainValidationSplit](/concepts/trainvalidationsplit.md) to optimize XGBoost parameters (e.g., `maxDepth`, `eta`, `numRound`) automatically.
- **Scalability** – Leverage Apache Spark's distributed computing for training on large datasets.
- **Reproducibility** – Serialize the entire pipeline (including XGBoost stages) using [MLflow](/concepts/mlflow.md) or Spark's persistence API for production deployment.

## Requirements

The integration is available in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) and uses the XGBoost4J-Spark library. Users must have a compatible Spark environment and the necessary XGBoost dependencies on the cluster. The notebooks provided assume a Scala-based workflow.

## Related Concepts

- XGBoost on Databricks – General guidance for using XGBoost on the platform
- [ML Pipelines](/concepts/mllib-pipelines-api.md) – The core abstraction for building workflows in MLlib
- Cross-validation – Technique for hyperparameter tuning supported by the pipeline
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre-configured runtime for machine learning workloads
- Scala API for Spark ML – The language-API used in the example notebooks

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
