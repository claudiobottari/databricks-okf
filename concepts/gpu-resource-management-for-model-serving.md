---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1c343f9d7378e0f66aa4366a787cfff41bb4720aafc0cc09dca2df78d0d3cf0
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-resource-management-for-model-serving
    - GRMFMS
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: GPU Resource Management for Model Serving
description: Handling GPU availability, GPU container builds, and custom GPU serving configurations in Databricks Model Serving.
tags:
  - model-serving
  - gpu
  - containers
  - databricks
timestamp: "2026-06-19T09:56:37.169Z"
---

# GPU Resource Management for Model Serving

**GPU Resource Management for Model Serving** refers to the practices and considerations for provisioning, diagnosing, and optimizing GPU resources when deploying deep learning models on Databricks Model Serving. Because GPU availability is often constrained, proper management involves understanding GPU build failures, dependency configuration, and concurrency limitations.

## Overview

Model Serving endpoints that require GPU acceleration (e.g., for large language models or computer vision pipelines) depend on cloud GPU instance capacity. Several common issues can arise during container build and runtime that relate directly to GPU resource management. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## GPU Build Failures

Due to global GPU supply restrictions, a build may fail with the error:

```
Build could not start due to an internal error - please contact your Databricks representative.
```

To resolve this, contact your Databricks account team. Depending on region availability, they can provision additional GPU resources. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Dependency Management for GPU-Based Models

### Custom GPU Serving

For custom GPU serving endpoints, Model Serving automatically installs the recommended versions of `cuda` and `cuDNN` according to the public PyTorch and TensorFlow documentation. It is important to define all critical libraries as model dependencies to ensure reproducible behavior across environments. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Models Requiring `flash-attn`

If a model depends on `flash-attn`, Databricks recommends using a custom wheel version of `flash-attn` rather than relying on pip resolution alone. Otherwise, build errors such as `ModuleNotFoundError: No module named 'torch'` can occur. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

When specifying the custom wheel, you must include compatible PyTorch, torch, and torchvision versions that align with the CUDA version targeted by the `flash-attn` wheel. For example, for CUDA 11.8, use: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

- PyTorch index: `https://download.pytorch.org/whl/cu118`
- Torch 2.0.1+cu118
- Torchvision 0.15.2+cu118
- Flash-Attn wheel: `https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`

All pip requirements should be passed as a list to `mlflow.transformers.log_model(..., pip_requirements=[...])`.

## Space Constraints on GPU Nodes

A build may fail with:

```
OSError: [Errno 28] No space left on device
```

This can occur if too many large artifacts are logged alongside the model unnecessarily. Strip extraneous artifacts from the MLflow model and redeploy the slimmed-down package. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Concurrency and Quota Management

GPU endpoints are subject to the same concurrency and quota limits as CPU endpoints. The following errors may be encountered:

- **Workspace exceeded provisioned concurrency quota**: Indicates the workspace-level concurrency limit is reached for GPU endpoints. Free quota by deleting or stopping unused endpoints, or contact your Databricks account team to request an increase (limits depend on regional GPU availability). ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Too many concurrent requests (429)**: The endpoint’s current provisioned concurrency cannot handle the traffic. Enable autoscaling or manually increase provisioned concurrency. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- Model Serving Debugging Guide
- [Container Build Failures](/concepts/container-build-event-logs.md)
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- [Route Optimized Endpoints](/concepts/route-optimized-endpoints.md)
- GPU Availability on Databricks

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
