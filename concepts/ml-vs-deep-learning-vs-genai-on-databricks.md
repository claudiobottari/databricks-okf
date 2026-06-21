---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca7c6e253c9c2ad77bf5790123c8b34dafa68147590ad5f87a8608dc4c5bdd59
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-vs-deep-learning-vs-genai-on-databricks
    - MVDLVGOD
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: ML vs Deep Learning vs GenAI on Databricks
description: The relationship and shared platform support between classic ML, deep learning, and generative AI paradigms on Databricks
tags:
  - machine-learning
  - deep-learning
  - generative-ai
timestamp: "2026-06-19T14:22:24.263Z"
---

# ML vs Deep Learning vs GenAI on Databricks

**ML vs Deep Learning vs GenAI on Databricks** describes the relationship between machine learning (ML), deep learning (DL), and generative AI (GenAI) on the Databricks platform, along with the shared infrastructure and tools that support all three paradigms.

## Overview

The boundaries between machine learning, deep learning, and generative AI can be fuzzy. Modern deep learning and generative AI methods are technically types of ML, but each paradigm has distinct characteristics and use cases. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

- **Classic Machine Learning (ML):** Includes techniques like classification, regression, anomaly detection, forecasting, and recommendation. Typically uses structured data and algorithms such as random forests, gradient boosting, and linear models. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]
- **Deep Learning (DL):** A subset of ML that uses multi-layered neural networks to model complex patterns. Often applied to unstructured data like images, audio, and text. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]
- **Generative AI (GenAI):** A further subset of deep learning focused on generating new content — text, images, code, or audio — based on learned patterns from training data. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Shared Platform Features

Databricks provides a unified platform with features that support all three paradigms: ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

| Feature | Description |
|---------|-------------|
| [Model Serving](/concepts/model-serving.md) | Supports classic ML, deep learning, and custom GenAI models for both real-time and batch inference. |
| [`ai_query`](/docs/aws/en/large-language-models/ai-query#custom-model) | Supports SQL queries and batch inference workloads for all three paradigms. |
| [AI Runtime](/concepts/ai-runtime.md) and GPU-enabled [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) | Support training and fine-tuning across all three paradigms. |
| [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) | Tracks runs and experiments for all three paradigms. |
| Databricks AI Search | Serves unstructured data for all three paradigms. |

## Related Concepts

- Concepts: Data science and machine learning on Databricks
- Concepts: Generative AI on Databricks
- Machine Learning Lifecycle
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md)
- GPU Scheduling

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
