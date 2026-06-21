---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 558a5eb926cd073e207ad53c80f6f7690b37a4c39b21c19a298ab14b5750c6d3
  pageDirectory: concepts
  sources:
    - query-with-the-anthropic-messages-api-databricks-on-aws.md
  confidence: 0.75
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - pay-per-token-foundation-models-on-databricks
    - PFMOD
  citations:
    - file: query-with-the-anthropic-messages-api-databricks-on-aws.md
title: Pay-Per-Token Foundation Models on Databricks
description: A pricing model for foundation models on Databricks where users are charged per token consumed, supported by the Anthropic Messages API for hosted Claude models.
tags:
  - pricing
  - model-serving
  - foundation-models
timestamp: "2026-06-19T20:05:36.044Z"
---

# Pay-Per-Token Foundation Models on Databricks

**Pay-Per-Token Foundation Models** are a class of [Foundation Model APIs](/concepts/foundation-model-apis.md) hosted by Databricks that are billed based on the number of input and output tokens consumed. These models are accessed through specialized APIs that provide native SDK compatibility for specific providers, such as Claude models via the Anthropic Messages API.

## Overview

The Anthropic Messages API is explicitly designed for use with Anthropic pay-per-token foundation models and external models. It offers native Anthropic SDK compatibility, making it suitable for users who need Anthropic‑specific features or are migrating existing Anthropic SDK code. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

For a unified API that works across all providers (including pay-per-token models), Databricks recommends the [Chat Completions API](/concepts/chat-completions-api.md). ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Requirements

- An active Databricks workspace with the ability to query foundation model endpoints. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]
- The `anthropic` Python package installed on the compute environment. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]
- A Databricks authentication token (bearer token) for API calls. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Supported Models

The following Anthropic Claude pay-per-token foundation models are available through the Anthropic Messages API on Databricks:

- `databricks-claude-opus-4-7`
- `databricks-claude-opus-4-6`
- `databricks-claude-sonnet-4-6`
- `databricks-claude-sonnet-4-5`
- `databricks-claude-haiku-4-5`
- `databricks-claude-opus-4-1`
- `databricks-claude-sonnet-4`

^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

> **Note:** Anthropic Claude 3.7 Sonnet was retired on April 12, 2026. See the [Retired Models Policy](/concepts/partner-model-retirement-policy.md) for replacement guidance.

## Access Methods

### Anthropic Messages API (Python example)

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

^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

### REST API

The same endpoint can be invoked directly via HTTP POST requests against the serving endpoint URL, using the same authentication and payload structure. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Input Types

Anthropic Claude models on Databricks accept both **text** and **image** inputs. For image format and size requirements, see Query Vision Models. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Related Concepts

- [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md)
- [Chat Completions API](/concepts/chat-completions-api.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- Query a Chat Model
- [External Models](/concepts/external-models.md)
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md)

## Sources

- query-with-the-anthropic-messages-api-databricks-on-aws.md

# Citations

1. [query-with-the-anthropic-messages-api-databricks-on-aws.md](/references/query-with-the-anthropic-messages-api-databricks-on-aws-5094c68d.md)
