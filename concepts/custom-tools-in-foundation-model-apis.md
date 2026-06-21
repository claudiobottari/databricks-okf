---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c5242e8c9f78a3fff453c168f132f7cbd9d9b1994a1fddce12f3996b2307bc9
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-tools-in-foundation-model-apis
    - CTIFMA
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Custom Tools in Foundation Model APIs
description: A tool type in Databricks Foundation Model APIs that allows models to return arbitrary string output (e.g., code, patches) instead of JSON-formatted function arguments, supporting grammar-based output formats for GPT-5 series models.
tags:
  - api
  - llm
  - tool-use
timestamp: "2026-06-19T10:39:12.793Z"
---

# Custom Tools in Foundation Model APIs

**Custom Tools** allow a model to return arbitrary plain text output instead of JSON-formatted function arguments. They are part of the [Responses API](/concepts/responses-api.md) and are designed for use cases such as code generation, applying patches, or any scenario where structured JSON is not required. Custom tools are only supported with GPT-5 series models (`gpt-5`, `gpt-5.1`, `gpt-5.2`) through the Responses API; they are not available in the Chat Completions API or with other model families. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## How Custom Tools Work

When defining a custom tool, you specify the tool’s type as `"custom"`, a name, and a description. The model returns plain text output instead of JSON arguments. The response includes a `CustomToolCall` output item containing the tool call’s `input` as a raw string. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

Custom tools can optionally include a `format` object to constrain the output using a grammar. This is useful when the output must follow a specific syntax — for instance, a patch file format. Grammar-based formats are only supported with GPT-5 series models. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Example: Basic Custom Tool

```json
{
  "type": "custom",
  "name": "code_exec",
  "description": "Executes arbitrary Python code. Return only valid Python code."
}
```

When the model calls `code_exec`, the response output contains a `CustomToolCall` object with `input` set to the Python code string. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Example: Custom Tool with Grammar-Based Output

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

## Request and Response Types

| Type | Description |
|------|-------------|
| `CustomToolObject` | Defines a custom tool in the tools array of a Responses API request. Contains `type: "custom"`, `name`, `description`, and optional `format`. |
| `CustomToolCall` | Returned in the response `output` array when a custom tool is invoked. Contains plain text `input` instead of JSON `arguments`. |
| `CustomToolCallOutput` | Input message type used to provide the result of a custom tool call back to the model in a multi-turn conversation. |

All these types are only valid in the Responses API. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Responses API](/concepts/responses-api.md) — The API that supports custom tools and multi-turn conversations.
- [Function Calling](/concepts/llm-function-calling.md) — Traditional function calling with JSON arguments; custom tools extend this paradigm.
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Grammar-based constraints for model output (similar to `format` in custom tools).
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The broader API surface including Chat Completions, Embeddings, and Completions.

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
