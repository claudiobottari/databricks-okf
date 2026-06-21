---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f0590c1b0716d0ecae7ebf32914f509ee865cd0bcaa25921522330424b448e6
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - catalog-explorer-lineage-tab
    - CELT
    - Catalog Explorer Lineage
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: Catalog Explorer Lineage Tab
description: The UI surface in Databricks Catalog Explorer where users can view lineage for tables, model versions, and functions, including a 'See lineage graph' option for a visual graph view.
tags:
  - catalog-explorer
  - lineage
  - ui
timestamp: "2026-06-18T12:18:33.772Z"
---

# Catalog Explorer Lineage Tab

The **Lineage tab** in [Catalog Explorer](/concepts/catalog-explorer.md) displays the upstream and downstream dependencies of Unity Catalog objects — including tables, MLflow Models, model versions, and functions — that were captured during model logging with the [Feature Engineering Client](/concepts/featureengineeringclient-api.md). ^[feature-governance-and-lineage-databricks-on-aws.md]

## Overview

When you log a model using `FeatureEngineeringClient.log_model`, the features used in the model are automatically tracked. This lineage information is stored in Unity Catalog and can be viewed in the Lineage tab of any related table, model version, or function. In addition to feature tables, Python UDFs that are used to compute on-demand features are also tracked. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Viewing Lineage

To view the lineage of a feature table, model, or function:

1. Navigate to the table, model version, or function page in Catalog Explorer.
2. Select the **Lineage** tab. The left sidebar shows Unity Catalog components that were logged with this table, model version, or function.
3. Click **See lineage graph** to open the interactive lineage graph. For details about exploring the lineage graph, see [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md).
4. To close the lineage graph, click the close button in the upper-right corner. ^[feature-governance-and-lineage-databricks-on-aws.md]

## What Is Tracked

The Lineage tab captures relationships between the following Unity Catalog objects: ^[feature-governance-and-lineage-databricks-on-aws.md]

- **Feature tables** — Tables containing features used in model training or inference
- **Functions** — Python UDFs used to compute on-demand features
- **Models** — MLflow models logged with feature metadata

## How Lineage Is Captured

Lineage information is automatically captured when you call `FeatureEngineeringClient.log_model`. The `FeatureLookup` and `FeatureFunction` objects passed to `create_training_set` define the upstream dependencies that are recorded. ^[feature-governance-and-lineage-databricks-on-aws.md]

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
        udf_name="main.on_demand_demo.haversine_distance",
        output_name="distance",
        input_bindings={
            "x1": "restaurant_longitude", "y1": "restaurant_latitude",
            "x2": "user_longitude", "y2": "user_latitude"
        },
    )
]

training_set = fe.create_training_set(
    label_df, feature_lookups=features, label="label",
    exclude_columns=["restaurant_id", "json_blob", "restaurant_latitude",
                     "restaurant_longitude", "user_latitude", "user_longitude", "ts"]
)

fe.log_model(
    IsClose(),
    model_name,
    flavor=mlflow.pyfunc,
    training_set=training_set,
    registered_model_name=registered_model_name
)
```

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Detailed exploration of the lineage graph
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The API used to log models with lineage tracking
- [Feature Tables](/concepts/feature-tables.md) — Tables containing features tracked in lineage
- MLflow Models — Models whose dependencies are captured in the Lineage tab
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI where the Lineage tab is located
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores lineage metadata

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
