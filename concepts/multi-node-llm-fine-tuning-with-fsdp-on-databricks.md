---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ed8f3ea095dd754d814a20f44b785b095c0f4f55359efa16b7a76c383a2bfd9
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-node-llm-fine-tuning-with-fsdp-on-databricks
    - MLFWFOD
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Multi-node LLM fine-tuning with FSDP on Databricks
description: Distributed supervised fine-tuning of Llama-3.1-8B across 16 H100 GPUs (2 nodes) using torchrun and PyTorch Fully Sharded Data Parallel (FSDP), with MLflow logging and Unity Catalog checkpointing.
tags:
  - distributed-training
  - LLM
  - FSDP
  - databricks
timestamp: "2026-06-19T08:56:13.686Z"
---

# Multi-node LLM fine-tuning with FSDP on Databricks

**Multi-node LLM fine-tuning with FSDP on Databricks** is a supervised fine-tuning pattern for large language models (LLMs) that uses PyTorch [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) across multiple compute nodes. This approach enables training models that exceed the memory capacity of a single GPU by distributing model parameters, gradients, and optimizer states across many GPUs on multiple nodes. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

The pattern enables supervised fine-tuning of models such as Llama-3.1-8B across 16 H100 GPUs distributed across 2 nodes. The training uses `torchrun` (PyTorch's elastic launch utility) and FSDP for distributed training. Experiment tracking logs metrics to [MLflow](/concepts/mlflow.md), and model checkpoints are saved to a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Workload Architecture

A multi-node FSDP fine-tuning workload on Databricks consists of three components:

1. **Workload YAML** (`train.yaml`) – Defines the compute resources, launcher command, and environment configuration submitted via the `air run -f train.yaml` command from the `air` CLI. ^[ai-runtime-cli-examples-databricks-on-aws.md]
2. **Launcher script** – Sets up the distributed training environment and invokes `torchrun` with appropriate node and GPU arguments. ^[ai-runtime-cli-examples-databricks-on-aws.md]
3. **Training code** – The Python script that loads the base model, applies FSDP wrapping, configures the optimizer, runs the training loop, logs metrics to MLflow, and saves checkpoints. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Key Components

### PyTorch FSDP

Fully Sharded Data Parallel shards model parameters, gradients, and optimizer states across all available GPUs. This is essential for models that cannot fit in a single GPU's memory, such as Llama-3.1-8B. FSDP overlaps communication with computation to maintain training throughput while reducing per-GPU memory footprint. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### `torchrun`

PyTorch's elastic launch utility handles multi-node process initialization, including world size computation, rank assignment, and node discovery. When running across 2 nodes with 8 H100 GPUs each, `torchrun` automatically configures 16 processes with appropriate ranks. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### MLflow Integration

Training metrics are logged to [MLflow](/concepts/mlflow.md) experiments, providing a central record of loss curves, learning rates, and hyperparameters across runs. This enables experiment comparison and reproducibility. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Unity Catalog Checkpoints

Model checkpoints are saved to a [Unity Catalog](/concepts/unity-catalog.md) volume, providing governed, versioned storage that integrates with Databricks' data governance framework. Checkpoints can later be loaded for inference or continued training. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Usage

To submit a multi-node FSDP fine-tuning workload, use the `air CLI` with a workload YAML file:

```bash
air run -f train.yaml
```

The workload definition in `train.yaml` specifies:
- The number of nodes and GPU types (e.g., 2 nodes of g5.48xlarge with 8 H100 GPUs each)
- The launcher command invoking `torchrun`
- Environment variables for distributed training configuration
- The training script and its arguments

## Prerequisites

- **AI Runtime** – The workload runs on Databricks AI Runtime, which includes PyTorch and dependencies optimized for distributed training. ^[ai-runtime-cli-examples-databricks-on-aws.md]
- **GPU compute** – Access to multi-node GPU clusters (e.g., 2 nodes with 8 H100 GPUs each). See [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) for GPU availability considerations. ^[ai-runtime-cli-examples-databricks-on-aws.md]
- **Unity Catalog** – A volume for storing checkpoints must be configured. ^[ai-runtime-cli-examples-databricks-on-aws.md]
- **MLflow experiment** – Required for logging training metrics. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – The distributed training strategy used
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Alternative for models fitting in single GPU memory
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – Scaling guidance for larger models
- [DeepSpeed](/concepts/deepspeed.md) – Alternative distributed training framework with advanced memory optimizations
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line tool for submitting training workloads
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime with GPU and deep learning libraries
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) – General guidance for deep learning workflows

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
