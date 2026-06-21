---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 986c1defdb8a8d6b4a621dfc77406abb865da1ebdee662d72f4f91dd8ab1c03c
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-compute-specification
    - SGCS
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Serverless GPU Compute Specification
description: Configuration of GPU resources for AIR workloads, including accelerator type (e.g., GPU_1xA10), count of accelerators, and distributed multi-node support.
tags:
  - databricks
  - gpu
  - compute
  - infrastructure
timestamp: "2026-06-19T08:57:09.506Z"
---

Here is the wiki page for "Serverless GPU Compute Specification".

---

## Serverless GPU Compute Specification

The **Serverless GPU Compute Specification** defines the hardware and software resources allocated to a serverless GPU workload. It is specified in a YAML configuration file used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) and determines the type and number of accelerators, as well as the serverless environment version. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Specification Fields

#### `compute` block

The `compute` block in the YAML configuration describes the GPU resources required for the workload. It contains two required fields:

- **`num_accelerators`**: The number of GPU accelerators to allocate for the workload. For example, `1` specifies a single GPU. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]
- **`accelerator_type`**: The type of GPU accelerator. The available types include serverless-compatible GPU types, such as `GPU_1xA10`, which provisions a single NVIDIA A10 GPU. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Example:

```yaml
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
```

#### `environment` block

The optional `environment` block specifies the serverless GPU environment version. The `version` field selects the runtime environment used for the workload. If omitted, it defaults to `'4'`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Example:

```yaml
environment:
  version: '4'
```

The environment also supports a `dependencies` list, where Python packages (e.g., `torch`, `transformers`) can be declared for automatic installation on the remote compute node. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Overriding the Specification

Specification fields can be overridden at submission time via the command line. For example:

```bash
air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120
```

This overrides `num_accelerators` to 32 and sets a new timeout, while leaving the rest of the YAML config intact. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Validation

The specification can be validated without submitting a workload using the `--dry-run` flag:

```bash
air run --file train.yaml --dry-run
```

This checks the configuration for errors without consuming any GPU resources. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool used to submit workloads with this specification.
- GPU Scheduling — How GPU resources are allocated and managed across workloads.
- Serverless GPU Environment Versions — The full list of available runtime versions.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) — The complete reference for all YAML configuration fields.

### Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
