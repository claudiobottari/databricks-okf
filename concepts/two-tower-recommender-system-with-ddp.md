---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60ab0ba61788bcd5c9af47ea6ef347aaca69a586fa7237bd70d82babb590c7b0
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - two-tower-recommender-system-with-ddp
    - TRSWD
    - two-tower-recommender-system-training
    - TRST
    - Recommender system training
    - two-tower-recommender-training-with-ddp
    - TRTWD
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: Two-tower recommender system with DDP
description: Training a two-tower recommendation model using PyTorch Lightning and DDP on Databricks, including data preparation with Mosaic Streaming (MDS) format.
tags:
  - recommender-systems
  - pytorch-lightning
  - distributed-training
timestamp: "2026-06-18T15:29:02.303Z"
---

# Two-tower recommender system with DDP

**Two-tower recommender system with DDP** refers to the use of [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training, typically via [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), to scale the training of two-tower recommendation models across multiple GPUs. The two-tower architecture consists of separate neural networks (towers) for encoding user features and item features, whose outputs are combined (e.g., via dot product) to produce a relevance score. This approach is common in retrieval and ranking stages of modern recommendation systems.

## Overview

Training a large-scale two-tower recommender requires efficient distribution of data across multiple GPUs. DDP is a natural fit when each tower fits in a single GPU’s memory, as it replicates the full model on each GPU and splits the training data into micro-batches. PyTorch Lightning provides a high-level interface that automatically handles DDP configuration, including process group initialization, gradient synchronization, and mixed-precision orchestration. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Example workflow on AI Runtime

The Databricks AI Runtime includes notebook examples that demonstrate end-to-end training of a two-tower recommendation model using PyTorch Lightning. The steps typically include:

1. **Data preparation**: Raw interaction logs are converted into the [Mosaic Streaming (MDS) format](/concepts/mosaic-streaming-mds-format.md), which enables efficient, distributed data loading. MDS format shards the data and allows each GPU worker to stream only the shards it needs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
2. **Model definition**: A two-tower architecture is defined with separate encoding branches for users and items. The outputs are combined via a similarity function (e.g., dot product or cosine similarity).
3. **Distributed training**: PyTorch Lightning’s `Trainer` is configured with a DDP strategy. The trainer automatically spawns the appropriate number of processes, replicates the model, and synchronizes gradients after each step. Training is performed across GPU resources such as A10 GPUs or H100 GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
4. **Evaluation and logging**: Metrics such as recall or NDCG are computed in a distributed fashion, and results are logged to [MLflow](/concepts/mlflow.md).

## When to use this approach

- **Model fits in GPU memory**: Each tower independently fits within the memory of a single GPU. If the combined model is too large, consider [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md).
- **High throughput needed**: DDP scales linearly with the number of GPUs when communication overhead is manageable.
- **Simplified development**: PyTorch Lightning abstracts boilerplate DDP code, reducing the risk of common distributed training errors.

## Key components

| Component               | Role                                                                 |
|-------------------------|----------------------------------------------------------------------|
| PyTorch Lightning       | High-level training framework that automates DDP setup               |
| DDP                     | Data-parallel strategy that replicates the model and splits batches  |
| Mosaic Streaming (MDS)  | Distributed data format that supports sharded, streamed loading      |
| A10 / H100 GPUs         | GPU hardware used for training                                       |
| Databricks AI Runtime   | Managed environment that bundles GPU drivers, PyTorch, and Lightning |

## Related concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [Mosaic Streaming (MDS)](/concepts/mosaic-streaming-mds-format.md)
- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md)
- GPU training on Databricks
- A10 GPU support on Databricks
- H100 GPU support on Databricks
- MLflow integration with PyTorch Lightning

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
