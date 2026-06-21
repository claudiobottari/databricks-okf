---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b13d921923b94d0cd9bafbb8a73ceac15d2bc4ca571f8bd35eb5e4d7e6f2e06e
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-production-tracing-on-databricks
    - MPTOD
  citations:
    - file: trace-agents-deployed-on-databricks-databricks-on-aws.md
title: MLflow Production Tracing on Databricks
description: Automatic capture of GenAI application traces when deployed on Databricks, with traces logged to MLflow experiments for real-time viewing and optional long-term Delta table storage via Production Monitoring.
tags:
  - mlflow
  - tracing
  - databricks
  - genai
timestamp: "2026-06-19T23:07:11.885Z"
---

# [MLflow](/concepts/mlflow.md) Production Tracing on Databricks

**MLflow Production Tracing on Databricks** enables automatic capture of [Traces](/concepts/traces.md) for GenAI applications deployed on Databricks. [Traces](/concepts/traces.md) are logged to an [MLflow](/concepts/mlflow.md) experiment for real-time viewing and can optionally be stored long-term in [Delta tables](/concepts/delta-lake-table.md) via [Production Monitoring](/concepts/production-monitoring.md). The system supports two deployment paths: Custom Agents (recommended) and custom CPU [Model Serving](/concepts/model-serving.md). ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Overview

When a GenAI application is deployed on Databricks, [MLflow Tracing](/concepts/mlflow-tracing.md) captures request-level [Traces](/concepts/traces.md) without additional configuration if you use Custom Agents. For custom CPU serving, you must add environment variables to enable tracing. [Traces](/concepts/traces.md) are written to the [MLflow Experiment](/concepts/mlflow-experiment.md) specified during deployment and are visible immediately in the [MLflow](/concepts/mlflow.md) UI. They are stored as artifacts; you can control access by setting an `artifact_location` (e.g., a [Unity Catalog](/concepts/unity-catalog.md) volume). ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

For apps deployed outside Databricks, see [Trace agents deployed outside of Databricks](/concepts/custom-agents-deployment-for-genai-on-databricks.md). ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Deploy with Custom Agents (recommended)

Custom Agents provide the simplest setup – tracing works automatically once your agent is instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md). Follow these steps:

1. **Set up storage location(s):**  
   - If you plan to use [Production Monitoring](/concepts/production-monitoring.md) for long-term Delta table storage, ensure it is enabled for your workspace.  
   - [Create an MLflow Experiment|Create an MLflow experiment](/concepts/creating-mlflow-experiments-on-databricks.md) to hold production [Traces](/concepts/traces.md).

2. **Instrument and deploy your agent:**  
   - Install the latest version of `mlflow[databricks]`.  
   - Connect to the experiment via `mlflow.set_experiment(...)`.  
   - Wrap your agent code using the MLflow ResponsesAgent and enable [MLflow Tracing](/concepts/mlflow-tracing.md) (automatic or manual instrumentation).  
   - Log the agent as an [MLflow](/concepts/mlflow.md) model and register it in [Unity Catalog](/concepts/unity-catalog.md).  
   - Ensure `mlflow` is included in the model's Python dependencies, with the same version used in your notebook.  
   - Use `agents.deploy(...)` to deploy the model to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md).

**Note:** If you deploy from a [Databricks Git folders|Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md), set a non-Git-associated experiment with `mlflow.set_experiment()` before `agents.deploy()` to enable real-time tracing. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Deploy with custom CPU serving (alternative)

If Custom Agents are not an option, deploy via custom CPU [Model Serving](/concepts/model-serving.md):

1. **Set up storage location(s)** – same as above ([Production Monitoring](/concepts/production-monitoring.md) enabled if needed, create an [MLflow Experiment](/concepts/mlflow-experiment.md)).

2. **Instrument and deploy your model:**  
   - Log your agent as an [MLflow](/concepts/mlflow.md) model with tracing instrumentation (automatic or manual).  
   - Deploy the model to a CPU serving endpoint (via UI or APIs).  
   - Provision a Service Principal or Personal Access Token with `CAN_EDIT` access to the experiment.  
   - On the serving endpoint's **Edit endpoint** page, add the following environment variables for each deployed model to be traced:  
     - `ENABLE_MLFLOW_TRACING=true`  
     - `MLFLOW_EXPERIMENT_ID=<ID of your experiment>`  
     - If using a Service Principal: `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`  
     - If using a PAT: `DATABRICKS_HOST` and `DATABRICKS_TOKEN` ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Trace storage

[Traces](/concepts/traces.md) are logged to the [MLflow Experiment](/concepts/mlflow-experiment.md) set via `mlflow.set_experiment(...)` during deployment. They are available for real-time viewing in the [MLflow](/concepts/mlflow.md) UI. Because [Traces](/concepts/traces.md) are stored as artifacts, you can specify a custom storage location. For example, if you create a workspace experiment with its `artifact_location` pointing to a [Unity Catalog](/concepts/unity-catalog.md) volume, trace data access is governed by Unity Catalog volume privileges. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Store [Traces](/concepts/traces.md) long-term with [Production Monitoring](/concepts/production-monitoring.md)

After [Traces](/concepts/traces.md) are logged to your [MLflow Experiment](/concepts/mlflow-experiment.md), you can optionally enable [Production Monitoring](/concepts/production-monitoring.md) (in beta) to store them durably in Delta tables. Benefits include:

- **Durable storage** – [Traces](/concepts/traces.md) persist beyond the [MLflow](/concepts/mlflow.md) artifact lifecycle.
- **No trace size limits** – handles [Traces](/concepts/traces.md) of any size.
- **Automated quality assessment** – run [MLflow Scorers](/concepts/mlflow-scorers.md) on production [Traces](/concepts/traces.md) continuously.
- **Fast sync** – [Traces](/concepts/traces.md) sync to Delta tables approximately every 15 minutes. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Next steps

- View traces in the Databricks MLflow UI|View traces in the [MLflow](/concepts/mlflow.md) UI.
- [Production Monitoring](/concepts/production-monitoring.md) – store [Traces](/concepts/traces.md) in Delta tables and evaluate with [[scorers|Scorers]].
- [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – attach metadata for request tracking, user sessions, and environment data. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Sources

- trace-agents-deployed-on-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-on-databricks-databricks-on-aws.md](/references/trace-agents-deployed-on-databricks-databricks-on-aws-962e29f6.md)
