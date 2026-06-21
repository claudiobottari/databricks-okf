---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 333778ac48f1a6776a0fdda86898595afefef42379e2bc13fb5dfe59ed74de14
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-training-workloads-on-databricks
    - DTWOD
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Distributed Training Workloads on Databricks
description: Multi-GPU training workloads submitted and managed via the AI Runtime CLI or the in-notebook Python API (@distributed and @ray_launch).
tags:
  - databricks
  - distributed-training
  - gpu-computing
timestamp: "2026-06-18T14:21:35.753Z"
---

# Distributed Training Workloads on Databricks

**Distributed training workloads** on Databricks leverage the [AI Runtime](/concepts/ai-runtime.md) platform to train deep learning models across multiple GPUs in a serverless, on-demand environment. Databricks provides both a CLI-based and notebook-based API to define, submit, and manage these workloads, integrating with [MLflow](/concepts/mlflow.md) for experiment tracking and the Jobs system for orchestration. ^[ai-runtime-cli-databricks-on-aws.md]

## AI Runtime Overview

AI Runtime is the on-demand serverless GPU compute platform that powers distributed training on Databricks. It automatically provisions and scales GPU clusters without requiring manual infrastructure management. Workloads can be submitted from a local development environment (laptop) or directly from a Databricks notebook. ^[ai-runtime-cli-databricks-on-aws.md]

## The AI Runtime CLI (`air`)

The `air` command-line interface is used to submit and manage distributed training workloads from the terminal. It is particularly useful when you want to:

- Submit GPU training jobs from your laptop and code editor without opening a notebook.
- Define training jobs declaratively in YAML configuration so they can be checked into source control and reused. ^[ai-runtime-cli-databricks-on-aws.md]

The CLI is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types) and supports workspace-based and git-based code workflows. It integrates with MLflow for run tracking and the Jobs run page for monitoring. ^[ai-runtime-cli-databricks-on-aws.md]

## Notebook-Based API

For users who prefer working within Databricks notebooks, an alternative Python API is available. The `@distributed` decorator and `@ray_launch` function allow multi-GPU training directly from notebook cells. See Multi-GPU workload for details. ^[ai-runtime-cli-databricks-on-aws.md]

## Workload Configuration

Distributed training jobs are defined using YAML configuration files. These files specify the code source (workspace path or git repository), compute requirements (GPU type, count), MLflow experiment to log to, and training parameters. The configuration is passed to the `air` CLI when submitting the job. ^[ai-runtime-cli-databricks-on-aws.md]

## MLflow Integration

All runs submitted via the AI Runtime CLI are automatically tracked in [MLflow](/concepts/mlflow.md) experiments. Metrics, parameters, and artifacts are logged, enabling comparison across training runs. The Jobs run page provides a consolidated view of job status, logs, and performance. ^[ai-runtime-cli-databricks-on-aws.md]

## Additional Resources

For detailed command reference, see [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md). For example workloads and step-by-step instructions, refer to [AI Runtime CLI examples](/concepts/ai-runtime-cli.md).

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
