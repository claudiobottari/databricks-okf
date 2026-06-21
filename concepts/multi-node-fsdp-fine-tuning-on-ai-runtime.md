---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 708edb62c613802fff8b54d4bde62aea72945cb5cdf929469c5a7a85a4d332af
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-node-fsdp-fine-tuning-on-ai-runtime
    - MFFOAR
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Multi-node FSDP fine-tuning on AI Runtime
description: Supervised fine-tuning of LLMs (e.g., Llama-3.1-8B) across multiple nodes using PyTorch Fully Sharded Data Parallel on H100 GPUs
tags:
  - fine-tuning
  - fsdp
  - llm
  - distributed-training
timestamp: "2026-06-19T17:30:58.539Z"
---

# Multi-node FSDP fine-tuning on AI Runtime

**Multi-node FSDP fine-tuning on AI Runtime** refers to the supervised fine-tuning of large language models across multiple compute nodes using PyTorch's Fully Sharded Data Parallel (FSDP) on the Databricks AI Runtime platform. This approach enables training models that exceed the memory capacity of a single GPU by sharding model parameters, gradients, and optimizer states across GPUs distributed across multiple nodes. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

The typical configuration for multi-node FSDP fine-tuning on AI Runtime uses 2 nodes equipped with H100 GPUs, providing a total of 16 GPUs for distributed training. This setup is commonly used for supervised fine-tuning of models in the 8 billion parameter range, such as Llama-3.1-8B. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## How It Works

The training job uses `torchrun` for process launching across nodes and PyTorch FSDP for model sharding. Key components include:

- **Workload YAML**: A configuration file (typically `train.yaml`) that defines the compute resources, environment, and entry point for the training job.
- **Launcher script**: A script that sets up the distributed environment and invokes `torchrun` with the appropriate arguments for multi-node execution.
- **Training code**: The actual Python training loop that loads the model, applies FSDP wrapping, and performs the fine-tuning.

^[ai-runtime-cli-examples-databricks-on-aws.md]

## Submission

Training jobs are submitted using the `air` CLI with the following command:

```bash
air run -f train.yaml
```

This command reads the workload YAML file, provisions the requested GPU resources across multiple nodes, and launches the training process. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Integration

Multi-node FSDP fine-tuning on AI Runtime integrates with:

- **MLflow**: Training metrics and model artifacts are logged to MLflow for experiment tracking and model management.
- **Unity Catalog volumes**: Model checkpoints are saved to Unity Catalog volumes for persistence and versioning.

^[ai-runtime-cli-examples-databricks-on-aws.md]

## Prerequisites

Before running a multi-node FSDP fine-tuning job, users should first complete the AI Runtime CLI quickstart guide to understand the basics of submitting runs. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — The sharding strategy used to distribute model state across GPUs.
- [Supervised Fine-Tuning](/concepts/supervised-fine-tuning-sft.md) — The training technique applied to adapt pre-trained models to specific tasks.
- H100 GPU Support on Databricks — The GPU hardware used for multi-node training.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool used to submit and manage training jobs.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concept of training across multiple GPUs and nodes.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and storage for model checkpoints.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment logging and model registry integration.

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
