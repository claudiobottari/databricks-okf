---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2bc1ea40453ca7502c1012ae488e0302ab0db34785f5cf6abb72cadb36d42418
  pageDirectory: concepts
  sources:
    - serve-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - querying-model-serving-endpoints-with-databricks-sdk
    - QMSEWDS
    - Deploy a model serving endpoint with Databricks SDK
  citations:
    - file: serve-declarative-features-databricks-on-aws.md
title: Querying Model Serving Endpoints with Databricks SDK
description: Using the Databricks Python SDK's WorkspaceClient.serving_endpoints.query() method to send inference requests with dataframe_records payloads.
tags:
  - sdk
  - model-serving
  - api
timestamp: "2026-06-19T23:02:53.418Z"
---

## Querying [Model Serving](/concepts/model-serving.md) Endpoints with Databricks SDK

**Querying [Model Serving](/concepts/model-serving.md) Endpoints with Databricks SDK** refers to using the `databricks.sdk` Python library to interact with [Databricks Model Serving Endpoints](/concepts/databricks-model-serving-endpoints.md) — sending inference requests and receiving predictions. This approach is the standard way to invoke models deployed through [Unity Catalog](/concepts/unity-catalog.md), especially when those models rely on online feature lookups. ^[serve-declarative-features-databricks-on-aws.md]

### Prerequisites

Before querying, a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) must exist. You can use an existing endpoint or create one programmatically using `w.serving_endpoints.create()` as shown in [Deploy a model serving endpoint with Databricks SDK](/concepts/model-serving-endpoint-databricks.md). The model must be registered in [Unity Catalog](/concepts/unity-catalog.md). ^[serve-declarative-features-databricks-on-aws.md]

### Basic Query

To query an endpoint, instantiate a `WorkspaceClient` and call `w.serving_endpoints.query()`, providing the endpoint name and the input data as a list of records under `dataframe_records`. The following example sends a single record with entity key fields for [Feature Lookup](/concepts/feature-lookup.md):

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
response = w.serving_endpoints.query(
    name="fraud-detection-endpoint",
    dataframe_records=[
        {"user_id": "user_123", "transaction_time": "2026-03-01T12:00:00"},
    ],
)
```

^[serve-declarative-features-databricks-on-aws.md]

The response object contains the model’s prediction output.

### Query with `RequestSource` Features

If the model was trained with `RequestSource` features — columns that are passed directly in the request rather than fetched from an online store — the payload must include all `RequestSource` columns. These columns are part of the [MLflow](/concepts/mlflow.md) model signature captured during `log_model`, so the endpoint’s API schema enforces them. ^[serve-declarative-features-databricks-on-aws.md]

```python
response = w.serving_endpoints.query(
    name="fraud-detection-endpoint",
    dataframe_records=[
        {
            "user_id": "user_123",
            "transaction_time": "2026-03-01T12:00:00",
            "transaction_amount": 275.30,  # [[requestsource|RequestSource]] column
            "vendor_id": "v_42",           # [[requestsource|RequestSource]] column (also used as entity key)
        },
    ],
)
```

^[serve-declarative-features-databricks-on-aws.md]

Entity keys (like `vendor_id` in this example) are used to look up table-backed features from the [online store](/concepts/online-feature-store.md). `RequestSource` columns are passed directly to the model without online lookup. ^[serve-declarative-features-databricks-on-aws.md]

### Query with `curl`

You can also query endpoints using `curl`, which is useful for non-Python workflows or testing. The request must include a valid Databricks API token in the `Authorization` header:

```bash
curl -X POST "https://<workspace>.cloud.databricks.com/serving-endpoints/<endpoint>/invocations" \
  -H "Authorization: Bearer $DATABRICKS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "dataframe_records": [
      {
        "user_id": "user_123",
        "transaction_time": "2026-03-01T12:00:00",
        "transaction_amount": 275.30,
        "vendor_id": "v_42"
      }
    ]
  }'
```

^[serve-declarative-features-databricks-on-aws.md]

### Relevant Endpoints

The primary endpoint type used in this workflow is a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that serves a model registered in [Unity Catalog](/concepts/unity-catalog.md). For feature‑serving scenarios where the model was trained via [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md), Feature Serving endpoints are **not** supported — you must deploy a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) instead. ^[serve-declarative-features-databricks-on-aws.md]

### Related Concepts

- [WorkspaceClient](/concepts/workspaceclient-dbutils.md) — The client class used to interact with Databricks APIs.
- [Unity Catalog](/concepts/unity-catalog.md) — Required for serving models that use [Feature Store](/concepts/feature-store.md) lookups.
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The feature engineering approach that produces models needing [Online Feature Serving](/concepts/online-feature-serving.md).
- [Online Store](/concepts/online-feature-store.md) — The system that serves pre‑computed feature values for real‑time predictions.
- [Create model serving endpoints](/concepts/model-serving-endpoint.md) — How to deploy a new endpoint via SDK or UI.

### Sources

- serve-declarative-features-databricks-on-aws.md

# Citations

1. [serve-declarative-features-databricks-on-aws.md](/references/serve-declarative-features-databricks-on-aws-86fbe897.md)
