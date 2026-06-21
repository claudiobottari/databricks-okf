---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1678e21de608135becc9a3ad815295dd3c3b5d701c0c8ef38939f858f1ec2f71
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - decision-framework-ddp-vs-fsdp-vs-deepspeed
    - DFDVFVD
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: "Decision Framework: DDP vs FSDP vs DeepSpeed"
description: Guidelines for choosing between DDP (simpler use cases), FSDP (PyTorch-native large model training), and DeepSpeed (advanced memory optimization with ZeRO stages) on Databricks.
tags:
  - decision-guide
  - distributed-training
  - best-practices
timestamp: "2026-06-19T10:18:38.176Z"
---

Here is a wiki page about "Decision Framework: DDP vs FSDP vs DeepSpeed" based on the provided source material.

# Decision Framework: DDP vs FSDP vs DeepSpeed

**Decision Framework: DDP vs FSDP vs DeepSpeed** helps practitioners choose the right distributed training strategy for deep learning models. The selection depends on model size, memory requirements, and the need for advanced optimization features.

## Overview

Distributed training is required when a model is too large to fit into a single GPU's memory. Different frameworks offer different trade-offs between simplicity, memory efficiency, and advanced features. The three main approaches are [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), and [DeepSpeed](/concepts/deepspeed.md). ^[distributed-training-using-deepspeed-databricks-on-aws.md, fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to Use Each Framework

### DDP

DDP is the simplest approach for distributed training. Use DDP when your model fits entirely within a single GPU's memory. It distributes the training workload across multiple GPUs but does not provide any memory efficiency improvements for the model itself. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

- **Best for:** Models that fit in a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Key limitation:** No memory efficiency for model parameters. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### FSDP

FSDP shards model parameters, gradients, and optimizer states across multiple GPUs. Use FSDP when your model is too large to fit in a single GPU's memory. It is the standard choice for training models in the [20B to 120B+ parameter range](/concepts/20b-to-120b-parameter-model-training.md). FSDP offers a better trade-off for memory efficiency compared to DDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

- **Best for:** Overcoming single-GPU memory limitations for large models. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Key feature:** Shards all model states (parameters, gradients, optimizer states) across GPUs. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### DeepSpeed

DeepSpeed provides advanced memory optimization techniques beyond standard FSDP. Use DeepSpeed when you need fine-grained control over optimizer state sharding (ZeRO stages 1, 2, or 3), additional features like gradient accumulation fusion, or CPU offloading. It is particularly suitable for very large language models (1B to 100B+ parameters). ^[distributed-training-using-deepspeed-databricks-on-aws.md]

- **Best for:** Advanced memory optimization needs and large language models. ^[distributed-training-using-deepspeed-databricks-on-aws.md]
- **Key feature:** ZeRO stages for fine-grained control over memory reduction. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Decision Table

| Framework | When to Use | Key Trade-off |
|-----------|-------------|---------------|
| DDP | Model fits in single GPU memory | Simple, no memory efficiency |
| FSDP | 20B+ parameter models | Standard, good memory efficiency |
| DeepSpeed | 1B+ models needing advanced features | Most control, most advanced |

## Related Concepts

- [ZeRO (Zero Redundancy Optimizer)](/concepts/zero-zero-redundancy-optimizer.md) — The memory optimization technique behind DeepSpeed.
- GPU Memory Optimization — Techniques for fitting large models into limited GPU memory.
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md) — A technique for reducing memory usage during training.
- [CPU Offloading](/concepts/cpu-offloading.md) — Moving optimizer states to CPU to free GPU memory.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Basic distributed training approach.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Standard approach for large model training.

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
