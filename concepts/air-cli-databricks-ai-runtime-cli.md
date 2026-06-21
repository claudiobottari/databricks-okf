---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0d23b605463dac0a40043fb3f203d09d28dfed157ae67e0a90d9aaa73f15318
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-cli-databricks-ai-runtime-cli
    - AC(ARC
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: air CLI (Databricks AI Runtime CLI)
description: Command-line tool for submitting and managing distributed AI/ML training workloads on Databricks infrastructure
tags:
  - databricks
  - command-line-tool
  - machine-learning
  - distributed-training
timestamp: "2026-06-18T14:21:49.578Z"
---

# air CLI (Databricks AI Runtime CLI)

The **`air` CLI** is a command-line tool for submitting distributed training workloads on Databricks AI Runtime. It enables users to run end-to-end training jobs defined in a YAML configuration file, targeting clusters with H100 GPUs. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Usage

The primary command is `air run -f <workload.yaml>`, where the YAML file specifies the training configuration including the launcher script, training code, compute resources, and any dependencies. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Examples

The following complete workloads demonstrate real distributed‑training patterns:

- **Multi‑node LLM fine‑tuning with FSDP** – Supervised fine‑tuning of Llama‑3.1‑8B across 16 H100 GPUs (2 nodes) using `torchrun` and [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/fsdp-fully-sharded-data-parallel.md). The job logs metrics to [MLflow](/concepts/mlflow.md) and saves checkpoints to a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]
- **Distributed training with Ray Train** – Distributed data‑parallel fine‑tuning with [Ray Train](/concepts/ray-train-resource-allocation.md)’s `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Getting started

Before submitting a run, consult the [quickstart](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart) guide, which covers prerequisites and the first `air run` workflow. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- FSDP training
- [Ray Train](/concepts/ray-train-resource-allocation.md)
- Unity Catalog volumes
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- torchrun
- H100 GPU

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
