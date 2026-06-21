---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65c4481e3ef42e08c9e104c30f7af3a270d4edf06df27b6d5412eac70f8f2cd7
  pageDirectory: concepts
  sources:
    - multi-gpu-distributed-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fsdp-fully-sharded-data-parallel-on-databricks
    - F(SDPOD
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: multi-gpu-distributed-training-databricks-on-aws.md
title: FSDP (Fully Sharded Data Parallel) on Databricks
description: A parallelism technique that shards model parameters, gradients, and optimizer states across GPUs to reduce memory usage for large models.
tags:
  - parallelism
  - deep-learning
  - databricks
timestamp: "2026-06-19T19:47:31.391Z"
---

## FSDP (Fully Sharded Data Parallel) on Databricks

**Fully Sharded Data Parallel (FSDP)** is a distributed training technique available on Databricks that shards model parameters, gradients, and optimizer states across multiple GPUs. By distributing these components, FSDP significantly reduces the per‑GPU memory footprint, enabling the training of very large models that would otherwise exceed the memory capacity of a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### How FSDP Works

Unlike standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), which replicates the entire model on each GPU, FSDP partitions the model’s parameters, gradients, and optimizer states across the available GPUs. During the forward and backward passes, FSDP collects the sharded parameters on‑demand and then discards them after use, which further reduces memory consumption. This sharding strategy makes FSDP the appropriate choice for models that do not fit into a single GPU’s memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### When to Use FSDP

FSDP is best suited for **memory‑constrained training of large models** and for models that do not fit in a single GPU. ^[multi-gpu-distributed-training-databricks-on-aws.md] It is the standard recommended approach for models in the 20 billion to 120+ billion parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] For models that fit comfortably in a single GPU, DDP is simpler and sufficient; when even more advanced memory optimization is needed, practitioners may consider [DeepSpeed](/concepts/deepspeed.md) as an alternative. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Availability and Usage

FSDP is supported on Databricks AI Runtime (which includes the necessary PyTorch and CUDA libraries) and works with H100 GPUs. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] You can use the `@distributed` decorator from the `serverless_gpu` library to coordinate FSDP across multiple GPUs on a single node or across nodes (multi‑node distributed training). For a detailed walkthrough, Databricks provides example notebooks that demonstrate FSDP fine‑tuning using Hugging Face Transformers and PyTorch FSDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Comparison with Other Techniques

- **DDP**: Replicates the full model on each GPU; simpler but no memory savings for large models. ^[multi-gpu-distributed-training-databricks-on-aws.md]
- **DeepSpeed**: Offers additional memory‑optimization features beyond FSDP, such as ZeRO stages. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- H100 GPU Support on Databricks
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md)

### Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- multi-gpu-distributed-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
2. [multi-gpu-distributed-training-databricks-on-aws.md](/references/multi-gpu-distributed-training-databricks-on-aws-acaa7a08.md)
