---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2a0790b41f253b29c35ee34ee4ecaab0eb7d11c5b1906e02a9f6f129edbbc4e
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nccl-network-configuration-for-distributed-gpu-xgboost
    - NNCFDGX
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: NCCL Network Configuration for Distributed GPU XGBoost
description: Troubleshooting NCCL communication failures in multi-node GPU training by setting NCCL_SOCKET_IFNAME environment variable to eth
tags:
  - gpu
  - networking
  - troubleshooting
  - xgboost
timestamp: "2026-06-19T10:17:45.575Z"
---

# NCCL Network Configuration for Distributed GPU XGBoost

**NCCL Network Configuration for Distributed GPU XGBoost** refers to the environment variable settings required to ensure reliable GPU‑to‑GPU communication via the NVIDIA Collective Communications Library (NCCL) when training distributed XGBoost models on multiple nodes. Incorrect NCCL network interface configuration is a common source of failures in multi‑node GPU training.

## Overview

When using the `xgboost.spark` module with `use_gpu=True` and `num_workers > 1`, the distributed training process relies on NCCL to exchange gradients and model data across GPUs on different nodes. NCCL must select a suitable network interface (e.g., Ethernet, InfiniBand) for inter‑node communication. On some cluster configurations, NCCL may fail to use the correct interface, leading to a training error. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## NCCL Failure Error

During multi‑node GPU training, the following error message indicates a network communication problem:

```
NCCL failure: remote process exited or there was a network error
```

This error typically arises because NCCL cannot use certain network interfaces for GPU communication across nodes. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Resolution: Setting `NCCL_SOCKET_IFNAME`

To resolve the issue, set the cluster’s Spark configuration property `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This assigns the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all worker processes on each node, forcing NCCL to use the Ethernet interface for socket‑based communication. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

This configuration can be applied when creating or editing a Databricks cluster, in the **Spark Config** section:

| Key | Value |
|-----|-------|
| `spark.executorEnv.NCCL_SOCKET_IFNAME` | `eth` |

After saving and restarting the cluster, subsequent distributed GPU XGBoost training jobs will use the correct network interface.

## Related Concepts

- [Distributed XGBoost Training on Databricks](/concepts/distributed-xgboost-training-on-databricks.md) – Using `xgboost.spark` with `num_workers`.
- [GPU Training with xgboost.spark](/concepts/gpu-training-with-xgboostspark.md) – Enabling GPU acceleration (`use_gpu=True`).
- NCCL (NVIDIA Collective Communications Library) – The library used for multi‑GPU communication.
- Spark Configuration for GPU Clusters – Other relevant Spark settings such as `spark.task.resource.gpu.amount`.

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
