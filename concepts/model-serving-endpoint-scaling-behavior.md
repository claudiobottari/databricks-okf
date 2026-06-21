---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02c6e518e1c4f61da9eb1f8b21d70ec207903498e7db8a56907ea8317b7986d1
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-scaling-behavior
    - MSESB
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Model Serving endpoint scaling behavior
description: "Serving endpoints auto-scale based on traffic: scale up near-instantly under load, scale down every five minutes, with optional scale-to-zero after 30 minutes of inactivity (cold start adds latency). Provisioned concurrency = QPS × execution time."
tags:
  - model-serving
  - scaling
  - performance
timestamp: "2026-06-19T18:03:34.379Z"
---

# Model Serving Endpoint Scaling Behavior

**Model Serving Endpoint Scaling Behavior** describes how [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints for custom models automatically adjust capacity in response to traffic patterns. Endpoints scale up to handle increased load and scale down to reduce resource consumption during periods of lower activity. The behavior described in this page applies to endpoints serving custom models and does not apply to endpoints that serve foundation models or external models. ^[custom-models-overview-databricks-on-aws.md]

## Provisioned Concurrency

Provisioned concurrency is the maximum number of parallel requests the system can handle. To estimate the required concurrency for an endpoint, use the following formula:

```
provisioned concurrency = queries per second (QPS) × model execution time (s)
```

To validate your concurrency configuration, see [Load testing for serving endpoints](/concepts/load-testing-for-ml-serving-endpoints.md). ^[custom-models-overview-databricks-on-aws.md]

## Scaling Up

Endpoints scale up almost immediately with increased traffic. When a new node is added, it becomes ready to serve traffic only after the model is downloaded and passes health checks. The time required to scale up depends on the model size and load time. ^[custom-models-overview-databricks-on-aws.md]

## Scaling Down

Endpoints scale down every five minutes to match reduced traffic levels. ^[custom-models-overview-databricks-on-aws.md]

## Scale to Zero

Scale to zero is an optional feature for endpoints. When enabled, the endpoint scales down to zero after 30 minutes of inactivity. The first request after scaling to zero experiences a "cold start," which results in higher latency. Scaling up from zero typically takes 10–20 seconds, but can sometimes take minutes. There is no SLA on scale from zero latency. ^[custom-models-overview-databricks-on-aws.md]

> **Warning:** Scale to zero should not be used for production workloads that require consistent uptime or guaranteed response times. For latency-sensitive applications or endpoints requiring continuous availability, disable scale to zero. ^[custom-models-overview-databricks-on-aws.md]

## GPU Workload Scaling

Autoscaling for GPU serving takes longer than for CPU serving. Additionally, GPU capacity is not guaranteed when scaling to zero — GPU endpoints might experience extra high latency for the first request after scaling to zero. ^[custom-models-overview-databricks-on-aws.md]

## Performance Optimization

For high QPS and low latency use cases, route optimization is the optimal and recommended option to improve performance. For faster endpoint deployment speed, use [express deployments](/concepts/express-deployments-databricks.md). ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md)
- [Query serving endpoints for custom models](/concepts/model-serving-endpoint-custom-models.md)
- [Route optimization on serving endpoints](/concepts/route-optimization-for-serving-endpoints.md)
- [Express deployments for model serving endpoints](/concepts/express-deployments-for-model-serving.md)
- Model Serving Debugging
- [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md)

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
