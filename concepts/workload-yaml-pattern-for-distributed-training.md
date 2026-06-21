---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25f3170cdec95f15f6ec44d4a1b0c5d6a52c351761206dd78df302c25702b53a
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.7
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workload-yaml-pattern-for-distributed-training
    - WYPFDT
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Workload YAML pattern for distributed training
description: Configuration-driven approach where distributed training workloads are defined in YAML files (e.g., train.yaml) and submitted via `air run -f`, separating launcher scripts from training code.
tags:
  - configuration
  - distributed-training
  - YAML
timestamp: "2026-06-19T08:56:21.347Z"
---

# Workload YAML Pattern for Distributed Training

The **Workload YAML pattern for distributed training** is a declarative configuration approach used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) to define and submit distributed training jobs. A YAML file (commonly named `train.yaml`) specifies the compute resources, launcher script, and training code, enabling reproducible and scalable multi-node or multi-GPU workloads. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Structure

A typical workload YAML for distributed training includes:

- **Compute resources**: Number of nodes and GPUs (e.g., 16 H100 GPUs across 2 nodes).
- **Launcher script**: The distributed launch mechanism, such as `torchrun` for PyTorch or the Ray Train launcher.
- **Training code**: The Python script that implements the model training loop.
- **Logging and checkpointing**: Configuration for [MLflow](/concepts/mlflow.md) logging and saving checkpoints to a [Unity Catalog](/concepts/unity-catalog.md) volume.

The job is submitted from the command line using:

```bash
air run -f train.yaml
```

^[ai-runtime-cli-examples-databricks-on-aws.md]

## Examples from the Source

The AI Runtime CLI documentation provides two complete end-to-end examples that illustrate this pattern:

| Example | Description |
|---------|-------------|
| **Multi-node LLM fine-tuning with FSDP** | Supervised fine-tuning of Llama-3.1-8B across 16 H100 GPUs (2 nodes) using `torchrun` and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). Logs to MLflow and checkpoints to a Unity Catalog volume. |
| **Distributed training with Ray Train** | Distributed data-parallel fine-tuning with [Ray Train's TorchTrainer](/concepts/ray-train-torchtrainer.md) across 8 H100 GPUs (single node), with one worker per GPU. |

^[ai-runtime-cli-examples-databricks-on-aws.md]

Each example includes the workload YAML itself, a launcher script, and the training source code. These serve as templates for adapting the pattern to other distributed training scenarios.

## Benefits

- **Declarative configuration**: Resource requirements and orchestration logic are captured in a single file, making jobs reproducible and easier to version-control.
- **Unified submission**: A single `air run` command handles launching the job on the cluster, regardless of the underlying distributed framework (FSDP, Ray Train, etc.).
- **Integration with Databricks ecosystem**: Built-in support for [MLflow](/concepts/mlflow.md) tracking and [Unity Catalog](/concepts/unity-catalog.md) volumes for checkpoints and artifacts.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Ray Train](/concepts/ray-train-resource-allocation.md)
- torchrun
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
