---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0a0deac37a3ddee25bf25fe9e533a68dcd1bfa085f2247f79c999d3964c5b5e
  pageDirectory: concepts
  sources:
    - multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-air-cli-distributed-workflows
    - AR(CDW
  citations:
    - file: multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
title: AI Runtime (air) CLI Distributed Workflows
description: Databricks' CLI tool and YAML-based workload configuration system for defining and submitting multi-node distributed training jobs, with built-in secret injection, MLflow integration, Unity Catalog volume access, and automatic rendezvous variable injection.
tags:
  - databricks
  - mlops
  - workflow-orchestration
timestamp: "2026-06-19T19:48:07.906Z"
---

# AI Runtime (air) CLI Distributed Workflows

**AI Runtime (air) CLI Distributed Workflows** refers to the capability of the `air` command‑line interface to orchestrate multi‑node, multi‑GPU deep learning training jobs on Databricks. The CLI handles node provisioning, environment setup, and process launching so that users can focus on the training script itself. The primary example involves supervised fine‑tuning (SFT) of large language models using PyTorch [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) across multiple nodes. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Overview

A distributed workflow is defined by a YAML configuration file (e.g., `train.yaml`). This file declares the experiment name, compute resources, code source, command to run, environment variables, secrets, and hyperparameters. When submitted with `air run -f train.yaml`, the CLI provisions the requested nodes, injects rendezvous environment variables on each node, executes the command once per node, and streams logs back to the user. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Key Components of a Distributed Workflow

### Compute Specification

The `compute` field in the YAML specifies the number of accelerators and their type. For multi‑node training, the total number of GPUs is divided across nodes of a given type. For example, `num_accelerators: 16` with `accelerator_type: GPU_8xH100` provisions two nodes, each containing 8 H100 GPUs. The CLI automatically determines the node count based on the accelerator type’s per‑node GPU count. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Command and Process Launcher

The `command` field runs once per node. Distributed training frameworks such as `torchrun` are invoked inside this command, reading the environment variables that AI Runtime sets on each node to coordinate process ranks across nodes. The typical `torchrun` invocation is:

```bash
torchrun \
  --nnodes="$NUM_NODES" \
  --node_rank="$NODE_RANK" \
  --nproc_per_node="${LOCAL_WORLD_SIZE:-8}" \
  --master_addr="$MASTER_ADDR" \
  --master_port="$MASTER_PORT" \
  train.py
```

This eliminates the need for a separate launcher script; the entire multi‑node launch is defined inline in the YAML. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Rendezvous Environment Variables

AI Runtime sets the following environment variables on each node before running the command:

| Variable       | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `NUM_NODES`    | Total number of nodes in the job                                        |
| `NODE_RANK`    | Zero‑based rank of this node                                            |
| `LOCAL_WORLD_SIZE` | Number of processes (GPUs) per node                                 |
| `MASTER_ADDR`  | Hostname of the rank‑0 node for NCCL rendezvous                         |
| `MASTER_PORT`  | Port used for rendezvous                                                |

These variables mirror the arguments expected by `torchrun`, making integration straightforward. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Secret Injection

Sensitive credentials, such as Hugging Face tokens, can be injected via the `secrets` block. The token is referenced as a Databricks secret (scope/key) and made available as an environment variable inside the command. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Hyperparameters

Arbitrary hyperparameters are defined under `parameters`. The CLI writes them to a file and sets `HYPERPARAMETERS_PATH` as an environment variable. The training script reads this file (e.g., using `yaml.safe_load`) to obtain values such as `model_name`, `learning_rate`, and `output_dir`. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Environment and Dependencies

The `environment` block specifies a client image version and a list of Python dependencies (installed on top of the base AI Runtime image). The `torch` package ships by default; only extras need to be listed. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Submitting and Monitoring Runs

Submit a distributed run with validation and watch logs in real‑time:

```bash
air run -f train.yaml --dry-run   # validate configuration
air run -f train.yaml --watch     # submit and stream logs
```

Because multiple nodes execute the same command, logs can be inspected per node:

```bash
air get run <run-id>
air logs <run-id> --node 0
air logs <run-id> --node 1
```

^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## End‑to‑End Example: FSDP Fine‑Tuning

The canonical distributed workflow example fine‑tunes Llama‑3.1‑8B on 16 H100 GPUs (2 nodes) using FSDP. The project contains two files:

- `train.yaml` – the workload configuration described above.
- `train.py` – a Python script that uses `torch.distributed` to initialise the process group, wraps each transformer layer with FSDP, trains on a tokenised instruction dataset, and consolidates the checkpoint to a [Unity Catalog](/concepts/unity-catalog.md) volume from rank 0.

Metrics are logged to the [MLflow](/concepts/mlflow.md) experiment named in `experiment_name`, and the fine‑tuned model is saved to the output path defined in `parameters.output_dir`. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- torchrun
- [Multi-node training](/concepts/multi-node-llm-fine-tuning-with-fsdp.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [AI Runtime (air) CLI Installation](/concepts/ai-runtime-cli-installation-via-uv.md)
- Workload YAML configuration reference

## Sources

- multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md

# Citations

1. [multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md](/references/multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws-d26ca320.md)
