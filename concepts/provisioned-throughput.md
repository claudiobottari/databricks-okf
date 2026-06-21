---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7d6afb7f301e996797e7ff91eae69db88c9c2dba38c3a4f3029448e30b533ad
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
    - model-serving-concepts-databricks-on-aws.md
    - provisioned-throughput-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput
    - Model Units in Provisioned Throughput
    - REST API for provisioned throughput
    - throughput
  citations:
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Provisioned Throughput
description: A deployment option for production workloads using base or fine-tuned models with performance guarantees, available through Foundation Model APIs.
tags:
  - model-serving
  - provisioned-throughput
  - production
timestamp: "2026-06-19T18:02:07.151Z"
---

# Provisioned Throughput

**Provisioned Throughput** is a model serving capability on the Databricks platform that enables users to allocate dedicated, guaranteed inference capacity for foundation models. It is designed for production workloads that require consistent performance and reliable throughput. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Overview

Provisioned throughput endpoints provide a guaranteed amount of tokens per second throughput. You can configure both a minimum and maximum provisioned throughput for an endpoint. Unlike [pay-per-token](/concepts/pay-per-token-pricing.md) endpoints, which use shared infrastructure, provisioned throughput endpoints allocate dedicated resources to the model, ensuring that inference latency and throughput are not affected by other workloads. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

Databricks recommends provisioned throughput for production use cases requiring performance guarantees, and it provides optimized inference for foundation models with performance guarantees. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md, create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Key Concepts

### Model Units

Provisioned throughput endpoints scale in increments of [Model Units](/concepts/model-units.md). Each model architecture has a specific `throughput_chunk_size` that determines the base unit of scalability. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Configuration

When creating a provisioned throughput endpoint, you specify:

- **Entity**: The model from [Unity Catalog](/concepts/unity-catalog.md) that you want to serve.
- **Minimum provisioned throughput**: The lowest throughput the endpoint can scale down to.
- **Maximum provisioned throughput**: The highest throughput the endpoint can scale up to.

Provisioned throughput endpoints automatically scale between these configured values based on demand. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Creating a Provisioned Throughput Endpoint

### Via the UI

1. Navigate to the **Serving UI** in your workspace.
2. Select **Create serving endpoint**.
3. In the **Entity** field, select your model from Unity Catalog. For eligible models, the UI shows the **Provisioned Throughput** screen.
4. In the **Up to** dropdown you can configure the maximum tokens per second throughput for your endpoint.
   - Optionally, select **Modify** to view the minimum tokens per second your endpoint can scale down to. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Via the REST API

To deploy a model using provisioned throughput, you must specify `min_provisioned_throughput` and `max_provisioned_throughput` fields in the request body. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

Example request structure:

```json
{
  "name": "prov-throughput-endpoint",
  "config": {
    "served_entities": [
      {
        "entity_name": "ml.llm-catalog.foundation-model",
        "entity_version": 3,
        "min_provisioned_throughput": 2000,
        "max_provisioned_throughput": 3000
      }
    ]
  }
}
```

You can also use the model optimization information API to get the throughput chunk size for your model:

```
GET api/2.0/serving-endpoints/get-model-optimization-info/{registered_model_name}/{version}
```

The response includes `throughput_chunk_size` and `model_type` (e.g., `llama`, `gte`). ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

### Via the MLflow Deployments SDK

You can create provisioned throughput endpoints using the [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md, provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Supported Models

Provisioned throughput is available for foundation model architectures that have been optimized for inference. Supported model types include `llama` and `gte`. Each model type has a specific `throughput_chunk_size` that determines how much throughput can be provisioned in a single step. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

For a complete list of supported models, see [Supported foundation models on Model Serving](/concepts/foundation-model-serving-modes.md).

## Auto-scaling Behavior

Provisioned throughput endpoints automatically scale between the minimum and maximum values you configure. This allows you to handle variable traffic patterns while maintaining performance guarantees. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Limitations

- Model deployment might fail due to GPU capacity issues, which results in a timeout during endpoint creation or update. Contact your Databricks account team for resolution. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]
- Only specific model architectures are supported for provisioned throughput. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform that hosts provisioned throughput endpoints.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API layer for querying foundation models.
- [Pay-per-token](/concepts/pay-per-token-serving-mode.md) — The alternative pricing model for experimentation.
- [Model Units](/concepts/model-units.md) — The unit of compute for provisioned throughput.
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog where foundation models are stored.
- [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md) — SDK for programmatic endpoint creation.

## Sources

- provisioned-throughput-foundation-model-apis-databricks-on-aws.md
- model-serving-concepts-databricks-on-aws.md
- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
2. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
