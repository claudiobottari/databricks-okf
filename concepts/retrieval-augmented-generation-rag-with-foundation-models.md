---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c2cd7bdf294b192289191c83d71f2af2311fce02b6ae1c4cc17b56d50c68474
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retrieval-augmented-generation-rag-with-foundation-models
    - RAG(WFM
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Retrieval Augmented Generation (RAG) with Foundation Models
description: Databricks recommends using retrieval augmented generation (RAG) alongside foundation models to improve factual accuracy and reduce hallucination risks in scenarios where correctness is critical.
tags:
  - rag
  - machine-learning
  - best-practice
timestamp: "2026-06-19T18:13:23.180Z"
---

# Retrieval Augmented Generation (RAG) with Foundation Models

**Retrieval Augmented Generation (RAG)** is a technique that combines a retrieval component with a generative Foundation Model to produce more accurate, factual outputs. Instead of relying solely on the model’s internal knowledge, RAG first retrieves relevant information from an external knowledge base—often using Embedding Models to find semantically similar text snippets—and then injects that retrieved context into the model’s prompt. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Motivation

Large language models (LLMs) and other foundation models may omit facts or occasionally produce false information, a phenomenon often called hallucination. To mitigate this risk, Databricks recommends using RAG in scenarios where accuracy is especially important. RAG grounds the model’s generation in verifiable, up‑to‑date content, reducing the likelihood of incorrect or unsupported outputs. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Role of Embedding Models

RAG relies on embedding models to convert text into dense vector representations. These vectors encode meaning rather than surface form and can be used in [Vector Indexes](/concepts/vector-index-for-llm-applications.md) for tasks such as semantic search, retrieval, classification, and clustering. Databricks offers several embedding models through its Foundation Model APIs: ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

- **Qwen3‑Embedding‑0.6B** — A compact model (~600M parameters) supporting 100+ languages and long contexts up to ~32K tokens. It produces configurable embeddings up to 1024 dimensions and is instruction‑aware.
- **GTE Large (En)** — Maps text to 1024‑dimension vectors with an embedding window of 8192 tokens. This endpoint does *not* generate normalized embeddings.
- **BGE Large (En)** — Maps text to 1024‑dimension vectors with an embedding window of 512 tokens. This endpoint generates normalized embeddings.

All three models can be used to find relevant text snippets in large document collections, which are then fed as context to an LLM as part of a RAG pipeline. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Optimizing Retrieval with Instructions

When using BGE Large in a RAG application, the retrieval system’s performance may be further improved by including an instruction parameter. The BGE authors suggest trying the instruction `"Represent this sentence for searching relevant passages:"` for query embeddings. The actual impact of this instruction is domain‑dependent. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Security and Hosting

RAG can be implemented entirely within the Databricks security perimeter. Foundation Model API endpoints for both generative models and embedding models are hosted by Databricks, keeping data in‑house during retrieval and generation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The pay‑per‑token and provisioned‑throughput endpoints for models on Databricks.
- Embedding Models — Models that produce dense vector representations for text.
- [Vector Indexes](/concepts/vector-index-for-llm-applications.md) — Indexes used to efficiently search embedding vectors.
- LLMs — Large language models that can be augmented via RAG.
- Prompt Engineering — Techniques to structure prompts, including retrieved context.
- Hallucination — A common failure mode of LLMs that RAG helps mitigate.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
