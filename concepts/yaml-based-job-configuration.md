---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3abe8f9d24a400455d20f8afa217b6c80109ee76285502699ebaff4691650bc1
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - yaml-based-job-configuration
    - YJC
    - YAML Job Configuration
    - YAML configuration files
    - configure-job
    - configuring jobs
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: YAML-based job configuration
description: Declarative approach to defining training jobs using YAML configuration files that can be checked into source control.
tags:
  - yaml
  - configuration
  - job-definition
timestamp: "2026-06-19T17:30:11.877Z"
---

# YAML-based Job Configuration

**YAML-based job configuration** refers to the mechanism provided by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) for defining distributed training workloads on [AI Runtime](/concepts/ai-runtime.md) in a declarative, human-readable format. Instead of writing notebook code, users describe their job parameters—such as the command to run, number of GPUs, and environment settings—in a YAML file that can be tracked in version control. ^[ai-runtime-cli-databricks-on-aws.md]

## Purpose

The YAML configuration allows developers to submit GPU training workloads directly from their laptop or code editor without opening a notebook. By defining training jobs declaratively in YAML, teams can check these configurations into source control, enabling reproducible and auditable workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Integration

The AI Runtime CLI uses YAML-based job configuration in combination with [MLflow](/concepts/mlflow.md) for experiment tracking. It also supports both workspace-based and git-based code workflows, giving teams flexibility in how they manage training code. ^[ai-runtime-cli-databricks-on-aws.md]

## Benefits

- **Declarative**: Job specifications are written as data, not code, making them easy to read and modify.
- **Version‑controllable**: YAML files can be committed to git repositories alongside code, ensuring that job definitions are tracked and reviewed.
- **Portable**: The same YAML configuration can be reused across different environments or runs without modification.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line tool that interprets YAML configurations and submits workloads.
- [AI Runtime](/concepts/ai-runtime.md) – The on-demand serverless GPU compute platform on Databricks.
- [MLflow](/concepts/mlflow.md) – Integrated experiment tracking for training runs submitted via the CLI.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Detailed schema for all supported fields in the job configuration.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
