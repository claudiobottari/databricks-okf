---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1974bfad94be818fb1d44f69ae404f6479b1d9590d66f71b9c5ec124f6c7a95b
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connecting-to-ai-runtime-via-interactive-notebooks
    - CTARVIN
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Connecting to AI Runtime via Interactive Notebooks
description: Primary method to use AI Runtime by attaching a notebook to Serverless GPU compute and selecting an accelerator and base environment.
tags:
  - databricks
  - notebooks
  - ai-runtime
timestamp: "2026-06-18T14:43:32.898Z"
---

---

title: Connecting to AI Runtime via Interactive Notebooks
summary: Step-by-step guide for attaching a Databricks notebook to AI Runtime using Serverless GPU, including accelerator selection, environment configuration, and best practices.
sources:
  - connect-to-ai-runtime-databricks-on-aws.md
kind: concept
createdAt: 2026-06-18T10:00:00.000Z
updatedAt: 2026-06-18T10:00:00.000Z
tags:
  - databricks
  - ai-runtime
  - notebooks
  - serverless-gpu
aliases:
  - connecting-to-ai-runtime-via-interactive-notebooks
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# Connecting to AI Runtime via Interactive Notebooks

**Connecting to AI Runtime via Interactive Notebooks** is the primary way to use [AI Runtime](/concepts/ai-runtime.md) on Databricks. By attaching a notebook to a Serverless GPU compute resource and selecting the appropriate environment, users can run deep learning and AI workloads directly from the notebook interface. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Prerequisites

- A Databricks workspace with access to [Serverless GPU](/concepts/serverless-gpu-compute.md) compute (Public Preview for single-node tasks; Beta for multi-GPU distributed training). ^[connect-to-ai-runtime-databricks-on-aws.md]
- An existing notebook in the workspace.

## Connecting the Notebook

1. In the notebook, click the compute drop-down menu at the top of the page and select **Serverless GPU**. ^[connect-to-ai-runtime-databricks-on-aws.md]
2. Click the **Environment** icon (sliders icon) in the notebook toolbar to open the **Environment** side panel. ^[connect-to-ai-runtime-databricks-on-aws.md]
3. In the **Accelerator** field, choose the GPU accelerator. For distributed training workloads, select **8xH100**. Refer to the [AI Runtime Hardware Options](/concepts/ai-runtime-hardware-options.md) for guidance. ^[connect-to-ai-runtime-databricks-on-aws.md]
4. In the **Base environment** field, select either **None** (the default environment) or **AI v4** (the AI environment). ^[connect-to-ai-runtime-databricks-on-aws.md]
5. Click **Apply** and then **Confirm** to apply AI Runtime to the notebook environment. ^[connect-to-ai-runtime-databricks-on-aws.md]

After these steps, the notebook is connected to AI Runtime and can execute cells that require GPU acceleration.

## Important Notes

- **Auto-termination:** The connection to the compute resource auto-terminates after 60 minutes of inactivity. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **GPU resource conservation:** For operations that do not require GPUs (e.g., cloning a Git repository, converting data formats, or exploratory data analysis), Databricks recommends attaching the notebook to a CPU cluster instead to preserve GPU resources. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — Overview of the Databricks AI Runtime environment
- [Serverless GPU](/concepts/serverless-gpu-compute.md) — Compute type used for AI Runtime notebooks
- [AI Environment](/concepts/ai-runtime-environments.md) — The pre-configured environment (AI v4) available for AI Runtime
- GPU Accelerator Options — Available hardware accelerators for AI Runtime
- AI Runtime Default Environment — The base environment without additional AI libraries
- [Scheduling Notebook Jobs on AI Runtime](/concepts/scheduled-jobs-with-ai-runtime.md) — Using AI Runtime for recurring jobs

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
