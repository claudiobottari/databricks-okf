---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86caf525938eb09ef769f2047c83a52154e292608bd4a136137a258cc433c36b
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-collection-verification
    - MTCV
  citations:
    - file: trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
title: MLflow Trace Collection Verification
description: Programmatic method to verify that traces are being collected from an external deployment by checking MLflow experiment connectivity and searching for recent traces.
tags:
  - mlflow
  - tracing
  - verification
  - debugging
timestamp: "2026-06-19T23:07:51.186Z"
---

# [[mlflow-trace|MLflow Trace]] Collection Verification

**MLflow Trace Collection Verification** is the process of confirming that distributed [Traces](/concepts/traces.md) from production GenAI agents deployed outside of Databricks are being successfully logged to a Databricks workspace. Proper verification ensures that the [MLflow Tracing](/concepts/mlflow-tracing.md) pipeline is correctly configured, authenticated, and actively capturing execution data for observability. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Overview

When an agent is deployed outside of Databricks (for example, in a Docker container or Kubernetes cluster), [Traces](/concepts/traces.md) are sent to a [Databricks Workspace](/concepts/workspace-feature-store-ui.md) via environment-variable configuration. After deployment, verification checks two things: (1) that the [MLflow](/concepts/mlflow.md) client can connect to the workspace, and (2) that [Traces](/concepts/traces.md) are being logged under the expected [MLflow Experiments|experiment](/concepts/mlflow-experiment.md). ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Prerequisites

Before verifying, ensure the following environment variables are set in the deployment environment:

| Variable | Purpose |
|----------|---------|
| `DATABRICKS_HOST` | Databricks workspace URL |
| `DATABRICKS_TOKEN` | Personal access token or service principal token |
| `MLFLOW_TRACKING_URI` | Must be set to `databricks` |
| `MLFLOW_EXPERIMENT_NAME` | Workspace path for the experiment (e.g., `/Shared/production-genai-app`) |

These variables must be accessible to the application at runtime. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Verification Steps

After the agent is deployed and has started generating [Traces](/concepts/traces.md), run the following Python code (either within the same environment or from a notebook that has the same connectivity) to verify collection:

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

- **Connection check**: `client.search_experiments()` confirms that the workspace is reachable and authentication is valid.
- **Traces check**: `mlflow.search_traces()` retrieves recent [Traces](/concepts/traces.md) from the specified experiment. If the returned list has length greater than zero, [Traces](/concepts/traces.md) are being collected. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Next Steps

Once verification confirms that [Traces](/concepts/traces.md) are flowing, you can:

- View traces in the MLflow UI for analysis and debugging.
- Store [Traces](/concepts/traces.md) long-term using [Production Monitoring](/concepts/production-monitoring.md), which syncs [Traces](/concepts/traces.md) to Delta tables every ~15 minutes and removes trace size limits.
- [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) (user/session IDs, custom tags, feedback) to enrich observability.

## Sources

- trace-agents-deployed-outside-of-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-outside-of-databricks-databricks-on-aws.md](/references/trace-agents-deployed-outside-of-databricks-databricks-on-aws-afaae7ad.md)
