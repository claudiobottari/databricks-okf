---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12452530abfadb750a4619ff5f5e92ee6e58b5003df562ef42a7d26f56f63fc2
  pageDirectory: concepts
  sources:
    - multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchrun-multi-node-launcher
    - TML
  citations:
    - file: multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
title: Torchrun Multi-Node Launcher
description: A PyTorch distributed launcher that reads rendezvous environment variables (NUM_NODES, NODE_RANK, LOCAL_WORLD_SIZE, MASTER_ADDR, MASTER_PORT) to launch one training process per GPU across multiple nodes without a separate launcher script.
tags:
  - distributed-training
  - pytorch
  - infrastructure
timestamp: "2026-06-19T19:47:57.777Z"
---

# Torchrun Multi-Node Launcher

**Torchrun Multi-Node Launcher** refers to the use of PyTorch’s `torchrun` utility to launch distributed training jobs that span multiple compute nodes, each with multiple GPUs. The launcher is commonly paired with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) to train large language models that cannot fit into a single GPU’s memory. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## How It Works

When using `torchrun` in a multi-node environment, the launcher expects a set of rendezvous environment variables that describe the cluster topology. On Databricks, the AI Runtime automatically sets the following variables on each node: `NUM_NODES`, `NODE_RANK`, `LOCAL_WORLD_SIZE`, `MASTER_ADDR`, and `MASTER_PORT`. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

The `torchrun` command reads these variables to coordinate process group initialization across nodes. It launches one process per GPU, so the number of processes equals the total number of GPUs across all nodes. For example, with two 8‑GPU nodes, `torchrun` starts 16 processes, each owning one GPU. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Example Command

The following command is used in a workload configuration to run a training script across two nodes:

```bash
torchrun \
  --nnodes="$NUM_NODES" \
  --node_rank="$NODE_RANK" \
  --nproc_per_node="${LOCAL_WORLD_SIZE:-8}" \
  --master_addr="$MASTER_ADDR" \
  --master_port="$MASTER_PORT" \
  train.py
```

- `--nnodes`: Total number of nodes (set by AI Runtime as `$NUM_NODES`).  
- `--node_rank`: Rank of the current node (set as `$NODE_RANK`).  
- `--nproc_per_node`: Number of processes (GPUs) per node; defaults to 8 if `LOCAL_WORLD_SIZE` is unset.  
- `--master_addr` and `--master_port`: Address and port of the master node for rendezvous.  

Because AI Runtime supplies all required environment variables, the inline command serves as the complete launcher. No separate launcher script is needed. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Integration with FSDP

In multi-node FSDP training, `torchrun` initializes a process group over the network (using NCCL backend) so that every GPU rank can communicate. The script then wraps the model with `FullyShardedDataParallel`, sharding parameters, gradients, and optimizer states across all ranks. The combination of `torchrun` and FSDP allows training models like Llama‑3.1‑8B on 16 GPUs across two nodes. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient parallelism strategy enabled by multi-node launchers.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Alternative parallelism approach for multi-node training.
- [AI Runtime on Databricks](/concepts/ai-runtime-on-databricks.md) – Platform that sets rendezvous environment variables for `torchrun`.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – Common node type used in multi-node distributed training.

## Sources

- multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md

# Citations

1. [multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md](/references/multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws-d26ca320.md)
