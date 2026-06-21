---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa086691df3b6425ecc437c463fbc3f4aa750db1908767e2632bf22618332119
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-types-for-databricks-model-serving
    - CTFDMS
    - Compute Types for Model Serving
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Compute Types for Databricks Model Serving
description: Variety of CPU and GPU workload types for model deployment, including CPU_MEDIUM and CPU_LARGE which trade concurrency for more memory per worker on the same CPU hardware.
tags:
  - compute
  - model-serving
  - databricks
  - infrastructure
timestamp: "2026-06-19T14:40:16.771Z"
---

# Compute Types for Databricks Model Serving

**Compute Types for Databricks Model Serving** refers to the CPU and GPU hardware options available when deploying custom models as production-grade APIs on the Databricks platform. The choice of compute type affects throughput, memory capacity, latency, and cost for inference workloads.

## Overview

Model Serving provides a variety of CPU and GPU options for deploying custom models. These compute types control the resources available to each model replica and influence how many concurrent requests an endpoint can handle. ^[custom-models-overview-databricks-on-aws.md]

## CPU Compute Types

The standard CPU workload type provides a baseline level of memory and compute. For models that require additional memory without moving to a different hardware class, Databricks offers two extended CPU types:

- **`CPU_MEDIUM`** – Trades some concurrency for more memory per worker while remaining on the same CPU hardware as the standard CPU type.
- **`CPU_LARGE`** – Provides an even larger memory footprint per worker, suitable for models with higher memory demands.

Use `CPU_MEDIUM` or `CPU_LARGE` when your model needs more memory than the standard CPU type provides. ^[custom-models-overview-databricks-on-aws.md]

## GPU Compute Types

GPU endpoints are available for custom models that benefit from hardware acceleration, such as deep learning models built with PyTorch, TensorFlow, or HuggingFace Transformers. When deploying with a GPU, you must ensure that your prediction code runs on the GPU using your framework’s device management methods. MLflow handles this automatically for models logged with the PyTorch or Transformers flavors. ^[custom-models-overview-databricks-on-aws.md]

For very large language models, Databricks recommends using [Foundation Model APIs](/concepts/foundation-model-apis.md) instead of custom model GPU serving because the container build and deployment process for large models may timeout (exceeding 60 minutes) or fail due to storage limitations. ^[custom-models-overview-databricks-on-aws.md]

## GPU Workload Considerations

When using GPU compute types, be aware of the following limitations:

- **Container image creation** takes longer for GPU serving than CPU serving because of larger model sizes and increased installation requirements.
- **Model deployment timeout** can occur if the container build and model deployment exceed 60 minutes.
- **Autoscaling** is slower for GPU endpoints compared to CPU endpoints.
- **Scale-to-zero** behavior: GPU capacity is not guaranteed when scaling to zero, and the first request after scaling from zero may experience extra high latency.
- **Storage limits**: Container builds may fail with a “No space left on device” error for very large models.

These limitations make GPU serving most appropriate for models that are not extremely large and that have predictable traffic patterns. ^[custom-models-overview-databricks-on-aws.md]

## Best Practices

- Use `CPU_MEDIUM` or `CPU_LARGE` for models that are memory-bound but do not require GPU acceleration.
- For GPU deployments, explicitly set the device in your custom code unless using an MLflow native flavor that handles it automatically.
- Avoid serving very large language models (e.g., 10B+ parameters) as custom GPU models; use [Foundation Model APIs](/concepts/foundation-model-apis.md) instead.
- Disable scale-to-zero for production GPU endpoints to avoid cold-start latency.
- Validate concurrency requirements using load testing before setting provisioned concurrency.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The core serving infrastructure on Databricks
- Custom models – Models deployed via MLflow that can use CPU or GPU compute
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Serverless endpoint for large foundation models
- MLflow PyTorch flavor – Automatic GPU handling for PyTorch models
- [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md) – Automatic GPU handling for HuggingFace models
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) – Maximum parallel requests a serving endpoint can handle
- [Scale to zero](/concepts/scale-to-zero-in-model-serving.md) – Optional feature for endpoints to scale down after inactivity

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
