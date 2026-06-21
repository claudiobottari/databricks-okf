---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73cac9731d1c5c854d673175736da2313030c9fc795c3995665662e8e86fb2f8
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-environments
    - DARE
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: Databricks AI Runtime Environments
description: "Two managed Python environments offered by AI Runtime: a minimal default base environment and a full-featured Databricks AI environment pre-loaded with ML frameworks like PyTorch and Transformers."
tags:
  - databricks
  - environment
  - ml-frameworks
timestamp: "2026-06-18T14:22:44.632Z"
---

# Databricks AI Runtime Environments

**Databricks AI Runtime Environments** are managed Python environments available within [AI Runtime](/concepts/ai-runtime.md), Databricks' compute offering for deep learning workloads on serverless GPU infrastructure. AI Runtime provides two environment options: a minimal default base environment and a full-featured Databricks AI environment pre-loaded with popular machine learning frameworks. ^[ai-runtime-databricks-on-aws.md]

## Environment Options

### Default Base Environment

The default base environment is a minimal Python environment that provides maximum flexibility for users who want to manage their own dependencies. This environment is suitable when you need precise control over package versions or have specific dependency requirements. ^[ai-runtime-databricks-on-aws.md]

### Databricks AI Environment

The full-featured Databricks AI environment comes pre-loaded with popular ML frameworks such as PyTorch and Transformers. This environment is designed to accelerate development by providing commonly used deep learning libraries out of the box, reducing the time spent on environment setup. ^[ai-runtime-databricks-on-aws.md]

## Installing Dependencies

### Notebook-Based Installation

For interactive notebook sessions, you can install additional dependencies programmatically using `%pip install` commands directly in your notebook. This approach is supported for both environment options. ^[ai-runtime-databricks-on-aws.md]

### Scheduled Jobs Limitation

Adding dependencies using the **Environments** panel is not supported for AI Runtime scheduled jobs. For scheduled jobs, you must install dependencies programmatically using `%pip install` in your notebook instead. ^[ai-runtime-databricks-on-aws.md]

## Caching Behavior

AI Runtime environments implement caching mechanisms to improve performance. The specific caching behavior affects how quickly environments are available for subsequent runs. ^[ai-runtime-databricks-on-aws.md]

## Importing Custom Modules

Users can import custom modules within AI Runtime environments. The environment supports standard Python module import patterns for custom code. ^[ai-runtime-databricks-on-aws.md]

## Known Limitations

- For scheduled jobs on AI Runtime, auto recovery behavior for incompatible package versions associated with your notebook is not supported. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days. For model training jobs that exceed this limit, implement checkpointing and restart the job once the maximum runtime is reached. ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The compute offering that provides these environments
- [Serverless GPU Infrastructure](/concepts/serverless-gpu-infrastructure.md) — The underlying infrastructure for AI Runtime
- PyTorch — A deep learning framework included in the full-featured environment
- Transformers — A library for transformer models included in the full-featured environment
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU training capabilities available on AI Runtime
- MLflow Integration — Experiment tracking and model management on AI Runtime

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
