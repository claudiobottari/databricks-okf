---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48ac8442731173b289a8a5d2499d2a3dbac278f4b0b11d9afbc6e90180f18b9e
  pageDirectory: concepts
  sources:
    - query-with-the-openai-responses-api-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - responses-api-limitations-on-pay-per-token-models
    - RALOPM
  citations:
    - file: query-with-the-openai-responses-api-databricks-on-aws.md
title: Responses API Limitations on Pay-Per-Token Models
description: Restrictions on pay-per-token foundation models when using the Responses API, including unsupported parameters (background, store, previous_response_id, service_tier) and a specific set of supported tool types.
tags:
  - limitations
  - API
  - pay-per-token
  - Databricks
timestamp: "2026-06-19T20:06:24.458Z"
---

# Responses API Limitations on Pay-Per-Token Models

The **Responses API** has specific limitations when used with [Pay-per-token foundation models](/concepts/pay-per-token-foundation-model-apis.md) on Databricks. These limitations restrict which API parameters and tools are available, and they do not apply to external models. For a unified API that works across all providers, use the [Chat Completions API](/concepts/chat-completions-api.md) instead. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Unsupported Parameters

The following parameters are not supported and return a **400 error** if specified: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

- `background` — Background processing is not supported.
- `store` — Stored responses is not supported.
- `previous_response_id` — Stored responses is not supported.
- `service_tier` — Service tier selection is managed by Databricks.

These parameters are available for external models but are restricted for [pay-per-token foundation models](/concepts/pay-per-token-foundation-model-apis.md). ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Supported Tool Types

The following tool types are supported for pay-per-token foundation models: ^[query-with-the-openai-responses-api-databricks-on-aws.md]

- `function` — Traditional structured function calling
- `custom` — Custom user-defined tools
- `apply_patch` — Code patching operations
- `shell` — Shell command execution
- `image_generation` — Image generation
- `mcp` — Model Context Protocol tools
- `web_search` — Web search

## Custom Tools Requirement

Custom tools are only supported with **GPT-5 series models** through the Responses API. The supported models include `databricks-gpt-5`, `databricks-gpt-5-1`, `databricks-gpt-5-2`, `databricks-gpt-5-4`, `databricks-gpt-5-5`, and `databricks-gpt-5-5-pro`. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Tool Behavior Differences

Custom tools allow the model to return arbitrary string output instead of JSON-formatted function arguments. This is useful for code generation, applying patches, or other use cases where structured JSON is not required. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Built-in Tools

Built-in tools allow the model to call platform-provided capabilities without requiring you to implement the tool backend yourself. These tools return structured outputs and are fully managed by the platform. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Related Concepts

- [Pay-per-token foundation models](/concepts/pay-per-token-foundation-model-apis.md) — The token-based pricing model for Databricks-hosted foundation models
- [Chat Completions API](/concepts/chat-completions-api.md) — A unified alternative for querying across all model providers
- [External Models](/concepts/external-models.md) — Models not hosted by Databricks that have fewer limitations
- Function calling — Structured tool invocation on Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The broader set of APIs for serving foundation models on Databricks

## Sources

- query-with-the-openai-responses-api-databricks-on-aws.md

# Citations

1. [query-with-the-openai-responses-api-databricks-on-aws.md](/references/query-with-the-openai-responses-api-databricks-on-aws-0558036c.md)
