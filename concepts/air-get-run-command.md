---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3a2e7f452946fb482905327f875505bfdf3391e63aaf436bbcf007830378672
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-get-run-command
    - AGRC
    - air get run
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: air get run command
description: Displays metadata, status, and configuration details for a specific AI Runtime run.
tags:
  - cli
  - command
  - monitoring
timestamp: "2026-06-19T08:55:12.601Z"
---

# air get run command

The **`air get run` command** is a subcommand of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) that displays metadata, status, and configuration for a specific run. It is used to inspect the details of a previously submitted workload.

## Overview

`air get run` retrieves and prints information about a single AI Runtime run, including its current state (e.g., running, completed, failed), the YAML configuration that defined the workload, and other associated metadata. This command is useful for checking the progress or outcome of a workload after it has been submitted with `air run`.^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Usage

```
air get run <run-id>
```

- `<run-id>` – The identifier of the run to inspect. The run ID is returned when the workload is submitted with `air run`, or it can be found using [air list runs command](/concepts/air-list-runs-command.md).

The command outputs a structured summary of the run. The exact format is determined by the CLI version and may include fields such as status, submission timestamp, and the resolved YAML configuration. No additional flags are documented for this command in the source material.^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## See also

- [air run command](/concepts/air-run-command.md) – Submit a workload defined by a YAML file.
- [air list runs command](/concepts/air-list-runs-command.md) – List recent runs.
- [air logs command](/concepts/air-logs-command.md) – Stream or download logs for a run.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Overview and global flags.
- AI Runtime CLI quickstart – Getting started guide.
- Workload YAML reference – Field reference for the YAML configuration.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
