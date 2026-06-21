---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b85cac1efef1333dd98828b8f4546a71299cb90d06e4ffd38e5e6c27046d966d
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-databricks
    - ARC(
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: AI Runtime CLI (Databricks)
description: A command-line interface for submitting and managing machine learning training workloads on Databricks serverless GPU infrastructure, currently in Beta.
tags:
  - databricks
  - cli
  - machine-learning
  - devops
timestamp: "2026-06-19T08:56:26.291Z"
---

# AI Runtime CLI (Databricks)

**AI Runtime CLI** is a command-line tool for Databricks that enables users to submit, monitor, and manage training workloads on serverless GPU infrastructure. It is currently in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Overview

The AI Runtime CLI allows data scientists and ML engineers to run training jobs without manually provisioning clusters or managing infrastructure. Workloads are defined in YAML configuration files and submitted via the `air` command. The CLI handles code upload, dependency installation, job submission, and log streaming. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Installation and Authentication

Before using the CLI, users must install it and configure authentication. See the [installation guide](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation) for detailed instructions. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Workflow

### Step 1: Write a YAML Config

Create a YAML file (e.g., `train.yaml`) that describes the workload. The minimal configuration requires three fields: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

To run custom training code, add an `environment` block for Python dependencies and a `code_source` block to upload local code: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-first-air-run
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
code_source:
  type: snapshot
  snapshot:
    root_path: .
command: python $CODE_SOURCE_PATH/train.py
```

The `$CODE_SOURCE_PATH` variable resolves to the uploaded code location on the remote node. Databricks recommends using this variable rather than hardcoding paths. The `environment.version` field selects the serverless GPU environment version (defaults to `'4'`). ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Step 2: Submit the Run

Submit the workload using: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml
```

The CLI uploads local code (if configured), submits the job, and prints a run ID. To watch logs until completion, add the `--watch` flag: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml --watch
```

Each submission creates a run in the [MLflow](/concepts/mlflow.md) experiment specified in `experiment_name`. The run captures metrics, parameters, artifacts, and logs, all viewable in the workspace MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Step 3: Inspect the Run

Check run status: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air status <run-id>
```

Stream or download logs: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air logs <run-id>
air logs <run-id> --node 2
air logs <run-id> --download-to ./logs/
```

For distributed workloads running across multiple nodes, use `--node` to specify which node's logs to view. Use `--download-to` to write logs to a local directory. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

List recent runs: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air list runs --limit 10
air list runs --active
```

Cancel a run: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air cancel <run-id>
```

## Common Patterns

**Override YAML fields from the command line:** ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120
```

**Validate the config without submitting:** ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml --dry-run
```

**Make a submission safely retryable:** ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml --idempotency-key my-unique-key
```

If the same key has been used before, the existing run is returned instead of creating a new one. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Experiment tracking and run management
- [Serverless GPU Infrastructure](/concepts/serverless-gpu-infrastructure.md) — The underlying compute platform
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-node workload support
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built ML environments

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
