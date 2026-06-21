---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 901b8f25b2d0b85905271d27dab2ae8a9edeab6dfff16632b17a0b6b57cd7ad2
  pageDirectory: concepts
  sources:
    - serve-declarative-features-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - unity-catalog-feature-lookup
    - UCFL
  citations:
    - file: serve-declarative-features-databricks-on-aws.md
title: Unity Catalog Feature Lookup
description: Model serving endpoints use Unity Catalog to look up table-backed features from online stores at inference time, using entity keys from the request payload.
tags:
  - unity-catalog
  - feature-store
  - model-serving
timestamp: "2026-06-19T23:02:50.886Z"
---

---
title: [Unity Catalog](/concepts/unity-catalog.md) [Feature Lookup](/concepts/feature-lookup.md)
summary: Models trained with features from Databricks [Unity Catalog](/concepts/unity-catalog.md) automatically track feature lineage; when deployed as [Model Serving](/concepts/model-serving.md) endpoints, they use [Unity Catalog](/concepts/unity-catalog.md) to look up features from online stores.
sources:
  - serve-declarative-features-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - unity-catalog
  - feature-store
  - model-serving
  - online-inference
aliases:
  - unity-catalog-feature-lookup
  - UCFL
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# [Unity Catalog](/concepts/unity-catalog.md) [Feature Lookup](/concepts/feature-lookup.md)

**Unity Catalog Feature Lookup** is the mechanism by which models trained using features from Databricks [Unity Catalog](/concepts/unity-catalog.md) automatically retrieve those features from online stores when deployed as [Model Serving](/concepts/model-serving.md) endpoints. When a model is trained with features registered in [Unity Catalog](/concepts/unity-catalog.md), Databricks records lineage linking the model to the features it used. At serving time, the [Model Serving Endpoint](/concepts/model-serving-endpoint.md) uses [Unity Catalog](/concepts/unity-catalog.md) to look up the required feature values from online stores. ^[serve-declarative-features-databricks-on-aws.md]

## Deploying a [Model Serving Endpoint](/concepts/model-serving-endpoint.md)

To enable [Feature Lookup](/concepts/feature-lookup.md), you deploy a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using a model that is registered in [Unity Catalog](/concepts/unity-catalog.md). The model must be logged through [MLflow](/concepts/mlflow.md) with the appropriate feature metadata. You can either use an existing endpoint or create a new one with the Databricks SDK. ^[serve-declarative-features-databricks-on-aws.md]

The following example creates a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) for a fraud detection model:

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

## Querying the Endpoint

When you query the endpoint, you provide entity keys (such as `user_id` and `transaction_time`) that the serving infrastructure uses to look up table‑backed features from the online store. The following example shows a basic query:

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

If the model was trained with **RequestSource** features (features provided directly in the request payload rather than looked up from the online store), the request must include all columns defined as `RequestSource` in the model signature. These columns are added to the [MLflow](/concepts/mlflow.md) model signature during `log_model`, so the endpoint's API schema reflects the required fields. Entity keys are still used for table‑backed [Feature Lookup](/concepts/feature-lookup.md); `RequestSource` columns are passed through directly to the model. ^[serve-declarative-features-databricks-on-aws.md]

Example request:

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

The same request can be made with `curl`:

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

## Limitations

Feature Serving endpoints (the older serving type for [Feature Store](/concepts/feature-store.md) functions) are not supported for [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md). To serve features online, you must deploy a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using a model logged through [Unity Catalog](/concepts/unity-catalog.md). ^[serve-declarative-features-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Central repository for registering and sharing features.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – Infrastructure to deploy and query ML models.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that manages [Feature Tables](/concepts/feature-tables.md) and model lineage.
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) – Approach that defines feature transformations declaratively.
- [Online Store](/concepts/online-feature-store.md) – Low‑latency storage used for [Feature Lookup](/concepts/feature-lookup.md) during serving.

## Sources

- serve-declarative-features-databricks-on-aws.md

# Citations

1. [serve-declarative-features-databricks-on-aws.md](/references/serve-declarative-features-databricks-on-aws-86fbe897.md)
