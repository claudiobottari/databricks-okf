---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5b59f6cf8d907d6de8bb115ac8bb0c5e84b9dae20f9cee15d44cc4a804508a5
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - covariates-in-time-series-forecasting
    - CITSF
    - Covariate Forecasting
    - Covariates in Forecasting
    - Covariates in Time Series
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Covariates in Time Series Forecasting
description: External regressors — additional variables outside the target time series that can improve forecasting model accuracy.
tags:
  - time-series
  - forecasting
  - feature-engineering
timestamp: "2026-06-19T17:38:53.343Z"
---

# Covariates in Time Series Forecasting

**Covariates**, also known as **external regressors**, are additional variables outside the target time series that can improve the accuracy of forecasting models. Unlike the target variable, which is the primary value being predicted, covariates provide supplementary information that captures external factors influencing the target. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend can help predict customer behavior more accurately than using historical occupancy data alone. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Covariates with AutoML

Databricks AutoML supports incorporating covariates into forecasting experiments through the [Feature EngineeringClient](/concepts/featureengineeringclient-api.md). To use covariates, you must store the feature-engineered variables as feature tables in [Unity Catalog](/concepts/unity-catalog.md) and reference them using the `feature_store_lookups` parameter. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Requirements

- Covariates must be stored in a feature table with a primary key that matches the time column in the training dataset (typically a date column). ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- The `feature_store_lookups` parameter accepts a list of dictionaries, each containing `table_name` and `lookup_key` fields. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- Multiple covariate feature tables can be joined with the primary training data. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Basic Workflow

1. **Feature engineering**: Create derived features from existing data that may improve predictions. Common examples include binary indicators for weekends, holidays, or seasons. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
2. **Store as a feature table**: Save the feature-engineered DataFrame to a feature table with a primary key matching the time column. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
3. **Configure lookups**: Define the feature store lookups by specifying the table name and the key columns used for joining. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
4. **Pass to AutoML**: Pass the `feature_store_lookups` parameter to the `automl.forecast()` API call, alongside the primary dataset and forecasting parameters. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Example: Weekend Feature as a Covariate

The following example demonstrates the complete workflow for predicting hotel occupancy rates using a weekend indicator as a covariate. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Step 1: Feature Engineering

Create a feature that indicates whether a date is a weekend:

```python
from pyspark.sql.functions import dayofweek, when

def compute_hotel_weekend_features(df):
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)           # Weekend
    )
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Step 2: Create Feature Table

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

### Step 3: Configure Feature Lookups

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Step 4: Run AutoML Experiment

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

- **Choose relevant covariates**: Select external variables that have a known or expected relationship with the target time series. Irrelevant covariates can add noise and reduce forecast accuracy. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Align time granularity**: Ensure covariate data matches the frequency and time range of the target time series to enable proper joining. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Use multiple covariate tables when appropriate**: The `feature_store_lookups` parameter supports multiple feature tables, allowing you to combine different types of external information. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Advantages Over Direct Feature Inclusion

Using covariate tables through the feature store offers several advantages over adding features directly to the training dataset:

- **Reusability**: Feature tables can be reused across multiple experiments and models. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Governance**: Features are managed under [Unity Catalog](/concepts/unity-catalog.md) with access control and lineage tracking. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Consistency**: Feature engineering logic is maintained in a single location rather than duplicated across notebooks. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Limitations

- Covariates require data at the same time granularity as the primary training data (e.g., daily covariates for a daily forecast). ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- The join between covariate tables and training data is performed at experiment time, so covariate data must be available in the feature store at that point. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning for forecasting and other tasks
- [Feature EngineeringClient](/concepts/featureengineeringclient-api.md) — Python API for managing feature tables
- [Feature Store](/concepts/feature-store.md) — Managed feature storage and serving
- [Data Profiling](/concepts/data-profiling.md) — Statistical analysis of data quality and distributions
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for data and AI assets
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The broader discipline of predicting future values from historical data
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) — Monitoring model predictions over time

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
