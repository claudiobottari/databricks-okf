---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21024cce83b86f28b5c235141807c3150d2fe29527389b9eb25dbbb383309785
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connecting-to-ai-runtime-from-interactive-notebooks
    - CTARFIN
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Connecting to AI Runtime from Interactive Notebooks
description: Step-by-step process to attach a notebook to Serverless GPU compute with accelerator selection and environment configuration
tags:
  - databricks
  - notebooks
  - configuration
timestamp: "2026-06-19T17:51:29.873Z"
---

# Connecting to AI Runtime from Interactive Notebooks

**Connecting to AI Runtime from Interactive Notebooks** allows you to leverage GPU-accelerated environments directly within Databricks notebooks for single-node and multi-node deep learning workloads. This guide covers the steps to attach a notebook to AI Runtime, configure the environment, and manage compute resources efficiently.

## Interactive Notebook Connection

This is the primary way to use AI Runtime. To connect your notebook and configure the environment:

1. From a notebook, click the compute drop-down menu at the top and select **Serverless GPU**. ^[connect-to-ai-runtime-databricks-on-aws.md]
2. Click the **Environment icon** to open the **Environment** side panel. ^[connect-to-ai-runtime-databricks-on-aws.md]
3. Select an accelerator from the **Accelerator** field. For distributed training workloads, select **8xH100**. See [Hardware options](/concepts/ai-runtime-hardware-options.md) for guidance on choosing an accelerator. ^[connect-to-ai-runtime-databricks-on-aws.md]
4. Select **None** for the [default environment](/concepts/default-vs-ai-environments-in-ai-runtime.md) or **AI v4** for the AI environment from the **Base environment** field. ^[connect-to-ai-runtime-databricks-on-aws.md]
5. Click **Apply** and then **Confirm** to apply the AI Runtime to your notebook environment. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Compute Auto-Termination

Connection to your compute auto-terminates after 60 minutes of inactivity. ^[connect-to-ai-runtime-databricks-on-aws.md]

## GPU Resource Conservation

For operations that do not require GPUs — such as cloning a Git repository, converting data formats, or exploratory data analysis — attach your notebook to a CPU cluster to preserve GPU resources. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Supported Environments

When connecting to AI Runtime, you can choose between two base environment types:

- **None (Default Environment)**: The basic runtime environment without additional AI-specific libraries. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **AI v4**: A pre-configured environment that includes common AI/ML libraries for deep learning workloads. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Hardware Options

Selecting the right accelerator depends on your workload:

- **Single GPU workloads**: Choose a single GPU accelerator for standard training and inference tasks.
- **8xH100**: Select this option for distributed training workloads that require multiple GPUs. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- AI Runtime Overview — General introduction to AI Runtime capabilities.
- Default Environment — The base runtime environment configuration.
- [AI Environment](/concepts/ai-runtime-environments.md) — Pre-configured AI-specific runtime environment.
- Hardware Options for AI Runtime — Detailed guidance on accelerator selection.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU compute infrastructure.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Multi-GPU setup for distributed training.
- [Scheduled Jobs with AI Runtime](/concepts/scheduled-jobs-with-ai-runtime.md) — Running AI Runtime workloads as recurring jobs.
- Jobs API and Databricks Asset Bundles — Programmatic job management.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
