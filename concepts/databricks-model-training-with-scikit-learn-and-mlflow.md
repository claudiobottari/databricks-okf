---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 574cc655dae70ddefe10bf244b5f139637f237788921a60bbdbdecbcf7bc764e
  pageDirectory: concepts
  sources:
    - model-training-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-training-with-scikit-learn-and-mlflow
    - MLflow and Databricks model training with scikit-learn
    - DMTWSAM
  citations:
    - file: model-training-examples-databricks-on-aws.md
title: Databricks model training with scikit-learn and MLflow
description: End-to-end machine learning on Databricks using scikit-learn with Unity Catalog, MLflow tracking, and automated hyperparameter tuning via Hyperopt/Optuna.
tags:
  - machine-learning
  - scikit-learn
  - mlflow
  - databricks
timestamp: "2026-06-19T19:44:49.811Z"
---

# Databricks Model Training with scikit-learn and MLflow

**Databricks model training with scikit-learn and MLflow** refers to the practice of building, training, and tracking machine learning models on the Databricks platform using the scikit-learn library for model development and MLflow for experiment tracking, model registration, and deployment. This combination enables reproducible, well-governed machine learning workflows at scale.

## Overview

Databricks provides comprehensive support for training machine learning models using popular open-source libraries, including scikit-learn. When combined with MLflow, scikit-learn model training becomes fully traceable, with automatic logging of parameters, metrics, and model artifacts. ^[model-training-examples-databricks-on-aws.md]

The platform offers several example notebooks demonstrating scikit-learn model training with key Databricks features:

- **Unity Catalog** integration for model governance
- **Classification model** development
- **MLflow** tracking for experiment management
- **Automated hyperparameter tuning** using Hyperopt and MLflow

^[model-training-examples-databricks-on-aws.md]

## Key Features

### MLflow Integration

MLflow is automatically integrated with scikit-learn training on Databricks. During model training, MLflow logs:

- Model parameters (hyperparameters)
- Performance metrics (accuracy, F1 score, etc.)
- Model artifacts (serialized model files)
- Source code and environment information

This integration ensures full reproducibility of training runs. ^[model-training-examples-databricks-on-aws.md]

### Unity Catalog Support

Models trained with scikit-learn can be registered in [Unity Catalog](/concepts/unity-catalog.md), providing centralized model governance, access control, and lineage tracking across the organization. ^[model-training-examples-databricks-on-aws.md]

### Automated Hyperparameter Tuning

Databricks supports automated hyperparameter tuning for scikit-learn models. The platform provides example notebooks demonstrating hyperparameter optimization using:

- **Hyperopt** (deprecated after Databricks Runtime 16.4 LTS ML)
- **Optuna** for single-node optimization (recommended replacement)
- **RayTune** for distributed hyperparameter tuning

^[model-training-examples-databricks-on-aws.md]

## Example Workflows

### Basic Machine Learning Tutorial

The basic scikit-learn example on Databricks demonstrates:

1. Loading and preparing data
2. Training a classification model with scikit-learn
3. Tracking the experiment with MLflow
4. Performing automated hyperparameter tuning with Hyperopt and MLflow
5. Registering the model in Unity Catalog

^[model-training-examples-databricks-on-aws.md]

### End-to-End Example

The end-to-end scikit-learn example extends the basic workflow by incorporating:

- Unity Catalog for model governance
- Classification model development
- MLflow experiment tracking
- Automated hyperparameter tuning with Hyperopt and MLflow
- XGBoost integration alongside scikit-learn

^[model-training-examples-databricks-on-aws.md]

## Hyperparameter Tuning Considerations

The open-source version of Hyperopt is no longer being maintained. Hyperopt is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. Databricks recommends the following alternatives:

- **Optuna** for single-node hyperparameter optimization
- **RayTune** for distributed hyperparameter tuning (similar experience to the deprecated Hyperopt functionality)

^[model-training-examples-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Open-source platform for the machine learning lifecycle
- [Unity Catalog](/concepts/unity-catalog.md) — Unified governance solution for data and AI assets
- AutoML — Automated machine learning on Databricks
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — Optimization of model hyperparameters
- [Optuna](/concepts/optuna.md) — Recommended hyperparameter optimization framework
- [RayTune](/concepts/raytune.md) — Distributed hyperparameter tuning framework
- [XGBoost](/concepts/xgboostspark-module.md) — Gradient boosting framework often used alongside scikit-learn
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-configured environment for ML workloads

## Sources

- model-training-examples-databricks-on-aws.md

# Citations

1. [model-training-examples-databricks-on-aws.md](/references/model-training-examples-databricks-on-aws-47a05943.md)
