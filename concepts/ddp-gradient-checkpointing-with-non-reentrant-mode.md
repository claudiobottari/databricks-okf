---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f25273c0f61866351404971d7342812926e768b90ec475ad2410e4101640d4bf
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ddp-gradient-checkpointing-with-non-reentrant-mode
    - DGCWNM
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: DDP gradient checkpointing with non-reentrant mode
description: A distributed training fix required when combining PyTorch DDP with gradient checkpointing to avoid 'mark a variable ready only once' errors.
tags:
  - distributed-training
  - pytorch
  - debugging
timestamp: "2026-06-19T10:16:06.545Z"
---

# DDP Gradient Checkpointing with Non-Reentrant Mode

**DDP gradient checkpointing with non-reentrant mode** is a required configuration when using gradient checkpointing (also known as activation checkpointing) together with [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training. This setting prevents a common error where DDP attempts to mark a variable as "ready" multiple times during the backward pass.

## Overview

When training large models with [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), gradient checkpointing is often used to reduce memory consumption by trading compute for memory — intermediate activations are recomputed during the backward pass rather than stored. However, the default reentrant mode of gradient checkpointing can cause conflicts with DDP's gradient synchronization mechanism. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## The Problem: Reentrant Checkpointing with DDP

In reentrant mode, the checkpointed function can be called multiple times during the backward pass, which can lead to DDP seeing the same gradient computation graph multiple times. This causes DDP to attempt to mark a variable as "ready" more than once, resulting in the error: "mark a variable ready only once." ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## The Solution: Non-Reentrant Mode

Setting `use_reentrant=False` in the gradient checkpointing configuration ensures that each checkpointed segment is computed exactly once during the backward pass, avoiding the multiple-ready-marking issue with DDP. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Implementation

The non-reentrant mode is enabled by passing the `gradient_checkpointing_kwargs` parameter when calling `gradient_checkpointing_enable()`:

```python
model.gradient_checkpointing_enable(
    gradient_checkpointing_kwargs={"use_reentrant": False}
)
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## When to Use

This configuration is specifically required when:

- Training with [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- Using gradient checkpointing to reduce memory usage
- The model's forward pass contains operations that would otherwise be re-entered during the backward pass

It is commonly used in distributed fine-tuning workflows, such as when using [Unsloth](/concepts/unsloth.md) with LoRA adapters across multiple GPUs. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Gradient Checkpointing](/concepts/activation-checkpointing.md) — The general technique of trading compute for memory by recomputing activations
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — PyTorch's distributed training paradigm
- [Unsloth](/concepts/unsloth.md) — An optimized library for fine-tuning LLMs
- LoRA — Low-Rank Adaptation for parameter-efficient fine-tuning
- [Activation Checkpointing](/concepts/activation-checkpointing.md) — Alternative name for gradient checkpointing

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
