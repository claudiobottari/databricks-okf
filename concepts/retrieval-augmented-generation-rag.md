---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5057ea9b81f4fb6b424b1d507ef1bc4b2fac8ed7f1b3996763a46ecd2c6bcf45
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retrieval-augmented-generation-rag
    - RAG(
    - RAG
    - RAG (Retrieval Augmented Generation)
    - RAG (Retrieval-Augmented Generation)
    - RAG|retrieval-augmented generation
    - Retrieval Augmented Generation
    - Retrieval-Augmented Generation
    - Retrieval-augmented generation
    - retrieval-augmented generation
    - Retrieval-augmented generation pipeline
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Retrieval Augmented Generation (RAG)
description: A technique recommended across all supported models to improve factual accuracy by retrieving relevant context from external sources and injecting it into the model prompt.
tags:
  - llm
  - accuracy
  - pattern
timestamp: "2026-06-19T14:51:17.003Z"
---

# Retrieval Augmented Generation (RAG)

**Retrieval Augmented Generation (RAG)** is a technique that enhances large language model (LLM) outputs by grounding them in external, retrieved knowledge. Rather than relying solely on the model's internal parameters, RAG systems first search a knowledge store (such as a vector database or document corpus) for relevant information, then incorporate that retrieved context into the model's prompt before generating a response.

## Overview

RAG addresses a fundamental limitation of LLMs: they can produce plausible-sounding but factually incorrect or hallucinated information. Because LLMs have no built-in mechanism to verify facts, their outputs may omit details or contain falsehoods. Databricks recommends using RAG in any scenario where accuracy is especially important. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

By supplying the model with real, retrieved documents at inference time, RAG provides two main benefits:

- **Grounding in facts** – The model can draw on actual source material rather than guessing from its training distribution.
- **Transparency** – Outputs can be traced back to specific retrieved passages, making verification easier.

## How RAG Works

A typical RAG system follows a two-step pipeline:

1. **Retrieval** – A user query is encoded into a vector (using an embedding model) and used to search a pre‑indexed corpus of documents. The system returns the most relevant text snippets.
2. **Generation** – Those snippets are inserted into the LLM's prompt as context. The model then generates a response that cites or paraphrases the retrieved information.

Embedding models such as GTE Large (En) and BGE Large (En) are particularly effective for the retrieval step, as they map text to dense vectors that capture semantic meaning. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## When to Use RAG

RAG is recommended whenever application accuracy is critical. This includes:

- **Enterprise question answering** over internal documents
- **Customer support agents** that must provide verified answers
- **Legal or compliance workflows** where hallucination is unacceptable
- **Research assistants** that need to summarize from specific sources
- **Any deployment** where the cost of a single false fact is high

Almost every model listed in the Databricks Foundation Model APIs documentation carries the same note: *output may omit some facts and occasionally produce false information; use retrieval augmented generation (RAG) in scenarios where accuracy is especially important.* ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Retrieval Components

RAG systems typically rely on an [embedding model](/concepts/text-embedding-models.md) to convert documents and queries into fixed‑length vectors. These vectors are then stored in a vector index for fast similarity search. Databricks offers several embedding models through its Foundation Model APIs:

- **GTE Large (En)** – Maps text to 1024‑dimensional vectors with an embedding window of 8192 tokens. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **BGE Large (En)** – Produces normalized 1024‑dimensional embeddings with a 512‑token window. The BGE authors suggest appending an instruction parameter (e.g., `"Represent this sentence for searching relevant passages:"`) to improve retrieval quality. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Both models are described as "especially effective when used in tandem with LLMs for retrieval augmented generation (RAG) use cases." ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The hosted model endpoints that support RAG workflows.
- Vector index – The data structure used for efficient similarity search in RAG pipelines.
- [Embedding model](/concepts/text-embedding-models.md) – The model class that converts text into vectors for retrieval.
- Hallucination – The problem RAG is designed to mitigate.
- [Retrieval-augmented generation pipeline](/concepts/retrieval-augmented-generation-rag.md) – End‑to‑end architecture for building RAG applications.
- ChatGPT Enterprise RAG – Example of RAG patterns in production use.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
