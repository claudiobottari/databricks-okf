---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 013d25f00d277401187dbde37357573b4a0fa02f1a3f1e04c41dde3d1f1bca3f
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deprecation-of-sparkdlxgboost-in-favor-of-xgboostspark
    - DOSIFOX
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: Deprecation of sparkdl.xgboost in Favor of xgboost.spark
description: The sparkdl.xgboost module is deprecated since Databricks Runtime 12.0 ML, with recommendation to migrate to the xgboost.spark module
tags:
  - deprecation
  - migration
  - databricks
  - xgboost
timestamp: "2026-06-19T18:35:44.596Z"
---

# Deprecation of sparkdl.xgboost in Favor of xgboost.spark

The `sparkdl.xgboost` module, which provided PySpark estimators (`XgboostRegressor` and `XgboostClassifier`) for [XGBoost](/concepts/xgboostspark-module.md) model training, has been **deprecated** since **Databricks Runtime 12.0 ML**. Databricks recommends that existing users migrate their code to the `xgboost.spark` module, which is the modern and actively maintained alternative. A migration guide is available to assist with the transition.^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Background

`sparkdl.xgboost` was designed to integrate XGBoost with [PySpark ML Pipelines](/concepts/mllib-pipelines-api.md). It supported both distributed training (via the `num_workers` parameter) and GPU training (via `use_gpu=True`). However, the module is now deprecated and users should move to `xgboost.spark` for long-term support and compatibility with newer Databricks Runtime versions.^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Migration Path

Databricks provides a dedicated migration guide to help users transition from `sparkdl.xgboost` to `xgboost.spark`. The guide covers code changes, parameter mappings, and any behavioral differences between the two modules. See [the migration guide](https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost-spark#xgboost-migration) for detailed instructions.^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Features of sparkdl.xgboost (for context)

While deprecated, `sparkdl.xgboost` offered the following capabilities:

- **Distributed training** – Set `num_workers` to a value ≤ the total number of Spark task slots. To use all slots, set `num_workers=sc.defaultParallelism`.
- **GPU training** – Set `use_gpu=True` on clusters with compatible GPUs (requires compute capability 5.2+ for Databricks Runtime 11.3 LTS ML and above).
- **PySpark ML Pipeline integration** – Estimators could be used as stages in a `Pipeline`.

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Limitations of Distributed Training

When using the distributed training mode in `sparkdl.xgboost`, the following limitations applied:

- `mlflow.xgboost.autolog` is not supported.
- `baseMarginCol` is not supported.
- Distributed training cannot run on a cluster with autoscaling enabled.

^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Troubleshooting (sparkdl.xgboost)

During multi-node training, an error `NCCL failure: remote process exited or there was a network error` may occur due to NCCL communication issues. The recommended workaround is to set the Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth` in the cluster’s Spark configuration. This sets the environment variable `NCCL_SOCKET_IFNAME` for all workers on a node.^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Notebook Example

A sample notebook demonstrating `sparkdl.xgboost` usage with Spark MLlib is available in the Databricks documentation. The notebook notes the deprecation and the recommended migration.^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – The underlying gradient boosting library.
- [PySpark ML Pipeline](/concepts/mllib-pipelines-api.md) – The API for building machine learning pipelines in Spark.
- [xgboost.spark](/concepts/xgboostspark-module.md) – The recommended replacement module for XGBoost integration with PySpark.
- [MLflow](/concepts/mlflow.md) – Logging and tracking of machine learning experiments (note: autolog not supported with distributed `sparkdl.xgboost`).
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Training models across multiple workers in a Spark cluster.
- GPU Training on Databricks – Using GPU accelerators for model training.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The ML-optimized runtime that includes these libraries.

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
