---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f554e4d79f6ca18b9439ccc43ab1d7747f3a0e7782d473ff8e479e60cb13da61
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alternatives-to-ddp-fsdp-and-deepspeed
    - "DeepSpeed and Alternatives to DDP: FSDP"
    - ATDFAD
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: "Alternatives to DDP: FSDP and DeepSpeed"
description: Fully Sharded Data Parallel (FSDP) and DeepSpeed as alternatives to DDP for models that don't fit in a single GPU's memory
tags:
  - distributed-training
  - model-parallelism
  - alternatives
timestamp: "2026-06-19T15:12:19.483Z"
---

# Alternatives to DDP: FSDP and DeepSpeed

Distributed Data Parallel (DDP) is the most common parallelism technique for distributed training: the full model is replicated on each GPU and data batches are split across GPUs. However, DDP requires the model to fit entirely into a single GPU’s memory. For larger models that exceed a single GPU’s memory capacity, alternative approaches such as **Fully Sharded Data Parallel (FSDP)** and **DeepSpeed** are used. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Fully Sharded Data Parallel (FSDP)

FSDP shards model parameters, gradients, and optimizer states across multiple GPUs, significantly reducing the per-GPU memory footprint. This enables training of very large models that would otherwise be impossible. FSDP is the primary recommended approach for training models in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

FSDP offers a better trade-off for memory efficiency compared to standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). While DDP is simpler for models that fit in a single GPU, FSDP becomes the necessary choice for models that do not. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## DeepSpeed

DeepSpeed provides additional memory optimization features beyond what FSDP offers out-of-the-box. It is considered when more sophisticated optimization features are required, such as for models that need even more advanced memory management strategies. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to Use Each Strategy

- **DDP**: Best suited for models that fit within a single GPU’s memory. It is the simplest distributed training approach with automatic support in most frameworks. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
- **FSDP**: The standard choice for training models in the 20B to 120B+ parameter range to overcome single-GPU memory limitations. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **DeepSpeed**: Considered when more sophisticated memory optimization features beyond FSDP are required. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
