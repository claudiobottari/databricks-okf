---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe76291cbbbf594161ab48abac362516283dd9a7549b0cb5d6d2ca689d51680d
  pageDirectory: concepts
  sources:
    - serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-model-serving-endpoint
    - MSE
    - Serve Multiple Models to Serving Endpoint
    - Serve multiple models to serving endpoint
  citations:
    - file: serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
title: Multi-Model Serving Endpoint
description: A Databricks model serving endpoint that hosts multiple models simultaneously to enable A/B testing, traffic splitting, and side-by-side comparison.
tags:
  - machine-learning
  - model-serving
  - databricks
timestamp: "2026-06-19T23:03:42.339Z"
---

# [Multi-Model Serving](/concepts/multi-model-serving.md) Endpoint

A **Multi-Model Serving Endpoint** is a [Databricks Model Serving](/concepts/databricks-model-serving.md) configuration that enables serving multiple models from a single endpoint, with configurable traffic splitting between them. This approach supports A/B testing, model comparison, and gradual rollout of new model versions alongside existing production models. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

Serving multiple models from a single endpoint allows you to split traffic between different models to compare their performance and facilitate A/B testing. You can also serve different versions of a model at the same time, making experimenting with new versions easier while keeping the current version in production. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Supported Model Types

You can serve any of the following model types on a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). However, you **cannot** serve different model types in a single endpoint — for example, you cannot serve a custom model and an external model in the same endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

- **Custom models** — User-created models deployed via [Databricks Model Serving](/concepts/databricks-model-serving.md)
- **Generative AI models** — Models made available through [Foundation Model APIs](/concepts/foundation-model-apis.md) with [Provisioned Throughput](/concepts/provisioned-throughput.md)
- **External models** — Models hosted on external platforms such as OpenAI or Anthropic

## Creating a Multi-Model Endpoint

When creating a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using the [Model Serving](/concepts/model-serving.md) API or the [Model Serving](/concepts/model-serving.md) UI, you can set the initial traffic split for the models you want to serve. The endpoint configuration requires specifying `served_entities` and a `traffic_config` with `routes` defining the `traffic_percentage` for each entity. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

### Custom Models Example

The following example creates a single endpoint with two custom [Models in Unity Catalog](/concepts/models-in-unity-catalog.md). The served entity `current` hosts version 1 of `model-A` and gets 90% of the endpoint traffic, while `challenger` hosts version 1 of `model-B` and gets 10% of the traffic:

```json
POST /api/2.0/serving-endpoints
{
  "name": "multi-model",
  "config": {
    "served_entities": [
      {
        "name": "current",
        "entity_name": "catalog.schema.model-A",
        "entity_version": "1",
        "workload_size": "Small",
        "scale_to_zero_enabled": true
      },
      {
        "name": "challenger",
        "entity_name": "catalog.schema.model-B",
        "entity_version": "1",
        "workload_size": "Small",
        "scale_to_zero_enabled": true
      }
    ],
    "traffic_config": {
      "routes": [
        { "served_model_name": "current", "traffic_percentage": "90" },
        { "served_model_name": "challenger", "traffic_percentage": "10" }
      ]
    }
  }
}
```

^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

### [Provisioned Throughput](/concepts/provisioned-throughput.md) Example

For [Foundation Model APIs](/concepts/foundation-model-apis.md) with [Provisioned Throughput](/concepts/provisioned-throughput.md), you can serve multiple models with different throughput configurations:

```json
POST /api/2.0/serving-endpoints
{
  "name": "multi-pt-model",
  "config": {
    "served_entities": [
      {
        "name": "meta_llama_v3_1_70b_instruct",
        "entity_name": "system.ai.meta_llama_v3_1_70b_instruct",
        "entity_version": "4",
        "min_provisioned_throughput": 0,
        "max_provisioned_throughput": 2400
      },
      {
        "name": "meta_llama_v3_1_8b_instruct",
        "entity_name": "system.ai.meta_llama_v3_1_8b_instruct",
        "entity_version": "4",
        "min_provisioned_throughput": 0,
        "max_provisioned_throughput": 1240
      }
    ],
    "traffic_config": {
      "routes": [
        { "served_model_name": "meta_llama_v3_1_8b_instruct", "traffic_percentage": "60" },
        { "served_model_name": "meta_llama_v3_1_70b_instruct", "traffic_percentage": "40" }
      ]
    }
  }
}
```

^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

### [External Models](/concepts/external-models.md) Example

You can also configure multiple [External Models](/concepts/external-models.md) in a serving endpoint as long as they have the same task type and each model has a unique `name`. You cannot mix [External Models](/concepts/external-models.md) and non-external models in the same endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

The following example creates an endpoint that routes 50% of traffic to `gpt-4` from OpenAI and 50% to `claude-3-opus-20240229` from Anthropic:

```python
import [[mlflow|MLflow]].deployments

client = [[mlflow|MLflow]].deployments.get_deploy_client("databricks")

client.create_endpoint(
    name="mix-chat-endpoint",
    config={
        "served_entities": [
            {
                "name": "served_model_name_1",
                "external_model": {
                    "name": "gpt-4",
                    "provider": "openai",
                    "task": "llm/v1/chat",
                    "openai_config": {
                        "openai_api_key": "{{secrets/my_openai_secret_scope/openai_api_key}}"
                    }
                }
            },
            {
                "name": "served_model_name_2",
                "external_model": {
                    "name": "claude-3-opus-20240229",
                    "provider": "anthropic",
                    "task": "llm/v1/chat",
                    "anthropic_config": {
                        "anthropic_api_key": "{{secrets/my_anthropic_secret_scope/anthropic_api_key}}"
                    }
                }
            }
        ],
        "traffic_config": {
            "routes": [
                {"served_model_name": "served_model_name_1", "traffic_percentage": 50},
                {"served_model_name": "served_model_name_2", "traffic_percentage": 50}
            ]
        }
    }
)
```

^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Updating the Traffic Split

You can update the traffic split between served models after endpoint creation. This can be done either through the Databricks UI via the **Edit configuration** button on the **Serving** tab, or programmatically using the API: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```json
PUT /api/2.0/serving-endpoints/{name}/config
{
  "served_entities": [
    {
      "name": "current",
      "entity_name": "catalog.schema.model-A",
      "entity_version": "1",
      "workload_size": "Small",
      "scale_to_zero_enabled": true
    },
    {
      "name": "challenger",
      "entity_name": "catalog.schema.model-B",
      "entity_version": "1",
      "workload_size": "Small",
      "scale_to_zero_enabled": true
    }
  ],
  "traffic_config": {
    "routes": [
      { "served_model_name": "current", "traffic_percentage": "50" },
      { "served_model_name": "challenger", "traffic_percentage": "50" }
    ]
  }
}
```

^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Querying Individual Models

In some scenarios, you might want to query individual models behind the endpoint rather than relying on the automatic traffic split. This can be done by targeting the specific served model directly: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```
POST /serving-endpoints/{endpoint-name}/served-models/{served-model-name}/invocations
```

The request format is the same as querying the endpoint. When querying an individual served model, the traffic settings are ignored — if all requests are sent to the `challenger` served model, then all requests are served by that model regardless of the configured traffic split. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The underlying infrastructure for deploying models
- A/B Testing — A common use case for [Multi-Model Serving](/concepts/multi-model-serving.md)
- Custom Models — User-created models deployable on endpoints
- [External Models](/concepts/external-models.md) — Models hosted on third-party platforms
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Pre-built generative AI models
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Reserved capacity for foundation models
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry for custom models
- MLflow Deployments — Python API for managing serving endpoints

## Sources

- serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md](/references/serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws-64227d03.md)
