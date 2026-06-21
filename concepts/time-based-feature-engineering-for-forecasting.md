---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4f989bd4edcfa60a59c5e0269f4bcb66805d9b10b3b87ec8607d526f747509e
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-based-feature-engineering-for-forecasting
    - TFEFF
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Time-Based Feature Engineering for Forecasting
description: Creating derived temporal features such as is_weekend from date columns to improve forecasting model performance
tags:
  - feature-engineering
  - time-series
  - databricks
timestamp: "2026-06-19T09:07:00.763Z"
---

# Time-Based Feature Engineering for Forecasting

**Time-based feature engineering** is the practice of creating predictive input variables from the temporal components of a date or timestamp column in a time-series dataset. These engineered features help forecasting models capture recurring patterns—such as daily, weekly, or seasonal cycles—that are not directly present in the raw target variable. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Common Time-Based Features

The most frequently used time-based features include:

- **Day of week** (1–7 or Monday–Sunday)
- **Weekend indicator** (binary: 1 if Saturday or Sunday, else 0)
- **Month** (1–12)
- **Day of month** (1–31)
- **Week of year**
- **Quarter**
- **Holiday indicator**
- **Hour of day** (for hourly data)
- **Is business day** indicator

These features are considered **covariates** (also called external regressors)—additional variables outside the target time series that can improve forecasting models. For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend helps predict customer behavior. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Engineering a Weekend Indicator (Example)

The following example uses a randomized hotel‑occupancy dataset and a PySpark `compute_hotel_weekend_features` function to create an `is_weekend` binary feature:

```python
from pyspark.sql.functions import dayofweek, when

def compute_hotel_weekend_features(df):
    ''' Returns a DataFrame with 'date' as primary key '''
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)           # Weekend
    )
```

The function reads the original Spark DataFrame (which contains a `date` column) and appends the `is_weekend` column while preserving the `date` primary key. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Storing Features for Reuse

Once computed, time-based features should be stored as a [Feature Store](/concepts/feature-store.md) table so they can be joined with training and inference data consistently. Using the Databricks `FeatureEngineeringClient`:

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

Feature tables can also be created using SQL or Delta Live Tables. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Time-Based Covariates in AutoML Forecasting

To include engineered time features in an [AutoML Forecasting](/concepts/automl-forecast.md) experiment, pass them via the `feature_store_lookups` parameter. This parameter accepts a list of dictionaries, each specifying the feature table name and the lookup key(s) to join with the primary training data:

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [hotel_weekend_feature_lookup]

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

Multiple feature table lookups can be provided in the list, enabling you to combine several time-based feature tables (e.g., weekend indicators, holiday calendars, weather data) in a single experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Best Practices

- **Compute features at the grain of the prediction**: Ensure the feature table's primary key matches the date or timestamp granularity of the training data.
- **Avoid look‑ahead bias**: Only use time-based features that are known at the time of prediction (e.g., "is_weekend" is known for future dates, but rolling statistics computed from future data are not).
- **Store features centrally**: A Feature Store provides a single source of truth and enables automatic feature freshness for batch and streaming pipelines.
- **Combine with external regressors**: Time-based features can be complemented with domain-specific covariates (e.g., weather, promotional schedules) to further improve model accuracy.

## Related Concepts

- [Covariates](/concepts/covariates-external-regressors-for-forecasting.md)
- [Feature Store](/concepts/feature-store.md)
- [AutoML Forecasting](/concepts/automl-forecast.md)
- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- PySpark
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- [Machine Learning](/concepts/cicd-for-machine-learning.md)

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
