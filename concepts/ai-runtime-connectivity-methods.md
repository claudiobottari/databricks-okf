---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a18604c1ce3b219867e5f34c05911d6975d8e72a0f3dcf05c23f17405038d0f
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-connectivity-methods
    - ARCM
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Connectivity Methods
description: Ways to connect to AI Runtime including interactive notebooks, scheduled jobs, Jobs API, and Databricks Asset Bundles.
tags:
  - connectivity
  - notebooks
  - jobs
timestamp: "2026-06-19T13:58:00.898Z"
---

# AI Runtime Connectivity Methods

**AI Runtime Connectivity Methods** refers to the ways users can access and run workloads on [AI Runtime](/concepts/ai-runtime.md), Databricks' serverless GPU compute offering for deep learning. Connectivity is supported via interactive notebooks, recurring scheduled jobs, and programmatic job creation using APIs and infrastructure-as-code tools. ^[ai-runtime-databricks-on-aws.md]

## Overview

AI Runtime is a fully managed compute offering that provides GPU support for Databricks Serverless. It eliminates the need for cluster configuration, driver selection, or autoscaling policies. Users connect to AI Runtime through the Databricks workspace interface or programmatically, and the infrastructure is provisioned on demand in supported AWS regions. ^[ai-runtime-databricks-on-aws.md]

## Connectivity Methods

### Interactive Notebooks

The primary interactive method is connecting from Databricks notebooks. Users attach a notebook to an AI Runtime compute resource directly from the notebook UI. This enables iterative development, experimentation, and real-time debugging with GPU acceleration. ^[ai-runtime-databricks-on-aws.md]

### Scheduled Jobs

Notebooks running on AI Runtime can be scheduled as recurring [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md). This allows routine tasks such as model retraining or batch inference to execute on a cron-like schedule without manual intervention. ^[ai-runtime-databricks-on-aws.md]

### Programmatic Jobs (API and Bundles)

For automated workflows, connectivity is supported through the Jobs API and Databricks Asset Bundles. These programmatic methods allow users to create, trigger, and manage AI Runtime jobs from external systems, CI/CD pipelines, or custom tooling. ^[ai-runtime-databricks-on-aws.md]

## Requirements

To connect to AI Runtime, the workspace must be in one of the supported AWS regions (`us-west-2`, `us-west-1`, `us-east-1`, `us-east-2`, `ca-central-1`, `sa-east-1`) and the AI Runtime preview must be enabled by a workspace admin. ^[ai-runtime-databricks-on-aws.md]

## Limitations Affecting Connectivity

- AI Runtime is **not supported for [compliance security profile](/concepts/compliance-security-profile-databricks-on-aws.md) workspaces** (e.g., HIPAA, PCI). Regulated data cannot be processed. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for any connected workload is seven days. Jobs exceeding this limit must implement checkpointing and restart. ^[ai-runtime-databricks-on-aws.md]
- Adding dependencies through the **Environments** panel is not supported for scheduled jobs; dependencies must be installed programmatically via `%pip install`. ^[ai-runtime-databricks-on-aws.md]
- GPU capacity is on-demand and may occasionally be constrained or unavailable in a region. During high demand, cross-region GPUs may be used, incurring potential egress costs. ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The compute offering itself, including hardware options and use cases.
- Databricks Serverless — The underlying serverless architecture that AI Runtime leverages.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The scheduling and orchestration service for running notebooks programmatically.
- Databricks Asset Bundles — Infrastructure-as-code tool for defining and deploying jobs.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Broader category of on-demand GPU resources on Databricks.

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
