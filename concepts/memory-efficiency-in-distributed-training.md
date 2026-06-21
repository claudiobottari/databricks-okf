---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fca48070087d35feaa54800af4901df0ec1b397ffc72ada93c77013ac40b0992
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - memory-efficiency-in-distributed-training
    - MEIDT
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Memory Efficiency in Distributed Training
description: The comparative memory efficiency of FSDP over DDP as a key consideration for choosing training strategies
tags:
  - memory-optimization
  - distributed-training
  - gpu
timestamp: "2026-06-18T12:27:03.460Z"
---

<!-- NOTE: This page is derived from the provided source material only. Additional detail on memory efficiency techniques, such as activation checkpointing or mixed-precision training, is not included because it is not present in the source. -->

# Memory Efficiency in Distributed Training

**Memory efficiency** is a critical concern when training large neural networks, particularly models with billions of parameters that exceed the memory capacity of a single GPU. Distributed training techniques address this problem by partitioning the model’s memory footprint—parameters, gradients, and optimizer states—across multiple devices, enabling the training of much larger models than a single GPU could hold. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Fully Sharded Data Parallel (FSDP)

[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is a PyTorch-based strategy that shards model parameters, gradients, and optimizer states across all available GPUs. During training, each GPU holds only a slice of the full model state, and the shards are gathered on-demand for forward and backward passes. This dramatically reduces per-GPU memory consumption, making it possible to train models in the 20 billion to 120 billion+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### When to Use FSDP

FSDP is the recommended approach when:

- The model is too large to fit in a single GPU’s memory.
- The target model size is in the 20 billion to 120 billion+ parameter range.
- Greater memory efficiency is required than what [Data Distributed Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) provides.

For smaller models that fit comfortably in a single GPU, DDP offers a simpler implementation. For scenarios that demand even more advanced memory optimization, such as offloading to CPU or fine-grained control over sharding, [DeepSpeed](/concepts/deepspeed.md) provides additional features. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [GPU Memory](/concepts/gpu-utilization-monitoring-dashboard.md)
- [Large Language Models](/concepts/large-language-models-llms-on-databricks.md)
- Model Parallelism
- Tensor Parallelism

## Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
