---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3129962d54b8e75015ec62747d8fb81d2d0d42beeb8ee968cd308f2444df269
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-deprecation-policy
    - DRMDP
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Databricks Runtime ML Deprecation Policy
description: Databricks Runtime for Machine Learning drops Hyperopt after version 16.4 LTS ML, reflecting a shift toward Optuna and RayTune.
tags:
  - databricks
  - runtime
  - platform-changes
timestamp: "2026-06-18T11:04:10.070Z"
---

# Databricks Runtime ML Deprecation Policy

**Databricks Runtime ML Deprecation Policy** describes the lifecycle for features, libraries, and tools that are removed or replaced in Databricks Runtime for Machine Learning. When a component is deprecated, Databricks communicates the timeline and recommended migration paths, giving users time to adapt their workflows before the component is removed from future releases. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Overview

Databricks periodically updates the libraries and tools bundled in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) to align with community developments, security requirements, and performance improvements. Deprecated components are announced in release notes and documented in migration guides. Users are expected to move to the recommended alternatives before the deprecated component is removed from the runtime. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Deprecated Components

### Hyperopt

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained. Hyperopt is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Timeline

- **Hyperopt inclusion**: Present in Databricks Runtime ML through version 16.4 LTS ML.
- **Removal**: Hyperopt is removed starting from version 17.0 (and later releases). ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Recommended Migrations

For hyperparameter tuning that was previously done with Hyperopt, Databricks recommends the following alternatives:

- **[Optuna](/concepts/optuna.md)** for single-node optimization.
- **[RayTune](/concepts/raytune.md)** for distributed hyperparameter tuning that provides a similar experience to the deprecated Hyperopt distributed functionality. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

RayTune can be used on Databricks with [Ray on Databricks](/concepts/ray-on-databricks.md) integration, and Optuna works directly in notebooks and jobs. See the migration documentation for detailed examples of converting Hyperopt workflows to these alternatives. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The machine learning runtime that packages libraries and tools
- [Hyperopt](/concepts/hyperopt.md) — The open-source hyperparameter optimization library (deprecated)
- [Optuna](/concepts/optuna.md) — Recommended single-node hyperparameter optimizer
- [RayTune](/concepts/raytune.md) — Recommended distributed hyperparameter tuning framework
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management (used alongside tuning libraries)

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
