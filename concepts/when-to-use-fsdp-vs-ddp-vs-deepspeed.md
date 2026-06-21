---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78dbdd1d6b95e401c13640e8b486808552311945981c3037af74a3c054200e71
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-to-use-fsdp-vs-ddp-vs-deepspeed
    - WTUFVDVD
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: When to use FSDP vs DDP vs DeepSpeed
description: Decision framework for choosing between FSDP, DDP, and DeepSpeed based on model size and memory efficiency needs
tags:
  - decision-framework
  - distributed-training
  - model-scaling
timestamp: "2026-06-18T12:26:50.462Z"
---

# When to use FSDP vs DDP vs DeepSpeed

Choosing the right distributed training strategy is critical for efficiently training large models on GPUs. **Fully Sharded Data Parallel (FSDP)**, **Distributed Data Parallel (DDP)**, and **DeepSpeed** are three popular approaches, each suited to different model sizes, memory constraints, and performance requirements.

## Overview

All three techniques enable training across multiple GPUs, but they differ in how they manage memory and communication:

- **DDP** replicates the entire model on each GPU and synchronizes gradients during backpropagation.
- **FSDP** shards model parameters, gradients, and optimizer states across GPUs, reducing per-GPU memory usage.
- **DeepSpeed** provides a suite of memory optimization features, including ZeRO stages, that go beyond FSDP's sharding capabilities.

## When to use DDP

Use **Distributed Data Parallel (DDP)** when:

- Your model fits entirely within a single GPU's memory.
- You prioritize simplicity and ease of implementation.
- You are training smaller models (typically under 1B parameters) where memory is not a bottleneck.

DDP is the simplest of the three approaches and requires minimal code changes. Each GPU holds a full copy of the model, and gradients are averaged across GPUs after each backward pass. For models that fit comfortably in GPU memory, DDP offers excellent performance with low overhead. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to use FSDP

Use **Fully Sharded Data Parallel (FSDP)** when:

- Your model is too large to fit in a single GPU's memory.
- You need to train models in the 20B to 120B+ parameter range.
- You want more memory efficiency than DDP provides.

FSDP shards model parameters, gradients, and optimizer states across GPUs, enabling training of very large models that would otherwise be impossible on available hardware. It provides a good balance between memory savings and training speed, making it the preferred choice for large-scale training where DeepSpeed's advanced features are not required. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to use DeepSpeed

Use **DeepSpeed** when:

- You need advanced memory optimization features beyond basic sharding, such as ZeRO stages (1, 2, and 3), offloading to CPU or NVMe, and mixed precision training optimizations.
- You require fine-grained control over memory and communication trade-offs.
- You are working with extremely large models (100B+ parameters) where FSDP's memory savings are insufficient.

DeepSpeed offers a richer set of optimization techniques than FSDP, including ZeRO-Infinity for offloading parameters to CPU or disk, and pipeline parallelism for distributing model layers across GPUs. It is particularly well-suited for pushing the boundaries of model scale on limited hardware. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Comparison Table

| Criterion | DDP | FSDP | DeepSpeed |
|-----------|-----|------|-----------|
| Model fits in single GPU | ✅ Best choice | ❌ Overkill | ❌ Overkill |
| Model 1B–20B parameters | ❌ May not fit | ✅ Good fit | ✅ Good fit |
| Model 20B–120B+ parameters | ❌ Won't fit | ✅ Good fit | ✅ Best choice |
| Memory efficiency | Low | High | Very high |
| Implementation complexity | Low | Medium | High |
| Advanced features (offloading, ZeRO stages) | ❌ | Limited | ✅ Full suite |

## Choosing the Right Strategy

1. **Start with DDP** if your model fits in a single GPU. It is the simplest and most performant option for small to medium models.
2. **Move to FSDP** when your model exceeds single-GPU memory. FSDP provides significant memory savings with reasonable complexity.
3. **Adopt DeepSpeed** when you need the most advanced memory optimizations, especially for extremely large models or when training on constrained hardware.

For smaller models that fit in single GPU memory, consider DDP for simplicity. For advanced memory optimization features, see DeepSpeed. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The simplest distributed training strategy
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient sharding for large models
- [DeepSpeed](/concepts/deepspeed.md) — Advanced memory optimization suite
- [ZeRO Optimization](/concepts/deepspeed-zero-stage-3-optimization.md) — The memory optimization stages underlying DeepSpeed
- GPU Memory Management — Techniques for fitting large models into GPU memory
- Model Parallelism — Alternative approach for distributing model layers across GPUs

## Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
