---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9c9e6ed5056b7947bc0a00b625a072957dc791fd80cf9801b5ce5e39a08b3a8
  pageDirectory: concepts
  sources:
    - point-in-time-feature-joins-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lookback-window-for-feature-lookups
    - LWFFL
  citations:
    - file: point-in-time-feature-joins-databricks-on-aws.md
title: Lookback window for feature lookups
description: A timedelta parameter in FeatureLookup that excludes feature values older than a specified duration from the training set, applied during training and batch inference but not during online serving.
tags:
  - feature-engineering
  - time-series
  - api
timestamp: "2026-06-19T19:56:37.381Z"
---

#Lookback window for feature lookups

The **lookback window for feature lookups** is a parameter that limits the age of historical feature values used during point-in-time joins when creating training datasets or performing batch inference. It prevents the model from using stale features that are no longer relevant, while still allowing the point-in-time join to retrieve the most recent value within the specified time range.

## Overview

When you create a training set from a [Time series feature table](/concepts/time-series-feature-table.md), the point-in-time join retrieves the latest feature value *prior to* the timestamp in the label observation. Without a lookback window, all historical values are eligible, no matter how old they are. By setting a lookback window, you exclude feature values whose timestamp is older than a specified duration from the observation timestamp. This is useful when feature values become meaningless or should be treated as missing after a certain period (for example, a user's 30-day purchase history should not include data from 90 days ago). ^[point-in-time-feature-joins-databricks-on-aws.md]

## How to specify a lookback window

The lookback window is set on the `FeatureLookup` object via the `lookback_window` parameter. Its value must be a `datetime.timedelta` object. The default is `None`, meaning all feature values are used regardless of age. ^[point-in-time-feature-joins-databricks-on-aws.md]

The following example excludes any feature values that are more than 7 days old when performing the point-in-time join:

```python
from datetime import timedelta

feature_lookups = [
    FeatureLookup(
        table_name="ml.ads_team.user_features",
        feature_names=["purchases_30d", "is_free_trial_active"],
        lookup_key="u_id",
        timestamp_lookup_key="ad_impression_ts",
        lookback_window=timedelta(days=7)
    )
]
```^[point-in-time-feature-joins-databricks-on-aws.md]

## Behavior during training, batch inference, and online inference

The lookback window is applied during two phases:

- **Training** – When you call `create_training_set`, the point-in-time join automatically excludes feature values older than the lookback window. ^[point-in-time-feature-joins-databricks-on-aws.md]
- **Batch inference** – When you call `score_batch`, the same lookback logic is applied. ^[point-in-time-feature-joins-databricks-on-aws.md]

During **online inference**, the lookback window is ignored. The online store always returns the latest feature value for the given primary key, regardless of its age. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Requirements

- Feature Store client v0.13.0 or above (Workspace Feature Store).
- Any version of the Feature Engineering in Unity Catalog client.

^[point-in-time-feature-joins-databricks-on-aws.md]

## Related concepts

- [Point-in-Time Feature Joins](/concepts/point-in-time-feature-joins.md) – The broader technique for ensuring temporal correctness in training datasets.
- [Time series feature table](/concepts/time-series-feature-table.md) – A feature table that includes a timestamp key for point-in-time lookups.
- [FeatureLookup](/concepts/featurelookup.md) – The API object that defines how to retrieve features for training and inference.
- Data leakage – The problem that point-in-time joins and lookback windows help prevent.
- [Online store](/concepts/online-feature-store.md) – The serving layer where feature values are published for real-time inference.

## Sources

- point-in-time-feature-joins-databricks-on-aws.md

# Citations

1. [point-in-time-feature-joins-databricks-on-aws.md](/references/point-in-time-feature-joins-databricks-on-aws-2568db47.md)
