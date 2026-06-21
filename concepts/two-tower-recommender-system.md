---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f97516c8418c83b42cc405afb385659d82d5bb5c7d3be3f6cc136967216d8d1c
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - two-tower-recommender-system
    - TRS
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: Two-Tower Recommender System
description: A recommendation model architecture demonstrated as a use case for distributed training with DDP on Databricks
tags:
  - recommender-systems
  - deep-learning
  - use-case
timestamp: "2026-06-19T15:13:04.643Z"
---

# Two-Tower Recommender System

A **two-tower recommender system** is a neural architecture that uses two separate neural network "towers" — one for encoding user features and one for encoding item features — to produce embeddings that are compared via a similarity function (e.g., dot product) for ranking or retrieval. The architecture is widely used in modern recommendation pipelines for its scalability and ability to handle large, sparse user-item interaction data. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Architecture

The two-tower architecture consists of two distinct neural networks that process different input modalities:

- **User tower**: Encodes user features such as user ID, demographics, historical behavior, and contextual signals into a dense embedding vector.
- **Item tower**: Encodes item features such as item ID, category, description, and metadata into a dense embedding vector of the same dimensionality.

The output embeddings from both towers are then compared using a similarity function — most commonly the dot product — to produce a relevance score for a user-item pair. During training, the model learns to maximize the similarity between positive user-item interactions and minimize it for negative samples.

## Training on Databricks

On Databricks, a concrete example of training a two-tower recommendation model using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) is available. PyTorch Lightning provides a high-level interface that automatically handles [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) configuration for multi-GPU training. The example includes data preparation using [Mosaic Streaming (MDS) format](/concepts/mosaic-streaming-mds-format.md) and distributed training across A10 or H100 GPUs. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

The training workflow on [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) involves:

1. **Data preparation**: Converting raw user-item interaction data into the Mosaic Streaming (MDS) format for efficient streaming during training.
2. **Model definition**: Defining the user tower, item tower, and similarity computation using PyTorch Lightning modules.
3. **Distributed training**: Leveraging DDP through PyTorch Lightning to scale training across multiple GPUs.
4. **Evaluation and deployment**: Using the trained embeddings for candidate generation and ranking in production recommendation pipelines.

## Use Cases

Two-tower recommender systems are particularly well-suited for:

- **Retrieval stage**: Generating a shortlist of candidate items from a large corpus efficiently using approximate nearest neighbor search on item embeddings.
- **Personalized recommendations**: Learning user preferences from historical interactions and serving recommendations in real time.
- **Cross-domain recommendation**: Adapting the architecture to handle heterogeneous user and item features from different domains.

## Advantages

- **Scalability**: Both towers can be trained independently and embeddings can be precomputed for fast retrieval.
- **Flexibility**: Each tower can accept arbitrary feature types (categorical, numerical, text, image).
- **Cold-start handling**: New users or items can be encoded through their features even without interaction history.
- **Distributed training compatibility**: The architecture maps naturally to data-parallel training frameworks like DDP.

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [Mosaic Streaming (MDS) format](/concepts/mosaic-streaming-mds-format.md)
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md)
- A10 GPU Support on Databricks
- H100 GPU Support on Databricks
- Recommendation Engines
- Embeddings
- Approximate Nearest Neighbor Search

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
