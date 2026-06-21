---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c369b80c453bb8f2dd118dec7ceeb27efb4201d7fe23a3538b90d5f4be84979
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - covariates-external-regressors-in-time-series-forecasting
    - C(RITSF
    - Covariates
    - covariates
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Covariates (External Regressors) in Time Series Forecasting
description: Additional variables outside the target time series that can improve forecasting model accuracy by providing exogenous information.
tags:
  - time-series
  - forecasting
  - feature-engineering
timestamp: "2026-06-19T22:11:38.798Z"
---

# Covariates (External Regressors) in Time Series Forecasting

**Covariates**, also known as **external regressors**, are additional variables outside the target time series that can improve forecasting model accuracy by providing external context and explanatory power. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

In time series forecasting, standard models primarily learn patterns from the historical values of the target variable alone. Covariates enrich this signal by incorporating information about external factors that influence the outcome. For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend can help predict customer behavior more accurately than using occupancy history alone. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Covariates with AutoML

[Databricks AutoML](/concepts/databricks-automl.md) supports the use of covariates through integration with the [Feature Store](/concepts/feature-store.md). To use covariates in an AutoML forecasting experiment, you must store the covariate data as a Feature Store table and reference it during the experiment configuration. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Workflow

1. **Create the time series dataset.** Prepare the primary dataset containing the target variable and time column.
2. **Engineer covariate features.** Compute additional features from external data sources. For example, derive an `is_weekend` binary flag from the date column.
3. **Store covariates in the Feature Store.** Use the `FeatureEngineeringClient` to create a feature table with a primary key that matches the time column in the primary dataset.
4. **Configure the AutoML experiment.** Pass the feature table lookups to AutoML using the `feature_store_lookups` parameter, which accepts a list of dictionaries containing `table_name` and `lookup_key` fields. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
5. **Run the experiment.** AutoML automatically joins the covariate features with the primary training data during model training.

### Example: Weekend Feature as a Covariate

The following demonstrates a complete workflow for forecasting hotel occupancy rates with a weekend covariate. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

#### Step 1: Create the Primary Dataset

```python
df = spark.sql("""
  SELECT explode(sequence(to_date('2024-01-01'), to_date('2024-01-31'), interval 1 day)) as date,
         rand() as occupancy_rate
  FROM (SELECT 1 as id) tmp
  ORDER BY date
""")
```

#### Step 2: Engineer the Covariate Feature

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

#### Step 3: Store in Feature Store

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

#### Step 4: Configure AutoML with Covariates

```python
from databricks import automl

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

## Feature Store Lookups

The `feature_store_lookups` parameter accepts a list of dictionaries, each containing two fields: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

| Field | Description |
|-------|-------------|
| `table_name` | The name of the Feature Store table containing the covariate features |
| `lookup_key` | A list of column names used to join the feature table with the primary dataset |

You can include multiple feature table lookups in a single experiment, allowing you to combine covariates from different sources. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Alternative Methods for Creating Feature Tables

While this example uses the Python `FeatureEngineeringClient` to create and write tables, you can also use SQL or Delta Live Tables to write and create feature tables. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Best Practices

- **Align time keys precisely.** Ensure the covariate table's primary key matches the time column in the primary dataset at the same granularity (daily, hourly, etc.). ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Avoid lookahead bias.** Covariate features must be available at prediction time. Do not include future information in the covariate table. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Use meaningful external signals.** Choose covariates that have a plausible causal or correlational relationship with the target variable. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- **Store covariates in Unity Catalog.** Feature tables in [Unity Catalog](/concepts/unity-catalog.md) provide governance, versioning, and discoverability for covariate features. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

Note: The best practices listed above are inferred from the workflow described in the source.

## Related Concepts

- [Databricks AutoML](/concepts/databricks-automl.md) — Automated machine learning platform for forecasting
- [Feature Store](/concepts/feature-store.md) — Centralized repository for feature management
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution for feature tables
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The broader forecasting methodology
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Techniques for creating predictive features
- Delta Live Tables — Alternative method for creating feature tables

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
