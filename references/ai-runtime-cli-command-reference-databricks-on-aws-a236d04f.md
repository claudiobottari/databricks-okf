---
title: AI Runtime CLI command reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/command-reference
ingestedAt: "2026-06-18T08:08:05.093Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Machine learning](https://docs.databricks.com/aws/en/machine-learning/)
*   [Train models](https://docs.databricks.com/aws/en/machine-learning/train-model/)
*   [AI Runtime (Preview)](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/)
*   [AI Runtime CLI (Beta)](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/)
*   Command reference

Last updated on **Jun 12, 2026**

Beta

The AI Runtime CLI is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This page lists the subcommands accepted by the `air` CLI. The same information is always available from the CLI itself:

Bash

    air --help              # All commandsair <command> --help    # Flags for a specific commandair -h config           # YAML config referenceair -h config.compute   # Per-field help for a YAML section

The CLI help reflects the exact version you have installed, so it is the source of truth if it differs from the table below.

## Commands[​](#commands "Direct link to Commands")

Command

Purpose

`air run`

Submit a workload defined by a YAML file. Supports `--file`, `--watch`, `--dry-run`, `--override`, `--idempotency-key`, `--email`, and `-p` to select an authentication profile.

`air get run`

Show metadata, status, and configuration for a specific run.

`air list runs`

List recent runs. Use `--limit` to bound the result count and `--active` to show only running workloads.

`air logs`

Stream or download logs for a run. Use `--node` to target a specific node and `--download-to` to write logs to a directory.

`air cancel`

Cancel a running workload.

## Global flags[​](#global-flags "Direct link to Global flags")

Flag

Purpose

`--version`

Print the installed CLI version.

`-p`, `--profile`

Use the named Databricks CLI authentication profile instead of the default.

`-h`, `--help`

Show help. When followed by a config path (`-h config.compute`), show YAML field help.

## See also[​](#see-also "Direct link to See also")

*   [AI Runtime CLI quickstart](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart)
*   [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config)
*   [Track runs with MLflow and the Jobs run page](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/track-runs)
