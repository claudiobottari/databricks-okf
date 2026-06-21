---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9b146f922f16d8253c2730527da2f26775690b39871612258de07e1ebde89ec
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scale-to-zero-in-model-serving
    - STZIMS
    - Scale to zero
    - Scale-to-Zero
    - Scale-to-zero
    - scale-to-zero
    - scale-to-zero behavior
    - scaled to zero
    - scale-to-zero-for-model-serving-endpoints
    - SFMSE
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Scale to Zero in Model Serving
description: Configuration option allowing endpoints to scale down when not in use, introducing cold-start latency and not recommended for production
tags:
  - scaling
  - performance
  - model-serving
timestamp: "2026-06-18T14:53:54.517Z"
---

# Scale to Zero in Model Serving

**Scale to Zero in Model Serving** is a configuration option for custom model serving endpoints on Databricks that allows the endpoint to shut down all compute resources when not actively serving requests. This feature is primarily designed for development, testing, and non-production workloads where continuous availability is not required.

## Overview

When you create a custom model serving endpoint, you can specify whether the endpoint should scale to zero when not in use. When enabled, the endpoint releases all allocated compute resources during periods of inactivity, reducing costs for idle endpoints.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

However, scale to zero is **not recommended for production endpoints**, as capacity is not guaranteed when scaled to zero. When an endpoint scales to zero, there is additional latency — also referred to as a cold start — when the endpoint scales back up to serve requests.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Configuration

Scale to zero can be configured during endpoint creation in the **Serving UI** under the **Compute Scale-out** section for each served entity. The available scale-out sizes include **Small** (0-4 requests), **Medium** (8-16 requests), and **Large** (16-64 requests).^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

Scale to zero is appropriate for:

- Development and testing environments
- Staging endpoints used intermittently
- Prototype or demo applications
- Workloads where occasional latency is acceptable

It is not suitable for:

- Production serving with strict latency requirements
- Business-critical applications requiring consistent response times
- High-throughput workloads

## Cold Start Considerations

When a scaled-to-zero endpoint receives a request, it must provision compute resources before it can serve the request. This cold start process introduces additional latency compared to a warm endpoint that maintains provisioned capacity. The exact latency depends on the model size, compute type (CPU or GPU), and cloud provider resource availability.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — The endpoints that support scale-to-zero configuration
- [GPU Workload Types on Databricks](/concepts/gpu-workload-types-in-databricks-model-serving.md) — Available GPU compute options for serving endpoints
- [Compute Scale-out Configuration](/concepts/compute-scale-out-configuration.md) — How to set min/max provisioned concurrency for serving
- [Serving Endpoint States](/concepts/model-serving-endpoint-status.md) — Understanding endpoint readiness and status transitions
- Model Serving Limits — Resource allocation constraints for serving endpoints
- [Cold Start in Model Serving](/concepts/foundation-model-serving-modes.md) — Performance implications of scaling from zero
- Production Model Serving Best Practices — Guidance for production-grade deployments

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
