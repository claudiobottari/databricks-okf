---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3d69a239c18d5b703a6a40cf38b46207172afe350adb0b108d68562e853e6e2
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-agents-deployment-for-genai-on-databricks
    - CADFGOD
    - Trace agents deployed outside of Databricks
    - trace agents deployed on Databricks
  citations:
    - file: trace-agents-deployed-on-databricks-databricks-on-aws.md
title: Custom Agents Deployment for GenAI on Databricks
description: The recommended deployment method for GenAI applications on Databricks that provides automatic MLflow Tracing with minimal configuration by wrapping agent code with MLflow ResponsesAgent and deploying via agents.deploy().
tags:
  - deployment
  - genai
  - databricks
  - mlflow
timestamp: "2026-06-19T23:07:22.357Z"
---

# Custom Agents Deployment for GenAI on Databricks

**Custom Agents Deployment for GenAI on Databricks** is the recommended method for deploying generative AI applications on the Databricks platform. It enables automatic capture of production [Traces](/concepts/traces.md) via [MLflow Tracing](/concepts/mlflow-tracing.md) without requiring additional configuration. Custom Agents are built using the Databricks Agent Framework and are deployed to [Model Serving](/concepts/model-serving.md) endpoints. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Overview

When you deploy a GenAI application using Custom Agents, [MLflow Tracing](/concepts/mlflow-tracing.md) works automatically. [Traces](/concepts/traces.md) are stored in the agent’s [MLflow Experiment](/concepts/mlflow-experiment.md), allowing real-time viewing in the [MLflow](/concepts/mlflow.md) UI. Optionally, [Traces](/concepts/traces.md) can be stored long-term in Delta tables using [Production Monitoring](/concepts/production-monitoring.md) for durable storage and automated quality assessment. This approach is preferred over custom CPU [Model Serving](/concepts/model-serving.md) because it eliminates manual instrumentation and environment variable setup. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Deploy with Custom Agents (recommended)

To deploy a GenAI application with Custom Agents, follow these steps:

1. **Set up storage locations for [Traces](/concepts/traces.md):**
   - If you plan to use [Production Monitoring](/concepts/production-monitoring.md) to store [Traces](/concepts/traces.md) in Delta tables, ensure it is enabled for your workspace.
   - [Create an [MLflow Experiment](/concepts/mlflow-experiment.md)](https://docs.databricks.com/aws/en/[MLflow](/concepts/mlflow.md)/experiments#create-workspace-experiment) specifically for your application’s production [Traces](/concepts/traces.md).

2. **Instrument and deploy your agent from a Python notebook:**
   - Install the latest version of `mlflow[databricks]`.
   - Connect to the [MLflow Experiment](/concepts/mlflow-experiment.md) using `mlflow.set_experiment(...)`.
   - Wrap your agent code using the MLflow `ResponsesAgent` interface.
   - Enable [MLflow Tracing](/concepts/mlflow-tracing.md) using [automatic](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic) or [manual](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/) instrumentation.
   - Log your agent as an [MLflow](/concepts/mlflow.md) model and register it to [Unity Catalog](/concepts/unity-catalog.md).
   - Ensure that `mlflow` is included in the model’s Python dependencies with the same package version used in your notebook environment.
   - Use `agents.deploy(...)` to deploy the [Unity Catalog](/concepts/unity-catalog.md) model (agent) to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md).

3. **Important note for Git‑associated notebooks:**
   If you are deploying an agent from a notebook stored in a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md), [MLflow 3](/concepts/mlflow-3.md) real‑time tracing does not work by default. To enable it, set the experiment to a non‑Git‑associated experiment using `mlflow.set_experiment()` **before** running `agents.deploy()`.

^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Alternative: Deploy with custom CPU serving

If Custom Agents cannot be used, you can deploy an agent using custom CPU [Model Serving](/concepts/model-serving.md). This method requires manual instrumentation and environment variable configuration. The steps are:

1. Set up the [MLflow Experiment](/concepts/mlflow-experiment.md) and [Production Monitoring](/concepts/production-monitoring.md) (same as above).
2. Log the agent as an [MLflow](/concepts/mlflow.md) model with tracing instrumentation.
3. Deploy the model to a CPU serving endpoint via the UI or API.
4. Configure environment variables on the endpoint:
   - `ENABLE_MLFLOW_TRACING=true`
   - `MLFLOW_EXPERIMENT_ID=<experiment ID>`
   - If using a Service Principal: `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`
   - If using a Personal Access Token: `DATABRICKS_HOST` and `DATABRICKS_TOKEN`

The Service Principal or PAT must have `CAN_EDIT` access to the [MLflow Experiment](/concepts/mlflow-experiment.md).

^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Trace storage

[Traces](/concepts/traces.md) are logged to the [MLflow Experiment](/concepts/mlflow-experiment.md) set via `mlflow.set_experiment(...)`. They are stored as artifacts and can be viewed in real‑time in the [MLflow](/concepts/mlflow.md) UI. You can specify a custom artifact storage location (e.g., a Unity Catalog volume), which governs trace data access through [Unity Catalog](/concepts/unity-catalog.md) volume privileges. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Store [Traces](/concepts/traces.md) long‑term with [Production Monitoring](/concepts/production-monitoring.md)

After [Traces](/concepts/traces.md) are logged to the [MLflow Experiment](/concepts/mlflow-experiment.md), you can enable [Production Monitoring](/concepts/production-monitoring.md) (in beta) to store them in Delta tables for long‑term retention. Key benefits include:

- **Durable storage** beyond the [MLflow Experiment](/concepts/mlflow-experiment.md) artifact lifecycle.
- **No trace size limits** – [Production Monitoring](/concepts/production-monitoring.md) handles [Traces](/concepts/traces.md) of any size.
- **Automated quality assessment** using run [MLflow Scorers](/concepts/mlflow-scorers.md) on production [Traces](/concepts/traces.md).
- **Fast sync** – [Traces](/concepts/traces.md) sync to Delta tables approximately every 15 minutes.

^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Next steps

- View [Traces](/concepts/traces.md) in the [Databricks [MLflow](/concepts/mlflow.md) UI](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/ui-traces).
- Set up [Production Monitoring](/concepts/production-monitoring.md) for long‑term storage and automated evaluation.
- Add [context to [Traces](/concepts/traces.md)](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces) for request tracking, user sessions, and environment metadata.

^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Sources

- trace-agents-deployed-on-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-on-databricks-databricks-on-aws.md](/references/trace-agents-deployed-on-databricks-databricks-on-aws-962e29f6.md)
