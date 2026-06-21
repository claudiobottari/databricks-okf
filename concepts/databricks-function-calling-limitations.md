---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ff5f67242b2c37f0e905b4dff2d49f17eba2577234bc730537e710e550e92a3
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-function-calling-limitations
    - DFCL
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Databricks Function Calling Limitations
description: "Current Public Preview restrictions: single-turn optimization for most models, no parallel function calling, max 32 functions, no support on existing provisioned-throughput endpoints, and no 'id' field for Gemini models."
tags:
  - function-calling
  - limitations
  - public-preview
  - databricks
timestamp: "2026-06-19T18:56:36.412Z"
---

Here is the wiki page for "Databricks Function Calling Limitations".

---

## Databricks Function Calling Limitations

**Databricks Function Calling Limitations** describes the restrictions and unsupported behaviors that apply to the function calling feature on the Databricks platform during its Public Preview. Function calling is an OpenAI-compatible feature that allows users to control LLM output by describing functions in the API call, after which the model generates a JSON object that can be used to call those functions in user code. ^[function-calling-on-databricks-databricks-on-aws.md]

### Current Limitations

The following limitations apply to function calling during Public Preview:

- **Multi-turn function calling.** For multi-turn (conversational) function calling, Databricks recommends using the supported Claude models. When using Llama 4 Maverick, the current solution is optimized for single-turn calls. Multi-turn is supported but is under active development. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Parallel function calling.** Parallel function calling is not supported. The model can only be asked to call one function at a time. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Maximum number of functions.** The maximum number of functions that can be defined in the `tools` parameter is 32. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Provisioned throughput.** Function calling is only supported on new endpoints created with provisioned throughput. You cannot add function calling to previously created endpoints. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Google Gemini `id` field.** For Google Gemini endpoints, the `id` field on `function_call` and `function_response` is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]

### JSON Schema Limitations

Foundation Model APIs broadly support function definitions accepted by OpenAI. However, the system only supports a subset of [JSON Schema specifications](https://json-schema.org/specification). Using a simpler JSON schema for function definitions results in higher quality function call JSON generation. ^[function-calling-on-databricks-databricks-on-aws.md]

The following function call definition keys are **not supported**:

- Regular expressions using `pattern`.
- Complex nested or schema composition and validation using `anyOf`, `oneOf`, `allOf`, `prefixItems`, or `$ref`.
- Lists of types, except for the special case of `[type, "null"]` where one type in the list is a valid JSON type and the other is `"null"`. ^[function-calling-on-databricks-databricks-on-aws.md]

Additionally, the following limitations apply:

- The maximum number of keys that can be specified in the JSON schema is **16**.
- Foundation Model APIs do **not enforce** length or size constraints for objects and arrays, including keywords like `maxProperties`, `minProperties`, and `maxLength`.
- Heavily nested JSON schemas result in lower quality generation. Flattening the JSON schema improves results. ^[function-calling-on-databricks-databricks-on-aws.md]

### Token Usage Impact

Prompt injection and other techniques are used to enhance the quality of tool calls. This impacts the number of input and output tokens consumed by the model, which results in billing implications. The more tools you use, the more your input tokens increase. ^[function-calling-on-databricks-databricks-on-aws.md]

### Supported Models

Function calling is only available during model serving as part of [Foundation Model APIs](/concepts/foundation-model-apis.md) and serving endpoints that serve [External Models](/concepts/external-models.md). For a complete list of supported models, see the "Supported models" section of the function calling documentation. ^[function-calling-on-databricks-databricks-on-aws.md]

For multi-turn function calling, Databricks recommends supported Claude models. ^[function-calling-on-databricks-databricks-on-aws.md]

### Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [External Models](/concepts/external-models.md)
- [Chat Completions API](/concepts/chat-completions-api.md)
- [Structured outputs](/concepts/structured-outputs-in-foundation-model-apis.md)

### Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
