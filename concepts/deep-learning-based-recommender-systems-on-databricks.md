---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91f7a65347debd57e6e7e6455e97284a9474815611dc742404adf57e0968e447
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - deep-learning-based-recommender-systems-on-databricks
    - DLBRSOD
    - Deep Learning Based Recommender Systems on AI Runtime
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: Deep Learning Based Recommender Systems on Databricks
description: The overall pattern of building modern recommendation systems using deep learning approaches within the Databricks platform, leveraging AI Runtime and GPU acceleration.
tags:
  - recommendation-systems
  - deep-learning
  - databricks
  - machine-learning
timestamp: "2026-06-19T18:18:52.815Z"
---

Here is the updated wiki page for "Deep Learning Based Recommender Systems on Databricks":

---

# Deep Learning Based Recommender Systems on Databricks

**Deep learning based recommender systems** on Databricks leverage the [AI Runtime](/concepts/ai-runtime.md) platform to build efficient, modern recommendation models using advanced deep learning techniques. AI Runtime provides a purpose-built environment for single-node and multi-GPU machine learning workloads, enabling data scientists and engineers to develop production-grade recommendation systems at scale. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Overview

AI Runtime for single-node tasks is in Public Preview, while the distributed training API for multi-GPU workloads remains in Beta. These examples demonstrate how to create efficient recommendation models using modern deep learning approaches on Databricks. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Key Concepts

### AI Runtime

AI Runtime is Databricks' optimized environment for machine learning workloads, including recommendation systems. It provides pre-configured dependencies, GPU acceleration, and integration with [MLflow](/concepts/mlflow.md) for experiment tracking and model management.

### Two-Tower Architecture

The core architectural pattern demonstrated is the **two-tower model**, which separates the representation learning for users and items into two distinct neural network towers. This architecture is particularly suitable for large-scale recommendation tasks due to its ability to efficiently compute embeddings for candidate items and user queries.

## Tutorial: Two-Tower Recommendation Model

The primary tutorial available demonstrates how to create a **two-tower recommendation model** using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) for distributed training. This approach enables: ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

- **Scalable training** across multiple GPUs using AI Runtime's distributed training capabilities
- **Efficient inference** through the two-tower architecture's candidate generation and retrieval pipeline
- **Integration with MLflow** for experiment tracking, model versioning, and deployment

## Implementation Steps

### 1. Environment Setup

Configure AI Runtime with GPU acceleration and install required dependencies including PyTorch Lightning and GPU-optimized libraries.

### 2. Data Preparation

Prepare user-item interaction data, including:
- User features and identifiers
- Item features and identifiers
- Interaction timestamps and signals
- Negative sampling strategies

### 3. Model Architecture

Build the two-tower architecture:
- **User tower**: Embeds user features into a dense representation
- **Item tower**: Embeds item features into a dense representation
- **Matching function**: Computes similarity between user and item embeddings (e.g., dot product or cosine similarity)

### 4. Training Configuration

Configure distributed training parameters:
- Number of GPUs and workers
- Batch size and learning rate
- Loss function (e.g., cross-entropy for recommendation tasks)
- Optimization strategy

### 5. Evaluation and Deployment

Use MLflow to:
- Track experiments and hyperparameters
- Log model artifacts and performance metrics
- Register models for production serving
- Monitor online performance with [MLflow Monitoring](/concepts/mlflow-production-monitoring.md)

## Best Practices

- **Use two-tower architecture** for large-scale candidate retrieval tasks
- **Leverage GPU acceleration** with AI Runtime for faster training and inference
- **Implement negative sampling** strategies to improve model robustness
- **Monitor model performance** in production using MLflow's monitoring capabilities
- **Scale horizontally** with distributed training across multiple GPUs

## Related Resources

- Two-Tower Recommendation System with PyTorch Lightning — Full tutorial on building two-tower models on Databricks ^[deep-learning-based-recommender-systems-databricks-on-aws.md]
- GPU Recommendation Examples — Additional example notebooks
- [AI Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Platform overview and capabilities
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU infrastructure for training workloads

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
