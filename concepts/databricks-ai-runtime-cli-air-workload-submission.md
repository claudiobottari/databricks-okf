---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7000dcf7ed7543562ead7719ae01438c56972af370616ffc2c88e891853bdd1f
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-cli-air-workload-submission
    - DARC(WS
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Databricks AI Runtime CLI (air) workload submission
description: CLI tool for submitting distributed training workloads to Databricks using YAML configuration with inline dependencies, compute specs, and command scripts.
tags:
  - databricks
  - cli
  - workload-management
timestamp: "2026-06-18T12:08:24.568Z"
---

# Databricks [AI Runtime CLI (air)](/concepts/ai-runtime-cli-air.md) Workload Submission

The **Databricks AI Runtime CLI (`air`) workload submission** feature allows you to define and run distributed ML training workloads directly from the command line. By writing a YAML configuration file and using the `air run` command, you can submit jobs that specify compute resources, dependencies, code, and execution commands, then inspect results via `air logs` and `air get run`. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

The `air` CLI is part of the [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) ecosystem and provides a lightweight interface for running AI workloads without manually configuring clusters or using the Databricks Jobs UI. Workloads are defined declaratively in a YAML file that describes the experiment name, environment dependencies, compute requirements, code source, and the command to execute. The CLI supports dry-run validation, real-time streaming of logs (`--watch`), and post-hoc inspection of run metadata and logs. ^[distributed-training-with-ray-train-databricks-on-aws.md]

Workloads run on Databricks compute with full access to [MLflow](/concepts/mlflow.md) tracking. The environment automatically injects environment variables such as `MLFLOW_RUN_ID` and configures the Databricks tracking URI, so metrics logging to MLflow works without explicit authentication setup. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Submitting a Workload

Use the `air run` command to submit a workload defined in a YAML file:

```bash
air run -f train.yaml          # basic submission
air run -f train.yaml --dry-run   # validate config without starting
air run -f train.yaml --watch     # stream logs to terminal in real-time
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Workload YAML Structure

The YAML configuration file defines all aspects of the workload. The following fields are supported (based on the reference example): ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `experiment_name`
A user-defined name for the MLflow experiment under which run metrics and artifacts are logged. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `environment`
Specifies the runtime version and Python dependencies:
- `version`: The Databricks AI Runtime client image version (e.g., `'4'`).
- `dependencies`: A list of Python packages to install (e.g., `ray[default,train]>=2.30`, `transformers>=4.45`).

Dependencies are installed in the execution environment before the workload command runs. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `compute`
Defines the hardware resources for the workload:
- `num_accelerators`: Number of accelerators (e.g., GPUs) to use.
- `accelerator_type`: The type of accelerator (e.g., `GPU_8xH100` for 8 H100 GPUs on a single node).

The compute specification determines the shape of the node(s) allocated to the workload. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `code_source`
Specifies how the workload code is uploaded. The example uses the `snapshot` type:
- `type: snapshot`: Uploads the local project directory.
- `snapshot.root_path`: Path to the project root (e.g., `.` for the current directory).

The code is made available at the `$CODE_SOURCE_PATH` environment variable during execution. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `command`
A shell command that runs as the workload entry point. The command can include environment variable references (e.g., `$CODE_SOURCE_PATH`, `$MASTER_ADDR`, `$LOCAL_WORLD_SIZE`). Multi-node workloads use `NODE_RANK` to distinguish head and worker roles. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `max_retries`
Maximum number of retries on failure (e.g., `0` for no retries). ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `timeout_minutes`
Maximum runtime in minutes (e.g., `90`). ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `env_variables`
Custom environment variables passed to the workload process (e.g., `NCCL_SOCKET_IFNAME: eth0`). ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Monitoring and Inspecting Runs

After submission, you can retrieve run metadata and logs: ^[distributed-training-with-ray-train-databricks-on-aws.md]

```bash
air get run <run-id>    # show run status, configuration, and final metrics
air logs <run-id>       # stream or retrieve stdout/stderr from the run
```

If submitted with `--watch`, logs stream live to the terminal during execution. ^[distributed-training-with-ray-train-databricks-on-aws.md]

Metrics reported with `ray.train.report` and logged to MLflow are visible in the workspace MLflow UI under the experiment named in `experiment_name`. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Example: Distributed Training with Ray Train

A common use case is running [Ray Train](/concepts/ray-train-resource-allocation.md) for distributed data-parallel fine-tuning. The workload YAML requests a single `GPU_8xH100` node, installs dependencies (`ray[default,train]`, `transformers`, `datasets`, `fsspec`), uploads the local project via `snapshot`, and executes a command that starts a Ray head, runs a Python driver, and stops the cluster. The driver uses `ray.train.torch.TorchTrainer` to launch one worker per GPU, wrapping the model in DDP via `prepare_model` and sharding data via `prepare_data_loader`. ^[distributed-training-with-ray-train-databricks-on-aws.md]

This pattern is documented in detail in the [Distributed training with Ray Train](/concepts/distributed-training-with-ray-train.md) example.

## Related Concepts

- [Databricks AI Runtime CLI](/concepts/databricks-ai-runtime-cli-air.md) — Installation and authentication
- [Ray Train](/concepts/ray-train-resource-allocation.md) — Distributed training framework used in workload examples
- [MLflow](/concepts/mlflow.md) — Experiment tracking and metric logging
- [FSDP multi-node training](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) — Another workload pattern for large model fine-tuning
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) — Full field documentation

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
