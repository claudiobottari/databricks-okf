---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 263aa79c8e09510a48ae1680c9ff7493d311b78afe30a4ffdefc517f52219bce
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-cli
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: air CLI
description: Command-line interface for submitting and managing distributed training workloads on Databricks AI Runtime, using `air run -f train.yaml` as the primary submission command.
tags:
  - cli
  - databricks
  - workload-management
timestamp: "2026-06-19T13:56:26.304Z"
---

<answer>

# air CLI

**`air` CLI** is a command-line tool for submitting distributed training workloads on Databricks GPU infrastructure. It is part of the Databricks AI Runtime and is used to run end-to-end workloads defined in a YAML configuration file.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

The `air` CLI enables users to launch multi-GPU and multi-node training jobs directly from the command line. Workloads are defined using a `train.yaml` file and submitted with `air run -f train.yaml`. The tool is designed for common distributed-training patterns on H100 GPUs, including large language model fine-tuning and distributed data-parallel training.^[ai-runtime-cli-examples-databricks-on-aws.md]

Before submitting a run, it is recommended to review the quickstart guide for the air CLI.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Key Features

- **Multi-node orchestration:** Submit jobs that span multiple GPU nodes (e.g., 2 nodes with 8 H100 GPUs each).
- **YAML-based configuration:** Workloads are defined declaratively in a `train.yaml` file, making configuration reproducible and version-controllable.
- **Integration with MLflow and Unity Catalog:** Training runs can log metrics to [MLflow](/concepts/mlflow.md) and save checkpoints to a Unity Catalog volume.
- **Support for popular frameworks:** Works with `torchrun`, PyTorch [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), and [Ray Train](/concepts/ray-train-resource-allocation.md) (`TorchTrainer`).

## Usage

The basic command to submit a workload is:

```bash
air run -f train.yaml
```

where `train.yaml` specifies the launcher script, training code, GPU resources, and any other configuration needed.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Examples

The documentation provides two complete, end-to-end workloads as examples:

- **Multi-node LLM fine-tuning with FSDP:** Supervised fine-tuning of Llama-3.1-8B across 16 H100 GPUs (2 nodes) using `torchrun` and PyTorch Fully Sharded Data Parallel (FSDP). The job logs to MLflow and checkpoints to a Unity Catalog volume.^[ai-runtime-cli-examples-databricks-on-aws.md]
- **Distributed training with Ray Train:** Distributed data-parallel fine-tuning with Ray Train's `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU.^[ai-runtime-cli-examples-databricks-on-aws.md]

These examples are available at the [Examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/) page.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The environment providing the `air` CLI and preconfigured libraries for GPU workloads.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient parallelism strategy used in multi-node training.
- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed training framework supported by the `air` CLI.
- torchrun – PyTorch launcher used in workload scripts.
- H100 GPU Support on Databricks – The GPU hardware targeted by these workloads.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging metrics and parameters from training runs.
- [Unity Catalog](/concepts/unity-catalog.md) – Governed storage for checkpoints and data.

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

</answer>

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
