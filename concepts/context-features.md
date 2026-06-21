---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 39954ad3788a452e2e9a6a9f2fbd22d7b06e39be5ef80580ae18f72f9a4d0fbe
  pageDirectory: concepts
  sources:
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - context-features
    - Text Features
  citations:
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
title: Context Features
description: Features provided at inference time (not stored in feature tables) that serve as runtime inputs to feature functions for dynamic computation
tags:
  - feature-store
  - inference
  - runtime
timestamp: "2026-06-19T18:44:03.943Z"
---

The existing wiki page already contains a solid skeleton; we will expand it with concrete details from the source example while keeping the structure clean and adding proper citations.

```markdown
---
title: Context Features
summary: Input data provided at inference time that is not stored in feature tables, such as user location, used by feature functions for on-demand computation.
sources:
  - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:14:14.831Z"
updatedAt: "2026-06-19T10:25:08.591Z"
tags:
  - inference
  - real-time
  - feature-engineering
aliases:
  - context-features
confidence: 0.85
provenanceState: extracted
inferredParagraphs: 1
---

# Context Features

**Context Features** are feature values that are not known until inference time and must be provided dynamically when querying a [[Feature Serving Endpoint]]. Unlike precomputed features stored in a [[Feature Table]], context features are supplied by the caller as part of the prediction request, enabling real-time computations that depend on changing user or environment conditions. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Overview

In feature engineering pipelines, most feature values are precomputed and stored in feature tables. However, some features depend on data that is only available at the moment of inference — for example, a user's current GPS coordinates, session ID, or timestamp. Context features solve this problem by allowing the caller to pass these dynamic values alongside the primary key when querying a serving endpoint. The endpoint then uses these values in any on-demand functions defined in the [[FeatureSpec|Feature Spec]] to compute derived features in real time. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## How Context Features Work

Context features are integrated into a feature serving endpoint through the [[FeatureSpec|Feature Spec]] (`FeatureSpec` in the Python API). When creating a feature spec, you define a [[FeatureFunction]] that takes both precomputed feature columns from the feature table and context feature columns as input bindings. The context feature values are not stored in any table — they are provided as part of the query payload at serving time. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

### Example: Distance Calculation

A common use case for context features is calculating the distance between a fixed location (stored as a precomputed feature) and a user's current location (provided as a context feature):

1. A feature table stores destination locations with `destination_id` as the primary key and `latitude` and `longitude` as precomputed features.
2. A [[Unity Catalog|Unity Catalog function]] defines a `distance()` calculation using the Haversine formula.
3. In the feature spec, the function is bound with `latitude` and `longitude` mapped to feature table columns, and `user_latitude` and `user_longitude` mapped to context features supplied at inference time.

```python
features = [
    FeatureLookup(
        table_name="main.on_demand_demo.location_features",
        lookup_key="destination_id"
    ),
    FeatureFunction(
        udf_name="main.on_demand_demo.distance",
        output_name="distance",
        input_bindings={
            "latitude": "latitude",
            "longitude": "longitude",
            "user_latitude": "user_latitude",
            "user_longitude": "user_longitude"
        },
    ),
]
```

^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Querying with Context Features

When querying a feature serving endpoint, the request payload includes both the primary key values for the feature lookup and the context feature values. Using the MLflow Deployments API for Databricks:

```python
response = client.predict(
    endpoint="fse-location",
    inputs={
        "dataframe_records": [
            {"destination_id": 1, "user_latitude": 37, "user_longitude": -122},
            {"destination_id": 2, "user_latitude": 37, "user_longitude": -122},
        ]
    },
)
```

In this example, `destination_id` is the lookup key for the feature table, while `user_latitude` and `user_longitude` are context features used by the distance function. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Benefits

- **Real-time computation**: Enables calculations that depend on data that is constantly changing or not known until the moment of inference. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- **Reduced storage**: Context features do not need to be precomputed and stored in feature tables, saving storage resources. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- **Flexibility**: The same precomputed features can be combined with different context values for different users or scenarios. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- **Low latency**: The feature serving endpoint performs feature lookups and function execution within a single request-response cycle. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Requirements

- Context features must be defined in a [[FeatureSpec|Feature Spec]] as part of a `FeatureFunction`'s `input_bindings`. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- The function used must be a [[Unity Catalog|Unity Catalog function]] created using `CREATE OR REPLACE FUNCTION`. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- When querying the endpoint, context feature values must be included in the `dataframe_records` payload alongside the lookup keys. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Feature Serving — The serving infrastructure that delivers features for online inference
- [[FeatureSpec|Feature Spec]] — Configuration that binds feature lookups and on-demand functions together
- [[FeatureFunction]] — A Unity Catalog function applied at serving time with context feature bindings
- [[Online Feature Store]] — Stores precomputed features for low-latency serving
- [[Feature Lookup]] — Retrieves precomputed feature values by primary key
- On-Demand Feature Computation — The broader pattern of computing features at inference time
- MLflow Deployments API — Client API for querying serving endpoints

## Sources

- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
```

# Citations

1. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
