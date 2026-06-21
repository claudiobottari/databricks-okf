---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 361df79ec62dea4971e4f8d7c1eb773074153fb17084bb291458efca51d38ce7
  pageDirectory: concepts
  sources:
    - query-a-chat-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rest-api-for-model-serving
    - RAFMS
  citations:
    - file: query-a-chat-model-databricks-on-aws.md
title: REST API for Model Serving
description: Direct HTTP requests to Databricks model serving endpoints for querying chat models with structured JSON payloads.
tags:
  - databricks
  - rest-api
  - model-serving
timestamp: "2026-06-19T20:00:46.569Z"
---

# REST API for Model Serving

The **REST API for Model Serving** allows you to send synchronous inference requests to model serving endpoints, including [Foundation Models APIs](/concepts/foundation-model-apis.md) (Databricks-hosted foundation models) and [External Models](/concepts/external-models.md) (models hosted outside of Databricks). This API uses standard HTTP methods and JSON payloads, and is one of several client options for querying models. ^[query-a-chat-model-databricks-on-aws.md]

## Request Format

A REST API request to a chat model serving endpoint conforms to a JSON body with a `messages` array. Each message has a `role` (e.g., `user`, `system`) and `content`. Optional parameters such as `max_tokens` and `temperature` can be included. ^[query-a-chat-model-databricks-on-aws.md]

Example request body:

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

For external models, you can include additional parameters that are valid for the provider and endpoint configuration. ^[query-a-chat-model-databricks-on-aws.md]

## Response Format

The response is a JSON object containing:

- `model` – The name of the model that generated the completion.
- `choices` – Array of choice objects, each containing a `message`, `index`, and `finish_reason`.
- `usage` – Token usage statistics (`prompt_tokens`, `completion_tokens`, `total_tokens`).
- `object` – Always `"chat.completion"`.
- `id` – May be `null` for Databricks-hosted endpoints.
- `created` – Unix timestamp of the generation.

Example response:
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

## Requirements

To use the REST API for model serving, you must:

- Have access to a Databricks workspace with a model serving endpoint configured.
- For external models, provide your Databricks workspace instance URL and an API token (e.g., `dapi-...`). ^[query-a-chat-model-databricks-on-aws.md]

## Client Options

The REST API is one of several ways to query models. Other options include the [OpenAI client](/concepts/openai-client-compatibility.md) (via `openai` library or `DatabricksOpenAI`), the [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md), the Databricks Python SDK, and LangChain. For SQL-based inference, see [AI Functions](/concepts/ai-functions.md). ^[query-a-chat-model-databricks-on-aws.md]

## Supported Models

See Foundation Model Types for the list of supported chat models available via the REST API. ^[query-a-chat-model-databricks-on-aws.md]

## Additional Resources

- [Query an embedding model](/concepts/text-embedding-models.md)
- Query reasoning models
- Query vision models

## Sources

- query-a-chat-model-databricks-on-aws.md

# Citations

1. [query-a-chat-model-databricks-on-aws.md](/references/query-a-chat-model-databricks-on-aws-0a958863.md)
