---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e8733d4f8e958ff43193a3c471ac76ef057f72b7ce623104ad65be644f357cc
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-workload-yaml-configuration
    - AWYC
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: AIR Workload YAML Configuration
description: A YAML-based configuration format (train.yaml) that defines experiment name, compute spec, command, environment dependencies, and code source for AI Runtime CLI training jobs.
tags:
  - databricks
  - yaml
  - configuration
  - workload
timestamp: "2026-06-19T08:56:51.396Z"
---

# AIR [Workload YAML Configuration](/concepts/workload-yaml-configuration.md)

**AIR Workload YAML Configuration** is the primary method for defining and configuring distributed training jobs using the Databricks AI Runtime CLI (`air`). The YAML file specifies the experiment, compute resources, code source, dependencies, environment variables, and the command to execute. ^[distributed-training-with-ray-train-databricks-on-aws.md]  
A minimal configuration requires only `experiment_name`, `compute`, and `command`; other fields are optional and can be added as needed. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Overview

An Air workload configuration is declared in a YAML file (commonly named `train.yaml`) that describes all aspects of a training run. The configuration includes the experiment name, compute requirements, code location, software dependencies, and the command that orchestrates the training process. The workload is submitted using the `air run -f train.yaml` command. ^[distributed-training-with-ray-train-databricks-on-aws.md]  
The CLI uploads local code (if a `code_source` is configured), submits the job, and prints a run ID. The run is automatically tracked in an MLflow experiment, making metrics, parameters, artifacts, and logs viewable in the workspace MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Top-Level Fields

The YAML configuration typically includes the following top-level fields:

| Field | Description | Required |
|-------|-------------|----------|
| `experiment_name` | Name of the [MLflow Experiment](/concepts/mlflow-experiment.md) for tracking metrics and artifacts | Yes |
| `environment` | Container image version and Python dependencies | No (but needed for custom dependencies) |
| `compute` | Compute resource requirements including GPU count and accelerator type | Yes |
| `code_source` | Method for uploading project code (e.g., snapshot) | No (required when running local code) |
| `command` | Shell command to execute on the compute node | Yes |
| `max_retries` | Number of retry attempts on failure | Yes |
| `timeout_minutes` | Maximum runtime before the job is killed | Yes |
| `env_variables` | Environment variables to set on the compute node | No |

^[distributed-training-with-ray-train-databricks-on-aws.md]  
The minimal config (with no local code) can be as short as:

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### experiment_name

The `experiment_name` field specifies the [MLflow Experiment](/concepts/mlflow-experiment.md) where training metrics and artifacts are logged. Results are viewable in the workspace MLflow UI under this experiment. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### environment

The `environment` block declares the base container image version and Python dependencies for the training run. Dependencies are listed inline under a `dependencies` key, with the base image `version` specifying the serverless GPU environment version. This approach eliminates the need for a separate requirements file. The `version` field is optional and defaults to `'4'`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md, distributed-training-with-ray-train-databricks-on-aws.md]

```yaml
environment:
  version: '4'
  dependencies:
    - ray[default,train]>=2.30
    - transformers>=4.45
    - datasets>=3.0
    - huggingface_hub>=0.34
    - fsspec>=2024.6.1
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### compute

The `compute` block specifies the hardware resources for the training job. Key fields include `num_accelerators` (number of GPUs) and `accelerator_type` (e.g., `GPU_8xH100`, `GPU_1xA10`). ^[distributed-training-with-ray-train-databricks-on-aws.md, ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### code_source

The `code_source` field specifies how project code is uploaded. The `snapshot` type with a `root_path` of `.` uploads the entire local directory. The code is available at `$CODE_SOURCE_PATH` within the command. Databricks recommends using `$CODE_SOURCE_PATH` rather than hardcoding a path. ^[ai-runtime-cli-quickstart-databricks-on-aws.md, distributed-training-with-ray-train-databricks-on-aws.md]

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### command

The `command` field contains the shell commands executed on the compute node. This is typically a multi-line script that sets up distributed computing frameworks (such as Ray), launches training scripts, and cleans up resources. When using local code, prefix the command with `cd $CODE_SOURCE_PATH` to change to the uploaded code directory. ^[ai-runtime-cli-quickstart-databricks-on-aws.md, distributed-training-with-ray-train-databricks-on-aws.md]

```yaml
command: python $CODE_SOURCE_PATH/train.py
```

For distributed training, a more complex script is used:

```yaml
command: |
  cd $CODE_SOURCE_PATH
  RAY_HEAD_PORT=6379
  GPUS_PER_NODE=${LOCAL_WORLD_SIZE:-8}
  if [ "${NODE_RANK:-0}" = "0" ]; then
    ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE"
    python train_ray.py
    ray stop
  else
    ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT" --num-gpus="$GPUS_PER_NODE" --block
  fi
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

### max_retries and timeout_minutes

`max_retries` controls the number of automatic retry attempts on failure. Setting it to `0` means no retries. `timeout_minutes` sets the maximum runtime; the job is killed if it exceeds this limit. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```yaml
max_retries: 0
timeout_minutes: 90
```

### env_variables

The `env_variables` field sets environment variables on the compute node. This is useful for configuring networking (e.g., NCCL socket interface) and other runtime settings. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```yaml
env_variables:
  NCCL_SOCKET_IFNAME: eth0
```

## Environment Variables Available in Commands

The AI Runtime CLI injects several environment variables that are available in the `command`:

| Variable | Description |
|----------|-------------|
| `$CODE_SOURCE_PATH` | Path to the uploaded code snapshot |
| `$LOCAL_WORLD_SIZE` | Number of GPUs on the local node |
| `$NODE_RANK` | Rank of the current node (0 for the primary node) |
| `$MASTER_ADDR` | Address of the primary node for distributed coordination |
| `$MLFLOW_RUN_ID` | [MLflow Run](/concepts/mlflow-run.md) ID for logging metrics (when applicable) |

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Submitting the Workload

A workload is submitted from the command line using the `air run` command. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```bash
air run --file train.yaml
```

The CLI uploads local code (if configured), submits the job, and returns a run ID. Use that ID to inspect, watch, or cancel the run. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Watching Logs

To stream logs until the job completes, add `--watch`:

```bash
air run --file train.yaml --watch
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Overriding YAML Fields

Override any YAML field from the command line without editing the file:

```bash
air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Validating Configuration

Use `--dry-run` to validate the configuration without submitting:

```bash
air run --file train.yaml --dry-run
```

^[distributed-training-with-ray-train-databricks-on-aws.md, ai-runtime-cli-quickstart-databricks-on-aws.md]

### Idempotent Submissions

Use `--idempotency-key` to make a submission safely retryable. If the same key has been used before, the existing run is returned instead of creating a new one.

```bash
air run --file train.yaml --idempotency-key my-unique-key
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Inspecting Runs

After submission, runs can be inspected using the `air` CLI: ^[distributed-training-with-ray-train-databricks-on-aws.md, ai-runtime-cli-quickstart-databricks-on-aws.md]

- **View status and details** – `air get run <run-id>` (output includes clickable links to the MLflow experiment and run in the workspace UI).
- **Stream or download logs** – `air logs <run-id>` streams logs from node 0. Use `--node <n>` to view logs from a specific node, and `--download-to ./logs/` to write logs to a local directory.
- **List recent runs** – `air list runs --limit 10` or `air list runs --active`.
- **Cancel a run** – `air cancel run <run-id>`.

## Common Patterns

- **Minimal config without code**: Useful for testing infrastructure or running built-in commands.
- **Local code with dependencies**: Add `environment` and `code_source` blocks and place your script alongside `train.yaml`.
- **Override fields per submission**: Use `--override` to adjust resources or timeouts without modifying the file.
- **Use `$CODE_SOURCE_PATH`**: Always prefix commands with `cd $CODE_SOURCE_PATH` when running local scripts to ensure correct path resolution.

## Best Practices

- **Pin dependency versions** to ensure reproducible builds across runs.
- **Set appropriate timeouts** based on expected training duration. The job is killed if it exceeds the timeout.
- **Use `--dry-run`** before submitting to validate the configuration.
- **Name experiments meaningfully** to organize results in the MLflow UI.
- **Handle multi-node orchestration** in the `command` using `NODE_RANK` and `MASTER_ADDR` for distributed frameworks.
- **Use `--idempotency-key`** in automation scripts to avoid duplicate submissions.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool for submitting Air workloads
- [Ray Train](/concepts/ray-train-resource-allocation.md) — Distributed training framework commonly used with Air
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concept of training across multiple GPUs or nodes
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Tracking and organizing training runs
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) — Complete specification of all configuration fields
- [Serverless Environment Versions](/concepts/serverless-environment-versioning.md) — Available versions for the `environment.version` field

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md
- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
2. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
