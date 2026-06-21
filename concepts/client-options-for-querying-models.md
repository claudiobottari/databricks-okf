---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dac02f529346610d422eac4ece948c20715a5414c7b3101e0972e4cea89e7709
  pageDirectory: concepts
  sources:
    - query-a-chat-model-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-options-for-querying-models
    - COFQM
  citations:
    - file: query-a-chat-model-databricks-on-aws.md
title: Client Options for Querying Models
description: Multiple available client interfaces for querying Databricks models including OpenAI client, REST API, SQL, MLflow Deployments SDK, Databricks Python SDK, and LangChain.
tags:
  - databricks
  - client
  - sdks
timestamp: "2026-06-19T20:01:33.413Z"
---

Here is the wiki page for "Client Options for Querying Models".

---

## Client Options for Querying Models

**Client Options for Querying Models** refers to the various programming interfaces, SDKs, and API clients that can be used to send requests to chat-optimized Foundation Models hosted on [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints. The choice of client determines the required Python package, the authentication method, and whether the model is served inside or outside the Databricks workspace.

### Overview

Databricks provides several client options for querying foundation models, including those served by [Foundation Model APIs](/concepts/foundation-model-apis.md) (Databricks-hosted) and [External Models](/concepts/external-models.md) (hosted outside of Databricks). Each client has its own configuration requirements and request format. ^[query-a-chat-model-databricks-on-aws.md]

### Client Options and Requirements

The following table summarizes the available client options and their corresponding setup requirements:

| Client | Package | Use Case |
|--------|---------|----------|
| [OpenAI Client](/concepts/openai-client-compatibility.md) (via `databricks_openai`) | `databricks-openai` | Querying Databricks-hosted models within the workspace |
| [OpenAI Client](/concepts/openai-client-compatibility.md) (direct) | `openai` | Querying foundation models hosted outside of Databricks |
| REST API | `requests` or `curl` | Direct HTTP requests to the model serving endpoint |
| SQL | Databricks SQL | Querying models via SQL statements |
| [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) | `mlflow` | Deploying and querying models via MLflow |
| Databricks Python SDK | `databricks-sdk` | Programmatic access via Databricks SDK |
| LangChain | `langchain` | Integration with LangChain frameworks |

^[query-a-chat-model-databricks-on-aws.md]

#### OpenAI Client (Inside Workspace)

To query Databricks-hosted foundation models from within the workspace, use the `databricks_openai` package. This client allows you to specify the model serving endpoint name directly as the `model` parameter. ^[query-a-chat-model-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is a mixture of experts model?"}
    ],
    max_tokens=256
)
```

#### OpenAI Client (Outside Workspace)

To query foundation models hosted outside of your workspace, you must use the standard `openai` client directly. You also need your Databricks workspace instance URL to connect the OpenAI client to Databricks. The following example assumes you have a Databricks API token and `openai` installed on your compute. ^[query-a-chat-model-databricks-on-aws.md]

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
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is a mixture of experts model?"}
    ],
    max_tokens=256
)
```

#### REST API

When using the REST API, the expected request format for a chat model includes a `messages` array with `role` and `content` fields, along with optional parameters like `max_tokens` and `temperature`. ^[query-a-chat-model-databricks-on-aws.md]

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

#### REST API Response Format

The response from a REST API request is in JSON format and includes fields such as `model`, `choices`, `usage`, and `object`. Each `choice` contains a `message` object and an `index`. The `usage` field reports token counts (`prompt_tokens`, `completion_tokens`, `total_tokens`). ^[query-a-chat-model-databricks-on-aws.md]

```json
{
  "model": "databricks-claude-sonnet-4-5",
  "choices": [
    {
      "message": {},
      "index": 0,
      "finish_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 7,
    "completion_tokens": 74,
    "total_tokens": 81
  },
  "object": "chat.completion",
  "id": null,
  "created": 1698824353
}
```

#### SQL

Client option for querying models via SQL is available but no example provided in the source material.

#### MLflow Deployments SDK

Client option for querying models via MLflow Deployments SDK is available but no example provided in the source material.

#### Databricks Python SDK

Client option for querying models via Databricks Python SDK is available but no example provided in the source material.

#### LangChain

Client option for querying models via LangChain is available but no example provided in the source material.

### External Model Query Parameters

For external models, you can include additional query parameters that are valid for a given provider and endpoint configuration. See Additional Query Parameters for details. ^[query-a-chat-model-databricks-on-aws.md]

### Related Concepts

- Query a Chat Model – Core tutorial for sending chat requests.
- [Query an Embedding Model](/concepts/text-embedding-models.md) – Tutorial for embedding requests.
- [Query Reasoning Models](/concepts/hybrid-reasoning-models.md) – Tutorial for reasoning model requests.
- Query Vision Models – Tutorial for vision model requests.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of hosted model APIs.
- [External Models](/concepts/external-models.md) – Models hosted outside of Databricks.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The target for all client requests.
- [Chat Completions API](/concepts/chat-completions-api.md) – The standard request/response format for chat models.

### Sources

- query-a-chat-model-databricks-on-aws.md

# Citations

1. [query-a-chat-model-databricks-on-aws.md](/references/query-a-chat-model-databricks-on-aws-0a958863.md)
