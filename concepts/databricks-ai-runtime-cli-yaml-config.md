---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4570ac38bc09044513865853fc1a65ed490f356a958a8d3ba854705b66e5bc7b
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-cli-yaml-config
    - DARCYC
    - AI Runtime YAML Config
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: Databricks AI Runtime CLI YAML config
description: The YAML-based configuration system used by the air CLI to define workload specifications, with field-level help accessible via '-h config'.
tags:
  - configuration
  - yaml
  - databricks
timestamp: "2026-06-19T22:01:39.782Z"
---

# Databricks AI Runtime CLI YAML Config

The **Databricks AI Runtime CLI YAML config** is a file-based configuration used to define and submit workloads via the `air run` command. The `air` CLI accepts a YAML file that describes the workload specification, including compute resources, environment settings, and the command to execute. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Getting Help for YAML Config

The `air` CLI provides built-in help for the YAML configuration schema:

- `air -h config` displays the full YAML config reference, listing all supported top-level fields and their types. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]
- `air -h config.compute` shows per‑field help for the `compute` section (e.g., node type, number of GPUs). ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

Because the CLI help reflects the exact installed version, it is the authoritative source of field‑level information. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Usage

The primary command that consumes the YAML file is:

```
air run --file <path-to-yaml>
```

Additional flags such as `--watch`, `--dry-run`, `--override`, `--idempotency-key`, and `--email` can be used alongside `--file`. For a complete list of `air run` options, see the [AI Runtime CLI Command Reference](/concepts/ai-runtime-cli-commands.md). ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

The full YAML specification is documented separately in the [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config) (linked from the CLI command reference page). ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Overview of the CLI tool.
- [AI Runtime CLI Commands](/concepts/ai-runtime-cli-commands.md) – All subcommands (`run`, `get run`, `list runs`, `logs`, `cancel`).
- AI Runtime CLI Quickstart – Step‑by‑step guide to create and run a YAML‑based workload.
- Track Runs with MLflow and the Jobs Run Page – How to monitor YAML‑defined runs.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
