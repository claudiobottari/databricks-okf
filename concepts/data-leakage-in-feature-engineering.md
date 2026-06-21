---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2e949e412b94bf86e5a8abea5f885f1902703ecdcb64ee1e1adee39c625765c
  pageDirectory: concepts
  sources:
    - point-in-time-feature-joins-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-leakage-in-feature-engineering
    - DLIFE
  citations:
    - file: point-in-time-feature-joins-databricks-on-aws.md
title: Data leakage in feature engineering
description: A modeling error that occurs when feature values unavailable at prediction time (e.g., future data) are included in the training set, degrading model performance.
tags:
  - machine-learning
  - data-quality
  - feature-engineering
timestamp: "2026-06-19T19:56:13.540Z"
---

# Data Leakage in Feature Engineering

**Data leakage** in feature engineering occurs when feature values used for model training include information that was not available at the time the label (target variable) was recorded. This type of error can be difficult to detect and can negatively affect the model's performance, leading to overly optimistic evaluation metrics and poor generalization to new data. ^[point-in-time-feature-joins-databricks-on-aws.md]

## How Data Leakage Occurs

Data leakage typically arises when training datasets are constructed without proper temporal alignment between features and labels. For example, if a sensor reading taken at 8:52 AM is used as a feature to predict whether a person was present in a room at 8:50 AM, the feature contains future information that would not have been available at prediction time. This "future data" leaks into the training set, impairing the model's real-world performance. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Preventing Data Leakage with Point-in-Time Correctness

The primary technique for preventing data leakage in feature engineering is **point-in-time correctness**, which ensures that each training example reflects feature values as of the time the label observation was recorded. This is achieved through [Point-in-Time Feature Joins](/concepts/point-in-time-feature-joins.md), which use timestamp keys to match features to labels based on temporal ordering. ^[point-in-time-feature-joins-databricks-on-aws.md]

### Time Series Feature Tables

[Time Series Feature Tables](/concepts/time-series-feature-tables.md) include a timestamp key column that ensures each row in the training dataset represents the latest known feature values as of the row's timestamp. These tables should be used whenever feature values change over time, such as with:

- Time series data
- Event-based data
- Time-aggregated data

^[point-in-time-feature-joins-databricks-on-aws.md]

### AS OF Joins

Point-in-time correctness is implemented using **AS OF joins**, which match feature values based on the primary key and timestamp key. The AS OF join ensures that the most recent value of the feature at the time of the timestamp is used in the training set, rather than any future values. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Requirements for Point-in-Time Lookups

To use point-in-time functionality and prevent data leakage, you must specify time-related keys using the `timeseries_columns` argument (for Feature Engineering in Unity Catalog) or the `timestamp_keys` argument (for Workspace Feature Store). This indicates that feature table rows should be joined by matching the most recent value for a particular primary key that is not later than the value of the timestamp column. ^[point-in-time-feature-joins-databricks-on-aws.md]

If you only designate a time series column as a primary key column without using `timeseries_columns` or `timestamp_keys`, the feature store does not apply point-in-time logic during joins. Instead, it matches only rows with an exact time match, which can still lead to leakage if future timestamps are present. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Lookback Windows

To further prevent leakage from stale features, you can set a **lookback window** using the `lookback_window` parameter in `FeatureLookup`. This excludes feature values with timestamps older than a specified duration (e.g., 7 days) from the training set. The lookback window is applied during training and batch inference, but during online inference, the latest feature value is always used regardless of the window. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Related Concepts

- [Point-in-Time Feature Joins](/concepts/point-in-time-feature-joins.md)
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md)
- [Feature Store](/concepts/feature-store.md)
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- Training Data Quality

## Sources

- point-in-time-feature-joins-databricks-on-aws.md

# Citations

1. [point-in-time-feature-joins-databricks-on-aws.md](/references/point-in-time-feature-joins-databricks-on-aws-2568db47.md)
