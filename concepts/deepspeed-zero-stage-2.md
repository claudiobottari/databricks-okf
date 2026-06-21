---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95c5c338bfd7914557871fb6eaf63bb5a222f229e695f9a9d048e3f3f48ab409
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-zero-stage-2
    - DZS2
    - deepspeed-zero-stage-1
    - DZS1
    - ZeRO Stage 1
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: DeepSpeed ZeRO Stage 2
description: ZeRO stage that shards both optimizer states and gradients across GPUs, further reducing memory compared to Stage 1.
tags:
  - distributed-training
  - memory-optimization
  - deep-learning
timestamp: "2026-06-18T12:06:54.734Z"
---

# DeepSpeed ZeRO Stage 2

**DeepSpeed ZeRO Stage 2** (also known as the **Zero Redundancy Optimizer Stage 2**) is an advanced memory optimization technique that partitions both optimizer states and gradients across distributed training processes, eliminating data redundancy and enabling efficient training of large-scale machine learning models. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Overview

DeepSpeed's ZeRO (Zero Redundancy Optimizer) framework provides three stages of memory optimization for distributed training of [large language models](/concepts/large-language-models-llms-on-databricks.md). ZeRO Stage 2 builds upon Stage 1 by sharding not only the optimizer states but also the gradients across all participating processes, reducing per-device memory consumption beyond what Stage 1 achieves alone. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## How ZeRO Stage 2 Works

During training, each process in a distributed setup independently computes its portion of the model's gradients through backpropagation. In ZeRO Stage 2, these gradients are partitioned across processes rather than being fully replicated on every device. Each process retains only the gradient shard it needs to update its corresponding optimizer state partition. This distribution enables each device to handle larger model partitions than would fit in its memory under [ZeRO Stage 1](/concepts/deepspeed-zero-stage-2.md). ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Technical Details

### Memory Savings

ZeRO Stage 2 reduces redundant storage of gradients across processes. In a standard [data parallel](/concepts/data-parallelism-spark.md) setup with N processes, gradients are typically replicated N times. With Stage 2, each gradient is stored exactly once across the distributed group, reducing gradient memory by a factor of N compared to [DDP (Distributed Data Parallel)](/concepts/distributed-data-parallel-ddp.md). When combined with optimizer state sharding from Stage 1, the total memory savings compound: the optimizer states are sharded N ways, and the gradients are sharded N ways, while the model parameters remain replicated. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

### Comparison with ZeRO Stages

| Stage | Optimizer States | Gradients | Model Parameters |
|-------|-----------------|-----------|-----------------|
| [ZeRO Stage 1](/concepts/deepspeed-zero-stage-2.md) | Partitioned | Replicated | Replicated |
| **ZeRO Stage 2** | Partitioned | Partitioned | Replicated |
| [ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md) | Partitioned | Partitioned | Partitioned |

^[distributed-training-using-deepspeed-databricks-on-aws.md]

### Communication Overhead

ZeRO Stage 2 introduces additional all-reduce or all-gather communication operations to collect partitioned gradients before they can be used for parameter updates, adding moderate communication overhead compared to Stage 1. However, this overhead is smaller than the full parameter gathering required by [ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md), making Stage 2 suitable for models where the optimizer and gradient memory are the primary bottlenecks but the model parameters still fit in aggregate device memory. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## When to Use ZeRO Stage 2

ZeRO Stage 2 is most effective when:

- The model's optimizer states and gradients exceed available per-device memory, but the model parameters themselves can still fit in aggregate device memory.
- The model is large enough that gradient replication across processes creates a significant memory burden.
- You need the additional memory headroom provided by gradient partitioning without the full parameter communication overhead of Stage 3.
- The training workload benefits from [Gradient Accumulation Fusion](/concepts/gradient-accumulation-fusion.md), which DeepSpeed can combine with Stage 2 for additional efficiency.

For smaller models, [DDP (Distributed Data Parallel)](/concepts/distributed-data-parallel-ddp.md) or [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) may provide sufficient memory without DeepSpeed's specialized optimizations. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) — The library providing ZeRO optimization stages
- [ZeRO Stage 1](/concepts/deepspeed-zero-stage-2.md) — Optimizer state partitioning, the foundation for Stage 2
- [ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md) — Full model parameter partitioning for extreme memory savings
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — The broader context of multi-device model training
- [Large Language Models](/concepts/large-language-models-llms-on-databricks.md) — Model architectures that benefit from ZeRO Stage 2
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md) — A technique that ZeRO Stage 2 can optimize through fusion
- [CPU Offloading](/concepts/cpu-offloading.md) — An additional DeepSpeed feature that can be combined with Stage 2

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
