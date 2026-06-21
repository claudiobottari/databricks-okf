---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7db738e05fd85876478c2fb42ab20b7eaf435a875823bcb334daa2884f295f6a
  pageDirectory: concepts
  sources:
    - provider-native-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-native-apis-databricks
    - PNA(
    - Provider Native APIs
    - Provider native APIs
  citations:
    - file: provider-native-apis-databricks-on-aws.md
title: Provider Native APIs (Databricks)
description: Direct access to provider-specific API surfaces (OpenAI, Anthropic, Google) on Databricks Model Serving, bypassing the unified OpenAI-compatible API to use latest provider features.
tags:
  - databricks
  - model-serving
  - api
timestamp: "2026-06-19T19:58:49.094Z"
---

# Provider Native APIs (Databricks)

**Provider Native APIs** on Databricks give you direct access to provider-specific API surfaces when you need features beyond the unified OpenAI-compatible APIs. These APIs allow you to access the latest provider-specific features or to migrate existing provider SDK code to Databricks without rewriting your application logic. ^[provider-native-apis-databricks-on-aws.md]

## Overview

While Databricks provides a unified OpenAI-compatible API for querying foundation models, some use cases require access to provider-specific capabilities that are not available through the standard interface. Provider Native APIs bridge this gap by exposing the native API surfaces of supported model providers directly through Databricks. ^[provider-native-apis-databricks-on-aws.md]

## Requirements

To use Provider Native APIs, you must meet the same requirements as for scoring foundation models generally. Additionally, you must install the appropriate package to your cluster based on the provider you choose. ^[provider-native-apis-databricks-on-aws.md]

## Available Native APIs

The following provider-native APIs are available on Databricks:

| Provider | API | Compatible Models | Supported Input Types |
|---|---|---|---|
| OpenAI | [OpenAI Responses API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-openai-responses) | GPT-5 series, GPT-4o | text, image |
| Anthropic | [Anthropic Messages API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-anthropic-messages) | Claude models | text, image |
| Google | [Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api) | Gemini models | text, image, video, audio |

^[provider-native-apis-databricks-on-aws.md]

For per-model input type details, see the documentation on [Databricks-hosted foundation models available in Foundation Model APIs](/concepts/databricks-model-serving-foundation-model-apis-fmapi.md). ^[provider-native-apis-databricks-on-aws.md]

## Use Cases

Provider Native APIs are particularly useful in the following scenarios:

- **Accessing latest provider features**: When a provider releases new capabilities that are not yet available through the unified API, you can use the native API to access them immediately. ^[provider-native-apis-databricks-on-aws.md]
- **Migrating existing code**: If you have existing code that uses a provider's SDK directly, you can migrate it to Databricks with minimal changes by using the native API surface. ^[provider-native-apis-databricks-on-aws.md]
- **Multimodal inputs**: Some native APIs support input types beyond text and images, such as video and audio (available through the Google Gemini API). ^[provider-native-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The unified API surface for querying foundation models on Databricks.
- Query a chat model — Using the chat completion interface for conversational AI.
- Use foundation models — General guidance on scoring foundation models.
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) — The catalog of available models and their capabilities.
- [Model Serving](/concepts/model-serving.md) — The infrastructure that hosts and serves models on Databricks.

## Sources

- provider-native-apis-databricks-on-aws.md

# Citations

1. [provider-native-apis-databricks-on-aws.md](/references/provider-native-apis-databricks-on-aws-188451d9.md)
