---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 409a8338e609566419442cf87fce7ae6e10c9baf348b37c3d6ff0f9c6ff5f667
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - route-optimized-model-serving-endpoints
    - RMSE
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Route-Optimized Model Serving Endpoints
description: A Databricks Model Serving feature that enables OAuth-based authentication and requires specific endpoint configuration (fixed concurrency, disabled scale-to-zero) for effective load testing.
tags:
  - model-serving
  - networking
  - authentication
timestamp: "2026-06-19T09:22:24.455Z"
---

---
title: Route-Optimized Model Serving Endpoints
summary: A configuration option for Databricks Model Serving endpoints that improves routing efficiency, recommended as a best practice when load testing custom model serving endpoints.
sources:
  - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:30:00.000Z"
updatedAt: "2026-06-18T11:30:00.000Z"
tags:
  - databricks
  - model-serving
  - load-testing
  - optimization
aliases:
  - route-optimized-model-serving-endpoints
  - ROMSE
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Route-Optimized Model Serving Endpoints

**Route-Optimized Model Serving Endpoints** refer to a configuration setting in Databricks Model Serving that enables advanced routing logic for incoming inference requests. When enabled, the endpoint distributes requests more efficiently across available replicas, reducing latency and improving throughput. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

Route optimization is a recommended best practice when setting up [Model Serving endpoints](/concepts/model-serving-endpoint.md) for production workloads, particularly when conducting load testing. The Databricks documentation advises enabling route optimization as part of the endpoint configuration to achieve reliable performance metrics during load tests. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Configuration

Route optimization is enabled at endpoint creation time through the Serving UI or API. For load testing purposes, Databricks recommends:

- Starting with a "Small" CPU endpoint (endpoint concurrency of 4) with both minimum and maximum concurrency set to 4.
- Enabling route optimization.
- Disabling Scale to Zero to ensure constant availability during the test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Importance in Load Testing

When performing load testing with tools like Locust, enabling route optimization ensures that the endpoint's routing layer does not become a bottleneck. Standardized load tests assume that route optimization is turned on so that the measured performance reflects the model's true serving capacity. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The core endpoint where models are deployed for inference.
- [Load testing for serving endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) – General approach to testing endpoint performance.
- Endpoint concurrency – The number of simultaneous requests an endpoint can handle.
- Scale to Zero – Feature that automatically shuts down idle endpoints; recommended to disable during load tests.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
