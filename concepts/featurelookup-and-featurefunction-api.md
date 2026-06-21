---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2cd7047ae92db4c5a7d87a36e22e160e1e420ce332f493308d911c1a67b9a4ec
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featurelookup-and-featurefunction-api
    - FeatureFunction API and FeatureLookup
    - FAFA
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: FeatureLookup and FeatureFunction API
description: Features for a training set can be defined via FeatureLookup (table-based) or FeatureFunction (UDF-based) to compute on-demand features
tags:
  - feature-store
  - api
  - feature-engineering
timestamp: "2026-06-19T10:29:53.517Z"
---

# FeatureLookup and FeatureFunction API

**FeatureLookup and FeatureFunction API** are components of the Databricks Feature Engineering client (`FeatureEngineeringClient`) that define how features are sourced for model training and inference. `FeatureLookup` retrieves features from existing feature tables, while `FeatureFunction` computes on-demand features using Python UDFs registered in Unity Catalog.

## Overview

When building a training set for a machine learning model, the `FeatureEngineeringClient.create_training_set()` method accepts a list of feature specifications. Each specification is either a `FeatureLookup` or a `FeatureFunction` that tells the client how to resolve feature values for the provided label data. Together, these APIs enable a modular, reusable approach to feature engineering. ^[feature-governance-and-lineage-databricks-on-aws.md]

## FeatureLookup

`FeatureLookup` defines a lookup from a feature table in Unity Catalog. It specifies which columns to retrieve, how to map them to output names, and which key columns in the label data to join on.

### Parameters

- **`table_name`**: The fully-qualified name of the feature table in Unity Catalog (e.g., `main.on_demand_demo.restaurant_features`).
- **`feature_names`**: A list of column names to retrieve from the feature table.
- **`rename_outputs`** (optional): A dictionary mapping original column names to new output names. This is useful when the same feature table is used multiple times with different aliases, or to avoid naming collisions.
- **`lookup_key`**: The column in the feature table that matches the key column in the label data. This determines how rows from the two tables are joined.
- **`timestamp_lookup_key`** (optional): The timestamp column used for point-in-time lookups, ensuring that feature values are retrieved as they existed at a specific time.

### Example

```python
from databricks.feature_engineering import FeatureLookup

FeatureLookup(
    table_name="main.on_demand_demo.restaurant_features",
    feature_names=["latitude", "longitude"],
    rename_outputs={
        "latitude": "restaurant_latitude",
        "longitude": "restaurant_longitude",
    },
    lookup_key="restaurant_id",
    timestamp_lookup_key="ts",
)
```

This lookup retrieves the `latitude` and `longitude` columns from the `restaurant_features` table, renames them for clarity, joins on `restaurant_id`, and uses the `ts` column for point-in-time correctness. ^[feature-governance-and-lineage-databricks-on-aws.md]

## FeatureFunction

`FeatureFunction` invokes a Python user-defined function (UDF) registered in Unity Catalog to compute a feature on demand. The UDF receives input bindings from columns in the label data or from other resolved features and returns a computed value.

### Parameters

- **`udf_name`**: The fully-qualified name of the UDF in Unity Catalog.
- **`output_name`**: The name of the output column that will contain the computed feature.
- **`input_bindings`**: A dictionary mapping UDF parameter names to the columns or expressions that provide their values. These sources can be columns from the label data or outputs from previously specified features.

### Example

```python
from databricks.feature_engineering import FeatureFunction

FeatureFunction(
    udf_name="main.on_demand_demo.haversine_distance",
    output_name="distance",
    input_bindings={
        "x1": "restaurant_longitude",
        "y1": "restaurant_latitude",
        "x2": "user_longitude",
        "y2": "user_latitude",
    },
)
```

This invocation computes the haversine distance between restaurant and user coordinates by binding the first pair of coordinates (from the renamed `FeatureLookup` outputs) and the second pair (from another `FeatureFunction` that extracts user coordinates). ^[feature-governance-and-lineage-databricks-on-aws.md]

## Using FeatureLookup and FeatureFunction Together

`FeatureLookup` and `FeatureFunction` are designed to compose naturally. A `FeatureFunction` can reference the renamed output of a `FeatureLookup` in its `input_bindings`, enabling a pipeline where base features are first retrieved from tables and then transformed by UDFs.

### Complete Example

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup, FeatureFunction

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name="main.on_demand_demo.restaurant_features",
        feature_names=["latitude", "longitude"],
        rename_outputs={
            "latitude": "restaurant_latitude",
            "longitude": "restaurant_longitude",
        },
        lookup_key="restaurant_id",
        timestamp_lookup_key="ts",
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
            "y2": "user_latitude",
        },
    ),
]

training_set = fe.create_training_set(
    label_df,
    feature_lookups=features,
    label="label",
    exclude_columns=[
        "restaurant_id", "json_blob",
        "restaurant_latitude", "restaurant_longitude",
        "user_latitude", "user_longitude", "ts",
    ],
)
```

In this pipeline:
1. `FeatureLookup` retrieves restaurant latitude and longitude from a feature table.
2. Two `FeatureFunction` calls extract user latitude and longitude from a JSON blob.
3. A final `FeatureFunction` computes the distance using all four coordinates.
4. The intermediate columns are excluded from the training set, leaving only the derived `distance` feature. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Lineage Tracking

When a model is logged using `FeatureEngineeringClient.log_model()`, the features used — both from `FeatureLookup` and `FeatureFunction` — are automatically tracked. This lineage appears in the Catalog Explorer **Lineage** tab, showing the relationships between feature tables, UDFs, and the model. This automatic tracking enables impact analysis and governance across the ML lifecycle. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Related Concepts

- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) – The client class that provides `create_training_set()` and `log_model()`.
- Feature Store and Unity Catalog – How feature tables are registered and governed.
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – Broader lineage tracking across data assets.
- User-Defined Functions in Unity Catalog – Registering Python UDFs for use with `FeatureFunction`.
- [Point-in-Time Lookups](/concepts/point-in-time-lookups.md) – The concept behind `timestamp_lookup_key`.

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
