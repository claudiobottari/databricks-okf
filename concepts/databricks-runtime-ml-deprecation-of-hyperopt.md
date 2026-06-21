---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 778cc3a2c65c14af8aa82b4b3cb4939f65a0bca22eb8ba6ae5af5d02a80e18f3
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-deprecation-of-hyperopt
    - DRMDOH
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Databricks Runtime ML deprecation of Hyperopt
description: Hyperopt removed from Databricks Runtime for Machine Learning after version 16.4 LTS ML
tags:
  - databricks
  - deprecation
  - runtime
timestamp: "2026-06-19T14:20:06.633Z"
---

# Databricks Runtime ML Deprecation of Hyperopt

**Databricks Runtime ML deprecation of Hyperopt** refers to the removal of the Hyperopt library from Databricks Runtime for Machine Learning (ML) starting with version 16.4 LTS ML and later. This change follows the discontinuation of maintenance for the open-source Hyperopt project and Databricks's recommendation to migrate to alternative hyperparameter optimization frameworks.

## Overview

Hyperopt was a popular open-source library for hyperparameter tuning, supporting both single-node and distributed optimization via `SparkTrials`. Databricks previously bundled Hyperopt in Databricks Runtime ML and provided integrations with [MLflow](/concepts/mlflow.md) for experiment tracking. However, the open-source [Hyperopt](https://github.com/hyperopt/hyperopt) project is no longer being maintained, leading to its deprecation within the Databricks ecosystem. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Deprecation Timeline

Hyperopt is **not included** in Databricks Runtime for Machine Learning after version **16.4 LTS ML**. Users of Databricks Runtime ML 16.4 LTS ML and earlier may continue to use the bundled Hyperopt, but no updated versions or bug fixes will be provided by Databricks. For all later runtimes, the library is absent and must be installed manually if needed, though this is not recommended. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Impact

| Aspect | Detail |
|--------|--------|
| **Removed in** | Databricks Runtime ML 16.4 LTS ML and later |
| **Status of Hyperopt** | Open-source project no longer maintained |
| **Existing code using `SparkTrials`** | Will not run on newer runtimes without manual installation |

The deprecation primarily affects workflows that use `SparkTrials` for distributed hyperparameter tuning across a Spark cluster. Workloads relying on Hyperopt's single-node search must also migrate to an alternative. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Recommendations

Databricks recommends migrating to one of the following alternatives depending on your use case: ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### For Single-Node Optimization: Optuna

[Optuna](/concepts/optuna.md) is a modern hyperparameter optimization framework designed for single-node execution. It offers efficient sampling and pruning algorithms, and integrates well with MLflow on Databricks. Databricks recommends using Optuna for all new single-node hyperparameter tuning projects. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### For Distributed Hyperparameter Tuning: RayTune

[RayTune](/concepts/raytune.md) provides a distributed hyperparameter tuning experience similar to the deprecated Hyperopt with `SparkTrials`. It scales across multiple nodes using the Ray distributed computing framework. Databricks provides native support for running Ray workloads, including RayTune, on the platform. For detailed guidance, see the documentation on using RayTune on Databricks. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Migration Path

1. **Identify current Hyperopt usage** – Review notebooks and code that import `hyperopt` or use `SparkTrials`.
2. **Choose a replacement** – Use Optuna for single-node jobs; use RayTune for distributed tuning.
3. **Rewrite tuning logic** – Adapt the search space definition, objective function, and trial execution logic to the new framework.
4. **Update runtime** – Ensure the cluster runs Databricks Runtime ML 16.4 LTS ML or later; install the chosen library if not already bundled (Optuna and Ray are available as add-on libraries).

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The general practice of optimizing model hyperparameters.
- [SparkTrials](/concepts/sparktrials.md) – The deprecated Hyperopt component for distributed tuning on Spark.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment logging used alongside all tuning frameworks.
- Optuna on Databricks – Documentation and examples for single-node tuning.
- [Ray on Databricks](/concepts/ray-on-databricks.md) – Distributed computing framework that powers RayTune.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The ML-focused runtime that no longer bundles Hyperopt.

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
