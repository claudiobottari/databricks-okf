---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 489a825898c487731185c93b977e59cb23fc2d00e1da26847a538e8244971ef8
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-zero-stage-1
    - DZS1
    - ZeRO Stage 1
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: DeepSpeed ZeRO Stage 1
description: ZeRO stage that shards optimizer states across GPUs, reducing memory consumption while gradients and model parameters remain fully replicated.
tags:
  - distributed-training
  - memory-optimization
  - deep-learning
timestamp: "2026-06-18T12:07:09.489Z"
---

# DeepSpeed ZeRO Stage 1

**DeepSpeed ZeRO Stage 1** is the first of three stages in DeepSpeed's ZeRO (Zero Redundancy Optimizer) memory optimization framework, designed to reduce the memory footprint of large-model training by sharding optimizer states across GPUs. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Overview

ZeRO Stage 1 partitions optimizer states (such as momentum and variance for Adam) among the available GPUs in a distributed training group. Each GPU maintains only its own shard of the optimizer states, eliminating redundant copies and reducing per-device memory consumption. This enables training larger models than would fit in a single GPU's memory, without changing the underlying model code. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

Stage 1 is the least aggressive of the three ZeRO stages. It does not shard gradients (Stage 2) or model parameters (Stage 3), making it suitable for scenarios where optimizer states are the primary memory bottleneck. It provides a simple upgrade path from standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) or [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) training. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Relation to Other ZeRO Stages

DeepSpeed offers three ZeRO stages that trade off communication overhead for memory savings: ^[distributed-training-using-deepspeed-databricks-on-aws.md]

| Stage | Memory components sharded | Communication overhead |
|-------|--------------------------|------------------------|
| **Stage 1** | Optimizer states | Low |
| Stage 2 | Optimizer states + gradients | Moderate |
| Stage 3 | Optimizer states + gradients + model parameters | High |

Stage 1 provides the smallest memory savings but also the lowest communication cost. Users who need finer-grained control over how memory is optimized can select Stage 1, 2, or 3 based on model size and available cluster resources. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## When to Use ZeRO Stage 1

Use ZeRO Stage 1 when you require advanced memory optimization beyond what standard [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) provides, and you want to start with the simplest ZeRO configuration. It is particularly effective for large language models in the 1 billion to 100 billion+ parameter range where optimizer states alone consume significant memory. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

For simpler training scenarios, [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) may suffice. For greater memory savings that trade higher communication overhead, consider ZeRO Stage 2 or Stage 3. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) — The optimization library providing ZeRO stages
- [ZeRO Optimization](/concepts/deepspeed-zero-stage-3-optimization.md) — The general memory optimization technique
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — An alternative sharding approach in PyTorch
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Simpler parallel training strategy
- [Gradient Accumulation Fusion](/concepts/gradient-accumulation-fusion.md) — A feature enabled by DeepSpeed that further reduces memory

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
