---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e45a7c71609e358e3a9730d51b616098b78831b6bcdd772501d29b5f74567a0
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-distributed-xgboost
    - LODX
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: Limitations of Distributed XGBoost
description: "Restrictions when using distributed XGBoost on Databricks: no mlflow.xgboost.autolog, no baseMarginCol, and incompatibility with autoscaling clusters."
tags:
  - machine-learning
  - limitations
  - xgboost
  - spark
timestamp: "2026-06-19T10:17:06.541Z"
---

# Limitations of Distributed XGBoost

**Limitations of Distributed XGBoost** refers to the constraints and unsupported features when training XGBoost models in a distributed manner using `sparkdl.xgboost` on Databricks. While distributed training can accelerate model training by leveraging multiple Spark task slots, certain functionalities are restricted or unavailable in distributed mode.

## Unsupported Features

### [MLflow Autologging](/concepts/mlflow-autologging.md)

You cannot use `mlflow.xgboost.autolog` with distributed XGBoost. Automatic logging of parameters, metrics, and models is not supported when training is distributed across multiple workers. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

### baseMarginCol Parameter

The `baseMarginCol` parameter is not supported with distributed XGBoost. If your workflow requires base margin values for each training instance, you cannot use distributed training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Infrastructure Constraints

### Autoscaling Clusters

Distributed XGBoost training cannot run on a cluster with autoscaling enabled. The cluster must have a fixed number of workers to ensure consistent resource allocation during distributed training. To use distributed XGBoost, you must disable autoscaling on the cluster. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Considerations

When using distributed XGBoost, ensure that the `num_workers` parameter is set to a value less than or equal to the total number of Spark task slots on your cluster. Setting `num_workers=sc.defaultParallelism` uses all available Spark task slots. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

For GPU training with distributed XGBoost, be aware of potential NCCL communication errors that can occur when NCCL cannot use certain network interfaces for GPU communication across nodes. See NCCL Network Configuration for troubleshooting guidance. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Deprecation Note

The `sparkdl.xgboost` module is deprecated since Databricks Runtime 12.0 ML. Databricks recommends migrating code to use the `xgboost.spark` module instead. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [Distributed XGBoost Training](/concepts/distributed-xgboost-training-on-databricks.md) — Setting up multi-worker XGBoost training
- [XGBoost GPU Training](/concepts/gpu-accelerated-xgboost-training.md) — GPU-enabled XGBoost training configurations
- SparkDL XGBoost Migration — Guide for migrating to `xgboost.spark`
- Autoscaling Clusters — Cluster configuration for Databricks

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
