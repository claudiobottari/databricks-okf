---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c29f3795308d115c36bf85f3fa8efedf352366500d5f65df150d05f8ce6b6435
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nccl-socket-configuration-for-spark-xgboost
    - NSCFSX
  citations:
    - file: distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md
title: NCCL Socket Configuration for Spark XGBoost
description: Troubleshooting NCCL communication failures during multi-node GPU training by setting spark.executorEnv.NCCL_SOCKET_IFNAME to eth.
tags:
  - troubleshooting
  - networking
  - gpu
  - xgboost
timestamp: "2026-06-19T10:17:27.673Z"
---

# NCCL Socket Configuration for Spark XGBoost

When performing distributed training of XGBoost models using `sparkdl.xgboost` on multi-node GPU clusters, you may encounter a `NCCL failure: remote process exited or there was a network error` message. This error indicates a problem with network communication among GPUs, arising when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Resolution

To resolve this issue, set the cluster's Spark configuration (`sparkConf`) for `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This effectively sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers in a node. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Configuration Detail

The configuration parameter `NCCL_SOCKET_IFNAME` controls which network interface NCCL uses for inter-node GPU communication. By setting it to `eth`, you instruct NCCL to use the Ethernet interface, which can resolve network connectivity issues that occur when NCCL cannot properly identify or use the available network interfaces. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Application Scope

This configuration is specifically relevant when using [sparkdl.xgboost](/concepts/sparkdlxgboost-module.md) with the `num_workers` parameter for distributed GPU training. It is not typically needed for single-node training or CPU-based distributed training. ^[distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md]

## Related Concepts

- [Distributed XGBoost Training](/concepts/distributed-xgboost-training-on-databricks.md)
- [GPU Training with XGBoost](/concepts/gpu-training-with-xgboostspark.md)
- Spark Configuration
- NCCL
- Multi-node GPU Communication

## Sources

- distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-sparkdlxgboost-databricks-on-aws-08446b58.md)
