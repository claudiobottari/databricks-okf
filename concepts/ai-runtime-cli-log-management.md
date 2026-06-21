---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7e7fa13842acd466990725e100a0b66de4ef7c383e154b0bf2e3473f49acfc3
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-log-management
    - ARCLM
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: AI Runtime CLI Log Management
description: Commands and patterns for streaming, filtering by node, downloading to local directory, and inspecting logs from AI Runtime training runs.
tags:
  - databricks
  - logging
  - cli
timestamp: "2026-06-19T22:03:34.570Z"
---

# AI Runtime CLI Log Management

**AI Runtime CLI Log Management** refers to the commands and options available in the [AI Runtime CLI](/concepts/ai-runtime-cli.md) for streaming, downloading, and inspecting logs from training jobs submitted via the `air` command‑line tool. Logs are captured both in [MLflow](/concepts/mlflow.md) and as raw output from the job, and the CLI provides several ways to access them outside the MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## The `air logs` Command

The primary tool for retrieving logs is `air logs`, which accepts a run ID and optionally a node index or a download destination. The basic usage is:

```
air logs <run-id>
```

This streams the log output from the job’s default node (node 0) directly to the terminal. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Options

- **`--node <node>`** – View logs from a specific compute node in a distributed workload. Distributed jobs run across multiple nodes; by default, only node 0’s logs are shown. Use this flag to inspect other nodes. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]
- **`--download-to <directory>`** – Write the logs to a local directory instead of streaming them to the terminal. This is useful for preserving logs for offline analysis or debugging. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Example Usage

```bash
# Stream logs from node 0 (default)
air logs 1234567

# Stream logs from node 2
air logs 1234567 --node 2

# Download all logs for a run to a local folder
air logs 1234567 --download-to ./logs/
```

## Viewing Logs While a Job Runs

In addition to the `air logs` command, you can watch logs **during** submission by adding the `--watch` flag to the `air run` command. This streams logs to the terminal until the job completes. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```
air run --file train.yaml --watch
```

After the job completes, you can still retrieve logs with `air logs` as described above.

## Log Storage in MLflow

Every run submitted via the AI Runtime CLI is automatically tracked in an [MLflow Experiment](/concepts/mlflow-experiment.md). The run’s metrics, parameters, artifacts, and logs are all captured in the [MLflow Run](/concepts/mlflow-run.md) and can be viewed in the Databricks workspace MLflow UI. This provides a persistent, queryable record of log output alongside other run metadata. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Commands for Run Inspection

- `air list runs` – Lists recent runs; can be filtered with `--active` or `--limit`. Useful for finding the run ID needed for `air logs`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]
- `air cancel` – Cancels a running job (log output is still available for the portion that ran). ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Best Practices

- Use `--download-to` for long‑running or distributed jobs so you can inspect logs offline without keeping a terminal open.
- Use `--node` to isolate issues on a specific compute node in a [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) workload.
- Combine `air logs` with the MLflow UI for a complete view: the CLI gives raw output, while MLflow preserves the full history with search and comparison capabilities.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The parent tool that provides log management.
- [MLflow](/concepts/mlflow.md) – Tracking system that also stores logs.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Config syntax for setting up training jobs.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Jobs that produce logs across multiple nodes.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The compute infrastructure used by AI Runtime CLI.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
