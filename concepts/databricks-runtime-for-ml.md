---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e0d3eaadf65ff97a8724a0826dc7396053debe9da6c0d92f011376698768f23
  pageDirectory: concepts
  sources:
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-for-ml
    - DRFM
  citations:
    - file: machine-learning-on-databricks-databricks-on-aws.md
title: Databricks Runtime for ML
description: Pre-configured compute clusters for machine learning on Databricks, bundling libraries like scikit-learn, XGBoost, MLflow, and deep learning frameworks.
tags:
  - databricks
  - machine-learning
  - infrastructure
timestamp: "2026-06-19T19:20:56.940Z"
---

# Databricks Runtime for ML

**Databricks Runtime for ML** is a pre-configured cluster environment on Databricks designed specifically for machine learning and deep learning workloads. It includes a curated set of libraries and frameworks that support the complete ML lifecycle, from data preparation through model training and deployment.

## Overview

Databricks Runtime for ML provides a ready-to-use environment that eliminates the need for manual dependency management and library version conflicts. It includes popular machine learning libraries such as scikit-learn, XGBoost, MLflow, and also supports deep learning frameworks for more advanced workloads. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Included Libraries

The runtime comes pre-installed with libraries optimized for classic machine learning and deep learning tasks:

- **scikit-learn** – For building classification, regression, and clustering models
- **XGBoost** – For gradient-boosted tree models
- **MLflow** – For experiment tracking, model management, and deployment throughout the model development lifecycle
- Deep learning frameworks for neural network training

^[machine-learning-on-databricks-databricks-on-aws.md]

## Use Cases

Databricks Runtime for ML supports the full range of machine learning workflows, including:

- **Classic machine learning** – Training models with scikit-learn, XGBoost, and other traditional algorithms
- **Deep learning** – Training neural networks with support for distributed training across multiple GPUs using frameworks like PyTorch
- **Distributed training** – Leveraging managed compute and built-in frameworks for training large models at scale

## Related Concepts

- AutoML – Automated feature engineering and hyperparameter tuning
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment tracking and model comparison
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Creating and managing features with automated data pipelines
- [AI Runtime](/concepts/ai-runtime.md) – Serverless GPU compute for custom deep learning workloads
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Scaling ML workloads across multiple GPUs and nodes
- [Model Serving](/concepts/model-serving.md) – Deploying custom models as scalable REST endpoints

## Sources

- machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
