---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c07ae09b49beae5fb96ec88eb2b82d4ef2ba47f31c4af67f6e44168ce98e5dc
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autoscaling-restriction-for-distributed-xgboost
    - ARFDX
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: Autoscaling Restriction for Distributed XGBoost
description: Distributed XGBoost training cannot be used on clusters with autoscaling enabled because new worker nodes remain idle
tags:
  - autoscaling
  - spark
  - xgboost
  - cluster-configuration
timestamp: "2026-06-19T10:17:54.516Z"
---

# Autoscaling Restriction for Distributed XGBoost

**Autoscaling Restriction for Distributed XGBoost** refers to the incompatibility between distributed XGBoost training (using the `xgboost.spark` module) and cluster autoscaling on Databricks. When autoscaling is enabled, new worker nodes that are added during training cannot receive new sets of tasks and remain idle, making distributed training ineffective. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Cause

Distributed XGBoost in `xgboost.spark` uses the `num_workers` parameter to spawn a fixed number of concurrent Spark tasks for training. When a cluster autoscales (adds or removes nodes), the task allocation mechanism cannot assign work to the newly added workers. These new nodes stay idle, wasting resources and causing the training job to stall or fail to complete. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Recommended Practice

To use distributed XGBoost, disable autoscaling on the cluster before starting the training job. Instructions to disable autoscaling are provided in the Databricks documentation on Enable autoscaling. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- [Distributed XGBoost](/concepts/distributed-training-with-xgboostspark.md) – Training XGBoost models across multiple workers using `xgboost.spark`.
- XGBoost on Databricks – General guidance for using XGBoost on the Databricks platform.
- Cluster Configuration – How to configure fixed-size clusters for distributed training.
- Autoscaling on Databricks – The mechanism that dynamically adjusts cluster size.

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
