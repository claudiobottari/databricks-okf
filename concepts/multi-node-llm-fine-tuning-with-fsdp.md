---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7a0b802e521bf7358a654e97645f7ecf0570764fc13cb855fced5ee3097496a
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-node-llm-fine-tuning-with-fsdp
    - MLFWF
    - Multi-Node LLM Fine-Tuning
    - Multi-node LLM Fine-tuning
    - Multi‑node LLM Fine‑tuning
    - Multi‑node LLM fine‑tuning with FSDP
    - FSDP multi-node training
    - Large Language Model (LLM) Fine-tuning
    - Model Fine-tuning
    - Multi-Node Multi-GPU Fine-tuning
    - Multi-node LLM SFT example
    - Multi-node training
    - model fine-tuning
    - multi-node-fsdp-fine-tuning-on-databricks
    - MFFOD
    - multi-node-llm-fine-tuning-with-fsdp-on-databricks
    - MLFWFOD
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Multi-node LLM fine-tuning with FSDP
description: A distributed-training pattern using PyTorch FSDP and torchrun to fine-tune Llama-3.1-8B across 16 H100 GPUs (2 nodes), with MLflow logging and Unity Catalog checkpointing.
tags:
  - distributed-training
  - llm
  - fsdp
  - fine-tuning
timestamp: "2026-06-18T10:42:55.753Z"
---



# Multi-node LLM fine-tuning with FSDP

**Multi-node LLM fine-tuning with FSDP** is a distributed training pattern that uses PyTorch Fully Sharded Data Parallel (FSDP) to fine-tune large language models across multiple GPU nodes. This approach enables training models that would not fit into a single GPU's memory by sharding model parameters, gradients, and optimizer states across accelerators.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

FSDP (Fully Sharded Data Parallel) shards model parameters across the entire data-parallel group, reducing per-GPU memory consumption. Each GPU holds only a fraction of the model's total parameters at any given time, making it possible to fine-tune models like Llama-3.1-8B (8 billion parameters) across 16 H100 GPUs distributed over 2 nodes.^[ai-runtime-cli-examples-databricks-on-aws.md]

The training uses `torchrun` for process orchestration, which handles distributed process group initialization, world size calculation, and per-node rank assignment automatically.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Workload architecture

### Compute configuration

A typical multi-node FSDP workload requests 16 H100 GPUs across 2 compute nodes:

```yaml
compute:
  num_accelerators: 16
  accelerator_type: GPU_2xH100_2nodes
```

Each node contains 8 H100 GPUs. The `num_accelerators` field must equal `num_nodes * num_gpus_per_node` (in this example, `2 * 8 = 16`).^[ai-runtime-cli-examples-databricks-on-aws.md]

### Launch script

The launcher script uses `torchrun` with FSDP:

```python
# train.py
import torch
from torch.distributed.fsdp import FullyShardedDataParallel
# ... model loading, training loop
```

`torchrun` sets environment variables `LOCAL_RANK`, `RANK`, `WORLD_SIZE`, and `MASTER_ADDR` on each process, which FSDP uses to shard parameters correctly. The model is wrapped in `FullyShardedDataParallel` before the optimizer is created.^[ai-runtime-cli-examples-databricks-on-aws.md]

### MLflow and checkpoint integration

Training logs metrics, parameters, and artifacts to an [MLflow](/concepts/mlflow.md) experiment. Checkpoints are saved to a Unity Catalog volume for persistence and downstream evaluation.^[ai-runtime-cli-examples-databricks-on-aws.md]

## When to use FSDP

FSDP is appropriate when:
- The model is too large for a single GPU's memory
- You have access to multiple GPU nodes (2 or more)
- You want to reduce memory footprint without sacrificing training throughput
- You need to distribute training across multiple machines

## Related concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The `air` CLI used to submit FSDP workloads
- [Fully Sharded Data Parallel](/concepts/fully-sharded-data-parallel-fsdp.md) — PyTorch's implementation of full-shard data parallelism
- torchrun — PyTorch's distributed launcher
- [MLflow](/concepts/mlflow.md) — Experiment tracking
- [LLM fine-tuning](/concepts/llm-fine-tuning-on-databricks.md) — General fine-tuning patterns
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) — Parallel training across multiple accelerators

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
