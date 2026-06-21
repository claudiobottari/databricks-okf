---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6c6b2b5f0c3757c520ba7bf8504ab6522deb529ad392be8150cf87091f5ea6c
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - covariates-external-regressors-for-forecasting
    - C(RFF
    - Covariates and External Regressors
    - External Regressors / Covariates
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Covariates (External Regressors) for Forecasting
description: Additional variables outside the target time series that can improve forecasting model accuracy by providing external context.
tags:
  - machine-learning
  - time-series
  - forecasting
  - automl
timestamp: "2026-06-19T14:06:54.278Z"
---

# Covariates (External Regressors) for Forecasting

**Covariates (External Regressors)** are additional variables outside the target time series that can be used to improve the accuracy of forecasting models. They capture exogenous factors that influence the predicted quantity but are not part of the historical values of the series itself.

## Overview

When building a forecasting model, the primary input is the history of the target variable (e.g., daily hotel occupancy rates). Covariates bring in extra information—such as day-of-week indicators, holiday flags, weather data, or promotional calendars—that the model can leverage to make better predictions. By including relevant covariates, the model can learn patterns that are not apparent from the target series alone. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

On Databricks, covariates are supported through AutoML forecasting experiments. They must be stored as [Feature Store](/concepts/feature-store.md) tables and then joined to the primary training data via the `feature_store_lookups` parameter. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Example: Hotel Occupancy Forecasting

A common use case is predicting hotel occupancy rates. For instance, knowing whether a given date falls on a weekend can help the model capture higher demand patterns on Saturdays and Sundays. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Creating the Data

The example generates random daily occupancy data for January 2024 and then forecasts the occupancy rate for February 1, 2024.

```python
df = spark.sql("""
  SELECT explode(sequence(to_date('2024-01-01'), to_date('2024-01-31'), interval 1 day)) as date,
         rand() as occupancy_rate
  FROM (SELECT 1 as id) tmp
  ORDER BY date
""")
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Feature Engineering

A simple covariate, `is_weekend`, is computed from the `date` column using the day of the week.

```python
from pyspark.sql.functions import dayofweek, when

def compute_hotel_weekend_features(df):
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)
        .when(dayofweek("date").isin(6, 7), 1)
    )

hotel_weekend_feature_df = compute_hotel_weekend_features(df)
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Storing Covariates in the Feature Store

Covariates must be registered as a [Feature Store](/concepts/feature-store.md) table so that AutoML can look them up during training. The table must have a primary key (typically the time column) that will be used to join with the training data.

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',
    primary_keys=['date'],
    df=hotel_weekend_feature_df,
    description='Hotel is_weekend features table'
)
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

Feature tables can also be created using SQL or Delta Live Tables. See [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) for more options. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Configuring AutoML with Covariates

The `feature_store_lookups` parameter of the `automl.forecast()` function specifies which Feature Store tables to join and which column(s) to use as lookup keys.

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

You can include multiple lookups in the list, each referencing a different feature table. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Running the Experiment

Pass the `feature_lookups` to the AutoML forecasting API call along with the training dataset, target column, time column, frequency, and horizon.

```python
from databricks import automl

summary = automl.forecast(
    dataset=df,
    target_col="occupancy_rate",
    time_col="date",
    frequency="d",
    horizon=1,
    timeout_minutes=30,
    identity_col=None,
    feature_store_lookups=feature_lookups
)
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Best Practices

- **Select relevant covariates** – Only include factors that have a causal or correlational relationship with the target.
- **Ensure Lookup Keys Align** – The `lookup_key` column(s) in the feature table must match a column in the training dataset (typically the date/time column).
- **Use Feature Store** – All covariates must be registered as Feature Store tables to be accessible by AutoML.
- **Handle Future Values** – For forecasting, covariates must be known for the forecast horizon (e.g., a `is_weekend` flag can be computed for future dates).

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The main entry point for automated time series modeling.
- [Feature Store](/concepts/feature-store.md) – Central repository for storing and serving features, including covariates.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – Broader topic covering models and techniques.
- [Unity Catalog](/concepts/unity-catalog.md) – Governs Feature Store tables and other data assets.

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
