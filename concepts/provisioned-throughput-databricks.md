---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d28aaf990a0d1ed5f158688943bb1d66a5ee4e6b123d750541410ce1413f100f
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
    - provisioned-throughput-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-databricks
    - PT(
  citations:
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Provisioned Throughput (Databricks)
description: A deployment option for production workloads using base or fine-tuned models with performance guarantees, as opposed to pay-per-token pricing.
tags:
  - databricks
  - provisioned-throughput
  - deployment
timestamp: "2026-06-18T11:23:29.133Z"
---

# Provisioned Throughput (Databricks)

**Provisioned Throughput** is a deployment mode for foundation models on Databricks Model Serving that allocates dedicated inference capacity with performance guarantees. It is designed for production workloads requiring consistent throughput and optimized inference for supported foundation model architectures.^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Overview

When you create a provisioned throughput model serving endpoint on Databricks, you allocate dedicated inference capacity to ensure consistent throughput for the foundation model you want to serve. Model serving endpoints that serve foundation models can be provisioned in chunks of [Model Units](/concepts/model-units.md). The number of model units you allocate allows you to purchase exactly the throughput required to reliably support your production GenAI application.^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

Provisioned throughput is distinct from [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md), which provide base models for immediate use without performance guarantees. Databricks recommends provisioned throughput for production workloads.^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md, create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Supported Models

For a list of supported model architectures for provisioned throughput endpoints, see [Supported foundation models on Model Serving](/concepts/foundation-model-serving-modes.md).^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

Base models and fine-tuned variants of foundation models made available using Foundation Model APIs provisioned throughput can be deployed.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Requirements

See the requirements for [Foundation Model APIs](/concepts/foundation-model-apis.md).^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Creating a Provisioned Throughput Endpoint

### Recommended: Deploy from Unity Catalog

Databricks recommends using the foundation models that are pre-installed in Unity Catalog. You can find these models under the catalog `system` in the schema `ai` (`system.ai`).^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

To deploy a foundation model from Unity Catalog:

1. Navigate to `system.ai` in Catalog Explorer.
2. Click on the name of the model to deploy.
3. On the model page, click the **Serve this model** button.
4. The **Create serving endpoint** page appears.

> **Note:** To deploy a Meta Llama model from `system.ai` in Unity Catalog, you must choose the applicable **Instruct** version. Base versions of the Meta Llama models are not supported for deployment from Unity Catalog.^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Using the UI

After the logged model is in Unity Catalog, create a provisioned throughput serving endpoint with the following steps:

1. Navigate to the **Serving UI** in your workspace.
2. Select **Create serving endpoint**.
3. In the **Entity** field, select your model from Unity Catalog. For eligible models, the UI for the served entity shows the **Provisioned Throughput** screen.
4. In the **Up to** dropdown you can configure the maximum tokens per second throughput for your endpoint.
   - Provisioned throughput endpoints automatically scale, so you can select **Modify** to view the minimum tokens per second your endpoint can scale down to.

^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Using the REST API

To deploy your model in provisioned throughput mode using the REST API, you must specify `min_provisioned_throughput` and `max_provisioned_throughput` fields in your request. If you prefer Python, you can also create an endpoint using the [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md).^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

To identify the suitable range of provisioned throughput for your model, use the model optimization information API:

```bash
GET api/2.0/serving-endpoints/get-model-optimization-info/{registered_model_name}/{version}
```

The following is an example response from the API:

```json
{
  "optimizable": true,
  "model_type": "llama",
  "throughput_chunk_size": 980
}
```

^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

The following Python example demonstrates creating a provisioned throughput endpoint:

```python
import requests
import json

# Set the name of the MLflow endpoint
endpoint_name = "prov-throughput-endpoint"

# Name of the registered MLflow model
model_name = "ml.llm-catalog.foundation-model"

# Get the latest version of the MLflow model
model_version = 3

# Get the API endpoint and token for the current notebook context
API_ROOT = "<YOUR-API-URL>"
API_TOKEN = "<YOUR-API-TOKEN>"

headers = {"Context-Type": "text/json", "Authorization": f"Bearer {API_TOKEN}"}

optimizable_info = requests.get(
  url=f"{API_ROOT}/api/2.0/serving-endpoints/get-model-optimization-info/{model_name}/{model_version}",
  headers=headers
).json()

if 'optimizable' not in optimizable_info or not optimizable_info['optimizable']:
  raise ValueError("Model is not eligible for provisioned throughput")

chunk_size = optimizable_info['throughput_chunk_size']

# Minimum desired provisioned throughput
min_provisioned_throughput = 2 * chunk_size

# Maximum desired provisioned throughput
max_provisioned_throughput = 3 * chunk_size

# Send the POST request to create the serving endpoint
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
  },
}

response = requests.post(
  url=f"{API_ROOT}/api/2.0/serving-endpoints", json=data, headers=headers
)

print(json.dumps(response.json(), indent=4))
```

^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Log Probability for Chat Completion Tasks

For chat completion tasks, you can use the `logprobs` parameter to provide the log probability of a token being sampled as part of the large language model generation process. You can use `logprobs` for a variety of scenarios including classification, assessing model uncertainty, and running evaluation metrics. See [Chat Completions API](/concepts/chat-completions-api.md) for parameter details.^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Limitations

Model deployment might fail due to GPU capacity issues, which results in a timeout during endpoint creation or update. Reach out to your Databricks account team to help resolve.^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform for deploying and serving models on Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API layer for accessing foundation models
- [Model Units](/concepts/model-units.md) — The unit of throughput allocation for provisioned endpoints
- [External Models](/concepts/external-models.md) — Foundation models hosted outside of Databricks
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) — The endpoints that serve deployed models
- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md) — The alternative pricing model for foundation models

## Sources

- provisioned-throughput-foundation-model-apis-databricks-on-aws.md
- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
2. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
