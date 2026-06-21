---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 165e7f99a45472da77ce63e8eefbc17726ebc812330fd750bded0a4b69780099
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-multi-gpu-fine-tuning-pipeline
    - SMFP
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Single-Node Multi-GPU Fine-tuning Pipeline
description: A complete reference pattern for fine-tuning large language models (like Qwen2.5-3B) using Ray Train on a single node with 8 H100 GPUs, covering Ray cluster setup, DDP training, and metric logging.
tags:
  - fine-tuning
  - llm
  - ray
  - databricks
timestamp: "2026-06-18T15:34:20.606Z"
---

# Single-Node Multi-GPU Fine-tuning Pipeline

A **Single-Node Multi-GPU Fine-tuning Pipeline** is a distributed training pattern that uses all GPUs within a single compute node to fine-tune a model in a data-parallel fashion. This approach is ideal for models that fit within the combined memory of the node’s GPUs but are too large for one GPU, or when faster training is desired by splitting the workload across multiple accelerators on the same node.

## Overview

In this pattern, a cluster of GPUs on one machine (e.g. 8 × H100) is treated as a local distributed system. A framework such as [Ray Train](/concepts/ray-train-resource-allocation.md) launches one worker process per GPU, wraps the model in [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), and shards the dataset across workers automatically. Metrics from all workers are aggregated and typically logged to [MLflow](/concepts/mlflow.md) for experiment tracking. ^[distributed-training-with-ray-train-databricks-on-aws.md]  

The pipeline avoids inter-node networking overhead, making communication (e.g. gradient all-reduce) extremely fast. It also simplifies cluster setup because only a single node needs to be provisioned and orchestrated. The source material demonstrates this pattern using a single node with 8 H100 GPUs, a Ray cluster started by a bootstrap script, and the `TorchTrainer` API. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Key Components

### Ray Train and TorchTrainer

[Ray Train](/concepts/ray-train-resource-allocation.md) provides the `TorchTrainer` abstraction, which orchestrates distributed training. The user defines a `train_func` that runs on every worker. The trainer handles:

- Worker placement: one worker per GPU on the node.
- Model distribution via `prepare_model()` – wraps the model in DDP and moves it to the worker’s device.
- Data loading via `prepare_data_loader()` – injects a DistributedSampler to ensure each worker sees a unique subset of the data.
- Metric aggregation: workers report metrics with `ray.train.report()`; the trainer aggregates them across workers. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Single-Node Compute Configuration

The workload YAML requests a node with a specific number of GPUs (e.g. `GPU_8xH100`). A bootstrap script inside the YAML `command` starts a Ray head on the node using all GPUs, runs the driver script, and stops the cluster after training. The same command can also handle multiple nodes when scaling out, but for single-node use only the head branch executes. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### MLflow Integration

MLflow logging is configured automatically by the AI Runtime environment. The driver script checks for the `MLFLOW_RUN_ID` environment variable (injected by the runtime) and logs hyperparameters and per-step training loss. The results appear in the [MLflow Experiment](/concepts/mlflow-experiment.md) named in the workload YAML. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Example Workflow

1. **Write the workload YAML** – Defines the compute (accelerator type, count), dependencies (Ray, transformers, datasets, etc.), and the command to start Ray and run the training script.
2. **Write the training script** – Imports the model (e.g. Qwen2.5-3B), loads a dataset (e.g. Alpaca), defines `train_func`, and configures `TorchTrainer` with `ScalingConfig(num_workers=total_gpus, use_gpu=True)`.
3. **Submit the run** – Using the `air` CLI: `air run -f train.yaml --watch`.
4. **Inspect results** – View logs with `air logs <run-id>` and metrics in the MLflow UI.

The source material uses a public Hugging Face model so no authentication token is required. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## When to Use

- The model and optimizer fit comfortably across the GPUs on a single node.
- Training speed is limited by single-GPU throughput and you have access to a multi-GPU node.
- You want to avoid the complexity of multi-node networking and setup.

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The underlying parallelism strategy used by `prepare_model`.
- [Multi-Node Multi-GPU Fine-tuning](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) – Scaling beyond one node, often using [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md).
- [Ray Train](/concepts/ray-train-resource-allocation.md) – The framework used to manage distributed workers.
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) – The specific Ray Train API for PyTorch workloads.
- ScalingConfig – Configuration for number of workers and GPU usage.
- [MLflow Tracking] – Logging and experiment management.
- [AI Runtime CLI] – Command-line tool for submitting workloads on Databricks.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
