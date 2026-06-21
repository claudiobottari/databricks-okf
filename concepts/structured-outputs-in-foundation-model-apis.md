---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9222dcd51a64b1e3525f1650faea77d22209f2b1f87ac6619defdf23b00a48b8
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - structured-outputs-in-foundation-model-apis
    - SOIFMA
    - Structured Output Generation
    - Structured Outputs
    - Structured Outputs (Databricks)
    - Structured outputs
    - Structured outputs on Databricks
    - structured output
    - structured outputs
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Structured Outputs in Foundation Model APIs
description: A feature allowing specification of output format via JSON Schema in Databricks Foundation Model API requests, supported across both Responses and Chat Completions APIs.
tags:
  - api
  - structured-outputs
  - databricks
timestamp: "2026-06-19T10:39:30.811Z"
---

# Structured Outputs in Foundation Model APIs

**Structured Outputs in Foundation Model APIs** refers to the mechanism that allows users to specify a desired output format — most commonly a JSON Schema — when querying a model through the Databricks Foundation Model APIs. By providing a schema, callers can constrain the model’s response to adhere to a predefined structure, which is essential for programmatic consumption, data extraction, and integration with downstream systems. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Overview

Structured outputs are supported in two of the major API families provided by Databricks Foundation Model APIs: the [Chat Completions API](/concepts/chat-completions-api.md) and the [Responses API](/concepts/responses-api.md). Both APIs accept a `response_format` object that can specify a JSON Schema definition. The model then returns a response that matches the given schema, rather than free‑form text. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Using Structured Outputs in the Chat Completions API

In the Chat Completions API, structured outputs are configured via the `response_format` field of the request body. The field uses the `ResponseFormatObject` type, which contains a `json_schema` object. The `json_schema` object follows the structure of `JsonSchemaObject`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

The `JsonSchemaObject` is documented under the [Structured outputs on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs) guide. It defines the expected schema for the model’s response, such as required fields, types, and nested properties. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

For more details, see the `ResponseFormatObject` and `JsonSchemaObject` definitions in the Foundation Model REST API reference. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Using Structured Outputs in the Responses API

The Responses API, which is compatible only with OpenAI models, also supports structured outputs. A `TextConfig` object in the request contains an optional `format` field of type `ResponsesFormatObject`. As in the Chat Completions API, the `json_schema` object inside this type has the same structure as `JsonSchemaObject`. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

This allows callers to enforce a structured response when using the Responses API for multi‑turn conversations or other tasks. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The overarching service that hosts and serves foundation models on Databricks.
- [Chat Completions API](/concepts/chat-completions-api.md) – The REST API for multi‑turn chat conversations.
- [Responses API](/concepts/responses-api.md) – An alternative API for OpenAI models that uses `input` instead of `messages`.
- JSON Schema – The standard used to define the expected structure of model outputs.
- [Structured Output Generation](/concepts/structured-outputs-in-foundation-model-apis.md) – Broader topic of constraining model outputs to a specific format.

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
