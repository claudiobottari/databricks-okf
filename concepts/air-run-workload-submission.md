---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7488eb096e5baec752cbbd7cc4721b775798baa5a7830ab9c1a0eb6196035572
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - air-run-workload-submission
    - AR-WS
    - AWS
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: air run - Workload submission
description: The primary CLI command for submitting AI workloads defined by YAML configuration files to Databricks AI Runtime.
tags:
  - cli
  - workloads
  - databricks
timestamp: "2026-06-19T22:01:17.233Z"
---

# air run – Workload submission

The `air run` command is part of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (Beta). Its purpose is to **submit a workload defined by a YAML file**. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Flags

The command supports the following flags: `--file`, `--watch`, `--dry-run`, `--override`, `--idempotency-key`, `--email`, and `--profile` (which selects an authentication profile). ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related commands

- [air get run](/concepts/air-get-run-command.md) – Show metadata, status, and configuration for a specific run.
- [air list runs](/concepts/air-list-runs-command.md) – List recent runs (supports `--limit` and `--active`).
- [air logs](/concepts/air-logs-command.md) – Stream or download logs (supports `--node` and `--download-to`).
- [air cancel](/concepts/air-cancel-command.md) – Cancel a running workload.

## Related concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface for AI Runtime workloads.
- Workload YAML reference – Reference for the YAML configuration file used by `air run`.
- Track runs with MLflow and the Jobs run page – How runs are tracked after submission.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
