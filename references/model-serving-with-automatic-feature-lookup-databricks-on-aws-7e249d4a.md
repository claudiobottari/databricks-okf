---
title: Model Serving with automatic feature lookup | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/automatic-feature-lookup
ingestedAt: "2026-06-18T08:10:05.462Z"
---

[Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) can automatically look up feature values from a [Databricks Online Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store) or a [third-party online store](https://docs.databricks.com/aws/en/machine-learning/feature-store/third-party-online-stores). For real-time serving of feature values, Databricks recommends using [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

## Requirements[​](#requirements "Direct link to Requirements")

*   The model must have been logged with `FeatureEngineeringClient.log_model` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.log_model` (for legacy Workspace Feature Store), requires v0.3.5 and above).

*   For third-party online stores, the online store must be [published with read-only credentials](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication#provide-online-store-credentials-using-databricks-secrets).

note

You can publish the feature table at any time prior to model deployment, including after model training.

## Automatic feature lookup[​](#automatic-feature-lookup "Direct link to automatic-feature-lookup")

Databricks [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) supports automatic feature lookup from these online stores:

*   [Databricks Online Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store)
*   Amazon DynamoDB (v0.3.8 and above)

Automatic feature lookup is supported for the following data types:

*   `IntegerType`
*   `FloatType`
*   `BooleanType`
*   `StringType`
*   `DoubleType`
*   `LongType`
*   `TimestampType`
*   `DateType`
*   `ShortType`
*   `ArrayType`
*   `MapType`

## Override feature values in online model scoring[​](#override-feature-values-in-online-model-scoring "Direct link to Override feature values in online model scoring")

All features required by the model (logged with `FeatureEngineeringClient.log_model` or `FeatureStoreClient.log_model`) are automatically looked up from online stores for model scoring. To override feature values when scoring a model using a REST API with [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#score) include the feature values as a part of the API payload.

note

The new feature values must conform to the feature's data type as expected by the underlying model.

## Save the augmented DataFrame in the inference table[​](#-save-the-augmented-dataframe-in-the-inference-table "Direct link to -save-the-augmented-dataframe-in-the-inference-table")

For endpoints created starting February 2025, you can configure a model serving endpoint to log the augmented DataFrame that contains the looked-up feature values and function return values. The DataFrame is saved to the inference table for the served model.

For instructions on setting this configuration, see [Log feature lookup DataFrames to inference tables](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving#features).

For information about inference tables, see [Monitor served models using Unity AI Gateway\-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables).

## Notebook examples[​](#notebook-examples "Direct link to notebook-examples")

With Databricks Runtime 13.3 LTS and above, any Delta table in Unity Catalog with a primary key can be used as a feature table. When you use a table registered in Unity Catalog as a feature table, all Unity Catalog capabilities are automatically available to the feature table.

### Databricks Online Feature Store[​](#databricks-online-feature-store "Direct link to Databricks Online Feature Store")

The following notebook illustrates how to publish features to a Databricks Online Feature Store for real-time serving and automated feature lookup.

#### Databricks online store demo notebook

### Third-party online stores[​](#third-party-online-stores "Direct link to Third-party online stores")

This example notebook illustrates how to publish features to a third-party online store and then serve a trained model that automatically looks up features from the online store.

#### Third-party online store example notebook (Unity Catalog)

### Workspace Feature Store (legacy)[​](#workspace-feature-store-legacy "Direct link to Workspace Feature Store (legacy)")

This example notebook illustrates how to publish features to an online store and then serve a trained model that automatically looks up features from the online store.

#### Third-party online store example notebook (Workspace Feature Store)
