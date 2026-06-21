---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b6c9bbf3ca6b0587f9b6c908c75529b95360e3740f49f9ca827d90d3b5d297c
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - zero-zero-redundancy-optimizer
    - Z(RO
    - ZeRO
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: ZeRO (Zero Redundancy Optimizer)
description: A memory optimization technique in DeepSpeed that shards optimizer states, gradients, and parameters across devices to enable training of large models
tags:
  - machine-learning
  - memory-optimization
  - distributed-training
timestamp: "2026-06-19T18:36:40.688Z"
---

# ZeRO (Zero Redundancy Optimizer)

**ZeRO (Zero Redundancy Optimizer)** is a memory optimization technique provided by the [DeepSpeed](/concepts/deepspeed.md) library that partitions model states across GPUs to reduce memory redundancy, enabling efficient training of large-scale deep learning models with billions of parameters. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Overview

DeepSpeed's ZeRO stages offer advanced memory optimization beyond standard [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). ZeRO provides fine-grained control over sharding of optimizer states in stages 1, 2, and 3, and supports additional features such as gradient accumulation fusion and CPU offloading. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

### ZeRO Stages

ZeRO optimizes memory by partitioning different model states across data-parallel processes:

- **ZeRO Stage 1**: Partitions optimizer states across data-parallel processes, reducing memory consumption by a factor equal to the data parallel degree while maintaining the same communication volume as traditional data parallelism.

- **ZeRO Stage 2**: Partitions both optimizer states and gradients across data-parallel processes, further reducing memory usage beyond Stage 1 with moderate increase in communication overhead.

- **ZeRO Stage 3**: Partitions optimizer states, gradients, and model parameters across data-parallel processes, achieving the greatest memory reduction at the cost of increased communication. This stage enables training of models that would not fit in a single GPU's memory. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

### Advanced Features

Beyond basic sharding, ZeRO supports:

- **Gradient accumulation fusion**: Combines gradient accumulation operations with communication to reduce overhead.
- **CPU offloading**: Moves optimizer states and gradients to CPU memory when GPU memory is insufficient, enabling training of even larger models.
- **Mixed precision training**: Integrates with automatic mixed precision to further reduce memory footprint. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## When to Use DeepSpeed with ZeRO

Use DeepSpeed (and its ZeRO stages) when:

- You need advanced memory optimization beyond standard FSDP.
- You want fine-grained control over optimizer state sharding (ZeRO Stage 1, 2, or 3).
- You need additional features like gradient accumulation fusion or CPU offloading.
- You are working with large language models (1B to 100B+ parameters). ^[distributed-training-using-deepspeed-databricks-on-aws.md]

For simpler use cases, consider [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). For PyTorch-native large model training, use [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Comparison with FSDP

While both ZeRO and FSDP share the concept of sharding model states, ZeRO provides more granular control through its distinct stages. FSDP is a PyTorch-native implementation that offers a simpler API but fewer configuration options. ZeRO's CPU offloading and gradient accumulation fusion features give it an edge for extremely large models that push against memory limits. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Memory Efficiency

For models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range, ZeRO's memory partitioning becomes critical. Without ZeRO, a 100B parameter model would require approximately 400 GB of GPU memory just for parameters in FP32 (plus gradients and optimizer states). With ZeRO Stage 3 and 64 GPUs, this memory is distributed such that each GPU holds roughly 6.25 GB of parameters, making training feasible. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Gradient Accumulation Fusion](/concepts/gradient-accumulation-fusion.md)
- [CPU Offloading](/concepts/cpu-offloading.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
