---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70eb1f486bc48b1c0218e1b6a8488d2eab12f9f5fe2b24bce07fdd9bea065a4e
  pageDirectory: concepts
  sources:
    - serve-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - requestsource-features
  citations:
    - file: serve-declarative-features-databricks-on-aws.md
title: RequestSource Features
description: Features passed directly in the request payload at inference time rather than looked up from an online store; these columns are added to the MLflow model signature during log_model.
tags:
  - machine-learning
  - feature-store
  - inference
timestamp: "2026-06-19T23:02:51.738Z"
---

# [RequestSource](/concepts/requestsource.md) Features

**RequestSource Features** are features that are provided directly in the request payload when querying a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), rather than being looked up from an online [Feature Store](/concepts/feature-store.md). These features are marked as `RequestSource` during model training and are recorded in the [MLflow](/concepts/mlflow.md) model signature, making them required fields in the inference API. ^[serve-declarative-features-databricks-on-aws.md]

## Overview

When a model is trained using Databricks [Feature Store](/concepts/feature-store.md), features can originate from two sources: table-backed [Feature Tables](/concepts/feature-tables.md) (which are looked up from an online store at serving time) and `RequestSource` features, which are supplied by the client in the API call. `RequestSource` columns are added to the model signature during `log_model`, so the [Model Serving Endpoint](/concepts/model-serving-endpoint.md)'s API schema automatically reflects them as required input fields. ^[serve-declarative-features-databricks-on-aws.md]

Entity keys, by contrast, are used to look up table-backed features from the online store. `RequestSource` columns bypass the [Feature Store](/concepts/feature-store.md) lookup and are passed through directly to the model. ^[serve-declarative-features-databricks-on-aws.md]

## Serving Models with [RequestSource](/concepts/requestsource.md) Features

[Feature Serving endpoints](/concepts/feature-serving-endpoint.md) are not supported for [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md). Instead, to serve features online, deploy a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using a model that is logged through [Unity Catalog](/concepts/unity-catalog.md). The model must be registered in [Unity Catalog](/concepts/unity-catalog.md). ^[serve-declarative-features-databricks-on-aws.md]

Models that are trained using features from Databricks automatically track lineage to the features they were trained on. When deployed as [Model Serving](/concepts/model-serving.md) endpoints, these models use [Unity Catalog](/concepts/unity-catalog.md) to look up features from online stores—except for `RequestSource` features, which are provided at query time. ^[serve-declarative-features-databricks-on-aws.md]

## Querying an Endpoint with [RequestSource](/concepts/requestsource.md) Features

When querying a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), the request payload must include all `RequestSource` columns that were part of the model signature. The following example shows a payload for a fraud detection model that includes both entity keys (`user_id`, `transaction_time`) and `RequestSource` columns (`transaction_amount`, `vendor_id`):

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
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

The same request can be made via `curl`:

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

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Centralized feature management and serving.
- [Model Serving](/concepts/model-serving.md) – Deploying models as REST endpoints.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and metadata catalog for features and models.
- [MLflow](/concepts/mlflow.md) – Tracks model signatures and feature lineage.
- Entity Keys – Identifiers used for online feature lookups.
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) – A deployment method incompatible with Feature Serving endpoints.

## Sources

- serve-declarative-features-databricks-on-aws.md

# Citations

1. [serve-declarative-features-databricks-on-aws.md](/references/serve-declarative-features-databricks-on-aws-86fbe897.md)
