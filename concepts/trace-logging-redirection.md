---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bcb40ca2f11ea108d6a31c216cbb4a538c9c0c8fe93e9ab148f1f40ccfab5116
  pageDirectory: concepts
  sources:
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-logging-redirection
    - TLR
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
title: Trace Logging Redirection
description: The step of stopping writes to the source experiment and redirecting trace logging to a new Unity Catalog-backed destination experiment before running migration, preventing data loss.
tags:
  - mlflow
  - tracing
  - production
timestamp: "2026-06-19T19:33:01.131Z"
---

# Trace Logging Redirection

**Trace Logging Redirection** is the process of changing the destination where MLflow trace data is written, typically from a workspace-level MLflow experiment to a [Unity Catalog](/concepts/unity-catalog.md)-backed experiment. This is a key step when migrating existing traces to Unity Catalog or when reconfiguring production tracing workflows.

## Overview

Trace logging redirection involves updating the trace destination configuration so that new traces are written to a different experiment than the one currently in use. This is commonly performed as part of a migration workflow where traces are moved from a standard MLflow experiment to Unity Catalog Delta tables. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## When to Redirect Trace Logging

Trace logging redirection is necessary in the following scenarios:

- **Before migrating existing traces**: To ensure no new traces are written to the source experiment during migration, trace logging must first be redirected to the destination experiment. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- **When switching to Unity Catalog storage**: After creating a Unity Catalog-backed experiment, all trace logging must be redirected to the new experiment to take advantage of Unity Catalog's storage limits, access controls, and queryability. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## How to Redirect Trace Logging

### Using the MLflow API

The primary method for redirecting trace logging is to call `mlflow.set_experiment()` with the destination experiment, either by name or by ID: ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

```python
import mlflow

# By experiment name
mlflow.set_experiment(
    experiment_name="/Workspace/Users/<user>/<destination_experiment_name>",
)

# Or by experiment ID
mlflow.set_experiment(experiment_id="<destination_experiment_id>")
```

### Using Environment Variables

Trace logging can also be redirected through environment variables, which are commonly used by deployed applications, containerized services, model serving endpoint configurations, and IDE or local development setups: ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

- `MLFLOW_EXPERIMENT_NAME`
- `MLFLOW_EXPERIMENT_ID`

## Important Considerations

### Stop Writes to the Source Experiment

Before redirecting trace logging, all writes to the source experiment must be stopped. This includes verifying that no notebooks, jobs, or deployed models are actively logging to the source experiment. Any traces written to the source experiment during migration might not be copied to the destination. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Production Tracing Configuration

For detailed guidance on configuring trace destinations in production environments, see the documentation on Trace agents deployed on Databricks and [Trace agents deployed outside of Databricks](/concepts/custom-agents-deployment-for-genai-on-databricks.md). ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Migrate experiment traces to Unity Catalog — The full migration workflow that includes trace logging redirection
- [Store traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md) — Setting up a new experiment to write traces directly to Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and storage layer for trace data
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and traces
- Trace agents deployed on Databricks — Production tracing configuration for Databricks-deployed agents
- [Trace agents deployed outside of Databricks](/concepts/custom-agents-deployment-for-genai-on-databricks.md) — Production tracing configuration for external agents

## Sources

- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
