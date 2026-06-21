---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 707b8b7e5a5bbb00e3478aab468c0f49fd9ab6c3651989d01805a87d561ea9cc
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-logs-and-run-inspection
    - Run Inspection and AIR Logs
    - ALARI
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: AIR Logs and Run Inspection
description: "Commands and patterns for inspecting training runs: checking status, streaming/downloading logs (with per-node support), listing active/recent runs, and canceling runs."
tags:
  - databricks
  - logging
  - monitoring
  - debugging
timestamp: "2026-06-19T08:56:43.072Z"
---

# AIR Logs and Run Inspection

**AIR Logs and Run Inspection** refers to the set of commands and workflows for viewing, downloading, and managing the output of training jobs submitted with the AI Runtime (AIR) CLI. After submitting a workload, users can inspect its status, stream or retrieve log files, list recent or active runs, and cancel runs — all from the command line. Logs are also automatically captured in the experiment’s [MLflow](/concepts/mlflow.md) run, making them accessible via the Databricks workspace UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Overview

When a training run is submitted using `air run --file <config>` (optionally with `--watch`), the CLI prints a run ID. That ID is used for all subsequent inspection operations. The CLI can stream logs from a specific node, download logs to a local directory, list runs, and cancel runs. In addition, each run is recorded as an [MLflow Run](/concepts/mlflow-run.md) in the experiment named in the YAML config, and the CLI output includes clickable links to both the MLflow experiment and the [MLflow Run](/concepts/mlflow-run.md) in the workspace UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Commands for Run Inspection

### `air logs`

Streams or downloads logs for a submitted run. By default, logs are streamed from node 0. To change the node, use the `--node` flag. To save logs to a file instead of streaming to the terminal, use `--download-to`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
# Stream logs from node 0 (default)
air logs <run-id>

# Stream logs from a specific node
air logs <run-id> --node 2

# Download logs to a local directory
air logs <run-id> --download-to ./logs/
```

Distributed workloads run across multiple nodes. The `--node` flag allows targeting a specific node’s output, which is useful for debugging parallel tasks. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### `air list runs`

Lists recent or currently active runs. The `--limit` flag controls how many recent runs are shown. The `--active` flag filters to only those runs that are still running. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
# List the 10 most recent runs
air list runs --limit 10

# List all active runs
air list runs --active
```

### `air cancel`

Cancels a running run by its ID. This is useful for stopping a long-running or erroneous job without needing to navigate to the UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air cancel <run-id>
```

## Watching Logs During a Run

When submitting a run with `air run`, adding the `--watch` flag streams logs to the terminal until the run completes. This provides a real-time view of progress without a separate `air logs` call. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml --watch
```

## Viewing Logs in the MLflow UI

Every run created by the AIR CLI is automatically logged to the [MLflow Experiment](/concepts/mlflow-experiment.md) specified in the `train.yaml` config. The experiment captures metrics, parameters, artifacts, and logs. The run’s [MLflow Run](/concepts/mlflow-run.md) page in the Databricks workspace provides a graphical view of the same log data, making it convenient for browsing historical runs and comparing experiments. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Best Practices

- **Use the run ID** to inspect logs after submission. The ID is printed when the run is created and can be retrieved via `air list runs`.
- **For distributed jobs**, check logs from all nodes by running `air logs` multiple times with different `--node` values, or download all logs at once if needed.
- **Combine with `--watch`** during development to catch errors early without manual polling.
- **Use `--idempotency-key`** when submitting runs to make retries safe; if the same key is reused, the existing run’s logs and status are returned instead of creating a duplicate. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line tool for submitting and managing training jobs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The underlying system that stores run metadata, logs, and artifacts.
- AI Runtime CLI Quickstart – A step-by-step guide to using the CLI.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Full field reference for the configuration file.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
