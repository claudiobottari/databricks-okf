---
title: "AutoML: Improve forecasting with covariates (external regressors) | Databricks on AWS"
source: https://docs.databricks.com/aws/en/machine-learning/automl/automl-covariate-forecast
ingestedAt: "2026-06-18T08:09:23.747Z"
---

This article shows you how to use covariates, also known as external regressors, to improve AutoML forecasting models.

Covariates are additional variables outside the target time series that can improve forecasting models. For example, if you're forecasting hotel occupancy rates, knowing if it's the weekend could help predict customer behavior.

In this example, you:

1.  Create a randomized time-series dataset.
2.  Perform basic feature engineering work.
3.  Store the dataset as a `FeatureStore` table.
4.  Use the `FeatureStore` as covariates in an AutoML forecasting experiment.

## Create the data[​](#create-the-data "Direct link to Create the data")

This example uses randomly generated time series data for hotel occupancy rates in January 2024. Then, use AutoML to predict the `occupancy_rate` for the first day of February 2024.

Run the following code to generate the sample data.

Python

    df = spark.sql("""SELECT explode(sequence(to_date('2024-01-01'), to_date('2024-01-31'), interval 1 day)) as date, rand() as occupancy_rate FROM (SELECT 1 as id) tmp ORDER BY date""")display(df)

## Feature engineering[​](#feature-engineering "Direct link to Feature engineering")

Use the sample dataset to feature engineer a feature called `is_weekend` that a binary classifier of whether or not a `date` is a weekend.

Python

    from pyspark.sql.functions import dayofweek, whendef compute_hotel_weekend_features(df):  ''' is_weekend feature computation code returns a DataFrame with 'date' as primary key'''  return df.select("date").withColumn(      "is_weekend",      when(dayofweek("date").isin( 1, 2, 3, 4, 5), 0) # Weekday      .when(dayofweek("date").isin(6, 7), 1) # Weekend  )hotel_weekend_feature_df = compute_hotel_weekend_features(df)

## Create the Feature Store[​](#create-the-feature-store "Direct link to Create the Feature Store")

To use covariates on AutoML, you must use a [Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/) to join one or more covariate feature tables with the primary training data in AutoML.

Store the data frame `hotel_weather_feature_df` as a Feature Store.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()hotel_weekend_feature_table = fe.create_table(  name='ml.default.hotel_weekend_features', # change to desired location  primary_keys=['date'],  df=hotel_weekend_feature_df,  description='Hotel is_weekend features table')

note

This example uses the Python `FeatureEngineeringClient` to create and write tables. However, you can also use SQL or DeltaLiveTables to write and create tables. See [Feature tables in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc) for more options.

## Configure the AutoML experiment[​](#configure-the-automl-experiment "Direct link to Configure the AutoML experiment")

Use the `feature_store_lookups` parameter to pass the Feature Store to AutoML. `feature_store_lookups` contains a dictionary with two fields: `table_name` and `lookup_key`.

Python

    hotel_weekend_feature_lookup = {  "table_name": "ml.default.hotel_weekend_features", # change to location set above  "lookup_key": ["date"]}feature_lookups = [hotel_weekend_feature_lookup]

note

`feature_store_lookups` can contain multiple feature table lookups.

## Run the AutoML experiment[​](#run-the-automl-experiment "Direct link to Run the AutoML experiment")

Use the following code to pass the `features_lookups` to an AutoML experiment API call.

Python

    from databricks import automlsummary = automl.forecast(dataset=df, target_col="occupancy_rate", time_col="date", frequency="d", horizon=1, timeout_minutes=30, identity_col=None, feature_store_lookups=feature_lookups)

## Next steps[​](#next-steps "Direct link to Next steps")

*   [AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference)
*   [Feature tables in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc)
