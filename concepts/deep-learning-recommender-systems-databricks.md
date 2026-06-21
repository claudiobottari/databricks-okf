---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0fd98f440714dddabfb3646c5ddc506ba354ddbeff7ae7b7f1d3df34fb72a17e
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-recommender-systems-databricks
    - DLRS(
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Deep Learning Recommender Systems (Databricks)
description: Examples for building recommendation systems using deep learning approaches like two-tower models on AI Runtime
tags:
  - recommender-systems
  - deep-learning
  - databricks
timestamp: "2026-06-19T08:57:31.683Z"
---

# Deep Learning Recommender Systems (Databricks)

**Deep Learning Recommender Systems (Databricks)** refers to the set of example notebooks and best practices for building recommendation systems using modern deep learning approaches, such as two-tower models, within the Databricks environment. These resources are part of the [AI Runtime for single-node tasks](/concepts/ai-runtime-for-single-node-tasks.md) (in Public Preview) and leverage GPU acceleration for training and inference. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

Databricks provides example notebooks demonstrating how to build recommendation systems using deep learning, covering both single-node and multi-GPU distributed training scenarios. The examples focus on modern architectures like two-tower models, which separate user and item embeddings into distinct towers and compute relevance via dot product or similarity. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

These notebooks are part of a larger collection of AI Runtime examples, which also cover [Large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md), Computer vision, Classic ML, and [Multi-GPU distributed training](/concepts/multi-gpu-distributed-training-databricks.md). ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Two-Tower Models

A two-tower model is a neural architecture commonly used for recommendation and retrieval. It consists of:

- **User tower**: Encodes user features (e.g., history, demographics) into an embedding vector.
- **Item tower**: Encodes item features (e.g., content, metadata) into an embedding vector of the same dimensionality.

The dot product (or cosine similarity) between the two embeddings represents the predicted relevance score. Two-tower models are efficient for large-scale candidate generation because item embeddings can be precomputed and indexed for fast retrieval. Databricks examples cover training such models at scale, including data preparation, model definition, and inference pipelines. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example Notebooks

The notebooks are available in the Databricks AI Runtime examples repository under the "Deep learning based recommender systems" category. They include end-to-end workflows such as:

- Data ingestion and feature engineering for user-item interactions.
- Training two-tower models using TensorFlow, PyTorch, or other frameworks.
- Evaluation and hyperparameter tuning.
- Deployment for real-time or batch recommendation.

For full details, see the official Databricks documentation: [Deep learning based recommender systems examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-recommendation). ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime for single-node tasks](/concepts/ai-runtime-for-single-node-tasks.md)
- [Two-tower model](/concepts/two-tower-recommendation-model.md) — Neural architecture for recommendation
- GPU-accelerated training on Databricks
- Recommender systems best practices
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
