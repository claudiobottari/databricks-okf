---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74f4b1a1d99fb86497c006c406df3850a59035ddb15215254389e1024bbd3318
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chat-completions-api
    - CCA
    - Chat Completion API
    - Chat Completions
    - Chat completions
    - ChatCompletion
    - Chat Completions Endpoint
    - Chat and Completion Models
    - Chat completions endpoint
    - LLM Chat Completions
    - OpenAI Chat Completions
    - chat completion model
    - chat completions endpoint
    - streaming completions
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Chat Completions API
description: An API on Databricks for multi-turn conversations using 'messages' array, supporting content types including text, image, reasoning, and document content.
tags:
  - api
  - llm
  - databricks
timestamp: "2026-06-19T10:39:24.225Z"
---

# Chat Completions API

The **Chat Completions API** enables multi-turn conversations with a language model by sending a series of messages and receiving a model-generated response. It is part of the [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) and is designed to be similar to OpenAI's REST API to make migrating existing projects easier. Both pay-per-token and provisioned throughput endpoints accept the same REST API request format. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Endpoints

The Chat Completions API is accessed via HTTP POST requests to serving endpoints. Use the following endpoint to query a serving endpoint:

```
POST /serving-endpoints/{name}/invocations
```

^[foundation-model-rest-api-reference-databricks-on-aws.md]

Requests and responses use JSON. Chat endpoints support streaming responses, where the response is a `text/event-stream` and each event is a completion chunk object. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Chat Request

The request body contains a list of messages that represent the conversation history, along with optional parameters for controlling the model's behavior.

### `ChatMessage`

Messages in the conversation are represented by chat message objects. Each message has a `role` and `content`. Supported roles include:

- **`system`**: Can only be used once, as the first message in a conversation. It overrides the model's default system prompt.
- **`user`**: Represents user input in the conversation.
- **`assistant`**: Represents model responses (included for multi-turn conversations).

^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ContentItem`

The content of a message can be one of the following content types:

| Content Type | Description |
|---|---|
| `TextContent` | Text input with optional citation fields |
| `ImageContent` | Image input via image URL fields |
| `ReasoningContent` | Reasoning-related content from the model, including `TextSummary` and `EncryptedTextSummary` subtypes |
| `DocumentContent` | Document input (requests only) with a `Source` field |
| `FileContent` | File input with file-specific fields |

### `ToolCall`

A tool call action suggested by the model. See [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) for details. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `FunctionCallCompletion`

A function call completion object. Note that `ToolChoiceObject`, `ToolObject`, and `FunctionObject` are shared between the [Responses API](/concepts/responses-api.md) and the Chat Completions API. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ResponseFormatObject`

Specifies the output format for the model response. See Structured Outputs on Databricks for details. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `JsonSchemaObject`

A JSON schema object used with structured outputs. See Structured Outputs on Databricks for details. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Chat Response

For non-streaming requests, the response is a single chat completion object. For streaming requests, the response is a `text/event-stream` where each event is a completion chunk object. The top-level structure of completion and chunk objects is almost identical: only `choices` has a different type. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### `ChatCompletionChoice`

Represents a single completion choice in a non-streaming response, containing the model's message and the finish reason.

### `ChatCompletionChunk`

Represents a streaming completion chunk, containing incremental content from the model.

## Usage Information

Responses include a `usage` sub-message that reports the number of tokens in the request and response. `prompt_tokens` includes all text added by the server, including any prompt templates or system prompts applied. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Supported Models

A preconfigured endpoint is available in each workspace for each pay-per-token supported model. See Supported Foundation Models on Model Serving for the complete list. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Provisioned Throughput

Provisioned throughput endpoints can be created using the API or the Serving UI. These endpoints support multiple models per endpoint for A/B testing, as long as both served models expose the same API format (for example, both are chat models). See [Creating Serving Endpoints](/concepts/migrating-llm-serving-endpoints.md) for configuration parameters. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Foundation Model REST API Reference](/concepts/foundation-model-apis.md) — General API information and model support
- [Responses API](/concepts/responses-api.md) — An alternative API for multi-turn conversations using `input` instead of `messages`
- [Chat Completions API](/concepts/chat-completions-api.md) — This API, for multi-turn conversations
- [Embeddings API](/concepts/embeddings-api.md) — For mapping input strings to embedding vectors
- [Completions API](/concepts/completions-api.md) — For single-prompt text generation with batched inputs
- [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) — Tool and function calling capabilities
- Structured Outputs on Databricks — JSON schema output formatting
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Preconfigured endpoints with usage-based pricing
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Custom endpoints with reserved capacity

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
