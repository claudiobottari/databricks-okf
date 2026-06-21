---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46c2c93d93b8559eea6ae4948ab53f854a322ed2591c2c24abfada5c18c0aa06
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-cluster-bootstrap-on-databricks-nodes
    - RCBODN
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Ray Cluster Bootstrap on Databricks Nodes
description: Pattern for starting a Ray cluster on Databricks compute nodes using the workload command, including head node initialization and worker node joining logic.
tags:
  - ray
  - databricks
  - cluster
timestamp: "2026-06-19T10:19:21.501Z"
---

# Ray Cluster Bootstrap on Databricks Nodes

**Ray Cluster Bootstrap on Databricks Nodes** refers to the process of starting a Ray cluster directly on Databricks compute nodes as part of an AI Runtime (AIR) workload. This bootstrap is typically performed inline within the workload’s `command` section and enables distributed training frameworks like [Ray Train](/concepts/ray-train-resource-allocation.md) to leverage all available GPUs on a node (or across multiple nodes) without requiring a separate cluster management service.

## Overview

In an `air` workload, the bootstrap script is written as a shell command that determines whether the current node is the head (rank 0) or a worker. On the head node, the script starts a Ray head process, runs the training driver, and then stops the cluster. On worker nodes, the script connects to the head using the `MASTER_ADDR` and joins the cluster in blocking mode. ^[distributed-training-with-ray-train-databricks-on-aws.md]

The bootstrap is fully contained in the workload YAML, making the workload self-contained and reproducible. No external Ray launcher or additional infrastructure is needed.

## Bootstrap Process

### Head Node (Rank 0)

When the environment variable `NODE_RANK` is `0`, the node is treated as the head. The bootstrap script does the following:

1. Starts a Ray head process with all available GPUs, a specified port, and an accessible dashboard.
2. Executes the Python training driver (e.g., `train_ray.py`).
3. Stops the Ray cluster after the driver finishes.

The command used is:  
`ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE" --dashboard-host=0.0.0.0`  
^[distributed-training-with-ray-train-databricks-on-aws.md]

The number of GPUs per node is determined by the environment variable `LOCAL_WORLD_SIZE`, which defaults to `8` if not set. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Worker Nodes (Rank != 0)

On non-head nodes, the script attempts to connect to the head using `ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT"` with the same `--num-gpus` flag and the `--block` option to keep the process alive. If the connection fails, it retries up to 12 times with a 5-second delay between attempts. ^[distributed-training-with-ray-train-databricks-on-aws.md]

This pattern allows the same YAML command to be reused across single-node and multi-node deployments — when a job requests only one node, the worker branch is never reached.

## Example Configuration

The following excerpt from a `train.yaml` file shows the inline bootstrap command and the environment variables used: ^[distributed-training-with-ray-train-databricks-on-aws.md]

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

The example also sets `NCCL_SOCKET_IFNAME: eth0` as an environment variable to ensure correct network interface selection for inter-GPU communication. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Accessing the Ray Cluster from the Driver

After the head starts, the Python training driver (e.g., `train_ray.py`) connects to the Ray cluster with `ray.init(address="auto")`. The driver then obtains the total GPU count from cluster resources and creates a [Ray Train TorchTrainer](/concepts/ray-train-torchtrainer.md) with one worker per GPU. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Environment Variables

| Variable | Role |
|----------|------|
| `NODE_RANK` | Set by the Databricks runtime; `0` indicates the head node. |
| `LOCAL_WORLD_SIZE` | Number of GPUs on the node; defaults to `8`. |
| `MASTER_ADDR` | IP address of the head node, used by workers to connect. |
| `RAY_HEAD_PORT` | Port for the Ray head (6379 in the example). |
| `NCCL_SOCKET_IFNAME` | Network interface for NCCL communication (set to `eth0`). |

## Related Concepts

- [Distributed training with Ray Train](/concepts/distributed-training-with-ray-train.md)
- [AI Runtime (AIR) Workloads](/concepts/ai-runtime-air-cli-workload-yaml.md)
- [Ray Train TorchTrainer](/concepts/ray-train-torchtrainer.md)
- [Multi-node LLM fine-tuning with FSDP](/concepts/multi-node-llm-fine-tuning-with-fsdp.md)
- Workload YAML reference

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
