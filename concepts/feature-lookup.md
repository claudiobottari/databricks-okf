---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56d0208e8ca711a064b38accb1b1dc3728f9432955dd2d3a6d74a2b5374735f6
  pageDirectory: concepts
  sources:
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-lookup
  citations:
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
title: Feature Lookup
description: A mechanism to retrieve precomputed features from a feature table by primary key at serving time
tags:
  - feature-store
  - retrieval
  - lookup
timestamp: "2026-06-19T18:44:19.467Z"
---

# Feature Lookup

**Feature Lookup** is a component of the Databricks [Feature Engineering Client](/concepts/featureengineeringclient-api.md) that specifies which precomputed features from a feature table should be retrieved and served at inference time. It is used when constructing a [FeatureSpec](/concepts/featurespec.md), which defines the complete set of features an endpoint serves. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Overview

A `FeatureLookup` object declares a reference to a feature table stored in Unity Catalog and identifies the **lookup key** that matches the primary key of that table. When a serving endpoint receives a request, it uses the lookup key to fetch the corresponding feature values from the online store or offline table. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

Feature lookups are intended for precomputed, static (or periodically updated) feature values. For features that must be computed on the fly — such as a distance calculation that depends on live user input — a [FeatureFunction](/concepts/featurefunction.md) is used instead. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Key Properties

| Property | Description |
|----------|-------------|
| `table_name` | The full Unity Catalog name of the feature table (`catalog.schema.table`). |
| `lookup_key` | The column name that acts as the primary key for the feature table. This key is provided in the request payload to identify which row(s) to retrieve. |

The source example shows a feature lookup against the table `feature_table_name` using `"destination_id"` as the lookup key. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Usage in FeatureSpec

`FeatureLookup` objects are passed as a list to the `features` parameter of `FeatureEngineeringClient.create_feature_spec()`. The resulting FeatureSpec can then be deployed to a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md), which handles the orchestration of lookups and function calls for each inference request. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

### Example

```python
from databricks.feature_engineering import FeatureLookup, FeatureFunction, FeatureEngineeringClient

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name=feature_table_name,
        lookup_key="destination_id"
    ),
    FeatureFunction(
        udf_name=function_name,
        output_name="distance",
        input_bindings={
            "latitude": "latitude",
            "longitude": "longitude",
            "user_latitude": "user_latitude",
            "user_longitude": "user_longitude"
        },
    ),
]

fe.create_feature_spec(name=feature_spec_name, features=features, exclude_columns=None)
```

^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [FeatureSpec](/concepts/featurespec.md) – The collection of FeatureLookups and FeatureFunctions that defines a serving endpoint's schema.
- [FeatureFunction](/concepts/featurefunction.md) – Defines an on-demand computation using a Unity Catalog UDF.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The Python API used to create online stores, feature tables, and feature specs.
- Feature Serving – The serving infrastructure that uses a FeatureSpec to serve features with low latency.
- [Online Feature Store](/concepts/online-feature-store.md) – The low-latency store that backs feature lookups for real-time serving.

## Sources

- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md

# Citations

1. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
