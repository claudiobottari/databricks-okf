---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20889240f95ca0a2821ae2faa099b23c9eabed82de1e55143e4d8b55e6f78ef3
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-compute-types
    - MSCT
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Model Serving Compute Types
description: Variety of CPU and GPU compute options including CPU_MEDIUM and CPU_LARGE for trading concurrency for more memory; GPU requires explicit code setup for predictions.
tags:
  - compute
  - model-serving
  - databricks
timestamp: "2026-06-18T11:26:38.562Z"
---

# Model Serving Compute Types

**Model Serving Compute Types** refer to the CPU and GPU hardware options available for deploying custom models on Databricks Model Serving. When creating a serving endpoint, you select a compute type that determines the processing hardware, memory allocation, and concurrency characteristics for your model deployment. ^[custom-models-overview-databricks-on-aws.md]

## Available Compute Types

Model Serving provides a variety of CPU and GPU options for deploying custom models. The choice of compute type affects model performance, cost, and scaling behavior. ^[custom-models-overview-databricks-on-aws.md]

### CPU Compute Types

| Workload Type | Description |
|---|---|
| `CPU` | Standard CPU compute for general-purpose model serving |
| `CPU_MEDIUM` | CPU compute with increased memory per worker compared to standard `CPU` |
| `CPU_LARGE` | CPU compute with the highest memory per worker among CPU options |

The `CPU_MEDIUM` and `CPU_LARGE` workload types let you trade concurrency for more memory per worker on the same CPU hardware. Use them when your model needs more memory than standard `CPU` provides. ^[custom-models-overview-databricks-on-aws.md]

### GPU Compute Types

GPU compute types are available for models that benefit from GPU acceleration, such as deep learning models built with PyTorch, TensorFlow, or HuggingFace transformers. ^[custom-models-overview-databricks-on-aws.md]

When deploying with a GPU, you must ensure that your code is set up so that predictions are run on the GPU, using the methods provided by your framework. MLflow does this automatically for models logged with the PyTorch or Transformers flavors. ^[custom-models-overview-databricks-on-aws.md]

## Selecting a Compute Type

The appropriate compute type depends on your model's characteristics:

- **Model size and complexity**: Larger models with more parameters may require GPU compute or higher-memory CPU options.
- **Latency requirements**: GPU compute can significantly reduce inference time for deep learning models.
- **Concurrency needs**: Higher concurrency requires more compute resources. Estimate required concurrency using the formula: provisioned concurrency = queries per second (QPS) × model execution time (s). ^[custom-models-overview-databricks-on-aws.md]
- **Cost considerations**: CPU compute types are generally less expensive than GPU options.

## GPU Workload Limitations

When using GPU compute types, be aware of the following limitations: ^[custom-models-overview-databricks-on-aws.md]

- **Longer deployment time**: Container image creation for GPU serving takes longer than for CPU serving due to model size and increased installation requirements.
- **Timeout risk for large models**: When deploying very large models, the deployment process might timeout if the container build and model deployment exceed a 60-minute duration, or the container build might fail with "No space left on device" error due to storage limitations. For large language models, use [Foundation Model APIs](/concepts/foundation-model-apis.md) instead.
- **Slower autoscaling**: Autoscaling for GPU serving takes longer than for CPU serving.
- **Cold start latency**: GPU capacity is not guaranteed when scaling to zero. GPU endpoints might experience extra high latency for the first request after scaling to zero.

## Scaling Behavior

Serving endpoints automatically scale based on traffic and the capacity of provisioned concurrency units. The compute type influences scaling behavior: ^[custom-models-overview-databricks-on-aws.md]

- Endpoints scale up almost immediately with increased traffic.
- Endpoints scale down every five minutes to match reduced traffic.
- Nodes are ready to serve traffic after the model is downloaded and pass health checks; the model size and load time determine how long this takes.
- [Scale to zero](/concepts/scale-to-zero-in-model-serving.md) is an optional feature that allows endpoints to scale down to zero after 30 minutes of inactivity. The first request after scaling to zero experiences a "cold start," leading to higher latency.

## Related Concepts

- Custom Models — Models deployable on Model Serving using CPU or GPU compute
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Alternative for large language models that avoids GPU deployment limitations
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The deployment target for custom models
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) — Maximum parallel requests a serving endpoint can handle
- Scale to Zero — Optional feature for reducing endpoints to zero after inactivity
- Route Optimization — Performance improvement for high QPS and low latency use cases
- [Express Deployments](/concepts/express-deployments-databricks.md) — Faster endpoint deployment option

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
