---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4960070badc9e1e81d1c4873631154f1ade5ff376d3999493a7e6e0217ade665
  pageDirectory: concepts
  sources:
    - model-training-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - optuna-for-single-node-optimization-on-databricks
    - OFSOOD
    - single-node optimization
  citations:
    - file: model-training-examples-databricks-on-aws.md
title: Optuna for single-node optimization on Databricks
description: Optuna is recommended by Databricks as the replacement for Hyperopt for single-node hyperparameter optimization workloads.
tags:
  - machine-learning
  - hyperparameter-tuning
  - optimization
  - databricks
timestamp: "2026-06-19T19:45:07.408Z"
---

## Optuna for Single-Node Optimization on Databricks

**Optuna** is an open-source hyperparameter optimization framework that Databricks recommends for **single-node** hyperparameter tuning workflows. Following the deprecation of the open-source version of Hyperopt, Optuna serves as the primary alternative for users who need to tune models on a single compute node (as opposed to distributed tuning across multiple nodes, for which [RayTune](/concepts/raytune.md) is recommended). ^[model-training-examples-databricks-on-aws.md]

On Databricks, Optuna can be used similarly to how Hyperopt was used for single-node tasks, such as tuning scikit-learn or [XGBoost](/concepts/xgboostspark-module.md) models. Users typically define an objective function, set a search space, and run the optimization inside a notebook or job. Databricks does not bundle Optuna in Databricks Runtime for Machine Learning after version 16.4 LTS ML, so users may need to install it manually via `%pip install optuna` if it is not already present. ^[model-training-examples-databricks-on-aws.md]

### Recommendation Context

The deprecation of Hyperopt (open-source) means that existing Hyperopt-based single-node tuning code should be migrated to Optuna. For distributed hyperparameter tuning that spans multiple workers or GPUs, Databricks recommends [RayTune](/concepts/raytune.md) instead. ^[model-training-examples-databricks-on-aws.md]

### Related Concepts

- [Hyperopt (deprecated)](/concepts/hyperopt-deprecation-on-databricks.md) – The earlier recommended library for hyperparameter tuning on Databricks.
- [RayTune](/concepts/raytune.md) – Databricks’ recommended solution for distributed hyperparameter tuning.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General concepts and best practices.
- Single-Node Training – Workloads that fit on one machine, where Optuna is most appropriate.

### Sources

- model-training-examples-databricks-on-aws.md

# Citations

1. [model-training-examples-databricks-on-aws.md](/references/model-training-examples-databricks-on-aws-47a05943.md)
