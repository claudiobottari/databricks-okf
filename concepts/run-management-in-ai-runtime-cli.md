---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42518dda5f43d3f3867c67d97ded8d39565d0a4e3ea64545fb6b9ce5fa9abebd
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - run-management-in-ai-runtime-cli
    - RMIARC
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Run management in AI Runtime CLI
description: Commands for listing, inspecting status, and cancelling runs using air list runs and air cancel commands, with filtering options like --active and --limit.
tags:
  - databricks
  - cli
  - run-management
timestamp: "2026-06-19T13:56:57.634Z"
---

# Run Management in AI Runtime CLI

**Run management in AI Runtime CLI** refers to the lifecycle of training and evaluation jobs submitted through the `air` command-line tool. The CLI supports submitting, inspecting, streaming logs for, listing, and cancelling runs. All runs are tracked in [MLflow](/concepts/mlflow.md) experiments, making metrics, parameters, and artifacts accessible from the Databricks workspace UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Submitting a Run

To submit a run, create a YAML configuration file that describes the workload and then use the `air run` command. The minimal config requires an `experiment_name`, a `compute` block specifying the number and type of accelerators, and a `command`. For example: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

To run a local training script, add an `environment` block with Python dependencies and a `code_source` block that uploads code. The placeholder `$CODE_SOURCE_PATH` resolves to the uploaded code location on the remote node. Databricks recommends using this variable rather than hardcoding a path. The `environment.version` field selects the serverless GPU environment version (defaults to `'4'`). ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Submit the workload with:

```bash
air run --file train.yaml
```

The CLI uploads code (if configured), submits the job, and prints a run ID. The submission creates a run in the MLflow experiment named in `experiment_name`. The run captures metrics, parameters, artifacts, and logs, viewable in the MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

To watch logs until completion, use `--watch`:

```bash
air run --file train.yaml --watch
```

## Inspecting Runs

Check run status and get clickable links to the MLflow experiment and run in the workspace UI by using `air list runs`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Stream or download logs:

```bash
air logs <run-id>
air logs <run-id> --node 2
air logs <run-id> --download-to ./logs/
```

Distributed workloads run across multiple nodes. By default, `air logs` streams from node 0. Use `--node` to target a specific node. Use `--download-to` to write logs to a local directory instead of streaming them to the terminal. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

List recent runs:

```bash
air list runs --limit 10
air list runs --active
```

## Cancelling a Run

Cancel a running job with:

```bash
air cancel <run-id>
```

## Common Patterns

- **Override YAML fields** from the command line without editing the config file:
  ```bash
  air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120
  ```

- **Validate the config** without submitting:
  ```bash
  air run --file train.yaml --dry-run
  ```

- **Make a submission safe to retry** with an idempotency key:
  ```bash
  air run --file train.yaml --idempotency-key my-unique-key
  ```
  If the same key has been used before, the existing run is returned instead of creating a new one. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI YAML Reference](/concepts/ai-runtime-cli-yaml-workload-definition.md) — Full field documentation for workload configuration.
- [AI Runtime CLI Command Reference](/concepts/ai-runtime-cli-commands.md) — Complete list of `air` commands and flags.
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — How runs are organized and logged.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying infrastructure that executes the runs.
- Distributed Training with AI Runtime — Patterns for multi-node training jobs.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
