---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 68c99da17cb2e1ee2d52484d69a5c0815cdd44b766307b6a3681a5a52e26ff41
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chat-completions-api-databricks
    - CCA(
    - Chat Completions API on Databricks
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Chat Completions API (Databricks)
description: Multi-turn conversation API compatible with OpenAI's Chat Completions format, supporting system/assistant/user messages, tool calls, and streaming.
tags:
  - api
  - chat
  - multi-turn
timestamp: "2026-06-19T18:54:59.162Z"
---

## Chat Completions API (Databricks)

The **Chat Completions API** on Databricks provides a REST interface for multi-turn conversations with supported foundation models. The API is designed to be similar to OpenAI's Chat Completions API, making it straightforward to migrate existing projects. Both pay‑per‑token and provisioned throughput endpoints accept the same request format. Requests and responses use JSON, and streaming responses are supported. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Endpoint

All chat completion requests are made via an HTTP POST to the model serving endpoint:

```
POST /serving-endpoints/{name}/invocations
```

The `{name}` parameter is the name of the deployed serving endpoint. For pay‑per‑token models, a preconfigured endpoint exists in the workspace. Provisioned throughput endpoints can be created via the Serving UI or the API. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Request Structure

The request body contains a list of `messages` and optional parameters. The following components are used:

- **ChatMessage** – Each message has a `role` (e.g., `system`, `user`, `assistant`) and `content`. The `system` role can only be used once, as the first message in the conversation; it overrides the model’s default system prompt. ^[foundation-model-rest-api-reference-databricks-on-aws.md]
- **ContentItem** – The content of a message can be one of several types:
  - `TextContent`
  - `ReasoningContent`
  - `DocumentContent`
  - `ImageContent`
  - `FileContent`
- **ToolCall** – A tool call action suggested by the model. See Function calling on Databricks.
- **FunctionCallCompletion** – The result of a function call.
- **ResponseFormatObject** – Specifies the output format (used with structured outputs). See [Structured outputs on Databricks](/concepts/structured-outputs-in-foundation-model-apis.md).
- **JsonSchemaObject** – A JSON schema object for structured output formats. See [Structured outputs on Databricks](/concepts/structured-outputs-in-foundation-model-apis.md).

The `Usage` sub‑message reports `prompt_tokens` and `completion_tokens`. For models that use a prompt template (e.g., `databricks-meta-llama-3-3-70b-instruct`), `prompt_tokens` includes all text added by the server (including any system prompt). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Response Structure

For non‑streaming requests, the response is a single chat completion object. For streaming requests, the response is a `text/event‑stream` where each event is a completion chunk object. The top‑level structure of completion and chunk objects is nearly identical; only the `choices` field differs in type. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

- **ChatCompletionChoice** – Represents one completion choice in the non‑streaming response.
- **ChatCompletionChunk** – Represents one chunk in a streaming response.

Each choice contains a `ChatMessage` (the assistant’s response) and may include tool calls or function calls.

### Key Characteristics

- The model response provides the next `assistant` message in the conversation.
- The API supports multi‑turn conversations by including the full message history.
- System messages are allowed only once and must be the first message.
- Streaming is enabled by setting `stream: true` in the request.
- The API is compatible with both pay‑per‑token and provisioned throughput endpoints.

### Related Concepts

- [Foundation Model APIs (Databricks)](/concepts/foundation-model-apis-databricks.md)
- Multi-turn conversation
- Function calling on Databricks
- [Structured outputs on Databricks](/concepts/structured-outputs-in-foundation-model-apis.md)
- Streaming responses
- Token counting in API responses

### Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
