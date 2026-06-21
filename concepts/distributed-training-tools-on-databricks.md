---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce0198d5a96113c836793a6214fa1cc9ff2ee3170d493888ea1f494f25557678
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-tools-on-databricks
    - DTTOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Distributed Training Tools on Databricks
description: Built-in distributed training support via TorchDistributor, DeepSpeed, and Ray, plus adaptive hyperparameter tuning with Optuna.
tags:
  - distributed-training
  - databricks
  - pytorch
timestamp: "2026-06-19T09:10:01.778Z"
---

# Distributed Training Tools on Databricks

**Distributed Training Tools on Databricks** refer to the built-in libraries and frameworks within [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) that enable scaling deep learning workloads from a single GPU to multi-GPU and multi-node clusters. These tools help manage the complexity of distributed training—including model sharding, communication overhead, and hyperparameter tuning—so that data scientists can train larger models more efficiently.

## Overview

Databricks Runtime ML includes a curated set of distributed training libraries that are pre-installed and pre-configured for GPU clusters. These tools support both PyTorch and TensorFlow workflows and integrate with [MLflow Tracking](/concepts/mlflow-tracking.md) for experiment logging. The recommended path for distributed training begins with a [Single Node cluster](/concepts/single-node-clusters-for-pytorch.md) (driver only) for development, then moves to distributed training when the dataset or model size exceeds single-node capacity. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

The primary distributed training tools on Databricks are:

| Tool | Purpose |
|------|---------|
| [TorchDistributor](/concepts/torchdistributor.md) | Launch PyTorch training jobs as Spark jobs on a cluster |
| [DeepSpeed](/concepts/deepspeed.md) | Advanced memory optimization and sharding for very large models |
| Ray | Distributed batch data processing and training (Ray Data) |
| [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) | Model sharding for PyTorch models from 20B to 120B+ parameters |
| [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) | Simple data parallelism for models that fit in a single GPU |
| [Optuna](/concepts/optuna.md) | Adaptive hyperparameter tuning across distributed trials |

## TorchDistributor

TorchDistributor is an open-source module in PySpark that facilitates distributed training with PyTorch on Spark clusters. It allows you to launch PyTorch training jobs as Spark jobs, leveraging the cluster’s resources without manual orchestration. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **When to use**: For PyTorch models that need to scale across multiple GPUs and nodes using standard data parallelism or custom distributed strategies.
- **Integration**: Works with PySpark and can be combined with [Delta Lake](/concepts/delta-lake.md) for data loading.

## DeepSpeed

DeepSpeed is a deep learning optimization library developed by Microsoft that provides memory efficiency and training speed improvements. On Databricks, DeepSpeed is available as a pre-installed library in Databricks Runtime ML and is recommended for models that require advanced memory optimization features beyond what FSDP offers out-of-the-box. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md] ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

- **Key features**: ZeRO optimization stages, offloading to CPU/NVMe, mixed precision training.
- **When to use**: For very large models (e.g., 100B+ parameters) where FSDP may not provide sufficient memory savings, or when specific DeepSpeed features (like custom gradient partitioning) are needed.

## Ray

Ray provides distributed batch data processing capabilities (Ray Data) that can be used for streaming large datasets during training or inference. On Databricks, Ray is included in Databricks Runtime ML. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **Use case**: Efficiently load and preprocess datasets that do not fit in memory, especially for [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming or custom data pipelines.

## Fully Sharded Data Parallel (FSDP)

[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is a PyTorch native technique that shards model parameters, gradients, and optimizer states across GPUs. On Databricks, FSDP is the recommended approach for training models in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

- **Benefit**: Reduces per-GPU memory footprint, enabling training of models that would otherwise exceed GPU memory.
- **Comparison with DDP**: Standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is simpler for models that fit in a single GPU, but FSDP becomes necessary when models do not fit. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Comparison with DeepSpeed**: FSDP offers a good balance of memory efficiency and ease of use; DeepSpeed is considered when more advanced optimization features are required. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Distributed Data Parallel (DDP)

DDP is PyTorch’s built-in data parallelism. It is well-suited for models that can fit in a single GPU’s memory and is simpler to set up than FSDP or DeepSpeed. On Databricks, DDP can be used via TorchDistributor or directly with `torch.distributed`. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

- **Limitation**: DDP does not reduce the memory footprint of the model itself, so it is not suitable for models that exceed single-GPU memory.

## Optuna

Optuna is an adaptive hyperparameter tuning framework that can parallelize training across a cluster. Databricks Runtime ML includes Optuna for automated hyperparameter search. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **Usage**: Combine with early stopping and batch size tuning to optimize training performance.
- **Integration**: Optuna can leverage the cluster’s distributed resources to run multiple hyperparameter trials concurrently.

## Best Practices for Distributed Training on Databricks

- **Start with a Single Node cluster** for fast iteration, then move to multi-GPU or multi-node when data or model size demands it. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Use GPU scheduling** to maximize utilization—configure the cluster to gang-schedule GPUs for distributed workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Monitor training** with [TensorBoard](/concepts/tensorboard-on-databricks.md) (pre-installed) and cluster metrics to identify bottlenecks like network I/O. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Optimize data loading** via Delta Lake tables for efficient I/O, and use streaming APIs (PyTorch IterableDataset, Hugging Face streaming, or Ray Data) for very large datasets that do not fit in memory. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- GPU Scheduling
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [MLflow Autologging](/concepts/mlflow-autologging.md)
- [Cluster Policies for Deep Learning](/concepts/notebook-scoped-libraries-and-cluster-policies-for-deep-learning.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- Early Stopping
- Batch Size Tuning
- [Transfer Learning](/concepts/transfer-learning.md)

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
