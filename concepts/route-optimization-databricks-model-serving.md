---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8de67bd28de48e08460d82406fec4d5f9ec5fc902b689244c5f454c365c2c30f
  pageDirectory: concepts
  sources:
    - route-optimization-on-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - route-optimization-databricks-model-serving
    - RO(MS
  citations:
    - file: route-optimization-on-serving-endpoints-databricks-on-aws.md
title: Route Optimization (Databricks Model Serving)
description: A feature that improves network path for inference requests on Databricks serving endpoints, enabling higher QPS and lower latency.
tags:
  - model-serving
  - optimization
  - latency
  - databricks
timestamp: "2026-06-19T20:15:24.275Z"
---

# Route Optimization (Databricks Model Serving)

**Route Optimization** is a feature of Databricks Model Serving that improves the network path for inference requests, enabling faster, more direct communication between a client and the deployed model. When enabled on a serving endpoint, route optimization reduces overhead latency and can support substantially higher throughput compared to non‑optimized endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## What is Route Optimization?

Route optimization reconfigures the networking layer so that inference requests take a more direct route from the client to the model. This results in lower and more stable latencies, and the endpoint can handle a higher number of queries per second (QPS) than a conventional serving endpoint. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Requirements

- **Model serving endpoints** must meet the same requirements as non‑route‑optimized model serving endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]
- **Feature serving endpoints** must meet the same requirements as non‑route‑optimized feature serving endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Enable Route Optimization on a Model Serving Endpoint

Route optimization can only be enabled at the time the serving endpoint is created; it cannot be added to an existing endpoint. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

**Via the Serving UI**
1. In the sidebar, click **Serving**.
2. Click **Create serving endpoint**.
3. In the **Route optimization** section, select **Enable route optimization**.
4. After creation, Databricks sends a notification about how to query the new route‑optimized endpoint.

**Via the REST API**  
Set `"route_optimized": true` in the request body when creating an endpoint. The same flag applies when using the Python client or Databricks SDK.

## Enable Route Optimization on a Feature Serving Endpoint

For feature serving endpoints using Feature Functions Serving, specify the full name of the feature specification in the `entity_name` field. The `entity_version` is not required for `FeatureSpecs`. The creation request must include `"route_optimized": true`. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

Example API request:

```json
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

## Querying Route‑Optimized Endpoints

Route‑optimized endpoints are queried differently from non‑optimized endpoints:
- They use a different URL.
- Authentication is performed using OAuth Tokens; personal access tokens (PATs) are **not** supported. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

For detailed instructions, see [Query Route‑Optimized Serving Endpoints](/concepts/query-route-optimized-serving-endpoints.md).

## Limitations

- Route optimization is available only for **custom model serving endpoints** and **feature serving endpoints**. Endpoints that use Foundation Model APIs or [External Models](/concepts/external-models.md) are not supported. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]
- Authentication is limited to Databricks in‑house OAuth tokens. Personal access tokens are not allowed. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Additional Resources

- Model Serving Documentation
- Optimize Model Serving Endpoints for Production
- Create and Manage Serving Endpoints

## Sources

- route-optimization-on-serving-endpoints-databricks-on-aws.md

# Citations

1. [route-optimization-on-serving-endpoints-databricks-on-aws.md](/references/route-optimization-on-serving-endpoints-databricks-on-aws-9093903f.md)
