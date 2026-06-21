---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2b289fe92291aee56ca8fa90aa05db969f28ec2547a2a5bde209447bd7b0533
  pageDirectory: concepts
  sources:
    - route-optimization-on-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoints-databricks
    - MSE(
  citations:
    - file: route-optimization-on-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoints (Databricks)
description: Custom model serving endpoints on Databricks that can be configured with route optimization for improved performance.
tags:
  - model-serving
  - endpoints
  - databricks
  - machine-learning
timestamp: "2026-06-19T20:15:58.049Z"
---

# Model Serving Endpoints (Databricks)

**Model Serving Endpoints** on Databricks provide a managed infrastructure for deploying machine learning models and feature serving functions as production-ready API endpoints. These endpoints enable real-time inference with configurable compute resources, automatic scaling, and monitoring capabilities.

## Overview

Databricks Model Serving allows you to deploy custom models, foundation models, and feature serving functions behind REST API endpoints. Endpoints can be configured with different workload sizes, scale-to-zero capabilities, and compute types (CPU or GPU). ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

Serving endpoints support both model serving (for ML model inference) and Feature Serving (for feature function serving), each with similar configuration options and management interfaces. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Route Optimization

**Route optimization** is a feature that improves the network path for inference requests on custom model serving endpoints and feature serving endpoints. When enabled, route optimization provides:

- Faster, more direct communication between client and model
- Higher queries per second (QPS) throughput
- More stable and lower latency ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

### Enabling Route Optimization

Route optimization can only be enabled **during endpoint creation** — existing endpoints cannot be updated to use route optimization. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

For model serving endpoints, route optimization is enabled through the Serving UI by selecting **Enable route optimization** during creation. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

For feature serving endpoints, route optimization is enabled by specifying the full name of the feature specification in the `entity_name` field and setting `"route_optimized": true` in the API request. The `entity_version` is not needed for `FeatureSpecs`. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

### Querying Route-Optimized Endpoints

Route-optimized endpoints use a different URL and authentication mechanism compared to non-optimized endpoints. They require OAuth tokens for authentication — personal access tokens are not supported for route-optimized endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

### Limitations of Route Optimization

- Available only for **custom model serving endpoints** and **feature serving endpoints**
- Not supported for [Foundation Model APIs](/concepts/foundation-model-apis.md) or [External Models](/concepts/external-models.md)
- Only supports Databricks in-house OAuth tokens; personal access tokens cannot be used ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Requirements

Route-optimized model serving endpoints must meet the same requirements as non-route-optimized [Model Serving Endpoints](/concepts/model-serving-endpoint.md) for model deployment and configuration. Similarly, route-optimized feature serving endpoints follow the same requirements as standard feature serving endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Feature Serving — Deploying feature functions through serving endpoints
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Pre-built model endpoints (not supported with route optimization)
- [External Models](/concepts/external-models.md) — Third-party model integration (not supported with route optimization)
- Model Serving Production Optimization — Best practices for production deployment
- [Query Route-Optimized Serving Endpoints](/concepts/query-route-optimized-serving-endpoints.md) — Specific instructions for querying optimized endpoints
- OAuth Authentication — Required authentication method for route-optimized endpoints

## Sources

- route-optimization-on-serving-endpoints-databricks-on-aws.md

# Citations

1. [route-optimization-on-serving-endpoints-databricks-on-aws.md](/references/route-optimization-on-serving-endpoints-databricks-on-aws-9093903f.md)
