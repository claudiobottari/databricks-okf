---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c81a37aff7d4378ab2dac81d742924d1c23e9946ccd284695c255c497514db2
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - production-monitoring-for-long-term-trace-storage
    - PMFLTS
  citations:
    - file: trace-agents-deployed-on-databricks-databricks-on-aws.md
title: Production Monitoring for Long-term Trace Storage
description: Optional beta feature that stores MLflow traces in Delta tables for durable long-term retention, removes trace size limits, enables automated quality assessment via MLflow scorers, and syncs approximately every 15 minutes.
tags:
  - monitoring
  - delta-tables
  - tracing
  - databricks
timestamp: "2026-06-19T23:07:23.989Z"
---

# [Production Monitoring](/concepts/production-monitoring.md) for Long-term Trace Storage

**Production Monitoring for Long-term Trace Storage** is a Databricks feature (in beta) that provides durable storage of [[MLflow Trace|MLflow Traces]] in [Delta Tables](/concepts/delta-lake-table.md), enabling long-term retention beyond the default [MLflow Experiment](/concepts/mlflow-experiment.md) artifact lifecycle. Beyond storage, it also enables automated quality assessment and analysis of production [Traces](/concepts/traces.md).

## Overview

After [MLflow Tracing](/concepts/mlflow-tracing.md) logs [Traces](/concepts/traces.md) to an [MLflow Experiment](/concepts/mlflow-experiment.md) during production inference, those [Traces](/concepts/traces.md) can optionally be stored long-term using [Production Monitoring](/concepts/production-monitoring.md). This feature syncs [Traces](/concepts/traces.md) from the [MLflow Experiment](/concepts/mlflow-experiment.md) to Delta tables, making them available for durable storage, large-scale analysis, and automated quality evaluation. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Benefits

[Production Monitoring](/concepts/production-monitoring.md) offers several advantages for trace storage compared to relying solely on [MLflow Experiment](/concepts/mlflow-experiment.md) artifacts: ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

- **Durable storage**: [Traces](/concepts/traces.md) are stored in [Delta Tables](/concepts/delta-lake-table.md) for long-term retention, independent of the [MLflow Experiment](/concepts/mlflow-experiment.md) artifact lifecycle.
- **No trace size limits**: [Production Monitoring](/concepts/production-monitoring.md) handles [Traces](/concepts/traces.md) of any size, unlike alternative storage methods that may impose size restrictions.
- **Automated quality assessment**: [MLflow Scorers](/concepts/mlflow-scorers.md) can be run on production [Traces](/concepts/traces.md) to continuously monitor application quality and detect regressions.
- **Fast sync**: [Traces](/concepts/traces.md) sync to Delta tables approximately every 15 minutes, providing near-real-time access to production trace data.

## Prerequisites

Before using [Production Monitoring](/concepts/production-monitoring.md) for trace storage, ensure the following are in place: ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

1. [Production Monitoring](/concepts/production-monitoring.md) must be enabled for your [Databricks Workspace](/concepts/workspace-feature-store-ui.md).
2. An [MLflow Experiment](/concepts/mlflow-experiment.md) must be created for storing your application's production [Traces](/concepts/traces.md).

## Setup Workflow

The general workflow for enabling long-term trace storage with [Production Monitoring](/concepts/production-monitoring.md) is: ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

1. **Enable Production Monitoring**: Ensure the feature is enabled for your workspace.
2. **Create an [MLflow](/concepts/mlflow.md) Experiment**: Set up a workspace experiment for your application's production [Traces](/concepts/traces.md).
3. **Deploy your agent**: Deploy your GenAI application using either Custom Agents (recommended) or custom CPU [Model Serving](/concepts/model-serving.md).
4. **Traces are logged**: Databricks automatically logs [Traces](/concepts/traces.md) to the [MLflow Experiment](/concepts/mlflow-experiment.md) during inference.
5. **Traces sync to Delta tables**: [Production Monitoring](/concepts/production-monitoring.md) syncs [Traces](/concepts/traces.md) to Delta tables approximately every 15 minutes for durable storage.

## Deployment Methods

### Custom Agents (Recommended)

When deploying GenAI applications using Custom Agents, [MLflow Tracing](/concepts/mlflow-tracing.md) works automatically without additional configuration. [Traces](/concepts/traces.md) are stored in the agent's [MLflow Experiment](/concepts/mlflow-experiment.md). This method is the recommended approach for deployment. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

### Custom CPU [Model Serving](/concepts/model-serving.md) (Alternative)

If Custom Agents cannot be used, applications can be deployed using custom CPU [Model Serving](/concepts/model-serving.md). This method requires manually setting environment variables to enable tracing, including `ENABLE_MLFLOW_TRACING=true` and specifying the [MLflow Experiment](/concepts/mlflow-experiment.md) ID. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Trace Storage Mechanism

When [Traces](/concepts/traces.md) are logged to the [MLflow Experiment](/concepts/mlflow-experiment.md), they are available for real-time viewing in the [MLflow UI](/concepts/mlflow.md). With [Production Monitoring](/concepts/production-monitoring.md) enabled, these same [Traces](/concepts/traces.md) are also synced to Delta tables for long-term storage. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

[Traces](/concepts/traces.md) are stored as [MLflow](/concepts/mlflow.md) artifacts. If the experiment is created with `artifact_location` set to a Unity Catalog Volume, then trace data access is governed by Unity Catalog Volume Privileges. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The framework for capturing trace data during GenAI application inference
- [Production Monitoring](/concepts/production-monitoring.md) — The broader feature for monitoring production ML applications
- [MLflow Scorers](/concepts/mlflow-scorers.md) — Automated evaluators for quality assessment on production [Traces](/concepts/traces.md)
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format for long-term trace retention
- Custom Agents — Recommended deployment method for GenAI applications on Databricks
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The organizational unit for [MLflow](/concepts/mlflow.md) runs and trace storage

## Sources

- trace-agents-deployed-on-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-on-databricks-databricks-on-aws.md](/references/trace-agents-deployed-on-databricks-databricks-on-aws-962e29f6.md)
