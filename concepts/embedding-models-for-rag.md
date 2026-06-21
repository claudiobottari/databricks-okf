---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e5c7df8443a9a5b22a04dad2ce6ac6dfb242f691fe222b8997b71539eee5957
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - embedding-models-for-rag
    - EMFR
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Embedding Models for RAG
description: Text embedding models like GTE, BGE, and Qwen3-Embedding that map text to dense vectors for semantic search, retrieval, and RAG use cases, available alongside generative LLMs in Foundation Model APIs.
tags:
  - databricks
  - embeddings
  - rag
  - vector-search
timestamp: "2026-06-19T09:52:25.212Z"
---

# Embedding Models for RAG

**Embedding Models for RAG** are specialized neural network models that convert text inputs into dense vector representations, capturing semantic meaning rather than surface form. In [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) pipelines, these models are used to index a knowledge base and retrieve relevant document snippets for inclusion in an LLM’s context, improving factuality and reducing hallucination. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Overview

Embedding models map arbitrary text to fixed‑dimensional vectors. By measuring the vector similarity (e.g., cosine distance) between a query and pre‑computed document embeddings, a RAG system can quickly identify the most relevant passages. Databricks Foundation Model APIs offer several embedding models that are designed for semantic tasks such as retrieval, similarity search, clustering, classification, and question answering. These models are “especially effective when used in tandem with LLMs for retrieval augmented generation (RAG) use cases.” ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Available Embedding Models on Databricks

Databricks provides three embedding models through its pay‑per‑token endpoints. The table below summarizes their key characteristics.

| Model | Parameters | Max Input Tokens | Output Dimensions | Normalization | Language Support | Instruction‑Aware |
|-------|------------|------------------|-------------------|---------------|------------------|-------------------|
| Qwen3‑Embedding‑0.6B | ~600 M | ~32K | Configurable up to 1024 | Not specified | 100+ languages and code | Yes |
| GTE Large (En) | Not specified | 8,192 | Fixed 1024 | No | English only | No |
| BGE Large (En) | Not specified | 512 | Fixed 1024 | Yes (normalized) | English only | Recommended via instruction |

All three models accept text input and produce dense vectors that can be stored in a vector index for efficient retrieval. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Qwen3‑Embedding‑0.6B

This compact model (approximately 600 million parameters) is built on a transformer encoder and fine‑tuned specifically for embedding generation. It supports over 100 languages (including code) and can handle long contexts up to about 32K tokens. Qwen3‑Embedding‑0.6B is instruction‑aware, allowing task‑specific biasing through prompts. Its output dimensionality is configurable up to 1024, balancing quality with inference efficiency. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### GTE Large (En)

General Text Embedding (GTE) Large is an English‑only model that maps text to a fixed 1024‑dimensional vector. It has an embedding window of 8,192 tokens and does **not** generate normalized embeddings. GTE is well‑suited for RAG pipelines that require larger context windows per document segment. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### BGE Large (En)

BAAI General Embedding (BGE) Large is an English‑only model that produces 1024‑dimensional, normalized embeddings. It has a shorter embedding window of 512 tokens, making it best suited for short‑passage retrieval. The BGE authors recommend including the instruction `"Represent this sentence for searching relevant passages:"` for query embeddings to improve retrieval performance, though its impact is domain‑dependent. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Best Practices for RAG

- **Choose the right model for your context length.** If your documents contain long paragraphs, models with larger context windows (Qwen3‑Embedding‑0.6B or GTE Large) may perform better. For short, dense passages, BGE Large’s normalized embeddings can simplify similarity computations. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Leverage instruction‑aware models.** When using Qwen3‑Embedding‑0.6B, provide a task‑specific prompt (e.g., “Retrieve relevant passages about …”) to bias the embedding space toward your use case. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Consider normalization.** BGE produces normalized embeddings by default, which can simplify distance calculations. If you use GTE Large, you may need to normalize embeddings manually if your distance metric assumes unit vectors. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Test query‑side instructions.** For BGE, empirically evaluate whether prefixing queries with the recommended instruction improves retrieval accuracy in your domain. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- Vector Search
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Text Embedding](/concepts/text-embedding-models.md)
- Semantic Search
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md)

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
