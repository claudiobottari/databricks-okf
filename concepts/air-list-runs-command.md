---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bbfc7f42a77a7ef40a7d1dad5feafd5c325de264af4e34bc77ad6d65463e001
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-list-runs-command
    - ALRC
    - air list runs
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: air list runs command
description: Lists recent AI Runtime runs with optional filters for result count and active-only status.
tags:
  - cli
  - command
  - listing
timestamp: "2026-06-19T08:55:24.157Z"
---

# `air list runs` Command

The **`air list runs`** command is a subcommand of the [AI Runtime CLI (Beta)](/concepts/ai-runtime-cli.md) that lists recent AI Runtime workloads submitted via the `air` CLI. It provides a quick way to view the history of runs and to filter only currently active workloads. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Usage

```
air list runs [--limit <count>] [--active] [global flags]
```

Run `air list runs --help` from the terminal for the most up‑to‑date flags. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Flags

| Flag | Purpose |
|------|---------|
| `--limit <count>` | Restrict the number of runs returned (e.g., `--limit 10`). ^[ai-runtime-cli-command-reference-databricks-on-aws.md] |
| `--active` | Display only runs that are currently running. ^[ai-runtime-cli-command-reference-databricks-on-aws.md] |

In addition, the command accepts the global flags available to the `air` CLI: ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

| Global Flag | Purpose |
|-------------|---------|
| `--version` | Print the installed CLI version. |
| `-p`, `--profile` | Use a named Databricks CLI authentication profile instead of the default. |
| `-h`, `--help` | Show help for any subcommand. |

## Examples

List the ten most recent runs (default behavior without `--limit` may vary):

```bash
air list runs --limit 10
```

Show only workloads that are still running:

```bash
air list runs --active
```

## Related Commands

- [air run command](/concepts/air-run-command.md) – Submit a new workload.
- [air get run command](/concepts/air-get-run-command.md) – Show detailed metadata for a specific run.
- [air logs command](/concepts/air-logs-command.md) – Stream or download logs for a run.
- [air cancel command](/concepts/air-cancel-command.md) – Cancel a running workload.

## Related Concepts

- [AI Runtime (Preview)](/concepts/ai-runtime.md) – The underlying runtime for running ML workloads.
- AI Runtime CLI quickstart – Getting started guide.
- Track runs with MLflow and the Jobs run page – How runs are logged and monitored.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment tracking integration.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
