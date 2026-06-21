---
title: Trace agents deployed on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing
ingestedAt: "2026-06-18T08:18:05.900Z"
---

This page shows how to deploy GenAI applications on Databricks so that production traces are captured automatically.

For apps deployed outside Databricks, see [Trace agents deployed outside of Databricks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing-external).

You can deploy GenAI applications on Databricks using [Custom Agents](https://docs.databricks.com/aws/en/generative-ai/agent-framework/build-agents) (recommended) or custom CPU Model Serving. Regardless of which deployment method you choose, Databricks logs traces to your MLflow experiment for real-time viewing. You can optionally store traces long-term in Delta tables using [Production Monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) for durable storage and automated quality assessment.

![MLflow production tracing overview](https://docs.databricks.com/aws/en/assets/images/prod-tracing-overview-378230532faf6af7ec8b70b4f920135c.png)

## Deploy with Custom Agents (recommended)[​](#-deploy-with-custom-agents-recommended "Direct link to -deploy-with-custom-agents-recommended")

When you deploy GenAI applications using [Custom Agents](https://docs.databricks.com/aws/en/generative-ai/agent-framework/build-agents), MLflow Tracing works automatically without additional configuration. Traces are stored in the agent's MLflow experiment.

Set up the storage location(s) for traces:

1.  If you plan to use [Production Monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) to store traces in Delta tables, then ensure it is enabled for your workspace.
2.  [Create an MLflow Experiment](https://docs.databricks.com/aws/en/mlflow/experiments#create-workspace-experiment) for storing your app's production traces.

Next, in your Python notebook, instrument your agent with MLflow Tracing, and use Custom Agents to deploy your agent:

1.  Install the latest version of `mlflow[databricks]` in your Python environment.
2.  Connect to the MLflow Experiment using [`mlflow.set_experiment(...)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_experiment).
3.  Wrap your agent code using [MLflow `ResponsesAgent`](https://docs.databricks.com/aws/en/generative-ai/agent-framework/author-agent-model-serving). In your agent code, enable MLflow Tracing using [automatic](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic) or [manual](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/) instrumentation.
4.  Log your agent as an MLflow model, and register it to Unity Catalog.
5.  Ensure that `mlflow` is in the model's Python dependencies, with the same package version used in your notebook environment.
6.  Use `agents.deploy(...)` to deploy the Unity Catalog model (agent) to a Model Serving endpoint.

note

If you are deploying an agent from a notebook stored in a [Databricks Git folder](https://docs.databricks.com/aws/en/repos/), MLflow 3 real-time tracing does not work by default.

To enable real-time tracing, set the experiment to a non-Git-associated experiment using [`mlflow.set_experiment()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=set_experiment#mlflow.set_experiment) before running `agents.deploy()`.

This notebook demonstrates the deployment steps above.

#### Custom Agents and MLflow Tracing notebook

## Deploy with custom CPU serving (alternative)[​](#-deploy-with-custom-cpu-serving-alternative "Direct link to -deploy-with-custom-cpu-serving-alternative")

If you can't use Custom Agents, deploy your agent using custom CPU Model Serving instead.

First, set up the storage location(s) for traces:

1.  If you plan to use [Production Monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) to store traces in Delta tables, then ensure it is enabled for your workspace.
2.  [Create an MLflow Experiment](https://docs.databricks.com/aws/en/mlflow/experiments#create-workspace-experiment) for storing your app's production traces.

Next, in your Python notebook, instrument your agent with MLflow Tracing, and use the Model Serving UI or APIs to deploy your agent:

1.  Log your agent as an MLflow model with [automatic](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic) or [manual](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/) tracing instrumentation.
2.  Deploy the model to CPU serving.
3.  Provision a Service Principal or Personal Access Token (PAT) with `CAN_EDIT` access to the MLflow experiment.
4.  In the CPU serving endpoint page, go to "Edit endpoint." For each deployed model to trace, add the following environment variables:
5.  `ENABLE_MLFLOW_TRACING=true`
6.  `MLFLOW_EXPERIMENT_ID=<ID of the experiment you created>`
7.  If you provisioned a Service Principal, set `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`. If you provisioned a PAT, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN`.

## Trace storage[​](#trace-storage "Direct link to Trace storage")

Databricks logs traces to the MLflow experiment that you set with [`mlflow.set_experiment(...)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_experiment) during deployment. Traces are available for real-time viewing in the MLflow UI.

Traces are stored as artifacts, for which you can specify a custom storage location. For example, if you [create a workspace experiment](https://docs.databricks.com/aws/en/mlflow/experiments#create-experiment-from-the-workspace) with `artifact_location` set to a Unity Catalog volume, then trace data access is governed by [Unity Catalog volume privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#read-volume).

## Store traces long-term with Production Monitoring[​](#-store-traces-long-term-with-production-monitoring "Direct link to -store-traces-long-term-with-production-monitoring")

After traces are logged to your MLflow experiment, you can optionally store them long-term in Delta tables using [Production Monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) (in beta).

Benefits of Production Monitoring for trace storage:

*   **Durable storage**: Store traces in Delta tables for long-term retention beyond the MLflow experiment artifact lifecycle.
*   **No trace size limits**: Unlike alternative storage methods, Production Monitoring handles traces of any size.
*   **Automated quality assessment**: Run MLflow scorers on production traces to continuously monitor application quality.
*   **Fast sync**: Traces sync to Delta tables approximately every 15 minutes.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [View traces in the Databricks MLflow UI](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/ui-traces) - View traces in the MLflow UI.
*   [Production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Store traces in Delta tables for long-term retention and automatically evaluate with scorers.
*   [Add context to traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces) - Attach metadata for request tracking, user sessions, and environment data.
