---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a041e35a8b46106093092025864a52692eefc02de9fdfead9c176126a7fd2c0d
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featureengineeringclientlog_model
    - FeatureEngineeringClient.log_model
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
title: FeatureEngineeringClient.log_model
description: API method that automatically captures lineage of features, feature tables, and Python UDFs when logging an ML model
tags:
  - api
  - feature-store
  - mlflow
timestamp: "2026-06-19T18:48:05.260Z"
---

# FeatureEngineeringClient.log_model

`FeatureEngineeringClient.log_model` is a method on the [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) class that logs a machine learning model along with its feature definitions, automatically capturing lineage between the model, the feature tables it references, and any Python UDF functions used for on-demand feature computation. This lineage is then visible in Unity Catalog's Catalog Explorer. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Overview

`FeatureEngineeringClient.log_model` is the primary method for registering a model trained using features from a [Databricks Feature Store](/concepts/databricks-feature-store.md). The method accepts a model object (such as an MLflow PyFunc model), a training set created via `create_training_set`, and metadata like the registered model name. It persists the model in the Unity Catalog registry and associates it with the feature tables and functions used during training. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Lineage Capture

When you call `log_model`, two types of lineage relationships are automatically recorded:

- **Feature table lineage** – Every [FeatureLookup](/concepts/featurelookup.md) in the `training_set` is tracked, so the model version shows which feature tables it depends on.
- **On‑demand function lineage** – Every [FeatureFunction](/concepts/featurefunction.md) (a Python UDF) used to compute on‑demand features is also captured.

You can inspect this lineage in the **Lineage** tab of Catalog Explorer for the model version, each feature table, and each function. The lineage graph visualises how these Unity Catalog objects are connected. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Requirements for Model Serving with Automatic Feature Lookup

Models logged with `FeatureEngineeringClient.log_model` (or the legacy `FeatureStoreClient.log_model`) can be served with automatic feature lookup from online stores. The following requirements apply:

- The model must be logged with `FeatureEngineeringClient.log_model` (requires Feature Engineering in Unity Catalog) or `FeatureStoreClient.log_model` (legacy Workspace Feature Store, requires v0.3.5 and above). ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]
- For third-party online stores, the store must be published with read-only credentials. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]
- Supported data types for automatic feature lookup include `IntegerType`, `FloatType`, `BooleanType`, `StringType`, `DoubleType`, `LongType`, `TimestampType`, `DateType`, `ShortType`, `ArrayType`, and `MapType`. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

Automatic feature lookup is supported for [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) and Amazon DynamoDB (v0.3.8 and above). ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Override Feature Values During Scoring

When scoring a model served via Model Serving, you can override feature values by including them in the REST API payload. The new values must conform to the feature's expected data type. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Save Augmented DataFrame to Inference Table

For endpoints created starting February 2025, you can configure a model serving endpoint to log the augmented DataFrame containing looked-up feature values and function return values. This DataFrame is saved to the inference table for the served model. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Usage Example

The following example creates a training set with feature lookups and feature functions, defines a Python model, and logs it with `FeatureEngineeringClient.log_model`. Lineage for the feature tables and UDFs is captured automatically.

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup, FeatureFunction

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name="main.on_demand_demo.restaurant_features",
        feature_names=["latitude", "longitude"],
        rename_outputs={"latitude": "restaurant_latitude", "longitude": "restaurant_longitude"},
        lookup_key="restaurant_id",
        timestamp_lookup_key="ts"
    ),
    FeatureFunction(
        udf_name="main.on_demand_demo.extract_user_latitude",
        output_name="user_latitude",
        input_bindings={"blob": "json_blob"},
    ),
    FeatureFunction(
        udf_name="main.on_demand_demo.extract_user_longitude",
        output_name="user_longitude",
        input_bindings={"blob": "json_blob"},
    ),
    FeatureFunction(
        udf_name="main.on_demand_demo.haversine_distance",
        output_name="distance",
        input_bindings={
            "x1": "restaurant_longitude",
            "y1": "restaurant_latitude",
            "x2": "user_longitude",
            "y2": "user_latitude"
        },
    )
]

training_set = fe.create_training_set(
    df,
    feature_lookups=features,
    label="label",
    exclude_columns=["restaurant_id", "json_blob", "restaurant_latitude",
                     "restaurant_longitude", "user_latitude", "user_longitude", "ts"]
)

class IsClose(mlflow.pyfunc.PythonModel):
    def predict(self, ctx, inp):
        return (inp['distance'] < 2.5).values

model_name = "fe_packaged_model"
mlflow.set_registry_uri("databricks-uc")

fe.log_model(
    IsClose(),
    model_name,
    flavor=mlflow.pyfunc,
    training_set=training_set,
    registered_model_name=registered_model_name
)
```

After logging, open the model version in Catalog Explorer and select the **Lineage** tab to see the feature tables and functions the model depends on. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Access Control

Access to the feature tables a model references is enforced separately by [Unity Catalog](/concepts/unity-catalog.md) privileges. The `log_model` method does not grant additional access; users attempting to read the model or its feature lineage must have appropriate permissions on the underlying objects. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Related Concepts

- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) – The client class that provides `log_model`.
- [FeatureLookup](/concepts/featurelookup.md) – References a feature table column to use as a feature.
- [FeatureFunction](/concepts/featurefunction.md) – References a Python UDF to compute an on‑demand feature.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI where model lineage is displayed.
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – How lineage is represented and queried.
- MLflow Models – The model registry that `log_model` writes to.
- [Model Serving with Automatic Feature Lookup](/concepts/model-serving-with-automatic-feature-lookup.md) – Serving models logged with `log_model`.
- [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) – Recommended online store for feature serving.

## Sources

- feature-governance-and-lineage-databricks-on-aws.md
- model-serving-with-automatic-feature-lookup-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
2. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
