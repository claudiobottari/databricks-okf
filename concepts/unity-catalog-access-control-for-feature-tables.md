---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca57370120988091a3d7999beb34175f0688f498d987403d1c8fc710b1261404
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-access-control-for-feature-tables
    - UCACFFT
    - Access control for feature tables
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: Unity Catalog Access Control for Feature Tables
description: Governance of feature table access managed through Unity Catalog's privilege system, controlling who can read or write feature tables
tags:
  - governance
  - unity-catalog
  - access-control
timestamp: "2026-06-19T18:48:13.055Z"
---

---
title: Unity Catalog Access Control for Feature Tables
summary: Access control for feature tables stored in Unity Catalog is governed entirely by Unity Catalog's privilege model, not by Feature Store-specific ACLs. Lineage is automatically captured when models are logged.
sources:
  - feature-governance-and-lineage-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:18:40.385Z"
updatedAt: "2026-06-25T10:00:00.000Z"
tags:
  - unity-catalog
  - access-control
  - feature-store
  - lineage
aliases:
  - unity-catalog-access-control-for-feature-tables
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Unity Catalog Access Control for Feature Tables

Access control for [Feature Tables](/concepts/feature-tables.md) in [Databricks Feature Store](/concepts/databricks-feature-store.md) is managed entirely through [Unity Catalog](/concepts/unity-catalog.md)'s privilege model. Because feature tables are stored as Unity Catalog tables, the same permission system that governs other securable objects — such as schemas, tables, and views — applies to feature tables. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Access Control

To control who can read, write, or manage a feature table, use Unity Catalog privileges. Common privileges for feature tables include `SELECT` (to read features for training or serving), `MODIFY` (to add or update feature data), and ownership or administrative roles. These privileges can be granted at the catalog, schema, or individual table level using SQL `GRANT` and `REVOKE` statements or through Catalog Explorer. ^[feature-governance-and-lineage-databricks-on-aws.md]

For the full list of available privileges and detailed instructions on granting and revoking access, see [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). ^[feature-governance-and-lineage-databricks-on-aws.md]

## Lineage Tracking

In addition to access control, Databricks Feature Store automatically captures [lineage](/concepts/data-lineage.md) information when you log a model using `FeatureEngineeringClient.log_model`. The lineage tracks which feature tables, [feature functions](/concepts/feature-function-udf.md) (including Python UDFs used to compute on-demand features), and models were used. ^[feature-governance-and-lineage-databricks-on-aws.md]

Lineage is visible in the **Lineage** tab of Catalog Explorer. You can click **See lineage graph** to explore the full lineage graph. For details about exploring the lineage graph, see [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md). ^[feature-governance-and-lineage-databricks-on-aws.md]

### Viewing Lineage

To view the lineage of a feature table, model, or function:

1. Navigate to the table, model version, or function page in Catalog Explorer.
2. Select the **Lineage** tab. The left sidebar shows Unity Catalog components that were logged with this table, model version, or function.
3. Click **See lineage graph**.
4. To close the lineage graph, click the close button in the upper-right corner. ^[feature-governance-and-lineage-databricks-on-aws.md]

### Capturing Lineage with Code

Lineage information is automatically captured when you call `log_model`. The example below demonstrates how to log a model with feature lookups and feature functions, which then appear in the lineage graph.

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
    label_df,
    feature_lookups=features,
    label="label",
    exclude_columns=[
        "restaurant_id", "json_blob",
        "restaurant_latitude", "restaurant_longitude",
        "user_latitude", "user_longitude", "ts"
    ]
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

^[feature-governance-and-lineage-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md)
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md)
- [Feature Tables](/concepts/feature-tables.md)
- [Feature functions](/concepts/feature-function-udf.md)

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
