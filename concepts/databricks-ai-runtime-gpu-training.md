---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14312ce2226cba10ea0e75e9fa959de29c32aa0a85d950cf6bc55d2cf4a3f277
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-gpu-training
    - DARGT
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
    - file: a100-gpu-support-on-databricks.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: 20b-to-120b-parameter-model-training.md
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: Databricks AI Runtime GPU training
description: Databricks' managed environment supporting distributed GPU training with DDP, PyTorch Lightning, and serverless GPU resources.
tags:
  - databricks
  - gpu
  - distributed-training
  - cloud
timestamp: "2026-06-19T18:32:25.320Z"
---

Here is the wiki page for "Databricks AI Runtime GPU Training", written based solely on the provided source material.

---

## Databricks AI Runtime GPU Training

**Databricks AI Runtime GPU Training** refers to the set of tools, runtimes, and best practices for running deep learning and large language model (LLM) training workloads on GPU clusters within the Databricks platform. The runtime provides pre-configured environments and supports multiple distributed training strategies to accommodate models ranging from those that fit on a single GPU to models with over 100 billion parameters.

### Overview

Databricks AI Runtime includes GPU-accelerated runtimes that bundle popular deep learning frameworks and libraries, enabling users to train models without manually managing infrastructure. The platform supports various NVIDIA GPU types, including A100 and H100 GPUs, across major cloud providers. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md, a100-gpu-support-on-databricks.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Supported Distributed Training Strategies

Databricks supports three primary distributed training strategies, each suited to different model sizes and memory requirements.

#### Distributed Data Parallel (DDP)
DDP is the most common parallelism technique for distributed training, where the full model is replicated on each GPU and data batches are split across GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md] Use DDP when:
- Your model fits completely in a single GPU's memory
- You want to scale training by increasing data throughput
- You need the simplest distributed training approach with automatic support in most frameworks

^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

For larger models that don't fit in single GPU memory, consider FSDP or DeepSpeed instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

#### Fully Sharded Data Parallel (FSDP)
FSDP shards model parameters, gradients, and optimizer states across multiple GPUs, significantly reducing the per-GPU memory footprint. It is the recommended approach for training models in the **20 billion to 120+ billion parameter range**. FSDP offers a better trade-off for memory efficiency compared to DDP for models that do not fit on a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md, 20b-to-120b-parameter-model-training.md]

#### DeepSpeed
DeepSpeed provides advanced memory optimization techniques through its ZeRO (Zero Redundancy Optimizer) stages. Use DeepSpeed when you need:
- Advanced memory optimization beyond standard FSDP
- Fine-grained control over optimizer state sharding
- Additional features like gradient accumulation fusion or CPU offloading
- Support for large language models ranging from 1 billion to over 100 billion parameters

^[distributed-training-using-deepspeed-databricks-on-aws.md]

### GPU Instance Support

Databricks supports a wide range of GPU instance types. A100 GPUs are supported on all clouds and are recommended for deep learning tasks such as training and tuning LLMs, natural language processing, and recommendation engines. H100 GPUs offer larger FLOPS and HBM compared to A10 GPUs, making them suitable for large model training. ^[a100-gpu-support-on-databricks.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Strategy Selection Guide

| Strategy | Model Size | Complexity | Key Feature |
|----------|-----------|------------|-------------|
| DDP | Fits in single GPU | Low | Simple replication and gradient sync |
| FSDP | 20B to 120B+ parameters | Medium | Shards all states across GPUs |
| DeepSpeed | 1B to 100B+ parameters | High | ZeRO stages, CPU offloading, memory optimization |

^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md, distributed-training-using-deepspeed-databricks-on-aws.md, distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- H100 GPU Support on Databricks
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- distributed-training-using-deepspeed-databricks-on-aws.md
- a100-gpu-support-on-databricks.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- 20b-to-120b-parameter-model-training.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
2. a100-gpu-support-on-databricks.md
3. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
4. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
5. 20b-to-120b-parameter-model-training.md
6. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
