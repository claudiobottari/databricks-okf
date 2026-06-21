---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7c388fe05d7271f5b4c0dca74f6117e1817c57969818da63eb435b2105433d5
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-model-training-examples
    - DRMMTE
    - model training examples
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Databricks Runtime ML model training examples
description: Databricks provides notebook examples for training models including hyperparameter tuning documentation within the Databricks Runtime ML ecosystem
tags:
  - databricks
  - machine-learning
  - documentation
timestamp: "2026-06-19T17:48:05.988Z"
---

## Databricks Runtime ML model training examples

**Databricks Runtime ML model training examples** are sample notebooks and code patterns that illustrate how to train, tune, and compare machine learning models using the libraries bundled in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). These examples cover a range of techniques, from single-node optimization to distributed hyperparameter tuning, and are designed to help users quickly adopt best practices for model development on the Databricks platform.

### Example: Comparing model types with Hyperopt and MLflow

A representative example is the notebook **Compare models using scikit-learn, Hyperopt, and MLflow**. This notebook demonstrates how to tune the hyperparameters of multiple model types and select the best overall model. It uses Hyperopt with `SparkTrials` to evaluate each model type with a different set of hyperparameters appropriate for that type. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

#### Deprecation note

The open-source version of Hyperopt is no longer being maintained. Hyperopt is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for a distributed experience similar to the deprecated Hyperopt functionality. You can also use RayTune on Databricks via the Ray integration. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

Despite this deprecation, the notebook remains a useful reference for understanding the cross‑model comparison workflow. For new projects, Databricks suggests adopting Optuna or RayTune. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Other model training examples

The Databricks documentation provides additional model training examples covering topics such as:

- [Fully Sharded Data Parallel (FSDP) training](/concepts/fully-sharded-data-parallel-fsdp.md) for large language models (20B to 120B+ parameters)
- Serverless GPU compute with H100 GPUs for distributed training on 8xH100 single-node clusters
- [Deep learning best practices](/concepts/deep-learning-best-practices-on-databricks.md) using A100 GPUs and other GPU types

These examples, together with the Hyperopt‑based comparison notebook, form a comprehensive set of resources for model training on Databricks Runtime ML.

### Related concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General approaches for optimizing model hyperparameters.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging and comparing training runs, used in the example notebook.
- [SparkTrials](/concepts/sparktrials.md) – Hyperopt’s parallel trial execution on a Spark cluster.
- [Optuna](/concepts/optuna.md) – Recommended single‑node hyperparameter optimization library.
- [RayTune](/concepts/raytune.md) – Recommended distributed hyperparameter tuning library.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – Techniques for scaling model training across multiple GPUs or nodes.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment that includes pre‑installed ML libraries.

### Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
