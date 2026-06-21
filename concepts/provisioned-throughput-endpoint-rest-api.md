---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3cab9cf5faebe95630a63dec9b6e585b6ad29db9fb1233ace39f00bb8cd6186
  pageDirectory: concepts
  sources:
    - provisioned-throughput-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-endpoint-rest-api
    - PTERA
    - Create your provisioned throughput endpoint using the REST API
  citations:
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
title: Provisioned Throughput Endpoint REST API
description: Creating provisioned throughput serving endpoints via REST API by specifying min/max provisioned throughput fields and querying model optimization info.
tags:
  - databricks
  - api
  - serving
timestamp: "2026-06-19T19:59:22.221Z"
---

# Provisioned Throughput Endpoint REST API

The **Provisioned Throughput Endpoint REST API** allows you to programmatically create and manage model serving endpoints on Databricks that use dedicated inference capacity for foundation models. When using this API, you specify a model from [Unity Catalog](/concepts/unity-catalog.md) and define the minimum and maximum provisioned throughput in tokens per second, enabling guaranteed performance for production GenAI workloads. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Overview

Provisioned throughput endpoints allocate dedicated inference capacity in chunks of [Model Units](/concepts/model-units.md). The API lets you set `min_provisioned_throughput` and `max_provisioned_throughput` fields to control the scaling range. The system automatically scales within that range. To identify the correct range, you must first query the model optimization information API, which returns a `throughput_chunk_size` value specific to the model. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Key Endpoints

| Operation | HTTP Method | Path | Description |
|-----------|-------------|------|-------------|
| Create serving endpoint | POST | `/api/2.0/serving-endpoints` | Creates a new provisioned throughput endpoint |
| Get model optimization info | GET | `/api/2.0/serving-endpoints/get-model-optimization-info/{registered_model_name}/{version}` | Returns whether a model is optimizable and its throughput chunk size |

^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Creating an Endpoint with the REST API

To deploy a model in provisioned throughput mode:

1. **Get model optimization info** – Call the GET endpoint to verify the model is eligible and retrieve its `throughput_chunk_size`.
2. **Define `min_provisioned_throughput` and `max_provisioned_throughput`** – These must be multiples of `throughput_chunk_size`. For example, if `chunk_size` is 980 tokens per second, you might set `min_provisioned_throughput = 2 * 980 = 1960` and `max_provisioned_throughput = 3 * 980 = 2940`.
3. **Send the POST request** – Provide the endpoint name, model name, version, and the throughput fields in the `served_entities` configuration.

Below is a Python example using the `requests` library: ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

```python
import requests, json

endpoint_name = "prov-throughput-endpoint"
model_name = "ml.llm-catalog.foundation-model"
model_version = 3
API_ROOT = "<YOUR-API-URL>"
API_TOKEN = "<YOUR-API-TOKEN>"

headers = {"Context-Type": "text/json", "Authorization": f"Bearer {API_TOKEN}"}

# Get optimization info
optimizable_info = requests.get(
    url=f"{API_ROOT}/api/2.0/serving-endpoints/get-model-optimization-info/{model_name}/{model_version}",
    headers=headers
).json()

if 'optimizable' not in optimizable_info or not optimizable_info['optimizable']:
    raise ValueError("Model is not eligible for provisioned throughput")

chunk_size = optimizable_info['throughput_chunk_size']

min_provisioned_throughput = 2 * chunk_size
max_provisioned_throughput = 3 * chunk_size

# Create endpoint
data = {
    "name": endpoint_name,
    "config": {
        "served_entities": [
            {
                "entity_name": model_name,
                "entity_version": model_version,
                "min_provisioned_throughput": min_provisioned_throughput,
                "max_provisioned_throughput": max_provisioned_throughput,
            }
        ]
    }
}

response = requests.post(
    url=f"{API_ROOT}/api/2.0/serving-endpoints",
    json=data,
    headers=headers
)
print(json.dumps(response.json(), indent=4))
```

## Model Optimization Info API

Use the GET endpoint to check eligibility and retrieve the throughput chunk size:

```
GET api/2.0/serving-endpoints/get-model-optimization-info/{registered_model_name}/{version}
```

Example response:

```json
{
  "optimizable": true,
  "model_type": "llama",
  "throughput_chunk_size": 980
}
```

The `throughput_chunk_size` is measured in tokens per second and varies by model. This value must be used as the granularity when setting `min_provisioned_throughput` and `max_provisioned_throughput`. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Log Probability for Chat Completion Tasks

For chat completion models, the API supports a `logprobs` parameter that returns the log probability of each sampled token. This is useful for classification, uncertainty estimation, and running evaluation metrics. See the [Chat Completions API](/concepts/chat-completions-api.md) reference for parameter details. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Limitations

- Model deployment may fail due to GPU capacity issues, resulting in a timeout during endpoint creation or update. Contact your Databricks account team if this occurs. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]
- Only certain model architectures are supported for provisioned throughput; see [Supported foundation models on Model Serving](/concepts/foundation-model-serving-modes.md) for the list. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Overview of dedicated inference capacity.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The general API category for hosting foundation models.
- [Model Units](/concepts/model-units.md) – Units of compute allocation for provisioned throughput.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The serving endpoint resource managed via this API.
- [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md) – An alternative Python SDK for creating endpoints.
- [Unity Catalog](/concepts/unity-catalog.md) – Where foundation models are registered (catalog `system`, schema `ai`).

## Sources

- provisioned-throughput-foundation-model-apis-databricks-on-aws.md

# Citations

1. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
