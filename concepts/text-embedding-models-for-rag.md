---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c217a5efd3a5c59102ae58831e092d32833ef57e04e0281a7ff5deb7f757823b
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - text-embedding-models-for-rag
    - TEMFR
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Text Embedding Models for RAG
description: Embedding models like GTE Large, BGE Large, and Qwen3-Embedding available via Databricks APIs that map text to dense vectors for semantic search, retrieval, clustering, and classification, often used with LLMs for RAG.
tags:
  - embeddings
  - rag
  - vector-search
  - semantic-search
timestamp: "2026-06-19T18:13:31.457Z"
---

Here is the wiki page for "Text Embedding Models for RAG".

---

## Text Embedding Models for RAG

**Text Embedding Models** are neural network models that map text inputs (words, sentences, or documents) into dense vector representations, known as embeddings. These vectors capture semantic meaning, allowing systems to measure the similarity between different pieces of text. In a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) pipeline, an embedding model is used to convert a user's query into a vector and then search a vector index to find the most semantically relevant text chunks from a knowledge base. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Embedding models are especially effective when used in tandem with LLMs for RAG use cases. They can be used to find relevant text snippets in large chunks of documents that can then be placed into the context of an LLM. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Available Models on Databricks

Databricks Foundation Model APIs provide several text embedding models that can be used for RAG workflows. These are available as pay-per-token endpoints. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

#### GTE Large (En)

The **General Text Embedding (GTE)** model maps any text to a 1024-dimension embedding vector with an embedding window of 8192 tokens. These vectors are used in vector indexes for LLMs and for tasks like retrieval, classification, question-answering, clustering, or semantic search. The endpoint serves the English version of the model and does not generate normalized embeddings. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

#### BGE Large (En)

The **BAAI General Embedding (BGE)** model maps any text to a 1024-dimension embedding vector with an embedding window of 512 tokens. Like GTE, its vectors are used in vector indexes for tasks including retrieval, classification, and semantic search. This endpoint serves the English version of the model and generates normalized embeddings. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

In RAG applications, the BGE authors recommend including an instruction parameter to improve retrieval performance. For query embeddings, they suggest trying the instruction `"Represent this sentence for searching relevant passages:"`, though its performance impact is domain dependent. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

#### Qwen3-Embedding-0.6B

The **Qwen3-Embedding-0.6B** model is a compact text embedding model with approximately 600 million parameters. It encodes text into dense vectors for semantic tasks like retrieval, similarity search, clustering, and classification. The model supports over 100 languages (including code) and handles long contexts up to roughly 32K tokens, making it suitable for embedding long documents. It produces embeddings with a configurable dimensionality up to 1024 and is instruction-aware, allowing task-specific biasing through prompts. Built on a transformer encoder and fine-tuned specifically for embedding generation, Qwen3-Embedding-0.6B balances embedding quality with efficient inference. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- Vector Index
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- Semantic Search
- BAAI General Embedding (BGE)
- General Text Embedding (GTE)

### Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
