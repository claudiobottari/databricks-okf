---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e8f8edf869e593b7ba078e3e1449e4790ff6690aa7106686ff4a3d62c570e3b
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-feature-lineage-capture
    - AFLC
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: Automatic Feature Lineage Capture
description: Lineage information tracking feature tables and Python UDFs used in models is automatically captured when calling log_model
tags:
  - lineage
  - feature-store
  - governance
timestamp: "2026-06-19T10:29:52.266Z"
---

# Automatic Feature Lineage Capture

**Automatic Feature Lineage Capture** is a capability of Databricks Feature Store that automatically records the relationships between feature tables, Python UDF functions, and models during model logging. This lineage information is stored in Unity Catalog and can be viewed via the **Lineage** tab in Catalog Explorer. ^[feature-governance-and-lineage-databricks-on-aws.md]

## How It Works

When you log a model using `FeatureEngineeringClient.log_model`, the features used in the model — including references to feature tables and Python UDFs that compute on-demand features — are automatically tracked. This provides end-to-end traceability from raw feature sources to the trained model. ^[feature-governance-and-lineage-databricks-on-aws.md]

To capture lineage, the `FeatureLookup` and `FeatureFunction` objects passed in the `feature_lookups` parameter of `create_training_set` are recorded. For example:

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
    # ... additional FeatureFunctions
]

training_set = fe.create_training_set(
    label_df,
    feature_lookups=features,
    label="label",
    exclude_columns=["restaurant_id", ...]
)

fe.log_model(
    model,
    model_name,
    flavor=mlflow.pyfunc,
    training_set=training_set,
    registered_model_name=registered_model_name
)
```

After `log_model` is called, the lineage information is automatically stored in Unity Catalog. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Viewing Lineage

To view the lineage of a feature table, model version, or function:

1. Navigate to the table, model version, or function page in **Catalog Explorer**.
2. Select the **Lineage** tab. The left sidebar shows Unity Catalog components that were logged with this object.
3. Click **See lineage graph** to open an interactive graph showing upstream and downstream dependencies. ^[feature-governance-and-lineage-databricks-on-aws.md]

The lineage graph includes both feature tables and Python UDFs used in model training. For further details about exploring the graph, see [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md).

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Central repository for feature tables used in machine learning.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer that manages access control and lineage.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for browsing and inspecting Unity Catalog assets.
- [Model Registry](/concepts/mlflow-model-registry.md) – Versioned storage for logged and registered models.
- [Data Profiling](/concepts/data-profiling.md) – Monitoring feature table data changes and model performance.

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
