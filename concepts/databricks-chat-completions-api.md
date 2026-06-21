---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b2d9962410d59d96e8428ead5b4218f6c725d891bfbcccd975c630dff677a145
  pageDirectory: concepts
  sources:
    - query-with-the-anthropic-messages-api-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-chat-completions-api
    - DCCA
  citations:
    - file: query-with-the-anthropic-messages-api-databricks-on-aws.md
title: Databricks Chat Completions API
description: A unified API on Databricks that works across all model providers, mentioned as an alternative to the Anthropic-specific Messages API.
tags:
  - model-serving
  - api
  - unified
timestamp: "2026-06-19T20:05:39.672Z"
---

#Databricks Chat Completions API

The **Databricks Chat Completions API** is a unified API endpoint for querying chat models across all supported providers on Databricks. It is designed to work with any provider's chat model, including Anthropic, OpenAI, and others, through a single interface. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Comparison with Provider-Specific APIs

Provider-specific APIs, such as the [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md), are only compatible with their respective pay‑per‑token foundation models and external models. When you need a single API that works across all providers — for example, to switch between Claude, GPT, and Llama models without changing your client code — the Chat Completions API is the recommended choice. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Usage Context

The Chat Completions API is documented as part of the [Model Serving](/concepts/model-serving.md) guide on Databricks. It is the standard way to query chat models when provider‑agnosticism is desired, and it is referenced as the alternative to the Anthropic‑specific Messages API. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Related Concepts

- [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md) – Provider‑specific API for Anthropic Claude models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pay‑per‑token endpoints for Databricks‑hosted models.
- [External Models](/concepts/external-models.md) – Models hosted outside Databricks but served through Databricks.
- [Model Serving](/concepts/model-serving.md) – The infrastructure used to deploy and query models.

## Sources

- query-with-the-anthropic-messages-api-databricks-on-aws.md

# Citations

1. [query-with-the-anthropic-messages-api-databricks-on-aws.md](/references/query-with-the-anthropic-messages-api-databricks-on-aws-5094c68d.md)
