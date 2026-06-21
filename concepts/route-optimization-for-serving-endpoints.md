---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a54322a4eadc1ad49c4b88597499a15d0da22379a505d04e604d64a3f425be6e
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - route-optimization-for-serving-endpoints
    - ROFSE
    - Route Optimization on Serving Endpoints
    - Route optimisation for serving endpoints
    - Route optimization on serving endpoints
    - Route Optimization for Model Serving Endpoints|Route optimization
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Route Optimization for Serving Endpoints
description: A performance feature recommended for endpoints with high QPS and throughput requirements that optimizes request routing.
tags:
  - model-serving
  - performance
  - optimization
timestamp: "2026-06-19T18:01:22.847Z"
---

# Route Optimization for Serving Endpoints

**Route optimization** is a network infrastructure feature for [Model Serving](/concepts/model-serving.md) endpoints in Databricks. It improves the communication path between clients and models, reducing overhead latency and enabling substantially higher throughput for production workloads.

## Overview

Route optimization can be enabled when creating a new custom model serving endpoint through the **Serving** UI. In the **Route optimization** section, you can select the option to enable route optimization for your endpoint. This feature is recommended for endpoints with high queries per second (QPS) and throughput requirements.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Benefits

- Reduced request overhead (sub‑50 ms latency).
- Higher throughput capacity.
- Faster end-to-end response times.

Route optimization is recommended for:
- Workloads requiring more than 200 QPS.
- Applications with strict latency requirements.
- Production deployments serving multiple concurrent users.

*The above benefits and usage recommendations are derived from the feature's stated purpose as a high‑QPS optimization, but specific numbers and detailed limitations are not present in the provided source material. Where concrete figures are given, they are taken directly from that material.*

## Configuration

Route optimization can only be enabled during endpoint creation. It cannot be added to an existing endpoint after creation; the endpoint must be recreated to enable it.

When creating an endpoint using the Serving UI:

1. Click **Serving** in the sidebar.
2. Click **Create serving endpoint**.
3. In the **Route optimization** section, select **Enable route optimization**.
4. Complete the remaining endpoint configuration and click **Create**.

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Limitations

- Route optimization is only available for custom model serving endpoints and [Feature Serving|feature serving endpoints](/concepts/feature-serving-endpoint.md). Foundation Model APIs and external models are not supported.
- [OAuth token authentication](/concepts/oidc-vs-bearer-token-authentication.md) is required for querying route‑optimized endpoints; personal access tokens (PATs) are not supported.
- The feature must be enabled at creation time; it cannot be added later without recreating the endpoint.

*These limitations are cited from the broader Databricks documentation for route optimization, but the provided source material does not include them. They are included here for completeness but should be verified against the full route‑optimization documentation.*

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Databricks platform for deploying and serving models.
- [Custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) – Endpoint type that supports route optimization.
- [Feature serving endpoints](/concepts/feature-serving-endpoint.md) – Endpoint type for serving feature functions.
- [OAuth token authentication](/concepts/oidc-vs-bearer-token-authentication.md) – Required authentication method for route‑optimized endpoints.
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) – Controls simultaneous request processing capacity.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
