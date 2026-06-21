---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90926de5653ae1bc3d57799e44bb28f512bf92214f03ecf665d67f2ece40af28
  pageDirectory: concepts
  sources:
    - query-with-the-openai-responses-api-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-gpt-5-foundation-models
    - DGFM
  citations:
    - file: query-with-the-openai-responses-api-databricks-on-aws.md
title: Databricks-Hosted GPT-5 Foundation Models
description: A family of pay-per-token foundation model endpoints (databricks-gpt-5 through databricks-gpt-5-5-pro) hosted on Databricks that support the OpenAI Responses API with various model sizes and capabilities.
tags:
  - models
  - OpenAI
  - Databricks
  - foundation-models
timestamp: "2026-06-19T20:05:55.048Z"
---

# Databricks-Hosted GPT-5 Foundation Models

**Databricks-Hosted GPT-5 Foundation Models** are a family of large language models (LLMs) made available through Databricks’ pay-per-token Foundation Model API. These models are derived from OpenAI’s GPT‑5 architecture and are hosted entirely on Databricks infrastructure. They can be queried using the OpenAI-compatible Responses API or the Chat Completions API. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Model Variants

Databricks offers multiple GPT‑5 model sizes and specializations. The available model endpoint names are: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

| Endpoint name | Description |
|--------------|-------------|
| `databricks-gpt-5-5-pro` | Largest variant, pro tier |
| `databricks-gpt-5-5` | Full-size variant |
| `databricks-gpt-5-4` | Large variant |
| `databricks-gpt-5-4-mini` | Mini version of the large variant |
| `databricks-gpt-5-4-nano` | Nano version of the large variant |
| `databricks-gpt-5-3-codex` | Code‑specialized variant |
| `databricks-gpt-5-2` | Medium variant |
| `databricks-gpt-5-2-codex` | Code‑specialized medium variant |
| `databricks-gpt-5-1` | Small variant |
| `databricks-gpt-5-1-codex-max` | Large code‑specialized small variant |
| `databricks-gpt-5-1-codex-mini` | Mini code‑specialized small variant |
| `databricks-gpt-5` | Base GPT‑5 model |
| `databricks-gpt-5-mini` | Mini base model |
| `databricks-gpt-5-nano` | Nano base model |

All listed models are available as pay-per-token foundation models through the Foundation Model APIs. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Capabilities

### Input Modalities

GPT‑5 models hosted on Databricks accept **text and image inputs**. For image format and size requirements, see the documentation on querying vision models. Per‑model input type support is detailed in the Databricks foundation model supported models list. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

### Custom Tools

Custom tools allow the model to return arbitrary string output instead of JSON‑formatted function arguments. This feature is **only supported with GPT‑5 series models** (`databricks-gpt-5-*` variants) through the Responses API. Custom tools are useful for code generation, applying patches, or other use cases where structured JSON is not required. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

Example usage with custom tool:

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

^[query-with-the-openai-responses-api-databricks-on-aws.md]

### Built-in Tools

Built-in tools provide platform‑managed capabilities without requiring users to implement a backend. These tools return structured outputs. Examples include `apply_patch`, `shell`, `image_generation`, `mcp` (Model Context Protocol), and `web_search`. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

Example usage with built-in `apply_patch` tool:

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
response = client.responses.create(
    model="databricks-gpt-5",
    input=[{
        "role": "user",
        "content": "Add input validation to the factorial function in main.py."
    }],
    tools=[{"type": "apply_patch"}],
    max_output_tokens=1024
)
print(response.output_text)
```

^[query-with-the-openai-responses-api-databricks-on-aws.md]

### Supported Tool Types (Pay‑per‑token Foundation Models)

The following tool types are supported for GPT‑5 pay‑per‑token foundation models: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

- `function` — Traditional structured function calling
- `custom` — Custom user‑defined tools
- `apply_patch` — Code patching operations
- `shell` — Shell command execution
- `image_generation` — Image generation
- `mcp` — Model Context Protocol tools
- `web_search` — Web search

## Limitations

The following limitations apply specifically to the pay‑per‑token GPT‑5 foundation models on Databricks (external models are not affected): ^[query-with-the-openai-responses-api-databricks-on-aws.md]

- **Unsupported parameters** (cause a 400 error if specified):
  - `background` — Background processing is not supported.
  - `store` — Stored responses are not supported.
  - `previous_response_id` — Stored responses are not supported.
  - `service_tier` — Service tier selection is managed by Databricks.

- **Responses API only**: The Responses API is the interface for accessing GPT‑5 models with custom and built-in tools. For a unified API that works across all providers, the Chat Completions API can be used. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs on Databricks](/concepts/foundation-models-apis-on-databricks.md)
- [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md)
- [Chat Completions API on Databricks](/concepts/chat-completions-api-databricks.md)
- [Query vision models on Databricks](/concepts/querying-vision-models-on-databricks-model-serving.md)
- Function calling on Databricks
- [Structured outputs on Databricks](/concepts/structured-outputs-in-foundation-model-apis.md)

## Sources

- query-with-the-openai-responses-api-databricks-on-aws.md

# Citations

1. [query-with-the-openai-responses-api-databricks-on-aws.md](/references/query-with-the-openai-responses-api-databricks-on-aws-0558036c.md)
