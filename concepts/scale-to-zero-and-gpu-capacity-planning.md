---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7238e20cff27e0aeb93141dc2ae3edaf55c7d8354952ebe156a56878c049a5c6
  pageDirectory: concepts
  sources:
    - serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scale-to-zero-and-gpu-capacity-planning
    - GPU Capacity Planning and Scale-to-Zero
    - SAGCP
    - capacity planning
  citations:
    - file: serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
title: Scale-to-Zero and GPU Capacity Planning
description: The scale-to-zero behavior and capacity planning considerations for custom LLM serving endpoints on Databricks, including fixed replica counts, cold start latency, and cloud provider GPU availability constraints.
tags:
  - scaling
  - capacity-planning
  - gpu
timestamp: "2026-06-19T23:02:15.896Z"
---

# Scale-to-Zero and GPU Capacity Planning

**Scale-to-Zero and GPU Capacity Planning** refers to the configuration decisions and operational considerations for managing GPU serving endpoints that can scale down to zero replicas when idle, and the capacity constraints that affect cold-start reliability for GPU-backed [Model Serving on Databricks](/concepts/model-serving-on-databricks.md).

## Overview

When deploying custom LLMs with [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md), you can configure endpoints to scale down to zero replicas when idle by setting `scale_to_zero_enabled=True`. This reduces costs during periods of no traffic but introduces cold-start latency and capacity risks. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Scale-to-Zero Behavior

Setting `scale_to_zero_enabled=True` allows the endpoint to scale down to zero replicas when idle. When a request arrives after the endpoint has scaled to zero, the system must acquire GPU capacity and start the model before it can serve the request. Cold starts are slow — loading model weights and starting vLLM typically takes one to several minutes. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

For latency-sensitive or production-critical workloads, set `scale_to_zero_enabled=False` and size `workload_size` for your peak traffic up front. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Capacity Planning Considerations

### No Autoscaling Between Replicas

Custom LLM serving in Beta provisions a fixed number of replicas behind your endpoint. **Autoscaling between more than zero replicas is not yet supported**, so you must size `workload_type` and `workload_size` for your peak traffic. The endpoint queues requests that exceed the capacity of provisioned replicas. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### GPU Capacity Constraints

**Scale-up capacity is not guaranteed.** Whenever Databricks needs to acquire a new GPU for your endpoint — on creation, on `workload_size` increase, or when an endpoint wakes up from zero — the request can stop responding if the cloud provider has no GPU capacity in your region. This applies to all GPU types but is most constrained for `GPU_XLARGE` (H100). Databricks mitigates this with warm pools and prereservation, which keep GPU capacity available and ready. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### H100 (GPU_XLARGE) Limitations

`GPU_XLARGE` (1xH100) endpoints do not support `scale_to_zero_enabled=True` during Beta. H100 capacity is too constrained to guarantee a successful cold-start scale-up. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Configuration Example

The following example shows a typical configuration with scale-to-zero enabled:

```python
ServedEntityInput(
    entity_name="main.<catalog>.<model_name>",
    entity_version="<version>",
    workload_type=ServingModelWorkloadType.GPU_MEDIUM,
    workload_size="Small",
    scale_to_zero_enabled=True,
)
```

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Best Practices

- **For development and low-traffic workloads**: Use `Small` workload size and enable scale-to-zero to minimize costs during idle periods. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- **For production-critical workloads**: Set `scale_to_zero_enabled=False` and size `workload_size` for your peak traffic to avoid cold-start latency and capacity acquisition failures. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- **For H100-based endpoints**: Do not enable scale-to-zero during Beta. Plan for always-on capacity. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- **Account for regional GPU availability**: Capacity constraints vary by region and GPU type. Consult with your Databricks account team for H100 availability. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) — The serving infrastructure for custom LLMs.
- vLLM — The inference engine used for custom LLM serving.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure that provisions GPU resources.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Multi-GPU configuration for training workloads.
- [Express Deployments](/concepts/express-deployments-databricks.md) — The deployment mechanism used by custom LLM serving.

## Sources

- serve-custom-llms-with-custom-model-serving-databricks-on-aws.md

# Citations

1. [serve-custom-llms-with-custom-model-serving-databricks-on-aws.md](/references/serve-custom-llms-with-custom-model-serving-databricks-on-aws-ee23a7aa.md)
