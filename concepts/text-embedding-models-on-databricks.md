---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9a42ecc7aa564042fe78d275ad4f9fb88fe5d03330aa1d7d741449de462b688
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - text-embedding-models-on-databricks
    - TEMOD
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Text Embedding Models on Databricks
description: A class of models (GTE, BGE, Qwen3-Embedding) available on Databricks for converting text into dense vector representations used in semantic search, clustering, and RAG pipelines.
tags:
  - embeddings
  - vector-search
  - rag
  - databricks
timestamp: "2026-06-18T15:07:41.499Z"
---

# Text Embedding Models on Databricks

**Text Embedding Models on Databricks** refers to the text embedding models available through [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) that convert text into dense vector representations. These embeddings capture semantic meaning and can be used for tasks such as retrieval, similarity search, clustering, classification, and [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md).

## Overview

Databricks provides access to several text embedding models through its Foundation Model APIs. These models encode text into fixed-dimensional vectors that represent meaning rather than surface form, enabling semantic search and comparison across large document collections. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Embedding models are especially effective when used in tandem with LLMs for RAG use cases. They can find relevant text snippets in large document collections that can then be provided as context to a large language model. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Available Models

### Alibaba Cloud Qwen3-Embedding-0.6B

**Endpoint name**: `databricks-qwen3-embedding-0-6b`

**Supported inputs**: text

Qwen3-Embedding-0.6B is a compact text embedding model with approximately 600 million parameters, designed for semantic tasks such as retrieval, similarity search, clustering, and classification. It encodes text into dense vectors that represent meaning rather than surface form. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

The model supports over 100 languages (including code) and handles long contexts up to approximately 32K tokens, making it suitable for embedding long documents. It produces embeddings with a configurable dimensionality up to 1024 and is instruction-aware, allowing task-specific biasing through prompts. Built on a transformer encoder and fine-tuned specifically for embedding generation, Qwen3-Embedding-0.6B balances embedding quality with efficient inference. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### GTE Large (En)

**Endpoint name**: `databricks-gte-large-en`

**Supported inputs**: text

General Text Embedding (GTE) is a text embedding model that can map any text to a 1024-dimension embedding vector with an embedding window of 8192 tokens. These vectors can be used in vector indexes for LLMs, and for tasks like retrieval, classification, question-answering, clustering, or semantic search. This endpoint serves the English version of the model and does not generate normalized embeddings. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### BGE Large (En)

**Endpoint name**: `databricks-bge-large-en`

**Supported inputs**: text

BAAI General Embedding (BGE) is a text embedding model that can map any text to a 1024-dimension embedding vector with an embedding window of 512 tokens. These vectors can be used in vector indexes for LLMs, and for tasks like retrieval, classification, question-answering, clustering, or semantic search. This endpoint serves the English version of the model and generates normalized embeddings. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

In RAG applications, you may be able to improve the performance of your retrieval system by including an instruction parameter. The BGE authors recommend trying the instruction `"Represent this sentence for searching relevant passages:"` for query embeddings, though its performance impact is domain dependent. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Use Cases

Text embedding models on Databricks support a variety of applications:

- **Retrieval Augmented Generation (RAG)**: Find relevant text snippets in large document collections to provide context to an LLM.
- **Semantic search**: Search documents by meaning rather than keyword matching.
- **Clustering**: Group similar documents based on embedding similarity.
- **Classification**: Use embeddings as features for downstream classifiers.
- **Question answering**: Match questions to relevant passages.
- **Similarity comparison**: Measure semantic similarity between texts.

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API layer for accessing embedding models
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – Primary use case for embedding models
- Vector Search – Using embeddings for similarity search
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) – Full catalog of available models
- [AI Playground](/concepts/ai-playground.md) – Interactive interface for testing models

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
