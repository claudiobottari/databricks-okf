---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4bbd4f5ab865f0bdbb180f7d2731fc23cca55c474d3f0c1a49fdca46e5b5b282
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-serving-endpoint-lifecycle-management
    - FSELM
    - Serving endpoint management
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Feature Serving endpoint lifecycle management
description: APIs and UI workflows for creating, retrieving, updating (never delete-and-recreate), and deleting Feature Serving endpoints, with warnings against downtime caused by deletion.
tags:
  - serving
  - api
  - lifecycle
timestamp: "2026-06-18T12:19:09.894Z"
---

# Feature Serving endpoint lifecycle management

**Feature Serving endpoint lifecycle management** refers to the set of operations for creating, updating, querying, monitoring, and deleting Feature Serving endpoints in Databricks. These endpoints serve structured data from [Unity Catalog](/concepts/unity-catalog.md) to models or applications deployed outside of Databricks, automatically scaling to real-time traffic with high availability and low latency. ^[feature-serving-endpoints-databricks-on-aws.md]

## Overview

A Feature Serving endpoint is defined by a [FeatureSpec](/concepts/featurespec.md) — a user-defined set of features and functions stored in Unity Catalog. The endpoint lifecycle follows a standard progression: create the endpoint from a `FeatureSpec`, query it for inference, optionally update its configuration, monitor its health, and delete it when no longer needed. ^[feature-serving-endpoints-databricks-on-aws.md]

Databricks provides several interfaces for managing the endpoint lifecycle: the Databricks UI, REST API, Python API, and Databricks SDK. ^[feature-serving-endpoints-databricks-on-aws.md]

## Prerequisites

Before creating a Feature Serving endpoint, you must meet the following requirements: ^[feature-serving-endpoints-databricks-on-aws.md]

- Databricks Runtime 14.2 ML or above
- `databricks-feature-engineering` version 0.1.2 or above (built into Databricks Runtime 14.2 ML; for earlier versions, install manually with `%pip install databricks-feature-engineering>=0.1.2`)
- `databricks-sdk` version 0.18.0 or above (for SDK usage)
- A Databricks API token (for REST API or MLflow Deployments SDK)

## Creating a FeatureSpec

A `FeatureSpec` is the foundation of a Feature Serving endpoint. It combines feature lookups from online feature store tables and feature functions. The `FeatureSpec` is stored in and managed by Unity Catalog and appears in Catalog Explorer. ^[feature-serving-endpoints-databricks-on-aws.md]

The tables specified in a `FeatureSpec` must be published to an online feature store or a third-party online store. ^[feature-serving-endpoints-databricks-on-aws.md]

### Defining a function

```python
from unitycatalog.ai.core.databricks import DatabricksFunctionClient

client = DatabricksFunctionClient()

CATALOG = "main"
SCHEMA = "default"

def difference(num_1: float, num_2: float) -> float:
    """A function that accepts two floating point numbers, subtracts the second one
    from the first, and returns the result as a float."""
    return num_1 - num_2

client.create_python_function(
    func=difference,
    catalog=CATALOG,
    schema=SCHEMA,
    replace=True
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

### Creating the FeatureSpec

```python
from databricks.feature_engineering import (
    FeatureFunction,
    FeatureLookup,
    FeatureEngineeringClient,
)

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name="main.default.customer_profile",
        lookup_key="user_id",
        feature_names=["average_yearly_spend", "country"]
    ),
    FeatureFunction(
        udf_name="main.default.difference",
        output_name="spending_gap",
        input_bindings={"num_1": "ytd_spend", "num_2": "average_yearly_spend"},
    ),
]

fe.create_feature_spec(
    name="main.default.customer_features",
    features=features,
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

### Specifying default values

You can specify default values for features using the `default_values` parameter in `FeatureLookup`. If feature columns are renamed using `rename_outputs`, `default_values` must use the renamed feature names. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
feature_lookups = [
    FeatureLookup(
        table_name="ml.recommender_system.customer_features",
        feature_names=["membership_tier", "age", "page_views_count_30days"],
        lookup_key="customer_id",
        default_values={
            "age": 18,
            "membership_tier": "bronze"
        },
    ),
]
```

## Creating an endpoint

Once the `FeatureSpec` is created, you can create a serving endpoint from it. ^[feature-serving-endpoints-databricks-on-aws.md]

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

^[feature-serving-endpoints-databricks-on-aws.md]

When the endpoint state is **Ready**, it is ready to respond to queries. You can view the endpoint by clicking **Serving** in the left sidebar of the Databricks UI. ^[feature-serving-endpoints-databricks-on-aws.md]

### Logging augmented DataFrames to inference tables

For endpoints created starting February 2025, you can configure the endpoint to log the augmented DataFrame containing looked-up feature values and function return values to the inference table. ^[feature-serving-endpoints-databricks-on-aws.md]

## Getting an endpoint

You can retrieve metadata and status of an existing endpoint using the Databricks SDK or Python API. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

workspace = WorkspaceClient()
endpoint = workspace.serving_endpoints.get(name="customer-features")
```

## Getting the endpoint schema

You can retrieve the OpenAPI schema of an endpoint using the Databricks SDK or REST API. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

workspace = WorkspaceClient()
endpoint = workspace.serving_endpoints.get_open_api(name="customer-features")
```

## Querying an endpoint

You can query a Feature Serving endpoint using the REST API, the MLflow Deployments SDK, or the Serving UI. ^[feature-serving-endpoints-databricks-on-aws.md]

### Using the MLflow Deployments SDK

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")

response = client.predict(
    endpoint="test-feature-endpoint",
    inputs={
        "dataframe_records": [
            {"user_id": 1, "ytd_spend": 598},
            {"user_id": 2, "ytd_spend": 280},
        ]
    },
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

### Using the UI

1. In the left sidebar, click **Serving**.
2. Click the endpoint you want to query.
3. Click **Query endpoint**.
4. Enter the request body in JSON format.
5. Click **Send request**.

The dialog includes generated example code in curl, Python, and SQL. ^[feature-serving-endpoints-databricks-on-aws.md]

## Updating an endpoint

To modify a Feature Serving endpoint's configuration — such as changing the `FeatureSpec` or workload size — always use the update APIs. Do not delete and recreate the endpoint to apply changes, as deleting a live endpoint causes immediate downtime. ^[feature-serving-endpoints-databricks-on-aws.md]

### Using the SDK

```python
from databricks.sdk import WorkspaceClient

workspace = WorkspaceClient()
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

^[feature-serving-endpoints-databricks-on-aws.md]

### Using the UI

1. Click **Serving** in the left sidebar.
2. Click the endpoint name.
3. Click **Edit endpoint**.
4. Edit the settings as needed.
5. Click **Update**. ^[feature-serving-endpoints-databricks-on-aws.md]

## Deleting an endpoint

Deleting a Feature Serving endpoint is irreversible and causes immediate downtime for any applications querying it. If you need to change the endpoint's configuration, use the update operation instead. ^[feature-serving-endpoints-databricks-on-aws.md]

### Using the SDK

```python
from databricks.sdk import WorkspaceClient

workspace = WorkspaceClient()
workspace.serving_endpoints.delete(name="customer-features")
```

^[feature-serving-endpoints-databricks-on-aws.md]

### Using the UI

1. Click **Serving** in the left sidebar.
2. Click the endpoint name.
3. Click the kebab menu and select **Delete**. ^[feature-serving-endpoints-databricks-on-aws.md]

## Monitoring endpoint health

For information about logs and metrics available for Feature Serving endpoints, see Monitor model quality and endpoint health. ^[feature-serving-endpoints-databricks-on-aws.md]

## Access control

For information about permissions on Feature Serving endpoints, see Manage permissions on a model serving endpoint. ^[feature-serving-endpoints-databricks-on-aws.md]

## Best practices

- **Use update instead of delete-recreate** to avoid downtime when changing endpoint configuration. ^[feature-serving-endpoints-databricks-on-aws.md]
- **Use OAuth tokens** for authentication with automated tools, systems, scripts, and apps. Databricks recommends using personal access tokens belonging to service principals instead of workspace users. ^[feature-serving-endpoints-databricks-on-aws.md]
- **For latency-sensitive workloads**, consider route optimization on custom model serving endpoints. ^[feature-serving-endpoints-databricks-on-aws.md]

## Related concepts

- [FeatureSpec](/concepts/featurespec.md) — The user-defined set of features and functions that defines an endpoint
- [Online Feature Store](/concepts/online-feature-store.md) — The store that provides pre-materialized features for serving
- [Model Serving](/concepts/model-serving.md) — The broader serving infrastructure for ML models
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores and manages FeatureSpecs
- [Inference Tables](/concepts/inference-tables.md) — Logging destination for augmented DataFrames

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
