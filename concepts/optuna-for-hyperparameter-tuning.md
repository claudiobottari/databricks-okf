---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5938d021b24beedc9dad42f35b4468161855e2462a5e7cde99e1f08f1cf85a86
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - optuna-for-hyperparameter-tuning
    - OFHT
    - Optuna Hyperparameter Tuning
    - Hyperparameter tuning with Optuna
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Optuna for Hyperparameter Tuning
description: Optuna provides adaptive hyperparameter tuning for machine learning models on Databricks, helping automate the search for optimal hyperparameters including batch size and learning rate combinations.
tags:
  - hyperparameter-tuning
  - optuna
  - automation
timestamp: "2026-06-19T14:10:02.723Z"
---

# Optuna for Hyperparameter Tuning

**Optuna** is an open‑source hyperparameter optimization framework that provides adaptive tuning for machine learning models. On Databricks, it is one of the recommended tools for automating the search over hyperparameter spaces, often used in conjunction with deep learning workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Overview

Optuna offers a flexible, define‑by‑run API that allows practitioners to specify search spaces programmatically and leverage adaptive sampling strategies (such as Tree‑structured Parzen Estimator, TPE) to converge on optimal configurations faster than brute‑force grid search. It is designed to scale from single‑node experiments to distributed parallel execution.

Within the Databricks ecosystem, Optuna is listed among the built‑in tools that help optimize deep learning training. It can be used to parallelize training jobs across multiple runs, which is especially useful when exploring a large hyperparameter space. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Using Optuna for Hyperparameter Tuning

Optuna can be applied to any part of the model training pipeline. A common scenario is **batch size tuning**: after manually adjusting the batch size by factors of 2 or 0.5, you can turn to Optuna to automate the finer‑grained search over batch size, learning rate, and other hyperparameters simultaneously. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Typical Workflow on Databricks

1. Install Optuna (it is pre‑installed in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) for many versions).
2. Define an objective function that trains a model and returns a validation metric (e.g., loss or accuracy).
3. Set up a study and sample hyperparameters using Optuna’s suggest API.
4. Optionally parallelize trials by launching multiple runs in a cluster. Optuna supports both local parallel execution and distributed storage backends (e.g., SQLite, MySQL, or PostgreSQL) for coordinating trials across workers.

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General principles of parameter optimisation.
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) – Broader guidance on training, data loading, and inference.
- Batch Size Tuning – A specific hyperparameter that Optuna can help tune.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The pre‑configured environment where Optuna is available.
- [AutoML and Hyperparameter Tuning on Databricks](/concepts/hyperparameter-tuning-on-databricks.md) – The official Databricks documentation page covering Optuna and other tools.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
