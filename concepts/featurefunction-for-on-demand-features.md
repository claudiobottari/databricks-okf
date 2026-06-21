---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ccddc784f532a55dcb39547ecc3d853702e94be3d4f6f5d5cc49bd368c5a731f
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featurefunction-for-on-demand-features
    - FFOF
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: FeatureFunction for On-Demand Features
description: A construct used with FeatureEngineeringClient to register Python UDFs that compute features on-demand at inference time, with lineage tracked like feature tables.
tags:
  - feature-store
  - udf
  - on-demand-features
timestamp: "2026-06-18T12:18:42.094Z"
---

# FeatureFunction for On-Demand Features

**FeatureFunction** is a component of the [Databricks Feature Store](/concepts/databricks-feature-store.md) that enables on-demand feature computation by applying user-defined functions (UDFs) to input data at inference or training time. Unlike [FeatureLookup](/concepts/featurelookup.md) which retrieves precomputed features from feature tables, FeatureFunction computes features dynamically by executing a registered Python UDF in [Unity Catalog](/concepts/unity-catalog.md).

## Overview

On-demand features are computed when needed rather than precomputed and stored in feature tables. This approach is useful when a feature value depends on runtime inputs or involves calculations that are impractical to precompute for all possible inputs. FeatureFunction allows you to specify a UDF registered in Unity Catalog, define input bindings that map source columns to the UDF's parameters, and designate the output column name.^[feature-governance-and-lineage-databricks-on-aws.md]

## How FeatureFunction Works

When you create a training set or serve a model using `FeatureEngineeringClient.log_model`, FeatureFunction executes the specified UDF on the provided input columns during feature computation. The UDF's output is then included as a feature in the training set or model inference pipeline.^[feature-governance-and-lineage-databricks-on-aws.md]

### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `udf_name` | The fully qualified name (three-level namespace) of the UDF registered in Unity Catalog |
| `output_name` | The name of the column that will contain the UDF's output |
| `input_bindings` | A dictionary mapping UDF parameter names to source column names from the input data |

^[feature-governance-and-lineage-databricks-on-aws.md]

## Example Usage

The following example demonstrates FeatureFunction for on-demand features in a restaurant recommendation model:^[feature-governance-and-lineage-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup, FeatureFunction

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name="main.on_demand_demo.restaurant_features",
        feature_names=["latitude", "longitude"],
        rename_outputs={
            "latitude": "restaurant_latitude",
            "longitude": "restaurant_longitude"
        },
        lookup_key="restaurant_id",
        timestamp_lookup_key="ts"
    ),
    FeatureFunction(
        udf_name="main.on_demand_demo.extract_user_latitude",
        output_name="user_latitude",
        input_bindings={"blob": "json_blob"},
    ),
    FeatureFunction(
        udf_name="main.on_demand_demo.extract_user_longitude",
        output_name="user_longitude",
        input_bindings={"blob": "json_blob"},
    ),
    FeatureFunction(
        udf_name="main.on_demand_demo.haversine_distance",
        output_name="distance",
        input_bindings={
            "x1": "restaurant_longitude",
            "y1": "restaurant_latitude",
            "x2": "user_longitude",
            "y2": "user_latitude"
        },
    )
]

training_set = fe.create_training_set(
    label_df,
    feature_lookups=features,
    label="label",
    exclude_columns=[
        "restaurant_id",
        "json_blob",
        "restaurant_latitude",
        "restaurant_longitude",
        "user_latitude",
        "user_longitude",
        "ts"
    ]
)
```

In this example, `extract_user_latitude` and `extract_user_longitude` are Python UDFs that parse a JSON blob to extract latitude and longitude values. The `haversine_distance` UDF then computes the geographic distance between the user and the restaurant using the extracted coordinates.^[feature-governance-and-lineage-databricks-on-aws.md]

## Lineage Tracking

When you log a model using `FeatureEngineeringClient.log_model`, FeatureStore automatically tracks the lineage of feature functions used in the model. This lineage appears in the **Lineage** tab of Catalog Explorer, showing the relationships between feature tables, functions, and models.^[feature-governance-and-lineage-databricks-on-aws.md]

To view lineage:

1. Navigate to the table, model version, or function page in Catalog Explorer.
2. Select the **Lineage** tab to see Unity Catalog components logged with that asset.
3. Click **See lineage graph** to explore the full lineage graph.^[feature-governance-and-lineage-databricks-on-aws.md]

## Access Control

Access to feature functions is governed by [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). Users must have the necessary permissions on the UDFs and feature tables they reference. See [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) for details on managing access control.^[feature-governance-and-lineage-databricks-on-aws.md]

## Related Concepts

- [FeatureLookup](/concepts/featurelookup.md) — Retrieves precomputed features from feature tables
- [Feature Store](/concepts/feature-store.md) — Central repository for managed features
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The client API for creating training sets and logging models
- [Python UDFs in Unity Catalog](/concepts/python-udfs-in-unity-catalog.md) — User-defined functions that can be used as on-demand feature transformers
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Tracking data flow across assets
- MLflow Models — Models logged with feature metadata and lineage

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
