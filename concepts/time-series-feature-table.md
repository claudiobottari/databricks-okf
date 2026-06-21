---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4472fbb7c387cb715ce65300adfafb403126295e99db5867a734773275a64f6a
  pageDirectory: concepts
  sources:
    - point-in-time-feature-joins-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-feature-table
    - TSFT
    - Time-Series Feature Store
  citations:
    - file: point-in-time-feature-joins-databricks-on-aws.md
title: Time series feature table
description: A feature table that includes a TIMESTAMP primary key column, enabling point-in-time AS OF joins so that each training row uses the latest feature value prior to the label's timestamp.
tags:
  - feature-store
  - time-series
  - databricks
timestamp: "2026-06-19T19:56:31.276Z"
---

# Time series feature table

A **time series feature table** is a [Feature Table](/concepts/feature-table.md) that includes a timestamp key column to enable *point-in-time correctness* when joining features to a training dataset. By ensuring each row in the training set reflects the latest known feature values *as of* the time the label was observed, time series feature tables prevent data leakage — a subtle but harmful error that occurs when future information is used to predict the past. ^[point-in-time-feature-joins-databricks-on-aws.md]

You should use time series feature tables whenever feature values change over time, for example with time series data, event-based data, or time-aggregated data. ^[point-in-time-feature-joins-databricks-on-aws.md]

## How time series feature tables work

Time series feature tables rely on an **AS OF join** to match feature values with label observations. The join matches rows based on the primary key (for example, a sensor or user ID) and then retrieves the most recent value of the feature that occurs *on or before* the timestamp of the label row. If no feature value has been recorded before that timestamp, the result is `null`. ^[point-in-time-feature-joins-databricks-on-aws.md]

A concrete example: suppose a sensor table records CO₂ readings with a timestamp, and a ground‑truth table records whether a person was present in the room at a given moment. Without point‑in‑time logic, a training row might pair a CO₂ reading taken at 8:52 with a label recorded at 8:50 — using future data to predict the past. Time series feature tables eliminate this kind of error. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Requirements

To activate point‑in‑time lookups, you must designate the timestamp column in the feature table’s definition:

- **Feature Engineering in Unity Catalog** (any version): use the `timeseries_columns` argument when creating the table.
- **Workspace Feature Store (legacy)** (v0.3.7+): use the `timestamp_keys` argument.

If you only declare a time‑series column as a *primary key* without using `timeseries_columns` or `timestamp_keys`, the Feature Store will match rows by *exact* time match only — it will not apply point‑in‑time logic. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Creating a time series feature table in Unity Catalog

In Unity Catalog, any table with a `TIMESERIES` primary key is a time series feature table. The timestamp key column must be of type `TimestampType` or `DateType`. Databricks recommends that time series feature tables have no more than two primary key columns for performant writes and lookups. Partition columns are not allowed on time series feature tables. ^[point-in-time-feature-joins-databricks-on-aws.md]

The following example creates a time series feature table using the Python `FeatureEngineeringClient`:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

fe.create_table(
    name="catalog.schema.user_behavior_features",
    primary_keys=["user_id", "event_timestamp"],
    timeseries_columns="event_timestamp",  # Enables point-in-time logic
    df=features_df
)
```

An important caveat: if a `DATE` or `TIMESTAMP` column is a primary key but is *not* declared via `timeseries_columns`, you cannot use the table with `create_feature_spec()`, `create_training_set()`, or `publish_table()`. For use cases that require exact‑match lookup semantics (no point‑in‑time logic), change the column type to `STRING`. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Publishing time series tables to online stores

When you publish a time series feature table to an online store (for example, for real‑time inference), you have two modes:^[point-in-time-feature-joins-databricks-on-aws.md]

- **Snapshot mode** – publishes only the latest feature value for each primary key. The online store supports key lookups but not point‑in‑time lookups. This is the default for providers that do not support time to live (TTL).
- **Window mode** – publishes *all* feature values for each primary key and automatically removes expired records. A record is expired if its timestamp (in UTC) is older than the specified TTL duration. The online store retrieves the value with the latest timestamp on each lookup.

To use window mode, you must set a `ttl` in the `OnlineStoreSpec` when creating the online store. The TTL cannot be changed afterward. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Updating a time series feature table

When writing features to a time series feature table, the DataFrame must supply values for *all* features of the table — unlike regular feature tables, which allow partial writes. This constraint reduces sparsity of feature values across timestamps. Both batch and streaming writes are supported; use `mode="merge"` for upserts. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Creating a training set with point‑in‑time lookups

To build a training set from a time series feature table, include a `FeatureLookup` with the `timestamp_lookup_key` parameter. This parameter specifies the column in your label DataFrame that contains the timestamps against which feature values should be looked up. The Feature Store returns the most recent feature value *prior to* each timestamp for the matching primary key(s). ^[point-in-time-feature-joins-databricks-on-aws.md]

Example:

```python
from databricks.feature_engineering import FeatureLookup

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

You can also set a `lookback_window` (as a `datetime.timedelta`) to exclude feature values older than a certain period. During online inference, the latest value is always used regardless of the lookback window. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Scoring models

When scoring a model trained with time series features, the DataFrame passed to `score_batch` must contain a timestamp column with the same name and `DataType` as the `timestamp_lookup_key` used during training. The Feature Store uses the metadata packaged with the model to perform the point‑in‑time lookup automatically. ^[point-in-time-feature-joins-databricks-on-aws.md]

For faster lookup performance with Photon enabled (and `databricks-feature-engineering` ≥0.6.0), you can pass `use_spark_native_join=True` to both `create_training_set` and `score_batch`. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Performance recommendations

- Use [Liquid Clustering](/concepts/liquid-clustering.md) on time series tables (requires `databricks-feature-engineering` ≥0.6.0) for better point‑in‑time lookup performance.
- Limit time series feature tables to two primary key columns at most.
- For broad compatibility, any Delta table in Unity Catalog with primary keys and a timestamp key can serve as a time series feature table (Databricks Runtime 13.3 LTS and above). ^[point-in-time-feature-joins-databricks-on-aws.md]

## Sources

- point-in-time-feature-joins-databricks-on-aws.md

# Citations

1. [point-in-time-feature-joins-databricks-on-aws.md](/references/point-in-time-feature-joins-databricks-on-aws-2568db47.md)
