---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42f3e32d6354954ecf4e03e96861799159e0fd81c1b76edf1bff17738aefc6f3
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - on-demand-feature-computation-with-udfs
    - OFCWU
    - On-Demand Feature Computation
    - On-demand feature computation
    - on-demand feature computation
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: On-Demand Feature Computation with UDFs
description: Python UDFs registered in Unity Catalog can be used as FeatureFunctions to compute features on-demand during model inference
tags:
  - feature-store
  - udf
  - real-time-inference
timestamp: "2026-06-19T10:30:04.897Z"
---

# On-Demand Feature Computation with UDFs

**On-Demand Feature Computation with UDFs** refers to the practice of using user-defined functions (UDFs) in [Databricks Feature Store](/concepts/databricks-feature-store.md) to compute features at inference time rather than pre-computing and storing them in feature tables. This approach is useful when features depend on input data that is only available at request time, or when the computation is too dynamic to pre-materialize.

## Overview

On-demand features are computed by Python UDFs registered in [Unity Catalog](/concepts/unity-catalog.md) that transform raw input data into feature values during model inference. These UDFs are referenced in the feature engineering pipeline using `FeatureFunction` objects, which specify the UDF name, output column name, and input bindings that map raw data columns to UDF parameters. ^[feature-governance-and-lineage-databricks-on-aws.md]

## How It Works

When defining a training set or serving pipeline, you include `FeatureFunction` objects alongside `FeatureLookup` objects. The `FeatureFunction` specifies:

- **`udf_name`**: The fully qualified name of the UDF in Unity Catalog (e.g., `main.on_demand_demo.haversine_distance`).
- **`output_name`**: The name of the output column that will contain the computed feature value.
- **`input_bindings`**: A dictionary mapping UDF parameter names to column names in the input data.

At inference time, the Feature Store executes the UDF with the provided input bindings and returns the computed result as a feature column. ^[feature-governance-and-lineage-databricks-on-aws.md]

### Example

The following example demonstrates computing on-demand features for a restaurant recommendation model. The UDFs extract user location from a JSON blob and compute the haversine distance between the user and restaurant: ^[feature-governance-and-lineage-databricks-on-aws.md]

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
        "restaurant_id", "json_blob",
        "restaurant_latitude", "restaurant_longitude",
        "user_latitude", "user_longitude", "ts"
    ]
)
```

## Lineage Tracking

When you log a model using `FeatureEngineeringClient.log_model`, the on-demand feature UDFs used in the model are automatically tracked in the lineage graph. This lineage can be viewed in the **Lineage** tab of [Catalog Explorer](/concepts/catalog-explorer.md), showing the relationships between feature tables, UDFs, and models. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Use Cases

On-demand feature computation is particularly useful for:

- **User-specific features**: Features that depend on user attributes provided at inference time (e.g., user location, device type).
- **Derived features**: Features that combine multiple raw inputs (e.g., distance calculations, ratios, aggregations).
- **Dynamic transformations**: Features that require computation that cannot be pre-computed because the input data changes per request.
- **Sensitive data**: When raw data should not be stored as features but can be transformed on-the-fly.

## Best Practices

- **Register UDFs in Unity Catalog**: Ensure all on-demand feature UDFs are registered in Unity Catalog so they can be discovered and reused across models.
- **Use descriptive names**: Name UDFs clearly to indicate their purpose (e.g., `haversine_distance`, `extract_user_latitude`).
- **Test UDFs independently**: Validate UDF behavior before integrating them into feature pipelines.
- **Monitor performance**: On-demand computation adds latency at inference time; consider caching or pre-computing features that are expensive to compute and do not change per request.

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Central repository for managing and serving features
- [FeatureLookup](/concepts/featurelookup.md) — Pre-computed features from feature tables
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — Client API for creating training sets and logging models
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and lineage for features, functions, and models
- Lineage Tracking — Automatic tracking of feature-to-model relationships
- [Model Serving](/concepts/model-serving.md) — Deploying models with feature computation pipelines

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
