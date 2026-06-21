---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 570e7a852ef3bba654d0a4754b31d8d9a2ff017f7da23885cb1277587aeba895
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - use-scikit-learn-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - optuna-hyperparameter-tuning-on-databricks
    - OHTOD
  citations:
    - file: best-practices-for-deep-learning-databricks-on-aws.md
    - file: use-scikit-learn-on-databricks-databricks-on-aws.md
title: Optuna Hyperparameter Tuning on Databricks
description: Using Optuna for adaptive hyperparameter tuning to optimize deep learning model performance, including batch size and learning rate tuning.
tags:
  - hyperparameter-tuning
  - optimization
  - optuna
timestamp: "2026-06-19T17:41:21.491Z"
---

## Optuna Hyperparameter Tuning on Databricks

**Optuna Hyperparameter Tuning on Databricks** refers to the integration of the [Optuna](https://optuna.org/) library within the Databricks platform for automating the search for optimal hyperparameters in machine learning models. Optuna provides adaptive hyperparameter tuning that can efficiently explore the hyperparameter space, reducing manual effort and improving model performance. ^[best-practices-for-deep-learning-databricks-on-aws.md]

### Integration

Optuna is included in Databricks Runtime ML, and Databricks recommends its use for hyperparameter tuning in both traditional machine learning and deep learning workflows. It can be used to automate hyperparameter search when tuning batch size and learning rate, among other parameters. ^[best-practices-for-deep-learning-databricks-on-aws.md]

### Example: scikit-learn Classification

Databricks provides example notebooks that demonstrate Optuna alongside [scikit-learn] and [MLflow]. In the basic scikit-learn classification notebook, Optuna is used to automate hyperparameter tuning for a simple classification model. ^[use-scikit-learn-on-databricks-databricks-on-aws.md]

### Example: End‑to‑End Pipeline

An end‑to‑end scikit‑learn notebook illustrates loading data, model training, distributed hyperparameter tuning (using Optuna), and model inference, along with model lifecycle management via the MLflow Model Registry. ^[use-scikit-learn-on-databricks-databricks-on-aws.md]

### Related Concepts

- [MLflow](/concepts/mlflow.md) – Tracks experiments and logs models tuned with Optuna.
- scikit-learn – Common library used with Optuna for hyperparameter tuning.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General concept of optimizing model parameters.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Optuna can be used in distributed settings for parallel tuning.
- Batch Size Tuning – A specific use case where Optuna helps find optimal batch sizes.

### Sources

- best-practices-for-deep-learning-databricks-on-aws.md
- use-scikit-learn-on-databricks-databricks-on-aws.md

# Citations

1. best-practices-for-deep-learning-databricks-on-aws.md
2. [use-scikit-learn-on-databricks-databricks-on-aws.md](/references/use-scikit-learn-on-databricks-databricks-on-aws-a9e701f4.md)
