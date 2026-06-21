---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 756717bee16179ee9bc05acd22418d1786d24494a2cf3da6a72bcf583462a9c3
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-get-run-air-list-runs-commands
    - AGR/ALRC
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: air get run / air list runs commands
description: Subcommands for querying run metadata, status, and configuration; list supports --limit and --active flags to filter results.
tags:
  - cli
  - commands
  - run-management
timestamp: "2026-06-19T13:55:51.596Z"
---

# `air get run` / `air list runs` Commands

The `air get run` and `air list runs` commands are subcommands of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) that allow users to inspect the status, metadata, and history of workloads submitted through the `air` CLI. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## `air get run`

Show the metadata, status, and configuration for a specific run. This command accepts the run identifier as its argument and returns a structured view of the workload’s current state, including its YAML configuration and any recent status transitions. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

**Basic usage:**

```bash
air get run <run-id>
```

## `air list runs`

List recent runs. By default, the command returns the most recent workloads. Use `--limit <N>` to bound the number of results returned. Use `--active` to filter the list to only running workloads. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

**Basic usage:**

```bash
air list runs               # Recent runs
air list runs --limit 5     # Last 5 runs
air list runs --active      # Only currently running runs
```

## Global Flags Relevant to These Commands

The following global flags apply to `air get run` and `air list runs` as well as all other `air` subcommands: ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

| Flag | Purpose |
|------|---------|
| `-p`, `--profile` | Use the named Databricks CLI authentication profile instead of the default. |
| `-h`, `--help` | Show help for the command. |

For the complete list of global flags, see the [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md).

## Related Subcommands

- [air run command](/concepts/air-run-command.md) — Submit a new workload defined by a YAML file.
- [air logs command](/concepts/air-logs-command.md) — Stream or download logs for a run.
- [air cancel command](/concepts/air-cancel-command.md) — Cancel a running workload.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
