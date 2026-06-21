---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a34fd369b3e24c5e5babb8bed46aff544ef02d07e9e8f7bdff04cafe68d54faf
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-workload-limitations-in-model-serving
    - GWLIMS
    - GPU Workload Limitations with Model Serving
    - GPU workload limitations
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: GPU Workload Limitations in Model Serving
description: GPU serving endpoints have longer container build times, potential timeout for large models exceeding 60-minute builds, longer autoscaling, and no GPU capacity guarantee when scaling to zero.
tags:
  - gpu
  - model-serving
  - limitations
timestamp: "2026-06-18T14:57:41.322Z"
---

# GPU Workload Limitations in Model Serving

**GPU Workload Limitations in Model Serving** refers to specific constraints and behaviors that apply when deploying custom [Model Serving](/concepts/model-serving.md) endpoints that use GPU compute resources. These limitations affect deployment time, scaling behavior, and reliability for GPU-backed models compared to CPU-based deployments.

## Overview

While GPU instances offer significant performance advantages for deep learning and large‑scale inference, they introduce additional operational overhead in the model serving lifecycle. Databricks documents the following known limitations for custom model serving endpoints that use GPU workloads. ^[custom-models-overview-databricks-on-aws.md]

## Key Limitations

### Longer Container Image Build Time

Container image creation for GPU serving takes longer than for CPU serving. This is due to larger model sizes and increased installation requirements—GPU‑based models often rely on CUDA, cuDNN, and other platform‑specific libraries that must be included in the image. ^[custom-models-overview-databricks-on-aws.md]

### Deployment Timeouts and Storage Failures for Large Models

When deploying very large models, the deployment process may time out if the container build and model deployment together exceed 60 minutes. Alternatively, the container build may fail with a “No space left on device” error due to storage limitations. For large language models, Databricks recommends using [Foundation Model APIs](/concepts/foundation-model-apis.md) instead of custom model serving to avoid these issues. ^[custom-models-overview-databricks-on-aws.md]

### Slower Autoscaling

Autoscaling for GPU serving takes longer than for CPU serving. This means that GPU endpoints may take more time to react to sudden traffic spikes, potentially leading to increased latency or request queuing during scale‑up events. ^[custom-models-overview-databricks-on-aws.md]

### Scale‑to‑Zero Latency and Capacity Uncertainty

GPU capacity is not guaranteed when scaling to zero is enabled. When a GPU endpoint scales down to zero (after 30 minutes of inactivity), the first request after scaling up may experience extra‑high latency. Additionally, there is no SLA on the scale‑from‑zero duration for GPU endpoints, and the cold start can be significantly longer than for CPU endpoints. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – General architecture for deploying custom models as endpoints.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Alternative for serving large language models without custom GPU deployment limitations.
- Scaling to Zero – Optional feature that affects cold‑start latency on GPU endpoints.
- Custom Models Overview – Broader context for model logging, dependencies, and deployment expectations.
- Route Optimization – Recommended for high QPS / low latency use cases.
- [Express Deployments](/concepts/express-deployments-databricks.md) – Option for faster endpoint deployment.

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
