---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abd8e8d5004fc3fae2f92d237d6563e788e4cb9246eb3bf5e9e6e9a699001858
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-based-recommender-systems
    - DLBRS
    - Deep Learning Based Recommender Systems on AI Runtime
    - Deep learning recommender systems
    - Deep learning recommendation examples
    - deep-learning-based recommendation models
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Deep learning based recommender systems
description: Notebook examples for building recommendation systems on Databricks AI Runtime using modern deep learning approaches like two-tower models.
tags:
  - databricks
  - recommender-systems
  - deep-learning
  - two-tower
timestamp: "2026-06-19T22:04:07.913Z"
---

# Deep Learning Based Recommender Systems

**Deep learning based recommender systems** are a class of recommendation algorithms that leverage neural network architectures to model user-item interactions and generate personalized recommendations. These approaches have become increasingly popular for building modern recommendation systems due to their ability to capture complex, non-linear relationships in user behavior data. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

Deep learning approaches to recommendation systems move beyond traditional collaborative filtering and matrix factorization methods by using neural networks to learn rich representations of users and items. These models can incorporate diverse data types including user demographics, item features, and contextual information to produce more accurate and personalized recommendations. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Two-Tower Models

A prominent deep learning architecture for recommendation systems is the **two-tower model** (also known as dual-encoder or Siamese network). This architecture consists of two separate neural networks:

- A **user tower** that encodes user features into a dense embedding vector
- An **item tower** that encodes item features into a dense embedding vector

The similarity between user and item embeddings is computed (often via dot product or cosine similarity) to generate relevance scores for recommendation candidates. Two-tower models are particularly effective for large-scale retrieval tasks because the item embeddings can be precomputed and indexed for efficient serving. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Implementation on Databricks

Databricks provides example notebooks demonstrating how to build deep learning based recommender systems using [AI Runtime](/concepts/ai-runtime.md). These examples cover:

- Building two-tower models for recommendation
- Training on GPU infrastructure for faster iteration
- Integrating with the Databricks platform for data processing and model management

The examples are available as part of the AI Runtime example notebooks collection under the deep learning based recommender systems section. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime environment optimized for AI and machine learning workloads
- [Two-tower models](/concepts/two-tower-recommendation-model.md) — The dual-encoder architecture commonly used in modern recommendation systems
- Collaborative filtering — Traditional recommendation approach that deep learning methods extend upon
- Matrix factorization — A foundational technique for recommendation that neural approaches generalize
- [Large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — Another category of deep learning models with example notebooks available
- Computer vision — Additional deep learning domain with example notebooks on Databricks
- [Multi-GPU distributed training](/concepts/multi-gpu-distributed-training-databricks.md) — Scaling recommendation model training across multiple GPUs

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
