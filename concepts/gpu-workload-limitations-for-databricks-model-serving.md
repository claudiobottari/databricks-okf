---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3421185e0d00771c2234ae158dded105bca8a945a9c5e8e68f648561c288e399
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-workload-limitations-for-databricks-model-serving
    - GWLFDMS
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: GPU Workload Limitations for Databricks Model Serving
description: "Specific limitations when serving models on GPU: longer container image creation, potential timeouts for very large models exceeding 60-minute deployment, longer autoscaling, and no GPU capacity guarantee when scaling to zero."
tags:
  - gpu
  - model-serving
  - limitations
  - databricks
timestamp: "2026-06-19T14:40:00.912Z"
---

# GPU Workload Limitations for Databricks Model Serving

**GPU Workload Limitations for Databricks Model Serving** describes the known constraints and operational characteristics that apply when deploying custom models on GPU compute resources through Databricks Model Serving. These limitations affect deployment time, scaling behavior, capacity guarantees, and model size thresholds.

## Overview

When serving custom models with GPU compute, several limitations differ from CPU-based serving. These constraints arise from the larger model sizes typically associated with GPU workloads, the increased complexity of GPU container builds, and the availability characteristics of GPU infrastructure in cloud environments. ^[custom-models-overview-databricks-on-aws.md]

## Deployment Time

Container image creation for GPU serving takes longer than image creation for CPU serving. This is due to the larger model sizes and increased installation requirements for models served on GPU. ^[custom-models-overview-databricks-on-aws.md]

## Deployment Timeouts and Storage Failures

When deploying very large models, the deployment process might timeout if the container build and model deployment exceed a 60-minute duration. Additionally, the container build might fail with a "No space left on device" error due to storage limitations. For large language models, Databricks recommends using [Foundation Model APIs](/concepts/foundation-model-apis.md) instead of custom model serving. ^[custom-models-overview-databricks-on-aws.md]

## Autoscaling Behavior

Autoscaling for GPU serving takes longer than for CPU serving. This means that GPU endpoints may respond more slowly to sudden increases in traffic compared to CPU-based endpoints. ^[custom-models-overview-databricks-on-aws.md]

## Scale to Zero Considerations

GPU capacity is not guaranteed when scaling to zero. GPU endpoints might experience extra high latency for the first request after scaling to zero. This "cold start" behavior is more pronounced for GPU workloads than for CPU workloads. ^[custom-models-overview-databricks-on-aws.md]

## Comparison with CPU Serving

The following table summarizes key differences between GPU and CPU serving limitations:

| Aspect | GPU Serving | CPU Serving |
|--------|-------------|-------------|
| Container build time | Longer | Standard |
| Deployment timeout threshold | 60 minutes | Standard |
| Storage failure risk | Higher for large models | Lower |
| Autoscaling speed | Slower | Faster |
| Scale-to-zero latency | Extra high latency possible | Standard cold start |

^[custom-models-overview-databricks-on-aws.md]

## Best Practices

- For large language models, use [Foundation Model APIs](/concepts/foundation-model-apis.md) instead of custom model serving to avoid deployment timeouts and storage failures. ^[custom-models-overview-databricks-on-aws.md]
- Plan for longer deployment and scaling times when using GPU compute for production workloads. ^[custom-models-overview-databricks-on-aws.md]
- Avoid scale to zero for latency-sensitive GPU workloads that require consistent response times. ^[custom-models-overview-databricks-on-aws.md]
- Consider using [Express deployments for model serving endpoints](/concepts/express-deployments-for-model-serving.md) for faster endpoint deployment speed. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- Custom Models Overview — General guidance for deploying custom models on Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Alternative for serving large language models
- Endpoint Scaling Expectations — General scaling behavior for serving endpoints
- Scale to Zero — Optional feature for endpoints with inactivity periods
- [Express Deployments](/concepts/express-deployments-databricks.md) — Faster deployment option for serving endpoints
- Route Optimization — Performance improvement for high QPS use cases

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
