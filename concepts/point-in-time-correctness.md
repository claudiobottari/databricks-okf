---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a3ce4d90fd3d527bd063997624d900a874fc04daa02363174127da2b06e570d
  pageDirectory: concepts
  sources:
    - point-in-time-feature-joins-databricks-on-aws.md
    - train-models-with-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - point-in-time-correctness
    - Point‑in‑Time Correctness
    - point-in-time correct
  citations:
    - file: point-in-time-feature-joins-databricks-on-aws.md
    - file: train-models-with-declarative-features-databricks-on-aws.md
title: Point-in-time correctness
description: A join strategy that ensures training datasets reflect only feature values that existed as of the timestamp of each label observation, preventing data leakage.
tags:
  - feature-engineering
  - time-series
  - machine-learning
timestamp: "2026-06-19T19:56:14.602Z"
---

# Point-in-time correctness

**Point-in-time correctness** is a property of training dataset creation that ensures feature values reflect the state of the world *as of the time each label observation was recorded*. It is a critical mechanism for preventing data leakage in [machine learning](/concepts/cicd-for-machine-learning.md) workflows. ^[point-in-time-feature-joins-databricks-on-aws.md, train-models-with-declarative-features-databricks-on-aws.md]

## Importance

Without point-in-time correctness, a training dataset may inadvertently include feature values that were not available at the time the label occurred. For example, a future sensor reading could be joined to a past ground-truth observation. This type of error — known as data leakage — can be hard to detect and negatively affects the model's ability to generalize. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Mechanism

Point-in-time correctness is achieved through **time series feature tables**, which include a timestamp key column in addition to the primary key(s). When a training dataset is assembled, the system performs an **AS OF join**: for each observation (label row), it retrieves the most recent feature value that has a timestamp *less than or equal to* the observation's timestamp. If no such value exists, the feature value is set to `null`. This ensures that only data available before the label moment is used. ^[point-in-time-feature-joins-databricks-on-aws.md]

In Databricks, the point-in-time logic is activated by designating one or more columns as time series keys:
- For **Feature Engineering in Unity Catalog**, use the `timeseries_columns` argument when creating a feature table.
- For the **Workspace Feature Store (legacy)**, use the `timestamp_keys` argument.

If a `DATE` or `TIMESTAMP` column is declared as a primary key but not as a timeseries key, the system performs an exact-time match only — it does **not** apply point-in-time AS OF logic. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Requirements

| Context | Requirement |
|---------|-------------|
| **Unity Catalog** | A table with a `TIMESERIES` primary key constraint (see create feature table). Must have exactly one timestamp key; no partition columns are allowed. The timestamp column must be `TimestampType` or `DateType`. |
| **Workspace Feature Store** | Feature Store client v0.3.7 or above. The `timestamp_keys` argument must be used when creating or updating the feature table. |
| **General** | Databricks recommends no more than two primary key columns for time series feature tables to ensure performant writes and lookups. Liquid clustering (available with `databricks-feature-engineering` 0.6.0+) is recommended for better lookup performance. |

^[point-in-time-feature-joins-databricks-on-aws.md]

## Creating a time series feature table

When writing features to a time series feature table, the DataFrame must supply values for **all** features of the table (unlike regular feature tables). This constraint reduces sparsity of feature values across timestamps.

- Feature Engineering in Unity Catalog (Python API):

```python
fe = FeatureEngineeringClient()
fe.create_table(
    name="catalog.schema.user_behavior_features",
    primary_keys=["user_id", "event_timestamp"],
    timeseries_columns="event_timestamp",
    df=features_df
)
```

- Write mode must be `"merge"` (or streaming write) so that updates correctly replace feature values for the same primary key and timestamp. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Creating a training set with point-in-time lookups

To perform a point-in-time lookup from a time series feature table, include a `FeatureLookup` object that specifies:
- `lookup_key` – column(s) in the training DataFrame that match the feature table's primary keys (excluding the timestamp key).
- `timestamp_lookup_key` – column in the training DataFrame containing the timestamps against which to match the feature table's time series key.

Example (Unity Catalog):

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup

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
    label="did_click"
)
training_df = training_set.load_df()
```

The system retrieves the latest feature value for each primary key (excluding timestamp key) that is not later than the value of `timestamp_lookup_key` for that row. ^[point-in-time-feature-joins-databricks-on-aws.md]

For faster lookup performance with Photon enabled, set `use_spark_native_join=True` (requires `databricks-feature-engineering` 0.6.0+). ^[point-in-time-feature-joins-databricks-on-aws.md]

### Declarative features

When using [declarative features](/concepts/declarative-feature-engineering-api.md) (the `Feature` API with `DeltaTableSource`), point-in-time correctness is automatically applied. The `Feature` object must include a `timeseries_column` parameter. During `create_training_set`, the system computes features using only source data available before each row's timestamp. ^[train-models-with-declarative-features-databricks-on-aws.md]

## Lookback window

Optionally, you can limit how far back the system looks for feature values by setting the `lookback_window` parameter on a `FeatureLookup`. Its value must be a `datetime.timedelta`. If set, the system excludes feature values with timestamps older than the specified duration relative to the observation's timestamp.

```python
from datetime import timedelta

feature_lookups = [
    FeatureLookup(
        table_name="...",
        feature_names=["purchases_30d"],
        lookup_key="u_id",
        timestamp_lookup_key="ad_impression_ts",
        lookback_window=timedelta(days=7)
    )
]
```

During training and batch inference, the lookback window is applied. During online inference, the latest feature value is always used, regardless of the lookback window. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Scoring models with time series feature tables

When performing batch inference with `score_batch`, the model's feature metadata (packaged during `log_model`) is used to automatically compute point-in-time correct features. The DataFrame passed to `score_batch` must contain:
- The entity columns (primary keys except timestamp) used during training.
- A timestamp column with the same name and `DataType` as the `timestamp_lookup_key` from training.

```python
predictions = fe.score_batch(
    model_uri="models:/main.ecommerce.fraud_model/1",
    df=inference_df
)
```

Photon-accelerated scoring is available with `use_spark_native_join=True` (requires `databricks-feature-engineering` 0.6.0+). ^[point-in-time-feature-joins-databricks-on-aws.md, train-models-with-declarative-features-databricks-on-aws.md]

## Publishing time series features to online stores

Time series feature tables can be published to an online store using `publish_table`. Two modes are supported:

- **Snapshot mode** – Publishes only the latest feature value for each primary key. The online store supports primary key lookup but not point-in-time lookup. This is the default for stores without TTL.

- **Window mode** – Publishes all feature values for each primary key and automatically removes expired records. A record is expired if its timestamp (UTC) is more than the specified time-to-live (TTL) duration in the past. The online store stores the record with the latest timestamp.

To use window mode, provide a `ttl` in the `OnlineStoreSpec` at creation time. The TTL cannot be changed afterward. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Related concepts

- Data leakage
- [Feature Store](/concepts/feature-store.md)
- [Time series feature table](/concepts/time-series-feature-table.md)
- Declarative features
- [AS OF join](/concepts/as-of-join.md)
- [Online store](/concepts/online-feature-store.md)

## Sources

- point-in-time-feature-joins-databricks-on-aws.md
- train-models-with-declarative-features-databricks-on-aws.md

# Citations

1. [point-in-time-feature-joins-databricks-on-aws.md](/references/point-in-time-feature-joins-databricks-on-aws-2568db47.md)
2. [train-models-with-declarative-features-databricks-on-aws.md](/references/train-models-with-declarative-features-databricks-on-aws-bc572b9c.md)
