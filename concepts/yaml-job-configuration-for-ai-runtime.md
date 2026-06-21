---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c424848a35a28afa54fc055fe35b5435c1e2eb8340979ea25a3baee43e7be94
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - yaml-job-configuration-for-ai-runtime
    - YJCFAR
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: YAML Job Configuration for AI Runtime
description: The declarative YAML-based job configuration format used by the AI Runtime CLI to define training jobs that can be checked into source control.
tags:
  - yaml
  - configuration
  - databricks
timestamp: "2026-06-19T08:55:54.187Z"
---

# YAML Job Configuration for AI Runtime

**YAML Job Configuration for AI Runtime** is a declarative format used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) to define and submit distributed training workloads on Databricks' serverless GPU compute platform. Jobs are defined in YAML files that can be checked into source control, enabling reproducible and version-controlled training workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Overview

The AI Runtime CLI (`air`) uses YAML-based job configuration to define training workloads. This approach allows users to submit GPU training workloads from their laptop and code editor without opening a notebook, and to define training jobs declaratively so they can be checked into source control. ^[ai-runtime-cli-databricks-on-aws.md]

The YAML configuration integrates with [MLflow](/concepts/mlflow.md) for experiment tracking and supports both workspace-based and git-based code workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Key Benefits

- **Declarative configuration**: Training jobs are defined in YAML files, making them reproducible and version-controllable.
- **No notebook required**: Submit GPU training workloads directly from your laptop and code editor.
- **Integration with MLflow**: Automatic tracking of runs and experiments.
- **Flexible code sources**: Support for both workspace-based and git-based code workflows.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The `air` command-line interface that consumes YAML job configurations
- [AI Runtime](/concepts/ai-runtime.md) – The on-demand serverless GPU compute platform
- [MLflow](/concepts/mlflow.md) – Experiment tracking and run management
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Multi-GPU workload execution
- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md)
- [AI Runtime CLI examples](/concepts/ai-runtime-cli.md)

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
