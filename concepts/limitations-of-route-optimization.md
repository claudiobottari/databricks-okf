---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dff4c9bae6df4326ca6b12daa2f5d987972931921e1fb5dc1c8bd77a652b28b5
  pageDirectory: concepts
  sources:
    - route-optimization-on-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-route-optimization
    - LORO
    - Endpoint Route Optimization
  citations:
    - file: route-optimization-on-serving-endpoints-databricks-on-aws.md
title: Limitations of Route Optimization
description: Route optimization is only available for custom model and feature serving endpoints, not Foundation Model APIs or external models.
tags:
  - model-serving
  - limitations
  - compatibility
  - databricks
timestamp: "2026-06-19T20:15:44.030Z"
---

# Limitations of Route Optimization

Route optimization on Databricks Model Serving improves network path for inference requests, enabling higher queries per second and lower latency. However, the feature has several important limitations that affect which endpoints can use it, how they are authenticated, and when the configuration can be applied.

## Supported Endpoint Types

Route optimization is available only for **custom model serving endpoints** and **feature serving endpoints**. Serving endpoints that use Foundation Model APIs or external models are not supported. This means that if you are serving a model via the built-in foundation model APIs (for example, Llama 2, DBRX, or other Databricks-provided models) or an external model service (such as OpenAI or Anthropic through a Databricks gateway), you cannot enable route optimization on that endpoint. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Authentication Restrictions

Only Databricks in-house OAuth tokens are supported for authentication to route-optimized endpoints. Personal access tokens (PATs) are not supported. This means that any client or application that relies on PATs to make inference requests must migrate to OAuth if the endpoint is route-optimized. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Enablement Timing

Route optimization can only be enabled **during endpoint creation**. You cannot update an existing non-route-optimized endpoint to become route-optimized. If you need route optimization, you must create a new endpoint with the `route_optimized` flag set to `true`. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Query Differences

Route-optimized endpoints must be queried differently from non-route-optimized endpoints. They use a different URL and require OAuth tokens for authentication. This imposes a migration burden for existing clients that are already configured to query a non-optimized endpoint. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Summary Table

| Limitation | Details |
|------------|---------|
| **Endpoint types** | Only custom model serving and feature serving endpoints; Foundation Model APIs and external models are excluded. |
| **Authentication** | Only Databricks OAuth tokens; personal access tokens are not supported. |
| **Enablement time** | Can only be set at endpoint creation; not modifiable after creation. |
| **Query protocol** | Different URL and authentication scheme compared to non-optimized endpoints. |

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- Feature Serving
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [External Models](/concepts/external-models.md)
- OAuth tokens
- [Create serving endpoint](/concepts/feature-serving-endpoint.md)

## Sources

- route-optimization-on-serving-endpoints-databricks-on-aws.md

# Citations

1. [route-optimization-on-serving-endpoints-databricks-on-aws.md](/references/route-optimization-on-serving-endpoints-databricks-on-aws-9093903f.md)
