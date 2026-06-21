---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d19e31d1a223b7a88834a0b3fee350320d508e65aa4f5bcf3b1f257a8c3ce64c
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-run-f-trainyaml
    - AR-T
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: air run -f train.yaml
description: Primary command pattern for launching distributed training workloads via the Databricks AI Runtime CLI using a YAML workload definition file
tags:
  - databricks
  - workflow
  - yaml
  - distributed-training
timestamp: "2026-06-18T14:21:47.396Z"
---

# `air run -f train.yaml`

The `air run -f train.yaml` command is used to submit complete, end-to-end workloads from the `air` CLI ([AI Runtime CLI](/concepts/ai-runtime-cli.md)). It accepts a YAML file that defines the workload configuration, including the training script, compute resources, and orchestration settings. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Usage

Each workload submitted with `air run -f train.yaml` typically consists of three components:

- A **workload YAML** (e.g., `train.yaml`) specifying parameters such as the launcher command, number of nodes, GPU type, and dependencies.
- A **launcher script** (e.g., `run.sh` or a Python launcher) that sets up the distributed environment and invokes the training code.
- The **training code** itself, often written in PyTorch or other frameworks, that performs the actual model training. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Examples

The documentation provides two reference examples that can be adapted for custom workloads:

1. **Multi-node LLM fine-tuning with FSDP** – Supervised fine-tuning of Llama-3.1-8B across 16 H100 GPUs (2 nodes) using `torchrun` and PyTorch [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). Logs to [MLflow](/concepts/mlflow.md) and checkpoints to a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

2. **Distributed training with Ray Train** – Data‑parallel fine‑tuning with Ray Train’s `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU. ^[ai-runtime-cli-examples-databricks-on-aws.md]

Both examples are fully self‑contained and demonstrate real distributed‑training patterns on H100 GPUs.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Ray Train](/concepts/ray-train-resource-allocation.md)
- torchrun
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [LLM fine-tuning](/concepts/llm-fine-tuning-on-databricks.md)

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
