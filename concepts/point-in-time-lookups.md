---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4add00b63ccbae99100054fa0a6b6f99accb5f6334bd3ab28fea15df4f63342d
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - workspace-feature-store-deprecated-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - point-in-time-lookups
    - Point-in-Time Lookup
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: workspace-feature-store-deprecated-databricks-on-aws.md
title: Point-in-Time Lookups
description: A time-aware join technique for time series feature tables that ensures training data uses only feature values known up to the timestamp of each target observation.
tags:
  - time-series
  - feature-engineering
  - data-joining
timestamp: "2026-06-18T15:07:09.113Z"
---

# Point-in-Time Lookups

**Point-in-Time Lookups** are a feature of the Databricks [Feature Store](/concepts/feature-store.md) that ensure time-dependent data is correctly joined during model training and inference. When working with temporal data, lookups must consider only feature values that were known *at or before* the timestamp of the target observation, to prevent data leakage and inaccurate model evaluation. Point-in-time lookups perform an “as-of” timestamp join, retrieving the latest known feature values as of each row’s timestamp.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## When to Use

Point-in-time lookups are essential whenever feature values change over time. Common use cases include:

- **Time series data** – sensor readings, stock prices, or weather measurements.
- **Event-based data** – clickstream logs, transaction records, or interaction histories.
- **Time-aggregated data** – rolling averages, counters, or windowed statistics.

Without point-in-time lookups, a model could inadvertently be trained on future information, causing optimistic performance that will not hold in production.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## How It Works

A time series feature table includes a **timestamp column** that records when each feature value was valid. When you create a training dataset or score batch data, the Feature Store automatically performs an as-of join: for each row in the input data, it finds the most recent feature value from the feature table whose timestamp is at or before the row’s timestamp.

You enable this behavior by designating certain primary key columns as time series columns. In [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md), use the `timeseries_columns` argument when creating the feature table. In the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md), use the `timestamp_keys` argument. During `create_training_set` or `score_batch`, you also specify a `timestamp_lookup_key` that maps to the timestamp column of the input data.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Configuration

```python
from databricks.feature_engineering import FeatureEngineeringClient
fe = FeatureEngineeringClient()

# Create a time series feature table (Unity Catalog)
fe.create_table(
    name="catalog.schema.user_features",
    primary_keys=["user_id", "feature_date"],
    timeseries_columns=["feature_date"],   # <-- enables point-in-time lookups
    df=features_df,
    schema=features_df.schema,
)
```

When later creating a training set, the system joins on matching primary keys and picks the latest feature value whose timestamp ≤ the input row’s timestamp.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Important Notes

- If you include a timestamp column in the primary keys **without** using `timeseries_columns` or `timestamp_keys`, the Feature Store performs an exact time match instead of an as-of join. This means it will only join rows where the timestamp is identical, not the latest row before that time.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- Point-in-time lookups are a core benefit of the Databricks Feature Store, helping maintain data integrity for time-sensitive machine learning workflows.^[workspace-feature-store-deprecated-databricks-on-aws.md]

## Related Concepts

- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) – Feature tables with timestamp columns for temporal joins.
- [FeatureLookup](/concepts/featurelookup.md) – The mechanism that specifies which features to retrieve and how to join.
- [Training Set](/concepts/training-set-feature-store.md) – The dataset created by joining label data with feature values, respecting point-in-time logic.
- Batch Scoring – Offline inference where point-in-time lookups prevent future data leakage.
- [Online Feature Store](/concepts/online-feature-store.md) – Low-latency store for serving pre-computed features, often derived from time series tables.

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- workspace-feature-store-deprecated-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [workspace-feature-store-deprecated-databricks-on-aws.md](/references/workspace-feature-store-deprecated-databricks-on-aws-a64a8491.md)
