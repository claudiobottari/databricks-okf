---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad5fa792b4547f56f8d0cf105acb2ed3e398a5dc4e3da0c10764c34c79240860
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-yaml-workload-definition
    - ARCYWD
    - AI Runtime CLI YAML Reference
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: AI Runtime CLI YAML workload definition
description: Workloads for the AI Runtime CLI are defined via YAML configuration files, with the CLI offering field-level help (-h config) and per-section help (-h config.compute) for authoring these files.
tags:
  - yaml
  - workload
  - configuration
timestamp: "2026-06-18T14:21:20.746Z"
---

# AI Runtime CLI YAML Workload Definition

**AI Runtime CLI YAML workload definition** refers to the configuration file format used by the `air` CLI to define and submit machine learning workloads to [AI Runtime](/concepts/ai-runtime.md). The YAML file specifies the compute resources, environment, source code, and execution parameters for a workload, which is then submitted using the `air run` command. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Overview

The AI Runtime CLI (`air`) accepts a YAML file that describes the complete workload configuration. This declarative approach allows users to define reproducible training, evaluation, or inference jobs without manually specifying command-line arguments for every parameter. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## YAML Configuration Structure

The YAML file is organized into sections that define different aspects of the workload. The CLI provides built-in help for the YAML schema: running `air -h config` displays the full configuration reference, and `air -h config.compute` shows per-field help for the compute section. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

### Key Sections

While the exact fields depend on the installed CLI version, the YAML configuration typically includes:

- **Compute** — Specifies the compute resources required, such as node type, number of workers, and cluster configuration.
- **Environment** — Defines the runtime environment, including Databricks Runtime version, libraries, and dependencies.
- **Source** — Points to the code to execute, which may be a notebook, Python script, or other executable.
- **Parameters** — Provides input parameters and arguments passed to the workload at runtime.

## Submitting a Workload

The primary command for submitting a YAML-defined workload is `air run`. This command accepts several flags that modify submission behavior: ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

| Flag | Purpose |
|------|---------|
| `--file` | Specifies the path to the YAML workload definition file |
| `--watch` | Streams logs and waits for the workload to complete |
| `--dry-run` | Validates the configuration without submitting the workload |
| `--override` | Overrides specific YAML fields from the command line |
| `--idempotency-key` | Ensures idempotent submission to prevent duplicate runs |
| `--email` | Sends an email notification when the run completes |
| `-p`, `--profile` | Selects a Databricks CLI authentication profile |

## Managing Workloads

After submission, workloads can be managed using other `air` commands that reference the run ID returned by `air run`: ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

- `air get run` — Displays metadata, status, and configuration for a specific run.
- `air list runs` — Lists recent runs, with `--limit` to bound results and `--active` to show only running workloads.
- `air logs` — Streams or downloads logs, with `--node` to target a specific node and `--download-to` to write logs to a directory.
- `air cancel` — Cancels a running workload.

## Best Practices

- **Use `--dry-run` first** to validate the YAML configuration before submitting a workload, catching errors early.
- **Specify an idempotency key** to prevent accidental duplicate submissions of the same workload.
- **Reference the CLI help** (`air -h config`) for the exact YAML schema supported by your installed version, as fields may vary between releases.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The execution environment for AI workloads
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for managing workloads
- Databricks Runtime — The runtime environment used by AI Runtime
- [MLflow Tracking](/concepts/mlflow-tracking.md) — For tracking runs and experiments alongside CLI submissions

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
