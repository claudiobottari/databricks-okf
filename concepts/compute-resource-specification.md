---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 516634f6a7fe4e6780ff9e4fa336e5a9ee87e47d732b0733e072906b584bd0c7
  pageDirectory: concepts
  sources:
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-resource-specification
    - CRS
    - CRPS
  citations:
    - file: workload-yaml-reference-databricks-on-aws.md
title: Compute Resource Specification
description: Configuration of GPU resources for a training workload using `num_accelerators` and `accelerator_type` fields, supporting types like GPU_1xA10 and GPU_8xH100.
tags:
  - gpu
  - compute
  - databricks
timestamp: "2026-06-19T23:27:04.188Z"
---

# Compute Resource Specification

The **compute resource specification** is a required block in the [AI Runtime](/concepts/ai-runtime.md) [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) that defines the GPU resources allocated to a training job. It is specified under the `compute` key and must include both the type and the number of accelerators. ^[workload-yaml-reference-databricks-on-aws.md]

## Fields

The `compute` block contains two mandatory fields:

- **`num_accelerators`** (`integer`): The number of GPUs (or accelerators) to allocate. Common values are `1` (single GPU) or `8` (full node). ^[workload-yaml-reference-databricks-on-aws.md]
- **`accelerator_type`** (`string`): The type of accelerator. Examples include `GPU_1xA10` for a single NVIDIA A10 GPU and `GPU_8xH100` for a node with eight NVIDIA H100 GPUs. ^[workload-yaml-reference-databricks-on-aws.md]

## Supported GPU Types

The reference documentation provides two example accelerator types:

| Accelerator Type | Description |
|------------------|-------------|
| `GPU_1xA10`      | Single NVIDIA A10 GPU |
| `GPU_8xH100`     | Eight NVIDIA H100 GPUs on a single node |

For a complete list of supported GPU types, capabilities, and recommended use cases, see the Hardware Options page. ^[workload-yaml-reference-databricks-on-aws.md]

## Examples

### Minimal configuration (single GPU)

```yaml
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
```

^[workload-yaml-reference-databricks-on-aws.md]

### Large model training (8 H100 GPUs)

```yaml
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
```

^[workload-yaml-reference-databricks-on-aws.md]

## Usage in Full YAML

The `compute` block is part of a larger workload YAML that includes `experiment_name`, `environment`, `command`, and optional fields such as `code_source`, `parameters`, `max_retries`, `timeout_minutes`, and `usage_policy_id`. ^[workload-yaml-reference-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The environment in which the workload runs.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The infrastructure provisioning GPU resources.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific compute configuration.
- [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) – Full reference for YAML fields.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – How multiple GPUs are used for training.

## Sources

- workload-yaml-reference-databricks-on-aws.md

# Citations

1. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
