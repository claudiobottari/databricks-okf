---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6305a902ead17ee16fe59376097e2c14971e55fbb5c7b4703428c6a3d4b17eed
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - json-schema-subset-for-function-definitions
    - JSSFFD
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: JSON Schema Subset for Function Definitions
description: The restricted JSON schema specification that Databricks Foundation Model APIs accept for function call definitions, excluding pattern, anyOf, oneOf, allOf, $ref, and limiting keys to 16.
tags:
  - json-schema
  - function-calling
  - api-limits
timestamp: "2026-06-19T18:56:10.321Z"
---

Here is the wiki page for "JSON Schema Subset for Function Definitions".

---

## JSON Schema Subset for Function Definitions

**JSON Schema Subset for Function Definitions** refers to the constrained set of JSON Schema specifications supported by Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) when defining function parameters for [function calling](/concepts/llm-function-calling.md). To promote higher quality [structured output](/concepts/structured-outputs-in-foundation-model-apis.md) generation from large language models (LLMs), only a simplified subset of the full JSON Schema specification is accepted. ^[function-calling-on-databricks-databricks-on-aws.md]

### Supported Capabilities

The API broadly supports function definitions that are compatible with the OpenAI API. However, using simpler schemas results in more reliable and higher quality function call JSON generation. ^[function-calling-on-databricks-databricks-on-aws.md]

The `parameters` field in a function definition uses a JSON Schema object. The schema must specify `type: "object"` and define its properties within a `properties` object, where each property can specify its own `type` and, optionally, an `enum` or `description`. ^[function-calling-on-databricks-databricks-on-aws.md]

### Unsupported Keywords

The following JSON Schema keywords and constructs are **not supported** for function call definitions: ^[function-calling-on-databricks-databricks-on-aws.md]

- `pattern` (regular expressions)
- Complex nested or schema composition keywords:
  - `anyOf`
  - `oneOf`
  - `allOf`
  - `prefixItems`
  - `$ref`
- Lists of types, except for the special case of `[type, "null"]` where one type in the list is a valid JSON type and the other is `"null"`.

### Additional Limitations

In addition to the unsupported keywords, the following constraints apply: ^[function-calling-on-databricks-databricks-on-aws.md]

- The maximum number of keys specified in the JSON schema is **16**.
- Length and size constraints for objects and arrays are not enforced by the API. This includes keywords such as `maxProperties`, `minProperties`, and `maxLength`.
- Heavily nested JSON schemas result in **lower quality generation**. For better results, schemas should be as flat as possible.

### Best Practices

To maximize the quality of function call generation, follow these recommendations: ^[function-calling-on-databricks-databricks-on-aws.md]

- Flatten nested schemas instead of using deep nesting.
- Keep the total number of keys below 16.
- Avoid the composition keywords (`anyOf`, `oneOf`, `allOf`, `$ref`, `prefixItems`) entirely.
- Do not rely on `pattern` for input validation; use `enum` or descriptions instead.

### Related Concepts

- [Function Calling](/concepts/llm-function-calling.md) — Overview of how LLMs generate structured JSON objects.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The Databricks API layer that supports function calling.
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Databricks recommendation for batch inference or data processing tasks that need structured responses.
- [OpenAI API Compatibility](/concepts/ollama-openai-api-compatibility.md) — Databricks function calling is OpenAI-compatible.
- LLM Structured Generation — General topic of constraining LLM outputs to a schema.

### Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
