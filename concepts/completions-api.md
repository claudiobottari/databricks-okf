---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c0d925577ce07ece71177219c7c2335c58efa22d74fb304c676c5b658e265d1
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - completions-api
    - LLM Completions
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Completions API
description: Text completion API for generating responses to single prompts, supporting batched independent prompts in one request.
tags:
  - api
  - completions
  - text-generation
timestamp: "2026-06-18T12:26:02.315Z"
---

# Completions API

The **Completions API** is a Databricks Foundation Model API endpoint for text completion tasks. Unlike the [Chat Completions API](/concepts/chat-completions-api.md), which is designed for multi-turn conversations, the Completions API generates responses to a single prompt and supports batched inputs — multiple independent prompts can be sent in one request. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Overview

Text completion tasks generate a continuation of a given prompt. The Completions API is suitable for single-turn generation tasks where no conversation history is required. It supports both pay-per-token and provisioned throughput endpoints, accepting the same REST API request format. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Endpoint

Requests are made via HTTP POST to the serving endpoint:

```
POST /serving-endpoints/{name}/invocations
```

^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Completion Request

The completion request accepts the following parameters:

### Request Body Fields

| Field | Type | Description |
|-------|------|-------------|
| `prompt` | string or array of strings | The prompt(s) to generate completions for. Multiple independent prompts can be sent in one request. |
| `max_tokens` | integer | Maximum number of tokens to generate. |
| `temperature` | float | Sampling temperature (0–2). Higher values make output more random. |
| `top_p` | float | Nucleus sampling parameter. |
| `stop` | string or array of strings | Sequences where the API will stop generating further tokens. |
| `stream` | boolean | Whether to stream the response. If `true`, the response is a `text/event-stream` where each event is a completion chunk object. |
| `echo` | boolean | Whether to echo back the prompt in the response. |
| `n` | integer | Number of completions to generate for each prompt. |
| `suffix` | string | The suffix that comes after a completion of inserted text. |

^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Request Example

```json
{
  "prompt": "The capital of France is",
  "max_tokens": 50,
  "temperature": 0.7,
  "n": 1
}
```

## Completion Response

For non-streaming requests, the response is a single completion object. For streaming requests, the response is a `text/event-stream` where each event is a completion chunk object. The top-level structure of completion and chunk objects is almost identical; only the `choices` field has a different type. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Response Body Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | A unique identifier for the completion. |
| `object` | string | The object type; always `"text_completion"`. |
| `created` | integer | Unix timestamp of when the completion was created. |
| `model` | string | The model used for the completion. |
| `choices` | array | An array of completion choices. |
| `usage` | object | Token usage information for the request. |

^[foundation-model-rest-api-reference-databricks-on-aws.md]

#### `CompletionChoice`

| Field | Type | Description |
|-------|------|-------------|
| `text` | string | The generated completion text. |
| `index` | integer | The index of the choice in the list of choices. |
| `finish_reason` | string | The reason the model stopped generating tokens: `"stop"`, `"length"`, or `"content_filter"`. |

^[foundation-model-rest-api-reference-databricks-on-aws.md]

#### Usage Object

The `usage` sub-message reports the number of tokens in the request and response:

| Field | Type | Description |
|-------|------|-------------|
| `prompt_tokens` | integer | Number of tokens in the prompt. |
| `completion_tokens` | integer | Number of tokens in the generated completion. |
| `total_tokens` | integer | Total number of tokens used. |

^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Response Example (Non-Streaming)

```json
{
  "id": "cmpl-abc123",
  "object": "text_completion",
  "created": 1680000000,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": " Paris.",
      "index": 0,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 2,
    "total_tokens": 7
  }
}
```

## Key Differences from Chat Completions API

| Feature | Completions API | Chat Completions API |
|---------|-----------------|----------------------|
| Input format | Single prompt string or array | Array of messages with role/content |
| Multi-turn support | No | Yes |
| Batched inputs | Yes (multiple prompts per request) | No |
| `system` role | Not applicable | Supported as first message |
| Streaming response | Supported (`text/event-stream`) | Supported (`text/event-stream`) |

^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Usage Considerations

- **Prompt tokens** include all text added by the server, including any prompt templates applied before passing the prompt to the model. For pay-per-token endpoints, a system prompt might also be added. ^[foundation-model-rest-api-reference-databricks-on-aws.md]
- The Completions API is designed to be similar to OpenAI's REST API format, making it easier to migrate existing projects. ^[foundation-model-rest-api-reference-databricks-on-aws.md]
- For models that use prompt templates (such as `databricks-meta-llama-3-3-70b-instruct`), the user prompt is transformed before being passed to the model. Tokens related to this transformation are included in `prompt_tokens`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Overview of Databricks Foundation Model APIs
- [Chat Completions API](/concepts/chat-completions-api.md) — Multi-turn conversation API
- [Responses API](/concepts/responses-api.md) — OpenAI-compatible responses API for multi-turn conversations
- [Model Serving](/concepts/model-serving.md) — Deploying and serving models on Databricks
- [Pay-per-token endpoint](/concepts/pay-per-token-endpoints.md) — Usage-based pricing model
- [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md) — Reserved capacity pricing model

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
