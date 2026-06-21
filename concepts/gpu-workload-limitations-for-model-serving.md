---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fd6b26b83f6fc0efa47d760afbaf74d3e6cacf943867d2742d37c53fa99c9d8
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-workload-limitations-for-model-serving
    - GWLFMS
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: GPU Workload Limitations for Model Serving
description: "Specific limitations when deploying custom models on GPU: longer container build times, potential timeout for large models (60-minute limit), longer autoscaling, and no guaranteed GPU capacity when scaling to zero."
tags:
  - gpu
  - model-serving
  - limitations
  - databricks
timestamp: "2026-06-19T09:39:52.665Z"
---

# GPU Workload Limitations for Model Serving

**GPU Workload Limitations for Model Serving** describes known constraints and behavioral characteristics specific to custom model serving endpoints that use GPU compute resources. These limitations do not apply to endpoints that serve foundation models or external models.^[custom-models-overview-databricks-on-aws.md]

## Longer Container Image Creation

Container image creation for GPU serving takes longer than for CPU serving due to larger model sizes and increased installation requirements for models served on GPU.^[custom-models-overview-databricks-on-aws.md]

## Deployment Timeouts and Storage Failures

When deploying very large models on GPU, the deployment process might timeout if the container build and model deployment exceed a 60-minute duration. The container build can also fail with a "No space left on device" error due to storage limitations. For large language models, use [Foundation Model APIs](/concepts/foundation-model-apis.md) instead.^[custom-models-overview-databricks-on-aws.md]

## Slower Autoscaling

Autoscaling for GPU serving takes longer than for CPU serving. This means that during traffic spikes, GPU endpoints may take more time to scale up provisioned concurrency to meet demand compared to CPU-based endpoints.^[custom-models-overview-databricks-on-aws.md]

## Scale-to-Zero Behavior and Cold Start Latency

GPU capacity is not guaranteed when scaling to zero. GPU endpoints might experience extra high latency for the first request after scaling to zero. This cold-start latency is in addition to the general scale-from-zero behavior documented for all endpoint types.^[custom-models-overview-databricks-on-aws.md]

## Alternative for Large Models

For large language models or other very large GPU-dependent models, Databricks recommends using [Foundation Model APIs](/concepts/foundation-model-apis.md) rather than serving the model as a custom GPU endpoint, to avoid the deployment timeouts, storage failures, and scaling delays described above.^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform providing custom model endpoint deployment
- Custom Models — User-provided models deployable on CPU or GPU
- [Endpoint Scaling](/concepts/model-serving-endpoint-scaling.md) — Autoscaling behavior and provisioned concurrency
- Scale to Zero — Optional feature that reduces endpoints to zero after inactivity
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Managed serving for large language models
- Container Build — The image packaging step that can fail for GPU models

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
