---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b814d085675dfc44e12ae0a1ee8c0827b1c222d5e706f15499b55e4120e6538
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-train-resource-allocation
    - RTRA
    - Ray Train
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: Ray Train Resource Allocation
description: Configuration guidance for setting resources_per_worker in Ray Train to avoid resource contention on Databricks clusters.
tags:
  - ray
  - databricks
  - resource-management
timestamp: "2026-06-19T19:11:20.498Z"
---

# Ray Train Resource Allocation

**Ray Train Resource Allocation** refers to the configuration of compute resources — particularly CPUs — for [Ray Train](/concepts/ray-train-resource-allocation.md) workers to avoid resource contention when running on Databricks clusters. Proper resource allocation ensures that Ray actors do not reserve all available cores, which can lead to errors during distributed training. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Configuring `resources_per_worker`

To prevent resource contention between Ray workers and other processes on the same node, you must adjust the `resources_per_worker` setting when using Ray Train on Databricks. Specifically, set the number of CPUs for each Ray worker to be **one less** than the total number of CPUs available on a Ray worker node. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

For example, if a worker node has 8 CPUs, configure each worker to use 7 CPUs:

```python
trainer = ray.train.torch.TorchTrainer(
    ...,
    scaling_config=ray.train.ScalingConfig(
        num_workers=4,
        resources_per_worker={"CPU": 7},  # leave one CPU free
    ),
)
```

This adjustment is crucial because if the trainer reserves **all** available cores for its Ray actors, it can lead to resource contention errors. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Fault Tolerance and Resource Management

Resource allocation for Ray Train is managed by [Ray Train](/concepts/ray-train-resource-allocation.md) itself, not by [MLflow](/concepts/mlflow.md). MLflow is responsible for tracking the model’s lifecycle — logging metrics, parameters, and artifacts — but does not handle fault tolerance during training. Ray Train independently manages checkpointing and recovery. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed model training framework.
- Ray Core – General-purpose distributed applications.
- [Ray Tune](/concepts/ray-tune.md) – Distributed hyperparameter tuning.
- MLflow Integration with Ray – Tracking Ray workloads with MLflow.
- Databricks Cluster Configuration – Setting up Spark and Ray clusters.

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
