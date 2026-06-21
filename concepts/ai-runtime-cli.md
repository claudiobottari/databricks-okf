---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a786062b37c23d60c4c70bbce68e93ecb6057d9efa9560998d7c86194ed074af
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli
    - ARC
    - AI Runtime (air) CLI
    - AI Runtime CLI (Beta)
    - AI Runtime CLI examples
    - ai-runtime-cli-databricks
    - ARC(
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: AI Runtime CLI
description: A Databricks command-line interface for submitting, monitoring, and managing machine learning training workloads on serverless GPU infrastructure.
tags:
  - databricks
  - cli
  - machine-learning
timestamp: "2026-06-19T22:03:05.948Z"
---

```markdown
---
title: AI Runtime CLI
summary: A command-line tool for submitting and managing distributed ML training workloads on Databricks serverless GPU infrastructure, currently in Beta.
sources:
  - ai-runtime-cli-databricks-on-aws.md
  - ai-runtime-cli-quickstart-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - databricks
  - cli
  - machine-learning
  - training
aliases:
  - ai-runtime-cli
  - ARC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AI Runtime CLI

The **AI Runtime CLI** (`air`) is a command-line interface for submitting and managing distributed training workloads on [[AI Runtime]], the Databricks on-demand serverless GPU compute platform. It supports YAML-based job configuration, integrates with [[MLflow]], and enables workspace-based and git-based code workflows. The CLI is currently in Beta. ^[ai-runtime-cli-databricks-on-aws.md, ai-runtime-cli-quickstart-databricks-on-aws.md]

## When to use the CLI

Use the AI Runtime CLI when you want to submit GPU training workloads from your laptop and code editor without opening a notebook, or define training jobs declaratively in YAML so they can be checked into source control. For the in-notebook Python API (`@distributed` and `@ray_launch`), see Multi-GPU workload instead. ^[ai-runtime-cli-databricks-on-aws.md]

## Quickstart

Before starting, [install the CLI and configure authentication](installation.md). ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Step 1: Write a YAML config

Create a `train.yaml` file describing the workload. The minimum configuration requires an experiment name, a compute spec, and a command. The following example runs without any local code, so you can submit your first run immediately: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

To run a local training script, add an `environment` block listing Python dependencies and a `code_source` block that uploads your local code: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

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

This configuration installs the listed dependencies, uploads the current directory (`root_path: .`), and runs `train.py` on a single A10 GPU. The `$CODE_SOURCE_PATH` environment variable resolves to the uploaded code location on the remote node — use it instead of hardcoding a path. The `environment.version` field selects the serverless GPU environment version and is optional (defaults to `'4'`). For all available versions, see [[Serverless Environment Versioning|Serverless environment versions]]. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

For the full field reference, see Workload YAML reference. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Step 2: Submit the run

Submit the workload with the `air run` command: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml
```

The CLI uploads your local code (if a `code_source` is configured), submits the job, and prints a run ID. Use this ID to inspect, watch, and cancel the run later. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The submission creates a run in the MLflow experiment named in `experiment_name` (an experiment can hold many runs). That run captures the workload's metrics, parameters, artifacts, and logs, all viewable in the workspace [[MLflow|MLflow UI]]. Logs are also available outside MLflow: stream them to your terminal or a file, or download them later with `air logs`. To watch logs until completion, add `--watch`: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml --watch
```

### Step 3: Inspect the run

Check the status of a run: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air status <run-id>
```

The output includes clickable links to the run's MLflow experiment and [[mlflow-run|MLflow Run]] in the workspace UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Stream or download logs: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air logs <run-id>
air logs <run-id> --node 2
air logs <run-id> --download-to ./logs/
```

Distributed workloads run across multiple nodes. By default, `air logs` streams from node 0. To view logs from a specific node, pass `--node`. Use `--download-to` to write logs to a local directory instead of streaming. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

List recent runs: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air list runs --limit 10
air list runs --active
```

Cancel a run: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air cancel <run-id>
```

## Common patterns

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

## Integration

The CLI uses YAML-based job configuration, integrates with [[MLflow]], and supports workspace-based and git-based code workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Related concepts

- [[AI Runtime]] — The serverless GPU compute platform
- [[AI Runtime CLI Installation via uv|AI Runtime CLI installation]] — How to install and configure the CLI
- [[AI Runtime CLI Commands|AI Runtime CLI command reference]] — Full documentation for `air` commands
- Workload YAML reference — YAML schema for training job definitions
- Track runs with MLflow and the Jobs run page — How runs are monitored
- [[AI Runtime CLI|AI Runtime CLI examples]] — Example configurations and commands
- Multi-GPU workload — The in-notebook Python API alternative
- [[MLflow]] — Experiment tracking integration
- [[Serverless Environment Versioning|Serverless environment versions]] — Available environment versions for GPU compute

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md
```

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
2. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
