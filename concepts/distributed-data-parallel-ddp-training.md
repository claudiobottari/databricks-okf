---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ecd4f584f111cd56414db7d2a4a3d79a8a027500094d490280197f40959eb078
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-data-parallel-ddp-training
    - DDP(T
    - DDP
    - Distributed Data-Parallel Training
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Distributed Data Parallel (DDP) Training
description: A parallelism technique for distributed training where the full model is replicated on each GPU and data batches are split across GPUs
tags:
  - distributed-training
  - pytorch
  - parallelism
timestamp: "2026-06-19T15:12:30.245Z"
---

# Distributed Data Parallel (DDP) Training

**Distributed Data Parallel (DDP) Training** is the most common parallelism technique for distributed training, where the full model is replicated on each GPU and data batches are split across GPUs. DDP is built into PyTorch's `torch.nn.parallel` module and provides automatic support across most deep learning frameworks. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Overview

DDP works by maintaining identical copies of the model on each GPU. During training, each GPU processes a different subset of the training data (a mini-batch), computes gradients independently, and then synchronizes gradients across all GPUs before updating the model parameters. This approach scales training by increasing data throughput rather than reducing memory per GPU. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use DDP

Use DDP when:

- Your model fits completely in a single GPU's memory
- You want to scale training by increasing data throughput
- You need the simplest distributed training approach with automatic support in most frameworks

^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

For larger models that do not fit in single GPU memory, consider [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Comparison with Other Techniques

- **DDP vs. [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)**: DDP replicates the entire model on each GPU, while FSDP shards model parameters, gradients, and optimizer states across GPUs. DDP is simpler and more performant for models that fit on a single GPU; FSDP is necessary for models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md, fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **DDP vs. [DeepSpeed](/concepts/deepspeed.md)**: DeepSpeed provides additional memory optimization strategies beyond DDP, such as ZeRO optimization stages, making it suitable for models that require more advanced memory management. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Hardware Considerations

DDP training benefits from multi-GPU configurations such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md), which provides eight NVIDIA H100 GPUs on a single node. The `@distributed` decorator from Databricks' `serverless_gpu` library can coordinate DDP-style parallelism across multiple GPUs on a single node. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

[A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) is also available across all cloud providers for DDP training workloads, though capacity may be limited and advance reservation is recommended. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Example Use Cases

- Training a simple multilayer perceptron (MLP) neural network using PyTorch's DDP module on serverless GPU resources
- Training a two-tower recommender system using PyTorch Lightning, which provides a high-level interface that automatically handles DDP configuration for multi-GPU training

These examples demonstrate DDP training on Databricks using A10 or H100 GPUs with data preparation via Mosaic Streaming (MDS) format. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
4. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
