---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9b037125ae77adf43caafc3e76195a729eeaa08d6edd25ea6fa31ea5e04c32c
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - responses-api-databricks
    - RA(
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Responses API (Databricks)
description: An OpenAI-compatible multi-turn conversation API that uses 'input' instead of 'messages', supporting custom tools, grammar-based outputs, and reasoning configs.
tags:
  - api
  - multi-turn
  - openai-compatible
timestamp: "2026-06-19T18:54:55.567Z"
---

# Responses API (Databricks)

The **Responses API** is a REST API provided by Databricks Foundation Model APIs that enables multi-turn conversations with supported models. It is designed to be compatible with OpenAI's Responses API format, making it easier to migrate existing projects. The Responses API is only compatible with OpenAI models. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Overview

Unlike the Chat Completions API, the Responses API uses `input` instead of `messages` to structure conversation data. Both pay-per-token and provisioned throughput endpoints accept the same REST API request format. Requests and responses use JSON, with the exact structure depending on the endpoint's task type. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Unsupported Parameters

The following parameters are not supported by Databricks and will return a 400 error if specified:

- `background` — Background processing is not supported
- `store` — Stored responses is not supported
- `conversation` — Conversation API is not supported
- `service_tier` — Service tier selection is managed by Databricks

^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Request Structure

### `ResponsesInput`

The `input` field accepts either a string or a list of input message objects with role and content. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ResponsesContentBlock`

Content blocks define the type of content in input and output messages. The content block type is determined by the `type` field. Supported content block types include:

- `InputText` — Text input content
- `OutputText` — Text output content
- `InputImage` — Image input content
- `InputFile` — File input content
- `FunctionCall` — Function call content
- `FunctionCallOutput` — Function call output content
- `CustomToolCall` — Returned in the response `output` array when a custom tool is called. Unlike function calls, custom tool calls return plain text `input` instead of JSON `arguments`.
- `CustomToolCallOutput` — Use this input type to provide the result of a custom tool call back to the model in a multi-turn conversation.

^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `StreamOptions`

Configuration for streaming responses. Only used when `stream: true`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `TextConfig`

Configuration for text output, including structured outputs. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ResponsesFormatObject`

Specifies the output format for text responses. The `json_schema` object has the same structure as `JsonSchemaObject` documented in the Chat Completions API. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ReasoningConfig`

Configuration for reasoning behavior in reasoning models (o-series and gpt-5 models). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ToolObject`

See [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) for details. The Responses API supports the following tool types: `function`, `custom`, `mcp`, `image_generation`, `shell`. Custom tools and grammar-based output formats are only available with GPT-5 series models (`gpt-5`, `gpt-5.1`, `gpt-5.2`). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `CustomToolObject`

Custom tools allow the model to return arbitrary string output instead of JSON-formatted function arguments. This is useful for code generation, applying patches, or other use cases where structured JSON is not required. Custom tools are only supported with GPT-5 series models through the Responses API. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

**Example custom tool:**

```json
{
  "type": "custom",
  "name": "code_exec",
  "description": "Executes arbitrary Python code. Return only valid Python code."
}
```

**Example custom tool with grammar:**

```json
{
  "type": "custom",
  "name": "apply_patch",
  "description": "Apply a patch to create or modify files.",
  "format": {
    "type": "grammar",
    "definition": "start: begin_patch hunk end_patch\nbegin_patch: \"*** Begin Patch\" LF\n...",
    "syntax": "lark"
  }
}
```

When a custom tool is called, the response contains a `custom_tool_call` output item with plain text `input` instead of JSON `arguments`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `CustomFormat`

Grammar-based output formats are only supported with GPT-5 series models. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `FunctionObject` and `ToolChoiceObject`

See [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) for details. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Response Structure

For non-streaming requests, the response is a single response object. For streaming requests, the response is a `text/event-stream` where each event is a response chunk. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ResponsesMessage`

Message objects in the `output` field containing the model's response content. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `Error`

Error information when a response fails. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `IncompleteDetails`

Details about why a response is incomplete. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Usage Information

Responses include a `usage` sub-message which reports the number of tokens in the request and response. The format of this sub-message is the same across all task types. For models like `databricks-meta-llama-3-3-70b-instruct`, a user prompt is transformed using a prompt template before being passed into the model. For pay-per-token endpoints, a system prompt might also be added. `prompt_tokens` includes all text added by the server. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Chat Completions API (Databricks)](/concepts/chat-completions-api-databricks.md) — An alternative API for multi-turn conversations using `messages` instead of `input`
- [Foundation Model APIs (Databricks)](/concepts/foundation-model-apis-databricks.md) — The broader API framework that includes the Responses API
- [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) — Details on function calling capabilities
- Structured Outputs on Databricks — Information on structured output formats
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Endpoints that support multiple models per endpoint for A/B testing
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Preconfigured endpoints for supported models

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
