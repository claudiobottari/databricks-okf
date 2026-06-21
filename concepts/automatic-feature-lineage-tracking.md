---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7a9bea86e210aff089ca35e85aa2e83ab28bbf9e22c488019ac34ffb3d0715d
  pageDirectory: concepts
  sources:
    - serve-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-feature-lineage-tracking
    - AFLT
  citations:
    - file: serve-declarative-features-databricks-on-aws.md
title: Automatic Feature Lineage Tracking
description: Models trained using Databricks features automatically track lineage to the features they were trained on, enabling runtime feature lookup from online stores.
tags:
  - machine-learning
  - feature-store
  - lineage
timestamp: "2026-06-19T23:02:44.736Z"
---

# [Automatic Feature Lineage](/concepts/automatic-feature-lineage.md) Tracking

**Automatic Feature Lineage Tracking** is a capability in Databricks that automatically records the relationships between machine learning models and the features they were trained on. When a model is trained using features from [Databricks Feature Store](/concepts/databricks-feature-store.md), the system automatically tracks which features were used, enabling downstream serving endpoints to look up those features from online stores at inference time. ^[serve-declarative-features-databricks-on-aws.md]

## Overview

Models trained with features from Databricks automatically capture lineage information connecting them to the specific features used during training. This lineage is stored in [Unity Catalog](/concepts/unity-catalog.md) alongside the model. When the model is deployed as a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), the serving infrastructure uses [Unity Catalog](/concepts/unity-catalog.md) to resolve and retrieve the required features from [Online Stores](/concepts/online-feature-store.md) during inference requests. ^[serve-declarative-features-databricks-on-aws.md]

This automatic tracking eliminates the need for manual feature specification at deployment time, reducing operational complexity and the risk of mismatches between training and serving feature sets.

## How It Works

1. **Training phase**: During model training, features are looked up from [Databricks Feature Store](/concepts/databricks-feature-store.md). The system records which features (including their source tables and versions) were used.
2. **Model registration**: When the model is logged to [Unity Catalog](/concepts/unity-catalog.md) (via `mlflow.log_model` or similar), the feature lineage is captured as part of the model metadata. The [MLflow](/concepts/mlflow.md) model signature includes all feature columns.
3. **Deployment phase**: When a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) is created or updated, the system reads the lineage information from [Unity Catalog](/concepts/unity-catalog.md) to identify which features need to be served.
4. **Inference phase**: During inference, the serving endpoint uses entity keys from the request payload to look up table-backed features from the online store. Features marked as `RequestSource` are passed directly through to the model.

## Querying Endpoints with Automatic Feature Resolution

When querying a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that uses automatically tracked features, the request payload must include entity keys for feature lookups. For models trained with `RequestSource` features, the payload must also include all `RequestSource` columns as defined in the model signature. ^[serve-declarative-features-databricks-on-aws.md]

The following example shows a query to a fraud detection endpoint with automatic feature resolution:

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

Entity keys are used for looking up table-backed features from the online store, while `RequestSource` columns are passed directly to the model. ^[serve-declarative-features-databricks-on-aws.md]

## Benefits

- **Reduced operational overhead**: No need to manually configure feature lookups when deploying models.
- **Consistency**: The same feature definitions used during training are automatically applied during serving.
- **Governance**: Feature lineage is captured in [Unity Catalog](/concepts/unity-catalog.md), providing auditability and traceability.
- **Simplified deployment**: [Model Serving](/concepts/model-serving.md) endpoints can be created with minimal configuration.

## Limitations

Feature Serving endpoints are not supported for [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md). To serve features online, models must be deployed through [Model Serving](/concepts/model-serving.md) endpoints using a model logged through [Unity Catalog](/concepts/unity-catalog.md). ^[serve-declarative-features-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Central repository for managing and serving features
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — Infrastructure for deploying models to production
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and metadata catalog used for feature resolution
- [Online Stores](/concepts/online-feature-store.md) — Low-latency storage for feature serving
- [RequestSource Features](/concepts/requestsource-features.md) — Features provided directly in the inference request payload
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — Alternative approach to feature engineering (not supported with Feature Serving endpoints)

## Sources

- serve-declarative-features-databricks-on-aws.md

# Citations

1. [serve-declarative-features-databricks-on-aws.md](/references/serve-declarative-features-databricks-on-aws-86fbe897.md)
