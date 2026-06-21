---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf9d7674307ba8a3e75897a0c6c708de134419c8c4b6a0c20c1d79068a52f985
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - completions-api-databricks
    - CA(
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Completions API (Databricks)
description: Text completion API for single prompts supporting batched inputs of multiple independent prompts in one request.
tags:
  - api
  - text-generation
timestamp: "2026-06-19T18:55:11.952Z"
---

# Completions API (Databricks)

The **Completions API** is a REST API endpoint in Databricks Foundation Model APIs designed for text completion tasks. It generates responses to a single prompt and supports batched inputs, allowing multiple independent prompts to be sent in a single request. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Overview

Unlike the [Chat Completions API (Databricks)](/concepts/chat-completions-api-databricks.md) which is designed for multi-turn conversations, the Completions API handles single-turn text generation from a prompt. It is part of Databricks's suite of [Foundation Model APIs](/concepts/foundation-model-apis.md), which are designed to be similar to OpenAI's REST API to make migrating existing projects easier. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Endpoint

The Completions API can be accessed via the standard serving endpoint invocation path:

```
POST /serving-endpoints/{name}/invocations
```

^[foundation-model-rest-api-reference-databricks-on-aws.md]

Both pay-per-token and provisioned throughput endpoints accept the same REST API request format. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Completion Request

A completion request includes a prompt and optional parameters to control the model's output. Multiple independent prompts can be batched together in one request. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Completion Response

The response contains one or more completion choices, depending on the number of prompts sent in the request. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `CompletionChoice`

Each completion choice represents a generated response for one of the input prompts. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Usage Information

Responses include a `usage` sub-message that reports the number of tokens in the request and response. The format of this sub-message is consistent across all task types in the Foundation Model APIs. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

For models like `databricks-meta-llama-3-3-70b-instruct`, a user prompt is transformed using a prompt template before being passed into the model. `prompt_tokens` includes all text added by the server. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The overarching API suite that includes the Completions API.
- [Chat Completions API (Databricks)](/concepts/chat-completions-api-databricks.md) — The multi-turn conversation counterpart to the Completions API.
- [Embeddings API (Databricks)](/concepts/embeddings-api-databricks.md) — Another task-specific API in the Foundation Model APIs suite.
- [Responses API (Databricks)](/concepts/responses-api-databricks.md) — A newer API for multi-turn conversations with OpenAI models.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — The infrastructure that hosts and serves foundation models.

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
