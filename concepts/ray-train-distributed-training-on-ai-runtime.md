---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 788427d52bb6ccd6b531b4eed4f35f7250eba6c139cf6e900ac35e705fccbfb6
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-train-distributed-training-on-ai-runtime
    - RTDTOAR
    - Ray Train distributed example
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Ray Train distributed training on AI Runtime
description: Distributed data-parallel fine-tuning using Ray Train's TorchTrainer across multiple H100 GPUs on a single node
tags:
  - ray
  - distributed-training
  - databricks
timestamp: "2026-06-19T17:30:34.131Z"
---

## Ray Train Distributed Training on AI Runtime

**Ray Train distributed training on AI Runtime** refers to the use of the Ray Train framework with the `TorchTrainer` class to perform distributed data‑parallel fine‑tuning on Databricks AI Runtime. This pattern is available as a complete, end‑to‑end CLI example that can be submitted via the `air run -f train.yaml` command. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Overview

The example demonstrates distributed data‑parallel fine‑tuning across **8 H100 GPUs** on a **single node**, with one Ray Train worker per GPU. It uses Ray Train’s `TorchTrainer` to orchestrate the training loop, leveraging the native distributed capabilities of PyTorch under the hood. This approach is suitable for medium‑sized models that can fit on a single node when sharded across multiple GPUs, or for data‑parallel scaling of training workloads. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### How It Works

- Workers are launched inside the AI Runtime environment using `air run -f train.yaml`, which references a launcher script and the training code.
- Each of the 8 workers corresponds to one H100 GPU, using Ray’s placement group and resource scheduling to ensure a 1:1 mapping.
- `TorchTrainer` wraps the user‑defined `train_func` and handles distributed communication (via NCCL by default), checkpointing, and logging.

The full source code and configuration files are part of the AI Runtime CLI examples library and serve as a reference for users who want to bring their own PyTorch training code into a distributed ray‑based framework. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### When to Use Ray Train

Consider Ray Train when you:
- Need a flexible, Python‑native distributed training framework that works with PyTorch (and other frameworks via Ray `Trainer` backends).
- Want to integrate with the broader Ray ecosystem (Ray Data for data preprocessing, Ray Tune for hyperparameter tuning, Ray Serve for serving).
- Prefer a worker‑based abstraction over the lower‑level `torchrun` or `torch.distributed` launchers.

For workloads that exceed a single node or require memory‑efficient sharding, AI Runtime also provides a [Multi‑node LLM fine‑tuning with FSDP](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) example that pairs `torchrun` with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) – The distributed training library used in this example.
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) – Ray Train’s API for PyTorch training.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command‑line tool used to submit workloads.
- H100 GPU Support on Databricks – Hardware infrastructure for the 8xH100 single‑node configuration.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – A common parallelism strategy that Ray Train can use under the hood.
- [Multi‑node LLM fine‑tuning with FSDP](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) – An alternative distributed training pattern for larger models.

### Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
