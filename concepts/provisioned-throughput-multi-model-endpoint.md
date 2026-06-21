---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a963df984023bd9cc365205b21f17d7e3df7dabfa5822c649f3d6792e676176c
  pageDirectory: concepts
  sources:
    - serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-multi-model-endpoint
    - PTME
  citations:
    - file: serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
title: Provisioned Throughput Multi-Model Endpoint
description: A Foundation Model API endpoint configured with provisioned throughput that serves multiple generative AI models with a shared traffic split.
tags:
  - model-serving
  - foundation-models
  - provisioned-throughput
  - databricks
timestamp: "2026-06-19T23:03:42.319Z"
---

# [Provisioned Throughput](/concepts/provisioned-throughput.md) Multi-Model Endpoint

A **Provisioned Throughput Multi-Model Endpoint** is a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint configured to serve multiple [Foundation Model APIs](/concepts/foundation-model-apis.md) models with [Provisioned Throughput](/concepts/provisioned-throughput.md) capacity, distributing traffic between them according to a configured traffic split. This setup enables A/B testing, progressive rollouts, and side-by-side comparison of different foundation models under a single endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

When you create a [Provisioned Throughput](/concepts/provisioned-throughput.md) Multi-Model Endpoint, you configure the endpoint with multiple served entities, each specifying a foundation model along with its minimum and maximum [Provisioned Throughput](/concepts/provisioned-throughput.md) values. The endpoint also includes a traffic configuration that defines the percentage of inference requests each model receives. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

Only models that use the [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md) offering can be combined in a single endpoint. You cannot serve different model types—such as custom models, [External Models](/concepts/external-models.md), and foundation models—in the same endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Configuration

### API Example

The following REST API example creates a [Provisioned Throughput](/concepts/provisioned-throughput.md) Multi-Model Endpoint named `multi-pt-model` that serves two foundation models with a 60/40 traffic split:

```bash
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

^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

In this configuration:
- The endpoint hosts version 4 of `meta_llama_v3_1_70b_instruct` with a maximum [Provisioned Throughput](/concepts/provisioned-throughput.md) of 2400 and version 4 of `meta_llama_v3_1_8b_instruct` with a maximum [Provisioned Throughput](/concepts/provisioned-throughput.md) of 1240.
- `meta_llama_v3_1_8b_instruct` receives 60% of the traffic, while `meta_llama_v3_1_70b_instruct` receives 40%.

## Updating the Traffic Split

You can update the traffic split between served models on an existing [Provisioned Throughput](/concepts/provisioned-throughput.md) Multi-Model Endpoint using the REST API or the Databricks UI. The endpoint configuration can be modified to change the `traffic_percentage` values in the `traffic_config` routes. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Querying Individual Models

In some scenarios, you may want to bypass the traffic configuration and send requests directly to a specific served model. You can do this by using the following endpoint path:

```bash
POST /serving-endpoints/{endpoint-name}/served-models/{served-model-name}/invocations
```

When querying an individual served model in this way, the traffic settings are ignored. For example, if all requests are sent to `/serving-endpoints/multi-pt-model/served-models/meta_llama_v3_1_70b_instruct/invocations`, all requests are served by `meta_llama_v3_1_70b_instruct` regardless of the configured traffic percentage. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Use Cases

- **A/B testing** — Compare performance of two different foundation models by sending a controlled percentage of traffic to each.
- **Gradual rollouts** — Slowly increase traffic to a new model version while monitoring performance.
- **Production experimentation** — Keep an existing model in production while evaluating a challenger model with lower traffic.
- **Cost-performance optimization** — Route the majority of traffic to a cost-efficient model while reserving a smaller portion for a higher-capability model.

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The general concept of serving models on Databricks.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Dedicated throughput capacity for foundation model inference.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Managed API offerings for popular foundation models.
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) — Serving custom [MLflow](/concepts/mlflow.md) models on endpoints (not combinable with foundation models in the same endpoint).
- External Model Serving — Serving models from external providers (not combinable with foundation models in the same endpoint).
- A/B Testing with Model Serving — Comparing model performance using traffic splitting.
- [Serving Endpoint ACLs](/concepts/serving-endpoint-acls.md) — Access control for [Model Serving](/concepts/model-serving.md) endpoints.

## Sources

- serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md](/references/serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws-64227d03.md)
