---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5dd16502a164bed4805e110f5551ebb23b0d9e68c18b11bc476bfb1bce9bd16b
  pageDirectory: concepts
  sources:
    - hyperparameter-tuning-databricks-on-aws.md
    - hyperparameter-tuning-with-optuna-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - optuna
  citations:
    - file: hyperparameter-tuning-databricks-on-aws.md
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
title: Optuna
description: A lightweight Python framework for hyperparameter tuning with dynamic search spaces, parallelization via Joblib, and MLflow integration.
tags:
  - machine-learning
  - python-library
  - hyperparameter-tuning
timestamp: "2026-06-19T19:08:21.731Z"
---

---
title: Optuna
summary: A lightweight Python framework for hyperparameter tuning, recommended by Databricks as a replacement for Hyperopt for single-node optimization tasks.
sources:
  - hyperparameter-tuning-databricks-on-aws.md
  - hyperparameter-tuning-with-optuna-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:03:45.140Z"
updatedAt: "2026-06-19T09:19:44.757Z"
tags:
  - machine-learning
  - hyperparameter-tuning
  - optimization
aliases:
  - optuna
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Optuna

**Optuna** is an open-source Python library for hyperparameter tuning and model selection. It is designed to be lightweight and provides a flexible API for defining dynamic search spaces. Optuna includes modern optimization algorithms and can be easily integrated into machine learning workflows.^[hyperparameter-tuning-databricks-on-aws.md]

## Role on Databricks

Databricks recommends Optuna as a replacement for [Hyperopt](/concepts/hyperopt.md) for single-node optimization. Hyperopt is no longer included in Databricks Runtime for Machine Learning after version 16.4 LTS ML and its open-source version is no longer maintained. For distributed hyperparameter tuning, Databricks recommends [Ray Tune](/concepts/ray-tune.md) as an alternative that provides a similar experience to the deprecated Hyperopt distributed functionality.^[hyperparameter-tuning-databricks-on-aws.md]

The following table summarizes the recommended libraries:

| Library | Use case | Recommendation |
|---------|----------|----------------|
| Optuna | Single-node optimization | Recommended |
| Ray Tune | Distributed hyperparameter tuning | Recommended for distributed workloads |
| Hyperopt | Legacy distributed tuning | Deprecated after Databricks Runtime 16.4 LTS ML |

## Key features

- **Dynamic search space**: Optuna allows users to define hyperparameter search spaces procedurally using `suggest_*` methods inside an objective function, enabling conditional parameters and complex spaces.^[hyperparameter-tuning-with-optuna-databricks-on-aws.md]
- **Parallelization with Joblib**: Optuna can be parallelized using Joblib to scale hyperparameter tuning across multiple computes.^[hyperparameter-tuning-databricks-on-aws.md]
- **MLflow integration**: Optuna integrates with [MLflow](/concepts/mlflow.md) to track hyperparameters and metrics across trials, enabling experiment tracking and reproducibility.^[hyperparameter-tuning-databricks-on-aws.md]

## Getting started

For a detailed guide on using Optuna on Databricks, see the dedicated documentation on [Hyperparameter tuning with Optuna](/concepts/optuna-for-hyperparameter-tuning.md). The library can be used with any machine learning framework and is compatible with Databricks [MLflow Autologging](/concepts/mlflow-autologging.md) for automatic metric tracking.^[hyperparameter-tuning-databricks-on-aws.md, hyperparameter-tuning-with-optuna-databricks-on-aws.md]

## Related concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The broader practice of optimizing model hyperparameters.
- [MLflow](/concepts/mlflow.md) — Experiment tracking platform used to log Optuna trials.
- [Ray Tune](/concepts/ray-tune.md) — Distributed hyperparameter tuning library for larger-scale workloads.
- [Hyperopt](/concepts/hyperopt.md) — Legacy hyperparameter optimization library (deprecated).
- Joblib — Library used for parallelizing Optuna trial execution.

## Sources

- hyperparameter-tuning-databricks-on-aws.md
- hyperparameter-tuning-with-optuna-databricks-on-aws.md

# Citations

1. [hyperparameter-tuning-databricks-on-aws.md](/references/hyperparameter-tuning-databricks-on-aws-6d74646d.md)
2. [hyperparameter-tuning-with-optuna-databricks-on-aws.md](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
