---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05bec160218f915869ebad90d206af46edb58e336f2b239da27e6ed65ec213ae
  pageDirectory: concepts
  sources:
    - point-in-time-feature-joins-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: point-in-time-feature-joins-databricks-on-aws.md
title: timestamp_lookup_key
description: A parameter in FeatureLookup that specifies which DataFrame column contains the timestamps against which to perform point-in-time lookups on a time series feature table.
tags:
  - api
  - feature-engineering
  - databricks
timestamp: "2026-06-19T19:56:55.753Z"
---

# timestamp_lookup_key

The **timestamp_lookup_key** is a parameter used in [FeatureLookup](/concepts/featurelookup.md) definitions within Databricks Feature Store to enable [Point-in-Time Feature Joins](/concepts/point-in-time-feature-joins.md). It specifies the column in the training or scoring DataFrame that contains timestamps against which time series features should be looked up.

## Purpose

When performing point-in-time lookups from a [Time series feature table](/concepts/time-series-feature-table.md), Databricks Feature Store retrieves the latest feature values that were recorded prior to the timestamps specified in the `timestamp_lookup_key` column. This ensures [Point-in-time correctness](/concepts/point-in-time-correctness.md) and prevents data leakage during model training. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Usage

The `timestamp_lookup_key` is specified as a parameter in a `FeatureLookup` object when creating a training set. Any `FeatureLookup` on a time series feature table must include a `timestamp_lookup_key` column. ^[point-in-time-feature-joins-databricks-on-aws.md]

### Example

```python
feature_lookups = [
    FeatureLookup(
        table_name="ml.ads_team.user_features",
        feature_names=["purchases_30d", "is_free_trial_active"],
        lookup_key="u_id",
        timestamp_lookup_key="ad_impression_ts"
    )
]

training_set = fe.create_training_set(
    df=raw_clickstream,
    feature_lookups=feature_lookups,
    exclude_columns=["u_id", "ad_id", "ad_impression_ts"],
    label="did_click",
)
training_df = training_set.load_df()
```

^[point-in-time-feature-joins-databricks-on-aws.md]

### Key Behavior

- Feature Store retrieves the most recent feature values from the time series feature table whose primary keys (excluding timestamp keys) match the DataFrame's `lookup_key` columns and whose timestamps are **not later than** the value in the `timestamp_lookup_key` column. ^[point-in-time-feature-joins-databricks-on-aws.md]
- If no feature value exists prior to the given timestamp, `null` is returned. ^[point-in-time-feature-joins-databricks-on-aws.md]
- Point-in-time lookup does not skip rows with `null` feature values stored in the time series feature table. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Relationship to Time Series Feature Tables

Time series feature tables are created by declaring a timestamp column using the `timeseries_columns` argument (for Feature Engineering in Unity Catalog) or the `timestamp_keys` argument (for Workspace Feature Store). These tables include both a primary key and a timestamp key column. When performing feature lookups, the `timestamp_lookup_key` tells the system which column in the input DataFrame provides the timestamps for the AS OF join. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Scoring with Time Series Features

When scoring a model trained with features from time series feature tables, the DataFrame passed to `score_batch` must contain a timestamp column with the **same name** and `DataType` as the `timestamp_lookup_key` used during training. Feature Store retrieves features using point-in-time lookups based on metadata packaged with the model. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Related Parameters

- [lookup_key](/concepts/feature-lookup-keys.md) – The column specifying primary keys for feature lookup, used alongside `timestamp_lookup_key`.
- lookback_window – An optional parameter that limits how far back in time to consider feature values, specified as a `datetime.timedelta`.
- [FeatureLookup](/concepts/featurelookup.md) – The API object that contains both `lookup_key` and `timestamp_lookup_key`.

## Sources

- point-in-time-feature-joins-databricks-on-aws.md

# Citations

1. [point-in-time-feature-joins-databricks-on-aws.md](/references/point-in-time-feature-joins-databricks-on-aws-2568db47.md)
