---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7686adb196cd4ea175660a7f58d996923e481f6f52ff9f317aefca9653d7026
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - feature-governance-and-lineage-databricks-on-aws.md
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - featurefunction
    - Feature functions
    - feature functions
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: feature-serving-endpoints-databricks-on-aws.md
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: FeatureFunction
description: A mechanism for on-demand feature computation that combines real-time inference inputs with stored feature values at scoring time.
tags:
  - feature-store
  - on-demand
  - inference
timestamp: "2026-06-19T18:12:24.500Z"
---

# FeatureFunction

**FeatureFunction** is a component of Databricks Feature Engineering that enables on‑demand feature computation at inference time. Unlike features that are pre‑computed and stored in feature tables, a `FeatureFunction` defines a computation that runs when an inference request arrives, combining real‑time inputs from the request with materialized values retrieved from feature tables. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## How It Works

A `FeatureFunction` wraps a user‑defined function (UDF) registered in [Unity Catalog](/concepts/unity-catalog.md). The UDF accepts parameters; some are bound to fields in the inference request (the “real‑time inputs”), and others to values from pre‑computed feature tables retrieved using [FeatureLookup](/concepts/featurelookup.md). When an inference request is processed, the serving infrastructure executes the UDF, combining the request‑supplied data with the looked‑up feature values in real time. The return value becomes a new feature column in the response. ^[feature-serving-endpoints-databricks-on-aws.md]

This pattern is essential when a feature depends on a calculation that cannot be pre‑materialized. Common use cases include:

- Computing the difference between a real‑time value (e.g., year‑to‑date spend) and a historical average stored in a feature table.
- Applying a transformation that uses request‑specific parameters, such as extracting parts of a JSON blob or computing a distance between two points.
- Combining several features into a derived score that incorporates live context.

## Creating a FeatureFunction

To use a `FeatureFunction`, you must first create a Python UDF in Unity Catalog. The function must be pure (no side effects) and its signature must match the bindings you intend to use. The following example creates a Python UDF that subtracts two numbers: ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from unitycatalog.ai.core.databricks import DatabricksFunctionClient

client = DatabricksFunctionClient()

def difference(num_1: float, num_2: float) -> float:
  """Subtracts num_2 from num_1 and returns the result."""
  return num_1 - num_2

client.create_python_function(
  func=difference,
  catalog="main",
  schema="default",
  replace=True
)
```

After the UDF exists, you define a `FeatureFunction` object that references it. The `FeatureFunction` requires: ^[feature-serving-endpoints-databricks-on-aws.md]

- **`udf_name`** – the fully qualified name of the UDF in Unity Catalog.
- **`output_name`** – the name of the feature column that the function’s return value will populate.
- **`input_bindings`** – a dictionary mapping UDF parameter names to either:
  - The name of a feature from a `FeatureLookup` (e.g., `"average_yearly_spend"`), or
  - The name of a field in the inference request (e.g., `"ytd_spend"`).

## Using FeatureFunction in a FeatureSpec

A [Feature Spec (FeatureSpec)](/concepts/featurespec.md) combines `FeatureLookup` entries and `FeatureFunction` entries into a single logical unit for serving. The `FeatureFunction` is added to the `features` list alongside `FeatureLookup` objects. Here is an example from the documentation: ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.feature_engineering import (
    FeatureFunction, FeatureLookup, FeatureEngineeringClient
)

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name="main.default.customer_profile",
        lookup_key="user_id",
        feature_names=["average_yearly_spend", "country"]
    ),
    FeatureFunction(
        udf_name="main.default.difference",
        output_name="spending_gap",
        input_bindings={
            "num_1": "ytd_spend",           # from request
            "num_2": "average_yearly_spend" # from lookup
        },
    ),
]

fe.create_feature_spec(
    name="main.default.customer_features",
    features=features,
)
```

In this example, the `spending_gap` feature is computed at inference time by subtracting the looked‑up `average_yearly_spend` from the real‑time `ytd_spend` provided in the request.

A more complex example from a governance tutorial shows multiple `FeatureFunction`s used together to extract coordinates from a JSON blob and then compute a haversine distance: ^[feature-governance-and-lineage-databricks-on-aws.md]

```python
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
        "x1": "restaurant_longitude", "y1": "restaurant_latitude",
        "x2": "user_longitude", "y2": "user_latitude"
    },
)
```

Here, the first two functions extract individual fields from a request‑supplied `json_blob`, and the third function uses those extracted values together with looked‑up coordinates to compute a derived distance feature.

## Serving with FeatureFunction

When a Feature Serving endpoint is created from a `FeatureSpec` that includes `FeatureFunction` entries, the serving infrastructure automatically executes the UDF for each inference request. The request must supply the fields referenced in the bindings (e.g., `"ytd_spend"` or `"json_blob"`). The augmented response includes both the looked‑up materialized features and the computed feature. ^[feature-serving-endpoints-databricks-on-aws.md]

The following query example shows a request to the endpoint that includes `user_id` and `ytd_spend`: ^[feature-serving-endpoints-databricks-on-aws.md]

```json
{
  "dataframe_records": [
    { "user_id": 1, "ytd_spend": 598 },
    { "user_id": 2, "ytd_spend": 280 }
  ]
}
```

The endpoint responds with all features defined in the `FeatureSpec`, including those computed on demand.

## Lineage Tracking

When a model is logged using `FeatureEngineeringClient.log_model`, any `FeatureFunction` referenced in the training set is automatically tracked as part of the model’s lineage. The UDFs used to compute on‑demand features appear in the **Lineage** tab of Catalog Explorer, alongside feature tables. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Requirements

- `databricks-feature-engineering` version 0.1.2 or above (built into Databricks Runtime 14.2 ML).
- The UDF must be created in Unity Catalog.
- For real‑time serving, the feature tables used in input bindings must be published to an online feature store. ^[feature-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Feature Spec (FeatureSpec)](/concepts/featurespec.md) – The container that groups `FeatureLookup`s and `FeatureFunction`s for serving.
- [FeatureLookup](/concepts/featurelookup.md) – Defines which materialized feature columns to retrieve from a feature table.
- Feature Serving – Low‑latency serving of features (materialized and on‑demand) via a REST endpoint.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer under which UDFs and feature specs are registered.
- [Online Feature Store](/concepts/online-feature-store.md) – Stores pre‑computed features for real‑time lookup.
- On-Demand Feature Computation – The broader concept of computing features at inference time.

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- feature-governance-and-lineage-databricks-on-aws.md
- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
3. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
