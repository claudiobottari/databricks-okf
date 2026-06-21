---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82c8ac4645dd76d145a0e60f6fcf1f7c1941fe09a5adebce1f4f7ecb8e6f704b
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-interactive-notebook-connection
    - ARINC
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime Interactive Notebook Connection
description: How to connect a Databricks notebook to an AI Runtime environment using serverless GPU compute via the Environment side panel.
tags:
  - databricks
  - ai-runtime
  - notebooks
  - configuration
timestamp: "2026-06-19T09:22:58.147Z"
---

# AI Runtime Interactive Notebook Connection

**AI Runtime Interactive Notebook Connection** refers to the process of attaching a Databricks notebook to a serverless GPU compute environment powered by AI Runtime. This is the primary way to use AI Runtime for single-node tasks and distributed training workloads. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Overview

Interactive notebook connection is the recommended method for working with AI Runtime. It allows users to configure GPU acceleration, select base environments, and run deep learning workloads directly from a notebook interface. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Connecting a Notebook

To connect a notebook to AI Runtime:

1. From a notebook, click the compute drop-down menu at the top and select **Serverless GPU**.
2. Click the **Environment** icon to open the **Environment** side panel.
3. Select an accelerator from the **Accelerator** field. For distributed training workloads, select **8xH100**. See Hardware Options for AI Runtime for guidance on choosing an accelerator.
4. Select **None** for the [default environment](/concepts/default-vs-ai-environments-in-ai-runtime.md) or **AI v4** for the AI environment from the **Base environment** field.
5. Click **Apply** and then **Confirm** to apply AI Runtime to your notebook environment.

^[connect-to-ai-runtime-databricks-on-aws.md]

## Auto-Termination

Connection to your compute auto-terminates after 60 minutes of inactivity. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Resource Optimization

For operations that do not require GPUs — such as cloning a Git repository, converting data formats, or exploratory data analysis — attach your notebook to a CPU cluster to preserve GPU resources. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime Environments](/concepts/ai-runtime-environments.md) — The base environments available for AI Runtime workloads
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute type used by AI Runtime
- Hardware Options for AI Runtime — Available accelerators and guidance for selection
- [Scheduled Jobs with AI Runtime](/concepts/scheduled-jobs-with-ai-runtime.md) — Running AI Runtime notebooks as recurring jobs
- [Jobs API and AI Runtime](/concepts/scheduled-jobs-with-ai-runtime.md) — Programmatic job creation with AI Runtime

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
