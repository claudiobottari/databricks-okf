---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4e8de65b3fa2d10c4691b05302d23b756be7d63c7181ca97c3cee3ee4397981
  pageDirectory: concepts
  sources:
    - hyperopt-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-deprecation-and-migration
    - migration and Hyperopt deprecation
    - HDAM
  citations:
    - file: hyperopt-concepts-databricks-on-aws.md
title: Hyperopt deprecation and migration
description: Hyperopt is no longer maintained and is excluded from Databricks Runtime ML after 16.4 LTS; Databricks recommends Optuna or RayTune as replacements.
tags:
  - deprecation
  - migration
  - Optuna
  - RayTune
  - Hyperopt
timestamp: "2026-06-19T19:08:06.080Z"
---

# Hyperopt Deprecation and Migration

The open-source version of **Hyperopt** is no longer being maintained, and Databricks has announced its removal from Databricks Runtime for Machine Learning (Databricks Runtime ML) starting after version **16.4 LTS ML**.^[hyperopt-concepts-databricks-on-aws.md] Users of Hyperopt on Databricks should plan to migrate their hyperparameter tuning workflows to supported alternatives.

## Deprecation Status

Hyperopt is not included in Databricks Runtime ML releases after 16.4 LTS ML. The open-source project is no longer actively maintained, which means no new features, bug fixes, or security patches will be provided.^[hyperopt-concepts-databricks-on-aws.md] The `SparkTrials` API, which was developed by Databricks to distribute Hyperopt runs across a Spark cluster, is also deprecated along with the rest of the Hyperopt integration.

## Recommended Migration Paths

Databricks recommends two primary alternatives, depending on the scale of your tuning workload:

- **[Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna)** – Best suited for **single-node optimization**. Optuna is a modern, actively maintained hyperparameter optimization framework that offers a similar API to Hyperopt’s `fmin()` and provides built-in pruning, sampling, and visualization capabilities.^[hyperopt-concepts-databricks-on-aws.md]

- **[RayTune](https://docs.ray.io/en/latest/tune/index.html)** – Recommended for **distributed hyperparameter tuning**, providing a drop-in replacement for the distributed functionality previously offered by `SparkTrials`. RayTune scales across a cluster of machines and integrates natively with [MLflow](/concepts/mlflow.md) for experiment tracking. Databricks provides guidance on using [RayTune on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow).^[hyperopt-concepts-databricks-on-aws.md]

## Migration Considerations

When migrating from Hyperopt, note the following key differences:

- **`fmin()` and `Trials`** – Hyperopt’s `fmin()` function and its `Trials` class (used for single-machine tuning) have no direct equivalent in Optuna or RayTune, but both frameworks offer comparable APIs. Optuna uses an `optuna.study` object and a `study.optimize()` call. RayTune provides a `tune.run()` API.

- **`SparkTrials`** – The `SparkTrials` class was specific to Databricks. For distributed tuning, RayTune is the recommended replacement. RayTune supports distribution via the `ray.tune.run()` function with `num_samples` and `resources_per_trial` parameters.

- **Parallelism and adaptivity trade-offs** – Both Optuna and RayTune offer configurable parallelism, similar to Hyperopt’s `parallelism` parameter in `SparkTrials`. The trade-off between speed and adaptivity (ability to use past results for smarter search) remains the same.

- **MLflow integration** – Hyperopt logged tuning results as nested MLflow runs via `SparkTrials`. Both Optuna and RayTune offer integrations with [MLflow](/concepts/mlflow.md) for automatic logging of trials and hyperparameters. Databricks recommends managing active runs explicitly when using these frameworks.^[hyperopt-concepts-databricks-on-aws.md]

- **Existing code** – Code that uses `hyperopt.fmin()`, `hyperopt.SparkTrials`, or `hyperopt.Trials` will need to be rewritten. The general logic (define an objective function, define a search space, run optimization) can be preserved, but the framework-specific APIs must be replaced.

## Related Concepts

- [Optuna](/concepts/optuna.md) – Hyperparameter optimization library for single-node use.
- [RayTune](/concepts/raytune.md) – Distributed hyperparameter tuning framework built on Ray.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model management platform.
- [Distributed hyperparameter tuning](/concepts/raytune-for-distributed-hyperparameter-tuning-on-databricks.md) – Techniques for scaling hyperparameter search across a cluster.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The machine learning runtime environment on Databricks.

## Sources

- hyperopt-concepts-databricks-on-aws.md

# Citations

1. [hyperopt-concepts-databricks-on-aws.md](/references/hyperopt-concepts-databricks-on-aws-853fbb92.md)
