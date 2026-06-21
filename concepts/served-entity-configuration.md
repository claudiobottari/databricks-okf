---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bce3ab3f567bbd6c73af0063d9779f35e69477228444c0ffb828a606c9ca2310
  pageDirectory: concepts
  sources:
    - serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - served-entity-configuration
    - SEC
  citations:
    - file: serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
title: Served Entity Configuration
description: Named configuration objects that define which model versions, workload sizes, and scaling settings are assigned to each model on a multi-model endpoint.
tags:
  - model-serving
  - configuration
  - databricks
timestamp: "2026-06-19T23:03:13.688Z"
---

# Served Entity Configuration

**Served Entity Configuration** refers to the specification of a model or foundation model API version deployed on a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) and the allocation of traffic among multiple served entities on the same endpoint. Each served entity represents a distinct model version that can receive inference requests.

## Overview

A [Model Serving Endpoint](/concepts/model-serving-endpoint.md) can host multiple served entities simultaneously, enabling traffic splitting between different models or model versions for A/B Testing, canary deployments, and performance comparison. The traffic split is configured through a `traffic_config` object that assigns a percentage of endpoint traffic to each served entity. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

Each served entity has a unique `name` within the endpoint configuration. This name is used in the traffic routing configuration and in individual model invocation requests. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Supported Model Types

You can serve any of the following model types on a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), but you cannot mix different types in a single endpoint: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

- [Custom models|Custom models](/concepts/custom-models-on-model-serving.md) — User-defined or custom-trained models
- Generative AI models — [Foundation Model APIs](/concepts/foundation-model-apis.md) with [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [External models](/concepts/external-models.md) — Hosted by third-party providers

## Served Entity Properties

When defining a served entity, you specify: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

- `name` — A unique identifier for this served entity within the endpoint
- `entity_name` — The fully qualified model name in [Unity Catalog](/concepts/unity-catalog.md) (e.g., `catalog.schema.model-A`)
- `entity_version` — The version of the model to serve
- `workload_size` — For custom models (e.g., `Small`, `Medium`, `Large`)
- `scale_to_zero_enabled` — Whether the workload scales down when idle
- `min_provisioned_throughput` / `max_provisioned_throughput` — For [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md)

## Traffic Configuration

The `traffic_config` defines how incoming requests are distributed among served entities. It contains a `routes` array where each route links a served entity name to a traffic percentage. The sum of all `traffic_percentage` values must equal 100. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```json
"traffic_config": {
  "routes": [
    {
      "served_model_name": "current",
      "traffic_percentage": "90"
    },
    {
      "served_model_name": "challenger",
      "traffic_percentage": "10"
    }
  ]
}
```

## Querying Individual Served Entities

Beyond the default traffic-split routing, you can bypass the traffic configuration and query a specific served entity directly. This is useful for targeted testing or debugging: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

```
POST /serving-endpoints/{endpoint-name}/served-models/{served-model-name}/invocations
```

The request format is the same as querying the endpoint. When querying an individual served model, the traffic settings are ignored and all requests go to that specific served entity. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Updating Configuration

You can update the served entity configuration after endpoint creation using the [Model Serving](/concepts/model-serving.md) API or the Databricks UI. This allows you to adjust traffic splits or change which models are served without recreating the endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## External Model Constraints

For [External Models](/concepts/external-models.md), additional constraints apply: ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

- All [External Models](/concepts/external-models.md) in a single endpoint must have the same task type (e.g., `llm/v1/chat`)
- Each external model must have a unique `name`
- You cannot mix [External Models](/concepts/external-models.md) with non-external models in the same endpoint
- Provider-specific configuration (such as `openai_config` or `anthropic_config`) must use Databricks Secrets for API keys

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- A/B Testing
- Canary Deployment
- [Traffic Splitting](/concepts/traffic-splitting-between-models.md)
- [Endpoint ACLs](/concepts/serving-endpoint-acls.md)
- [External Models](/concepts/external-models.md)

## Sources

- serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md](/references/serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws-64227d03.md)
