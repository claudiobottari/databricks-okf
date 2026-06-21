---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5fae3edcf9f4d11e188e035bf53596639318cc1e778e98985c580ce43a0a401
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - zero-stages-stage-1-2-3
    - ZS(123
    - ZeRO stages
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: ZeRO Stages (Stage 1, 2, 3)
description: Three stages of optimizer state sharding in DeepSpeed's ZeRO, providing increasing levels of memory savings by partitioning optimizer states, gradients, and model parameters respectively.
tags:
  - distributed-training
  - memory-optimization
  - deep-learning
timestamp: "2026-06-19T10:18:15.223Z"
---

# ZeRO Stages (Stage 1, 2, 3)

**ZeRO (Zero Redundancy Optimizer) Stages** are memory optimization techniques provided by [DeepSpeed](/concepts/deepspeed.md) that shard key training state across GPUs to enable training of large models that would otherwise exceed single‑GPU memory. The three stages incrementally reduce per‑GPU memory usage by partitioning different components of the training state: optimizer states, gradients, and model parameters.^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Overview

ZeRO stages are part of the DeepSpeed library, a distributed training framework that offers advanced memory optimization beyond standard [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). Each stage represents a different level of sharding, with Stage 1 being the least aggressive and Stage 3 the most memory‑efficient, at the cost of increased communication overhead.^[distributed-training-using-deepspeed-databricks-on-aws.md]

| ZeRO Stage | What is Sharded | Description |
|------------|-----------------|-------------|
| **Stage 1** | Optimizer states | Partitions optimizer states (e.g., Adam momentum and variance) across GPUs. Gradients and parameters remain replicated. |
| **Stage 2** | Optimizer states + gradients | Shards both optimizer states and gradients. Parameters remain replicated. |
| **Stage 3** | Optimizer states + gradients + parameters | Shards all three components. Parameters are gathered only when needed during forward/backward passes, minimizing per‑GPU memory to the maximum extent. |

^[distributed-training-using-deepspeed-databricks-on-aws.md]

> **Note:** ZeRO stages do **not** handle activation offloading, which is provided separately by DeepSpeed activation checkpointing. CPU offloading is an additional feature that can be combined with any ZeRO stage.^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Stage 1 – Optimizer State Partitioning

Stage 1 shards only the optimizer states (such as momentum and variance for optimizers like Adam) across the available GPUs. Gradients and model parameters remain fully replicated on each GPU. This stage is useful when the optimizer states are the primary memory bottleneck, which often occurs when using memory‑intensive optimizers with large models. Communication overhead is minimal because only the optimizer states are redistributed during the update step.^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Stage 2 – Gradient Partitioning

Stage 2 extends Stage 1 by also sharding the gradients across GPUs. After the backward pass, each GPU reduces only its own gradient shard, and gradients are communicated during the reduce‑scatter step. Parameters remain replicated. This stage reduces memory further than Stage 1 and is commonly used for models where gradient memory is a significant factor. The additional communication for gradient sharding increases overhead compared to Stage 1 but offers better memory savings.^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Stage 3 – Parameter Partitioning

Stage 3 shards all three components: optimizer states, gradients, and model parameters. During the forward and backward passes, the required parameter shards are gathered on‑demand from the owning GPUs. This stage provides the maximum possible memory reduction, making it possible to train very large models (e.g., 1B to 100B+ parameters) that would not fit even a single copy of the parameters on any one GPU. The trade‑off is increased communication overhead because parameters must be all‑gathered before each forward/backward step.^[distributed-training-using-deepspeed-databricks-on-aws.md]

## When to Use Each Stage

- **Stage 1:** Choose when optimizer states dominate memory and you need minimal communication overhead.
- **Stage 2:** Suitable for moderate‑sized models where both optimizer states and gradients are memory‑hungry, but parameters still fit on a single GPU.
- **Stage 3:** Best for very large models (1B to 100B+ parameters) where even the parameters cannot be stored on one GPU. The memory savings come at the cost of higher communication.

For simpler use cases where models fit on a single GPU, standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is often sufficient. For PyTorch‑native large model training, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) provides an alternative with similar sharding strategies. DeepSpeed’s ZeRO stages offer fine‑grained control and additional features like gradient accumulation fusion and CPU offloading.^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Comparison with Other Strategies

| Strategy | Memory Efficiency | Communication Overhead | Best Use Case |
|----------|------------------|------------------------|---------------|
| DDP | Low (no sharding) | Low | Models that fit on one GPU |
| FSDP | Medium to High (shards all three) | Medium to High | PyTorch‑native large model training |
| DeepSpeed ZeRO (any stage) | Adjustable (Stage 1 to 3) | Adjustable (Stage 1 lowest, Stage 3 highest) | Advanced memory optimization with fine‑grained control |

^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) – The library that implements ZeRO stages
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – PyTorch’s alternative for sharded training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Basic data parallelism without sharding
- [CPU Offloading](/concepts/cpu-offloading.md) – Additional DeepSpeed feature to offload states to CPU memory
- [Gradient Accumulation Fusion](/concepts/gradient-accumulation-fusion.md) – A DeepSpeed optimization complementary to ZeRO

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
