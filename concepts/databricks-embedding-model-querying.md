---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 897b63e83b7698bc79450582e45f5f530f316a20fa3f0d3226aca1d68f1b2c54
  pageDirectory: concepts
  sources:
    - query-an-embedding-model-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-embedding-model-querying
    - DEMQ
  citations:
    - file: query-an-embedding-model-databricks-on-aws.md
title: Databricks Embedding Model Querying
description: How to write and send query requests to foundation models optimized for embeddings tasks via Databricks model serving endpoints.
tags:
  - embedding-models
  - databricks
  - model-serving
  - querying
timestamp: "2026-06-19T20:01:08.103Z"
---

# Databricks Embedding Model Querying

**Databricks Embedding Model Querying** refers to the process of sending inference requests to foundation models that are optimized for embeddings tasks, using the Databricks Model Serving endpoint. These models convert text inputs into numerical vectors (embeddings) that capture semantic meaning, which are commonly used in search, [recommendation systems](/concepts/two-tower-models-for-recommendation-systems.md), and [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) pipelines. ^[query-an-embedding-model-databricks-on-aws.md]

The query examples in this article apply to two categories of models: **Databricks-hosted foundation models** made available through [Foundation Models APIs](/concepts/foundation-model-apis.md), and **foundation models hosted outside Databricks** accessed via [External Models](/concepts/external-models.md). ^[query-an-embedding-model-databricks-on-aws.md]

## Requirements

To query an embedding model on Databricks, you must meet the following prerequisites:
- Have the necessary permissions and API tokens for the model serving endpoint.
- Install the appropriate client package on your compute cluster, such as `openai`, `databricks-openai`, or the Databricks Python SDK, depending on the client option you choose. ^[query-an-embedding-model-databricks-on-aws.md]

## Query Examples

Embedding requests can be made using several client options, including the OpenAI client, SQL, REST API, MLflow Deployments SDK, Databricks Python SDK, and LangChain. The examples below demonstrate the request and response formats.

### Using the OpenAI Client

To use the Databricks-provided OpenAI client (`DatabricksOpenAI`), specify the model serving endpoint name as the `model` parameter, for example `databricks-gte-large-en`. ^[query-an-embedding-model-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
response = client.embeddings.create(
  model="databricks-gte-large-en",
  input="what is databricks"
)
```

To query a foundation model hosted outside your workspace (an external model), use the standard OpenAI client directly, configuring it with your Databricks workspace instance URL and an API token: ^[query-an-embedding-model-databricks-on-aws.md]

```python
import os
import openai
from openai import OpenAI

client = OpenAI(
    api_key="dapi-your-databricks-token",
    base_url="https://example.staging.cloud.databricks.com/serving-endpoints"
)

response = client.embeddings.create(
  model="databricks-gte-large-en",
  input="what is databricks"
)
```

### Using the REST API

The standard request format for an embedding model endpoint expects a JSON object with an `input` field containing an array of strings. For external models, you may include additional parameters that are valid for the provider and endpoint configuration. ^[query-an-embedding-model-databricks-on-aws.md]

```bash
{
  "input": [
    "embedding text"
  ]
}
```

The expected response contains the embedding vectors, model identifier, and token usage statistics: ^[query-an-embedding-model-databricks-on-aws.md]

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": []
    }
  ],
  "model": "text-embedding-ada-002-v2",
  "usage": {
    "prompt_tokens": 2,
    "total_tokens": 2
  }
}
```

## Supported Models

For a current list of supported embedding models available through Foundation Models APIs, see the documentation on Foundation model types. ^[query-an-embedding-model-databricks-on-aws.md]

## Checking Whether Embeddings Are Normalized

You can verify whether the embeddings returned by a model are unit-normalized (L2 norm equal to 1) using the following utility function: ^[query-an-embedding-model-databricks-on-aws.md]

```python
import numpy as np

def is_normalized(vector: list[float], tol=1e-3) -> bool:
    magnitude = np.linalg.norm(vector)
    return abs(magnitude - 1) < tol
```

## Additional Resources

- Query a chat model
- Query reasoning models
- Query vision models

## Sources

- query-an-embedding-model-databricks-on-aws.md

# Citations

1. [query-an-embedding-model-databricks-on-aws.md](/references/query-an-embedding-model-databricks-on-aws-18956bab.md)
