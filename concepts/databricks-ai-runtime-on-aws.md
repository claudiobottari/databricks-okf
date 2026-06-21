---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2897938c64d0eed526ef28f256644fd23894d321285e9870753062a17a7dea78
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-on-aws
    - DAROA
    - supported Databricks Runtime versions
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Databricks AI Runtime on AWS
description: A managed AI runtime environment on AWS for running distributed machine learning workloads, including LLM fine-tuning and GPU-based training.
tags:
  - databricks
  - AWS
  - machine-learning
timestamp: "2026-06-19T08:56:21.319Z"
---

# Databricks AI Runtime on AWS

**Databricks AI Runtime on AWS** is a runtime environment purpose-built for distributed training and fine-tuning of large-scale machine learning models on AWS infrastructure. It includes a command-line interface (CLI) called `air` that enables users to submit end-to-end workloads with a single command (`air run -f train.yaml`). ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

The AI Runtime is designed to simplify the orchestration of distributed training jobs on GPU clusters. It integrates with core Databricks services such as [MLflow](/concepts/mlflow.md) for experiment tracking and [Unity Catalog](/concepts/unity-catalog.md) for checkpoint storage, and supports popular distributed training frameworks. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Capabilities

### Multi-Node LLM Fine-Tuning with FSDP

The AI Runtime supports multi-node distributed training using [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) with `torchrun`. An example workload fine-tunes Llama-3.1-8B across 16 H100 GPUs (2 nodes of 8 GPUs each). The job logs metrics to MLflow and saves checkpoints to a Unity Catalog volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Distributed Training with Ray Train

The AI Runtime also integrates with [Ray Train](/concepts/ray-train-resource-allocation.md) for distributed data-parallel training. An example uses Ray Train's `TorchTrainer` to fine-tune a model across 8 H100 GPUs on a single node, with one worker per GPU. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- AI Runtime CLI quickstart – Getting started with the `air` CLI
- [Multi-node LLM SFT example](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) – Detailed walkthrough of FSDP fine-tuning
- [Ray Train distributed example](/concepts/ray-train-distributed-training-on-ai-runtime.md) – Detailed walkthrough of Ray Train usage
- H100 GPU Support on Databricks – Infrastructure for GPU-based training
- Unity Catalog Volumes – Checkpoint and artifact storage
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment logging and monitoring

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
