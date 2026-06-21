---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b42bf8b3412b0d806680f89d57768e4d35c8ad88b07b5f045fd22a9bb4fee82
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-python-api
    - ARPA
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: AI Runtime Python API
description: The in-notebook Python API (`@distributed` and `@ray_launch`) for multi-GPU workload training, an alternative to the CLI.
tags:
  - python-api
  - distributed-training
  - databricks
timestamp: "2026-06-18T10:42:38.667Z"
---

# AI Runtime Python API

The **AI Runtime Python API** provides decorators and utilities for launching multi-GPU distributed training workloads directly from Databricks Notebooks. It is an alternative to the [AI Runtime CLI](/concepts/ai-runtime-cli.md) for users who prefer to work within a notebook environment. ^[ai-runtime-cli-databricks-on-aws.md]

## Overview

The AI Runtime Python API enables you to run distributed training jobs on [AI Runtime](/concepts/ai-runtime.md)'s serverless GPU infrastructure without leaving your notebook. The API provides decorators such as `@distributed` and `@ray_launch` that handle the complexity of distributing workloads across multiple GPUs. ^[ai-runtime-cli-databricks-on-aws.md]

This API is designed for users who want to:

- Submit GPU training workloads from within a Databricks Notebook
- Use Python decorators to define distributed training jobs
- Leverage existing notebook-based workflows without switching to a CLI

^[ai-runtime-cli-databricks-on-aws.md]

## Key Decorators

### `@distributed`

The `@distributed` decorator allows you to launch multi-GPU training jobs directly from a notebook cell. It handles the distribution of work across available GPU resources on AI Runtime. ^[ai-runtime-cli-databricks-on-aws.md]

### `@ray_launch`

The `@ray_launch` decorator provides integration with [Ray on Databricks](/concepts/ray-on-databricks.md), enabling you to launch Ray-based distributed training workloads on AI Runtime's serverless GPU infrastructure. ^[ai-runtime-cli-databricks-on-aws.md]

## Usage

The Python API is used within Databricks Notebooks. You apply the decorator to a function that contains your training logic, and the API handles provisioning GPU resources and distributing the workload. ^[ai-runtime-cli-databricks-on-aws.md]

For detailed usage examples and code samples, see the [Multi-GPU workload](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training) documentation. ^[ai-runtime-cli-databricks-on-aws.md]

## Comparison with AI Runtime CLI

| Aspect | Python API | AI Runtime CLI |
|---|---|---|
| Environment | Databricks Notebook | Terminal, CI/CD pipeline |
| Job definition | Python decorators | YAML configuration files |
| Workflow | Interactive notebook-based | Declarative, version-controlled |
| Best for | Exploratory development, rapid iteration | Production jobs, automation |

^[ai-runtime-cli-databricks-on-aws.md]

## Integration with MLflow

Workloads launched using the Python API automatically integrate with [MLflow Tracking](/concepts/mlflow-tracking.md) for experiment logging, metric tracking, and model artifact management. This provides visibility into training runs and facilitates model comparison and selection. ^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The serverless GPU compute platform
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — Command-line alternative for managing workloads
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking and model management
- [Ray on Databricks](/concepts/ray-on-databricks.md) — Distributed computing framework
- Databricks Notebooks — Interactive development environment
- [AI Governance with Unity Catalog](/concepts/ai-governance-with-unity-catalog.md) — Governance for AI assets

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
