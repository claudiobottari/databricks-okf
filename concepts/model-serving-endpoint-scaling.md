---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef3a289d1a34acce2c96577f2a3e23cf1a568ebc5adf594cad69e930f5d3ff90
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-scaling
    - MSES
    - Model Serving Endpoint Sizing
    - Serving Endpoint Scaling
    - Endpoint Scaling
    - Endpoint autoscaling
    - Endpoint scaling
    - Endpoint scaling expectations
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Model Serving Endpoint Scaling
description: Automatic scaling of serving endpoints based on traffic and provisioned concurrency, including scale-to-zero after 30 minutes of inactivity, route optimization for high QPS, express deployments, and scaling behavior (immediate scale-up, 5-minute scale-down intervals).
tags:
  - scaling
  - model-serving
  - performance
  - databricks
timestamp: "2026-06-19T14:39:51.072Z"
---

# Model Serving Endpoint Scaling

**Model Serving Endpoint Scaling** describes how Databricks Model Serving endpoints for custom models automatically adjust their capacity based on incoming traffic and the configured provisioned concurrency. Understanding this behavior is essential for balancing performance, cost, and reliability in production deployments.^[custom-models-overview-databricks-on-aws.md]

## Provisioned Concurrency

**Provisioned concurrency** defines the maximum number of parallel requests the serving endpoint can handle simultaneously. To estimate the required concurrency for your workload, use the following formula:

```
provisioned concurrency = queries per second (QPS) × model execution time (seconds)
```

After configuring provisioned concurrency, Databricks recommends validating your settings through [load testing for serving endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) to ensure the endpoint can handle expected traffic patterns.^[custom-models-overview-databricks-on-aws.md]

## Scaling Behavior

Serving endpoints exhibit different scaling characteristics for scale-up and scale-down events:

- **Scale up**: Endpoints scale up almost immediately when traffic increases, adding capacity to handle the additional load.
- **Scale down**: Endpoints scale down every five minutes to match reduced traffic, gradually releasing unused resources.
- **Node readiness**: After a new node is provisioned, it becomes ready to serve traffic only once the model is fully downloaded and health checks pass. The time required depends on model size and load time.^[custom-models-overview-databricks-on-aws.md]

## Scale to Zero

**Scale to zero** is an optional feature that allows an endpoint to scale down to zero instances after 30 minutes of inactivity. When the first request arrives after scaling to zero, a "cold start" occurs, resulting in higher latency. Scaling up from zero typically takes 10–20 seconds but can sometimes take minutes. There is no SLA on scale-from-zero latency.^[custom-models-overview-databricks-on-aws.md]

> **Warning**: Scale to zero should not be used for production workloads that require consistent uptime or guaranteed response times. For latency-sensitive applications or endpoints requiring continuous availability, disable scale to zero.^[custom-models-overview-databricks-on-aws.md]

## Route Optimization

For high QPS and low latency use cases, route optimization is the optimal and recommended option to improve performance. Route optimization reduces per-request overhead by routing traffic more efficiently within the serving infrastructure.^[custom-models-overview-databricks-on-aws.md]

## Express Deployments

For faster endpoint deployment speed, use [express deployments](/concepts/express-deployments-databricks.md) for model serving endpoints. Express deployments reduce the time required to make a new model version available behind an endpoint.^[custom-models-overview-databricks-on-aws.md]

## GPU Workload Considerations

GPU serving endpoints have additional scaling limitations compared to CPU endpoints:

- **Autoscaling duration**: Autoscaling for GPU serving takes longer than for CPU serving.
- **Scale-to-zero risks**: GPU capacity is not guaranteed when scaling to zero. GPU endpoints may experience extra high latency for the first request after scaling to zero.
- **Deployment time**: Container image creation for GPU serving takes longer due to model size and increased installation requirements. For very large models, the deployment process might time out if the container build and model deployment exceed 60 minutes, or the container build might fail with "No space left on device" errors. For large language models, Databricks recommends using [Foundation Model APIs](/concepts/foundation-model-apis.md) instead.^[custom-models-overview-databricks-on-aws.md]

## Billing During Updates

During zero-downtime endpoint updates, you are billed for both the old and new endpoint configurations until the transition is complete. Databricks keeps the existing endpoint configuration active until the new one becomes ready to reduce risk of interruption.^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- Scale to Zero
- Route Optimization
- [Express Deployments](/concepts/express-deployments-databricks.md)
- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md)
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- GPU Workload Limitations

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
