---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e18065dac29b3027dacb0996846bfd35d92c7e6e4d33266dc1d03d3a4da6813
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-distributed-training
    - ARDT
    - ai-runtime-distributed-training-api
    - ARDTA
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Distributed Training
description: A Beta API for multi-GPU training on AI Runtime using the @distributed decorator from the serverless_gpu Python package, supporting PyTorch DDP, FSDP, and DeepSpeed with minimal configuration on a single multi-GPU node.
tags:
  - databricks
  - distributed-training
  - deep-learning
  - api
timestamp: "2026-06-19T22:03:47.201Z"
---

# AI Runtime Distributed Training

**AI Runtime Distributed Training** is a capability within Databricks AI Runtime that enables training deep learning models across multiple GPUs on a single node using a simplified API. It is designed to support popular distributed training frameworks with minimal configuration overhead. ^[ai-runtime-databricks-on-aws.md]

## Overview

AI Runtime supports distributed training across multiple GPUs on the single node that a notebook is connected to. Using the `@distributed` decorator from the `serverless_gpu` Python API, users can launch multi-GPU workloads with [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), or [DeepSpeed](/concepts/deepspeed.md) with minimal configuration. ^[ai-runtime-databricks-on-aws.md]

The distributed training API for multi-GPU workloads is currently in **Beta**. ^[ai-runtime-databricks-on-aws.md]

## Key Features

- **Simplified API**: The `@distributed` decorator abstracts away much of the complexity of setting up distributed training, allowing users to focus on model logic rather than infrastructure. ^[ai-runtime-databricks-on-aws.md]
- **Framework Support**: Compatible with PyTorch DDP, FSDP, and DeepSpeed, giving users flexibility in choosing the right parallelism strategy for their workload. ^[ai-runtime-databricks-on-aws.md]
- **Single-Node Multi-GPU**: All AI Runtime accelerators provision a single node, with the number of GPUs depending on the accelerator type (A10 or H100). ^[ai-runtime-databricks-on-aws.md]
- **Fully Managed Infrastructure**: No cluster configuration, driver selection, or autoscaling policies to manage. ^[ai-runtime-databricks-on-aws.md]

## Hardware Options

AI Runtime supports A10 and H100 accelerators. The number of GPUs available on a single node depends on the accelerator type selected. For detailed hardware specifications, see [AI Runtime Hardware Options](/concepts/ai-runtime-hardware-options.md). ^[ai-runtime-databricks-on-aws.md]

## Using the `@distributed` Decorator

The `serverless_gpu` Python library provides the `@distributed` decorator for running functions across multiple GPUs on a single node. The `runtime` module provides access to local and global GPU ranks for coordinating work. ^[ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(
    gpus=8,
    gpu_type='h100',
)
def train_model(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('Training started:', name)
    return rt.get_global_rank()

result = train_model.distributed('my_model')
```

- `gpus` specifies the number of processes to launch, typically one per GPU.
- `rt.get_local_rank()` returns the rank of the GPU within the node.
- `rt.get_global_rank()` returns the global rank across all processes.

## Supported Frameworks

### PyTorch Distributed Data Parallel (DDP)

DDP is suitable for models that fit within a single GPU's memory. It replicates the model across all GPUs and synchronizes gradients during backpropagation. ^[ai-runtime-databricks-on-aws.md]

### Fully Sharded Data Parallel (FSDP)

FSDP shards model parameters, gradients, and optimizer states across GPUs, enabling training of larger models that would not fit in a single GPU's memory. It is particularly useful for models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range. ^[ai-runtime-databricks-on-aws.md]

### DeepSpeed

DeepSpeed provides additional memory optimization features beyond FSDP, including ZeRO optimization stages and offloading to CPU or NVMe. ^[ai-runtime-databricks-on-aws.md]

## Use Cases

AI Runtime Distributed Training is recommended for any custom model training use cases that involve deep learning and require multiple GPUs. Common use cases include:

- Large Language Model (LLM) fine-tuning (LoRA, QLoRA, full fine-tuning)
- Computer vision (object detection, image classification)
- Deep-learning-based recommender systems
- Reinforcement learning
- Deep-learning-based time series forecasting

^[ai-runtime-databricks-on-aws.md]

## Limitations

- AI Runtime only supports A10 and H100 accelerators. ^[ai-runtime-databricks-on-aws.md]
- The distributed training API for multi-GPU workloads is in Beta. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days. For model training jobs that exceed this limit, implement checkpointing and restart the job once the maximum runtime is reached. ^[ai-runtime-databricks-on-aws.md]
- AI Runtime is not supported for compliance security profile workspaces (like HIPAA or PCI). ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The compute offering for deep learning workloads on Databricks Serverless
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The infrastructure that provisions GPU resources on demand
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — A specific hardware configuration for distributed training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — A parallelism strategy for multi-GPU training
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — A memory-efficient parallelism strategy
- [DeepSpeed](/concepts/deepspeed.md) — An optimization library for distributed training
- [Experiment Tracking and Observability](/concepts/ai-runtime-experiment-tracking-and-observability.md) — MLflow integration for tracking distributed training runs

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
