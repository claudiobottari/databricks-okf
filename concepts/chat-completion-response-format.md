---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44cc76a17ea6ae47b7ad7fa7f4fc286328184f3beb4e86b1196a439ce7860131
  pageDirectory: concepts
  sources:
    - query-a-chat-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chat-completion-response-format
    - CCRF
  citations:
    - file: query-a-chat-model-databricks-on-aws.md
title: Chat Completion Response Format
description: Standard structure of responses from Databricks chat model endpoints, including choices, usage tokens, and metadata.
tags:
  - databricks
  - api
  - response-format
timestamp: "2026-06-19T20:01:30.975Z"
---

# Chat Completion Response Format

The **Chat Completion Response Format** defines the structure of the JSON response returned by Databricks model serving endpoints when querying foundation models optimized for chat and general purpose tasks. This format is consistent across both Databricks-hosted foundation models (via [Foundation Models APIs](/concepts/foundation-model-apis.md)) and externally hosted models (via [External Models](/concepts/external-models.md)). ^[query-a-chat-model-databricks-on-aws.md]

## Standard Response Structure

When a chat completion request is made using the REST API, the endpoint returns a JSON object with the following top-level fields:

- `model` — The name of the model used to generate the response (e.g., `databricks-claude-sonnet-4-5`).
- `choices` — An array of response choices, each containing a `message` object, an `index` value, and a `finish_reason`.
- `usage` — An object containing token usage statistics.
- `object` — The object type, typically `chat.completion`.
- `id` — A unique identifier for the completion (may be `null`).
- `created` — A Unix timestamp indicating when the response was generated.

## Example Response

A typical response for a chat completion request looks like the following:

```json
{
  "model": "databricks-claude-sonnet-4-5",
  "choices": [
    {
      "message": {},
      "index": 0,
      "finish_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 7,
    "completion_tokens": 74,
    "total_tokens": 81
  },
  "object": "chat.completion",
  "id": null,
  "created": 1698824353
}
```

^[query-a-chat-model-databricks-on-aws.md]

## Fields in Detail

### `choices`
An array of response options. Each choice contains:
- `message` — The generated response message content, following the same structure as input messages (with `role` and `content` fields).
- `index` — The zero-based index of this choice among all returned choices.
- `finish_reason` — The reason the model stopped generating tokens (e.g., `stop`, `length`, `null` if still in progress).

### `usage`
Provides token count information for cost tracking and monitoring:
- `prompt_tokens` — The number of tokens in the input prompt.
- `completion_tokens` — The number of tokens in the generated response.
- `total_tokens` — The sum of prompt and completion tokens.

## Query Request Format

For reference, the corresponding request format for chat models uses the `messages` array to provide conversation context:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "What is a mixture of experts model?"
    }
  ],
  "max_tokens": 100,
  "temperature": 0.1
}
```

When using external models, additional parameters valid for a given provider and endpoint configuration may be included. See [External Models](/concepts/external-models.md) for details on extra query parameters. ^[query-a-chat-model-databricks-on-aws.md]

## Client-Specific Responses

Different client options produce the same underlying response structure but may wrap it differently:

- **OpenAI Client**: When using the [Databricks OpenAI client](/concepts/databricks-openai-client-for-embeddings.md) or the standard OpenAI client, the response object exposes the same fields via attributes (e.g., `response.choices`, `response.usage`).
- **REST API**: Returns the raw JSON structure shown above.
- **MLflow Deployments SDK**: Returns the response in the MLflow-compatible format.
- **Databricks Python SDK**: Returns the response as a Python object matching the JSON structure.

## Related Concepts

- Chat Completion Request Format — The input format for chat model queries.
- [Foundation Models APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation model endpoints.
- [External Models](/concepts/external-models.md) — Foundation models hosted outside of Databricks.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The infrastructure serving these models.
- [Token Usage Tracking](/concepts/mlflow-token-usage-tracking.md) — Monitoring and cost management for model invocations.

## Sources

- query-a-chat-model-databricks-on-aws.md

# Citations

1. [query-a-chat-model-databricks-on-aws.md](/references/query-a-chat-model-databricks-on-aws-0a958863.md)
