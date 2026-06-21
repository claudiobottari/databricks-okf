---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 314ddd73118ecc0184989f0d0b8e130f3bcf1421313d7cd7126d0b3f9178bf70
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-run-submission-and-lifecycle
    - Lifecycle and AIR Run Submission
    - ARSAL
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: AIR Run Submission and Lifecycle
description: The workflow for submitting training runs via `air run`, including idempotency keys, dry-run validation, field overrides, and run lifecycle tracking (status, logs, cancellation).
tags:
  - databricks
  - cli
  - workflow
  - job-submission
timestamp: "2026-06-19T08:56:37.000Z"
---

# AIR Run Submission and Lifecycle

**AIR Run Submission and Lifecycle** refers to the process of configuring, submitting, monitoring, and managing training jobs using the [AI Runtime CLI](/concepts/ai-runtime-cli.md). The lifecycle begins with a YAML workload configuration, progresses through submission and tracking in [MLflow](/concepts/mlflow.md), and ends with either successful completion or cancellation.

## Configuration

Every AIR run starts with a YAML configuration file (e.g., `train.yaml`). The minimal configuration requires three fields:

- `experiment_name` – the MLflow experiment under which the run is tracked.
- `compute` – a block specifying the number and type of accelerators (e.g., `num_accelerators: 1`, `accelerator_type: GPU_1xA10`).
- `command` – the command to execute on the remote node. For code that lives only in the configuration, a simple `echo` command can be used without any local code.

To run custom training scripts, add an `environment` block listing Python dependencies and a `code_source` block to upload local code. The `environment.version` selects the serverless GPU environment version (optional, defaults to `'4'`). The `code_source.type` set to `snapshot` uploads the directory specified by `snapshot.root_path`. The placeholder `$CODE_SOURCE_PATH` resolves to the uploaded location. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

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

For the full field reference, see the Workload YAML reference. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Submission

Submit a run with:

```bash
air run --file train.yaml
```

The CLI uploads any configured code, submits the job, and prints a run ID. The run is created in the MLflow experiment named in `experiment_name`, capturing metrics, parameters, artifacts, and logs in the workspace MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

To stream logs to the terminal until completion, add `--watch`:

```bash
air run --file train.yaml --watch
```

For safe retries, supply an `--idempotency-key`. If the same key was used before, the existing run is returned instead of creating a new one. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Run Tracking

Each submission creates an [MLflow Run](/concepts/mlflow-run.md) within the experiment. The run page in the workspace UI provides clickable links to the experiment and the run. All standard MLflow entities (metrics, parameters, artifacts) are accessible via the UI or programmatically. Logs are also available outside MLflow through the `air logs` command. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Monitoring and Inspection

### Check Status

Use `air status <run-id>` to view the current status. The output includes links to the MLflow experiment and run. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### View Logs

```bash
air logs <run-id>              # streams logs from node 0
air logs <run-id> --node 2     # logs from a specific node
air logs <run-id> --download-to ./logs/   # download logs to a local directory
```

Distributed workloads run across multiple nodes; `--node` selects which node’s logs to stream. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### List Runs

```bash
air list runs --limit 10   # most recent runs
air list runs --active     # currently active runs
```

### Cancel a Run

```bash
air cancel <run-id>
```

## Common Patterns

- **Override YAML fields from the command line:** `air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120`
- **Validate config without submitting:** `air run --file train.yaml --dry-run`
- **Safe retries:** `air run --file train.yaml --idempotency-key my-unique-key` ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI Installation and Authentication](/concepts/ai-runtime-cli-installation-via-uv.md)
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md)
- Serverless GPU Environment Versions
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md)

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
