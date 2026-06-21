---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: caaa177766b54d1f53e178e5d11b2eecfc5eed6b409be638b79ece40247ef55f
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - embeddings-api-databricks
    - EA(
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Embeddings API (Databricks)
description: API for mapping input strings into embedding vectors with batching support, where instructions are model-specific (e.g., BGE, Qwen3-Embedding, Instructor-XL).
tags:
  - api
  - embeddings
  - nlp
timestamp: "2026-06-19T18:55:02.748Z"
---

# Embeddings API (Databricks)

The **Embeddings API** is a REST API endpoint within the [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) that maps input strings into embedding vectors. It follows a request-response format similar to OpenAI's API to simplify migration of existing projects. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Endpoint

Embedding requests are sent via HTTP POST to the standard serving endpoint invocation URL:

```
POST /serving-endpoints/{name}/invocations
```

^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Embedding Request

The request accepts an `input` field containing one or more strings to embed. Multiple inputs can be batched together in a single request. An optional `instructions` field may be provided, though its usage is highly model-specific. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Instructions by Model

Different embedding models recommend different instruction strategies:

- **BGE models**: No instruction when indexing chunks; use `"Represent this sentence for searching relevant passages:"` for retrieval queries.
- **Qwen3-Embedding**: Use a task-specific instruction such as `"Given a web search query, retrieve relevant passages that answer the query"` for retrieval queries; no instruction when embedding retrieval documents.
- **Instructor-XL**: Supports a wide range of instruction strings.

^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Embedding Response

The response contains a list of embedding objects, one per input string. Each `EmbeddingObject` includes the embedding vector and associated metadata. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Usage Information

Responses include a `usage` sub-message that reports the number of tokens in the request and response. The format of this sub-message is consistent across all task types. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Supported Models

The Embeddings API is available for supported embedding models through both pay-per-token endpoints and provisioned throughput endpoints. Pay-per-token endpoints are preconfigured in each workspace. Provisioned throughput endpoints can be created via the API or the Serving UI and support multiple models per endpoint for A/B testing, as long as all served models expose the same API format. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — The overarching API framework for serving foundation models.
- [Chat Completions API (Databricks)](/concepts/chat-completions-api-databricks.md) — Multi-turn conversation API for chat models.
- [Completions API (Databricks)](/concepts/completions-api-databricks.md) — Text completion API for single-prompt generation.
- [Responses API (Databricks)](/concepts/responses-api-databricks.md) — Multi-turn conversation API for OpenAI models.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — Infrastructure for deploying and querying models.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Dedicated endpoints for production workloads.
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Usage-based pricing for foundation model APIs.

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
