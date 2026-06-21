---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c0000ac0b2384a5a398b4c9c71333f134b11e2177a47b348b491c797f95e381
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-type-options-for-model-serving-endpoints
    - CTOFMSE
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Compute type options for Model Serving endpoints
description: Model Serving provides CPU and GPU compute types including CPU_MEDIUM and CPU_LARGE variants that trade concurrency for higher memory per worker; GPU requires explicit code setup for GPU-based predictions, though MLflow handles this automatically for PyTorch and Transformers flavors.
tags:
  - compute
  - model-serving
  - infrastructure
timestamp: "2026-06-19T18:04:17.878Z"
---

# Compute type options for Model Serving endpoints

**Compute type options for Model Serving endpoints** refers to the CPU and GPU configurations available when deploying [custom models](/concepts/custom-mlflow-pythonmodel.md) as production-grade API endpoints on Databricks. These options determine the hardware resources allocated to process inference requests and affect both performance and cost.

## Overview

Model Serving provides a variety of CPU and GPU compute options for deploying custom models. The available compute types allow you to select the appropriate hardware for serving your model based on factors such as model size, latency requirements, memory needs, and whether the model requires GPU acceleration. ^[custom-models-overview-databricks-on-aws.md]

When deploying with a GPU, you must configure your code to run predictions on the GPU using the methods provided by your framework. MLflow handles this automatically for models logged with the PyTorch or Transformers flavors. ^[custom-models-overview-databricks-on-aws.md]

## CPU compute types

| Compute type | Description |
|--------------|-------------|
| `CPU`       | Standard CPU compute for models that do not require GPU acceleration |
| `CPU_MEDIUM` | Provides more memory per worker than standard `CPU` |
| `CPU_LARGE` | Provides even more memory per worker than `CPU_MEDIUM` |

The `CPU_MEDIUM` and `CPU_LARGE` workload types allow you to trade concurrency for additional memory per worker on the same CPU hardware. Use these options when your model requires more memory than the standard `CPU` configuration provides. ^[custom-models-overview-databricks-on-aws.md]

## GPU compute types

GPU compute types are available for models that benefit from GPU acceleration. The specific GPU types available depend on your workspace configuration and cloud provider. For a complete list of supported GPU instance types, see the supported GPU types on Databricks documentation. ^[custom-models-overview-databricks-on-aws.md]

## Selecting the appropriate compute type

Consider the following factors when selecting a compute type for your model serving endpoint:

- **Model size**: Larger models may require more memory than standard CPU provides
- **Inference latency**: GPU acceleration can reduce inference time for computationally intensive models
- **Concurrency requirements**: CPU configurations with more memory per worker can handle higher concurrency for memory-intensive workloads
- **Cost**: GPU compute types generally cost more than CPU compute types

For detailed guidance on creating and managing serving endpoints, see create custom model serving endpoints. ^[custom-models-overview-databricks-on-aws.md]

## Related concepts

- [Custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [External Models](/concepts/external-models.md)
- [Model Serving](/concepts/model-serving.md)
- GPU scheduling
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
