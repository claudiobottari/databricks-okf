---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3c978ecb3fa1ff89edb8bb85056ae3cf6739c6b5385eadad067d917a597279a
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-creation-update-and-maintenance-expectations
    - Maintenance Expectations and Endpoint Creation, Update,
    - ECUAME
    - Endpoint creation and update expectations
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Endpoint Creation, Update, and Maintenance Expectations
description: "Key operational characteristics: ~10-minute deployment time, zero-downtime updates by keeping old config until new one is ready, 597-second request timeout, and occasional zero-downtime system maintenance where models are reloaded."
tags:
  - operations
  - model-serving
  - deployment
  - reliability
timestamp: "2026-06-19T14:40:14.154Z"
---

# Endpoint Creation, Update, and Maintenance Expectations

**Endpoint Creation, Update, and Maintenance Expectations** describe the operational characteristics of Databricks [Model Serving](/concepts/model-serving.md) endpoints for [custom models](/concepts/custom-mlflow-pythonmodel.md). These expectations cover deployment time, update behavior, request limits, scaling dynamics, and periodic system maintenance. The information in this article does not apply to endpoints serving foundation models or external models. ^[custom-models-overview-databricks-on-aws.md]

## Deployment Time

Deploying a newly registered model version involves packaging the model and its environment and provisioning the endpoint itself. The process typically takes approximately 10 minutes, but may take longer depending on model complexity, size, and dependencies. ^[custom-models-overview-databricks-on-aws.md]

## Zero-Downtime Updates

Databricks performs zero-downtime updates by keeping the existing endpoint configuration active until the new one becomes ready. This reduces the risk of interruption for endpoints that are in use. During the update process, you are billed for both the old and new endpoint configurations until the transition is complete. ^[custom-models-overview-databricks-on-aws.md]

## Request Timeout

If model computation takes longer than **597 seconds**, requests will time out. ^[custom-models-overview-databricks-on-aws.md]

## System Updates and Maintenance

Databricks performs occasional zero-downtime system updates and maintenance on existing Model Serving endpoints. During maintenance, Databricks reloads models. If a model fails to reload, the endpoint update is marked as failed and the existing endpoint configuration continues to serve requests. You should ensure that customized models are robust and able to reload at any time. ^[custom-models-overview-databricks-on-aws.md]

## Endpoint Scaling Expectations

Serving endpoints automatically scale based on traffic and the capacity of provisioned concurrency units.

- **Provisioned concurrency** is the maximum number of parallel requests the system can handle. Estimate the required concurrency as: `provisioned concurrency = queries per second (QPS) × model execution time (s)`. Use load testing to validate the configuration. ^[custom-models-overview-databricks-on-aws.md]
- **Scaling up** happens almost immediately with increased traffic. **Scaling down** occurs every five minutes to match reduced traffic. Nodes are ready to serve traffic after the model is downloaded and health checks pass; the model size and load time determine how long this takes. ^[custom-models-overview-databricks-on-aws.md]
- **Scale to zero** is an optional feature that allows endpoints to scale down to zero after 30 minutes of inactivity. The first request after scaling to zero experiences a *cold start*, leading to higher latency. Scaling up from zero usually takes 10–20 seconds, but can sometimes take minutes. There is no SLA on scale-from-zero latency. Scale to zero should not be used for production workloads requiring consistent uptime or guaranteed response times. ^[custom-models-overview-databricks-on-aws.md]
- **Route optimization** is recommended for high QPS and low latency use cases to improve performance. ^[custom-models-overview-databricks-on-aws.md]
- **Express deployments** provide faster endpoint deployment speed. ^[custom-models-overview-databricks-on-aws.md]

## GPU Workload Limitations

The following limitations apply to serving endpoints with GPU workloads:

- Container image creation for GPU serving takes longer than for CPU serving due to model size and increased installation requirements. ^[custom-models-overview-databricks-on-aws.md]
- When deploying very large models, the deployment process might time out if the container build and model deployment exceed a 60-minute duration, or the container build might fail with a "No space left on device" error due to storage limitations. For large language models, use [Foundation Model APIs](/concepts/foundation-model-apis.md) instead. ^[custom-models-overview-databricks-on-aws.md]
- Autoscaling for GPU serving takes longer than for CPU serving. ^[custom-models-overview-databricks-on-aws.md]
- GPU capacity is not guaranteed when scaling to zero. GPU endpoints may experience extra high latency for the first request after scaling to zero. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [Custom models overview](/concepts/custom-models-on-model-serving.md)
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- [Scale to zero](/concepts/scale-to-zero-in-model-serving.md)
- Route optimization
- [Express deployments](/concepts/express-deployments-databricks.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Load testing for serving endpoints](/concepts/load-testing-for-ml-serving-endpoints.md)

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
