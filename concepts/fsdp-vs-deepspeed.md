---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3807948b4c099948f6b8d745e3e8659950a302dc546a68d7a8fb9b98e23f497a
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fsdp-vs-deepspeed
    - FVD
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: FSDP vs DeepSpeed
description: Comparison between FSDP and DeepSpeed, where DeepSpeed offers advanced memory optimization features as an alternative to FSDP for large model training.
tags:
  - distributed-training
  - comparison
  - deep-learning
timestamp: "2026-06-19T10:40:42.010Z"
---

# FSDP vs DeepSpeed

**FSDP (Fully Sharded Data Parallel)** and **DeepSpeed** are two distributed training frameworks that reduce the memory footprint of large models across multiple GPUs. While both enable training of models that exceed single‑GPU memory, they target different optimization levels and complexity.

## Overview

[FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) is a native PyTorch technique that shards model parameters, gradients, and optimizer states across GPUs. It is the recommended choice for training models in the **20B to 120B+ parameter range** on Databricks. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

[DeepSpeed](/concepts/deepspeed.md) is a more advanced framework developed by Microsoft that provides additional memory optimization features beyond what FSDP offers out of the box. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to Use FSDP

FSDP should be used when:

- Your model is too large to fit in a single GPU’s memory.
- You need to train models in the 20B to 120B+ parameter range.
- You want more memory efficiency than standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) provides.

For smaller models that fit in a single GPU, DDP is simpler and preferred. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to Use DeepSpeed

DeepSpeed should be considered when you require even more advanced memory optimization than FSDP. The FSDP documentation directs users to DeepSpeed for these scenarios, indicating that DeepSpeed offers strategies (such as ZeRO stages, offloading, etc.) that go beyond FSDP’s default capabilities. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] (The second citation is from the 20B page which repeats the same concept.)

## Key Differences

| Aspect | FSDP | DeepSpeed |
|--------|------|-----------|
| **Memory optimization** | Shards parameters, gradients, and optimizer states across GPUs. | Provides advanced optimization features (e.g., ZeRO stages, CPU offloading, activation checkpointing). |
| **Complexity** | Simpler to use, especially for PyTorch workflows. | More complex; intended for specialized memory optimization beyond FSDP. |
| **Recommended model scale** | 20B to 120B+ parameters. | For models that require even more aggressive memory reduction. |
| **When to switch** | Starting point for large models. | Consider when FSDP’s memory savings are insufficient. |

These distinctions come from the FSDP documentation’s recommendation to “see DeepSpeed” for advanced memory optimization. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Simpler alternative for models that fit on a single GPU.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The model scale where FSDP excels.
- ZeRO – The core memory optimization technique behind DeepSpeed.
- GPU Memory Optimization – General strategies for large‑model training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Detailed page on FSDP.

## Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
