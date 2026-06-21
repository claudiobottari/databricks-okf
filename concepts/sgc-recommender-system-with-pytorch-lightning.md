---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6a0c042e2c251365ea900da9f07b4a132176c08a8707d7699d1bc90bfc04c77
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - sgc-recommender-system-with-pytorch-lightning
    - SRSWPL
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: SGC recommender system with PyTorch Lightning
description: A tutorial pattern using Simplified Graph Convolution (SGC) for recommendations, implemented with PyTorch Lightning for distributed training on Databricks
tags:
  - graph-neural-networks
  - recommender-systems
  - pytorch
timestamp: "2026-06-18T15:13:19.060Z"
---

---

title: SGC Recommender System with PyTorch Lightning
summary: A two-tower recommendation model implemented using PyTorch Lightning for distributed training, available as a tutorial in Databricks AI Runtime.
sources:
  - deep-learning-based-recommender-systems-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:33:25.717Z"
updatedAt: "2026-06-18T14:33:25.717Z"
tags:
  - databricks
  - recommender-systems
  - pytorch-lightning
  - distributed-training
  - ai-runtime
aliases:
  - sgc-recommender-system-with-pytorch-lightning
  - SGC-RS-PL
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0

---

# SGC Recommender System with PyTorch Lightning

The **SGC recommender system with PyTorch Lightning** is a tutorial example that demonstrates how to build a **two-tower recommendation model** using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) for distributed training. It is part of the Databricks [AI Runtime](/concepts/ai-runtime.md) examples for deep-learning-based recommendation systems. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Overview

Two-tower models are a common architecture for large-scale recommendation systems. One tower encodes user features and the other encodes item features; the model learns to maximize the similarity between a user and an item they interact with. The SGC (Simplified Graph Convolution) variant often integrates graph signals into the towers, though the specific algorithm details are covered in the tutorial itself. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

This tutorial uses PyTorch Lightning to simplify distributed training across multiple GPUs, enabling efficient scaling for large recommendation datasets. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Availability and Status

- **AI Runtime for single-node tasks**: Public Preview.
- **Distributed training API for multi-GPU workloads**: Beta.

Users should verify the status of these features in their Databricks environment. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Related Concepts

- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- [AI Runtime](/concepts/ai-runtime.md)
- [Deep learning based recommender systems](/concepts/deep-learning-based-recommender-systems.md) (parent page)

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
