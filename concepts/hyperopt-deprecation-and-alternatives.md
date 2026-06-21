---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d4f41b1b80c3b03c6d92097d0631fea4e19a1ed94908d37196d7848ad2c8229
  pageDirectory: concepts
  sources:
    - parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-deprecation-and-alternatives
    - Alternatives and Hyperopt Deprecation
    - HDAA
  citations:
    - file: parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
title: Hyperopt Deprecation and Alternatives
description: The open-source Hyperopt library is no longer maintained and is removed from Databricks Runtime ML after 16.4 LTS. Databricks recommends Optuna for single-node or RayTune for distributed tuning.
tags:
  - hyperopt
  - deprecation
  - optuna
  - raytune
  - databricks
timestamp: "2026-06-19T19:54:10.439Z"
---

# Hyperopt Deprecation and Alternatives

**Hyperopt Deprecation and Alternatives** describes the end‑of‑life status of the open‑source Hyperopt library and the recommended migration paths for users on Databricks. The official Hyperopt project is no longer maintained, and support has been removed from the Databricks Machine Learning runtime starting with version 16.4 LTS ML. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Deprecated Hyperopt

The open‑source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained. Consequently, Hyperopt is not included in Databricks Runtime for Machine Learning after **16.4 LTS ML**. This affects users who relied on Hyperopt’s built‑in integration in the Databricks environment, including the `SparkTrials` class for distributed hyperparameter tuning. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Recommended Alternatives

Databricks recommends two primary replacement libraries depending on the workload:

| Use case | Recommended library | Notes |
|----------|---------------------|-------|
| Single‑node optimization | [Optuna](/concepts/optuna.md) | A lightweight, search‑space‑driven framework well suited for sequential tuning. |
| Distributed (parallel) tuning | [RayTune](/concepts/raytune.md) | Provides a similar experience to the deprecated Hyperopt `SparkTrials` distributed functionality. |

Users should migrate existing Hyperopt scripts to these libraries. Databricks provides documentation on using RayTune on Databricks to replicate the distributed tuning workflow. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Example of the Deprecated Workflow

The deprecated pattern used `SparkTrials` together with `fmin()` to distribute objective evaluations across a Spark cluster. A typical code snippet looked like:

```python
from hyperopt import fmin, tpe, hp, SparkTrials, STATUS_OK

def objective(params):
    # ... model training and evaluation ...
    return {'loss': loss, 'status': STATUS_OK}

search_space = hp.choice('x', [1, 2, 3])
spark_trials = SparkTrials()
argmin = fmin(fn=objective, space=search_space, algo=tpe.suggest, max_evals=16, trials=spark_trials)
```

This pattern is no longer supported after Databricks Runtime 16.4 LTS ML. Users should migrate to either Optuna (single‑node) or RayTune (distributed) to achieve equivalent functionality. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Migration Guidance

- **Single‑node optimization**: Replace Hyperopt’s `fmin` with Optuna’s `study.optimize`. Optuna uses a similar trial‑based API and supports many of the same search algorithms (e.g., TPE, random).
- **Distributed tuning**: Use RayTune with a cluster running [Ray on Databricks](/concepts/ray-on-databricks.md). RayTune natively supports distributed execution, checkpointing, and integration with [MLflow](/concepts/mlflow.md) tracking.
- **Inline code**: Remove any imports from `hyperopt` and `SparkTrials`. Update objective functions to match the library’s conventions.

For more information, refer to the Databricks documentation on Optuna integration and RayTune on Databricks. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) – The deprecated library; open‑source maintenance has ceased.
- [Optuna](/concepts/optuna.md) – Recommended single‑node hyperparameter optimization framework.
- [RayTune](/concepts/raytune.md) – Recommended distributed hyperparameter optimization framework.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime that removed Hyperopt support after version 16.4 LTS ML.
- [SparkTrials](/concepts/sparktrials.md) – The deprecated Hyperopt class for parallel tuning across Spark.
- [MLflow](/concepts/mlflow.md) – Automatic experiment tracking still available for both Optuna and RayTune workflows.
- [Ray on Databricks](/concepts/ray-on-databricks.md) – Infrastructure for running Ray clusters, enabling RayTune.

## Sources

- parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md](/references/parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws-b91f741c.md)
