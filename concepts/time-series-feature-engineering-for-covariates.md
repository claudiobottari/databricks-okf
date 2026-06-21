---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a60588f4b87fae876e7bbfeb56f3da6e1b1dd21ce2b29981f2ec3771e1148fb5
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-feature-engineering-for-covariates
    - TFEFC
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Time-Series Feature Engineering for Covariates
description: The process of deriving predictive features from time-series data, such as binary weekend indicators from date columns, to use as covariates.
tags:
  - feature-engineering
  - time-series
  - databricks
timestamp: "2026-06-18T14:30:48.716Z"
---

# Time-Series Feature Engineering for Covariates

**Time-Series Feature Engineering for Covariates** refers to the process of creating additional input variables (covariates, also known as external regressors) that can improve the accuracy of time-series forecasting models. These covariates represent information outside the target time series that may have predictive power.

## Overview

Covariates are additional variables beyond the target time series that can improve forecasting models. For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend could help predict customer behavior. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

Feature engineering for covariates involves transforming raw temporal data into meaningful features that capture patterns such as day-of-week effects, holiday indicators, seasonal cycles, or external events. These engineered features are then made available to forecasting models through a [Feature Store](/concepts/feature-store.md). ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Common Covariate Features

Typical time-series covariate features include:

- **Binary indicators** — Flags for weekends, holidays, or special events
- **Cyclical features** — Day of week, month, quarter, or day of year encoded to preserve circular relationships
- **Lag features** — Past values of related variables
- **Rolling statistics** — Moving averages or standard deviations over a window
- **External data** — Weather, economic indicators, or promotional calendars

## Feature Engineering Workflow

### 1. Create the Feature Computation Function

Define a function that transforms the time-series data into covariate features. The function should return a DataFrame with a primary key column (typically the date or timestamp) and the engineered feature columns. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from pyspark.sql.functions import dayofweek, when

def compute_hotel_weekend_features(df):
    ''' is_weekend feature computation code returns a DataFrame with 'date' as primary key'''
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)  # Weekend
    )
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### 2. Store Features in a Feature Store

To use covariates with AutoML forecasting, the engineered features must be stored in a [Feature Store](/concepts/feature-store.md) table. This allows the forecasting model to join covariate features with the primary training data at training and inference time. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

The feature table must have a primary key column (typically the time column) that matches the key in the training dataset. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### 3. Configure Feature Lookups

When running an AutoML forecasting experiment, pass the feature table lookups using the `feature_store_lookups` parameter. Each lookup specifies the `table_name` and the `lookup_key` columns used to join the features. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

Multiple feature table lookups can be provided in a single list, enabling the use of covariates from different sources. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### 4. Run the Forecasting Experiment

Pass the feature lookups to the AutoML forecasting API call. AutoML automatically joins the covariate features with the training data during model training. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

- **Use a primary key that matches the time column** — The feature table's primary key should align with the time column in the training dataset to ensure correct joins. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Engineer features that are available at forecast time** — Covariates must be known for the forecast horizon. For example, future weekend dates are always known, but future weather data may require a separate forecast. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Store features in Unity Catalog** — Feature tables in [Unity Catalog](/concepts/unity-catalog.md) provide governance, discoverability, and lineage tracking for covariate features. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Combine multiple covariate sources** — Multiple feature tables can be joined to provide a rich set of external regressors for the forecasting model. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — Automated time-series model selection and tuning
- [Feature Store](/concepts/feature-store.md) — Centralized repository for feature management
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Broader practice of creating predictive features
- Time-Series Forecasting — The overall forecasting workflow
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and discovery for feature tables
- External Regressors — Alternative term for covariates in forecasting

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
