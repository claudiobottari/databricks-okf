---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b1fa50280941392bfa88b05dfa58ebd774700dc982650c6d1234ec2bb2ce2c2
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-training-strategies-comparison
    - DTSC
    - Distributed Training Strategies
    - Distributed Computing Best Practices
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
    - file: distributed-training-using-ddp-databricks-on-aws.md
title: Distributed Training Strategies Comparison
description: A taxonomy of distributed training approaches including DDP (Data Distributed Parallel), FSDP (Fully Sharded Data Parallel), and DeepSpeed, each suited to different model sizes and use cases.
tags:
  - machine-learning
  - distributed-training
  - architecture
timestamp: "2026-06-18T15:33:11.592Z"
---

# Distributed Training Strategies Comparison

**Distributed Training Strategies Comparison** examines three primary approaches for training deep learning models across multiple GPUs: [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), and [DeepSpeed](/concepts/deepspeed.md). Each strategy offers different trade-offs in memory efficiency, complexity, and control, making them suitable for different model sizes and use cases.

## Overview

As model sizes grow, a single GPU’s memory becomes insufficient to hold the complete model parameters, gradients, and optimizer states. Distributed training strategies address this by dividing the work across multiple GPUs — either by replicating the model (data parallelism) or by sharding the model state across devices (model parallelism). The choice of strategy depends on the model size, available hardware, and the need for memory optimization versus implementation simplicity. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Strategy Comparison

| Strategy | Parallelism Type | Memory Efficiency | Complexity | Best For |
|----------|-----------------|-------------------|------------|----------|
| DDP | Data parallelism | Low (model fully replicated per GPU) | Low | Models that fit in a single GPU |
| FSDP | Data + model parallelism (sharded) | High (parameters, gradients, optimizer states sharded) | Moderate | Models from 20B to 120B+ parameters |
| DeepSpeed | Data + model parallelism (ZeRO stages) | Very high (advanced offloading, gradient fusion) | High | Models from 1B to 100B+ parameters requiring fine-grained control |

^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md, distributed-training-using-deepspeed-databricks-on-aws.md, best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Detailed Breakdown

### Distributed Data Parallel (DDP)

DDP replicates the model on every GPU and synchronizes gradients across all GPUs during training. Each GPU holds a complete copy of the model parameters, gradients, and optimizer states. This strategy is simple to implement and effective when the model fits comfortably within a single GPU’s memory. DDP does not provide any memory savings for the model itself; its benefit is purely in processing larger batches across multiple devices. ^[distributed-training-using-ddp-databricks-on-aws.md]

### Fully Sharded Data Parallel (FSDP)

FSDP shards model parameters, gradients, and optimizer states across all GPUs, greatly reducing the per-GPU memory footprint. It is a PyTorch-native solution that integrates seamlessly with existing PyTorch training code. During the forward and backward passes, FSDP gathers the relevant shards on demand and then discards them, achieving a memory efficiency that scales with the number of GPUs. FSDP is the recommended approach for training models in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### DeepSpeed

DeepSpeed is a library developed by Microsoft that provides advanced memory optimization through its ZeRO (Zero Redundancy Optimizer) stages. It offers fine-grained control over sharding strategies — ZeRO Stage 1 (optimizer state sharding), Stage 2 (gradient sharding), and Stage 3 (parameter sharding) — as well as additional features like CPU offloading and gradient accumulation fusion. DeepSpeed is well-suited for models from 1B to over 100B parameters when more optimization beyond standard FSDP is needed. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## When to Use Each Strategy

- **Use DDP** when your model fits entirely in a single GPU and you want the simplest possible distributed training setup. DDP is ideal for smaller models or when memory is not a bottleneck. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Use FSDP** for large models (20B+ parameters) when you need good memory efficiency without leaving the PyTorch ecosystem. FSDP balances performance and usability for most large-scale training tasks. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Use DeepSpeed** when you require advanced memory optimizations such as CPU offloading, gradient accumulation fusion, or precise control over ZeRO stages. DeepSpeed is particularly valuable for extremely large models or when hardware memory is constrained. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Related Concepts

- [ZeRO stages](/concepts/zero-stages-stage-1-2-3.md) – The three sharding levels in DeepSpeed (optimizer, gradient, parameter).
- Model Parallelism – A broader category that includes sharding strategies.
- [Data Parallelism](/concepts/data-parallelism-spark.md) – The replication strategy used by DDP.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The scale where FSDP becomes essential.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – Infrastructure considerations for large model training.
- GPU Scheduling – Optimizing GPU utilization across strategies.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- distributed-training-using-deepspeed-databricks-on-aws.md
- distributed-training-using-ddp-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
4. distributed-training-using-ddp-databricks-on-aws.md
