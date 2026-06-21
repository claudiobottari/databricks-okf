---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4841da197873af81579c4bc9e974668ab1980c7356ba8b144eda9bd197e3bdc
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workload-yaml-configuration-for-distributed-training
    - WYCFDT
    - Spark Configuration for Distributed Training
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Workload YAML configuration for distributed training
description: YAML schema defining experiment name, environment dependencies, compute resources, code source, and inline command for launching distributed ML workloads on Databricks.
tags:
  - databricks
  - configuration
  - distributed-training
timestamp: "2026-06-18T12:08:50.696Z"
---

# [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) for distributed training

**Workload YAML configuration for distributed training** refers to the declarative specification used by the [AI Runtime CLI (air)](/concepts/ai-runtime-cli-air.md)](/ai-runtime-cli) to define and submit distributed training jobs on Databricks. The YAML file describes compute resources, environment dependencies, source code, and the startup command that bootstraps a [Ray](/ray) cluster and launches a distributed training framework such as [Ray Train's TorchTrainer](/torchtrainer). This approach allows data-parallel fine-tuning (e.g., using [Distributed Data Parallel (DDP)](/distributed-data-parallel)) across multiple GPUs without manual cluster management. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

A workload YAML for distributed training typically requests a GPU node (e.g., `GPU_8xH100`), declares Python dependencies inline under `environment`, and specifies a `command` that starts a Ray head node, invokes a Python training script, and stops the cluster. The same YAML can optionally support multi-node scaling by including a worker branch that joins the head. Metrics are logged to [MLflow](/mlflow) via the experiment name provided in the YAML. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Prerequisites

Before using a workload YAML for distributed training, you must have the `air` CLI installed and authenticated. See [Install the AI Runtime CLI](/ai-runtime-cli-installation). ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Project layout

The source project is a directory with the following files:

- `train.yaml` — the [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) (inline dependencies and Ray bootstrap commands)
- `train_ray.py` — the Ray Train driver that uses `TorchTrainer` and per-worker training logic

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Workload YAML structure

The YAML defines the following top-level keys:

| Key | Description |
|-----|-------------|
| `experiment_name` | MLflow experiment name where metrics are logged |
| `environment` | Inline dependencies and the base image version |
| `compute` | Node type and number of accelerators (e.g., `GPU_8xH100`, `num_accelerators: 8`) |
| `code_source` | How to upload the local source (e.g., `type: snapshot`) |
| `command` | The shell command that bootstraps the Ray cluster and runs training |
| `max_retries` | Number of retry attempts (typically 0 for this pattern) |
| `timeout_minutes` | Maximum allowed runtime |
| `env_variables` | Environment variables set on the node (e.g., `NCCL_SOCKET_IFNAME`) |

^[distributed-training-with-ray-train-databricks-on-aws.md]

### `environment` section

Dependencies are declared as a list under `dependencies` and are installed during workload startup. The `version` field specifies the client image version (e.g., `'4'`). Example:

```yaml
environment:
  version: '4'
  dependencies:
    - ray[default,train]>=2.30
    - transformers>=4.45
    - datasets>=3.0
    - huggingface_hub>=0.34
    - fsspec>=2024.6.1   # Required to avoid download issues with newer huggingface_hub
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### `compute` section

Defines the hardware and accelerator configuration. For distributed training, set `num_accelerators` to the number of GPUs per node and `accelerator_type` to the desired node type:

```yaml
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### `command` section

The command is the critical part that starts the Ray cluster and launches the training script. A typical pattern for a single-node multi-GPU run is:

- On node rank 0 (the head): start Ray head with all GPUs, run the Python driver (`python train_ray.py`), then stop Ray.
- On worker nodes (for multi-node scaling): connect to the head and block.

The command uses environment variables like `$CODE_SOURCE_PATH`, `$LOCAL_WORLD_SIZE`, `$NODE_RANK`, and `$MASTER_ADDR`, which are injected by the AI Runtime. The `max_retries: 0` ensures the job fails fast if the command fails.

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

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Running the workload

Submit the workload YAML with the `air run` command:

```bash
air run -f train.yaml --dry-run   # Validate the configuration
air run -f train.yaml --watch     # Submit and stream logs
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Inspecting the run

After submission, use the following commands to inspect the run:

```bash
air get run <run-id>
air logs <run-id>
```

The Ray head and driver both execute on node 0, so logs stream from a single node. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Where results land

Metrics reported with `ray.train.report` and logged via MLflow appear in the MLflow experiment named in `experiment_name`, which can be viewed in the Databricks workspace MLflow UI. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Full training script

The example includes a complete `train_ray.py` that demonstrates:

- Building a dataset from Hugging Face (`tatsu-lab/alpaca`)
- Defining a `train_func` that runs on each worker, using `prepare_model` and `prepare_data_loader` for DDP wrapping and distributed sampling
- Configuring a `TorchTrainer` with `ScalingConfig(num_workers=total_gpus, use_gpu=True)`
- Logging per-step loss to MLflow on rank 0

The full script is available in the source documentation. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Next steps

- [Multi-node LLM fine-tuning with FSDP](/multinode-llm-sft)
- [Workload YAML reference](/workload-yaml-reference)

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
