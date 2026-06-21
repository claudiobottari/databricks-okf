---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afc033851f0c98296402059c99b08211a53ee6c3b601539a9709a15ae1709d30
  pageDirectory: concepts
  sources:
    - serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-type-restriction-on-endpoints
    - MTROE
  citations:
    - file: serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md
title: Model Type Restriction on Endpoints
description: The constraint that a single Databricks model serving endpoint cannot mix different model types (custom, foundation, external) — all served models must be of the same type.
tags:
  - model-serving
  - restrictions
  - databricks
timestamp: "2026-06-19T23:03:18.194Z"
---

# Model Type Restriction on Endpoints

The **Model Type Restriction on Endpoints** is a constraint on [Databricks Model Serving](/concepts/databricks-model-serving.md) that prevents different model types from being served together within a single serving endpoint. When configuring an endpoint to serve multiple models, all models must be of the same type.

## Restriction Details

A single [Model Serving Endpoint](/concepts/model-serving-endpoint.md) can serve any of the following model types, but cannot combine multiple types in the same endpoint:

- **Custom models** — Models registered in [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Model Registry](/concepts/workspace-model-registry.md)
- **Generative AI models** — Models made available through [Foundation Model APIs](/concepts/foundation-model-apis.md) with [Provisioned Throughput](/concepts/provisioned-throughput.md)
- **External models** — Models hosted on third-party platforms (e.g., OpenAI, Anthropic) and accessed through the external model integration

^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

For example, you cannot serve a custom model and an external model in the same endpoint. All models served on a single endpoint must share the same category. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Additional Constraint for [External Models](/concepts/external-models.md)

When serving multiple [External Models](/concepts/external-models.md) in a single endpoint, they must all have the same task type. Each model in the endpoint must also have a unique `name`. Additionally, you cannot have both [External Models](/concepts/external-models.md) and non-external models in the same serving endpoint. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Use Case

This restriction is relevant when configuring A/B testing or [Traffic Splitting Between Models](/concepts/traffic-splitting-between-models.md) on a single endpoint. Users must ensure that all models they want to compare or route traffic between belong to the same model type before configuring the endpoint's traffic split. ^[serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serving infrastructure that hosts models for inference
- [Traffic Splitting](/concepts/traffic-splitting-between-models.md) — Configuring how requests are distributed between multiple served models
- Custom Models — User-created models deployed on Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Managed generative AI models available on Databricks
- [External Models](/concepts/external-models.md) — Models hosted on third-party inference providers

## Sources

- serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws.md](/references/serve-multiple-models-to-a-model-serving-endpoint-databricks-on-aws-64227d03.md)
