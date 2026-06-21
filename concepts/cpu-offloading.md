---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a5e03d69573319d52436824b7205096b378d5680ab0911c7f7ede7e1db57194
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cpu-offloading
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: CPU Offloading
description: A memory optimization technique in DeepSpeed that offloads optimizer states or parameters from GPU memory to CPU memory to reduce GPU memory pressure
tags:
  - machine-learning
  - memory-optimization
  - deep-speed
timestamp: "2026-06-19T18:36:21.625Z"
---

# CPU Offloading

**CPU Offloading** is a memory optimization technique used in distributed deep learning training where selected data—such as model parameters, gradients, or optimizer states—is moved from GPU memory to CPU memory. By reducing the per‑GPU memory footprint, CPU offloading enables training of models that would otherwise exceed the capacity of the available GPUs.

## Context and Usage

CPU offloading is one of the advanced memory‑saving features provided by [DeepSpeed](/concepts/deepspeed.md) through its ZeRO (Zero Redundancy Optimizer) stages, particularly **ZeRO‑3**. It is typically used in conjunction with other optimizations such as gradient accumulation fusion to train large language models (1B to 100B+ parameters) in multi‑GPU or multi‑node environments. The technique trades higher CPU‑GPU communication overhead for significantly lower GPU memory consumption, making it practical to scale model size without upgrading hardware. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

CPU offloading is not limited to DeepSpeed; similar capabilities exist in [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) through the `cpu_offload` parameter, though the source material specifically highlights DeepSpeed as the recommended tool when this feature is required.

## How It Works

During training, the optimizer and gradient states (and optionally the model parameters) are stored in CPU memory instead of GPU memory. When a layer needs to be processed, its parameters are fetched from the CPU to the GPU just‑in‑time for the forward and backward passes, and then evicted back to CPU. This process is transparent to the user and managed by the training framework.

## When to Use CPU Offloading

CPU offloading is most beneficial when:

- The model size is too large to fit into GPU memory even after sharding with ZeRO‑2 or FSDP.
- GPU memory is a bottleneck and the training cluster has sufficient CPU RAM and high‑bandwidth CPU‑GPU interconnect (e.g., NVLink, PCIe Gen4/5).
- The training workload can tolerate the additional latency introduced by CPU‑GPU transfers.

For models that fit comfortably in GPU memory with standard sharding, CPU offloading may add unnecessary overhead and should be avoided.

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) – The framework that provides CPU offloading as part of ZeRO‑3.
- ZeRO Optimizer – The three‑stage sharding strategy; CPU offloading is a common complement to ZeRO‑3.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – An alternative sharding approach that also supports CPU offloading.
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md) – Another memory‑saving technique often combined with CPU offloading.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – A simpler parallelism strategy that does not natively support CPU offloading.

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
