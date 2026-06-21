---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d44fb960f1a1195c9f95835ff565a2041a6e918dbf3b7635d3aacc1f901190de
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - json-schema-subset-for-function-calling
    - JSSFFC
    - JSON Schema Support in Function Calling
    - JSON Schema Specification
    - JSON Schema specification
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: JSON Schema Subset for Function Calling
description: Databricks Foundation Model APIs support a simplified subset of JSON Schema for function definitions, excluding pattern, anyOf/oneOf/allOf, prefixItems, and $ref to improve generation quality.
tags:
  - json-schema
  - function-calling
  - databricks
timestamp: "2026-06-18T12:27:15.080Z"
---

## JSON Schema Subset for Function Calling

**JSON Schema Subset for Function Calling** refers to the simplified set of JSON Schema keywords that Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) accept when defining function parameters in a function‑calling request. Using this subset produces higher‑quality structured output from the language model, whereas unsupported or overly complex schema constructs degrade reliability. ^[function-calling-on-databricks-databricks-on-aws.md]

### Supported and Unsupported Keys

The system broadly supports the function‑definition format accepted by OpenAI, but it enforces restrictions on certain JSON Schema keywords to optimise generation quality. ^[function-calling-on-databricks-databricks-on-aws.md]

**Unsupported keys** (must not be used in a function’s `parameters` object):

- `pattern` (regular expressions)
- Complex nesting or schema composition keywords: `anyOf`, `oneOf`, `allOf`, `prefixItems`, `$ref`
- Lists of types, except the special case where one type is a valid JSON type and the other is `"null"` (e.g. `["string", "null"]`)

^[function-calling-on-databricks-databricks-on-aws.md]

**Additional limitations:**

- The maximum number of keys specified in the JSON schema is **16**.
- Length and size constraints such as `maxProperties`, `minProperties`, and `maxLength` are not enforced by the API.
- Heavily nested JSON schemas result in lower‑quality generation. Flattening the schema is recommended for better results.

^[function-calling-on-databricks-databricks-on-aws.md]

### Best Practices

- Keep function definitions simple and shallow. Use a flat structure instead of deep nesting.
- Define a clear `description` for each parameter and for the function itself, as the model uses these descriptions when deciding whether to call the function and how to fill arguments.
- Avoid any of the unsupported composition keywords; if you need conditional validation, restructure the schema or split the function.

### Related Concepts

- [Function Calling](/concepts/llm-function-calling.md) — The broader mechanism for controlling LLM output with tool definitions
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The Databricks serving layer that implements this subset
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — An alternative approach for batch or data‑processing tasks
- [Chat Completions API](/concepts/chat-completions-api.md) — The API endpoint where tools are specified

### Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
