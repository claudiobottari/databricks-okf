---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22f9dfe21872c264772ae3828fdd21ccbb2166d77e1c1bd154a5be3a5e815113
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-to-use-fsdp
    - WTUF
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: When to use FSDP
description: "Decision criteria for adopting FSDP: when models are too large for single GPU memory, when training models in the 20B to 120B+ parameter range, and when more memory efficiency than DDP is needed."
tags:
  - decision-guidance
  - best-practices
  - deep-learning
timestamp: "2026-06-19T10:40:42.648Z"
---

# When to use FSDP

**Fully Sharded Data Parallel (FSDP)** is a training technique that shards model parameters, gradients, and optimizer states across multiple GPUs to reduce per-GPU memory consumption. It is particularly useful for training large models that cannot fit into the memory of a single GPU.

## When to use FSDP

Use FSDP in the following scenarios:

- **Your model is too large to fit in a single GPU's memory**: FSDP shards all model components across GPUs, reducing the per-device memory footprint and enabling training of models that exceed single-GPU capacity.
- **You need to train models in the 20B to 120B+ parameter range**: This parameter range is where FSDP provides significant advantages over simpler data-parallel approaches, as the model memory requirements at this scale exceed what any single GPU can provide.
- **You want more memory efficiency than DDP provides**: For models that do not fit in a single GPU, FSDP offers a better memory-efficiency trade-off compared to Distributed Data Parallel (DDP). ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to consider alternatives

- **For smaller models that fit in single GPU memory**: DDP is a simpler alternative that may be preferable when model memory is not a constraint. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **For advanced memory optimization features**: [DeepSpeed](/concepts/deepspeed.md) provides additional training strategies and optimization features beyond what FSDP offers. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Related concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – The core technique for sharding model state across GPUs
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Simpler parallelism for models that fit in one GPU
- [DeepSpeed](/concepts/deepspeed.md) – Alternative with advanced memory optimization
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The parameter range where FSDP is especially useful

## Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
