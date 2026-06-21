---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05ad1f28a92ef62386cc8ce60139354109bd1f3a1a067d8a7c6282cf019367f1
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-models-for-function-calling-on-databricks
    - SMFFCOD
    - Supported Models for Function Calling
    - Function Calling on Databricks
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Supported Models for Function Calling on Databricks
description: A curated list of models (Meta Llama, Mixtral, Claude, Gemini, and Databricks DBRX) available through Foundation Model APIs or External Models for function calling.
tags:
  - models
  - compatibility
  - function-calling
timestamp: "2026-06-19T10:41:41.137Z"
---

# Supported Models for Function Calling on Databricks

**Supported Models for Function Calling on Databricks** lists the large language models (LLMs) that support function calling through [Foundation Model APIs](/concepts/foundation-model-apis.md) and [External Models](/concepts/external-models.md) on the Databricks platform. Function calling enables LLMs to generate structured JSON output based on user-defined function schemas, allowing applications to reliably control model responses and integrate with external APIs or data processing workflows.

## Overview

Databricks Function Calling is OpenAI-compatible and is available during model serving. The feature is supported by a curated set of models, each made available through either Foundation Model APIs (pay-per-token or provisioned throughput) or External Models. ^[function-calling-on-databricks-databricks-on-aws.md]

For models made available by Foundation Model APIs, region availability is governed by the [Foundation Model APIs limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits). For models made available by External Models, see the [Region availability](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions) documentation. ^[function-calling-on-databricks-databricks-on-aws.md]

## Model Availability and Retirements

### Important Retirement Notices

- **Meta-Llama-3.1-405B-Instruct**: Starting February 15, 2026, this model is not available for pay-per-token workloads. Starting May 15, 2026, it is not available for provisioned throughput workloads. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and migration guidance. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Meta-Llama-3.1-70B-Instruct**: Starting December 11, 2024, Meta-Llama-3.3-70B-Instruct replaces support for Meta-Llama-3.1-70B-Instruct in Foundation Model APIs pay-per-token endpoints. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Google Gemini 3 Pro**: Will be retired on March 26, 2026. Between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro will be temporarily redirected to Gemini 3.1 Pro. The pricing for both models is identical. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and migration guidance. ^[function-calling-on-databricks-databricks-on-aws.md]

## Using Function Calling with Supported Models

To use function calling, you provide function `parameters` and a `description` in the API call using the OpenAI SDK's `tools` parameter. The model decides whether to call the defined functions and returns a JSON object of strings that adheres to the custom schema. ^[function-calling-on-databricks-databricks-on-aws.md]

The default `tool_choice` is `"auto"`, which lets the model decide which functions to call and whether to call them. You can customize this behavior:

- `tool_choice: "required"` — The model always calls one or more functions.
- `tool_choice: {"type": "function", "function": {"name": "my_function"}}` — The model calls only a specific function.
- `tool_choice: "none"` — Disables function calling; the model generates a user-facing message only.

^[function-calling-on-databricks-databricks-on-aws.md]

## Limitations

The following limitations apply during the current Public Preview:

- **Multi-turn function calling**: Databricks recommends the supported Claude models for multi-turn function calling. If using Llama 4 Maverick, the current solution is optimized for single-turn function calls; multi-turn support is under development. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Parallel function calling**: Not supported. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Maximum functions**: The maximum number of functions that can be defined in `tools` is 32 functions. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Provisioned throughput**: Function calling is only supported on new endpoints. You cannot add function calling to previously created endpoints. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Google Gemini endpoints**: The `id` field on `function_call` and `function_response` is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md) — The core feature and its usage patterns
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure for supported models
- [External Models](/concepts/external-models.md) — Another serving option for supported models
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Recommended for batch inference and data processing tasks
- [Chat Completions API](/concepts/chat-completions-api.md) — The API syntax for function calling requests

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
