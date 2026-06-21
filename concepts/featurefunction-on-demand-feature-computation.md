---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f054fd038975544776b086768f5f273435fb4266b2281ea11ebc413a28a96db
  pageDirectory: concepts
  sources:
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featurefunction-on-demand-feature-computation
    - F(FC
  citations:
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
title: FeatureFunction (On-Demand Feature Computation)
description: A Unity Catalog function used in FeatureSpecs to compute feature values at inference time using runtime-provided context data
tags:
  - databricks
  - feature-engineering
  - on-demand-features
timestamp: "2026-06-18T12:13:58.709Z"
---

---
title: FeatureFunction (On-Demand Feature Computation)
summary: A FeatureFunction in Databricks Feature Engineering allows you to define on-demand feature transformations that are computed at inference time by referencing a Unity Catalog function.
sources:
  - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - feature-engineering
  - feature-serving
  - on-demand
aliases:
  - featurefunction-on-demand-feature-computation
  - on-demand-feature-computation
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# FeatureFunction (On-Demand Feature Computation)

A **FeatureFunction** is a component of a [FeatureSpec](/concepts/featurespec.md) in Databricks Feature Engineering that defines a feature value computed on demand at inference time, rather than being precomputed and stored in a feature table. It references a user-defined function (UDF) registered in [Unity Catalog](/concepts/unity-catalog.md) and binds its parameters to values from the request context or from other features retrieved by [FeatureLookup](/concepts/featurelookup.md) objects. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Purpose

Precomputed features are efficient when the input data does not change frequently. However, some features depend on runtime context — such as a user’s current location, session attributes, or real-time sensor readings — that cannot be known until the moment of inference. A FeatureFunction lets you compute such values on the fly using a serverless UDF, combining them with precomputed features in a single serving endpoint. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Anatomy of a FeatureFunction

You create a FeatureFunction by providing:

- `udf_name` — the fully qualified name of a function registered in Unity Catalog.
- `output_name` — the name of the output feature that the function produces.
- `input_bindings` — a dictionary mapping each parameter of the UDF to a source of its value. Sources can be:
  - a column from a feature table (obtained via a FeatureLookup),
  - a context parameter passed at query time (e.g., `user_latitude`, `user_longitude`).

The following Python snippet (from the tutorial) creates a FeatureFunction that calculates the distance between a destination (whose coordinates are taken from a feature table) and a user (whose coordinates are supplied at query time): ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
FeatureFunction(
    udf_name=function_name,               # e.g. "main.on_demand_demo.distance"
    output_name="distance",
    input_bindings={
        "latitude": "latitude",
        "longitude": "longitude",
        "user_latitude": "user_latitude",
        "user_longitude": "user_longitude"
    },
)
```

## Workflow

1. **Create the UDF** in Unity Catalog. The function can be written in Python or SQL. In the tutorial, a Python UDF implements the Haversine formula to compute geographic distance. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

2. **Define the FeatureSpec** that includes one or more FeatureLookup objects (to retrieve precomputed features by primary key) and one or more FeatureFunction objects (to compute on-demand features). ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

3. **Deploy the FeatureSpec** to a feature serving endpoint. The endpoint automatically handles the orchestration: it first fetches the precomputed features, then executes the specified UDF with the supplied bindings, and returns all features together. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

4. **Query the endpoint** by providing the primary key(s) of the precomputed features and any context parameters needed by the FeatureFunction. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Example

The tutorial illustrates a city recommendation use case. The feature table `location_features` contains precomputed latitude and longitude for each city (keyed by `destination_id`). A Python UDF `distance` computes the Haversine distance between the city’s fixed location and a user’s current coordinates. At query time, the client sends: ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```json
{
  "dataframe_records": [
    {"destination_id": 1, "user_latitude": 37, "user_longitude": -122},
    {"destination_id": 2, "user_latitude": 37, "user_longitude": -122}
  ]
}
```

The endpoint returns the `distance` for each city, computed on demand. This pattern avoids storing a user’s changing location in the feature store and recalculates the distance fresh for every request. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Benefits

- **Real-time context** — Features that depend on session, user, or environment parameters are computed exactly when needed.
- **No stale data** — Unlike precomputed features that may become outdated, on-demand functions always use the latest inputs.
- **Simplified pipeline** — Eliminates the need for batch jobs to update dynamic features or to maintain separate online tables for each contextual combination.
- **Low latency** — The feature serving endpoint executes the UDF in a serverless runtime, typically returning results in milliseconds.

## Requirements

- The UDF must be registered in Unity Catalog and accessible to the feature serving endpoint (the endpoint’s service principal must have `EXECUTE` permission on the function).
- FeatureFunctions can only be used within a FeatureSpec that is deployed to a feature serving endpoint. They are not available in offline (batch) scoring contexts.
- All input bindings must resolve to either a column name in a feature table or a context parameter name passed in the query request. Parameters not sourced from a feature table are expected in the request payload.

## Related Concepts

- [FeatureSpec](/concepts/featurespec.md) — The composition of [FeatureLookup](/concepts/featurelookup.md) and FeatureFunction objects that defines the features served by an endpoint.
- [FeatureLookup](/concepts/featurelookup.md) — A precomputed feature retrieved from an online feature store by primary key.
- [Online Feature Store](/concepts/online-feature-store.md) — The low-latency storage that serves precomputed features.
- Feature Serving — The mechanism for deploying and querying feature specs as REST endpoints.
- Unity Catalog Functions — The UDFs that power FeatureFunctions.

## Sources

- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md

# Citations

1. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
