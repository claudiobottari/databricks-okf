---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bcf071b6add1c1d5cba4e06c2bc46d05561d2a7732085e8d14efea78f7ead5cc
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-experiment-tracking-and-observability
    - Observability and AI Runtime Experiment Tracking
    - ARETAO
    - Experiment Tracking and Observability
    - Experiment tracking and observability
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Experiment Tracking and Observability
description: Integration with MLflow for experiment tracking, log viewing, and model checkpoint management on AI Runtime
tags:
  - mlflow
  - experiment-tracking
  - observability
  - monitoring
timestamp: "2026-06-19T17:31:34.789Z"
---

## AI Runtime Experiment Tracking and Observability

**AI Runtime Experiment Tracking and Observability** refers to the built-in capabilities within Databricks AI Runtime for monitoring, logging, and managing deep learning training runs. These features are fully integrated with the Databricks platform, enabling seamless experiment management directly from notebooks and jobs.

### Overview

AI Runtime provides experiment tracking and observability through three primary components:

- **MLflow integration** – Log metrics, parameters, and artifacts during training runs.
- **Log viewing** – Access training logs to monitor progress and debug issues.
- **Model checkpoint management** – Save and restore model checkpoints to resume training or evaluate intermediate states.

For detailed instructions and API references, see the official Databricks documentation on [Experiment tracking and observability](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability). ^[ai-runtime-databricks-on-aws.md]

### Context

These observability features are part of the AI Runtime compute offering, which is designed for deep learning workloads such as LLM fine-tuning, computer vision, reinforcement learning, and time series forecasting. Experiment tracking and observability are natively integrated across notebooks, jobs, Unity Catalog, and MLflow, allowing practitioners to track experiments without additional configuration. ^[ai-runtime-databricks-on-aws.md]

### Related Concepts

- [MLflow](/concepts/mlflow.md) – The open-source platform for machine learning lifecycle management, used as the backbone for experiment tracking.
- [AI Runtime](/concepts/ai-runtime.md) – The serverless GPU compute environment that provides these observability features.
- Model Checkpointing – Saving model states during training to enable recovery and evaluation.
- [Deep Learning on Databricks](/concepts/deep-learning-on-databricks.md) – Broader workflows that benefit from experiment tracking and observability.

### Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
