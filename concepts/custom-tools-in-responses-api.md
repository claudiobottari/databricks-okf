---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ac43e53ec38d3aea3a420d1c3114b2ff17fe0289796e122d39f915e787a3a52
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
    - query-with-the-openai-responses-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - custom-tools-in-responses-api
    - CTIRA
    - Custom Tools (Responses API)
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
    - file: query-with-the-openai-responses-api-databricks-on-aws.md
title: Custom Tools in Responses API
description: GPT-5 series model feature allowing models to return arbitrary plain text output instead of JSON-formatted function arguments, with optional grammar-based format constraints.
tags:
  - api
  - tool-calling
  - gpt-5
timestamp: "2026-06-19T18:55:15.830Z"
---

# Custom Tools in Responses API

**Custom Tools** extend the [Responses API] by allowing the model to return arbitrary string output instead of the structured JSON arguments required by traditional [function calling]. This makes them ideal for use cases like code generation, applying patches, or any scenario where the model needs to produce free‑form text as a tool invocation.

## Model Support

Custom tools are **only supported with GPT‑5 series models** (`databricks‑gpt‑5`, `databricks‑gpt‑5‑1`, `databricks‑gpt‑5‑2`, `databricks‑gpt‑5‑4`, `databricks‑gpt‑5‑5`, `databricks‑gpt‑5‑5‑pro`, and their sub‑variants) through the Responses API. They are not available through the [Chat Completions API] or with non‑GPT‑5 models. ^[foundation-model-rest-api-reference-databricks-on-aws.md, query-with-the-openai-responses-api-databricks-on-aws.md]

## How Custom Tools Work

When a custom tool is defined, the model can decide to call it by returning a `custom_tool_call` output item. Unlike function calls, the `custom_tool_call` contains plain text in its `input` field instead of a JSON object with `arguments`. You provide the result of the custom tool back to the model using the `CustomToolCallOutput` input type in a subsequent turn. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Defining a Custom Tool

A custom tool is defined as a JSON object with `type: "custom"`, a `name`, and an optional `description`. The following example defines a tool for executing arbitrary Python code: ^[foundation-model-rest-api-reference-databricks-on-aws.md]

```json
{
  "type": "custom",
  "name": "code_exec",
  "description": "Executes arbitrary Python code. Return only valid Python code."
}
```

### Custom Tools with Grammar‑Based Output

For GPT‑5 series models, you can optionally specify a **grammar** to constrain the tool’s output format. This is done by adding a `format` field that defines a Lark grammar: ^[foundation-model-rest-api-reference-databricks-on-aws.md]

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

## Querying with Custom Tools

Custom tools can be used with both the `DatabricksOpenAI` client and the OpenAI client. The Python example below demonstrates a custom tool call using Databricks’ client: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
response = client.responses.create(
    model="databricks-gpt-5",
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
    tools=[
        {
            "type": "custom",
            "name": "code_exec",
            "description": "Executes arbitrary Python code. Return only valid Python code."
        }
    ],
    max_output_tokens=1024
)
```

When the model calls the custom tool, the response’s `output` array contains a `custom_tool_call` item. The `output_text` property of the response object contains the last output text, but for tool calls you should inspect the `output` structure directly. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Supported Tool Types in Responses API

The `tools` parameter of a Responses API request supports the following tool types for pay‑per‑token foundation models: `function`, `custom`, `apply_patch`, `shell`, `image_generation`, `mcp`, and `web_search`. Custom tools and grammar‑based output formats are available only with GPT‑5 series models. ^[foundation-model-rest-api-reference-databricks-on-aws.md, query-with-the-openai-responses-api-databricks-on-aws.md]

## Limitations

- Custom tools are **not supported** in the Chat Completions API.
- For pay‑per‑token foundation models, the following Responses API parameters are unsupported and return a 400 error: `background`, `store`, `previous_response_id`, and `service_tier`. ^[query-with-the-openai-responses-api-databricks-on-aws.md]
- External model providers (OpenAI, Azure OpenAI) support all Responses API parameters and tools without these limitations. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Related Concepts

- [Responses API] – The API entry point for multi‑turn conversations that supports custom tools.
- [Function Calling] – The traditional JSON‑based tool calling method.
- [GPT‑5 Models] – The model family that supports custom tools and grammar‑based output.
- [Built‑in Tools] – Platform‑managed tools like `apply_patch` that do not require custom backend implementation.

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md
- query-with-the-openai-responses-api-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
2. [query-with-the-openai-responses-api-databricks-on-aws.md](/references/query-with-the-openai-responses-api-databricks-on-aws-0558036c.md)
