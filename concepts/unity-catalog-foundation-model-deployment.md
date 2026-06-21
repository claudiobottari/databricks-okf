---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef80c8a0bcfa1f63cb046f12d12bd993edb4540f090f51f73cce3f1120dcfe4c
  pageDirectory: concepts
  sources:
    - provisioned-throughput-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-foundation-model-deployment
    - UCFMD
  citations:
    - file: filename.md
    - file: source-a.md
    - file: source-b.md
    - file: filename.md:START-END
    - file: filename.md#LSTART-LEND
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
title: Unity Catalog Foundation Model Deployment
description: The recommended workflow for deploying foundation models from the system.ai catalog in Unity Catalog using Databricks Catalog Explorer.
tags:
  - databricks
  - unity-catalog
  - deployment
timestamp: "2026-06-19T20:00:35.260Z"
---

You are a wiki author. Write a clear, well-structured markdown page about "Unity Catalog Foundation Model Deployment".
Draw facts only from the provided source material.
Include a ## Sources section at the end listing the source document.
Suggest wikilinks to related concepts where appropriate.
Write in a neutral, informative tone. Be concise but thorough.

Source attribution: at the end of each prose paragraph, append a citation
marker showing which source file(s) the paragraph drew from.
Format: ^[filename.md] for single-source, ^[source-a.md, source-b.md] for multi-source.
When a single sentence makes a specific factual claim and you can identify the
exact line range it came from, you may use the claim-level form
^[filename.md:START-END] or ^[filename.md#LSTART-LEND] at the end of that
sentence — START and END are 1-indexed line numbers in the source file.
Paragraph-level citations remain the default; only switch to claim-level form
when it materially improves verifiability and the line range is unambiguous.
Place citations only at the end of prose paragraphs or sentences — not on
headings, list items, or code blocks.
Source filenames are visible as `--- SOURCE: filename.md ---` headers in the content below.

If a paragraph is your inference rather than a direct extraction, leave it
uncited — downstream lint rules will count uncited paragraphs as 'inferred'
to compute the page's provenance metadata.

---

## Unity Catalog Foundation Model Deployment

**Unity Catalog Foundation Model Deployment** refers to the process of deploying pre-installed foundation models from Unity Catalog to provisioned throughput serving endpoints on Databricks. Databricks recommends this approach for production workloads because it provides optimized inference with performance guarantees. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Overview

When deploying foundation models, Databricks recommends using the models that are pre-installed in Unity Catalog. These models are located under the catalog `system` in the schema `ai` (`system.ai`). ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

To deploy a Meta Llama model from `system.ai`, you must choose the applicable **Instruct** version. Base versions of the Meta Llama models are not supported for deployment from Unity Catalog. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Deployment Procedure

### Finding the Model

To locate a foundation model for deployment:

1. Navigate to `system.ai` in Catalog Explorer.
2. Click on the name of the model to deploy.
3. On the model page, click the **Serve this model** button.

This opens the **Create serving endpoint** page. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Creating a Provisioned Throughput Endpoint via UI

After the logged model is in Unity Catalog, create a serving endpoint with the following steps:

1. Navigate to the **Serving UI** in your workspace.
2. Select **Create serving endpoint**.
3. In the **Entity** field, select your model from Unity Catalog. For eligible models, the UI shows the **Provisioned Throughput** screen.
4. In the **Up to** dropdown, configure the maximum tokens per second throughput for your endpoint. Provisioned throughput endpoints automatically scale, so you can select **Modify** to view the minimum tokens per second your endpoint can scale down to. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Creating a Provisioned Throughput Endpoint via REST API

To deploy a model in provisioned throughput mode using the REST API, specify `min_provisioned_throughput` and `max_provisioned_throughput` fields in your request. You can also create an endpoint using the [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md). ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

The following Python example demonstrates creating a provisioned throughput endpoint via the REST API:

```python
import requests
import json

endpoint_name = "prov-throughput-endpoint"
model_name = "ml.llm-catalog.foundation-model"
model_version = 3

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
min_provisioned_throughput = 2 * chunk_size
max_provisioned_throughput = 3 * chunk_size

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

### Getting Provisioned Throughput Increments

Provisioned throughput is available in increments of tokens per second, with specific increments varying by model. To identify the suitable range for your needs, use the model optimization information API:

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

```json
{
  "optimizable": true,
  "model_type": "gte",
  "throughput_chunk_size": 980
}
```

^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Limitations

Model deployment might fail due to GPU capacity issues, which results in a timeout during endpoint creation or update. If this occurs, reach out to your Databricks account team for assistance. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) — The serving infrastructure for deploying models with dedicated performance guarantees.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The endpoints that serve deployed models to applications.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API interface for interacting with foundation models.
- [Model Units](/concepts/model-units.md) — The unit of allocation for provisioned throughput capacity.
- [Chat Completions API](/concepts/chat-completions-api.md) — The API for chat completion tasks, supporting parameters like `logprobs`.
- [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md) — Python SDK for creating and managing serving endpoints.

## Sources

- provisioned-throughput-foundation-model-apis-databricks-on-aws.md

# Citations

1. filename.md
2. source-a.md
3. source-b.md
4. filename.md:START-END
5. filename.md#LSTART-LEND
6. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
