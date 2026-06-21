---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f3a12f07fc84af15eda24707b095368d42f210aaa55664c7d91779cca9eb644
  pageDirectory: concepts
  sources:
    - serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traffic-splitting-between-models
    - TSBM
    - Traffic Split
    - Traffic Splitting
    - Traffic splitting
  citations:
    - file: serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
title: Traffic Splitting Between Models
description: Configuring percentage-based distribution of inference requests across different models hosted on the same serving endpoint.
tags:
  - model-serving
  - traffic-routing
  - databricks
timestamp: "2026-06-19T23:03:17.562Z"
---

# Traffic Splitting Between Models

**Traffic Splitting Between Models** is a feature of [Databricks Model Serving](/concepts/databricks-model-serving.md) that allows you to distribute incoming inference requests across multiple served models or model versions within a single serving endpoint. This enables A/B testing, gradual rollouts, and performance comparisons between different models or versions.

## Overview

Traffic splitting is configured via the `traffic_config` field in the endpoint configuration. This field contains a list of `routes`, each mapping a `served_model_name` to a `traffic_percentage`. The percentages across all routes must sum to 100. When the endpoint receives a request, the serving infrastructure routes it to one of the served models according to these percentages. Each request is handled entirely by the selected model; there is no blending of responses. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

Serving multiple models from a single endpoint allows you to compare model performance and facilitate A/B testing. You can also serve different versions of a model simultaneously, making it easier to experiment with new versions while keeping the current production version active. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Supported Model Types

You can split traffic between models of the same type on a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). The supported types are:

- Custom models (registered in [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Model Registry](/concepts/workspace-model-registry.md))
- Generative AI models made available through [Foundation Model APIs](/concepts/foundation-model-apis.md) with [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [External Models](/concepts/external-models.md) (e.g., OpenAI, Anthropic, etc.)

**Important:** You cannot serve different model types in a single endpoint. For example, you cannot serve a custom model and an external model in the same endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## API Examples

### Serve multiple custom models

The following REST API example creates an endpoint named `multi-model` that hosts two [Unity Catalog](/concepts/unity-catalog.md) models. The entity named `current` hosts version 1 of `model-A` and gets 90% of the traffic, while `challenger` hosts version 1 of `model-B` and gets the remaining 10%. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```json
POST /api/2.0/serving-endpoints
{
   "name":"multi-model",
   "config":
   {
      "served_entities":
      [
         {
            "name":"current",
            "entity_name":"catalog.schema.model-A",
            "entity_version":"1",
            "workload_size":"Small",
            "scale_to_zero_enabled":true
         },
         {
            "name":"challenger",
            "entity_name":"catalog.schema.model-B",
            "entity_version":"1",
            "workload_size":"Small",
            "scale_to_zero_enabled":true
         }
      ],
      "traffic_config":
      {
         "routes":
         [
            {
               "served_model_name":"current",
               "traffic_percentage":"90"
            },
            {
               "served_model_name":"challenger",
               "traffic_percentage":"10"
            }
         ]
      }
   }
}
```

### Serve multiple models on a [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md)

This example creates a [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md) with two foundation models: 60% of traffic to `meta_llama_v3_1_8b_instruct` and 40% to `meta_llama_v3_1_70b_instruct`. Each served entity specifies its own `min_provisioned_throughput` and `max_provisioned_throughput`. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```json
POST /api/2.0/serving-endpoints
{
   "name":"multi-pt-model",
   "config":
   {
      "served_entities":
      [
         {
            "name":"meta_llama_v3_1_70b_instruct",
            "entity_name":"system.ai.meta_llama_v3_1_70b_instruct",
            "entity_version":"4",
            "min_provisioned_throughput":0,
            "max_provisioned_throughput":2400
         },
         {
            "name":"meta_llama_v3_1_8b_instruct",
            "entity_name":"system.ai.meta_llama_v3_1_8b_instruct",
            "entity_version":"4",
            "min_provisioned_throughput":0,
            "max_provisioned_throughput":1240
         }
      ],
      "traffic_config":
      {
         "routes":
         [
            {
               "served_model_name":"meta_llama_v3_1_8b_instruct",
               "traffic_percentage":"60"
            },
            {
               "served_model_name":"meta_llama_v3_1_70b_instruct",
               "traffic_percentage":"40"
            }
         ]
      }
   }
}
```

### Serve multiple [External Models](/concepts/external-models.md)

You can also configure multiple [External Models](/concepts/external-models.md) of the same task type (e.g., both `llm/v1/chat`) in a single endpoint. Each external model must have a unique `name`. The following example uses the [MLflow](/concepts/mlflow.md) Deployments API to route 50% of traffic to OpenAI's GPT-4 and 50% to Anthropic's Claude 3 Opus. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

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
        },
    }
)
```

## Updating the Traffic Split

You can update the traffic split after endpoint creation using either the REST API or the Databricks UI. The following PUT request changes the split to 50/50 between `current` and `challenger`. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```json
PUT /api/2.0/serving-endpoints/{name}/config
{
   "served_entities":
   [
      {
         "name":"current",
         "entity_name":"catalog.schema.model-A",
         "entity_version":"1",
         "workload_size":"Small",
         "scale_to_zero_enabled":true
      },
      {
         "name":"challenger",
         "entity_name":"catalog.schema.model-B",
         "entity_version":"1",
         "workload_size":"Small",
         "scale_to_zero_enabled":true
      }
   ],
   "traffic_config":
   {
      "routes":
      [
         {
            "served_model_name":"current",
            "traffic_percentage":"50"
         },
         {
            "served_model_name":"challenger",
            "traffic_percentage":"50"
         }
      ]
   }
}
```

You can also make this update from the **Serving** tab in the Databricks UI using the **Edit configuration** button. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Querying Individual Models

In some scenarios, you may want to bypass the traffic split and send requests directly to a specific served model. This is supported by using the following endpoint path: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```
POST /serving-endpoints/{endpoint-name}/served-models/{served-model-name}/invocations
```

The request format is the same as querying the endpoint. Traffic settings are ignored when querying a specific served model. For example, all requests sent to `/serving-endpoints/multi-model/served-models/challenger/invocations` are served by the `challenger` model regardless of the configured traffic percentages. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Use Cases

- **A/B testing** – Compare a new model version (challenger) against the current production model by sending a small percentage of traffic to the challenger.
- **Gradual rollouts** – Incrementally increase traffic to a new model version while monitoring performance and errors, then shift 100% once validated.
- **Cost/performance trade-offs** – Route simple queries to a smaller, cheaper model and complex queries to a larger, more capable model (note: routing logic is based on static percentages; intelligent routing per query is not handled by this feature).
- **Multi-model endpoints** – Serve different models from a single endpoint URL, centralizing management and client configuration.

## Limitations

- All served models on an endpoint must be of the same type (custom, foundation, or external). Mixing types is not supported. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]
- Traffic splitting is based on random distribution per the configured percentages; there is no content-based or request-header-based routing.
- The endpoint must meet general [Model Serving Endpoint](/concepts/model-serving-endpoint.md) creation requirements.

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The API resource that hosts model deployments and inference routing.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Reserved capacity for [Foundation Model APIs](/concepts/foundation-model-apis.md), configured per served entity.
- [External Models](/concepts/external-models.md) – Third-party models (e.g., OpenAI, Anthropic) served through Databricks.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Databricks-managed generative AI models available with [Provisioned Throughput](/concepts/provisioned-throughput.md).
- [Unity Catalog](/concepts/unity-catalog.md) – Catalog for managing custom model registrations and versions.

## Sources

- serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md](/references/serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws-64227d03.md)
