---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6fc07b20e84e25e8aa449de6d33a27670c9a27982e46e9f70aaa8cd6590f4cb
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-ray-cluster-bootstrap
    - SRCB
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Single-Node Ray Cluster Bootstrap
description: A pattern where the workload command starts a Ray head on the local node with all GPUs, runs the training driver, then stops the cluster — with a fallback branch for multi-node scaling.
tags:
  - ray
  - cluster-management
  - databricks
timestamp: "2026-06-19T18:37:58.802Z"
---

# Single-Node Ray Cluster Bootstrap

**Single-Node Ray Cluster Bootstrap** refers to the initialization procedure that starts a Ray cluster entirely on one multi‑GPU node before executing a [Ray Train](/concepts/ray-train-resource-allocation.md) workload. This bootstrap is typically embedded in the `command` section of an AI Runtime workload YAML, handling the starting (and stopping) of Ray processes so that the training driver can connect and launch distributed workers. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

When running distributed data‑parallel fine‑tuning on a single 8×H100 node, a bootstrap script must start a Ray head process that discovers and manages all GPUs on that node. After the cluster is ready, the Ray Train driver (e.g., `TorchTrainer`) connects to the head, creates one worker per GPU, and the training function runs. Once training finishes, the bootstrap script stops the Ray cluster. This bootstrap logic is part of the workload `command` and does not require a separate launcher script. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Bootstrap Procedure in the Workload YAML

The following YAML excerpt from a `train.yaml` file shows the complete bootstrap command for a single node:

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
    ...
  fi
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

**Key steps for the head (rank 0):**

1. **Change to the code source directory** (`cd $CODE_SOURCE_PATH`).
2. **Start the Ray head** with all available GPUs using `ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE"`. The environment variable `LOCAL_WORLD_SIZE` (default 8) determines the GPU count.
3. **Run the training driver** (`python train_ray.py`), which calls `ray.init(address="auto")` and creates the `TorchTrainer`.
4. **Stop the Ray cluster** (`ray stop`) after the driver completes.

The head also starts the Ray dashboard (`--dashboard-host=0.0.0.0`) for monitoring. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Worker Branch (for future multi‑node scaling)

Although the single‑node scenario only uses the head branch, the bootstrap command includes a worker branch that would join the head via `ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT" --num-gpus="$GPUS_PER_NODE" --block`. This ensures the same YAML can later be extended to multiple nodes without modification. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Prerequisites

- The [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) must be installed and authenticated.
- The workload environment must declare `ray[default,train]>=2.30` and other required dependencies (see Dependency management).
- The compute target must be a single node with `num_accelerators: 8` and `accelerator_type: GPU_8xH100`.

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) – The high‑level distributed training framework launched after bootstrap.
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) – The Ray Train wrapper for PyTorch that handles worker management.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The parallelism strategy used by `prepare_model` on each worker.
- [MLflow](/concepts/mlflow.md) – Metrics are logged from the training function to the experiment.
- H100 GPU Support on Databricks – The hardware used in the example.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Full specification for the AI Runtime workload configuration.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
