---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abedea46f17ca4fddca5c973eea77db15b80de4a1f1fccf9c3a949d580338817
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-and-databricks-runtime-for-machine-learning
    - Databricks Runtime for Machine Learning and AI Runtime
    - ARADRFML
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: AI Runtime and Databricks Runtime for Machine Learning
description: Customizable training environments with GPU support that enable training and fine-tuning across classic ML, deep learning, and GenAI paradigms on Databricks.
tags:
  - infrastructure
  - runtime
  - training
timestamp: "2026-06-19T09:21:38.211Z"
---

---
title: AI Runtime and Databricks Runtime for Machine Learning
summary: AI Runtime and GPU-enabled Databricks Runtime for Machine Learning are pre-configured environments on Databricks that support training and fine-tuning across machine learning, deep learning, and generative AI.
sources:
  - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:09:54.678Z"
updatedAt: "2026-06-18T08:09:54.678Z"
tags:
  - databricks
  - runtime
  - machine-learning
  - deep-learning
  - generative-ai
aliases:
  - ai-runtime-and-databricks-runtime-for-machine-learning
  - ARDMRML
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# AI Runtime and Databricks Runtime for Machine Learning

**AI Runtime** and **GPU-enabled Databricks Runtime for Machine Learning** are the two primary pre-configured runtime environments on the Databricks platform that support training and fine-tuning workloads across classical machine learning (ML), deep learning (DL), and generative AI (GenAI).^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Both runtimes bundle the necessary libraries, frameworks, and GPU drivers to run distributed training, model tuning, and inference experiments. They are designed to work with [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) for logging runs, [Model Serving](/concepts/model-serving.md) for deployment, and ai_query for SQL-based batch inference.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## AI Runtime

AI Runtime is a purpose-built runtime for generative AI and deep learning workloads. It includes optimizations for large language model (LLM) training, fine-tuning, and serving. It is the recommended runtime for users building and deploying GenAI agents and custom models on Databricks.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Databricks Runtime for Machine Learning

Databricks Runtime for Machine Learning (Databricks Runtime ML) is the standard runtime for classical ML and deep learning tasks. The GPU-enabled version provides pre-installed GPU drivers, CUDA, and popular libraries (e.g., TensorFlow, PyTorch, scikit-learn, XGBoost) for training and inference on GPU clusters.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Shared Capabilities

Both runtimes support training and fine-tuning across ML, deep learning, and GenAI. They are integrated with other platform features:

- [Model Serving](/concepts/model-serving.md) – Deploy models for real-time or batch inference.
- ai_query – Run batch inference over SQL queries.
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – Track runs and compare results.
- Databricks AI Search – Serve unstructured data for retrieval-augmented generation (RAG) and other use cases.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Choosing Between the Two

- **Use AI Runtime** when your primary focus is generative AI, LLM fine-tuning, or building GenAI agents.
- **Use GPU-enabled Databricks Runtime for Machine Learning** when working with traditional deep learning models (e.g., CNNs, RNNs, transformers for non-generative tasks) or classical ML algorithms that benefit from GPU acceleration.

Both runtimes are available on GPU-enabled clusters across all major cloud providers. See GPU Scheduling for best practices on resource allocation.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- Machine Learning Lifecycle
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md)
- [Generative AI on Databricks](/concepts/ai-runtime-ai-v5-on-databricks.md)
- GPU Scheduling
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
