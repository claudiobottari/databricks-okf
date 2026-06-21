---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2340381c5fd2aa6c2bcd3223071917c2c042bb8b4ed736637675059b6f5507ca
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-impact-of-function-definitions
    - TIOFD
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Token Impact of Function Definitions
description: The use of tool definitions increases input token consumption and billing because prompt injection and other techniques are applied to improve tool-call quality.
tags:
  - billing
  - tokens
  - function-calling
  - performance
timestamp: "2026-06-19T18:56:16.016Z"
---

# Token Impact of Function Definitions

The **Token Impact of Function Definitions** refers to the effect that defining and using function calling tools has on the number of input and output tokens consumed by a large language model (LLM), which in turn affects billing and performance. When you describe functions using JSON schemas in the `tools` parameter of an API call, those function definitions are injected into the model's context, increasing the total token count for each request. ^[function-calling-on-databricks-databricks-on-aws.md]

## How Function Definitions Affect Token Usage

When you use [Function Calling](/concepts/llm-function-calling.md) on Databricks, the function definitions you provide in the `tools` parameter are incorporated into the model's input prompt through prompt injection and other techniques used to enhance the quality of tool calls. This injection directly increases the number of input tokens consumed by the model. ^[function-calling-on-databricks-databricks-on-aws.md]

The more functions you define, the more your input tokens increase. Each function's `name`, `description`, and `parameters` (including the JSON schema for parameter types, enumerations, and descriptions) all contribute to the token count. ^[function-calling-on-databricks-databricks-on-aws.md]

## Billing Implications

Because [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks bill based on token consumption, the increased input tokens from function definitions carry direct cost implications. When you add function definitions to a request, you are paying for both the model's reasoning about the functions and the structured JSON generation output. ^[function-calling-on-databricks-databricks-on-aws.md]

## Best Practices for Minimizing Token Impact

To manage the token impact of function definitions:

- **Keep function descriptions concise** — Verbose descriptions increase token consumption without necessarily improving generation quality.
- **Limit the number of functions** — The maximum number of functions that can be defined in `tools` is 32. Using fewer functions reduces input token overhead.
- **Flatten JSON schemas** — Heavily nested JSON schemas not only result in lower quality generation but may also increase token counts.
- **Limit schema complexity** — The maximum number of keys specified in the JSON schema is 16. Simpler schemas use fewer tokens.

## Relationship to Other Concepts

- [Function Calling](/concepts/llm-function-calling.md) — The broader feature that enables structured LLM output generation.
- JSON Schema Support in Function Calling — The subset of JSON schema specifications supported by Foundation Model APIs.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure through which function calling is available.
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — An alternative for batch inference that does not require function definitions in every call.

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
