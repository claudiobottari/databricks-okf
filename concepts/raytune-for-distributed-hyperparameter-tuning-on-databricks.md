---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d6276767f40327c71be94740db2799818fc5c55630c5cf6d909662256f1a96f
  pageDirectory: concepts
  sources:
    - model-training-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - raytune-for-distributed-hyperparameter-tuning-on-databricks
    - RFDHTOD
    - Distributed Hyperparameter Tuning
    - Distributed hyperparameter tuning
  citations:
    - file: model-training-examples-databricks-on-aws.md
      start: 1
      end: 3
    - file: model-training-examples-databricks-on-aws.md
      start: 9
      end: 13
    - file: model-training-examples-databricks-on-aws.md
      start: 5
      end: 8
title: RayTune for distributed hyperparameter tuning on Databricks
description: RayTune is recommended by Databricks as the replacement for Hyperopt for distributed hyperparameter tuning, providing a similar experience.
tags:
  - machine-learning
  - hyperparameter-tuning
  - distributed-computing
  - databricks
timestamp: "2026-06-19T19:45:01.985Z"
---

Here is the wiki page for "RayTune for distributed hyperparameter tuning on Databricks".

---

## RayTune for distributed hyperparameter tuning on Databricks

**RayTune** is a distributed hyperparameter tuning library that provides a scalable alternative to the now-deprecated open-source [Hyperopt](/concepts/hyperopt.md) library. On Databricks, RayTune is the recommended choice for distributed hyperparameter tuning workloads. For general information about hyperparameter tuning on the platform, see [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md).^[model-training-examples-databricks-on-aws.md:1-3]

The open-source version of Hyperopt is no longer being maintained and is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using either [Optuna](/concepts/optuna.md) for single-node optimization or RayTune for a similar experience to the deprecated Hyperopt distributed hyperparameter tuning functionality.^[model-training-examples-databricks-on-aws.md:9-13]

### Use with MLflow

RayTune can be integrated with [MLflow](/concepts/mlflow.md) for experiment tracking and logging of tuning results. For detailed guidance on using RayTune together with MLflow on Databricks, see the documentation on using RayTune on Databricks (referenced as `[RayTune]` on the platform).^[model-training-examples-databricks-on-aws.md:9-13]

### Example notebooks

The Databricks model training examples page includes references to notebooks that demonstrate hyperparameter tuning workflows. The scikit-learn examples on the page show automated hyperparameter tuning with both Hyperopt and MLflow. Users looking to transition from Hyperopt to RayTune can consult those examples for guidance on adapting the workflow.^[model-training-examples-databricks-on-aws.md:5-8]

### Related concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Optuna](/concepts/optuna.md) – Single-node alternative to RayTune.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – RayTune is designed for distributed hyperparameter search.
- [MLflow](/concepts/mlflow.md) – Tracking and logging of tuning experiments.
- Ray – The distributed compute framework underlying RayTune.

### Sources

- model-training-examples-databricks-on-aws.md

# Citations

1. [model-training-examples-databricks-on-aws.md:1-3](/references/model-training-examples-databricks-on-aws-47a05943.md)
2. [model-training-examples-databricks-on-aws.md:9-13](/references/model-training-examples-databricks-on-aws-47a05943.md)
3. [model-training-examples-databricks-on-aws.md:5-8](/references/model-training-examples-databricks-on-aws-47a05943.md)
