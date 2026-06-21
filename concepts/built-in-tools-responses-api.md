---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93b422fc3ce39beb0966a386bbdbe865675643128178333af356c5b7bf75d771
  pageDirectory: concepts
  sources:
    - query-with-the-openai-responses-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-tools-responses-api
    - BT(A
    - Beta
  citations:
    - file: query-with-the-openai-responses-api-databricks-on-aws.md
title: Built-in Tools (Responses API)
description: Platform-provided tool capabilities like apply_patch that return structured outputs and are fully managed by the platform, requiring no backend implementation from the user.
tags:
  - tools
  - managed-services
  - OpenAI
  - Databricks
timestamp: "2026-06-19T20:06:19.805Z"
---

# Built-in Tools (Responses API)

**Built-in Tools** are platform-provided capabilities in the [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md) on Databricks that allow models to perform actions without requiring you to implement the tool backend yourself. These tools return structured outputs and are fully managed by the platform. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Overview

The Responses API is an alternative to the [Chat Completions API](/concepts/chat-completions-api.md) that provides additional features for OpenAI models, including custom tools and multi-step workflows. Built-in tools extend the API's functionality by enabling the model to invoke platform-managed capabilities directly. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

Unlike [Custom Tools (Responses API)](/concepts/custom-tools-in-responses-api.md), which allow the model to return arbitrary string output—useful for code generation, applying patches, or other use cases where structured JSON is not required—built-in tools are pre-implemented capabilities that require no custom backend logic. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Supported Built-in Tools

For pay-per-token foundation models hosted on Databricks (GPT-5 series), the following tool types are supported: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

- `function` — Traditional structured function calling with JSON-formatted arguments.
- `custom` — Custom user-defined tools for arbitrary string output.
- `apply_patch` — Code patching operations.
- `shell` — Shell command execution.
- `image_generation` — Image generation.
- `mcp` — Model Context Protocol tools.
- `web_search` — Web search.

## Usage Example

The following Python example demonstrates using the `apply_patch` built-in tool to prompt a model to add input validation to a file: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()

response = client.responses.create(
    model="databricks-gpt-5",
    input=[{
        "role": "user",
        "content": "Add input validation to the factorial function in main.py."
    }],
    tools=[
        {
            "type": "apply_patch"
        }
    ],
    max_output_tokens=1024
)
print(response.output_text)
```

## Model Compatibility

Built-in tools are supported with GPT-5 series models through the Responses API. The `custom` tool type specifically is only available with the following models: `databricks-gpt-5`, `databricks-gpt-5-1`, `databricks-gpt-5-2`, `databricks-gpt-5-4`, `databricks-gpt-5-5`, and `databricks-gpt-5-5-pro`. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## External Model Support

External models—specifically those from the OpenAI model provider and Azure OpenAI model provider—support all Responses API parameters and tools, including built-in tools. The limitations that apply to pay-per-token foundation models do not apply to external models. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Limitations

For pay-per-token foundation models, several Responses API parameters are not supported and return a 400 error if specified, including `background`, `store`, `previous_response_id`, and `service_tier`. However, the listed built-in tool types remain fully supported. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Related Concepts

- [Custom Tools (Responses API)](/concepts/custom-tools-in-responses-api.md) — User-defined tools for arbitrary string output.
- [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) — Traditional structured function calling.
- [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md) — The API endpoint that provides built-in tool support.
- [Chat Completions API](/concepts/chat-completions-api.md) — Unified API alternative for all providers.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Pay-per-token model access on Databricks.
- [External Models](/concepts/external-models.md) — Third-party models from OpenAI and Azure OpenAI.

## Sources

- query-with-the-openai-responses-api-databricks-on-aws.md

# Citations

1. [query-with-the-openai-responses-api-databricks-on-aws.md](/references/query-with-the-openai-responses-api-databricks-on-aws-0558036c.md)
