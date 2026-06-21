---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c12317be4e392b27628a9caeb1b3d3210d354102b69c1b743869eda8d94e1918
  pageDirectory: concepts
  sources:
    - foundation-model-rest-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-vs-provisioned-throughput-endpoints
    - PVPTE
  citations:
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Pay-per-Token vs Provisioned Throughput Endpoints
description: "Two endpoint types in Databricks Foundation Model APIs: preconfigured pay-per-token endpoints and user-created provisioned throughput endpoints supporting A/B testing."
tags:
  - pricing
  - endpoints
  - deployment
timestamp: "2026-06-19T18:55:09.146Z"
---

# Pay-per-Token vs Provisioned Throughput Endpoints

**Pay-per-Token** and **Provisioned Throughput** are two endpoint types offered by the Databricks Foundation Model APIs for serving large language models. Both endpoint types accept the same REST API request format, making it straightforward to switch between them. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Pay-per-Token Endpoints

Pay-per-token endpoints are preconfigured endpoints that exist automatically in each workspace for every supported foundation model. Users can interact with them through standard HTTP POST requests, and billing is based on the number of tokens processed (input plus output tokens). No prior endpoint creation is required — the endpoint is ready to use as soon as the workspace is provisioned. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

These endpoints are ideal for variable workloads, experimentation, and low‑volume inference where predictable capacity is not needed.

## Provisioned Throughput Endpoints

Provisioned throughput endpoints offer reserved compute capacity for a model. They must be explicitly created using either the [Databricks Serving UI](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis) or the [POST /api/2.0/serving-endpoints](https://docs.databricks.com/api/workspace/servingendpoints/create) API. A key differentiator is that provisioned throughput endpoints can serve multiple models simultaneously on the same endpoint for A/B testing, provided that all served models expose the same API format (for example, all are chat models). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

These endpoints are suited for production workloads requiring consistent latency, high throughput, and guaranteed capacity.

## Comparison Summary

| Feature | Pay‑per‑Token | Provisioned Throughput |
|---------|---------------|------------------------|
| **Setup** | Pre‑configured; no creation needed | Must be created via UI or API |
| **Billing** | Per token consumed | Based on provisioned capacity (reserved) |
| **Multi‑model A/B testing** | Not supported | Supported (with compatible API formats) |
| **Use case** | Variable / exploratory workloads | Production / consistent throughput |

Both endpoint types support the same REST API format for [Chat Completions API](/concepts/chat-completions-api.md), [Completions API](/concepts/completions-api.md), [Embeddings API](/concepts/embeddings-api.md), and [Responses API](/concepts/responses-api.md) requests. They also both support streaming responses when applicable (chat and completions). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of the API family.
- [Model Serving](/concepts/model-serving.md) – The infrastructure underlying both endpoint types.
- Supported Foundation Models on Model Serving – List of models available for pay‑per‑token.
- Deploy Provisioned Throughput Foundation Model APIs – Guide to creating provisioned endpoints.
- Structured Outputs on Databricks – Feature available on both endpoint types.

## Sources

- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
