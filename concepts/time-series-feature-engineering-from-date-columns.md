---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46be3ee5688eb082a0de49c5c12119abefbdf9e92ecfcecf1fedd9790460d08a
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-feature-engineering-from-date-columns
    - TSFEFDC
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Time Series Feature Engineering from Date Columns
description: Techniques for deriving predictive features such as weekend indicators from date/time columns to enrich forecasting models.
tags:
  - feature-engineering
  - time-series
  - data-preparation
timestamp: "2026-06-19T22:11:46.135Z"
---

#Time Series Feature Engineering from Date Columns

**Time Series Feature Engineering from Date Columns** refers to the process of creating new predictor variables from a date/time column to improve forecasting models. Common date-derived features capture periodic patterns such as day of week, month, quarter, holiday indicators, or time since an event.

## Common Date-Based Features

Date columns can be decomposed into cyclical and binary features:

- **Temporal components**: year, month, day, hour, minute, second, day of year, week of year.
- **Cyclical encodings**: sine/cosine transforms for month, day of week, hour to preserve circular continuity.
- **Binary indicators**: `is_weekend`, `is_holiday`, `is_business_hour`, `is_month_end`.

## Example: `is_weekend` Feature

The source material demonstrates extracting an `is_weekend` binary indicator from a date column using PySpark. The logic uses `dayofweek()` (1=Sunday, 2=Monday, ..., 7=Saturday) and flags weekend days (Saturday and Sunday) as 1, weekdays as 0. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from pyspark.sql.functions import dayofweek, when

def compute_is_weekend_features(df):
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)          # Weekend
    )
```

This feature can improve forecasting models — for example, predicting hotel occupancy rates where weekends exhibit different behavior. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Engineered Features as Covariates

Feature-engineered columns from date can be stored in a [Feature Store](/concepts/feature-store.md) (e.g., a Unity Catalog feature table) and passed to [AutoML Forecasting](/concepts/automl-forecast.md) via the `feature_store_lookups` parameter. This allows AutoML to automatically join the date-based features with the primary training data. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – The broader task that benefits from date-based features.
- [Feature Store](/concepts/feature-store.md) – Centralized repository for reusable feature tables.
- [AutoML Forecasting](/concepts/automl-forecast.md) – Automated machine learning for time series, supporting covariate lookups.
- Cyclical Feature Encoding – Preserving periodic nature of time components (e.g., sine/cosine).
- Date/Time Columns – Raw input columns that serve as the source for derived features.

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
