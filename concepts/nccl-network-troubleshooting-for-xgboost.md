---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24558ad2bb880118a29b28b40d1ff4aa48f2d34a4b976f0f90f5113a5133e801
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nccl-network-troubleshooting-for-xgboost
    - NNTFX
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: NCCL Network Troubleshooting for XGBoost
description: Troubleshooting NCCL network failures in multi-node GPU training by setting spark.executorEnv.NCCL_SOCKET_IFNAME=eth to fix inter-GPU communication issues.
tags:
  - troubleshooting
  - gpu
  - networking
  - xgboost
timestamp: "2026-06-18T12:06:16.970Z"
---

# NCCL Network Troubleshooting for XGBoost

**NCCL Network Troubleshooting for XGBoost** addresses network communication failures that occur during distributed XGBoost training using GPUs. When performing multi-node GPU training with `xgboost.spark`, the NVIDIA Collective Communications Library (NCCL) manages GPU-to-GPU communication across worker nodes, and network misconfigurations can cause training to fail. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Error Message

During multi-node training with GPU workers, NCCL failures typically present with the following error:

```
NCCL failure: remote process exited or there was a network error
```

^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Cause

NCCL relies on network interfaces for inter-node GPU communication. The error occurs when NCCL cannot use certain network interfaces on the worker nodes — for example, when the interface NCCL attempts to use is not available, misconfigured, or blocked by firewall rules. This is a common issue in cloud and cluster environments where network interface naming may differ from NCCL's default expectations. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Solution

Set the Spark configuration `spark.executorEnv.NCCL_SOCKET_IFNAME` to `eth` on the cluster. This sets the environment variable `NCCL_SOCKET_IFNAME` to `eth` for all workers on every node, instructing NCCL to use the `eth` network interface for GPU communication. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Configuration Steps

1. Navigate to your cluster configuration in the Databricks workspace.
2. In the **Spark Config** section, add the following line:
   ```
   spark.executorEnv.NCCL_SOCKET_IFNAME eth
   ```
3. Restart the cluster for the configuration to take effect.

Alternatively, you can set this programmatically when creating the Spark session:

```python
spark.conf.set("spark.executorEnv.NCCL_SOCKET_IFNAME", "eth")
```

## Additional Considerations

### GPU Training with XGBoost Spark

When using GPU training with `xgboost.spark`, ensure the following:

- Set `use_gpu=True` on the XGBoost estimator. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- For distributed GPU training with `num_workers`, each Spark task uses only one GPU. Databricks recommends using the default value of `1` for the Spark cluster configuration `spark.task.resource.gpu.amount` to avoid idle GPUs. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

### Disable Autoscaling

Distributed XGBoost training cannot run on a cluster with autoscaling enabled. New worker nodes that start during elastic scaling cannot receive new sets of tasks and remain idle. Disable autoscaling on the cluster before running distributed training. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Example Configuration

The following example configures an XGBoost classifier for distributed GPU training on a cluster where NCCL is configured to use the `eth` interface:

```python
from xgboost.spark import SparkXGBClassifier

classifier = SparkXGBClassifier(
    num_workers=sc.defaultParallelism,
    use_gpu=True
)
```

This classifier distributes training across all available Spark task slots using GPUs. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- XGBoost Spark Distributed Training — Multi-node XGBoost training using the `xgboost.spark` module
- [GPU Training with XGBoost](/concepts/gpu-training-with-xgboostspark.md) — Configuring GPU resources for XGBoost on Spark
- NCCL Configuration — NCCL environment variables for network communication tuning
- Spark Cluster Autoscaling — Impact of autoscaling on distributed training reliability

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
