---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9aae5a8e32e308b63331893203693b393a84f9c58b1a0ef79db73ff69a73d18
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-distributed-xgboost-on-databricks
    - LODXOD
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: Limitations of Distributed XGBoost on Databricks
description: "Key restrictions when using distributed XGBoost training: mlflow.xgboost.autolog is unavailable, baseMarginCol cannot be used, and autoscaling clusters are not supported"
tags:
  - limitations
  - distributed-training
  - databricks
timestamp: "2026-06-19T18:35:24.600Z"
---

# Limitations of Distributed XGBoost on Databricks

Distributed training of XGBoost models using the deprecated `sparkdl.xgboost` module imposes several restrictions that do not apply in single‑worker mode. These limitations must be considered before enabling distributed training via the `num_workers` parameter.

> **Note:** The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating to the `xgboost.spark` module. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Limitations of Distributed Training

### [MLflow Autologging](/concepts/mlflow-autologging.md) Not Supported

You **cannot** use `mlflow.xgboost.autolog` with distributed XGBoost training. The autologging utility is not designed for the distributed workflow and may cause errors or incomplete logging. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### `baseMarginCol` Not Supported

The `baseMarginCol` parameter is not supported when `num_workers > 1`. You must omit or set it only for single‑worker training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### Autoscaling Incompatibility

Distributed XGBoost **cannot** be used on a cluster with autoscaling enabled. New worker nodes that join an autoscaling cluster during training cannot receive new task sets and remain idle, wasting resources and potentially causing training failure. To use distributed training, disable autoscaling in the cluster configuration. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## General Parameter Restrictions (All Training Modes)

The following parameters from the `xgboost` package are **not supported** in the `sparkdl.xgboost` module, regardless of whether training is distributed:

- `gpu_id`, `output_margin`, `validate_features`
- `sample_weight`, `eval_set`, `sample_weight_eval_set` (use `weightCol` and `validationIndicatorCol` instead)
- `base_margin`, `base_margin_eval_set` (use `baseMarginCol` instead)

These are not distributed‑mode limitations but must be noted when using the module. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [Distributed XGBoost Training](/concepts/distributed-xgboost-training-on-databricks.md) — Configuring the `num_workers` parameter
- [MLflow Autologging](/concepts/mlflow-autologging.md) — Logging models in single‑worker mode
- Autoscaling Clusters — Cluster configuration and autoscaling
- [XGBoost Parameter Reference](/concepts/sparkdlxgboost-parameter-differences-from-xgboost-package.md) — Supported and unsupported parameters per module
- [sparkdl.xgboost vs xgboost.spark Migration](/concepts/migration-from-sparkdlxgboost-to-xgboostspark.md) — Guidance for migrating to the recommended module

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
