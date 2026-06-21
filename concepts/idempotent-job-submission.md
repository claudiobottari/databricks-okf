---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8dfad12c6081bae837f877e300d614b52f41642d70d0c6f57a32d7522b74114c
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-job-submission
    - IJS
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Idempotent Job Submission
description: Pattern using --idempotency-key to make job submission safely retryable, returning the existing run if the same key was used before.
tags:
  - reliability
  - job-submission
  - pattern
timestamp: "2026-06-19T17:30:44.194Z"
---

# Idempotent Job Submission

**Idempotent job submission** is a feature of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) that allows a workload to be submitted safely multiple times without creating duplicate runs. By providing an idempotency key with the `air run` command, the CLI ensures that if the same key was used in a previous submission, the existing run is returned instead of creating a new one. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## How It Works

The idempotency key is an arbitrary string passed via the `--idempotency-key` flag on `air run`. The CLI stores the mapping between the key and the created run. On subsequent submissions with the same key, the CLI returns the original run metadata and does not launch a new workload. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Usage

```bash
air run --file train.yaml --idempotency-key my-unique-key
```

If a workload with the key `my-unique-key` already exists, the command returns the existing run rather than creating a duplicate. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Best Practices

- Choose a key that uniquely identifies the logical submission, such as a hash of the [Workload YAML reference|YAML configuration](/concepts/workload-yaml-configuration.md) combined with a timestamp or run identifier.
- Use idempotency keys in automation scripts or CI/CD pipelines where network interruptions or timeouts might cause duplicate `air run` calls.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool that provides the `air run` command.
- [air run command](/concepts/air-run-command.md) — The subcommand that accepts `--idempotency-key` and other flags.
- Workload YAML reference — The configuration format for defining workloads.
- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md) — Complete list of commands and flags.
- [AI Runtime CLI global flags](/concepts/ai-runtime-cli-global-flags.md) — Shared flags like `--profile` and `--help`.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
