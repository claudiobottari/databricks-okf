---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23af0d1873ceecaba209c4e5c369972a953fdd6e34e56d039f876c979d80a617
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - training-workload-yaml-format
    - TWYF
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Training workload YAML format
description: Configuration file format (train.yaml) that defines the distributed training job parameters for the AI Runtime CLI
tags:
  - configuration
  - yaml
  - databricks
timestamp: "2026-06-19T17:30:28.404Z"
---

# Training workload YAML format

The **Training workload YAML format** is the configuration file format used by the `air` CLI to define and submit distributed training workloads on Databricks AI Runtime. These YAML files are passed to `air run -f train.yaml` and specify the training job's compute resources, launcher script, and training code. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

Training workload YAML files serve as the primary interface for running end-to-end distributed training jobs from the command line. They encapsulate all configuration needed to launch workloads on H100 GPU clusters, including resource requirements, launcher commands, and script paths. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Structure

A training workload YAML file typically contains:

- **Compute configuration**: The number of nodes, GPUs per node, and GPU type
- **Launcher settings**: The distributed launcher to use (e.g., `torchrun` or Ray Train's `TorchTrainer`)
- **Script references**: Paths to the training script and any supporting code
- **Dependencies**: Libraries and runtime requirements
- **Output configuration**: Logging destinations like [MLflow](/concepts/mlflow.md) and checkpoint locations like [Unity Catalog](/concepts/unity-catalog.md) volumes

^[ai-runtime-cli-examples-databricks-on-aws.md]

## Example Workloads

The following examples demonstrate complete YAML-based training workloads:

- **Multi-node LLM fine-tuning with FSDP**: Fine-tuning Llama-3.1-8B across 16 H100 GPUs (2 nodes, 8 GPUs each) using `torchrun` and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). Logs to MLflow and checkpoints to a Unity Catalog volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]
- **Distributed training with Ray Train**: Data-parallel fine-tuning with Ray Train's `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Usage

To submit a training workload, run the `air` CLI with the YAML file:

```bash
air run -f train.yaml
```

This launches the defined training job on the specified GPU resources using the configured launcher and training script. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for submitting training workloads
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient parallelism used in multi-node YAML workloads
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Another parallelism strategy compatible with YAML workloads
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Common resource configuration for YAML-based training
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Scaling across multiple nodes in a YAML workload
- H100 GPU Support on Databricks — GPU infrastructure used by YAML workloads

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
