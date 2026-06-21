---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ca4b6a908b9a66f87e4dde65a1ec0824f71abc9dd5971858876165ea35b6669
  pageDirectory: concepts
  sources:
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-function-udf
    - FF(
    - Feature functions
    - feature functions
  citations:
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
title: Feature Function (UDF)
description: A user-defined function in Unity Catalog that computes on-demand features at inference time using input bindings from retrieved and context features
tags:
  - feature-store
  - udf
  - on-demand
timestamp: "2026-06-19T18:44:15.781Z"
---

# Feature Function (UDF)

A **Feature Function (UDF)** is a user-defined function (UDF) registered in [Unity Catalog](/concepts/unity-catalog.md) that computes features on-demand during model inference. It is used in Feature Serving endpoints to produce dynamic feature values that depend on request-time context — for example, calculating the distance between a fixed location and a user’s current coordinates. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Overview

In feature serving, most features are precomputed and stored in a Delta table. However, some features must be computed at the time of the request because their inputs (such as the user’s current location) are not known until the request arrives. A Feature Function wraps a SQL UDF or Python UDF stored in Unity Catalog. It is declared inside a [FeatureSpec](/concepts/featurespec.md) using the `FeatureFunction` class from the `databricks.feature_engineering` module. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Anatomy of a Feature Function

A Feature Function is defined by:

- **`udf_name`** – The fully qualified name of the UDF in Unity Catalog (e.g., `catalog.schema.function_name`).
- **`output_name`** – The name under which the computed result will be available in the feature vector.
- **`input_bindings`** – A dictionary mapping the UDF’s parameter names to the sources of their values. Sources can be:
  - Column names from the feature lookup (e.g., `"latitude": "latitude"` passes the `latitude` column retrieved from the feature table).
  - Context fields provided at query time (e.g., `"user_latitude": "user_latitude"` passes the user’s latitude passed in the request).

^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

### Example

The following example defines a Python UDF that computes the Haversine distance between two locations, then uses `FeatureFunction` to bind it in a feature spec:

```python
from databricks.feature_engineering import FeatureFunction

feature_fn = FeatureFunction(
    udf_name="main.on_demand_demo.distance",
    output_name="distance",
    input_bindings={
        "latitude": "latitude",
        "longitude": "longitude",
        "user_latitude": "user_latitude",
        "user_longitude": "user_longitude"
    }
)
```

The UDF (`distance`) takes four parameters: the destination’s latitude and longitude (retrieved from the feature table) and the user’s latitude and longitude (provided at request time). The resulting `distance` value is returned as part of the serving response. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Using a Feature Function in a FeatureSpec

A `FeatureFunction` is combined with one or more [FeatureLookup](/concepts/featurelookup.md) objects in a [FeatureSpec](/concepts/featurespec.md). The spec is then deployed to a Feature Serving endpoint. When the endpoint is queried, the feature serving logic first looks up the precomputed features, then calls the UDF with the bound inputs to compute the on-demand feature. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
features = [
    FeatureLookup(table_name=feature_table_name, lookup_key="destination_id"),
    FeatureFunction(
        udf_name=function_name,
        output_name="distance",
        input_bindings={...}
    )
]
feature_spec = fe.create_feature_spec(name=spec_name, features=features)
```

## Querying an Endpoint That Uses a Feature Function

When querying the endpoint, the request must include both the primary key values (used for lookups) and any context values required by the UDF. For example:

```python
client.predict(
    endpoint=endpoint_name,
    inputs={
        "dataframe_records": [
            {"destination_id": 1, "user_latitude": 37, "user_longitude": -122},
        ]
    }
)
```

The endpoint automatically retrieves the destination’s latitude/longitude from the online feature store, passes them along with the user’s location to the UDF, and returns the computed distance. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Benefits

- **Low latency**: On-demand computation happens inside the serving runtime, avoiding expensive lookups of dynamic values.
- **Separation of concerns**: Feature logic lives in Unity Catalog UDFs, independent of the serving infrastructure.
- **Reusable**: The same UDF can be referenced by multiple FeatureSpecs or applications.

## Related Concepts

- [FeatureSpec](/concepts/featurespec.md) – The container that groups FeatureLookups and FeatureFunctions.
- Feature Serving – The serving infrastructure that exposes feature specs as REST endpoints.
- [FeatureLookup](/concepts/featurelookup.md) – Retrieves precomputed features from an online table.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that stores the UDF definition.
- [On-Demand Features](/concepts/on-demand-features-databricks.md) – Features computed at inference time rather than precomputed.
- [Online Feature Store](/concepts/online-feature-store.md) – The system providing low-latency access to precomputed feature values.

## Sources

- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md

# Citations

1. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
