---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81694239be884045ba4eedfc6f6379301d1c621a58bde42ae8e393a8e7b4dced
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-get-run-and-air-list-runs-commands
    - air list runs commands and air get run
    - AGRAALRC
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: air get run and air list runs commands
description: Commands to query run metadata, status, and configuration, with filtering options like --limit and --active
tags:
  - cli
  - monitoring
  - workload-management
timestamp: "2026-06-19T17:29:38.168Z"
---

# `air get run` and `air list runs` commands

The `air get run` and `air list runs` commands are subcommands of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) that allow you to inspect the status, metadata, and history of workloads submitted via the `air` CLI. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

## `air get run`

Show metadata, status, and configuration for a specific run. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

## `air list runs`

List recent runs. The `--limit` flag bounds the result count, and the `--active` flag shows only running workloads. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

---

## Global flags

Both commands accept the global flags defined for the AI Runtime CLI: ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

| Flag | Purpose |
|------|---------|
| `--version` | Print the installed CLI version. |
| `-p`, `--profile` | Use the named Databricks CLI authentication profile instead of the default. |
| `-h`, `--help` | Show help. When followed by a config path (`-h config.compute`), show YAML field help. |

---

## Related concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Overview of the CLI and its installation
- [air run command](/concepts/air-run-command.md) – Submit a workload defined by a YAML file
- [air logs command](/concepts/air-logs-command.md) – Stream or download logs for a run
- [air cancel command](/concepts/air-cancel-command.md) – Cancel a running workload
- Track runs with MLflow and the Jobs run page – View run details in the Databricks UI

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
