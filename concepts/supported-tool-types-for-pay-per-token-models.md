---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cde1ac4dbfd3ffb3bb4be40a1466473bb16ca4b4b6d4e0160834d10b5645a55e
  pageDirectory: concepts
  sources:
    - query-with-the-openai-responses-api-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-tool-types-for-pay-per-token-models
    - STTFPM
  citations:
    - file: query-with-the-openai-responses-api-databricks-on-aws.md
title: Supported Tool Types for Pay-Per-Token Models
description: "The complete list of tool types supported by pay-per-token foundation models via the Responses API: function, custom, apply_patch, shell, image_generation, mcp, and web_search."
tags:
  - tools
  - API
  - function-calling
  - Databricks
timestamp: "2026-06-19T20:06:20.181Z"
---

# Supported Tool Types for Pay-Per-Token Models

The [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md) on Databricks supports a set of built-in tool types for [Pay-Per-Token Foundation Models](/concepts/pay-per-token-foundation-model-apis.md). These tools enable models to perform actions such as structured function calling, code patching, shell commands, image generation, and web searches, all within a single response. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Supported Tool Types

The following tool types are available for pay‑per‑token foundation models via the Responses API: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

- **`function`** – Traditional structured [function calling](/concepts/llm-function-calling.md) that returns JSON‑formatted arguments.
- **`custom`** – User‑defined tools that return arbitrary string output instead of JSON. **Note:** Custom tools are supported only with GPT‑5 series models (`databricks-gpt-5`, `databricks-gpt-5-1`, `databricks-gpt-5-2`, `databricks-gpt-5-4`, `databricks-gpt-5-5`, `databricks-gpt-5-5-pro`). ^[query-with-the-openai-responses-api-databricks-on-aws.md]
- **`apply_patch`** – Code patching operations that apply text patches directly to files.
- **`shell`** – Shell command execution inside a sandboxed environment.
- **`image_generation`** – Image generation driven by the model’s output.
- **`mcp`** – Tools defined via the Model Context Protocol for dynamic tool integration.
- **`web_search`** – Web search capabilities that allow the model to query external sources.

## Important Limitations

- The listed tool types apply only to **pay‑per‑token foundation models** hosted on Databricks. External models (e.g., OpenAI, Azure OpenAI) support all Responses API parameters and tools without restriction. ^[query-with-the-openai-responses-api-databricks-on-aws.md]
- Certain Responses API parameters (`background`, `store`, `previous_response_id`, `service_tier`) are **not supported** for pay‑per‑token models and return a 400 error if specified. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Related Concepts

- [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md)
- [Pay-Per-Token Foundation Models](/concepts/pay-per-token-foundation-model-apis.md)
- [Function Calling](/concepts/llm-function-calling.md)
- Custom Tools
- Model Context Protocol
- Web Search
- Code Patching
- Image Generation
- [Shell Command Execution](/concepts/remote-code-execution-model.md)

## Sources

- query-with-the-openai-responses-api-databricks-on-aws.md

# Citations

1. [query-with-the-openai-responses-api-databricks-on-aws.md](/references/query-with-the-openai-responses-api-databricks-on-aws-0558036c.md)
