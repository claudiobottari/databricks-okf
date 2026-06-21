---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 232ef9c6e6fb881b1cccd59d19d435d673d33f22b5b206d13610ba258ef3feb1
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - deepspeed
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: DeepSpeed
description: A deep learning optimization library by Microsoft that provides advanced memory optimization techniques for distributed training of large models
tags:
  - machine-learning
  - distributed-training
  - optimization
timestamp: "2026-06-19T18:36:14.022Z"
---

# DeepSpeed

**DeepSpeed** is a deep learning optimization library developed by Microsoft that provides advanced memory optimization techniques through its ZeRO (Zero Redundancy Optimizer) stages, enabling efficient training of large models. DeepSpeed is available on [AI Runtime](/concepts/ai-runtime.md) for distributed training workloads. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Key Features

DeepSpeed offers fine-grained control over optimizer state sharding through three ZeRO stages (Stage 1, 2, and 3). It also provides additional capabilities such as gradient accumulation fusion and CPU offloading, which help reduce memory usage and improve training throughput for large-scale deep learning workloads. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## When to Use DeepSpeed

Use DeepSpeed when you need advanced memory optimization beyond standard [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) (Fully Sharded Data Parallel), want fine-grained control over optimizer state sharding (ZeRO Stage 1, 2, or 3), require additional features like gradient accumulation fusion or CPU offloading, or are working with [Large Language Models](/concepts/large-language-models-llms-on-databricks.md) ranging from 1 billion to 100+ billion parameters. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

For simpler use cases, consider [DDP](/concepts/distributed-data-parallel-ddp.md) (Distributed Data Parallel). For PyTorch-native large model training, see [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md). ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Examples

Notebook examples for distributed training using DeepSpeed on AI Runtime are available in the Databricks documentation, demonstrating how to set up and run training workloads with DeepSpeed's memory optimization techniques. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Related Concepts

- ZeRO Optimizer — The Zero Redundancy Optimizer that forms the core of DeepSpeed’s memory optimization.
- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) — PyTorch-native fully sharded data parallel training as an alternative to DeepSpeed.
- [DDP](/concepts/distributed-data-parallel-ddp.md) — Distributed Data Parallel for simpler distributed training use cases.
- [AI Runtime](/concepts/ai-runtime.md) — The Databricks environment that supports DeepSpeed training.
- [Large Language Models](/concepts/large-language-models-llms-on-databricks.md) — Common workload type that benefits from DeepSpeed’s optimizations.

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
