---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 367dd2f169ca5841cc1ffeca8c65a3e6719c63478b7ff6e551d4dc69d311ac42
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retrieval-augmented-generation-rag-recommendation
    - RAG(R
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Retrieval Augmented Generation (RAG) Recommendation
description: Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important to mitigate the risk of LLMs omitting facts or producing false information.
tags:
  - best-practice
  - llm
  - accuracy
timestamp: "2026-06-18T11:39:04.608Z"
---

# Retrieval Augmented Generation (RAG) Recommendation

**Retrieval Augmented Generation (RAG) Recommendation** is a best practice guidance from Databricks for using retrieval augmented generation (RAG) architectures in scenarios where accuracy is especially important. The recommendation appears consistently across all supported foundation models in the Databricks Foundation Model APIs, emphasizing that even state-of-the-art large language models can produce inaccurate or incomplete outputs. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Overview

RAG is a technique that combines information retrieval with text generation. When a user submits a query, a RAG system first retrieves relevant information from a knowledge base and then feeds that retrieved context to a large language model to generate a grounded response. This approach helps mitigate issues such as hallucination, factual inaccuracy, and outdated knowledge that can occur when relying solely on a model's parametric memory. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

The RAG recommendation is a standard caveat included for every model listed in the Databricks Foundation Model APIs, including models from OpenAI, Google, Anthropic, Alibaba Cloud, and Meta.

## When to Use RAG

Databricks recommends using RAG "in scenarios where accuracy is especially important." ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] These scenarios include:

- **Document reasoning and question answering** — answering questions from large corpora of documents where precise facts must be verified
- **Enterprise agent workflows** — where agents must act on accurate, up-to-date internal data
- **Customer-facing applications** — where incorrect outputs could lead to customer dissatisfaction or compliance issues
- **Regulated industries** — such as finance, healthcare, and legal, where outputs must be traceable to specific sources
- **Complex multi-step reasoning tasks** — where models benefit from having verified facts available in context

## Implementation on Databricks

### Foundation Model APIs

Databricks Foundation Model APIs provide pay-per-token and provisioned throughput endpoints for a range of state-of-the-art models. All supported models can be used within a RAG pipeline by:

1. **Retrieving relevant documents** from a vector database or search index
2. **Augmenting the prompt** with the retrieved context
3. **Sending the augmented prompt** to any supported endpoint for generation

### Embedding Models for Retrieval

Databricks offers embedding models that are especially effective when used in tandem with LLMs for RAG use cases: ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

| Model | Endpoint Name | Embedding Dimension | Context Window | Use Case |
|-------|--------------|---------------------|----------------|----------|
| Qwen3-Embedding-0.6B | `databricks-qwen3-embedding-0-6b` | Up to 1024 | ~32K tokens | Semantic search, clustering, classification; supports 100+ languages |
| GTE Large (En) | `databricks-gte-large-en` | 1024 | 8192 tokens | English text embedding for retrieval and classification |
| BGE Large (En) | `databricks-bge-large-en` | 1024 | 512 tokens | English text embedding; supports instruction parameter for query embedding optimization |

These embedding models can be used to find relevant text snippets in large chunks of documents that can then be supplied as context for an LLM. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### BGE Optimization Tip

For BGE Large (En), the authors recommend trying the instruction `"Represent this sentence for searching relevant passages:"` for query embeddings to improve retrieval performance in RAG applications, though its impact is domain dependent. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Why RAG Is Recommended

All large language models, including state-of-the-art frontier models, share a common limitation: their output "might omit some facts and occasionally produce false information." ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] The RAG recommendation is not specific to any single model provider — it applies equally to:

| Provider | Model Families |
|----------|----------------|
| OpenAI | GPT-5, GPT-5.1, GPT-5.2, GPT-5.3 Codex, GPT-5.4, GPT-5.5, GPT OSS |
| Anthropic | Claude Opus 4.x, Claude Sonnet 4.x, Claude Haiku 4.5, Claude Fable 5 |
| Google | Gemini 2.5, Gemini 3 Flash, Gemini 3.1, Gemini 3.5 Flash |
| Alibaba Cloud | Qwen3.5, Qwen3-Next |
| Meta | Llama 3.1, Llama 3.3, Llama 4 Maverick |

RAG addresses these limitations by grounding model outputs in retrieved, verifiable source material rather than relying solely on the model's internal knowledge.

## Best Practices

- **Use a quality embedding model** for the retrieval step to ensure relevant context is surfaced
- **Configure appropriate chunk sizes and overlap** for document indexing based on the embedding model's context window
- **Consider instruction parameters** when using models like BGE that support task-specific prompt biasing
- **Evaluate retrieval quality** as part of your overall RAG system performance
- **Monitor for factual accuracy** even after implementing RAG — no system is perfect

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API layer for serving supported LLMs on Databricks
- Embedding Models — Models used to convert text into dense vector representations for retrieval
- [AI Playground](/concepts/ai-playground.md) — An interactive environment for experimenting with supported models
- LLM Pipeline Architecture — The broader architecture for deploying LLM-based applications
- Vector Search — The retrieval technique used in RAG to find relevant documents
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — The recommended serving mode for production RAG workloads

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
