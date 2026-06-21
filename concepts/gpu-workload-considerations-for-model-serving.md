---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 313ef506a9350aed409383ed4c3f525d9a6f749f0a0588f07989e2f1f29dfba4
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-workload-considerations-for-model-serving
    - GWCFMS
  citations:
    - file: custom-models-overview-databricks-on-aws.md
    - file: |-
        custom-models-overview-databricks-on-aws.md>

        Scale to zero should not be used for production workloads that require consistent uptime or guaranteed response times. For latency-sensitive applications or endpoints requiring continuous availability
    - file: disable scale to zero. ^[custom-models-overview-databricks-on-aws.md
title: GPU workload considerations for model serving
description: GPU serving has longer container build times, a 60-minute deployment timeout, storage constraints for large models, slower autoscaling than CPU, and no GPU capacity guarantee after scale-to-zero — large models should use Foundation Model APIs instead.
tags:
  - gpu
  - model-serving
  - performance-limitations
timestamp: "2026-06-19T18:03:47.925Z"
---

# GPU Workload Considerations for Model Serving

**GPU workload considerations for model serving** refers to the specific performance characteristics, limitations, and operational behaviors that apply when deploying custom models on GPU compute resources through Databricks Model Serving. Understanding these considerations is essential for planning reliable, low-latency production deployments.

## Deployment Time

Container image creation for GPU serving takes longer than image creation for CPU serving. This is due to larger model sizes and increased installation requirements for models served on GPU. ^[custom-models-overview-databricks-on-aws.md]

## Large Model Deployment Risks

When deploying very large models on GPU, the deployment process may timeout if the container build and model deployment exceed a 60-minute duration. Additionally, the container build might fail with a "No space left on device" error due to storage limitations. For large language models, Databricks recommends using [Foundation Model APIs](/concepts/foundation-model-apis.md) instead of custom model serving. ^[custom-models-overview-databricks-on-aws.md]

## Autoscaling Behavior

Autoscaling for GPU serving takes longer than for CPU serving. This means that GPU-backed endpoints may respond more slowly to sudden traffic spikes compared to CPU-backed endpoints. ^[custom-models-overview-databricks-on-aws.md]

## Scale to Zero Considerations

GPU capacity is not guaranteed when scaling to zero. If a GPU endpoint scales down to zero after 30 minutes of inactivity, the first request after scaling back up may experience extra high latency. This "cold start" latency is more pronounced for GPU workloads than for CPU workloads. ^[custom-models-overview-databricks-on-aws.md>

Scale to zero should not be used for production workloads that require consistent uptime or guaranteed response times. For latency-sensitive applications or endpoints requiring continuous availability, disable scale to zero. ^[custom-models-overview-databricks-on-aws.md]

## GPU Code Setup Requirements

When deploying with a GPU, you must ensure that your code is set up so that predictions run on the GPU, using the methods provided by your framework. MLflow does this automatically for models logged with the PyTorch or Transformers flavors. For other frameworks, manual configuration may be required. ^[custom-models-overview-databricks-on-aws.md]

## Compute Type Selection

Model Serving provides a variety of CPU and GPU options for deploying custom models. The `CPU_MEDIUM` and `CPU_LARGE` workload types allow trading concurrency for more memory per worker on the same CPU hardware, which can be useful when your model needs more memory than standard `CPU` provides. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- Custom Models Overview — General guidance for deploying custom models on Databricks.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Alternative for serving large language models without custom GPU deployment.
- [Model Serving Endpoint Scaling](/concepts/model-serving-endpoint-scaling.md) — General scaling behavior for serving endpoints.
- Scale to Zero — Optional feature affecting cold start latency.
- Route Optimization — Recommended for high QPS and low latency use cases.
- [Express Deployments](/concepts/express-deployments-databricks.md) — Faster endpoint deployment option.

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
2. custom-models-overview-databricks-on-aws.md>

Scale to zero should not be used for production workloads that require consistent uptime or guaranteed response times. For latency-sensitive applications or endpoints requiring continuous availability
3. disable scale to zero. ^[custom-models-overview-databricks-on-aws.md
