---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 805b1706ddef7bc5b6413117060c23c6833e6f303630f48a02c6db0f429b1a5a
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-sharding
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Model sharding
description: The technique of partitioning model parameters, gradients, and optimizer states across multiple devices to overcome single-GPU memory limitations.
tags:
  - distributed-training
  - memory-optimization
  - deep-learning
timestamp: "2026-06-19T18:55:50.124Z"
---

Here is the wiki page for "Model sharding", written based solely on the provided source material.

## Model Sharding

**Model sharding** is a distributed training technique used to train very large deep learning models that cannot fit into the memory of a single GPU. Instead of storing a complete copy of the model on each GPU, model sharding partitions the model's parameters, gradients, and optimizer states across multiple GPUs, significantly reducing the memory footprint per device. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Overview

As models grow to billions of parameters, standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) becomes impractical because each GPU must hold a full copy of the model, which exceeds available memory. Model sharding addresses this limitation by distributing the model components across GPUs, enabling the training of models that are much larger than what a single GPU can accommodate. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Implementation: Fully Sharded Data Parallel (FSDP)

The primary implementation of model sharding in PyTorch is [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). FSDP shards model parameters, gradients, and optimizer states across GPUs. During the forward and backward passes, FSDP collects the necessary shards for each layer on demand and then discards them, keeping only the shard assigned to the current GPU in memory at a time. This approach provides a better trade-off for memory efficiency compared to DDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

FSDP is particularly useful for training models in the [20B to 120B+ parameter range](/concepts/20b-to-120b-parameter-model-training.md). ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### When to Use Model Sharding

Model sharding (via FSDP) is recommended when:

- The model is too large to fit in a single GPU's memory.
- Training models in the 20B to 120B+ parameter range.
- Greater memory efficiency than DDP is required.

For smaller models that fit in single GPU memory, DDP is simpler to implement. For even more advanced memory optimization features, alternatives like [DeepSpeed](/concepts/deepspeed.md) may be considered. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

### Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
