---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44a0696b3283646138e741379ee0d3e9c64f7a3e1e9fb48e8e25d7a500e1c52b
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-production-tracing-for-external-deployments
    - MPTFED
    - MLflow Tracing with External Deployments
  citations:
    - file: trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
title: MLflow Production Tracing for External Deployments
description: Framework for capturing execution traces from GenAI agents deployed outside Databricks and sending them to a Databricks workspace for observability in the MLflow UI.
tags:
  - mlflow
  - tracing
  - genai
  - observability
timestamp: "2026-06-19T23:07:38.543Z"
---

# [MLflow](/concepts/mlflow.md) Production Tracing for External Deployments

**MLflow Production Tracing for External Deployments** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that provides comprehensive observability for production [GenAI](/concepts/mlflow-genai-evaluate-api.md) agents deployed outside of Databricks. It captures execution details — such as inference calls, tool invocations, and intermediate results — and sends them to your Databricks workspace, where you can view and analyze them in the [MLflow UI](/concepts/mlflow.md). This enables you to monitor and debug agents running on any infrastructure while centralizing trace storage in Databricks. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Prerequisites

To use production tracing for external deployments, install the required packages:

```python
## Install mlflow-tracing for production deployment tracing
%pip install --upgrade mlflow-tracing

## Install [[mlflow|MLflow]] for experimentation and development
%pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1"
```

The `mlflow-tracing` package is specifically intended for production logging; the `mlflow[databricks]` package is used during experimentation and development. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Basic Tracing Setup

Configure your application deployment to connect to your Databricks workspace by setting the following environment variables:

```bash
# Required: Set the Databricks workspace host and authentication token
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-databricks-token"

# Required: Set [[mlflow-tracking-uri|MLflow tracking URI]] to "databricks" to log to Databricks
export MLFLOW_TRACKING_URI=databricks

# Required: Configure the experiment name for organizing [[traces|Traces]] (must be a workspace path)
export MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"
```

These variables tell the [MLflow](/concepts/mlflow.md) client where to send [Traces](/concepts/traces.md) and under which [MLflow Experiment](/concepts/mlflow-experiment.md) to organize them. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

### Deployment Examples

After the environment variables are set, pass them to your application container at runtime. The following examples show how to provide the connection details for different deployment frameworks.

#### Docker

Create a `Dockerfile` that sets default environment variables (which can be overridden at runtime):

```dockerfile
FROM python:3.11-slim
# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy application code
COPY . /app
WORKDIR /app
# Set default environment variables (can be overridden at runtime)
ENV DATABRICKS_HOST=""
ENV DATABRICKS_TOKEN=""
ENV MLFLOW_TRACKING_URI=databricks
ENV MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"
CMD ["python", "app.py"]
```

Run the container with the environment variables set:

```bash
docker run -d \
  -e DATABRICKS_HOST="https://your-workspace.cloud.databricks.com" \
  -e DATABRICKS_TOKEN="your-databricks-token" \
  -e MLFLOW_TRACKING_URI=databricks \
  -e MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app" \
  -e APP_VERSION="1.0.0" \
  your-app:latest
```

The same approach can be applied to Kubernetes deployments by setting the environment variables in the pod or deployment specification. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

### Verify Trace Collection

After deploying your application, verify that [Traces](/concepts/traces.md) are being collected properly using the following code:

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].client import MlflowClient
import os

# Ensure [[mlflow|MLflow]] is configured for Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")

# Check connection to [[mlflow|MLflow]] server
client = MlflowClient()
try:
    # List recent experiments to verify connectivity
    experiments = client.search_experiments()
    print(f"Connected to [[mlflow|MLflow]]. Found {len(experiments)} experiments.")

    # Check if [[traces|Traces]] are being logged
    [[traces|Traces]] = [[mlflow|MLflow]].search_traces(
        experiment_names=[os.getenv("MLFLOW_EXPERIMENT_NAME", "/Shared/production-genai-app")],
        max_results=5
    )
    print(f"Found {len([[traces|Traces]])} recent [[traces|Traces]].")
except Exception as e:
    print(f"Error connecting to [[mlflow|MLflow]]: {e}")
    print(f"Check your authentication and connectivity")
```

This script confirms that your application can reach the Databricks workspace and that [Traces](/concepts/traces.md) are being logged to the specified experiment. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Store [Traces](/concepts/traces.md) Long‑Term with [Production Monitoring](/concepts/production-monitoring.md)

After [Traces](/concepts/traces.md) are logged to your [MLflow Experiment](/concepts/mlflow-experiment.md), you can store them long‑term in [Delta tables](/concepts/delta-lake-table.md) using [Production Monitoring](/concepts/production-monitoring.md) (in beta). This approach offers several benefits:

- **Durable storage**: [Traces](/concepts/traces.md) are kept in Delta tables beyond the lifecycle of the [MLflow Experiment](/concepts/mlflow-experiment.md) artifacts.
- **No trace size limits**: Unlike alternative storage methods, [Production Monitoring](/concepts/production-monitoring.md) handles [Traces](/concepts/traces.md) of any size.
- **Automated quality assessment**: [MLflow Scorers](/concepts/mlflow-scorers.md) can run on production [Traces](/concepts/traces.md) to continuously monitor application quality.
- **Fast sync**: [Traces](/concepts/traces.md) sync to Delta tables approximately every 15 minutes.

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Next Steps

After your agent is deployed with trace logging to the Databricks [MLflow](/concepts/mlflow.md) server, you can view, augment, and analyze your [Traces](/concepts/traces.md):

- View traces in the Databricks MLflow UI – Observing [Traces](/concepts/traces.md) in the [MLflow](/concepts/mlflow.md) UI.
- [Production Monitoring](/concepts/production-monitoring.md) – Storing [Traces](/concepts/traces.md) in Delta tables for long‑term retention and automatically evaluating with [[scorers|Scorers]].
- [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – Including user or session IDs, custom tags, or user feedback for better debugging and insights.

For agents deployed using [Databricks Model Serving](/concepts/databricks-model-serving.md), see the dedicated guide on deploying with custom agents. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Sources

- trace-agents-deployed-outside-of-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-outside-of-databricks-databricks-on-aws.md](/references/trace-agents-deployed-outside-of-databricks-databricks-on-aws-afaae7ad.md)
