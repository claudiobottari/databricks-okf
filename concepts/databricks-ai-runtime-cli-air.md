---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 31a9c6fb27fa994f9c1c25466a5db5345e5272de27f3f3f136d556a9c6b5591d
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-cli-air
    - DARC(
    - Databricks AI Runtime CLI
    - databricks-ai-runtime-cli-air-workload-submission
    - DARC(WS
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
    - file: ai-runtime-cli-examples-databricks-on-aws.md
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 48
      end: 52
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 94
      end: 100
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 98
      end: 100
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 56
      end: 92
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 56
      end: 65
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 66
      end: 69
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 71
      end: 92
    - file: distributed-training-with-ray-train-databricks-on-aws.md
      start: 103
      end: 107
title: Databricks AI Runtime CLI (air)
description: Command-line interface for submitting and managing distributed AI/ML workloads on Databricks clusters, using commands like `air run -f train.yaml`
tags:
  - cli
  - databricks
  - workload-management
timestamp: "2026-06-19T22:02:05.569Z"
---

# Databricks [AI Runtime CLI (air)](/concepts/ai-runtime-cli-air.md)

The **Databricks AI Runtime CLI (`air`)** is a command-line tool for submitting, monitoring, and managing distributed AI/ML workloads on Databricks using YAML configuration files. It is part of the [AI Runtime](/concepts/ai-runtime.md) ecosystem and enables users to run distributed training jobs, inspect run status, and retrieve logs without interacting with the Databricks web UI. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

The `air` CLI allows users to define workloads in YAML files that specify the experiment name, compute resources, code source, environment dependencies, and execution command. These workload YAMLs can describe complex distributed training patterns, including multi-node LLM fine-tuning with [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) and distributed data-parallel training with [Ray Train](/concepts/ray-train-resource-allocation.md). ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Installation

The CLI must be installed and authenticated before use. Databricks provides an [installation guide](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation) for setting up the `air` CLI. ^[distributed-training-with-ray-train-databricks-on-aws.md#L48-L52]

## Commands

The `air` CLI supports the following commands for workload management:

- **`air run -f <file>`** – Submits a workload from a YAML configuration file. The `--watch` flag streams logs to the terminal until the run completes; `--dry-run` validates the configuration without submitting. ^[distributed-training-with-ray-train-databricks-on-aws.md#L94-L100]
- **`air get run <run-id>`** – Retrieves metadata and status for a specific run by its run ID. ^[distributed-training-with-ray-train-databricks-on-aws.md#L98-L100]
- **`air logs <run-id>`** – Fetches logs from a completed or in-progress run. ^[distributed-training-with-ray-train-databricks-on-aws.md#L98-L100]

## Workload YAML Structure

A workload YAML file (e.g., `train.yaml`) defines the following key sections: ^[distributed-training-with-ray-train-databricks-on-aws.md#L56-L92]

| Section | Description |
|---------|-------------|
| `experiment_name` | Name of the MLflow experiment for tracking metrics |
| `environment` | Specifies the runtime version and inline Python dependencies |
| `compute` | Defines the accelerator type and number of GPUs (e.g., `GPU_8xH100`) |
| `code_source` | Declares how to upload code (e.g., `snapshot` for local directory) |
| `command` | The shell command to execute, including cluster setup and training script |
| `timeout_minutes` | Maximum runtime before the job is terminated |
| `env_variables` | Environment variables to set on the compute node |

### Environment Dependencies

Dependencies can be declared inline under the `environment` section using the dependencies array. The base image version is specified with the `version` field. For example, a workload using Ray Train would include dependencies like `ray[default,train]>=2.30` and `transformers>=4.45`. ^[distributed-training-with-ray-train-databricks-on-aws.md#L56-L65]

### Compute Configuration

The compute section specifies the hardware resources. For example, `num_accelerators: 8` and `accelerator_type: GPU_8xH100` requests a single node with 8 H100 GPUs. ^[distributed-training-with-ray-train-databricks-on-aws.md#L66-L69]

## Usage Example

A typical workflow proceeds as follows: ^[distributed-training-with-ray-train-databricks-on-aws.md#L94-L100]

```bash
# Validate the workload configuration without submitting
air run -f train.yaml --dry-run

# Submit the workload and stream logs until completion
air run -f train.yaml --watch

# After the run starts, inspect status and logs
air get run <run-id>
air logs <run-id>
```

## Distributed Training Patterns

The `air` CLI supports two main distributed training patterns, demonstrated in official examples: ^[ai-runtime-cli-examples-databricks-on-aws.md]

- **Multi-node LLM fine-tuning with FSDP**: Supervised fine-tuning of models like Llama-3.1-8B across 16 H100 GPUs (2 nodes) using `torchrun` and PyTorch FSDP. Logs to MLflow and checkpoints to a Unity Catalog volume.
- **Distributed training with Ray Train**: Data-parallel fine-tuning using Ray Train's `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU.

### Ray Cluster Bootstrap

For Ray Train workloads, the workload YAML's `command` section typically starts a Ray head node, runs the training script, and then stops the cluster. The command also includes a worker branch that joins the head, allowing the same YAML to scale to multiple nodes without modification. ^[distributed-training-with-ray-train-databricks-on-aws.md#L71-L92]

## Results and Metrics

Metrics reported during training appear in the MLflow experiment named in `experiment_name`, viewable in the Databricks workspace MLflow UI. For Ray Train workloads, metrics reported with `ray.train.report` are automatically logged. ^[distributed-training-with-ray-train-databricks-on-aws.md#L103-L107]

## Related Concepts

- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Complete specification for the YAML configuration format
- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment for AI workloads on Databricks
- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed training framework commonly used with the AI Runtime
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient distributed training strategy
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Multi-GPU and multi-node training patterns supported by the CLI
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Tracking and visualization of training metrics
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – GPU configuration commonly used with `air` CLI workloads

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md
- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
2. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
3. [distributed-training-with-ray-train-databricks-on-aws.md:48-52](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
4. [distributed-training-with-ray-train-databricks-on-aws.md:94-100](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
5. [distributed-training-with-ray-train-databricks-on-aws.md:98-100](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
6. [distributed-training-with-ray-train-databricks-on-aws.md:56-92](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
7. [distributed-training-with-ray-train-databricks-on-aws.md:56-65](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
8. [distributed-training-with-ray-train-databricks-on-aws.md:66-69](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
9. [distributed-training-with-ray-train-databricks-on-aws.md:71-92](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
10. [distributed-training-with-ray-train-databricks-on-aws.md:103-107](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
