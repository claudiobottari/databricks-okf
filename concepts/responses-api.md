---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 427b36a80b07e1f3e79e6002129ae3ffb53fa9063b9e22c1b79b9f9976832b76
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - responses-api
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Responses API
description: An OpenAI-compatible API on Databricks for multi-turn conversations using 'input' instead of 'messages', supporting custom tools, function calls, and grammar-based outputs for GPT-5 series models.
tags:
  - api
  - llm
  - databricks
timestamp: "2026-06-19T10:38:51.881Z"
---

---
title: Responses API
summary: OpenAI-compatible API for multi-turn conversations using `input` instead of `messages`, supporting custom tools and grammar-based output.
sources:
  - foundation-model-rest-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:25:25.339Z"
updatedAt: "2026-06-18T12:25:25.339Z"
tags:
  - api
  - responses
  - openai-compatible
aliases:
  - responses-api
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Responses API

The **Responses API** is a Databricks [Foundation Model API](/concepts/foundation-model-apis.md) endpoint that enables multi-turn conversations with a model. Unlike the [Chat Completions API](/concepts/chat-completions-api.md), the Responses API uses an `input` field instead of `messages` to manage conversation state. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Compatibility

The Responses API is only compatible with OpenAI models. It is accessible through both pay-per-token and provisioned throughput endpoints, accepting the same REST API request format as other Foundation Model APIs. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Request Format

The request body uses JSON. The primary fields include:

### `input` (`ResponsesInput`)

Accepts either a string or a list of input message objects, each with a `role` and `content`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Content Blocks (`ResponsesContentBlock`)

Content blocks define the type of content in input and output messages, determined by the `type` field. Supported types include:

| Type | Description |
|------|-------------|
| `InputText` | Plain text input. |
| `OutputText` | Generated text output. |
| `InputImage` | Image input (base64 or URL). |
| `InputFile` | File input. |
| `FunctionCall` | Request for the model to call a function, returned in the output. |
| `FunctionCallOutput` | Result of a function call provided back to the model. |
| `CustomToolCall` | Returned when a custom tool is called; returns plain text `input` instead of JSON `arguments`. |
| `CustomToolCallOutput` | Result of a custom tool call provided back to the model for multi-turn conversations. |

### `StreamOptions`

Configuration for streaming responses. Only used when `stream: true`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `TextConfig`

Configuration for text output, including [structured outputs](/concepts/structured-outputs-in-foundation-model-apis.md) via `ResponsesFormatObject`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ReasoningConfig`

Configuration for reasoning behavior in reasoning models (o-series and gpt-5 models). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Tool Objects

The Responses API supports the following tool types: `function`, `custom`, `mcp`, `image_generation`, `shell`. Custom tools and grammar-based output formats are only available with GPT-5 series models (`gpt-5`, `gpt-5.1`, `gpt-5.2`). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

Custom tools allow the model to return arbitrary string output instead of JSON-formatted function arguments, useful for code generation or applying patches. When a custom tool is called, the response contains a `custom_tool_call` output item with plain text `input`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Response Format

For non-streaming requests, the response is a single response object. For streaming requests, it is a `text/event-stream` where each event is a response chunk. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Response Objects

- `ResponsesMessage`: Message objects in the `output` field containing the model's response content.
- `Error`: Error information when a response fails.
- `IncompleteDetails`: Details about why a response is incomplete.

## Unsupported Parameters

The following parameters are not supported by Databricks and return a 400 error if specified: ^[foundation-model-rest-api-reference-databricks-on-aws.md]

| Parameter | Reason |
|-----------|--------|
| `background` | Background processing is not supported. |
| `store` | Stored responses are not supported. |
| `conversation` | Conversation API is not supported. |
| `service_tier` | Service tier is managed by Databricks. |

## Custom Tools and Grammar Output

Custom tools and grammar-based output formats are exclusive to the Responses API with GPT-5 series models. Grammar output is defined using `CustomFormat` with a `grammar` type and a Lark grammar `definition`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Chat Completions API](/concepts/chat-completions-api.md) — Alternative API for multi-turn conversations using `messages`.
- [Foundation Model API](/concepts/foundation-model-apis.md) — The overarching API for Databricks-hosted models.
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Controlling output format with JSON schemas.
- [Function Calling](/concepts/llm-function-calling.md) — Using tools that return JSON arguments.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Custom endpoints supporting multiple models.

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
