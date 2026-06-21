---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c753f8e4a05c3c4c70a4c109ade99285ca819645b402eaa9fafe63fdcc0091e6
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-cpu-model-serving-as-alternative-deployment
    - CCMSAAD
  citations:
    - file: trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md
title: Custom CPU Model Serving as Alternative Deployment
description: Alternative deployment method for GenAI agents on Databricks when Custom Agents cannot be used, requiring manual environment variable configuration (ENABLE_MLFLOW_TRACING, MLFLOW_EXPERIMENT_ID) and credential setup.
tags:
  - deployment
  - model-serving
  - databricks
  - mlflow
timestamp: "2026-06-19T23:08:25.994Z"
---

Here is the wiki page for "Custom CPU [Model Serving](/concepts/model-serving.md) as Alternative Deployment".

---

## Custom CPU [Model Serving](/concepts/model-serving.md) as Alternative Deployment

**Custom CPU Model Serving** is an alternative deployment method for [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications on Databricks when the recommended Custom Agents approach is not viable. It allows you to deploy a GenAI agent to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using CPU infrastructure, while still capturing production [Traces](/concepts/traces.md) via [MLflow Tracing](/concepts/mlflow-tracing.md). ^[trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md]

### When to Use This Method

Use custom CPU [Model Serving](/concepts/model-serving.md) when you cannot use the Custom Agents deployment method. It still enables automatic trace capture for your deployed agent. ^[trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md]

### Prerequisites

Before deploying, ensure you have the storage locations set up for [Traces](/concepts/traces.md):

1. If you plan to use [Production Monitoring](/concepts/production-monitoring.md) to store [Traces](/concepts/traces.md) in [Delta tables](/concepts/delta-lake-table.md), ensure it is **enabled** for your workspace.
2. Create an [MLflow Experiment](/concepts/mlflow-experiment.md) for storing your application's production [Traces](/concepts/traces.md). ^[trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md]

### Deployment Steps

To deploy an agent using custom CPU [Model Serving](/concepts/model-serving.md):

1. **Log your agent** as an [MLflow](/concepts/mlflow.md) model with automatic or manual tracing instrumentation.
2. **Deploy the model** to a CPU serving endpoint.
3. **Provision credentials**: Provision either a Service Principal or a Personal Access Token (PAT) with `CAN_EDIT` access to the [MLflow Experiment](/concepts/mlflow-experiment.md).
4. **Configure environment variables**: On the CPU serving endpoint page, go to "Edit endpoint" and add the following environment variables for each deployed model to trace:
   - `ENABLE_MLFLOW_TRACING=true`
   - `MLFLOW_EXPERIMENT_ID=<ID of the experiment you created>`
   - If using a Service Principal: `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`
   - If using a PAT: `DATABRICKS_HOST` and `DATABRICKS_TOKEN`

^[trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md]

### Trace Storage

[Traces](/concepts/traces.md) are logged to the [MLflow Experiment](/concepts/mlflow-experiment.md) you set with `mlflow.set_experiment(...)` during deployment. They are available for real-time viewing in the [MLflow UI](/concepts/mlflow.md) and are stored as artifacts. You can specify a custom [artifact location](/concepts/experiment-artifact-storage-locations.md); for example, if you create a workspace experiment with `artifact_location` set to a Unity Catalog volume, then trace data access is governed by Unity Catalog volume privileges. ^[trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md]

### Long-Term Trace Storage with [Production Monitoring](/concepts/production-monitoring.md)

After [Traces](/concepts/traces.md) are logged to your [MLflow Experiment](/concepts/mlflow-experiment.md), you can optionally store them long-term in Delta tables using [Production Monitoring](/concepts/production-monitoring.md) (in beta). Benefits include:

- **Durable storage**: Store [Traces](/concepts/traces.md) in Delta tables for long-term retention beyond the [MLflow Experiment](/concepts/mlflow-experiment.md) artifact lifecycle.
- **No trace size limits**: [Production Monitoring](/concepts/production-monitoring.md) handles [Traces](/concepts/traces.md) of any size.
- **Automated quality assessment**: Run [MLflow Scorers](/concepts/mlflow-scorers.md) on production [Traces](/concepts/traces.md) to continuously monitor application quality.
- **Fast sync**: [Traces](/concepts/traces.md) sync to Delta tables approximately every 15 minutes.

^[trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md]

### Related Concepts

- Custom Agents — The recommended deployment method for GenAI applications.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that captures production [Traces](/concepts/traces.md).
- [Production Monitoring](/concepts/production-monitoring.md) — System for storing [Traces](/concepts/traces.md) in Delta tables for long-term retention.
- [Model Serving](/concepts/model-serving.md) — The endpoint infrastructure for deploying models.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing data and models.
- [Delta tables](/concepts/delta-lake-table.md) — Storage format for long-term trace retention.

### Sources

- trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md

# Citations

1. trace-agents-deployed-on-databricks-databricks-databricks-on-aws.md
