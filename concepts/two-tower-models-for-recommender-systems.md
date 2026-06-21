---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 737f2248c27946fe5cddd4b5c91a164756caf981091a2db7fd74763eb85aaa33
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - two-tower-models-for-recommender-systems
    - TMFRS
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Two-Tower Models for Recommender Systems
description: A deep learning architecture for recommendation systems that uses separate neural networks (towers) to encode users and items into a shared embedding space.
tags:
  - machine-learning
  - recommender-systems
  - deep-learning
timestamp: "2026-06-19T13:58:06.156Z"
---

# Two-Tower Models for Recommender Systems

**Two-Tower Models for Recommender Systems** refers to a family of deep learning architectures used to build [recommendation systems](/concepts/two-tower-models-for-recommendation-systems.md). The Databricks [AI Runtime](/concepts/ai-runtime.md) provides example notebooks that demonstrate how to implement these models for modern recommendation tasks.^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

Two-tower models are a modern deep learning approach for recommendation systems. They typically encode user features and item features into separate neural network "towers" and learn to match users with relevant items. The Databricks AI Runtime includes a set of example notebooks under the **Deep learning based recommender systems** category that illustrate building such models.^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example Notebooks

The AI Runtime example notebooks are organized by task. The recommendation systems examples cover building recommender systems using modern deep learning approaches, with two-tower models as a highlighted technique. These notebooks are designed to be run on GPU-enabled clusters in the AI Runtime environment.^[ai-runtime-example-notebooks-databricks-on-aws.md]

For a full list of available examples, see the AI Runtime examples documentation.

## Related Concepts

- Recommendation Systems — The broader domain of algorithms that predict user preferences.
- Deep Learning — The underlying machine learning paradigm used by two-tower models.
- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime that provides the infrastructure for running these example notebooks.
- GPU-accelerated training — Two-tower model training often benefits from GPU resources.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
