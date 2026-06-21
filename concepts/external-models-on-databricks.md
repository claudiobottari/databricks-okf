---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb9dd0f0826460983a196fe7a1039b61350b2c699114e4b8dbf398b95a88ad69
  pageDirectory: concepts
  sources:
    - query-a-chat-model-databricks-on-aws.md
    - query-an-embedding-model-databricks-on-aws.md
    - query-with-the-anthropic-messages-api-databricks-on-aws.md
    - supported-foundation-models-on-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - external-models-on-databricks
    - EMOD
    - OpenAI models on Databricks
  citations:
    - file: supported-foundation-models-on-model-serving-databricks-on-aws.md
    - file: query-a-chat-model-databricks-on-aws.md
    - file: query-an-embedding-model-databricks-on-aws.md
    - file: query-with-the-anthropic-messages-api-databricks-on-aws.md
title: External Models on Databricks
description: Foundation models hosted outside of Databricks but integrated through Databricks model serving endpoints.
tags:
  - databricks
  - machine-learning
  - external-models
timestamp: "2026-06-19T20:00:54.135Z"
---

# External Models on Databricks

**External Models** are foundation models that are hosted outside of Databricks—such as those provided by OpenAI or Anthropic—and are accessed through Databricks’ model serving infrastructure. They are distinct from Databricks-hosted foundation models (available via Foundation Model APIs) in that the underlying model runs on the provider’s infrastructure, not on Databricks. ^[supported-foundation-models-on-model-serving-databricks-on-aws.md]

## Overview

External models enable you to use popular third‑party LLMs while centralizing their management and governance within Databricks. You create an endpoint that points to the external provider’s model, and then query that endpoint using a unified API. This streamlines the use of multiple providers across an organization. ^[supported-foundation-models-on-model-serving-databricks-on-aws.md]

The examples in the Databricks documentation for querying chat models, embedding models, and using the Anthropic Messages API apply equally to external models. ^[query-a-chat-model-databricks-on-aws.md, query-an-embedding-model-databricks-on-aws.md, query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Configuring an External Model Endpoint

To query an external model, you must first create a serving endpoint that references the external provider and model. Instructions for creating such endpoints are provided in the documentation for creating foundation model serving endpoints for external models. ^[supported-foundation-models-on-model-serving-databricks-on-aws.md]

## Querying External Models

Databricks provides an OpenAI‑compatible API for querying external models, which works across chat, embeddings, and other task types. For Anthropic models, you may also use the native Anthropic Messages API, which is compatible only with Anthropic pay‑per‑token and external models. ^[supported-foundation-models-on-model-serving-databricks-on-aws.md, query-with-the-anthropic-messages-api-databricks-on-aws.md]

### Chat Models

When using the OpenAI client, set the `base_url` to your Databricks workspace instance and pass a Databricks API token. The following example queries an external chat model (e.g., a Claude model hosted externally):

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key="dapi-your-databricks-token",
    base_url="https://example.staging.cloud.databricks.com/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is a mixture of experts model?"}
    ],
    max_tokens=256
)
```
^[query-a-chat-model-databricks-on-aws.md]

### Embedding Models

Embedding models are queried similarly. The following example uses the OpenAI client:

```python
client = OpenAI(
    api_key="dapi-your-databricks-token",
    base_url="https://example.staging.cloud.databricks.com/serving-endpoints"
)

response = client.embeddings.create(
    model="databricks-gte-large-en",
    input="what is databricks"
)
```
^[query-an-embedding-model-databricks-on-aws.md]

### Using the Anthropic Messages API

For Anthropic external models, you can use the native Anthropic Python SDK by setting the `base_url` to the Databricks serving‑endpoints path with `/anthropic` appended. The `api_key` is unused; authentication is handled via the `Authorization` header with your Databricks token.

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
        {"role": "user", "content": "What is a mixture of experts model?"}
    ],
)
print(message.content[0].text)
```
^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

### REST API

External models can also be queried using a standard REST request. The request format follows the provider’s schema, and you may include additional parameters that are valid for the specific provider and endpoint configuration. ^[query-a-chat-model-databricks-on-aws.md]

## Supported Providers and Models

The following table (non‑exhaustive) lists supported external model providers and their models that can be configured via Databricks external model endpoints. New model versions from the same provider are typically supported even if not listed. ^[supported-foundation-models-on-model-serving-databricks-on-aws.md]

| Provider | Example Models | Endpoint Type |
|----------|----------------|---------------|
| OpenAI   | GPT‑4, GPT‑3.5‑turbo | External model |
| Anthropic | Claude 3 Opus, Claude 3.5 Sonnet | External model |
| (Other LLM providers) | Various | External model |

> **Note**: Customers are responsible for compliance with applicable model licenses. Some providers support fine‑tuned completion and chat models; in such cases, populate the `name` field in the endpoint configuration with the fine‑tuned model name. ^[supported-foundation-models-on-model-serving-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Databricks‑hosted foundation models available via pay‑per‑token or provisioned throughput.
- [Model Serving](/concepts/model-serving.md) – The underlying serving infrastructure that hosts foundation model endpoints.
- Query a chat model – Detailed query examples for chat models (including external models).
- [Query an embedding model](/concepts/text-embedding-models.md) – Detailed query examples for embedding models.
- [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md) – Provider‑specific API for Anthropic models.

## Sources

- supported-foundation-models-on-model-serving-databricks-on-aws.md
- query-a-chat-model-databricks-on-aws.md
- query-an-embedding-model-databricks-on-aws.md
- query-with-the-anthropic-messages-api-databricks-on-aws.md

# Citations

1. [supported-foundation-models-on-model-serving-databricks-on-aws.md](/references/supported-foundation-models-on-model-serving-databricks-on-aws-87287248.md)
2. [query-a-chat-model-databricks-on-aws.md](/references/query-a-chat-model-databricks-on-aws-0a958863.md)
3. [query-an-embedding-model-databricks-on-aws.md](/references/query-an-embedding-model-databricks-on-aws-18956bab.md)
4. [query-with-the-anthropic-messages-api-databricks-on-aws.md](/references/query-with-the-anthropic-messages-api-databricks-on-aws-5094c68d.md)
