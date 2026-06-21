---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c38fe937af48ba75565791349f18a1b6a0c37e74f0ef56cc0bd1a702b8d3fa21
  pageDirectory: concepts
  sources:
    - model-serving-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - served-entities-configuration
    - SEC
  citations:
    - file: model-serving-concepts-databricks-on-aws.md
title: Served Entities Configuration
description: The served_entities array in a serving endpoint config where each entity specifies a name, entity_name, entity_version, and throughput limits.
tags:
  - databricks
  - model-serving
  - configuration
timestamp: "2026-06-19T19:43:40.404Z"
---

# Served Entities Configuration

**Served Entities Configuration** defines the set of models (entities) that are served on a Databricks Model Serving endpoint, along with their provisioning settings and traffic routing rules. The configuration is specified as a JSON payload when creating or updating a serving endpoint via the [Serving Endpoints API](https://docs.databricks.com/api/workspace/servingendpoints). ^[model-serving-concepts-databricks-on-aws.md]

## Structure

The `served_entities` array within the endpoint config lists each model to be served. Each entry contains the following fields: ^[model-serving-concepts-databricks-on-aws.md]

| Field | Description |
|-------|-------------|
| `name` | A user-defined alias for the served entity within the endpoint (e.g., `"meta_llama_v3_1_70b_instruct"`). |
| `entity_name` | The fully qualified name of the registered model in Unity Catalog (e.g., `"system.ai.meta_llama_v3_1_70b_instruct"`). |
| `entity_version` | The version of the registered model to serve (e.g., `"4"`). |
| `min_provisioned_throughput` | Minimum provisioned throughput in requests per second (0 means no minimum). |
| `max_provisioned_throughput` | Maximum provisioned throughput in requests per second (0 means no maximum). |

## Traffic Routing

A separate `traffic_config` block defines how incoming requests are distributed among the served entities using a list of `routes`. Each route maps a `served_model_name` (matching the `name` field in the served entity) to a `traffic_percentage`. The percentages across all routes should sum to 100. ^[model-serving-concepts-databricks-on-aws.md]

## Example

The following JSON configures an endpoint that serves two Llama models, with 60% of traffic going to the 8B model and 40% to the 70B model:

```json
{
  "name": "multi-pt-model",
  "config": {
    "served_entities": [
      {
        "name": "meta_llama_v3_1_8b_instruct",
        "entity_name": "system.ai.meta_llama_v3_1_8b_instruct",
        "entity_version": "4",
        "min_provisioned_throughput": 0,
        "max_provisioned_throughput": 1240
      },
      {
        "name": "meta_llama_v3_1_70b_instruct",
        "entity_name": "system.ai.meta_llama_v3_1_70b_instruct",
        "entity_version": "4",
        "min_provisioned_throughput": 0,
        "max_provisioned_throughput": 2400
      }
    ],
    "traffic_config": {
      "routes": [
        { "served_model_name": "meta_llama_v3_1_8b_instruct", "traffic_percentage": 60 },
        { "served_model_name": "meta_llama_v3_1_70b_instruct", "traffic_percentage": 40 }
      ]
    }
  }
}
```

^[model-serving-concepts-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Overview of Databricks Model Serving endpoints.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – How min/max throughput settings control concurrency and cost.
- Traffic Routing – Advanced traffic splitting between model versions.
- [Unity Catalog Models](/concepts/unity-catalog-for-ml-models.md) – How registered models in Unity Catalog are referenced by `entity_name`.

## Sources

- model-serving-concepts-databricks-on-aws.md

# Citations

1. [model-serving-concepts-databricks-on-aws.md](/references/model-serving-concepts-databricks-on-aws-b4c5ea15.md)
