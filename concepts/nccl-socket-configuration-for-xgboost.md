---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bdfefd93de8659613f70bd9b2e1bd03609973dc641dfe096c3fa0f3edf02360
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nccl-socket-configuration-for-xgboost
    - NSCFX
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: NCCL Socket Configuration for XGBoost
description: Troubleshooting NCCL failures during multi-node GPU training by setting spark.executorEnv.NCCL_SOCKET_IFNAME=eth to fix network communication issues.
tags:
  - troubleshooting
  - networking
  - xgboost
timestamp: "2026-06-19T18:35:56.427Z"
---

# NCCL Socket Configuration for XGBoost

The **NCCL Socket Configuration for XGBoost** refers to setting the environment variable `NCCL_SOCKET_IFNAME` when training [XGBoost](/concepts/xgboostspark-module.md) models on multiple GPU nodes using Databricks. This configuration resolves network communication errors that can occur when NCCL (NVIDIA Collective Communications Library) tries to use the wrong network interface for GPU-to-GPU communication across nodes. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Background

When performing distributed training of XGBoost models with GPU support enabled (by setting `use_gpu=True` in `xgboost.spark` estimators), the underlying NCCL library handles collective communication among GPUs across different worker nodes. NCCL attempts to automatically detect and use available network interfaces. On some cluster configurations, NCCL may fail to select the correct interface, leading to a connection error. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Error Message

The error manifests as:

```
NCCL failure: remote process exited or there was a network error
```

This message indicates a problem with network communication among GPUs. The issue arises when NCCL cannot use certain network interfaces for GPU communication. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Configuration

To resolve the NCCL network error during multi-node XGBoost training, set the Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth`. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all worker nodes in the cluster. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### How to Set

- **Via Spark Config**: Add `spark.executorEnv.NCCL_SOCKET_IFNAME eth` to the cluster's Spark configuration (in the cluster creation UI under Advanced options → Spark config).
- **Programmatically**: If using a notebook, you can set it before creating the Spark session, but typically it is set at cluster level.

After applying this configuration, NCCL will use the Ethernet interface (`eth`) for inter-node communication, which usually resolves the failure.

## Notes

- This configuration is only needed for multi-node GPU training. Single-node training with GPUs does not use NCCL for inter-node communication.
- The same environment variable can be set to other interface names (e.g., `ib0` for InfiniBand) if appropriate for the cluster's network topology, but `eth` is the common fix on Databricks clusters with Ethernet networking.
- Ensure the cluster has Spark GPU Scheduling properly configured with `spark.task.resource.gpu.amount = 1` as recommended for XGBoost GPU training.

## Related Concepts

- NCCL — The NVIDIA collective communications library used for GPU communication.
- [XGBoost GPU Training](/concepts/gpu-accelerated-xgboost-training.md) — Using GPUs with XGBoost on Databricks.
- [xgboost.spark](/concepts/xgboostspark-module.md) — The PySpark module for distributed XGBoost.
- spark.executorEnv — Mechanism to pass environment variables to Spark executors.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concept of training models across multiple workers.

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
