---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa9f4ab9ee927ff8f1c67018b48f8f3dac51ed00a3bc5348bfe496ae5b7e4b9d
  pageDirectory: concepts
  sources:
    - provider-native-apis-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - unified-openai-compatible-api-databricks
    - UOA(
  citations:
    - file: provider-native-apis-databricks-on-aws.md
title: Unified OpenAI-compatible API (Databricks)
description: The standard, provider-agnostic API interface on Databricks Model Serving, contrasted with provider native APIs which offer access to provider-specific features.
tags:
  - databricks
  - api
  - openai-compatible
timestamp: "2026-06-19T19:59:00.585Z"
---

Here is the wiki page for "Unified OpenAI-compatible API (Databricks)".

## Unified OpenAI-compatible API (Databricks)

The **Unified OpenAI-compatible API** is a standard interface on Databricks that allows you to query supported foundation models using the same request format as the OpenAI API. It provides a consistent, provider-agnostic way to interact with models hosted on the Databricks platform.

### Overview

The Unified OpenAI-compatible API is designed to handle common use cases such as chat completions and text generation. It uses the same schema and conventions as the OpenAI API. This means that if you already have code written for the OpenAI API, you can often point it at a Databricks endpoint with minimal changes. ^[provider-native-apis-databricks-on-aws.md]

This API is the primary, recommended interface for most users because it abstracts away provider-specific details. It provides a stable, single-pattern approach to model serving. ^[provider-native-apis-databricks-on-aws.md]

### When to Use Native APIs

Provider native APIs give you direct access to provider-specific surfaces, such as the [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md) or the [Google Gemini API](/concepts/google-gemini-api-on-databricks.md). These are available when you need features beyond what the Unified OpenAI-compatible API offers.

You should consider using a native API when you need to:
- Access the latest, provider-specific features that are not yet available in the unified interface.
- Migrate existing provider SDK code to Databricks without rewriting the core logic.

However, for general-purpose querying, the Unified OpenAI-compatible API is the simpler and more portable option. ^[provider-native-apis-databricks-on-aws.md]

### Related Concepts

- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md)
- [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md)
- [Google Gemini API](/concepts/google-gemini-api-on-databricks.md)
- OpenAI API
- Chat Model Querying
- [Model Serving](/concepts/model-serving.md)

### Sources

- provider-native-apis-databricks-on-aws.md

# Citations

1. [provider-native-apis-databricks-on-aws.md](/references/provider-native-apis-databricks-on-aws-188451d9.md)
