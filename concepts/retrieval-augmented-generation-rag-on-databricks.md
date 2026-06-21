---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 609d9e02de6a3023176e72f3b0e19237df260715e8243882d235da061171ad51
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - retrieval-augmented-generation-rag-on-databricks
    - RAG(OD
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: Retrieval Augmented Generation (RAG) on Databricks
description: A recommended pattern for improving LLM accuracy by retrieving relevant context from documents before generating responses, consistently advised across all Databricks-hosted foundation models.
tags:
  - rag
  - llm
  - databricks
  - best-practice
timestamp: "2026-06-18T15:07:46.344Z"
---

# Retrieval Augmented Generation (RAG) on Databricks

**Retrieval Augmented Generation (RAG)** is an architectural pattern that combines a retrieval step — fetching relevant context from a knowledge base — with a generative large language model (LLM) to improve the factual accuracy and relevance of model outputs. Databricks recommends using RAG in scenarios where accuracy is especially important, as standalone LLM outputs can omit facts or produce incorrect information. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## RAG Architecture on Databricks

Databricks supports two primary production architectures for RAG applications, as documented in the [LLMOps](/concepts/large-language-models-llms-on-databricks.md) reference: one that uses a third-party LLM API and one that uses a self-hosted fine-tuned model. Both architectures include an optional vector database, which can be replaced by directly querying the LLM through the model serving endpoint. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### RAG with a Third-Party LLM API

In this architecture, the RAG pipeline connects to a third-party LLM (e.g., OpenAI, Anthropic) via Databricks External Models. The model serving endpoint acts as the invocation point, adding complexity in latency, credential management, and external API calls. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### RAG with a Fine-Tuned Open Source Model

This architecture fine-tunes an open source model (e.g., Llama, Gemma) on custom data using Databricks Foundation Model Fine-tuning, then deploys the fine-tuned model to a model serving endpoint. The retrieval component is handled by a vector index. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Key Components

### Foundation Models and APIs

Databricks offers a wide selection of pre-trained foundation models through its Foundation Model APIs, including models from OpenAI (GPT-5 series, GPT OSS), Google (Gemini series), Meta (Llama series), and Anthropic (Claude series). Many of these model descriptions explicitly recommend using RAG for accuracy-critical use cases. The APIs support both pay-per-token and provisioned throughput modes. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Vector Index (AI Search)

For the retrieval step, Databricks provides AI Search functionality that allows any Delta table in Unity Catalog to be used as a vector index. The index automatically syncs with the underlying Delta table, enabling fast similarity searches. A model artifact can encapsulate the retrieval logic and provide the returned data as context to the LLM. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Model Serving

[Model Serving](/concepts/model-serving.md) provides a unified interface to deploy, govern, and query AI models. In a RAG pipeline, the serving endpoint handles both the retrieval call and the LLM invocation, whether the LLM is self-hosted or accessed via a third-party API. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Human Feedback in Monitoring

Human feedback loops are essential in RAG applications to assess output quality. Databricks recommends incorporating human feedback into near real-time monitoring pipelines. The MLflow review app facilitates gathering feedback from human reviewers. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Best Practices

- Use RAG when application accuracy is critical, as LLMs can produce hallucinations or omit facts. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- For production workloads, Databricks recommends provisioned throughput mode for Foundation Model APIs. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- Embedding models (e.g., GTE, BGE, Qwen3-Embedding) are especially effective when used in tandem with LLMs for RAG use cases; they can find relevant text snippets from large document collections. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- LLMOps workflows on Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- AI Search
- [Model Serving](/concepts/model-serving.md)
- [MLflow](/concepts/mlflow.md)
- Fine-tuning foundation models
- [Unity Catalog](/concepts/unity-catalog.md)
- Vector Search

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
2. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
