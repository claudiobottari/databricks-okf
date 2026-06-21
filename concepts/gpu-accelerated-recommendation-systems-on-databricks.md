---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d1bd80e8836c9b6599595e460673f56d30c1510224994e9f647803e611c00fb
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-accelerated-recommendation-systems-on-databricks
    - GRSOD
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: GPU-Accelerated Recommendation Systems on Databricks
description: The practice of building and training deep learning based recommendation models using GPU acceleration within the Databricks environment on AWS.
tags:
  - gpu
  - recommender-systems
  - databricks
  - aws
timestamp: "2026-06-19T09:57:49.289Z"
---

Here is the wiki page for "GPU-Accelerated Recommendation Systems on Databricks", written based solely on the provided source material.

---

## GPU-Accelerated Recommendation Systems on Databricks

**GPU-Accelerated Recommendation Systems on Databricks** refers to the use of [AI Runtime](/concepts/ai-runtime.md) and GPU clusters to build and train deep learning-based recommendation models, such as two-tower architectures. These workloads are supported on Databricks via specialized runtimes and are optimized for both single-node and distributed multi-GPU training scenarios.

## Overview

Recommendation systems on Databricks leverage modern deep learning approaches to create efficient models. The platform provides notebook examples and tutorials that demonstrate how to build these systems using [AI Runtime](/concepts/ai-runtime.md), which is designed for single-node tasks and is currently in Public Preview. For multi-GPU workloads, the distributed training API remains in Beta. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Two-Tower Recommendation Model

A key architecture demonstrated on Databricks is the [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md). This model uses [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) for distributed training. The two-tower architecture separately encodes user and item features into embedding vectors, then computes similarity scores (often via dot product) to generate recommendations. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

### Implementation with PyTorch Lightning

The tutorial on creating a two-tower recommendation model shows how to use PyTorch Lightning to enable efficient distributed training across multiple GPUs. This approach handles the scaling and parallelism required for large-scale recommendation workloads. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Supported Runtimes and APIs

- **AI Runtime for single-node tasks**: In Public Preview. Suitable for smaller-scale recommendation experiments and development.
- **Distributed training API for multi-GPU workloads**: In Beta. Used for scaling up training across multiple GPUs for production-grade recommendation systems.

## Available Tutorials

Databricks provides the following notebook-based tutorial for GPU-accelerated recommendation systems:

- **Two-tower recommendation model**: Learn how to create a two-tower recommendation model using PyTorch Lightning for distributed training.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment for GPU-accelerated machine learning tasks on Databricks.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – The deep learning framework used for distributed training of recommendation models.
- [Two-Tower Model](/concepts/two-tower-recommendation-model.md) – A neural architecture for recommendation systems that separately encodes users and items.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) – Multi-GPU training capabilities for scaling deep learning workloads.
- GPU Scheduling – Best practices for GPU resource allocation on Databricks.

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
