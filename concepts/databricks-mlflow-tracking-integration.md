---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82d69d9415f9f7f2f7b569fd1cce219d030fb78b49a49c1afbbb9ef6641fd865
  pageDirectory: concepts
  sources:
    - tracing-mistral-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-tracking-integration
    - DMTI
    - Databricks MLflow Tracking
  citations:
    - file: tracing-mistral-databricks-on-aws.md
title: Databricks MLflow Tracking Integration
description: Configuration to route MLflow experiment data to a Databricks workspace using mlflow.set_tracking_uri('databricks') and mlflow.set_experiment().
tags:
  - databricks
  - mlflow
  - tracking
  - experiment-management
timestamp: "2026-06-19T23:12:27.103Z"
---

# Databricks [MLflow Tracking](/concepts/mlflow-tracking.md) Integration

**Databricks [MLflow Tracking](/concepts/mlflow-tracking.md) Integration** refers to the process of configuring [MLflow](/concepts/mlflow.md) to log experiment metadata, parameters, metrics, and model artifacts directly to the Databricks workspace, enabling centralized experiment management and collaboration across teams.

## Overview

[MLflow Tracking](/concepts/mlflow-tracking.md) is a component of the open-source [MLflow](/concepts/mlflow.md) platform that records and queries experiments, including parameters, metrics, and artifacts. The Databricks [MLflow Tracking](/concepts/mlflow-tracking.md) Integration allows users to route all [MLflow](/concepts/mlflow.md) logging from any environment—including local machines, CI/CD pipelines, or cloud notebooks—to a central Databricks workspace. ^[tracing-mistral-databricks-on-aws.md]

## Configuration

To use Databricks as the tracking backend, you set the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) to `"databricks"` and specify an experiment path within the Databricks workspace: ^[tracing-mistral-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/my-experiment")
```

After this configuration, all subsequent [MLflow](/concepts/mlflow.md) runs log to the specified experiment in the Databricks workspace. Users can view and compare runs using the Databricks experiment UI. ^[tracing-mistral-databricks-on-aws.md]

## Integration with [Model Serving](/concepts/model-serving.md) and Tracing

The Databricks [MLflow Tracking](/concepts/mlflow-tracking.md) Integration is commonly used alongside [Model Serving](/concepts/model-serving.md) and tracing features. For example, when using [Mistral AI](/concepts/mistral-ai-python-sdk.md) models on Databricks, you can enable [MLflow Auto Tracing](/concepts/mlflow-automatic-tracing.md) to automatically capture model inference [Traces](/concepts/traces.md): ^[tracing-mistral-databricks-on-aws.md]

```python
# Enable auto tracing for Mistral AI
[[mlflow|MLflow]].mistral.autolog()
```

This integration logs [Traces](/concepts/traces.md) of model inference calls, including inputs, outputs, latency, and token usage, to the Databricks tracking server. The [Traces](/concepts/traces.md) appear in the experiment under the associated run. ^[tracing-mistral-databricks-on-aws.md]

## Authentication

When connecting to a Databricks workspace from an external environment, [MLflow](/concepts/mlflow.md) uses the authentication credentials configured in the Databricks CLI or environment variables (`DATABRICKS_HOST` and `DATABRICKS_TOKEN`). Within a Databricks notebook, these credentials are automatically available. ^[tracing-mistral-databricks-on-aws.md]

## Use Cases

- **Centralized experiment tracking** — Log all experiments from multiple team members to a single shared workspace.
- **Model observability** — Combine tracking with tracing to monitor model behavior in production or staging.
- **Collaboration** — Compare runs, share results, and promote models across the [ML Lifecycle](/concepts/ml-lifecycle.md) using Databricks' experiment UI.
- **Environment flexibility** — Develop locally or in CI/CD while still logging to the workspace.

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core component for logging parameters, metrics, and artifacts.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for grouping related runs.
- [MLflow Auto Tracing](/concepts/mlflow-automatic-tracing.md) — Automatic instrumentation of model inference for observability.
- Mistral AI Integration on Databricks — Using Mistral models with Databricks [MLflow](/concepts/mlflow.md).
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Manage and deploy registered models.

## Sources

- tracing-mistral-databricks-on-aws.md

# Citations

1. [tracing-mistral-databricks-on-aws.md](/references/tracing-mistral-databricks-on-aws-6af10854.md)
