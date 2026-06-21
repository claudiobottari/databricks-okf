---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97ee23713e1325981332e7687f6fe57833c5d25dfc496f437939620357043494
  pageDirectory: concepts
  sources:
    - query-serving-endpoints-for-custom-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-deployment-sdk
    - MDS
    - MLflow Deployment API
    - MLflow Deployments
    - MLflow Deployments API
    - MLflow deployments
  citations:
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
title: MLflow Deployment SDK
description: A Python SDK (MLflow 2.9+) for interacting with Databricks Model Serving endpoints programmatically, used to send scoring requests alongside REST API and PowerBI connectors
tags:
  - databricks
  - mlflow
  - sdk
  - deployment
timestamp: "2026-06-19T20:04:48.709Z"
---

## MLflow Deployment SDK

The **MLflow Deployment SDK** is a Python client library, included with [MLflow](/concepts/mlflow.md) 2.9 and later, that provides a programmatic interface for sending scoring requests to [model serving endpoints](/concepts/model-serving-endpoint.md) on Databricks. It is one of several querying methods available alongside the REST API and PowerBI. The SDK is intended for custom models — traditional ML models or custom Python models packaged in the MLflow format — and can be used to invoke endpoints that serve models registered in Unity Catalog or the workspace model registry. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

### Requirements

To use the MLflow Deployment SDK, the following prerequisites must be met:

- A model serving endpoint must already exist and be running. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]
- MLflow version **2.9 or above** is required for the SDK to be available. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]
- A Databricks API token is mandatory to authenticate requests sent through the SDK (or via the REST API). ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

### Usage

The SDK can be used to submit scoring requests in any of the supported scoring formats for custom models, including Pandas DataFrame formats (`dataframe_split`, `dataframe_records`) and tensor input formats (`instances`, `inputs`). The request and response format details are identical to those used by the REST API; the SDK simply wraps the HTTP calls behind a Python interface.

The following example (illustrative) shows how one would typically instantiate the client and query an endpoint:

```python
import mlflow
from mlflow.deployments import get_deploy_client

client = get_deploy_client("databricks")
response = client.predict(
    endpoint="<endpoint-name>",
    inputs={"dataframe_split": {
        "columns": ["feature1", "feature2"],
        "data": [[1.0, 2.0], [3.0, 4.0]]
    }}
)
print(response.predictions)
```

*Note: The exact method signature may vary; refer to the official MLflow documentation for the current API.*

The endpoint invocation URL and token are configured automatically by the SDK when the Databricks environment is properly set up (using `databricks-cli` or environment variables). If running outside of a Databricks workspace, the token and workspace URL must be provided explicitly via configuration.

### Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The serving infrastructure that hosts the model.
- [custom models](/concepts/custom-mlflow-pythonmodel.md) – MLflow-packaged models that can be served via these endpoints.
- Databricks API token – Required for authentication with the SDK.
- supported scoring formats for custom models – Detailed format specifications for `dataframe_split`, `dataframe_records`, `instances`, and `inputs`.

### Sources

- query-serving-endpoints-for-custom-models-databricks-on-aws.md

# Citations

1. [query-serving-endpoints-for-custom-models-databricks-on-aws.md](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
