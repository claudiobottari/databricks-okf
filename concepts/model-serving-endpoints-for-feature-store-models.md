---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c5416fecef4d32792ee2b90f7b330115943d1a345332e2b499a238843487079
  pageDirectory: concepts
  sources:
    - serve-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoints-for-feature-store-models
    - MSEFFSM
  citations:
    - file: serve-declarative-features-databricks-on-aws.md
title: Model Serving Endpoints for Feature Store Models
description: How to deploy and query models trained using Databricks Feature Store as model serving endpoints using Unity Catalog for online feature lookup.
tags:
  - machine-learning
  - model-serving
  - feature-store
timestamp: "2026-06-19T23:02:39.761Z"
---

# [Model Serving](/concepts/model-serving.md) Endpoints for [Feature Store](/concepts/feature-store.md) Models

**Model Serving Endpoints for [Feature Store](/concepts/feature-store.md) Models** allow you to deploy models that were trained using features from Databricks [Feature Store](/concepts/feature-store.md) as real-time inference endpoints. When such a model is deployed, the serving endpoint automatically uses [Unity Catalog](/concepts/unity-catalog.md) to look up the required features from online stores at inference time. ^[serve-declarative-features-databricks-on-aws.md]

## Overview

Models trained with features from [Databricks Feature Store](/concepts/databricks-feature-store.md) automatically track lineage to the features they were trained on. This lineage enables the serving infrastructure to resolve feature values from online stores when the model receives a request. To serve features online, you must deploy a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using a model that was logged through [Unity Catalog](/concepts/unity-catalog.md). Declarative Feature Engineering is not supported for Feature Serving endpoints. ^[serve-declarative-features-databricks-on-aws.md]

## Deploying a [Model Serving Endpoint](/concepts/model-serving-endpoint.md)

You can use an existing [Model Serving Endpoint](/concepts/model-serving-endpoint.md) or create a new one using the Databricks SDK. The model must be registered in [Unity Catalog](/concepts/unity-catalog.md). The following Python example demonstrates creating a new endpoint with the SDK:

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

w = WorkspaceClient()
endpoint_name = "fraud-detection-endpoint"
model_name = "main.ecommerce.fraud_model"

w.serving_endpoints.create(
    name=endpoint_name,
    config=EndpointCoreConfigInput(
        name=endpoint_name,
        served_entities=[
            ServedEntityInput(
                entity_name=model_name,
                entity_version=1,
                max_provisioned_concurrency=4,
                min_provisioned_concurrency=0,
            )
        ],
    ),
)
```

^[serve-declarative-features-databricks-on-aws.md]

For further details, see [Create custom [Model Serving](/concepts/model-serving.md) endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints). ^[serve-declarative-features-databricks-on-aws.md]

## Querying the Endpoint

Once deployed, you can query the endpoint by providing a payload that includes the entity keys used for [Feature Lookup](/concepts/feature-lookup.md). The following example uses the Databricks SDK to send inference requests:

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

## Querying with [RequestSource Features](/concepts/requestsource-features.md)

If the model was trained with `RequestSource` features, the request payload must also include all `RequestSource` columns. These columns are part of the [MLflow](/concepts/mlflow.md) model signature that was recorded during `log_model`, so the serving endpoint’s API schema reflects the required fields. ^[serve-declarative-features-databricks-on-aws.md]

Entity keys are used for looking up table-backed features from the online store, while `RequestSource` columns are passed directly to the model without an online store lookup. The example below shows a payload that includes both entity keys and `RequestSource` columns:

```python
response = w.serving_endpoints.query(
    name="fraud-detection-endpoint",
    dataframe_records=[
        {
            "user_id": "user_123",
            "transaction_time": "2026-03-01T12:00:00",
            "transaction_amount": 275.30,   # [[requestsource|RequestSource]] column
            "vendor_id": "v_42",            # [[requestsource|RequestSource]] column (also used as entity key)
        },
    ],
)
```

^[serve-declarative-features-databricks-on-aws.md]

You can also query the endpoint using `curl`:

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

- [Feature Store](/concepts/feature-store.md) – Central repository for feature definitions and lineage.
- [Unity Catalog](/concepts/unity-catalog.md) – Catalog that stores feature metadata and enables [Feature Lookup](/concepts/feature-lookup.md).
- [MLflow](/concepts/mlflow.md) – Framework for model logging and signature management.
- [Model Serving](/concepts/model-serving.md) – General infrastructure for deploying models as endpoints.
- [Online Store](/concepts/online-feature-store.md) – Low-latency storage for feature values used at inference time.
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) – Alternative feature creation approach (not supported for feature serving endpoints).

## Sources

- serve-declarative-features-databricks-on-aws.md

# Citations

1. [serve-declarative-features-databricks-on-aws.md](/references/serve-declarative-features-databricks-on-aws-86fbe897.md)
