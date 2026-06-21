---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b20d81d2348773f8bd1b82b7a0d2113d63c02a03b6fa907e63d858f0473c8a1
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-run-run-management-commands
    - AR-RMC
title: air run - Run management commands
description: Commands for inspecting, listing, canceling, and retrieving logs from AI Runtime runs, including 'air get run', 'air list runs', 'air logs', and 'air cancel'.
tags:
  - cli
  - monitoring
  - databricks
timestamp: "2026-06-19T22:01:31.131Z"
---

# air run - Run management commands

The **`air run`** command is a subcommand of the AI Runtime CLI (`air`) that submits a workload defined by a YAML configuration file. It is part of the [`air` CLI tool](https://docs.datatbricks.com/aws/en/machine-learning/ai-runtime/cli/) for managing machine learning workloads on Databricks.

## Usage

```
air run [flags]
```

## Flags

| Flag | Short | Purpose |
|------|-------|---------|
| `--file` | `-f` | Specify the YAML file that defines the workload configuration. |
| `--watch` | `-w` | Stream logs and monitor the run in real-time after submission. |
| `--dry-run` | `-d` | Validate the YAML configuration without actually submitting the workload. |
| `--override` | `-o` | Override specific fields in the YAML configuration (e.g., `--override compute.num_gpus=4`). |
| `--idempotency-key` | `-i` | Provide a unique key to ensure idempotent submissions. If a run was previously submitted with the same key, it will not be resubmitted. |
| `--email` | `-e` | Specify an email address to receive notifications about the run status. |
| `--profile` | `-p` | Select a Databricks CLI authentication profile to use instead of the default. |

## Examples

### Submit a basic workload

```bash
air run --file my_workload.yaml
```

### Submit and watch logs

```bash
air run --file my_workload.yaml --watch
```

### Validate configuration without running

```bash
air run --file my_workload.yaml --dry-run
```

### Override a compute parameter

```bash
air run --file my_workload.yaml --override compute.num_gpus=8
```

### Use an idempotency key to prevent duplicate submissions

```bash
air run --file my_workload.yaml --idempotency-key "my-unique-key-123"
```

### Specify a non-default authentication profile

```bash
air run --file my_workload.yaml --profile production
```

## Related Commands

The `air run` command is part of a suite of run management commands:

- **`air get run`** — Show metadata, status, and configuration for a specific run.
- **`air list runs`** — List recent runs. Use `--limit` to bound the result count and `--active` to show only running workloads.
- **`air logs`** — Stream or download logs for a run. Use `--node` to target a specific node and `--download-to` to write logs to a directory.
- **`air cancel`** — Cancel a running workload.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The CLI tool that provides the `air run` command.
- [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) — The YAML file format used to define workloads with `air run`.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — How runs submitted via `air run` are tracked.
- [Databricks CLI authentication profiles](/concepts/databricks-authentication-type.md) — How to configure and select authentication profiles for `air run`.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md
