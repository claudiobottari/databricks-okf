---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a772e091c1c02be3f9ac55c252cfc4bbba84a569788d0a01a1ce1e684edd7880
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-for-ai-runtime-cli
    - MIFARC
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: MLflow integration for AI Runtime CLI
description: Integration with MLflow to track and manage training runs submitted via the AI Runtime CLI.
tags:
  - mlflow
  - experiment-tracking
  - databricks
timestamp: "2026-06-19T17:30:16.510Z"
---

# MLflow Integration for AI Runtime CLI

The **MLflow integration for AI Runtime CLI** refers to the built-in support for tracking and managing distributed training runs using [MLflow](/concepts/mlflow.md) within the `air` command-line interface. The AI Runtime CLI submits and manages distributed training workloads on [AI Runtime](/concepts/ai-runtime.md), Databricks’ on‑demand serverless GPU compute platform. The CLI uses a YAML-based job configuration and supports both workspace-based and git-based code workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Tracking Runs

The CLI provides a dedicated documentation section, **Track runs with MLflow and the Jobs run page**, which explains how to log parameters, metrics, and artifacts from distributed training jobs and how to view those runs on the Databricks Jobs run page. Users can monitor experiment progress, compare results, and manage model lineage directly from the CLI‑submitted workloads. ^[ai-runtime-cli-databricks-on-aws.md]

## When to Use the CLI

The AI Runtime CLI is intended for users who want to:

- Submit GPU training workloads from a laptop or code editor without opening a notebook.
- Define training jobs declaratively in YAML so they can be checked into source control.

For in-notebook Python APIs (such as `@distributed` and `@ray_launch`), Databricks recommends the Multi-GPU Workload documentation instead. ^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Open‑source platform for the machine learning lifecycle.
- [AI Runtime](/concepts/ai-runtime.md) – Serverless GPU compute platform on Databricks.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Techniques for scaling model training across multiple GPUs.
- Jobs Run Page – Interface for viewing and comparing training run results.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Definition of the YAML schema used by the CLI.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
