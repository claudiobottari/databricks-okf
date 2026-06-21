---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33de44f0cb770d9a04192d28441d7c98c4105534169a381cebacf29ec090eeb5
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-cluster-bootstrap-pattern-for-multi-node-training
    - RCBPFMT
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Ray cluster bootstrap pattern for multi-node training
description: Pattern for starting a Ray cluster inline within a workload command, with a head node branch and worker node join logic, enabling single-node and multi-node scaling.
tags:
  - ray
  - cluster-management
  - distributed-training
timestamp: "2026-06-18T12:08:32.223Z"
---

# Ray Cluster Bootstrap Pattern for Multi-Node Training

The **Ray cluster bootstrap pattern for multi-node training** is a deployment approach where a single workload command starts a Ray cluster on each node and then runs a distributed training driver. This pattern is commonly used with [Ray Train](/concepts/ray-train-resource-allocation.md)'s `TorchTrainer` for data-parallel or model-parallel training across multiple GPUs and nodes. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

In this pattern, the workload's `command` field handles both Ray cluster initialization and training execution. One node acts as the Ray head, starting the cluster with all available GPUs, while other nodes join as workers. After the cluster is formed, the training script runs — typically a Ray Train driver that launches one worker per GPU. ^[distributed-training-with-ray-train-databricks-on-aws.md]

This approach eliminates the need for a separate cluster launcher or dependency file. The bootstrap logic is embedded directly in the workload configuration, making it self-contained and reproducible. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Bootstrap Command Structure

The bootstrap command uses environment variables like `NODE_RANK` and `MASTER_ADDR` to determine each node's role. A typical command has two branches: ^[distributed-training-with-ray-train-databricks-on-aws.md]

```bash
cd $CODE_SOURCE_PATH
RAY_HEAD_PORT=6379
GPUS_PER_NODE=${LOCAL_WORLD_SIZE:-8}

if [ "${NODE_RANK:-0}" = "0" ]; then
    # Node 0: start Ray head with all GPUs
    ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE" --dashboard-host=0.0.0.0
    python train_ray.py
    ray stop
else
    # Other nodes: connect to head
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

The head node starts the Ray cluster, runs the training driver, and stops the cluster when training completes. Worker nodes join the head and block until the job finishes. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Key Components

### Ray Head Initialization

The head node starts with `ray start --head`, specifying the port and GPU count. The `--dashboard-host=0.0.0.0` flag makes the Ray dashboard accessible for monitoring. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Worker Node Joining

Worker nodes connect to the head using `ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT"`. The `--block` flag keeps the worker process alive until the cluster is shut down. A retry loop handles transient connection failures. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Training Driver

After the cluster is ready, the training script (e.g., `train_ray.py`) initializes Ray with `ray.init(address="auto")` and uses [TorchTrainer](/concepts/ray-train-torchtrainer.md) to launch distributed training. The driver detects available GPUs via `ray.cluster_resources()` and configures the appropriate number of workers. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
def main():
    ray.init(address="auto")
    total_gpus = int(ray.cluster_resources().get("GPU", 0))
    trainer = TorchTrainer(
        train_func,
        train_loop_config={"lr": 2e-5, "batch_size": 4, "max_steps": 100},
        scaling_config=ScalingConfig(num_workers=total_gpus, use_gpu=True),
    )
    trainer.fit()
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Single-Node vs. Multi-Node

The bootstrap command is designed to work for both single-node and multi-node deployments: ^[distributed-training-with-ray-train-databricks-on-aws.md]

- **Single-node**: The head branch runs on the only node. The worker branch is never executed.
- **Multi-node**: Node 0 runs the head branch; all other nodes run the worker branch. The same command file works for both scenarios without modification.

## Environment Variables

The pattern relies on several environment variables: ^[distributed-training-with-ray-train-databricks-on-aws.md]

| Variable | Purpose |
|----------|---------|
| `NODE_RANK` | Determines which node is the head (rank 0) |
| `MASTER_ADDR` | Address of the head node for workers to connect |
| `LOCAL_WORLD_SIZE` | Number of GPUs on the current node |
| `CODE_SOURCE_PATH` | Path to the uploaded project code |

## Best Practices

- **Use a retry loop** for worker nodes to handle transient connection failures when joining the head. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Stop the Ray cluster** after training completes on the head node to clean up resources. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Set `NCCL_SOCKET_IFNAME`** to the appropriate network interface (e.g., `eth0`) for multi-node GPU communication. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Declare all dependencies inline** in the workload configuration to avoid separate requirement files. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) — The distributed training framework used with this bootstrap pattern
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) — Ray Train's trainer for PyTorch models
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The parallelism strategy used in the training script
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The tool used to submit and manage Ray workloads
- [Multi-Node LLM Fine-Tuning](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) — An advanced pattern building on this bootstrap approach
- [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) — The configuration format for defining Ray workloads

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
