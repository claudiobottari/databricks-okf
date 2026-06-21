---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 01b82b0b44049d4ae5d2b8f07f3d83e682114f63c39bb8857227332e800d8e27
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-serving
    - DFS
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Databricks Feature Serving
description: A managed serving infrastructure that exposes Databricks feature data (from Unity Catalog) to external models and applications via high-availability, low-latency, auto-scaling endpoints.
tags:
  - feature-store
  - serving
  - databricks
timestamp: "2026-06-19T18:48:55.983Z"
---

# Databricks Feature Serving

**Databricks Feature Serving** is a managed service that makes structured data stored in the Databricks platform available to models and applications deployed outside of Databricks. It provides high-availability, low-latency API endpoints that serve pre-materialized features and compute on-demand features in real time. Feature Serving endpoints automatically scale to adjust to traffic volume and are ideal for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications, models served outside Databricks, or any application that requires features based on data in [Unity Catalog](/concepts/unity-catalog.md). ^[feature-serving-endpoints-databricks-on-aws.md]

## Benefits

Databricks Feature Serving provides a single interface that serves both pre-materialized and on-demand features, with the following benefits: ^[feature-serving-endpoints-databricks-on-aws.md]

- **Simplicity.** Databricks handles all infrastructure. With a single API call, you create a production-ready serving environment.
- **High availability and scalability.** Endpoints automatically scale up and down to adjust to the volume of serving requests.
- **Security.** Endpoints are deployed in a secure network boundary and use dedicated compute that terminates when the endpoint is deleted or scaled to zero.

## Requirements

- **Databricks Runtime:** 14.2 ML or above.
- **Python API:** `databricks-feature-engineering` version 0.1.2 or above (built into Databricks Runtime 14.2 ML). For earlier runtimes, manually install with `%pip install databricks-feature-engineering>=0.1.2` and restart the Python kernel with `dbutils.library.restartPython()`.
- **Databricks SDK:** Version 0.18.0 or above. Install with `%pip install databricks-sdk>=0.18.0` and restart the Python kernel as above.
- **API access:** To use the REST API or MLflow Deployments SDK, you must have a Databricks API token. Databricks recommends using OAuth tokens for automated workflows and personal access tokens belonging to Service Principals instead of workspace users.

^[feature-serving-endpoints-databricks-on-aws.md]

## Core Concepts

### FeatureSpec

A `FeatureSpec` is the central abstraction that defines the set of features and functions exposed by a Feature Serving endpoint. It combines feature lookups from online feature tables with feature functions that compute derived values at serving time. `FeatureSpecs` are stored in and managed by Unity Catalog and appear in [Catalog Explorer](/concepts/catalog-explorer.md). ^[feature-serving-endpoints-databricks-on-aws.md]

The tables referenced in a `FeatureSpec` must be published to an [Online Feature Store](/concepts/online-feature-store.md) or a third-party online store before they can be served. ^[feature-serving-endpoints-databricks-on-aws.md]

### Feature Serving Endpoints

An endpoint is created from a `FeatureSpec` and exposes a RESTful API that accepts request data, performs the defined feature lookups and computations, and returns the augmented feature vector. ^[feature-serving-endpoints-databricks-on-aws.md]

## Creating a FeatureSpec

A `FeatureSpec` is created using the `databricks-feature-engineering` package. Features can be: ^[feature-serving-endpoints-databricks-on-aws.md]

- **FeatureLookup** — Looks up columns from a Unity Catalog table by a key provided at query time (for example, looking up `average_yearly_spend` by `user_id`).
- **FeatureFunction** — Computes a new feature by applying a Python function (registered in Unity Catalog) to other features or request parameters (for example, calculating `spending_gap` as `ytd_spend - average_yearly_spend`).

Default values can be specified for feature lookups using the `default_values` parameter. If feature columns are renamed with `rename_outputs`, default values must use the renamed feature names. ^[feature-serving-endpoints-databricks-on-aws.md]

The following example demonstrates creating a Python function in Unity Catalog and using it in a `FeatureSpec`: ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from unitycatalog.ai.core.databricks import DatabricksFunctionClient

client = DatabricksFunctionClient()

def difference(num_1: float, num_2: float) -> float:
    """Subtracts num_2 from num_1 and returns the result."""
    return num_1 - num_2

client.create_python_function(
    func=difference,
    catalog="main",
    schema="default",
    replace=True,
)
```

Then define the `FeatureSpec` using FeatureLookup and FeatureFunction: ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.feature_engineering import (
    FeatureFunction, FeatureLookup, FeatureEngineeringClient,
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

## Creating an Endpoint

Create an endpoint using the Databricks SDK, Python API, or REST API. The endpoint is configured with the `FeatureSpec` name and workload settings. ^[feature-serving-endpoints-databricks-on-aws.md]

### Using the Databricks SDK (Python)

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

After creation, the endpoint appears on the **Serving** page in the Databricks UI. When the state transitions to **Ready**, the endpoint can respond to queries. ^[feature-serving-endpoints-databricks-on-aws.md]

### Inference Table Integration

For endpoints created starting February 2025, you can configure the endpoint to log the augmented DataFrame (containing looked-up feature values and function return values) to an [Inference Table](/concepts/inference-tables.md). This provides a record of feature computations for monitoring and debugging. ^[feature-serving-endpoints-databricks-on-aws.md]

## Querying an Endpoint

Endpoints can be queried using the REST API, the [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md), or the Serving UI. ^[feature-serving-endpoints-databricks-on-aws.md]

### Using the MLflow Deployments SDK

Set environment variables for authentication, then create a client and send a prediction request: ^[feature-serving-endpoints-databricks-on-aws.md]

```bash
export DATABRICKS_HOST=...
export DATABRICKS_TOKEN=...
```

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

### Querying from the UI

1. In the left sidebar, click **Serving**.
2. Click the endpoint name.
3. Click **Query endpoint**.
4. Enter the request body in JSON format and click **Send request**.

The dialog includes generated code examples in curl, Python, and SQL. ^[feature-serving-endpoints-databricks-on-aws.md]

### Getting the Endpoint Schema

Use the Databricks SDK or REST API to retrieve the OpenAPI schema of an endpoint, which describes the request and response format: ^[feature-serving-endpoints-databricks-on-aws.md]

```python
endpoint = workspace.serving_endpoints.get_open_api(name="customer-features")
```

## Updating an Endpoint

To modify an endpoint's configuration (such as changing the `FeatureSpec` or workload size), always use the update APIs rather than deleting and recreating the endpoint. Deleting a live endpoint causes immediate downtime for all applications querying it. ^[feature-serving-endpoints-databricks-on-aws.md]

### Using the Databricks SDK

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

### Using the UI

1. On the **Serving** page, click the endpoint name.
2. Click **Edit endpoint**.
3. Modify the settings as needed.
4. Click **Update**. ^[feature-serving-endpoints-databricks-on-aws.md]

## Deleting an Endpoint

Deleting an endpoint is irreversible and causes immediate downtime. To change the configuration, update the existing endpoint instead. ^[feature-serving-endpoints-databricks-on-aws.md]

### Using the Databricks SDK

```python
workspace.serving_endpoints.delete(name="customer-features")
```

### Using the UI

1. On the **Serving** page, click the endpoint name.
2. Click the kebab menu and select **Delete**. ^[feature-serving-endpoints-databricks-on-aws.md]

## Monitoring

For information about logs and metrics available for Feature Serving endpoints, see Monitor Model Quality and Endpoint Health. ^[feature-serving-endpoints-databricks-on-aws.md]

## Access Control

For permissions management on Feature Serving endpoints, see [Manage Permissions on a Model Serving Endpoint](/concepts/update-model-serving-endpoints.md). ^[feature-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Serves ML models with automatic feature lookup
- [Online Feature Store](/concepts/online-feature-store.md) — Stores pre-materialized features for low-latency serving
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating and managing features
- [Unity Catalog](/concepts/unity-catalog.md) — Governs feature tables and `FeatureSpec` objects
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) — Programmatic interface for querying endpoints
- [Inference Tables](/concepts/inference-tables.md) — Logs serving requests and responses for monitoring
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for browsing Unity Catalog objects including `FeatureSpecs`

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
