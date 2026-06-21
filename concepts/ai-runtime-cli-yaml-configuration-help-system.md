---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc5a718489d5e1fcaebea51050badad6929823a61354f2dbf03a2cb7aec00014
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-command-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-yaml-configuration-help-system
    - ARCYCHS
    - AI Runtime CLI YAML Configuration
  citations:
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: AI Runtime CLI YAML configuration help system
description: Built-in help system that provides per-field documentation for YAML configuration sections via 'air -h config' and 'air -h config.compute'.
tags:
  - cli
  - configuration
  - documentation
timestamp: "2026-06-19T13:56:05.635Z"
---

# AI Runtime CLI YAML Configuration Help System

The **AI Runtime CLI YAML configuration help system** is a built-in documentation feature of the `air` CLI that provides per-field help for YAML configuration files used to define workloads. It allows users to explore available configuration options directly from the command line without consulting external documentation.

## Overview

The `air` CLI includes a hierarchical help system that documents the structure and fields of YAML configuration files used with the `air run` command. This system is accessible through the `-h` flag and supports drilling down into specific sections of the configuration. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Accessing YAML Configuration Help

### Top-Level Configuration Reference

To view the complete YAML configuration reference, use the `-h` flag with the `config` keyword:

```bash
air -h config
```

This displays all top-level sections and fields available in the YAML configuration file. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

### Per-Field Help

The help system supports drilling into specific sections of the YAML configuration. To view help for a particular section, append the section path to the `config` keyword:

```bash
air -h config.compute
```

This shows detailed documentation for the `compute` section of the YAML configuration, including all available fields, their types, and descriptions. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Key Features

- **Hierarchical navigation**: Users can explore configuration options at any level of nesting by specifying the dot-separated path to the section.
- **Version-specific documentation**: The help output reflects the exact version of the CLI installed, ensuring accuracy.
- **Command-level help**: The `--help` flag on any `air` command also provides relevant YAML configuration information. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related Commands

The YAML configuration help system is most relevant when using the `air run` command, which submits workloads defined by YAML files. Other commands that interact with runs include:

- `air get run` — Show metadata, status, and configuration for a specific run.
- `air list runs` — List recent runs.
- `air logs` — Stream or download logs for a run.
- `air cancel` — Cancel a running workload.

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Best Practices

- Use `air -h config` to get an overview of all available configuration sections before writing a YAML file.
- Use `air -h config.<section>` to explore specific sections in detail while authoring configuration files.
- Remember that the CLI help is the source of truth for the installed version — it takes precedence over external documentation if discrepancies exist. ^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for managing AI workloads.
- AI Runtime CLI Quickstart — Getting started guide for the `air` CLI.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) — Complete documentation of YAML configuration options.
- Track Runs with MLflow and the Jobs Run Page — Monitoring and tracking submitted workloads.

## Sources

- ai-runtime-cli-command-reference-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
