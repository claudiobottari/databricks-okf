---
title: AutoML Feature Store integration | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl/feature-store-integration
ingestedAt: "2026-06-18T08:09:30.378Z"
---

AutoML can augment the original input dataset with features from [feature tables in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/) or in the [legacy Workspace Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/).

## Requirements[​](#requirements "Direct link to Requirements")

*   Classification and regression experiments require Databricks Runtime 11.3 LTS ML and above.
*   Forecasting experiments require Databricks Runtime 12.2 LTS ML and above.

## Select a feature table using the AutoML UI[​](#select-a-feature-table-using-the-automl-ui "Direct link to select-a-feature-table-using-the-automl-ui")

After configuring your AutoML experiment, you can select a features table using the following steps:

1.  Click **Join features (optional)**.
    
    ![Select Join features button](https://docs.databricks.com/aws/en/assets/images/automl-join-features-1e4b1fc58a42e31d0ec0a4a2c5c00b24.png)
    
2.  On the **Join additional features** page, select a feature table in the **Feature Table** field.
    
3.  For each **Feature table primary key**, select the corresponding lookup key. The lookup key should be a column in the training dataset you provided for your AutoML experiment.
    
4.  For [time series feature tables](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series), select the corresponding timestamp lookup key. Similarly, the timestamp lookup key should be a column in the training dataset you provided for your AutoML experiment.
    
    ![Select primary key and lookup tables](https://docs.databricks.com/aws/en/assets/images/automl-feature-store-lookup-key-22b30d3a19919fc6172142d915576dd9.png)
    
5.  To add more feature tables, click **Add another feature table** and repeat the above steps.
    

## Use feature tables with the AutoML API[​](#use-feature-tables-with-the-automl-api "Direct link to Use feature tables with the AutoML API")

To use existing feature tables set the `feature_store_lookups` parameter in your [AutoML run specification](https://docs.databricks.com/aws/en/machine-learning/automl/regression-train-api).

Python

    feature_store_lookups = [  {     "table_name": "example.trip_pickup_features",     "lookup_key": ["pickup_zip", "rounded_pickup_datetime"],  },  {      "table_name": "example.trip_dropoff_features",     "lookup_key": ["dropoff_zip", "rounded_dropoff_datetime"],  }]

The following notebook shows how to join feature tables to your training dataset for use with AutoML.

#### AutoML experiment using feature tables notebook
