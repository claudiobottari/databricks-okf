---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0e7bc853c5d9213f0b7ff9c3a89275392e948833fa071eec3d9a99f8a32d029
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-platform-features-for-ml-deep-learning-and-genai
    - GenAI and Shared Platform Features for ML, Deep Learning,
    - SPFFMDLAG
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: Shared Platform Features for ML, Deep Learning, and GenAI
description: Databricks platform features — Model Serving, ai_query, AI Runtime, MLflow experiment tracking, and AI Search — that support classic ML, deep learning, and generative AI under a unified infrastructure.
tags:
  - machine-learning
  - deep-learning
  - genai
  - platform
timestamp: "2026-06-19T17:50:02.091Z"
---

## Shared Platform Features for ML, Deep Learning, and GenAI

Machine learning (ML), deep learning (DL), and generative AI (GenAI) share overlapping infrastructure and governance requirements. Databricks provides a unified platform with a set of features that support all three paradigms, enabling consistent experiment management, deployment, and monitoring across the full spectrum of AI workloads. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Model Serving

[Model Serving](/concepts/model-serving.md) supports classic ML, deep learning, and custom GenAI models for both real-time and batch inference. It provides a consistent endpoint interface, allowing teams to deploy and scale any model type without changing infrastructure. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### `ai_query` Function

The [`ai_query`](https://docs.databricks.com/aws/en/large-language-models/ai-query#custom-model) function enables SQL users to call models, including custom models, directly from queries. It supports batch inference workloads for all three paradigms, bridging the gap between data engineering and model consumption. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### AI Runtime and GPU-Enabled Databricks Runtime for Machine Learning

[AI Runtime](/concepts/ai-runtime.md) and GPU-enabled [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) provide optimized environments for training and fine-tuning. These runtimes include pre-installed libraries, kernel tuning, and GPU drivers that support ML, deep learning, and GenAI workloads. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### MLflow Experiment Tracking

[MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) logs runs and experiments for all three paradigms, enabling consistent experiment management, comparison, and reproducibility. Teams can use the same tracking API regardless of whether they are training a random forest, a transformer, or a large language model. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Databricks AI Search

Databricks AI Search serves unstructured data for all three paradigms, providing a single search infrastructure for AI applications such as retrieval-augmented generation (RAG), document retrieval, and semantic search. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [ML Lifecycle](/concepts/ml-lifecycle.md) – End-to-end journey from raw data to production models.
- [ML Platform](/concepts/ml-platform.md) – Combined infrastructure, tooling, and governance for ML.
- [Unity Catalog](/concepts/unity-catalog.md) – Unified governance of data and ML assets.
- [Model Serving](/concepts/model-serving.md) – Deployment infrastructure for real-time and batch inference.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime for ML workloads.
- [AI Runtime](/concepts/ai-runtime.md) – Specialized runtime for AI workloads.

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
