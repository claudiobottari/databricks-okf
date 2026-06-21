---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9b5dcc8f145ab3ce0a3ba237b7cb3f4de55aad02991901ea7fb4e22b5cb4cb3
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-run-workflow
    - ARW
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: air run workflow
description: Mechanism to submit distributed training jobs by specifying a YAML configuration file via the `air run -f train.yaml` command
tags:
  - cli
  - workflow
  - databricks
timestamp: "2026-06-19T17:30:29.130Z"
---

# `air run` Workflow

The **`air run` workflow** describes the process of submitting a distributed training job using the [`air` CLI](ai-runtime-cli-databricks-on-aws) on Databricks. This workflow is designed for end‑to‑end training on [H100 GPUs](h100-gpu-support-on-databricks) and is the primary way to launch jobs defined in a YAML configuration file. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

A typical `air run` workflow consists of three core artifacts bundled together:

- **Workload YAML** – A configuration file (commonly named `train.yaml`) that defines the job parameters, such as the number of GPUs, launcher command, and environment settings.
- **Launcher script** – A shell script or Python script that orchestrates the training process (e.g., invoking `torchrun` or `ray train`).
- **Training code** – The actual model‑training logic (e.g., a Python module implementing the forward/backward pass and checkpointing).

You submit the job by running `air run -f train.yaml` from the command line. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Example Patterns

The Databricks documentation provides two complete, end‑to‑end examples that illustrate the `air run` workflow:

### Multi‑Node LLM Fine‑Tuning with FSDP

- **Objective:** Supervised fine‑tuning of Llama‑3.1‑8B across 16 H100 GPUs (2 nodes).
- **Launcher:** Uses `torchrun` and PyTorch [Fully Sharded Data Parallel (FSDP)](fully-sharded-data-parallel-fsdp-training-databricks-on-aws).
- **Outputs:** Logs to [MLflow](mlflow-tracking-databricks) and checkpoints to a [Unity Catalog volume](unity-catalog-volumes-databricks). ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Distributed Training with Ray Train

- **Objective:** Data‑parallel fine‑training with Ray Train’s `TorchTrainer` across 8 H100 GPUs on a single node.
- **Launcher:** Uses Ray Train, with one worker per GPU.
- **Key feature:** Leverages the [Ray](ray-on-databricks) distributed computing framework. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Getting Started

If you have not yet submitted a run, refer to the [AI Runtime CLI quickstart](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart). The quickstart explains the prerequisites and walks through the first `air run` invocation. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command‑line interface that exposes the `air run` command.
- FSDP Training – Memory‑sharded distributed training used in the multi‑node example.
- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed training library used in the single‑node example.
- H100 GPU Support on Databricks – The accelerator that powers both example patterns.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) – Broader context for multi‑GPU workflows.

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
