---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29d0f2f2d926cac944f2650e0568d70bd30ba0169e61ade360fd9f3f64d598dd
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - json-schema-limitations-for-function-calling
    - JSLFFC
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: JSON Schema Limitations for Function Calling
description: Foundation Model APIs support only a subset of JSON schema for function definitions, excluding pattern, complex composition keywords, and limiting to 16 keys maximum.
tags:
  - schema
  - limitations
  - function-calling
timestamp: "2026-06-19T10:40:54.497Z"
---

# JSON Schema Limitations for Function Calling

**JSON Schema Limitations for Function Calling** describes the restricted subset of [JSON Schema specifications](https://json-schema.org/specification) that [Foundation Model APIs](/concepts/foundation-model-apis.md) support when defining function parameters for tool calls. Using a simpler schema yields higher quality JSON generation from the model.^[function-calling-on-databricks-databricks-on-aws.md]

## Unsupported JSON Schema Features

The following JSON Schema constructs are **not supported** in function definitions for Foundation Model APIs:^[function-calling-on-databricks-databricks-on-aws.md]

- Regular expressions using the `pattern` keyword.
- Complex nested or schema composition and validation using: `anyOf`, `oneOf`, `allOf`, `prefixItems`, or `$ref`.
- Lists of types except for the special case of `[type, "null"]` where one type in the list is a valid JSON type and the other is `"null"`.

## Additional Limitations

Beyond the unsupported schema features, the following constraints apply:^[function-calling-on-databricks-databricks-on-aws.md]

- **Maximum number of keys:** The JSON schema can define at most 16 keys.
- **No enforcement of length/size constraints:** Keywords like `maxProperties`, `minProperties`, `maxLength`, and similar constraints are not enforced by Foundation Model APIs.
- **Nested schemas:** Heavily nested JSON schemas result in lower quality generation. Flattening the schema is recommended for better results.
- **Overly complex schemas:** Using a simpler JSON schema for function call definitions leads to higher quality function call JSON generation overall.

## Best Practices

To maximize generation quality and reliability, consider the following:^[function-calling-on-databricks-databricks-on-aws.md]

- Use flat, shallow schemas where possible.
- Avoid `anyOf`, `oneOf`, `allOf`, and `$ref` entirely.
- Limit the number of properties to 16 or fewer.
- Do not rely on pattern validation, as it is unsupported.
- For nullable fields, use `[type, "null"]` as the type value (e.g., `"type": ["string", "null"]`).

## Related Concepts

- [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) — Full guide to using function calling.
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Recommended alternative for batch inference or data processing tasks.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving system that provides function calling support.
- [Supported Models for Function Calling](/concepts/supported-models-for-function-calling-on-databricks.md) — Models that support function calling features.
- [Chat Completions API](/concepts/chat-completions-api.md) — API syntax for including tools and function definitions.

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
