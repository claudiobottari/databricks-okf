---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4dad7505370c882dfe695ef7111b595aa6206a2d47af12583f3aebfcb3e915bc
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-data-parallel-fine-tuning-of-llms-with-ray-train
    - DDFOLWRT
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Distributed data-parallel fine-tuning of LLMs with Ray Train
description: End-to-end pattern for fine-tuning a large language model (e.g., Qwen2.5-3B) using Ray Train's TorchTrainer across multiple GPUs with DDP, covering model loading, dataset preparation, training loop, and metric reporting.
tags:
  - llm
  - fine-tuning
  - distributed-training
  - ray
timestamp: "2026-06-18T12:08:46.353Z"
---

# Distributed data-parallel fine-tuning of LLMs with Ray Train

**Distributed data-parallel fine-tuning of LLMs with Ray Train** refers to the practice of using [Ray Train](https://docs.ray.io/en/latest/train/train.html) to scale the fine-tuning of a large language model (LLM) across multiple GPUs by wrapping the model in PyTorch Distributed Data Parallel (DDP) and sharding the dataset automatically across workers. On Databricks, this is typically run through the AI Runtime CLI (`air`) on GPU-backed compute nodes. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

The workload starts a Ray cluster on a single node (or multiple nodes), then the Ray Train driver launches one worker per GPU. Each worker runs a training function (`train_func`) that builds the model, wraps it with DDP via `ray.train.torch.prepare_model`, creates a `DataLoader` and wraps it with `prepare_data_loader` to inject a distributed sampler, and executes the training loop. Metrics are reported via `ray.train.report` and logged to an [MLflow](/concepts/mlflow.md) experiment. ^[distributed-training-with-ray-train-databricks-on-aws.md]

A concrete example fine-tunes [Qwen2.5-3B](https://huggingface.co/Qwen/Qwen2.5-3B) on 8 H100 GPUs using a single node. The model is publicly accessible and does not require a Hugging Face token. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Prerequisites

- The `air` CLI installed and authenticated. See [AI Runtime CLI installation](/concepts/ai-runtime-cli-installation-via-uv.md). ^[distributed-training-with-ray-train-databricks-on-aws.md]
- Access to GPU compute resources (e.g., `GPU_8xH100`).
- A project directory containing a workload YAML file and a Ray Train driver script.

## Workflow

### 1. Project layout

Create a directory with the following files:

```
ray_train_distributed/
├── train.yaml           # Air workload configuration
└── train_ray.py         # Ray Train TorchTrainer driver + per-worker training
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### 2. Write the workload YAML

The YAML file declares the compute requirements, environment dependencies, inline command, and code source. Key sections:

- `compute`: requests 8 GPUs of type `GPU_8xH100` on a single node.
- `environment`: specifies Python packages (`ray[default,train]`, `transformers`, `datasets`, `huggingface_hub`, and a newer `fsspec` to avoid download failures).
- `command`: starts a Ray head with all GPUs on node 0, runs `train_ray.py`, then stops Ray. Also includes a branch for worker nodes that join the head (allowing the same YAML to scale to multiple nodes).

An example `train.yaml` is provided in the source. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### 3. Define the Ray Train driver

The `train_ray.py` script contains a `train_func` executed on every worker and a `main` function that initialises the `TorchTrainer`. Core steps in `train_func`:

1. Load a tokenizer and model (e.g., `AutoModelForCausalLM.from_pretrained`) with `torch.bfloat16`.
2. Wrap the model with `prepare_model(model)` – this moves the model to the worker’s GPU and wraps it in DDP.
3. Build a dataset (e.g., `tatsu-lab/alpaca`), tokenise it, and create a `DataLoader`.
4. Wrap the dataloader with `prepare_data_loader(loader)` – this injects a `DistributedSampler` and moves each batch to the GPU.
5. Run the training loop, calling `ray.train.report({"loss": ..., "step": ...})` after each step.
6. Log metrics to [MLflow](/concepts/mlflow.md) if the environment variable `MLFLOW_RUN_ID` is set (automatically injected by the AI Runtime).

The `main` function calls `ray.init(address="auto")`, discovers the total number of GPUs in the cluster, and configures a `TorchTrainer` with a `ScalingConfig` that sets `num_workers` to the GPU count and `use_gpu=True`. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### 4. Submit the run

Use the `air` CLI:

```bash
air run -f train.yaml --dry-run   # preview without execution
air run -f train.yaml --watch     # run and watch logs
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### 5. Inspect the run

```bash
air get run <run-id>
air logs <run-id>
```

Logs stream from a single node because the Ray head and driver both run on node 0. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### 6. View results

Metrics reported with `ray.train.report` and logged to MLflow appear in the experiment named in `experiment_name`, accessible through the workspace MLflow UI. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Key components

| Component | Role |
|-----------|------|
| [Ray Train](/concepts/ray-train-resource-allocation.md) | Distributed training framework providing `TorchTrainer`, `ScalingConfig`, and the reporting API. |
| [TorchTrainer](/concepts/ray-train-torchtrainer.md) | Launches `train_func` across multiple workers with automatic resource placement. |
| `prepare_model` | Moves the model to the worker’s GPU and wraps it in PyTorch DDP. |
| `prepare_data_loader` | Injects a `DistributedSampler` and ensures batches are placed on the correct device. |
| `ray.train.report` | Aggregates metrics across workers and makes them available to the trainer. |
| [MLflow](/concepts/mlflow.md) | Tracks hyperparameters, loss metrics, and run metadata. |

## Full training script

The complete `train_ray.py` script is provided in the source document for copy-paste. It includes dataset formatting, model loading, training loop, and MLflow integration. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Next steps

- [Multi-node LLM fine-tuning with FSDP](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) – scaling to multiple nodes with Fully Sharded Data Parallel.
- Workload YAML reference – full specification of the `air` configuration format.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
