---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 845a5f352fc6c83dee9555a645fe77cc69c87eff7af201d033e1a29f10e79636
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-recommender-systems-on-databricks
    - DLRSOD
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Deep learning recommender systems on Databricks
description: Examples for building recommendation systems using modern deep learning approaches like two-tower models on AI Runtime.
tags:
  - databricks
  - recommender-systems
  - deep-learning
timestamp: "2026-06-18T14:23:39.827Z"
---

---
title: Deep Learning Recommender Systems on Databricks
summary: Notebook examples and guidance for building recommendation systems with modern deep learning approaches, including two-tower models, using AI Runtime on Databricks.
sources:
  - ai-runtime-example-notebooks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - recommender-systems
  - deep-learning
  - ai-runtime
  - examples
aliases:
  - dl-recsys-databricks
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Deep Learning Recommender Systems on Databricks

**Deep Learning Recommender Systems on Databricks** refers to the set of notebook examples and best practices for building modern recommendation models using [AI Runtime](/concepts/ai-runtime.md). These examples demonstrate how to implement state-of-the-art deep learning approaches — such as two-tower models — within the Databricks environment. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

The Databricks documentation provides a dedicated notebook example for deep learning based recommender systems as part of its [AI Runtime example notebooks](/concepts/ai-runtime-example-notebooks.md). These examples are designed for single-node tasks (currently in Public Preview) and distributed multi-GPU workloads (currently in Beta). ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Notebook Examples

The recommender systems notebook covers **building recommendation systems using modern deep learning approaches like two-tower models**. Two-tower models are a popular architecture that uses two separate neural networks (a query tower and a candidate tower) to learn embeddings for users and items, enabling efficient retrieval and ranking. The notebook provides end-to-end code for training and evaluating such models on Databricks. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

Other AI Runtime example notebooks cover topics such as [large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md), [computer vision](/concepts/computer-vision-on-databricks.md), classic ML, and [multi-GPU distributed training](/concepts/multi-gpu-distributed-training-api.md). ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Key Techniques

- **Two-tower models**: The primary architecture illustrated in the recommender systems notebook. It separates user and item feature processing into two independent towers, then computes similarity scores (e.g., dot product) between their outputs. This design scales well to large candidate pools and supports real-time serving. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Status and Requirements

- **Single-node tasks**: AI Runtime for single-node recommender system training is in Public Preview. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Multi-GPU distributed training**: The distributed training API for multi-GPU workloads remains in Beta. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

Users can run the notebooks on Databricks clusters with appropriate GPU resources. The notebooks are accessible from the Databricks documentation site.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [AI Runtime example notebooks](/concepts/ai-runtime-example-notebooks.md)
- [Two-tower model](/concepts/two-tower-recommendation-model.md)
- Recommender system
- Deep learning
- [Large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- Computer vision
- [Multi-GPU distributed training](/concepts/multi-gpu-distributed-training-databricks.md)
- Public Preview
- Beta

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
