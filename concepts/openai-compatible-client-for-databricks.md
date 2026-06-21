---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7abff29fe2eb6449610ceb9ae46d9ee85e858d016259ea57563b24b78cec24b1
  pageDirectory: concepts
  sources:
    - query-a-chat-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - openai-compatible-client-for-databricks
    - OCFD
  citations:
    - file: query-a-chat-model-databricks-on-aws.md
title: OpenAI-Compatible Client for Databricks
description: Using the OpenAI Python client to query Databricks-hosted chat models with a familiar chat completions interface.
tags:
  - databricks
  - openai
  - api-client
timestamp: "2026-06-19T20:01:37.034Z"
---

# OpenAI-Compatible Client for Databricks

The **OpenAI-Compatible Client for Databricks** enables users to query foundation models served through Databricks model serving endpoints using the familiar OpenAI client API. This allows developers to leverage Databricks-hosted or externally hosted foundation models with minimal code changes when migrating from OpenAI. ^[query-a-chat-model-databricks-on-aws.md]

## Overview

The OpenAI-compatible client provides a drop-in replacement for standard OpenAI client code, allowing users to interact with Databricks model serving endpoints using the same `chat.completions.create()` pattern. This applies to foundation models made available through either [Foundation Models APIs](/concepts/foundation-model-apis.md) (Databricks-hosted foundation models) or [External Models](/concepts/external-models.md) (foundation models hosted outside of Databricks). ^[query-a-chat-model-databricks-on-aws.md]

## Usage

### Using the Databricks OpenAI Client

The `databricks_openai` package provides a Databricks-specific client that handles authentication and endpoint routing automatically within a Databricks workspace. ^[query-a-chat-model-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()

response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What is a mixture of experts model?",
      }
    ],
    max_tokens=256
)
```

The `model` parameter specifies the Databricks model serving endpoint name. ^[query-a-chat-model-databricks-on-aws.md]

### Using the Standard OpenAI Client

To query foundation models outside of your workspace, you must use the standard OpenAI client directly with your Databricks workspace instance and API token. This requires having the `openai` package installed on your compute. ^[query-a-chat-model-databricks-on-aws.md]

```python
import os
import openai
from openai import OpenAI

client = OpenAI(
    api_key="dapi-your-databricks-token",
    base_url="https://example.staging.cloud.databricks.com/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What is a mixture of experts model?",
      }
    ],
    max_tokens=256
)
```

The `base_url` should point to your Databricks workspace's serving endpoints URL. ^[query-a-chat-model-databricks-on-aws.md]

## Client Options

Users can query chat models using any of the following client options: ^[query-a-chat-model-databricks-on-aws.md]

- **OpenAI Chat Completions** – Using either `databricks_openai` or standard `openai` client
- **OpenAI Responses** – For response-based model interactions
- **SQL** – Using [AI Functions](/concepts/ai-functions.md) for batch inference
- **REST API** – Direct HTTP requests to the serving endpoint
- **MLflow Deployments SDK** – Using MLflow's deployment client
- **Databricks Python SDK** – Using Databricks' native SDK
- **LangChain** – Through LangChain's integration with Databricks

## REST API Format

When using the REST API directly, the request format mirrors the OpenAI chat completions API: ^[query-a-chat-model-databricks-on-aws.md]

```bash
{
  "messages": [
    {
      "role": "user",
      "content": "What is a mixture of experts model?"
    }
  ],
  "max_tokens": 100,
  "temperature": 0.1
}
```

The response follows a similar structure to OpenAI's response format, including model name, choices, usage statistics, and metadata. ^[query-a-chat-model-databricks-on-aws.md]

## Supported Models

See Foundation model types for supported chat models available through the OpenAI-compatible client. ^[query-a-chat-model-databricks-on-aws.md]

## Requirements

- See the [Model Serving](/concepts/model-serving.md) requirements documentation for prerequisites
- Install the appropriate package based on your chosen client option ^[query-a-chat-model-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The endpoints that host the models being queried
- [Foundation Models APIs](/concepts/foundation-model-apis.md) – Databricks-hosted foundation model offerings
- [External Models](/concepts/external-models.md) – Foundation models hosted outside of Databricks
- [Query an embedding model](/concepts/text-embedding-models.md) – Using the same client for embedding models
- Query reasoning models – Querying reasoning-optimized models
- Query vision models – Querying vision-capable models
- [AI Functions](/concepts/ai-functions.md) – Batch inference using SQL-based AI functions

## Sources

- query-a-chat-model-databricks-on-aws.md

# Citations

1. [query-a-chat-model-databricks-on-aws.md](/references/query-a-chat-model-databricks-on-aws-0a958863.md)
