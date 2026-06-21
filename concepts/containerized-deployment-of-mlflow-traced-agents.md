---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2b204e11646beade79a68721bb0078d0b2b6e57df3d181812e27b48a31e1586
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - containerized-deployment-of-mlflow-traced-agents
    - CDOMTA
  citations:
    - file: trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
title: Containerized Deployment of MLflow Traced Agents
description: Patterns for passing MLflow tracing configuration environment variables to Docker and Kubernetes deployments so external GenAI agents can send traces to Databricks.
tags:
  - mlflow
  - docker
  - kubernetes
  - deployment
timestamp: "2026-06-19T23:07:47.474Z"
---

# Containerized Deployment of [MLflow](/concepts/mlflow.md) Traced Agents

**Containerized Deployment of [MLflow](/concepts/mlflow.md) Traced Agents** refers to the practice of packaging a Generative AI (GenAI) application with [MLflow Tracing](/concepts/mlflow-tracing.md) enabled and deploying it outside of Databricks using container runtimes such as Docker or Kubernetes. This setup captures execution details ([Traces](/concepts/traces.md)) from the agent and sends them to a Databricks workspace, where they can be viewed in the [MLflow UI](/concepts/mlflow.md). ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

The approach is useful for production agents that are not deployed via [Databricks Model Serving](/concepts/databricks-model-serving.md) but still require the observability and debugging capabilities provided by [MLflow Tracing](/concepts/mlflow-tracing.md). ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Prerequisites

Install the required Python packages. For production tracing, use `mlflow-tracing`; for experimentation and development, install the full `mlflow` package with Databricks support:

```python
# For production deployment tracing
%pip install --upgrade mlflow-tracing

# For development and experimentation
%pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1"
```

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Basic Tracing Setup

To enable trace collection, the containerized application must be configured with environment variables that connect to a Databricks workspace. The following variables are required:

- `DATABRICKS_HOST` – The workspace URL.
- `DATABRICKS_TOKEN` – An authentication token for the workspace.
- `MLFLOW_TRACKING_URI` – Must be set to `databricks`.
- `MLFLOW_EXPERIMENT_NAME` – An experiment path in the workspace (e.g., `/Shared/production-genai-app`) to organize [Traces](/concepts/traces.md).

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-databricks-token"
export MLFLOW_TRACKING_URI=databricks
export MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"
```

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Container Deployment Examples

After the environment variables are set, they must be passed to the container at runtime. The source provides examples for Docker and Kubernetes:

### Docker

Define environment variables in the Dockerfile and override them when running the container:

```dockerfile
FROM python:3.11-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENV DATABRICKS_HOST=""
ENV DATABRICKS_TOKEN=""
ENV MLFLOW_TRACKING_URI=databricks
ENV MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"

CMD ["python", "app.py"]
```

Run the container with the required variables:

```bash
docker run -d \
  -e DATABRICKS_HOST="https://your-workspace.cloud.databricks.com" \
  -e DATABRICKS_TOKEN="your-databricks-token" \
  -e MLFLOW_TRACKING_URI=databricks \
  -e MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app" \
  -e APP_VERSION="1.0.0" \
  your-app:latest
```

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

### Kubernetes

(Not shown in the source, but the same environment variables can be passed via a `ConfigMap` or `Secret` in a pod specification. The source includes a Kubernetes tab but its contents are omitted in the extracted material; the Docker tab is the primary example provided.)

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Verify Trace Collection

After deployment, verify that [Traces](/concepts/traces.md) are being collected by running a connectivity check from within the application environment:

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].client import MlflowClient
import os

[[mlflow|MLflow]].set_tracking_uri("databricks")
client = MlflowClient()

try:
    experiments = client.search_experiments()
    print(f"Connected to [[mlflow|MLflow]]. Found {len(experiments)} experiments.")

    [[traces|Traces]] = [[mlflow|MLflow]].search_traces(
        experiment_names=[os.getenv("MLFLOW_EXPERIMENT_NAME", "/Shared/production-genai-app")],
        max_results=5
    )
    print(f"Found {len([[traces|Traces]])} recent [[traces|Traces]].")
except Exception as e:
    print(f"Error connecting to [[mlflow|MLflow]]: {e}")
    print("Check your authentication and connectivity")
```

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Store [Traces](/concepts/traces.md) Long-Term with [Production Monitoring](/concepts/production-monitoring.md)

After [Traces](/concepts/traces.md) are logged to the [MLflow Experiment](/concepts/mlflow-experiment.md), they can be stored durably in [Delta tables](/concepts/delta-lake-table.md) using [Production Monitoring](/concepts/production-monitoring.md) (beta). Benefits include:

- **Durable storage**: [Traces](/concepts/traces.md) are retained beyond the [MLflow Experiment](/concepts/mlflow-experiment.md) artifact lifecycle.
- **No trace size limits**: [Production Monitoring](/concepts/production-monitoring.md) handles [Traces](/concepts/traces.md) of any size.
- **Automated quality assessment**: [MLflow Scorers](/concepts/mlflow-scorers.md) can be applied to continuously monitor application quality.
- **Fast sync**: [Traces](/concepts/traces.md) sync to Delta tables approximately every 15 minutes.

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Next Steps

After the agent is deployed with trace logging, you can:

- View [Traces](/concepts/traces.md) in the [MLflow UI](/concepts/mlflow.md).
- Use [Production Monitoring](/concepts/production-monitoring.md) to store [Traces](/concepts/traces.md) long-term and evaluate with [[scorers|Scorers]].
- Add context to traces—such as user IDs, [session IDs](/concepts/session-id-tracing.md), custom tags, or [user feedback](/concepts/multi-dimensional-user-feedback.md)—for better debugging and insights.

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The tracing system used to capture execution details.
- [Production Monitoring](/concepts/production-monitoring.md) – Long-term trace storage and automated evaluation.
- [MLflow experiments](/concepts/mlflow-experiment.md) – Organizational unit for [Traces](/concepts/traces.md) and runs.
- [Databricks Model Serving](/concepts/databricks-model-serving.md) – Alternative deployment method with built-in tracing support.
- Environment variables for MLflow – Configuration variables required for tracing setup.
- GenAI agents – The application type being traced.
- [Delta tables](/concepts/delta-lake-table.md) – Storage format for long-term trace data.
- [MLflow UI](/concepts/mlflow.md) – Interface for viewing [Traces](/concepts/traces.md) and experiment data.

## Sources

- trace-agents-deployed-outside-of-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-outside-of-databricks-databricks-on-aws.md](/references/trace-agents-deployed-outside-of-databricks-databricks-on-aws-afaae7ad.md)
