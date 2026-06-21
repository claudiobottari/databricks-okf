---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72023308255a87abc10847dd3e36a9c252c30a50c408f169f6c3693733e59a30
  pageDirectory: concepts
  sources:
    - query-serving-endpoints-for-custom-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-dataframe-scoring-format
    - PDSF
    - pandas DataFrames
  citations:
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
title: Pandas DataFrame Scoring Format
description: A JSON-serialized format for scoring requests to Databricks Model Serving endpoints using Pandas DataFrame orientations, supporting both 'dataframe_split' (recommended) and 'dataframe_records' keys
tags:
  - databricks
  - pandas
  - scoring
  - api-format
timestamp: "2026-06-19T20:05:03.207Z"
---

# Pandas DataFrame Scoring Format

**Pandas DataFrame Scoring Format** refers to the structured JSON representation used to send scoring requests for custom models hosted on Databricks Model Serving endpoints. This format enables clients to submit tabular input data in a way that is compatible with traditional ML models and custom Python models packaged in MLflow format. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Overview

When querying a model serving endpoint for a custom model — such as scikit-learn, XGBoost, PyTorch, or Hugging Face transformer models — the scoring request must be formatted as a JSON-serialized Pandas DataFrame. Databricks Model Serving supports two primary orientations for this serialization: `dataframe_split` and `dataframe_records`. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Supported Formats

### `dataframe_split` (Recommended)

The `dataframe_split` format is a JSON-serialized Pandas DataFrame in the `split` orientation. This format explicitly separates the index, columns, and data arrays, ensuring that column ordering is preserved. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

```json
{
  "dataframe_split": {
    "index": [0, 1],
    "columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
    "data": [
      [5.1, 3.5, 1.4, 0.2],
      [4.9, 3.0, 1.4, 0.2]
    ]
  }
}
```

This format is preferred over `dataframe_records` because it guarantees the preservation of column ordering, which is important for models that rely on feature position. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

### `dataframe_records`

The `dataframe_records` format is a JSON-serialized Pandas DataFrame in the `records` orientation. In this format, each row is represented as a JSON object with column names as keys. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

```json
{
  "dataframe_records": [
    {
      "sepal length (cm)": 5.1,
      "sepal width (cm)": 3.5,
      "petal length (cm)": 1.4,
      "petal width (cm)": 0.2
    },
    {
      "sepal length (cm)": 4.9,
      "sepal width (cm)": 3,
      "petal length (cm)": 1.4,
      "petal width (cm)": 0.2
    }
  ]
}
```

**Note:** This format does not guarantee the preservation of column ordering. The `dataframe_split` format is preferred over the `records` format. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Response Format

The response from the endpoint contains the output from the model, serialized with JSON and wrapped in a `predictions` key. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

```json
{
  "predictions": [0, 1, 1, 1, 0]
}
```

## Sending Requests

To send a scoring request using the DataFrame format, use the endpoint URL in the form `https://<databricks-instance>/serving-endpoints/<endpoint-name>/invocations` along with a valid Databricks REST API token. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

Example using curl with `dataframe_split` format:

```bash
curl -X POST -u token:$DATABRICKS_API_TOKEN $ENDPOINT_INVOCATION_URL \
  -H 'Content-Type: application/json' \
  -d '{"dataframe_split": [{
    "columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
    "data": [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2]]
    }]
  }'
```

## Requirements

- A [Model Serving Endpoint](/concepts/model-serving-endpoint.md) must be created and deployed.
- For the [MLflow Deployment SDK](/concepts/mlflow-deployment-sdk.md), MLflow 2.9 or above is required.
- A valid Databricks API token is needed for REST API or SDK access.
- The request must use `Content-Type: application/json`. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Related Concepts

- Custom Models — Traditional ML or customized Python models in MLflow format
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The deployment infrastructure for serving models
- [Tensor Input Scoring Format](/concepts/tensor-input-scoring-format.md) — Alternative format for tensor-based models
- Foundation Model Scoring — Query format for generative AI and LLM workloads
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Model storage and versioning in Unity Catalog or workspace registry
- [Model Monitoring with Inference Tables](/concepts/production-ml-monitoring-with-inference-tables.md) — Monitoring served models using Unity AI Gateway

## Sources

- query-serving-endpoints-for-custom-models-databricks-on-aws.md

# Citations

1. [query-serving-endpoints-for-custom-models-databricks-on-aws.md](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
