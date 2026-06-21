---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c22ffe032d461115160f9900d57cc676b0bad8435874f4ae992587474ff42cff
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-air-cli-workload-yaml
    - AR(CWY
    - AI Runtime (AIR) Workloads
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: AI Runtime (air) CLI Workload YAML
description: A YAML configuration format for the Databricks AI Runtime CLI that defines distributed training jobs with compute requirements, environment dependencies, code sources, and inline bootstrap commands.
tags:
  - databricks
  - configuration
  - deployment
timestamp: "2026-06-19T18:38:04.619Z"
---

# AI Runtime (air) CLI Workload YAML

The **AI Runtime (air) CLI Workload YAML** is a configuration file format used to define and submit distributed training and machine learning workloads using the `air` CLI on Databricks. These YAML files specify the compute requirements, environment dependencies, code source, and execution command for a workload that runs on serverless GPU infrastructure.

## Overview

A workload YAML file serves as the primary configuration for `air run` commands, defining all aspects of a distributed training job. The file declares the experiment name, environment version and dependencies, compute resources, code source location, and the command to execute. The `air` CLI reads this configuration and submits the workload to Databricks serverless GPU compute. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Top-Level Fields

### `experiment_name`

Specifies the MLflow experiment name under which metrics and artifacts are logged. This is optional but recommended for organizing runs. When set, metrics reported with `ray.train.report` and logged with MLflow appear in this experiment, viewable in the workspace MLflow UI. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `environment`

Defines the runtime environment for the workload, including the AI Runtime version and Python package dependencies.

```yaml
environment:
  version: '4'
  dependencies:
    - ray[default,train]>=2.30
    - transformers>=4.45
    - datasets>=3.0
    - fsspec>=2024.6.1
```

- `version`: The AI Runtime client image version (e.g., `'4'`).
- `dependencies`: A list of pip-installable Python packages. Dependencies are declared inline, so a separate `requirements.txt` file is not needed.

The base image ships with some packages that may be too old for newer library versions. In the example above, the base image ships `fsspec` 2023.5.0, which is too old for modern `huggingface_hub` and breaks dataset/model downloads, so a newer `fsspec` is pinned. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `compute`

Specifies the GPU resources required for the workload.

```yaml
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
```

- `num_accelerators`: The number of GPUs to request (e.g., 8 for a full node).
- `accelerator_type`: The type of accelerator, such as `GPU_8xH100` for a single node with 8 H100 GPUs.

This configuration requests a single node with 8 H100 80GB GPUs. When using [Ray Train](/concepts/ray-train-resource-allocation.md), one worker is launched per GPU. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `code_source`

Defines how the source code is uploaded to the workload.

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
```

- `type: snapshot`: Uploads the local project directory as a snapshot.
- `root_path`: The root directory of the project relative to the workload YAML file. Using `.` uploads the current directory.

The uploaded code is available at the `$CODE_SOURCE_PATH` environment variable within the command. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `command`

The shell command to execute within the workload environment. This is the main entry point for the training logic.

```yaml
command: |
  cd $CODE_SOURCE_PATH
  RAY_HEAD_PORT=6379
  GPUS_PER_NODE=${LOCAL_WORLD_SIZE:-8}
  if [ "${NODE_RANK:-0}" = "0" ]; then
    echo "NODE_RANK=0: starting Ray head with $GPUS_PER_NODE GPU(s)..."
    ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE" --dashboard-host=0.0.0.0
    python train_ray.py
    ray stop
  else
    echo "NODE_RANK=$NODE_RANK: connecting to Ray head at $MASTER_ADDR:$RAY_HEAD_PORT..."
    for i in $(seq 1 12); do
      if ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT" --num-gpus="$GPUS_PER_NODE" --block 2>/dev/null; then
        break
      fi
      echo "Attempt $i failed, retrying in 5s..."
      sleep 5
    done
  fi
```

Key environment variables available in the command:
- `$CODE_SOURCE_PATH`: Path to the uploaded code.
- `$LOCAL_WORLD_SIZE`: Number of GPUs on the node (usually matches `num_accelerators`).
- `$NODE_RANK`: The rank of this node in a multi-node job (0 for the head node).
- `$MASTER_ADDR`: Address of the head node.

The command typically changes to the code directory (`cd $CODE_SOURCE_PATH`), sets up a distributed computing framework (like Ray), and runs the training script. For single-node jobs, the head node branch starts Ray and runs the driver. The worker branch is included for future multi-node scaling. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `max_retries` and `timeout_minutes`

- `max_retries`: The maximum number of retry attempts on failure (e.g., `0` for no retries).
- `timeout_minutes`: The maximum execution time before the workload is stopped (e.g., `90` minutes). ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `env_variables`

Custom environment variables passed to the workload.

```yaml
env_variables:
  NCCL_SOCKET_IFNAME: eth0
```

These are useful for configuring networking libraries like NCCL for GPU communication. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Example: Complete Workload YAML

```yaml
experiment_name: air-ray-train-distributed
environment:
  version: '4'
  dependencies:
    - ray[default,train]>=2.30
    - transformers>=4.45
    - datasets>=3.0
    - huggingface_hub>=0.34
    - fsspec>=2024.6.1
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
code_source:
  type: snapshot
  snapshot:
    root_path: .
command: |
  cd $CODE_SOURCE_PATH
  RAY_HEAD_PORT=6379
  GPUS_PER_NODE=${LOCAL_WORLD_SIZE:-8}
  if [ "${NODE_RANK:-0}" = "0" ]; then
    echo "NODE_RANK=0: starting Ray head with $GPUS_PER_NODE GPU(s)..."
    ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE" --dashboard-host=0.0.0.0
    python train_ray.py
    ray stop
  else
    echo "NODE_RANK=$NODE_RANK: connecting to Ray head at $MASTER_ADDR:$RAY_HEAD_PORT..."
    for i in $(seq 1 12); do
      if ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT" --num-gpus="$GPUS_PER_NODE" --block 2>/dev/null; then
        break
      fi
      echo "Attempt $i failed, retrying in 5s..."
      sleep 5
    done
  fi
max_retries: 0
timeout_minutes: 90
env_variables:
  NCCL_SOCKET_IFNAME: eth0
```

This example requests an 8xH100 node, starts a Ray cluster, runs a distributed fine-tuning script (`train_ray.py`), and logs metrics to the specified MLflow experiment. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Submitting the Workload

Use the `air run` command to submit the workload:

```bash
# Dry-run to validate the configuration
air run -f train.yaml --dry-run

# Submit and watch logs
air run -f train.yaml --watch
```

The `--dry-run` flag validates the YAML without submitting. The `--watch` flag streams logs to the terminal. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Inspecting Runs

After submission, runs can be inspected:

```bash
air get run <run-id>
air logs <run-id>
```

Logs stream from a single node (the head node where the Ray head and driver run). ^[distributed-training-with-ray-train-databricks-on-aws.md]

## MLflow Integration

The AI Runtime automatically injects `MLFLOW_RUN_ID` and configures the Databricks tracking URI on the node, so logging works without explicit `DATABRICKS_HOST` or `DATABRICKS_TOKEN` environment variables. This allows the training script to call `mlflow.log_metric()` directly without manual configuration. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Related Concepts

- [AI Runtime (air) CLI](/concepts/ai-runtime-cli-air.md) — The command-line interface that processes workload YAML files.
- [Ray Train](/concepts/ray-train-resource-allocation.md) — The distributed training framework commonly used in these workloads.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — The GPU configuration specified in `compute`.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying infrastructure that provisions the requested resources.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The parallelism strategy used by Ray Train within workload YAMLs.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — An alternative parallelism strategy for larger models.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
