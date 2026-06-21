---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10932618ef0af5d27392dfe51858de17059dcb559b29048e383f211a127c1b27
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store-lineage
    - DFSL
    - Feature Store Lineage
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: Databricks Feature Store Lineage
description: Automatic tracking of relationships between feature tables, functions, and models used to build ML models in Databricks
tags:
  - feature-store
  - lineage
  - governance
timestamp: "2026-06-19T18:47:55.149Z"
---

# Databricks Feature Store Lineage

**Databricks Feature Store Lineage** refers to the automatic tracking of relationships between feature tables, user-defined functions (UDFs), and models that are used together during model development. Lineage information is captured when you log a model using `FeatureEngineeringClient.log_model` and can be viewed in [Catalog Explorer](/concepts/catalog-explorer.md) through the **Lineage** tab. This lineage enables data scientists and governance teams to understand which features and functions contributed to a model’s training and inference. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Governance via Unity Catalog

Access control for feature tables stored in [Unity Catalog](/concepts/unity-catalog.md) is managed natively by Unity Catalog. This means that standard Unity Catalog privileges (e.g., `SELECT`, `MODIFY`) control who can read or write feature tables. No separate Feature Store permission model is required. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Capturing Lineage

Lineage is automatically captured when you call `FeatureEngineeringClient.log_model`. The `log_model` method records which feature tables and Python UDFs were used in the model’s training set. The following example demonstrates capturing lineage with [FeatureLookup](/concepts/featurelookup.md) and [FeatureFunction](/concepts/featurefunction.md) objects: ^[feature-governance-and-lineage-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup, FeatureFunction

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name = "main.on_demand_demo.restaurant_features",
        feature_names = ["latitude", "longitude"],
        rename_outputs={"latitude": "restaurant_latitude", "longitude": "restaurant_longitude"},
        lookup_key = "restaurant_id",
        timestamp_lookup_key = "ts"
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
        input_bindings={"x1": "restaurant_longitude", "y1": "restaurant_latitude",
                        "x2": "user_longitude", "y2": "user_latitude"},
    )
]

training_set = fe.create_training_set(
    label_df, feature_lookups=features, label="label",
    exclude_columns=["restaurant_id", "json_blob", "restaurant_latitude",
                     "restaurant_longitude", "user_latitude", "user_longitude", "ts"]
)

# ... define model class IsClose ...

fe.log_model(
    IsClose(),
    model_name,
    flavor=mlflow.pyfunc,
    training_set=training_set,
    registered_model_name=registered_model_name
)
```

After `log_model` executes, the lineage between the feature tables and UDFs in `training_set` and the resulting registered model is stored in Unity Catalog. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Viewing Lineage

1. In [Catalog Explorer](/concepts/catalog-explorer.md), navigate to the feature table, model version, or function whose lineage you want to examine.
2. Click the **Lineage** tab.
3. The left sidebar lists the Unity Catalog components that are related to the selected object.
4. Click **See lineage graph** to open an interactive graph showing the upstream and downstream dependencies.

For detailed guidance on exploring the lineage graph, see the [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) documentation. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Monitoring Data and Model Performance

In addition to lineage tracking, you can monitor the performance of a served model and changes in feature table data using the [Data Profiling](/concepts/data-profiling.md) feature in Unity Catalog. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Related Concepts

- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — The client used to log models and capture lineage
- [FeatureLookup](/concepts/featurelookup.md) — Specifies a lookup against a feature table by key
- [FeatureFunction](/concepts/featurefunction.md) — Wraps a Python UDF used for on-demand feature computation
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that controls access to feature tables
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for browsing and viewing lineage
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Broader concept of lineage for all Unity Catalog assets
- [Data Profiling](/concepts/data-profiling.md) — Monitoring data quality and model performance
- [MLflow](/concepts/mlflow.md) — Model tracking framework used with FeatureEngineeringClient

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
