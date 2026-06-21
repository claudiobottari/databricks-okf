---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e1d9ea73672a693dc44bd5998287e76b0104b596f3fdb490f6ed8e2943ca0be
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - text-embedding-models-for-semantic-search
    - TEMFSS
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Text Embedding Models for Semantic Search
description: Models like Qwen3-Embedding, GTE, and BGE that map text to dense vector representations for retrieval, clustering, classification, and semantic similarity tasks, often used to power RAG pipelines.
tags:
  - embeddings
  - semantic-search
  - rag
timestamp: "2026-06-19T14:51:14.201Z"
---

# Text Embedding Models for Semantic Search

**Text Embedding Models for Semantic Search** are machine learning models that encode text into dense vector representations (embeddings) that capture semantic meaning rather than surface-level lexical features. These embeddings enable similarity-based retrieval, clustering, classification, and other semantic understanding tasks by measuring the distance or angle between vectors in a high-dimensional space.

## Overview

Text embedding models map text of any length to a fixed-dimensional vector, typically in the range of 512 to 1024 dimensions. The resulting vectors can be stored in vector indexes and used to find text snippets that are semantically similar to a query, even when the query and the target text share no common keywords. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Embedding models are especially effective when used in tandem with [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) use cases. The embedding model retrieves relevant text snippets from a large document corpus, and those snippets are then included in the prompt context of an LLM to ground its responses in factual information. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Available Foundation Model API Endpoints

Databricks' Foundation Model APIs provide pay-per-token access to several text embedding models. These endpoints are hosted within the Databricks security perimeter and can be used for retrieval, similarity search, clustering, and classification tasks.

### Qwen3-Embedding-0.6B

The Qwen3-Embedding-0.6B model is a compact text embedding model with approximately 600 million parameters, developed by Alibaba Cloud. It encodes text into dense vectors that represent meaning rather than surface form. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

The model supports over 100 languages (including code) and handles long contexts of up to approximately 32,000 tokens, making it suitable for embedding long documents. It produces embeddings with a configurable dimensionality up to 1024 and is instruction-aware, allowing task-specific biasing through prompts. Built on a transformer encoder and fine-tuned specifically for embedding generation, Qwen3-Embedding-0.6B balances embedding quality with efficient inference. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### GTE Large (En)

The General Text Embedding (GTE) model, developed by Alibaba's NLP team, maps any text to a 1024-dimension embedding vector with an embedding window of 8192 tokens. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

This endpoint serves the English version of the model. Note that it does not generate normalized embeddings, so cosine similarity calculations may require manual normalization depending on the downstream use case. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### BGE Large (En)

The BAAI General Embedding (BGE) model, developed by the Beijing Academy of Artificial Intelligence, maps any text to a 1024-dimension embedding vector with an embedding window of 512 tokens. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

This endpoint serves the English version of the model and generates normalized embeddings, making it directly compatible with cosine similarity for retrieval. For RAG applications, the BGE authors recommend including the instruction `"Represent this sentence for searching relevant passages:"` for query embeddings to potentially improve retrieval performance, though its impact is domain-dependent. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Embedding Dimensionality and Token Windows

Different embedding models use different output dimensionalities and maximum input token counts. When selecting an embedding model for a Vector Index or Vector Database, practitioners must consider the trade-off between embedding quality (often higher with more dimensions) and storage/retrieval performance (more efficient with fewer dimensions). Similarly, the token window determines the maximum length of a single text chunk that can be embedded in one call.

## Use Cases

Text embedding models support a wide range of semantic tasks: ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

- **Retrieval** — Finding relevant documents or passages from a corpus based on a natural language query.
- **Semantic Search** — Searching by meaning rather than keyword overlap.
- **Clustering** — Grouping documents by thematic similarity.
- **Classification** — Assigning categories to text based on embedding proximity to labeled examples.
- **Question Answering** — Identifying the most relevant passage to answer a question.
- **Cross-Lingual Retrieval** — For multilingual models like Qwen3-Embedding-0.6B, retrieving documents in one language from a query in another.

## Integrating with Retrieval Augmented Generation (RAG)

In a typical [RAG Pipeline](/concepts/rag-pipeline-txtai.md), the embedding model is used to index a document corpus by computing and storing embeddings for each chunk. At query time, the same model encodes the user's question, and a nearest-neighbor search against the stored embeddings returns the most semantically relevant passages. These passages are then inserted into the prompt context of an LLM to generate a grounded answer. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service through which these embedding models are accessed.
- Vector Index — A data structure that enables efficient nearest-neighbor search over embeddings.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — The primary application pattern for text embedding models with LLMs.
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — The companion models used to generate text from retrieved context.
- Embedding Normalization — Whether the model outputs unit vectors, affecting distance metric choice.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
