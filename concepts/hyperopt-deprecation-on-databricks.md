---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e89cbcffee290f51a32ee43617ca0f60ddf53091767971b16e552635cf35e77
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
    - hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
    - model-training-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - hyperopt-deprecation-on-databricks
    - HDOD
    - Hyperopt (deprecated)
    - Hyperopt on Databricks
    - hyperopt-deprecation-in-databricks-runtime-ml
    - HDIDRM
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
    - file: hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
    - file: model-training-examples-databricks-on-aws.md
title: Hyperopt deprecation on Databricks
description: Hyperopt is no longer maintained and is removed from Databricks Runtime for Machine Learning after version 16.4 LTS ML
tags:
  - databricks
  - hyperparameter-tuning
  - deprecation
timestamp: "2026-06-19T17:47:49.309Z"
---

# Hyperopt deprecation on Databricks

**Hyperopt deprecation on Databricks** refers to the removal of the open-source Hyperopt library from Databricks Runtime for Machine Learning (ML) starting with version 16.4 LTS ML. Databricks no longer maintains, distributes, or supports Hyperopt, and existing users are encouraged to migrate to alternative optimization frameworks.

## Timeline and affected versions

Hyperopt is not included in Databricks Runtime for Machine Learning after **16.4 LTS ML**. Any Databricks Runtime ML version later than 16.4 LTS ML does not ship Hyperopt pre-installed. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md, hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md, model-training-examples-databricks-on-aws.md]

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is itself no longer being maintained by its community maintainers. This upstream unmaintained status is the primary reason Databricks removed the library from its ML runtime. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Recommended alternatives

Databricks recommends two replacement libraries, depending on the workload:

| Use case | Recommended alternative |
|----------|------------------------|
| Single‑node hyperparameter optimization | [Optuna](/concepts/optuna.md) |
| Distributed hyperparameter tuning (similar experience to Hyperopt with `SparkTrials`) | [RayTune](/concepts/raytune.md) |

- **Optuna** is the preferred choice for single‑machine tuning. It provides a modern, lightweight API and is actively maintained. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]
- **RayTune** offers a distributed tuning experience comparable to Hyperopt’s `SparkTrials`. It integrates with MLflow and can scale across multiple nodes. Databricks provides specific guidance on using [RayTune on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow). ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

For users already working with [MLflow](/concepts/mlflow.md), both alternatives log trial results natively, making migration straightforward.

## Impact on existing notebooks

Notebooks and training pipelines that depend on Hyperopt (e.g., `hyperopt.fmin` with `SparkTrials`) will fail if they run on Databricks Runtime ML versions later than 16.4 LTS ML. Users must either:

1. Pin their cluster to a Databricks Runtime ML version ≤ 16.4 LTS ML (not recommended for new work), or
2. Migrate the hyperparameter search code to Optuna or RayTune.

Databricks documentation includes a [notebook example](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) for Optuna and a RayTune integration guide to assist with migration. ^[model-training-examples-databricks-on-aws.md]

## Migration considerations

- **Single‑node workflows**: Optuna is the simplest drop‑in replacement. It supports similar search algorithms (e.g., Tree‑structured Parzen Estimator, grid, random) and can be used with minimal code changes.
- **Distributed workflows**: RayTune provides `Tuner` and `tune.run` APIs that replace Hyperopt’s `SparkTrials`. RayTune can leverage [Ray on Databricks](/concepts/ray-on-databricks.md) for multi‑node scaling.
- **Hyperopt‑specific features**: `hp.choice`, `hp.uniform`, and conditional spaces can be replicated in both Optuna and RayTune. Users who relied on Hyperopt’s `SparkTrials` for Spark integration should evaluate RayTune’s distributed scheduler.
- **Best practices**: Databricks previously published Hyperopt best practices (e.g., using `hp.choice` with `hyperopt.space_eval` for value retrieval, avoiding autoscaling clusters with `SparkTrials`). These guidelines are now superseded by the respective Optuna and RayTune documentation. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Related concepts

- [Optuna](/concepts/optuna.md) – recommended single‑node hyperparameter optimization library
- [RayTune](/concepts/raytune.md) – recommended distributed hyperparameter tuning library
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – versioned runtime that determines library availability
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – general concepts and tools
- [SparkTrials](/concepts/sparktrials.md) – deprecated Hyperopt integration with Spark
- [MLflow](/concepts/mlflow.md) – experiment tracking used with all three frameworks
- [Ray on Databricks](/concepts/ray-on-databricks.md) – infrastructure for running Ray workloads

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
- hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
- model-training-examples-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
2. [hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md](/references/hyperopt-best-practices-and-troubleshooting-databricks-on-aws-838e4655.md)
3. [model-training-examples-databricks-on-aws.md](/references/model-training-examples-databricks-on-aws-47a05943.md)
