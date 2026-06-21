---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67908b9bbceee17844bce8945b2a9ed0378b5219cc1113e222b8768e55c29a60
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - two-tower-recommender-system-training
    - TRST
    - Recommender system training
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: Two-tower recommender system training
description: A recommendation model architecture trained using PyTorch Lightning and DDP on Databricks, with data prepared in Mosaic Streaming format.
tags:
  - recommender-systems
  - deep-learning
  - pytorch-lightning
timestamp: "2026-06-19T18:32:12.229Z"
---

## Two-tower Recommender System Training

**Two-tower recommender system training** refers to the distributed training of a two-tower (dual-encoder) recommendation model on Databricks AI Runtime. This approach uses [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) with [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) to scale across multiple GPUs, along with [Mosaic Streaming (MDS)](/concepts/mosaic-streaming-mds-format.md) format for efficient data loading. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Overview

The two-tower architecture consists of separate neural networks (towers) for encoding user features and item features, producing embeddings that are compared via a similarity function (e.g., dot product) for recommendation. Training a two-tower model at scale requires distributed training because datasets are large and the model may not fit on a single GPU. Databricks provides a complete notebook example demonstrating this training pipeline using PyTorch Lightning, which automatically configures DDP for multi-GPU training. The example includes data preparation and conversion to MDS format, and supports distributed training across A10 GPU or H100 GPU accelerators. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Key Techniques

- **PyTorch Lightning**: Provides a high-level interface that handles DDP configuration automatically, abstracting away boilerplate code for multi-GPU synchronization. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
- **Distributed Data Parallel (DDP)**: The underlying parallelism strategy, where the full model is replicated on each GPU and data batches are split across GPUs. This is the most common technique for training models that fit in a single GPU's memory. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]
- **Mosaic Streaming (MDS) format**: Used for data preparation; the MDS format enables efficient streaming of large training datasets to GPUs without loading the entire dataset into memory. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Hardware and Platform

The training runs on Databricks AI Runtime with serverless GPU resources. The notebook supports both A10 GPU and H100 GPU instances. For larger model training, the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) or multi-node setups may be used. The complete example is part of the Databricks deep learning recommendation examples collection. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

### Related Concepts

- [Distributed Data Parallel (DDP) Training](/concepts/distributed-data-parallel-ddp-training.md)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [Mosaic Streaming (MDS)](/concepts/mosaic-streaming-mds-format.md)
- [Two-tower model](/concepts/two-tower-recommendation-model.md)
- [Recommender system training](/concepts/two-tower-recommender-system-training.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [AI Runtime on Databricks](/concepts/ai-runtime-on-databricks.md)
- [Deep learning recommendation examples](/concepts/deep-learning-based-recommender-systems.md)

### Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
