---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e500912713652de3673a889387d34e1100cd388a426f3642275d51bbdd5b2ba
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-serving-endpoint-lifecycle
    - FSEL
    - Serving Endpoint Lifecycle
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
    - file: |-
        feature-serving-endpoints-databricks-on-aws.md

        ## Lifecycle Stages

        ### 1. Create a FeatureSpec

        A `FeatureSpec` is a user‑defined set of [[FeatureLookup
title: Feature Serving Endpoint Lifecycle
description: The create/read/update/delete lifecycle for Feature Serving endpoints, emphasizing update-over-recreate to avoid downtime, and supporting UI, REST API, Python API, and Databricks SDK.
tags:
  - serving
  - operations
  - lifecycle
timestamp: "2026-06-19T18:48:23.666Z"
---

# Feature Serving Endpoint Lifecycle

**Feature Serving Endpoint Lifecycle** describes the complete set of stages for managing a Databricks [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md): creating, retrieving, querying, updating, monitoring, and deleting the endpoint. Endpoints serve pre‑materialized and on‑demand features from Unity Catalog to models or applications deployed outside of Databricks, automatically scaling to handle real‑time traffic with high availability and low latency. ^[feature-serving-endpoints-databricks-on-aws.md]

## Overview

Databricks Feature Serving provides a single interface for serving structured data, supporting use cases such as retrieval‑augmented generation (RAG) and feature lookups for externally hosted models. Benefits include simplicity (infrastructure is managed by Databricks), automatic scaling, and security (endpoints use dedicated compute within a secure network boundary). ^[feature-serving-endpoints-databricks-on-aws.md]

The lifecycle can be managed through the Databricks UI, REST API, Python API, or Databricks SDK. ^[feature-serving-endpoints-databricks-on-aws.md]

## Prerequisites

- Databricks Runtime 14.2 ML or above.
- `databricks-feature-engineering` version 0.1.2 or above (built into 14.2 ML; manually install and restart the Python kernel for earlier runtimes).
- To use the Databricks SDK, `databricks-sdk` version 0.18.0 or above.
- A Databricks API token for REST API or MLflow Deployments SDK usage.
- The feature tables referenced in the [FeatureSpec](/concepts/featurespec.md) must be published to an online feature store or third-party online store. ^[feature-serving-endpoints-databricks-on-aws.md

## Lifecycle Stages

### 1. Create a FeatureSpec

A `FeatureSpec` is a user‑defined set of [FeatureLookup](/concepts/featurelookup.md) and [FeatureFunction](/concepts/featurefunction.md) entries. It is stored in and managed by Unity Catalog. Before creating the endpoint, you define the `FeatureSpec` using the `FeatureEngineeringClient`. ^[feature-serving-endpoints-databricks-on-aws.md]

Default values can be specified for features via the `default_values` parameter in `FeatureLookup`. If features are renamed with `rename_outputs`, the default values must use the renamed names. ^[feature-serving-endpoints-databricks-on-aws.md]

### 2. Create an Endpoint

Create the endpoint by providing its name and a configuration that references the `FeatureSpec`. The endpoint automatically becomes ready to serve queries once the state is **Ready**. To save the augmented DataFrame (feature lookup results) to the inference table, configure the endpoint accordingly (supported for endpoints created from February 2025 onward). ^[feature-serving-endpoints-databricks-on-aws.md]

**SDK (Python example):**
```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

workspace = WorkspaceClient()
workspace.serving_endpoints.create(
    name="my-serving-endpoint",
    config=EndpointCoreConfigInput(
        served_entities=[
            ServedEntityInput(
                entity_name="main.default.customer_features",
                scale_to_zero_enabled=True,
                workload_size="Small"
            )
        ]
    )
)
```

Options include Databricks UI, REST API, Python API, and Databricks SDK. ^[feature-serving-endpoints-databricks-on-aws.md]

### 3. Get an Endpoint (Read)

Retrieve an endpoint's metadata and status using the SDK or Python API. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
endpoint = workspace.serving_endpoints.get(name="customer-features")
```

You can also obtain the endpoint's OpenAPI schema (including input/output signatures) using the SDK or REST API. ^[feature-serving-endpoints-databricks-on-aws.md]

### 4. Query an Endpoint

Query the endpoint using the REST API, [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md), or the Serving UI. The request body uses a `dataframe_records` format. ^[feature-serving-endpoints-databricks-on-aws.md]

**MLflow Deployments SDK example:**
```python
import mlflow.deployments
client = mlflow.deployments.get_deploy_client("databricks")
response = client.predict(
    endpoint="test-feature-endpoint",
    inputs={
        "dataframe_records": [
            {"user_id": 1, "ytd_spend": 598},
            {"user_id": 2, "ytd_spend": 280}
        ]
    }
)
```

The Serving UI provides a **Query endpoint** dialog with generated code examples (curl, Python, SQL). ^[feature-serving-endpoints-databricks-on-aws.md]

### 5. Update an Endpoint

To modify the endpoint's configuration—such as changing the `FeatureSpec`, workload size, or scaling options—always use the **update** API or UI. Do **not** delete and recreate the endpoint, as that causes immediate downtime. ^[feature-serving-endpoints-databricks-on-aws.md]

**SDK update example:**
```python
workspace.serving_endpoints.update_config(
    name="my-serving-endpoint",
    served_entities=[
        ServedEntityInput(
            entity_name="main.default.customer_features",
            scale_to_zero_enabled=True,
            workload_size="Small"
        )
    ]
)
```

In the UI, click **Edit endpoint** from the endpoint's page. ^[feature-serving-endpoints-databricks-on-aws.md]

### 6. Delete an Endpoint

Deletion is irreversible and causes immediate downtime for applications querying the endpoint. Use the REST API, Databricks SDK, Python API, or Serving UI. Always prefer updating over deleting if the intent is to change configuration. ^[feature-serving-endpoints-databricks-on-aws.md]

**SDK deletion example:**
```python
workspace.serving_endpoints.delete(name="customer-features")
```

In the UI, select **Delete** from the endpoint's kebab menu. ^[feature-serving-endpoints-databricks-on-aws.md]

### 7. Monitor Endpoint Health

Feature Serving endpoints expose logs and metrics for monitoring model quality and endpoint health. See the documentation on Monitor model quality and endpoint health for details. ^[feature-serving-endpoints-databricks-on-aws.md]

### 8. Access Control

Permissions on Feature Serving endpoints are managed similarly to model serving endpoints. See Manage permissions on a model serving endpoint. ^[feature-serving-endpoints-databricks-on-aws.md]

## Summary Table

| Stage | Action | Notes |
|-------|--------|-------|
| Create FeatureSpec | Define `FeatureLookup` and `FeatureFunction` entries | Stored in Unity Catalog |
| Create Endpoint | Provide name and config referencing the FeatureSpec | Use scale-to-zero and workload size configuration |
| Get Endpoint | Retrieve metadata and status | SDK `get()` and `get_open_api()` |
| Query Endpoint | Send inference requests | Supports `dataframe_records` format |
| Update Endpoint | Modify configuration | Do not delete; use update APIs |
| Delete Endpoint | Irreversible removal | Causes immediate downtime |
| Monitor | Health logs and metrics | Integrates with endpoint monitoring tools |

## Related Concepts

- [FeatureSpec](/concepts/featurespec.md)
- [FeatureLookup](/concepts/featurelookup.md)
- [FeatureFunction](/concepts/featurefunction.md)
- [Online Feature Store](/concepts/online-feature-store.md)
- [Model Serving](/concepts/model-serving.md)
- [Inference Tables](/concepts/inference-tables.md)
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
2. feature-serving-endpoints-databricks-on-aws.md

## Lifecycle Stages

### 1. Create a FeatureSpec

A `FeatureSpec` is a user‑defined set of [[FeatureLookup
