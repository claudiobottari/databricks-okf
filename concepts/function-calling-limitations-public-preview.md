---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c5d13650931c3fc386d29d42fe6121812ba99c11e0506d8651af05fb0a6fdea
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - function-calling-limitations-public-preview
    - FCL(P
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Function Calling Limitations (Public Preview)
description: Current limitations include no parallel function calling, max 32 functions, single-turn optimization, and restricted provisioned throughput support for new endpoints only.
tags:
  - limitations
  - preview
  - function-calling
timestamp: "2026-06-19T10:40:58.245Z"
---

Here is the wiki page for "Function Calling Limitations (Public Preview)":

# Function Calling Limitations (Public Preview)

**Function Calling Limitations (Public Preview)** describes the constraints and unsupported features that apply to [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) while it remains in public preview. Understanding these limitations helps users design their GenAI application workflows to avoid incompatible configurations or unexpected behavior during model serving.

## Multi-Turn Function Calling

- Multi-turn function calling is recommended only with supported Claude models. ^[function-calling-on-databricks-databricks-on-aws.md]
- If using Llama 4 Maverick, the current function calling solution is optimized for single turn function calls. Multi-turn function calling is supported during the preview, but is under development. ^[function-calling-on-databricks-databricks-on-aws.md]
- During Public Preview, function calling on Databricks is optimized for single turn function calling. ^[function-calling-on-databricks-databricks-on-aws.md]

## Parallel Function Calling

- Parallel function calling is not supported. The model can only call one function per turn. ^[function-calling-on-databricks-databricks-on-aws.md]

## Maximum Number of Functions

- The maximum number of functions that can be defined in the `tools` parameter is 32 functions. ^[function-calling-on-databricks-databricks-on-aws.md]

## Provisioned Throughput Endpoints

- For provisioned throughput support, function calling is only supported on new endpoints. You cannot add function calling to previously created endpoints. ^[function-calling-on-databricks-databricks-on-aws.md]

## Google Gemini Endpoints

- For Google Gemini endpoints, the `id` field on `function_call` and `function_response` is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]

## JSON Schema Limitations

[Foundation Model APIs](/concepts/foundation-model-apis.md) only support a subset of JSON schema specifications. Using a simpler JSON schema for function call definitions results in higher quality function call JSON generation. ^[function-calling-on-databricks-databricks-on-aws.md]

The following function call definition keys are **not supported**: ^[function-calling-on-databricks-databricks-on-aws.md]

- Regular expressions using `pattern`.
- Complex nested or schema composition and validation using: `anyOf`, `oneOf`, `allOf`, `prefixItems`, or `$ref`.
- Lists of types except for the special case of `[type, "null"]` where one type in the list is a valid JSON type and the other is `"null"`.

Additionally, the following limitations apply: ^[function-calling-on-databricks-databricks-on-aws.md]

- The maximum number of keys specified in the JSON schema is 16.
- Foundation Model APIs does not enforce length or size constraints for objects and arrays. This includes keywords like `maxProperties`, `minProperties`, and `maxLength`.
- Heavily nested JSON schemas result in lower quality generation. If possible, try flattening the JSON schema for better results.

## Related Concepts

- [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) — The feature that these limitations apply to
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure for function calling
- [JSON Schema Specification](/concepts/json-schema-subset-for-function-calling.md) — Reference for supported schema constructs
- [Supported Models for Function Calling](/concepts/supported-models-for-function-calling-on-databricks.md) — Models that support function calling
- [Chat Completions API](/concepts/chat-completions-api.md) — API reference for function calling syntax
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Alternative for batch inference or data processing tasks
- [External Models](/concepts/external-models.md) — Model serving feature that supports function calling
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Endpoint type with special function calling support rules

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
