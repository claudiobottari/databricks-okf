---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3294e87b2c094a4f23319741e2a0def9dd80a4ebe876086e2f127a83e2e0b037
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-for-llms
    - MSFL
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: Model Serving for LLMs
description: Unified interface to deploy, govern, and query AI models, including handling external API calls, latency, and credential management for third-party LLM APIs
tags:
  - model-serving
  - llm
  - deployment
timestamp: "2026-06-19T19:13:08.684Z"
---

# Model Serving for LLMs

**Model Serving for LLMs** refers to the deployment infrastructure and architectural patterns used to expose large language models (LLMs) to applications for inference. In the context of [LLMOps](/concepts/large-language-models-llms-on-databricks.md), serving introduces considerations not present in traditional MLOps—particularly when the application uses external or third-party LLM APIs.

## Overview

LLM applications often require real-time or near-real-time inference endpoints. Databricks provides Model Serving as a unified interface to deploy, govern, and query AI models. This platform handles the complexities of exposing models to production traffic, including scaling, security, and monitoring. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

Model Serving endpoints can be used to directly query the LLM, replacing the need for a separate vector database in some architectures. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Architectural Considerations

A key architectural change for LLM applications—especially those using [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) with a third-party API—is that the LLM pipeline makes external API calls from the Model Serving endpoint to internal or third-party LLM APIs. This introduces:

- **Increased complexity** – The serving pipeline must manage external dependencies.
- **Potential latency** – Network round trips to external services add response time.
- **Additional credential management** – Secure handling of API keys and tokens for external services becomes necessary. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

For RAG applications that fine-tune an open source model, the serving endpoint can host the custom model directly, avoiding external API calls while still benefiting from Databricks’ unified serving infrastructure. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Databricks Model Serving

Databricks Model Serving provides a managed serving infrastructure that integrates with [Unity Catalog](/concepts/unity-catalog.md) and supports multiple model flavors, including those logged via MLflow. It can serve:

- Foundation models from Unity Catalog or Databricks Marketplace
- Fine-tuned models created via Foundation Model Fine-tuning
- Custom models packaged in MLflow (e.g., LangChain or PyFunc)

The service handles deployment, autoscaling, and monitoring, and can be used in conjunction with AI Search indexes to provide context-rich responses. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Relationship to External Models

For applications that rely on third-party LLM APIs, Databricks supports [External Models](/concepts/external-models.md)—a feature that allows the Model Serving endpoint to route requests to services like OpenAI or Anthropic while still providing a unified governance and monitoring layer. This is the pattern illustrated in the RAG with third-party LLM architecture. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md)
- MLOps workflows on Databricks
- [Model Serving](/concepts/model-serving.md)
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)
- Vector Index and AI Search
- [External Models](/concepts/external-models.md)
- [Human feedback in MLflow](/concepts/human-feedback-collection-in-mlflow.md) – Monitoring and evaluation loops for served models

## Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
