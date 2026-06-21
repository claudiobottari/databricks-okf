---
title: Trace agents deployed outside of Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing-external
ingestedAt: "2026-06-18T08:18:08.037Z"
---

MLflow Tracing provides comprehensive observability for production GenAI agents deployed outside of Databricks by capturing execution details and sending them to your Databricks workspace, where you can view them in the MLflow UI.

![MLflow production tracing for external deployment](https://docs.databricks.com/aws/en/assets/images/prod-tracing-overview-external-3aa5beb9ecab0b86f5efa87225face3b.png)

This page covers deploying agents outside of Databricks with tracing enabled. If your agent is deployed using Databricks Model Serving, see [Deploy with Custom Agents (recommended)](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing#deploy-apps-with-tracing).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Install the required packages. The following table describes your options:

Python

    ## Install mlflow-tracing for production deployment tracing%pip install --upgrade mlflow-tracing## Install mlflow for experimentation and development%pip install --upgrade "mlflow[databricks]>=3.1"

## Basic tracing setup[​](#basic-tracing-setup "Direct link to Basic tracing setup")

Configure your application deployment to connect to your Databricks workspace so Databricks can collect traces.

Configure the following environment variables:

Bash

    # Required: Set the Databricks workspace host and authentication tokenexport DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-databricks-token"# Required: Set MLflow Tracking URI to "databricks" to log to Databricksexport MLFLOW_TRACKING_URI=databricks# Required: Configure the experiment name for organizing traces (must be a workspace path)export MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"

### Deployment examples[​](#deployment-examples "Direct link to Deployment examples")

After the environment variables are set, pass them to your application. Click the tabs to see how to pass the connection details to different frameworks.

*   Docker
*   Kubernetes

For Docker deployments, pass the environment variables through the container configuration:

Dockerfile

    # DockerfileFROM python:3.11-slim# Install dependenciesCOPY requirements.txt .RUN pip install -r requirements.txt# Copy application codeCOPY . /appWORKDIR /app# Set default environment variables (can be overridden at runtime)ENV DATABRICKS_HOST=""ENV DATABRICKS_TOKEN=""ENV MLFLOW_TRACKING_URI=databricksENV MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"CMD ["python", "app.py"]

Run the container with environment variables:

Bash

    docker run -d \  -e DATABRICKS_HOST="https://your-workspace.cloud.databricks.com" \  -e DATABRICKS_TOKEN="your-databricks-token" \  -e MLFLOW_TRACKING_URI=databricks \  -e MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app" \  -e APP_VERSION="1.0.0" \  your-app:latest

### Verify trace collection[​](#verify-trace-collection "Direct link to Verify trace collection")

After deploying your app, verify that traces are collected properly:

Python

    import mlflowfrom mlflow.client import MlflowClientimport os# Ensure MLflow is configured for Databricksmlflow.set_tracking_uri("databricks")# Check connection to MLflow serverclient = MlflowClient()try:    # List recent experiments to verify connectivity    experiments = client.search_experiments()    print(f"Connected to MLflow. Found {len(experiments)} experiments.")    # Check if traces are being logged    traces = mlflow.search_traces(        experiment_names=[os.getenv("MLFLOW_EXPERIMENT_NAME", "/Shared/production-genai-app")],        max_results=5    )    print(f"Found {len(traces)} recent traces.")except Exception as e:    print(f"Error connecting to MLflow: {e}")    print(f"Check your authentication and connectivity")

## Store traces long-term with Production Monitoring[​](#store-traces-long-term-with-production-monitoring "Direct link to Store traces long-term with Production Monitoring")

After traces are logged to your MLflow experiment, you can store them long-term in Delta tables using [Production Monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) (in beta).

Benefits of Production Monitoring for trace storage:

*   **Durable storage**: Store traces in Delta tables for long-term retention beyond the MLflow experiment artifact lifecycle.
*   **No trace size limits**: Unlike alternative storage methods, Production Monitoring handles traces of any size.
*   **Automated quality assessment**: Run MLflow scorers on production traces to continuously monitor application quality.
*   **Fast sync**: Traces sync to Delta tables approximately every 15 minutes.

## Next steps[​](#next-steps "Direct link to Next steps")

After your agent is deployed with trace logging to the Databricks MLflow server, you can view, augment, and analyze your traces:

*   [View traces in the Databricks MLflow UI](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/ui-traces) - View traces in the MLflow UI.
*   [Production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Store traces in Delta tables for long-term retention and automatically evaluate with scorers.
*   [Add context to traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces), including user or session IDs, custom tags, or user feedback for better debugging and insights.
