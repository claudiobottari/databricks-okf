---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22c244eae358dbbdef70fbb73003cecb328f236589d4dd1dc7f57a6d2591dafb
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-to-use-ddp
    - WTUD
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: When to use DDP
description: "Conditions for using DDP: model fits in single GPU memory, scaling via data throughput, and need for simplest distributed training approach."
tags:
  - distributed-training
  - best-practices
timestamp: "2026-06-19T18:32:00.929Z"
---

# When to use DDP

**Distributed Data Parallel (DDP)** is the most common parallelism technique for distributed training in PyTorch. In DDP, the full model is replicated on each GPU and data batches are split across GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to use DDP

Use DDP when:

- Your model fits completely in a single GPU's memory
- You want to scale training by increasing data throughput
- You need the simplest distributed training approach with automatic support in most frameworks

^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When not to use DDP

For larger models that don't fit in single GPU memory, consider alternative approaches instead:

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Shards model parameters, gradients, and optimizer states across GPUs, enabling training of models in the 20B to 120B+ parameter range.
- [DeepSpeed](/concepts/deepspeed.md) — Provides additional memory optimization features beyond what FSDP offers.

^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Comparison with other strategies

| Strategy | Best for | Memory model |
|---|---|---|
| DDP | Models that fit in a single GPU | Full model replicated on each GPU |
| FSDP | 20B to 120B+ parameter models | Sharded across GPUs |
| DeepSpeed | Models requiring advanced memory optimization | Sharded with additional features |

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
