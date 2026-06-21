---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4db459184f794216b3ce59393730dce87e43092ea18024aa095108befb1fc501
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - feature-lookup-with-timestamp-keys
    - FLWTK
    - Timestamp Keys
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: Feature Lookup with Timestamp Keys
description: Using FeatureLookup with a timestamp_lookup_key parameter to perform point-in-time lookups of feature values based on a time column in the label DataFrame.
tags:
  - feature-store
  - time-series
  - feature-lookup
timestamp: "2026-06-18T12:18:56.841Z"
---

# Feature Lookup with Timestamp Keys

**Feature Lookup with Timestamp Keys** refers to the use of the `timestamp_lookup_key` parameter in `FeatureLookup` to perform point-in-time feature retrieval from feature tables. By specifying a timestamp column, you ensure that each training or inference row receives feature values that were valid at the time indicated by that column, preventing data leakage from future observations. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Usage

When constructing a list of feature lookups for a training set, each `FeatureLookup` object accepts a `timestamp_lookup_key` parameter. This parameter names a column in the source DataFrame that contains the timestamp to use for the temporal join against the feature table. The feature table must also have a corresponding timestamp column that marks when each feature value was valid. ^[feature-governance-and-lineage-databricks-on-aws.md]

The `timestamp_lookup_key` is used together with the `lookup_key` (the join key) to retrieve the correct feature snapshot. In the example below, a `FeatureLookup` on the table `main.on_demand_demo.restaurant_features` uses `restaurant_id` as the lookup key and `ts` as the timestamp lookup key. The `ts` column is then excluded from the training set to avoid including it as a feature. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Example

The following code snippet shows a `FeatureLookup` that includes a `timestamp_lookup_key`:

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup

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
    # Additional FeatureFunction entries...
]

training_set = fe.create_training_set(
    label_df,
    feature_lookups=features,
    label="label",
    exclude_columns=[
        "restaurant_id", "json_blob",
        "restaurant_latitude", "restaurant_longitude",
        "user_latitude", "user_longitude",
        "ts"
    ]
)
```

In this example:
- `lookup_key="restaurant_id"` identifies the entity to join on.
- `timestamp_lookup_key="ts"` tells the Feature Store to use the `ts` column from the input label DataFrame to select the feature values that were current at that time.
- The `ts` column is listed in `exclude_columns` so it is not included as a model feature.

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Centralized repository for feature tables
- [FeatureLookup](/concepts/featurelookup.md) — The API object for defining a feature lookup
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — Client used to create training sets and log models
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) — Ensuring features do not leak future information
- [Feature Governance and Lineage](/concepts/feature-governance-and-lineage.md) — Automatically tracked lineage for feature tables and functions

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
