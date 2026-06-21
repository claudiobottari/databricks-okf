---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9e80aa5b46f121fdf935d90e6a24bbd812d9847ee161405a280c493f5e19eb8
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-for-recommender-systems
    - ARFRS
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: AI Runtime for Recommender Systems
description: Databricks AI Runtime provides infrastructure for building deep learning based recommendation systems, supporting both single-node (Public Preview) and multi-GPU distributed training (Beta).
tags:
  - databricks
  - recommender-systems
  - deep-learning
  - mLOps
timestamp: "2026-06-19T14:57:40.177Z"
---

## AI Runtime for Recommender Systems

AI Runtime provides notebook examples and tools for building deep learning–based recommendation systems. These examples demonstrate how to create efficient recommendation models using modern deep learning approaches, with a focus on the two‑tower architecture implemented with [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) for distributed training. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

As of the current documentation, AI Runtime for single-node tasks is in **Public Preview**, while the distributed training API (used for multi-GPU workloads such as multi-node recommendation training) remains in **Beta**. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

The primary example available is the **Two-tower recommendation model** tutorial, which shows how to create a two‑tower recommendation model using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) for distributed training. This model is a common architecture for large‑scale retrieval and candidate generation in recommender systems. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

### Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The underlying platform providing GPU‑accelerated environments for machine learning workloads.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — The training framework used in the two‑tower recommendation example.
- [Two-Tower Model](/concepts/two-tower-recommendation-model.md) — A neural architecture that learns separate embeddings for queries and items.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling recommendation model training across multiple GPUs and nodes.
- [Deep learning based recommender systems](/concepts/deep-learning-based-recommender-systems.md) — Broader methodology for building recommendation engines with neural networks.

### Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
