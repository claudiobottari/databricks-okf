---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6cb2e8216b9b54b75b5d501aaca1fd04112b3f696b4e2229a76f638d34d45ebf
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
    - tracing-langgraph-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-environment-configuration
    - MTEC
  citations:
    - file: trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
    - file: tracing-langgraph-databricks-on-aws.md
title: MLflow Tracing Environment Configuration
description: Required environment variables (DATABRICKS_HOST, DATABRICKS_TOKEN, MLFLOW_TRACKING_URI, MLFLOW_EXPERIMENT_NAME) to connect an external application to a Databricks workspace for trace collection.
tags:
  - mlflow
  - configuration
  - environment-variables
timestamp: "2026-06-19T23:07:44.399Z"
---

## [MLflow Tracing](/concepts/mlflow-tracing.md) Environment Configuration

**MLflow Tracing Environment Configuration** refers to the set of environment variables and setup steps required to enable [MLflow Tracing for GenAI](/concepts/mlflow-tracing-for-genai.md) agents, particularly when deploying agents outside of Databricks. Proper configuration ensures that trace data is captured and sent to a Databricks workspace for observability and analysis. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md, tracing-langgraph-databricks-on-aws.md]

### Prerequisites

Before configuring tracing, install the required [MLflow](/concepts/mlflow.md) package. The choice depends on the deployment scenario:

- **Production (outside Databricks):** Install `mlflow-tracing` for lightweight trace collection: `%pip install --upgrade mlflow-tracing`.
- **Development/experimentation (inside or outside Databricks):** Install the full [MLflow](/concepts/mlflow.md) package with Databricks extras: `%pip install --upgrade "[MLflow](/concepts/mlflow.md)[databricks]>=3.1"`. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md, tracing-langgraph-databricks-on-aws.md]

For LangGraph, you also need the relevant LangChain/LangGraph packages (e.g., `langgraph`, `langchain_core`, `langchain_openai`). [MLflow 3](/concepts/mlflow-3.md) is recommended for the best tracing experience with LangGraph.

### Environment Variables

Set the following environment variables to connect your application to a Databricks workspace:

```
# Required: Databricks workspace host and authentication token
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-databricks-token"

# Required: Set [[mlflow-tracking-uri|MLflow tracking URI]] to "databricks" to log to Databricks
export MLFLOW_TRACKING_URI=databricks

# Required: Experiment name for organizing [[traces|Traces]] (must be a workspace path)
export MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"
```

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

- For users inside Databricks notebooks, credentials (`DATABRICKS_HOST`, `DATABRICKS_TOKEN`) are automatically set — no explicit configuration is needed. ^[tracing-langgraph-databricks-on-aws.md]
- For production environments, secure API key management (e.g., using [AI Gateway](/concepts/ai-gateway.md) or Databricks secrets) is recommended for LLM provider keys like `OPENAI_API_KEY`. ^[tracing-langgraph-databricks-on-aws.md]

### Deployment Examples

Pass the environment variables to your application container. The following examples show how to configure Docker and Kubernetes.

#### Docker

Dockerfile:
```
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

Run the container with overridden environment variables:
```
docker run -d \
  -e DATABRICKS_HOST="https://your-workspace.cloud.databricks.com" \
  -e DATABRICKS_TOKEN="your-databricks-token" \
  -e MLFLOW_TRACKING_URI=databricks \
  -e MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app" \
  -e APP_VERSION="1.0.0" \
  your-app:latest
```

#### Kubernetes

For Kubernetes, define the environment variables in the pod spec (e.g., using a Secret for `DATABRICKS_TOKEN`). The same set of variables is required. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

### Enabling Tracing for LangGraph

For LangGraph applications, enable [Automatic Tracing](/concepts/automatic-tracing.md) by calling `mlflow.langchain.autolog()`. On serverless compute clusters, autologging is not automatically enabled — you must call this function explicitly. ^[tracing-langgraph-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].langchain.autolog()
```

After configuration, trace data is automatically captured when the LangGraph graph is invoked.

### Verifying Trace Collection

Use the following code to verify that [Traces](/concepts/traces.md) are being collected properly:

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
```

^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

### Long-Term Trace Storage with [Production Monitoring](/concepts/production-monitoring.md)

After [Traces](/concepts/traces.md) are logged to an [MLflow Experiment](/concepts/mlflow-experiment.md), they can be stored long-term in Delta tables using [Production Monitoring](/concepts/production-monitoring.md) (in beta). Benefits include durable storage beyond the experiment artifact lifecycle, no trace size limits, automated quality assessment via [MLflow Scorers](/concepts/mlflow-scorers.md), and fast sync (every ~15 minutes). ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- LangGraph
- LangChain Tracing
- [AI Gateway](/concepts/ai-gateway.md)
- Databricks Secrets

### Sources

- trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
- tracing-langgraph-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-outside-of-databricks-databricks-on-aws.md](/references/trace-agents-deployed-outside-of-databricks-databricks-on-aws-afaae7ad.md)
2. [tracing-langgraph-databricks-on-aws.md](/references/tracing-langgraph-databricks-on-aws-6240217a.md)
