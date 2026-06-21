---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50833c54129d84b4021577d3e86172eab039f7084389c40cb5ac5981f63c42a5
  pageDirectory: concepts
  sources:
    - provider-native-apis-databricks-on-aws.md
    - query-with-the-anthropic-messages-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - anthropic-messages-api-on-databricks
    - AMA(D
    - Anthropic Messages API
    - Query with the Anthropic Messages API
  citations:
    - file: provider-native-apis-databricks-on-aws.md
    - file: query-with-the-anthropic-messages-api-databricks-on-aws.md
title: Anthropic Messages API (on Databricks)
description: Databricks-hosted access to Anthropic's Messages API for Claude models, supporting text and image inputs.
tags:
  - anthropic
  - databricks
  - api
timestamp: "2026-06-19T19:58:56.066Z"
---

# Anthropic Messages API (on Databricks)

The **Anthropic Messages API** on Databricks provides native Anthropic SDK compatibility for Claude models, enabling direct access to Anthropic-specific API features through Databricks serving endpoints. ^[provider-native-apis-databricks-on-aws.md, query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Overview

The Anthropic Messages API is one of several [Provider Native APIs](/concepts/provider-native-apis-databricks.md) available on Databricks, alongside the [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md) and [Google Gemini API](/concepts/google-gemini-api-on-databricks.md). ^[provider-native-apis-databricks-on-aws.md] It gives you direct access to provider-specific API surfaces when you need features beyond the unified OpenAI-compatible APIs. Use this API to access the latest Anthropic-specific features or to migrate existing Anthropic SDK code to Databricks. ^[provider-native-apis-databricks-on-aws.md]

## Compatibility

The Anthropic Messages API is only compatible with Anthropic pay-per-token foundation models and external models. For a unified API that works across all providers, use the [Chat Completions API](/concepts/chat-completions-api.md). ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Requirements

- See the general requirements for [scoring foundation models](/concepts/foundation-model-apis.md). ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]
- Install the `anthropic` package on your compute. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Query Examples

The following example shows how to query a Foundation Model API pay-per-token endpoint using the Anthropic Messages API with the Python SDK: ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

```python
import anthropic
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = anthropic.Anthropic(
    api_key="unused",
    base_url="https://example.staging.cloud.databricks.com/serving-endpoints/anthropic",
    default_headers={
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
    },
)

message = client.messages.create(
    model="databricks-claude-sonnet-4-5",
    max_tokens=256,
    messages=[
        {"role": "user", "content": "What is a mixture of experts model?"},
    ],
)

print(message.content[0].text)
```

The API is also accessible via REST API. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Supported Models

### Databricks-Hosted Foundation Models

The following Claude models are available through the Anthropic Messages API on Databricks: ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

- `databricks-claude-opus-4-7`
- `databricks-claude-opus-4-6`
- `databricks-claude-sonnet-4-6`
- `databricks-claude-sonnet-4-5`
- `databricks-claude-haiku-4-5`
- `databricks-claude-opus-4-5`
- `databricks-claude-opus-4-1`
- `databricks-claude-sonnet-4`

**Note:** Anthropic Claude 3.7 Sonnet was retired on April 12, 2026. See [Retired Models Policy](/concepts/partner-model-retirement-policy.md) for the recommended replacement model and migration guidance. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

### External Models

The API supports external models from the Anthropic model provider and the Bedrock Anthropic model provider. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Supported Input Types

Anthropic Claude models on Databricks accept text and image inputs. See Query Vision Models for image format and size requirements. For per-model input types, see [Databricks-Hosted Foundation Models Available in Foundation Model APIs](/concepts/databricks-hosted-foundation-models.md). ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Related Concepts

- [Provider Native APIs](/concepts/provider-native-apis-databricks.md) — Overview of all provider-specific APIs on Databricks
- [Chat Completions API](/concepts/chat-completions-api.md) — Unified API that works across all providers
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — General serving infrastructure for foundation models
- Scoring Foundation Models — Requirements and setup for using foundation models
- [External Models](/concepts/external-models.md) — Using externally hosted models through Databricks

## Sources

- provider-native-apis-databricks-on-aws.md
- query-with-the-anthropic-messages-api-databricks-on-aws.md

# Citations

1. [provider-native-apis-databricks-on-aws.md](/references/provider-native-apis-databricks-on-aws-188451d9.md)
2. [query-with-the-anthropic-messages-api-databricks-on-aws.md](/references/query-with-the-anthropic-messages-api-databricks-on-aws-5094c68d.md)
