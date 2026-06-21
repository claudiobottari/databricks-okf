---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e61074708f0eafd04c96c7c35ec8da5bf1a1e86cacedd9d3faf6c42ad3783e29
  pageDirectory: concepts
  sources:
    - point-in-time-feature-joins-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - as-of-join
    - AOJ
    - As‑of Join
  citations:
    - file: point-in-time-feature-joins-databricks-on-aws.md
title: AS OF join
description: A temporal join that matches each row in the label DataFrame with the most recent feature value from a time series feature table whose timestamp is not later than the label's timestamp.
tags:
  - temporal-joins
  - feature-engineering
  - sql
timestamp: "2026-06-19T19:56:29.545Z"
---

# AS OF join

An **AS OF join** is a join operation that retrieves the most recent value of a feature for a given primary key as of a specified timestamp, rather than matching rows based on exact time equality. In Databricks Feature Store, AS OF joins are used to ensure point-in-time correctness when creating training datasets from time series feature tables. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Purpose

AS OF joins prevent data leakage during model training. Data leakage occurs when a training row includes feature values that were not yet available at the time the label was observed. By using an AS OF join, the training dataset reflects only feature values that were known *before* the label timestamp, preserving the temporal ordering of cause and effect. ^[point-in-time-feature-joins-databricks-on-aws.md]

## How it works

Time series feature tables include a timestamp key column in addition to one or more primary key columns. When joining such a table to a label DataFrame, an AS OF join matches rows based on:
- The primary key(s) of the feature table.
- The timestamp key: for each label row, the join selects the most recent feature table row whose timestamp is **less than or equal to** the label’s timestamp and follows the same primary key. If no feature value exists before that timestamp, the feature value is `null`. ^[point-in-time-feature-joins-databricks-on-aws.md]

The following diagram from the Databricks documentation illustrates the concept: the orange outlined circles indicate the feature value chosen for each label timestamp.

![Point-in-time join overview](https://docs.databricks.com/aws/en/assets/images/point-in-time-overview-e5699d6917724a99703d41f544ac98b6.png)

## Requirements

To use an AS OF join, the feature table must declare a timestamp column as a *time series key*:
- In **Feature Engineering in Unity Catalog**: use the `timeseries_columns` argument when creating the feature table.
- In **Workspace Feature Store (legacy)**: use the `timestamp_keys` argument.

If a timestamp column is declared only as a primary key without being designated as a time series key, Feature Store performs an exact-match join instead of an AS OF join. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Using AS OF joins in training sets

When creating a training set, each `FeatureLookup` that references a time series feature table must specify a `timestamp_lookup_key`. This is the name of a column in the label DataFrame that contains the timestamps against which the AS OF join is performed. ^[point-in-time-feature-joins-databricks-on-aws.md]

```python
feature_lookups = [
    FeatureLookup(
        table_name="ml.ads_team.user_features",
        feature_names=["purchases_30d", "is_free_trial_active"],
        lookup_key="u_id",
        timestamp_lookup_key="ad_impression_ts"
    )
]
```

Any `FeatureLookup` on a time series feature table must include a `timestamp_lookup_key`; point-in-time lookup is always used. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Lookback window

You can restrict the AS OF join to only consider feature values that are recent enough. Pass a `lookback_window` parameter of type `datetime.timedelta` to `FeatureLookup`. For example, `timedelta(days=7)` excludes any feature values older than 7 days relative to the label timestamp. During training and batch inference the lookback window is applied; during online serving the latest value is always used. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Publishing time series features to online stores

When publishing a time series feature table to an online store, two modes are available:
- **Snapshot mode**: publishes only the latest feature value for each primary key. Supports primary key lookup but not point-in-time lookup.
- **Window mode**: publishes all feature values within a time-to-live (TTL) window. The online store automatically retrieves the most recent value for a given key. Window mode requires specifying a `ttl` in the `OnlineStoreSpec`. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Related concepts

- [Point-in-time join](/concepts/point-in-time-joins.md) – The general concept of temporal join correctness.
- Data leakage – The training error that AS OF joins prevent.
- [Feature Store](/concepts/feature-store.md) – Centralized repository for features.
- [Time series feature table](/concepts/time-series-feature-table.md) – A feature table with a timestamp key enabling AS OF joins.
- [FeatureLookup](/concepts/featurelookup.md) – API element for defining how features are retrieved during training.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – The modern interface for managing features.
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) – The legacy feature store interface.

## Sources

- point-in-time-feature-joins-databricks-on-aws.md

# Citations

1. [point-in-time-feature-joins-databricks-on-aws.md](/references/point-in-time-feature-joins-databricks-on-aws-2568db47.md)
