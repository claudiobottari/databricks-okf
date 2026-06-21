---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb02c7f4f8dc821569d78624a9002171fbebc930ecc32f33f8941f5847a244c6
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-to-use-ddp-vs-fsdpdeepspeed
    - WTUDVF
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: When to use DDP vs FSDP/DeepSpeed
description: Decision criteria for choosing DDP over alternative distributed training techniques like FSDP or DeepSpeed based on model size and memory constraints.
tags:
  - distributed-training
  - model-scaling
  - decision-guide
timestamp: "2026-06-18T15:28:22.499Z"
---

# When to use DDP vs FSDP/DeepSpeed

Choosing the right distributed training strategy depends primarily on model size, memory constraints, and the need for advanced optimization features. The three main options—[Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), and [DeepSpeed](/concepts/deepspeed.md)—offer different trade-offs between simplicity, memory efficiency, and flexibility.

## When to use DDP

Use [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) when:

- **The model fits completely in a single GPU’s memory.** DDP replicates the full model on each GPU and splits the data batch across GPUs. No sharding of model state occurs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
- **You want to scale training by increasing data throughput.** DDP is efficient for larger batch sizes when memory is not the bottleneck. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
- **You need the simplest distributed training approach.** DDP is built into PyTorch and most frameworks support it automatically, requiring minimal configuration. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

For models that are too large for a single GPU, DDP is not sufficient.

## When to use FSDP

[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is the recommended choice when:

- **The model does not fit in a single GPU’s memory.** FSDP shards the model parameters, gradients, and optimizer states across multiple GPUs, dramatically reducing per-GPU memory footprint. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **You need a better memory-vs.-performance trade-off than DDP.** FSDP offers significantly lower memory consumption while maintaining good compute efficiency, making it the standard approach for models in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **DDP is too memory-constrained but you still want a built-in PyTorch solution.** FSDP is part of the PyTorch distributed package and integrates with existing training workflows. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to use DeepSpeed

Consider [DeepSpeed](/concepts/deepspeed.md) when:

- **You require more advanced memory optimization features beyond what FSDP offers out of the box.** DeepSpeed provides additional strategies such as ZeRO-Offload, CPU offloading, and more granular control over communication and gradient compression. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **You are scaling to very large models (e.g., 100B+ parameters) or need extreme memory savings.** DeepSpeed’s ZeRO stages and optimizer innovations can push memory efficiency further than standard FSDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **You have specialized hardware or need fine-grained tuning of distributed training behavior.** DeepSpeed offers many configuration knobs for advanced users. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Decision summary

| Condition | Recommended approach |
|-----------|----------------------|
| Model fits in single GPU; need simplest setup | DDP |
| Model does not fit in single GPU; need good memory/compute trade-off | FSDP |
| Model very large (e.g., >20B parameters) or extreme memory savings required | DeepSpeed or FSDP with advanced tuning |

## Related concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- GPU Scheduling

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
