---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 586a4971ac19cc3b76efc746977766185ea9ba315b2eb994f9734e142cdaea01
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - embeddings-api
    - Embeddings
    - Vector embeddings
    - embeddings-api-databricks
    - EA(
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Embeddings API
description: An API endpoint on Databricks for mapping input strings into embedding vectors, supporting batched inputs and model-specific instruction strings.
tags:
  - api
  - embeddings
  - databricks
timestamp: "2026-06-19T10:39:13.996Z"
---

---

title: Embeddings API
summary: API for mapping input strings into embedding vectors, supporting batched inputs and model-specific instructions.
sources:
  - foundation-model-rest-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:25:38.624Z"
updatedAt: "2026-06-18T12:25:38.624Z"
tags:
  - api
  - embeddings
  - vectors
aliases:
  - embeddings-api
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Embeddings API

The **Embeddings API** is a [Foundation Model APIs](/concepts/foundation-model-apis.md) endpoint that maps input strings into embedding vectors. Multiple inputs can be batched together in a single request. The API is designed to be similar to OpenAI's REST API to make migrating existing projects easier. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Endpoint

Embeddings requests are made via HTTP POST to the serving endpoint invocation URL:

```
POST /serving-endpoints/{name}/invocations
```

Parameters for querying the endpoint are defined in the Databricks API reference. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Embedding Request

The request body contains the input strings to embed. Instructions are optional and highly model-specific. For example:

- The BGE authors recommend **no instruction** when indexing chunks and recommend using the instruction `"Represent this sentence for searching relevant passages:"` for retrieval queries.
- The Qwen3-Embedding authors recommend a task-specific instruction such as `"Given a web search query, retrieve relevant passages that answer the query"` for retrieval queries, and no instruction when embedding retrieval documents.
- Other models like Instructor-XL support a wide range of instruction strings. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Embeddings Response

The response contains a list of `EmbeddingObject` entries, each with an embedding vector (array of floating-point numbers) and associated metadata. The exact JSON structure depends on the endpoint's task type. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `EmbeddingObject`

The response also includes a `usage` sub-message reporting token counts for the request and response. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Usage

Responses include a `usage` sub-message that reports `prompt_tokens` and `total_tokens`. For models that use a prompt template (e.g., `databricks-meta-llama-3-3-70b-instruct`), `prompt_tokens` includes all text added by the server, such as system prompts or templates. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Vector embeddings](/concepts/embeddings-api.md) — The mathematical representation of text as a dense vector
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The overarching API family that includes the Embeddings API
- [Chat Completions API](/concepts/chat-completions-api.md) — Another task type for multi-turn conversations
- [Completions API](/concepts/completions-api.md) — Text completion tasks supporting batched prompts
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Custom endpoints for A/B testing or higher throughput
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Preconfigured endpoints for supported models

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
