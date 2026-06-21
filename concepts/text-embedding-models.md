---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a46a1b603a543a957a5a0d5d6960cfec324ca2e30c809a5ba696a4d6f5fb87b
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - text-embedding-models
    - TEM
    - Embedding Models
    - Embedding model
    - embedding model
    - Query Embedding Models
    - Query an Embedding Model
    - Query an embedding model
    - Text Embedding
    - embedding-models-for-rag
    - EMFR
    - text-embedding-models-for-rag
    - TEMFR
    - text-embedding-models-for-semantic-search
    - TEMFSS
    - text-embedding-models-on-databricks
    - TEMOD
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Text Embedding Models
description: Compact models like GTE, BGE, and Qwen3-Embedding that map text to dense vector representations for semantic search, retrieval, clustering, and classification tasks, typically used alongside LLMs in RAG pipelines.
tags:
  - embeddings
  - vector-search
  - rag
timestamp: "2026-06-18T11:38:59.770Z"
---

# Text Embedding Models

**Text embedding models** are machine learning models that map natural language text into dense vector representations (embeddings) in a high-dimensional space. These vectors capture semantic meaning, enabling tasks such as retrieval, similarity search, clustering, classification, and question-answering. Embedding models are especially effective when used in tandem with large language models (LLMs) for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) use cases, where they retrieve relevant text snippets from large document collections that are then provided as context to an LLM. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) offer several text embedding models as pay-per-token endpoints. The models described below are hosted within the Databricks security perimeter unless otherwise noted. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Supported Models

### Qwen3-Embedding-0.6B

| Property | Value |
|----------|-------|
| **Endpoint name** | `databricks-qwen3-embedding-0-6b` |
| **Supported inputs** | text |
| **Parameters** | ~600M |
| **Embedding dimensionality** | Configurable up to 1,024 |
| **Context window** | ~32K tokens |
| **Language support** | 100+ languages (including code) |

This compact model is designed for semantic tasks such as retrieval, similarity search, clustering, and classification. It encodes text into dense vectors that represent meaning rather than surface form. Qwen3-Embedding-0.6B is instruction-aware, allowing task-specific biasing through prompts. Built on a transformer encoder and fine-tuned specifically for embedding generation, it balances embedding quality with efficient inference. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### GTE Large (En)

| Property | Value |
|----------|-------|
| **Endpoint name** | `databricks-gte-large-en` |
| **Supported inputs** | text |
| **Embedding dimensionality** | 1,024 |
| **Context window** | 8,192 tokens |
| **Embedding normalization** | Not normalized |

The General Text Embedding (GTE) model by Alibaba Cloud maps text to 1,024‑dimension vectors and can be used in vector indexes for LLMs, retrieval, classification, QA, clustering, or semantic search. This endpoint serves the English version of the model. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### BGE Large (En)

| Property | Value |
|----------|-------|
| **Endpoint name** | `databricks-bge-large-en` |
| **Supported inputs** | text |
| **Embedding dimensionality** | 1,024 |
| **Context window** | 512 tokens |
| **Embedding normalization** | Normalized embeddings |

The BAAI General Embedding (BGE) model maps text into 1,024‑dimension normalized vectors for retrieval, classification, QA, clustering, or semantic search. This endpoint serves the English version of the model. For RAG applications, the BGE authors recommend trying the instruction `"Represent this sentence for searching relevant passages:"` for query embeddings, though its performance impact is domain dependent. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Usage with RAG

Text embedding models are a core component of RAG pipelines. They convert both user queries and document chunks into vectors; a Vector Search engine then retrieves the most semantically similar chunks, which are injected into an LLM prompt to ground the model's response in factual data. Databricks recommends using embedding models in this way to improve accuracy and reduce hallucinations, especially in enterprise applications. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure for these models
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Common use case for embedding models
- Vector Search — Technology for similarity search on embeddings
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) — Assessing retrieval quality with embedding-based metrics
- [Custom Judges](/concepts/custom-judges.md) — Using embeddings to evaluate agent outputs

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
