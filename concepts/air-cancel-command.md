---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c55eece58d427075d6e948faacd4cecdec1799ca7687daaba998c9dd0feb7322
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-cancel-command
    - ACC
    - air cancel
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: air cancel command
description: Cancels a running workload, enabling lifecycle management of submitted jobs
tags:
  - cli
  - workload-management
timestamp: "2026-06-19T17:30:06.941Z"
---

Here is the wiki page for the "air cancel command" based on the provided source material.

---

The `air cancel` command cancels a currently running workload submitted via the AI Runtime CLI. It is part of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (Beta), which provides a command-line interface for managing AI workloads on Databricks. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Syntax

```bash
air cancel
```
^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Description

The command stops a running workload that was started with `air run`. This is useful for terminating workloads that are no longer needed, are taking too long, or require a restart with updated configuration. The command does not require additional flags beyond the global options. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related Commands

The `air cancel` command is one of several run management subcommands in the AI Runtime CLI:

- `air run` — Submit a workload defined by a YAML file
- `air get run` — Show metadata, status, and configuration for a specific run
- `air list runs` — List recent runs
- `air logs` — Stream or download logs for a run

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Global Flags

The `air cancel` command accepts the following global flags:

| Flag | Purpose |
|------|---------|
| `--version` | Print the installed CLI version |
| `-p`, `--profile` | Use the named Databricks CLI authentication profile instead of the default |
| `-h`, `--help` | Show help for the command |

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## See Also

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — Overview of the CLI tool
- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md) — Full list of available commands
- AI Runtime CLI quickstart — Getting started guide
- [air run command](/concepts/air-run-command.md) — Submitting workloads to AI Runtime
- [air get run command](/concepts/air-get-run-command.md) — Viewing run metadata and status
- [air list runs command](/concepts/air-list-runs-command.md) — Listing recent runs
- Track runs with MLflow and the Jobs run page — Monitoring and tracking submitted runs

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
