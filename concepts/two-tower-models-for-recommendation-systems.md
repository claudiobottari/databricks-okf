---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 45f6d45f3c318dc8fee7e026b625dbb1a1687cd085809a3092fad126b10801ce
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - two-tower-models-for-recommendation-systems
    - TMFRS
    - recommendation systems
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Two-Tower Models for Recommendation Systems
description: Deep learning approach for building recommender systems using dual neural network architectures (two-tower models) to represent users and items.
tags:
  - recommender-systems
  - deep-learning
  - databricks
timestamp: "2026-06-18T10:44:26.960Z"
---

---
title: Two-Tower Models for Recommendation Systems
summary: Deep learning architecture for recommendation systems, where separate encoders (towers) compute embeddings for users and items, and a similarity function scores the pair. Example notebooks are available in AI Runtime.
sources:
  - ai-runtime-example-notebooks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:00:00.000Z"
updatedAt: "2026-06-18T11:00:00.000Z"
tags:
  - recommendation-systems
  - deep-learning
  - ai-runtime
  - two-tower
aliases:
  - two-tower-recommender
  - two-tower-model
confidence: 0.85
provenanceState: extracted
inferredParagraphs: 1
---

# Two-Tower Models for Recommendation Systems

**Two-tower models** are a class of deep learning architectures commonly used for building [recommendation systems](/concepts/two-tower-models-for-recommendation-systems.md). The architecture consists of two separate neural networks (the “towers”) — one encoding user features into a user embedding, the other encoding item features into an item embedding. The model computes a relevance score by applying a similarity function (typically cosine similarity or dot product) between the two embeddings. This structure makes two-tower models efficient for large-scale retrieval and ranking tasks. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Examples in AI Runtime

The [AI Runtime](/concepts/ai-runtime.md) environment on Databricks provides example notebooks that demonstrate building recommendation systems using modern deep learning approaches, including two-tower models. These examples are part of the "Deep learning based recommender systems" category in the AI Runtime example notebooks collection. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- Recommendation System — The broader task of predicting user preferences, often solved with two-tower architectures
- Deep Learning — The neural network paradigm underlying two-tower models
- [AI Runtime example notebooks](/concepts/ai-runtime-example-notebooks.md) — The collection of notebooks that includes two-tower examples
- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime that provides GPU-accelerated execution for these models

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
