---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59697437db15fdbe652407aa69ef494436999edc2a33131fdd4f8e7d9fda6124
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-base-environments
    - ARBE
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime Base Environments
description: "The two base environment options for AI Runtime: None (default environment without AI libraries) and the AI environment (databricks_ai_v4/v5) which includes pre-installed AI and ML libraries."
tags:
  - databricks
  - ai-runtime
  - environments
  - configuration
timestamp: "2026-06-19T09:23:10.500Z"
---

# AI Runtime Base Environments

**AI Runtime Base Environments** are pre-configured software stacks that provide the libraries, dependencies, and runtime settings for workloads running on [Serverless GPU](/concepts/serverless-gpu-compute.md) compute within the Databricks [AI Runtime](/concepts/ai-runtime.md). When you attach a notebook or configure a job to use AI Runtime, you can choose between two base environment options: the **default environment** and the **AI environment**. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Default Environment

The default environment is a minimal base image that includes core Databricks runtime components but does **not** include the additional GenAI-oriented libraries bundled in the AI environment. In the notebook UI, this option appears as **None** in the **Base environment** field. ^[connect-to-ai-runtime-databricks-on-aws.md]

In Databricks Asset Bundle configurations, the default environment is specified by setting `environment_version` to `'4'` (as shown in the first YAML example in the source). ^[connect-to-ai-runtime-databricks-on-aws.md]

## AI Environment

The AI environment is a curated environment that includes pre-installed packages and optimizations for generative AI and large language model development. In the notebook UI, this option appears as **AI v4** in the **Base environment** field. ^[connect-to-ai-runtime-databricks-on-aws.md]

In Databricks Asset Bundle configurations, the AI environment is specified by setting `base_environment` to the corresponding identifier (for example, `databricks_ai_v5` for AI v5). The bundle configuration references this environment via the task's `environment_key`. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Selecting a Base Environment

The choice between environments depends on your workload requirements:

- **None (default environment)** – Use when you want a minimal base and plan to install only the specific dependencies your workload needs.
- **AI v4 (AI environment)** – Use when your workload benefits from the pre-installed GenAI libraries and optimizations, such as training or serving large language models.

When working from a notebook, you select the base environment **after** choosing an accelerator (e.g., `8xH100`) in the **Environment** side panel. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The overall runtime platform for GPU-accelerated workloads.
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – The compute type used with AI Runtime.
- Connect to AI Runtime – End-to-end guidance for setting up notebooks and jobs.
- Model Checkpointing – Recommended for long-running workloads that may exceed runtime limits.
- Databricks Asset Bundles – Configuration-based job deployment that supports environment versioning.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
