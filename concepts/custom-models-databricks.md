---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a45e434817d05b0d1ee782b8ff850266de0bb88f854f524f342e2bc68256b39
  pageDirectory: concepts
  sources:
    - query-serving-endpoints-for-custom-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-models-databricks
    - CM(
  citations:
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
title: Custom Models (Databricks)
description: Traditional ML models or customized Python models packaged in MLflow format, including scikit-learn, XGBoost, PyTorch, and Hugging Face transformers, registered in Unity Catalog or workspace model registry
tags:
  - databricks
  - mlflow
  - model-registry
  - machine-learning
timestamp: "2026-06-19T20:04:33.773Z"
---

# Custom Models (Databricks)

**Custom models** are traditional machine learning models or customized Python models that are packaged in the [MLflow](/concepts/mlflow.md) format and deployed on Databricks [Model Serving](/concepts/model-serving.md). These models are registered either in [Unity Catalog](/concepts/unity-catalog.md) or in the workspace [model registry](/concepts/mlflow-model-registry.md). Examples include scikit-learn, XGBoost, PyTorch, and Hugging Face transformer models. Custom models are distinct from foundation models used for generative AI and LLM workloads. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Requirements

To serve and query a custom model, you must have:

- A [Model Serving Endpoint](/concepts/model-serving-endpoint.md) already created.
- If using the MLflow Deployment SDK, MLflow 2.9 or above is required.
- Scoring requests must be in one of the #supported-scoring-formats|accepted formats.
- To send a request through the REST API or the MLflow Deployment SDK, you must have a Databricks API token.

^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

## Querying Methods and Examples

Model Serving provides several ways to send scoring requests to custom models:

- **REST API** – Send HTTP POST requests to the endpoint’s invocation URL (`https://<databricks-instance>/serving-endpoints/<endpoint-name>/invocations`). Use the Databricks API token for authentication.
- **MLflow Deployments SDK** – Use MLflow’s Python client to query the endpoint.
- **PowerBI** – Connect directly from PowerBI using the endpoint URL.

### Pandas DataFrame Scoring Example

The following example uses the `dataframe_split` format, which is the recommended orientation for preserving column order. The request body contains `columns` and `data` arrays. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

```json
{
  "dataframe_split": {
    "columns": ["sepal length (cm)", "sepal width (cm)"],
    "data": [[5.1, 3.5], [4.9, 3.0]]
  }
}
```

### Tensor Input Example

For models that accept tensor inputs (e.g., TensorFlow or PyTorch), follow the format defined in TensorFlow Serving’s API documentation. Use either `instances` (row format) or `inputs` (columnar format). ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

```json
{"inputs": 5.1, 3.5, 1.4, 0.2}
```

## Supported Scoring Formats

Custom model endpoints accept two categories of input formats: Pandas DataFrame and Tensor.

### Pandas DataFrame Format

Use JSON-serialized Pandas DataFrames with one of these keys:

- **`dataframe_split`** (recommended) – Uses the `split` orientation. Structure: `{"dataframe_split": {"columns": [...], "data": [[...], ...]}}`. Preserves column ordering.
- **`dataframe_records`** – Uses the `records` orientation. Structure: `{"dataframe_records": [{"col1": val, ...}, ...]}`. Does not guarantee column ordering; the `split` format is preferred.

The endpoint response is a JSON object with a `predictions` key containing the model’s output.

```json
{"predictions": [0, 1, 1, 1, 0]}
```

### Tensor Format

Two keys are supported:

- **`instances`** – Row-based format. Use when all input tensors have the same 0‑th dimension. Example: `{"instances": [1, 2, 3]}` or with named tensors.
- **`inputs`** – Columnar format. Use when tensors have different batch sizes. Example: `{"inputs": {"t1": ["a", "b"], "t2": [[1,2,3], [4,5,6]]}}`.

The response follows the same `predictions` structure as the DataFrame format.

## Additional Resources

- Monitor served models using [Unity AI Gateway](/concepts/unity-ai-gateway.md)-enabled inference tables.
- For generative AI and LLM queries, see Foundation Models.
- Refer to the Debugging Guide for Model Serving for troubleshooting.

## Sources

- query-serving-endpoints-for-custom-models-databricks-on-aws.md

# Citations

1. [query-serving-endpoints-for-custom-models-databricks-on-aws.md](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
