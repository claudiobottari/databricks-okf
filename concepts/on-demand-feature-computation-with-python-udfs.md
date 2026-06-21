---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf9ffe40ef0ddc0d29189e06ff1fd6bb6209ffaa16c6f279b7d6b2ae05a45c08
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - on-demand-feature-computation-with-python-udfs
    - OFCWPU
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: On-demand Feature Computation with Python UDFs
description: Pattern for computing features at inference time using registered Python UDFs that transform raw input data into feature values on the fly
tags:
  - feature-store
  - udf
  - inference
timestamp: "2026-06-19T18:48:39.014Z"
---

# On-demand Feature Computation with Python UDFs

**On-demand Feature Computation with Python UDFs** is a capability in Databricks Feature Store that allows users to define features as Python functions and compute them at inference time, rather than pre‑materialising them in feature tables. These on‑demand features are registered as [FeatureFunction](/concepts/featurefunction.md) objects and are automatically tracked in the Unity Catalog lineage alongside feature tables and models. ^[feature-governance-and-lineage-databricks-on-aws.md]

## How it works

When a model is logged using `FeatureEngineeringClient.log_model`, the system captures all feature lookups – both from static feature tables and from dynamic Python UDFs. The UDFs are defined as functions in Unity Catalog and are referenced by `FeatureFunction` objects in the feature list. During inference, the UDFs are executed on‑the‑fly using the input data bindings supplied at lookup time. ^[feature-governance-and-lineage-databricks-on-aws.md]

A typical workflow involves:

1. Registering a Python function as a Unity Catalog function (e.g. `extract_user_latitude`, `haversine_distance`).
2. Creating a `FeatureFunction` object that references the UDF, specifies the output column name, and maps input bindings to the function’s parameters.
3. Including the `FeatureFunction` in the feature list passed to `create_training_set` and later `log_model`.

The following example (adapted from the Databricks documentation) shows how on‑demand features are defined and used:

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

^[feature-governance-and-lineage-databricks-on-aws.md]

## Lineage tracking

Lineage for on‑demand feature functions is captured automatically when `log_model` is called. The[Unity Catalog](/concepts/unity-catalog.md) lineage graph shows the relationship between:

- The feature tables used in `FeatureLookup` objects.
- The Python UDFs used in `FeatureFunction` objects.
- The registered model version.

To view the lineage:

1. Navigate to the table, model version, or function page in Catalog Explorer.
2. Click the **Lineage** tab.
3. Click **See lineage graph** to open the interactive graph.

^[feature-governance-and-lineage-databricks-on-aws.md]

## Benefits

On‑demand computation reduces storage costs because features do not need to be pre‑computed and stored. It also makes it easy to derive features from raw data (e.g. JSON blobs) that change frequently, since the computation logic is centralised in a single UDF and reused across models. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Access control

Access to the underlying UDFs is governed by [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). Only users with the appropriate permissions on the function can reference it in `FeatureFunction` objects or execute it during inference. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Related concepts

- [Feature Store](/concepts/feature-store.md) — Central repository for feature definitions.
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — Client for creating training sets and logging models with feature lineage.
- [FeatureFunction](/concepts/featurefunction.md) — API object for referencing a Python UDF as an on‑demand feature.
- [FeatureLookup](/concepts/featurelookup.md) — API object for referencing a static feature table.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that manages privileges and lineage.
- [Data Lineage](/concepts/data-lineage.md) — Tracking how data flows from sources to models.

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
