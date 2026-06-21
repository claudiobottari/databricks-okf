---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a056d6918e0f12c6788af030590ec547b5b05c7ee33ef669acdbe5e08265024
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-fine-tuning-in-production
    - LFIP
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: LLM Fine-tuning in Production
description: Fine-tuning existing LLMs on custom data to improve performance for specific scenarios, represented as distinct pipeline jobs in production architecture
tags:
  - fine-tuning
  - llm
  - production
timestamp: "2026-06-19T19:12:59.258Z"
---

# LLM Fine-tuning in Production

**LLM Fine-tuning in Production** refers to the process of adapting a pre-trained large language model (LLM) to improve its performance for a specific application or domain, and then deploying that customized model into a production environment. This approach is common in LLMOps workflows because training LLMs from scratch is expensive and time-consuming. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Overview

Fine-tuning allows organizations to leverage existing, pre-trained foundation models and customize them using their own data. This is particularly important for LLM-based applications where general-purpose models may not perform adequately on domain-specific tasks. The fine-tuning process and subsequent model deployment are typically represented as distinct, separate pipelines in the production architecture. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## The Fine-tuning Pipeline

In a production LLMOps workflow, fine-tuning is a dedicated pipeline that takes a pre-trained model from a [Model Hub](/concepts/model-hub-in-llmops.md) and adapts it using domain-specific training data. The pipeline produces a fine-tuned model artifact that can then be evaluated and deployed. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Model Selection

LLM applications often use existing, pretrained models selected from an internal or external model hub. The model can be used as-is or fine-tuned. Databricks includes a selection of high-quality, pre-trained foundation models in [Unity Catalog](/concepts/unity-catalog.md) and in Databricks Marketplace. These pre-trained models provide state-of-the-art AI capabilities, saving the time and expense of building custom models from scratch. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Validation Before Deployment

Validating a fine-tuned model before deploying it to production is often a manual process. This validation step is critical to ensure the fine-tuned model meets quality and safety requirements before serving user traffic. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Production Architecture for Fine-tuned Models

### RAG with a Fine-tuned Open Source Model

A common production architecture involves fine-tuning an open source model and deploying it as part of a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) application. In this architecture:

- The fine-tuned model is served through [Model Serving](/concepts/model-serving.md), which provides a unified interface to deploy, govern, and query AI models.
- An optional Vector Index (such as Databricks AI Search) enables fast similarity searches to provide context or domain knowledge in LLM queries.
- The vector index can be replaced by directly querying the LLM through the Model Serving endpoint.

^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Foundation Model Fine-tuning on Databricks

Databricks provides [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md), which lets you use your own data to customize an existing LLM to optimize its performance for your specific application. This service handles the infrastructure complexity of training large models, allowing teams to focus on data preparation and model evaluation. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Monitoring and Evaluation

### Human Feedback Loops

Human feedback loops are essential in most LLM applications. After deploying a fine-tuned model, human feedback should be managed like other data and ideally incorporated into monitoring based on near real-time streaming. The [MLflow Review App](/concepts/mlflow-review-app.md) helps gather feedback from human reviewers to continuously assess and improve model performance. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- [LLMOps](/concepts/large-language-models-llms-on-databricks.md) — The operational practices for managing LLM applications throughout their lifecycle.
- MLOps Workflows — The broader MLOps framework that LLMOps builds upon.
- [Model Hub](/concepts/model-hub-in-llmops.md) — Central repository for selecting pre-trained models for fine-tuning.
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — Databricks' managed service for customizing LLMs.
- [Model Serving](/concepts/model-serving.md) — Infrastructure for deploying and querying AI models in production.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Common architecture pattern for LLM applications.
- Vector Index — Enables similarity search for providing context to LLM queries.
- Human Feedback in MLflow — Tools for incorporating human evaluation into monitoring.

## Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
