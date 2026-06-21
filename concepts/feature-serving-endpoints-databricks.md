---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b3be5ccb1cf134ce3859b03d5dc3b4041d8a0495d6d4c9e142a4593adb9a701
  pageDirectory: concepts
  sources:
    - route-optimization-on-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-serving-endpoints-databricks
    - FSE(
    - Feature serving on Databricks
  citations:
    - file: route-optimization-on-serving-endpoints-databricks-on-aws.md
title: Feature Serving Endpoints (Databricks)
description: Feature and function serving endpoints on Databricks that support route optimization using FeatureSpecs.
tags:
  - feature-serving
  - endpoints
  - databricks
  - feature-store
timestamp: "2026-06-19T20:15:36.853Z"
---

# Feature Serving Endpoints (Databricks)

**Feature Serving Endpoints** on Databricks provide a managed serving infrastructure for deploying and serving features from the [Feature Store](/concepts/feature-store.md) and Function Serving. These endpoints can be optimized for lower latency and higher throughput using route optimization. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Requirements

Route‑optimized feature serving endpoints have the same requirements as non‑route‑optimized feature serving endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Route Optimization

Route optimization improves the network path for inference requests, resulting in faster, more direct communication between the client and the endpoint. This unlocks higher queries per second (QPS) and provides more stable, lower latencies. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

Route optimization can be enabled **only during endpoint creation**; it cannot be added to an existing endpoint. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

### Enabling Route Optimization via REST API

To enable route optimization on a feature serving endpoint, specify the full name of the feature specification in the `entity_name` field (the `entity_version` is not needed for `FeatureSpecs`) and set `"route_optimized": true`:

```bash
POST /api/2.0/serving-endpoints
{
  "name": "my-endpoint",
  "config": {
    "served_entities": [
      {
        "entity_name": "catalog_name.schema_name.feature_spec_name",
        "workload_type": "CPU",
        "workload_size": "Small",
        "scale_to_zero_enabled": true
      }
    ]
  },
  "route_optimized": true
}
```

^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

### Querying a Route‑Optimized Feature Serving Endpoint

Route‑optimized endpoints use a different URL and require authentication with OAuth tokens. Databricks in‑house OAuth tokens are the only supported authentication; personal access tokens are not supported. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Limitations

- Route optimization is available only for **custom model serving endpoints** and **feature serving endpoints**. Endpoints that use [Foundation Model APIs](/concepts/foundation-model-apis.md) or [External Models](/concepts/external-models.md) are not supported. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]
- Only Databricks in‑house OAuth tokens can be used for authentication; personal access tokens are not supported. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Feature Store](/concepts/feature-store.md)
- Route Optimization
- Serving Endpoint Authentication

## Sources

- route-optimization-on-serving-endpoints-databricks-on-aws.md

# Citations

1. [route-optimization-on-serving-endpoints-databricks-on-aws.md](/references/route-optimization-on-serving-endpoints-databricks-on-aws-9093903f.md)
