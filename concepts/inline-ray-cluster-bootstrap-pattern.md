---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c5ffcdc7f8c1d445af82f29ae90d0b607a42de55ecf170f573849a3fabf55da
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inline-ray-cluster-bootstrap-pattern
    - IRCBP
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Inline Ray Cluster Bootstrap Pattern
description: A pattern for starting a Ray cluster directly within a workload command by running ray start on the head node and having worker nodes join the cluster, enabling distributed training without a separate cluster launcher.
tags:
  - ray
  - distributed-computing
  - infrastructure
timestamp: "2026-06-18T15:34:21.135Z"
---

# Inline Ray Cluster Bootstrap Pattern

The **Inline Ray Cluster Bootstrap Pattern** is a deployment approach for distributed training workloads on the Databricks AI Runtime platform. In this pattern, the Ray cluster is started, used, and stopped entirely within the workload's command section, without requiring a separate cluster launcher script or dependency file. All Ray cluster orchestration logic is embedded directly in the [Workload YAML Configuration](/concepts/workload-yaml-configuration.md). ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

In the inline bootstrap pattern, the workload's `command` field contains the complete logic for starting a Ray head node, running the training script, and stopping the cluster when training completes. This eliminates the need for external scripts to manage the Ray cluster lifecycle. The pattern also includes logic for worker nodes to join the head, allowing the same command to work across multi-node configurations. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## How It Works

### Single-Node Bootstrap

For single-node configurations, the bootstrap script performs the following steps in sequence: ^[distributed-training-with-ray-train-databricks-on-aws.md]

1. Start a Ray head node with all available GPUs on the node.
2. Execute the Ray Train driver script (typically `train_ray.py`).
3. Stop the Ray cluster after training completes.

### Multi-Node Support

The same bootstrap script includes logic for worker nodes. When `NODE_RANK` is not `0`, the script attempts to connect to the existing Ray head at the `MASTER_ADDR` address rather than starting its own head. This design allows the pattern to scale from single-node to multi-node configurations without modifying the bootstrap logic. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Example Configuration

The following YAML excerpt demonstrates the pattern. The `command` field contains the inline bootstrap logic, while all dependencies are declared in the `environment` section: ^[distributed-training-with-ray-train-databricks-on-aws.md]

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

## Advantages

- **Simplified deployment**: No separate cluster launcher scripts or dependency files are required. All configuration lives in a single YAML file. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Self-contained**: The workload is fully self-describing, making it easier to reproduce and share. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Scalable**: The same command works for both single-node and multi-node configurations without modification. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Clean lifecycle**: The Ray cluster is automatically stopped when training completes, preventing resource leaks. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Considerations

- **Retry logic**: Worker nodes include retry logic (up to 12 attempts with 5-second delays) when connecting to the Ray head, providing resilience against transient network issues. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- **Logging**: Both the Ray head and the driver run on node 0, so logs stream from a single node, simplifying log inspection. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) — The distributed training framework used with this bootstrap pattern
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) — Ray Train's wrapper for PyTorch distributed training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The underlying parallelism strategy used by Ray Train in this pattern
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool used to submit and manage workloads
- [Multi-node LLM fine-tuning with FSDP](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) — An alternative scaling approach for larger models
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) — Documentation for the full YAML configuration schema

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
