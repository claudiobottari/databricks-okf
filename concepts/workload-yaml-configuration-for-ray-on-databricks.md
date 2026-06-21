---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 49320644a6613b78c200df08d3de9d3893b267cfb71682b9ac7952df9ef717eb
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workload-yaml-configuration-for-ray-on-databricks
    - WYCFROD
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Workload YAML Configuration for Ray on Databricks
description: YAML configuration format for the Databricks AI Runtime CLI that defines compute resources, dependencies, code sources, and commands for distributed Ray training workloads.
tags:
  - databricks
  - configuration
  - ray
timestamp: "2026-06-19T10:19:37.604Z"
---

# [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) for Ray on Databricks

**Workload YAML Configuration for Ray on Databricks** refers to the YAML file used with the AI Runtime CLI (`air`) to define and submit a distributed Ray workload — such as fine-tuning a language model with [Ray Train](/concepts/ray-train-resource-allocation.md) — to a Databricks compute cluster. The YAML file specifies the environment, compute resources, source code, startup command, and runtime behavior for the workload.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

A workload YAML file serves as the single source of truth for a Ray training run on Databricks. It declares inline dependencies, GPU node requirements, how to start a Ray cluster on the node(s), and the Python script that drives the Ray Train job. The AI Runtime CLI reads this YAML, provisions the requested compute, uploads the code, and executes the defined command. This approach avoids the need for separate dependency files or launcher scripts.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Prerequisites

Before using a workload YAML for Ray on Databricks, you must have the `air` CLI installed and authenticated. See [AI Runtime CLI installation](/concepts/ai-runtime-cli-installation-via-uv.md) for setup instructions.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Key YAML Fields

The following table summarizes the main fields used in a workload YAML for Ray Train. All fields are under the root of the YAML document.

| Field | Description | Required |
|---|---|---|
| `experiment_name` | Name of the [MLflow Experiment](/concepts/mlflow-experiment.md) where metrics are logged. | No (but recommended) |
| `environment` | Specifies the AI Runtime client image version and a list of Python dependencies (inline). | Yes |
| `environment.version` | The AI Runtime version (e.g., `'4'`). | Yes |
| `environment.dependencies` | List of `pip` packages to install (e.g., `ray[default,train]>=2.30`). | Yes |
| `compute` | Defines the node type and accelerator count. | Yes |
| `compute.num_accelerators` | Number of GPUs per node (e.g., `8` for an 8‑GPU node). | Yes |
| `compute.accelerator_type` | The GPU instance type (e.g., `GPU_8xH100`). | Yes |
| `code_source` | How to upload the project code. Use `type: snapshot` with a `root_path` pointing to the local directory. | Yes |
| `code_source.snapshot.root_path` | Local directory path that contains the Python scripts and other files. | Yes |
| `command` | A shell command that runs on the provisioned node(s). Typically starts the Ray head, executes the training script, then stops Ray. | Yes |
| `max_retries` | Number of retries on failure (e.g., `0` for no retry). | Yes |
| `timeout_minutes` | Maximum runtime before the job is killed (e.g., `90`). | Yes |
| `env_variables` | Environment variables to set on the node (e.g., `NCCL_SOCKET_IFNAME: eth0`). | No |

^[distributed-training-with-ray-train-databricks-on-aws.md]

## The `command` Field in Detail

The `command` field is the core of a Ray workload YAML. It must start a Ray cluster on the node and then launch your Ray Train driver script. The source material shows a multi‑purpose command that handles both the head node and worker nodes:^[distributed-training-with-ray-train-databricks-on-aws.md]

- **Head node** (`NODE_RANK=0`): Starts a Ray head process with all GPUs (`--num-gpus=$GPUS_PER_NODE`), runs the training script (e.g., `python train_ray.py`), and stops Ray when training finishes.
- **Worker nodes** (any other rank): Connects to the head node at `$MASTER_ADDR:$RAY_HEAD_PORT` and starts a Ray worker that blocks. This branching makes the same YAML work for both single‑node and multi‑node runs.

The example command also includes retry logic for worker node connections.

## Environment and Dependencies

Inline dependencies are declared under `environment.dependencies`. The list should include at least:

- `ray[default,train]` with a minimum version (e.g., `>=2.30`) to provide Ray Core and Ray Train.
- `transformers`, `datasets`, `huggingface_hub` for model and dataset loading.
- Additional pins as needed — for example, the base image may ship an old `fsspec` version that breaks `huggingface_hub`, so pinning `fsspec>=2024.6.1` is required.^[distributed-training-with-ray-train-databricks-on-aws.md]

The `environment.version` specified controls the base Docker image used for the compute.

## Compute Configuration

For GPU‑based Ray Train jobs, set `compute.num_accelerators` to the number of GPUs per node. The source example uses `8` for a single `GPU_8xH100` node. When using multiple nodes, the same configuration applies to each node. Ray Train automatically detects the cluster resources and launches one worker per GPU.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Code Source

The `code_source` field with `type: snapshot` and `root_path: .` uploads the entire current directory to the Databricks cluster. The `command` can reference the uploaded files via the `$CODE_SOURCE_PATH` environment variable, which is set automatically by the AI Runtime. This eliminates the need for manual file syncing.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Full Example YAML

The following is a complete example (adapted from the source) that fine‑tunes a 3B‑parameter model on a single 8×H100 node:^[distributed-training-with-ray-train-databricks-on-aws.md]

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

## Running the Workload

Submit the workload using the `air` CLI:^[distributed-training-with-ray-train-databricks-on-aws.md]

```bash
# Dry-run to validate the YAML
air run -f train.yaml --dry-run

# Submit and watch logs
air run -f train.yaml --watch
```

After submission, you can inspect the run and retrieve logs:^[distributed-training-with-ray-train-databricks-on-aws.md]

```bash
air get run <run-id>
air logs <run-id>
```

## Best Practices

- **Pin dependency versions** to avoid conflicts with the base image. The source demonstrates pinning `fsspec` because the base image ships an incompatible version.^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Set `max_retries: 0`** for training runs when retries could produce duplicate results; accept failure and investigate instead.^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Use `env_variables`** to configure NCCL networking (e.g., `NCCL_SOCKET_IFNAME: eth0`) to match your cluster’s network interface.^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Include the multi‑node branch** in the `command` even for single‑node jobs — it makes scaling to multiple nodes a matter of changing the compute configuration only.^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Keep training scripts stateless** so they can be replayed or distributed across nodes without modification. The script should use `ray.train.report()` for metric aggregation and MLflow logging.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The tool that interprets workload YAML files.
- [Ray Train](/concepts/ray-train-resource-allocation.md) — The distributed training framework used with this configuration.
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) — The Ray Train trainer class used in the training script.
- FSDP Training on Databricks — An alternative distributed strategy for very large models.
- MLflow Integration with Ray — How metrics are logged from Ray Train workers to MLflow.
- Multi‑node LLM Fine‑tuning — Scaling the YAML to multiple nodes.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
