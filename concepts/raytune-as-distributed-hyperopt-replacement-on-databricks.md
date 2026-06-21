---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa6d41356493b5aca2a42263527a9839b59883d3f23024db4691e7036002973e
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - raytune-as-distributed-hyperopt-replacement-on-databricks
    - RADHROD
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: RayTune as distributed Hyperopt replacement on Databricks
description: Databricks recommends RayTune as a replacement for Hyperopt's distributed hyperparameter tuning functionality
tags:
  - databricks
  - hyperparameter-tuning
  - ray
  - distributed-computing
timestamp: "2026-06-19T17:47:50.562Z"
---

# RayTune as Distributed Hyperopt Replacement on Databricks

**RayTune** is a distributed hyperparameter tuning framework that Databricks recommends as a replacement for the deprecated open-source Hyperopt library. It provides a similar experience to Hyperopt's distributed tuning functionality, but with ongoing maintenance and support. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Background

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained, and it is not included in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) after version 16.4 LTS ML. Databricks recommends migrating to one of two alternatives depending on the workload: ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

- **[Optuna](/concepts/optuna.md)** – for single-node hyperparameter optimization.
- **RayTune** – for distributed hyperparameter tuning that closely mirrors the functionality previously provided by Hyperopt with `SparkTrials`.

## Using RayTune on Databricks

RayTune can be used on Databricks with the Ray integration. For full details, see the documentation on [using RayTune on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow). ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) – The deprecated library that RayTune replaces for distributed tuning.
- [Optuna](/concepts/optuna.md) – Alternative single-node hyperparameter optimization library.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – General process of searching for optimal hyperparameters.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment where tuning libraries are included.
- [Ray on Databricks](/concepts/ray-on-databricks.md) – The platform for running distributed Ray workloads, including RayTune.

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
