---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0155635597be7fa26f06328937ba1ec1036c681dae316e0d7d1aab08eb6957ac
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - two-tower-recommender-training-with-ddp
    - TRTWD
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: Two-Tower Recommender Training with DDP
description: Distributed training of a two-tower recommendation model using PyTorch Lightning DDP, including data preparation with Mosaic Streaming (MDS) format
tags:
  - recommender-systems
  - distributed-training
  - pytorch-lightning
  - databricks
timestamp: "2026-06-18T12:01:31.109Z"
---

---
title: Two-Tower Recommender Training with DDP
summary: Training a two-tower recommendation model using PyTorch Lightning and Distributed Data Parallel (DDP) on AI Runtime, including data preparation with Mosaic Streaming (MDS) format.
sources:
  - distributed-data-parallel-ddp-training-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:13:02.271Z"
updatedAt: "2026-06-18T11:13:02.271Z"
tags:
  - distributed-training
  - ddp
  - pytorch-lightning
  - recommendation
  - gpu
aliases:
  - two-tower-recommender-training-with-ddp
  - TTRTDDP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Two-Tower Recommender Training with DDP

**Two-Tower Recommender Training with DDP** refers to the practice of training a two-tower recommendation model using [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) with [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) on Databricks AI Runtime. The two-tower architecture consists of separate neural networks — a query tower and an item tower — that learn embeddings in a shared space. DDP replicates the full model on each GPU and splits data batches across GPUs, making it suitable when the model fits entirely in a single GPU’s memory and the goal is to scale training via increased data throughput. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## When to Use DDP for Two-Tower Recommenders

Use DDP when:
- The two-tower model fits completely in a single GPU’s memory.
- You want to scale training by increasing the number of training examples processed per second.
- You need the simplest distributed training approach, with automatic support in most frameworks like PyTorch Lightning. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

For larger models that do not fit in single GPU memory, consider [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) or [DeepSpeed](/concepts/deepspeed.md) instead. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Approach with PyTorch Lightning

PyTorch Lightning provides a high-level interface that automatically handles DDP configuration for multi-GPU training. The notebook example on Databricks demonstrates how to train a two-tower recommendation model using PyTorch Lightning on AI Runtime. Lightning abstracts away the boilerplate of setting up process groups, synchronizing gradients, and managing data loading, allowing the developer to focus on model and training logic. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Data Preparation with Mosaic Streaming (MDS)

The example includes data preparation using the [Mosaic Streaming (MDS)](/concepts/mosaic-streaming-mds-format.md) format. MDS is a binary format designed for high-performance streaming of large datasets to GPUs, reducing I/O bottlenecks during distributed training. Converting the training data to MDS format before launching the DDP job helps achieve efficient throughput across multiple GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## GPU Requirements

The training setup can run on A10 or H100 GPUs available in Databricks’ serverless GPU resources. The specific choice of GPU depends on model size and performance requirements. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Complete Notebooks

The full notebook for two-tower recommender training with DDP, along with data preparation steps, is available on the [Deep learning recommendation examples](/concepts/deep-learning-based-recommender-systems.md) page. This page also includes the companion notebook for data preparation and MDS format conversion. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The core parallelism technique used
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — The training framework that automates DDP orchestration
- [Mosaic Streaming (MDS)](/concepts/mosaic-streaming-mds-format.md) — Binary streaming format for efficient data loading
- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) — Fully Sharded Data Parallelism for larger models
- [DeepSpeed](/concepts/deepspeed.md) — Another alternative for very large models
- Multi-layer Perceptron (MLP) — Another DDP example using a simple neural network
- GPU training on AI Runtime — Infrastructure for distributed GPU workloads

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
