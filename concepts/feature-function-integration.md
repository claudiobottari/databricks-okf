---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0434d4a2894b952739cca616c02f87ced307097a63bc305ef43ed9409d615e6b
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-function-integration
    - FFI
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Feature Function Integration
description: The capability to define and include Python UDFs within a FeatureSpec to compute derived features on the fly, using input bindings from other features or request parameters.
tags:
  - feature-engineering
  - udf
  - databricks
timestamp: "2026-06-19T10:30:44.866Z"
---

# Feature Function Integration

**Feature Function Integration** is the practice of combining precomputed feature lookups from online tables with on-the-fly function computations inside a single [FeatureSpec](/concepts/featurespec.md) object. A FeatureSpec unifies both types of feature logic – materialized lookups and inline UDF calculations – so that a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) returns a complete feature vector without requiring the caller to separately fetch raw data and then apply a computation step.

## How a FeatureSpec Combines Lookups and Functions

A `FeatureSpec` is a user‑defined collection of `FeatureLookup` entries and `FeatureFunction` entries. The lookups retrieve already‑stored values from an online table, while the functions compute new values at serving time by calling a registered Unity Catalog UDF. Both kinds of entry are declared together in a single `FeatureSpec` and managed as a Unity Catalog object.  
^[feature-serving-endpoints-databricks-on-aws.md]

### FeatureLookup (materialized columns)

`FeatureLookup` specifies the online table, the key column used for the lookup, and the names of the columns to return. The endpoint automatically resolves the lookup and extracts the requested columns from the online store. Optionally you can supply default values for columns that are missing at lookup time.  
^[feature-serving-endpoints-databricks-on-aws.md]

### FeatureFunction (on‑the‑fly UDF)

`FeatureFunction` wraps a Unity Catalog function (created with `DatabricksFunctionClient.create_python_function()`) and gives it an output name. The function’s parameters are bound at serving time using `input_bindings`, which can reference other features returned by the same `FeatureSpec` or directly from the inference request. The result of the function call is a new feature column that is appended to the output vector.  
^[feature-serving-endpoints-databricks-on-aws.md]

## Why Integrate Lookups with Functions

1. **Latency reduction**. Without integration, a caller would first fetch the raw lookup columns, then run a separate compute step. Because the function is evaluated inside the serving endpoint, the whole vector is produced in a single round‑trip.  
   ^[feature-serving-endpoints-databricks-on-aws.md]

2. **Consistency**. The same `FeatureSpec` is deployed to both the offline training pipeline and the online serving endpoint, guaranteeing that training‑time and inference‑time features are computed identically.  
   ^[feature-serving-endpoints-databricks-on-aws.md]

3. **Automatic binding**. When a model served via [Model Serving](/concepts/model-serving.md) was built with features from a `FeatureSpec`, Model Serving automatically performs the lookup and function evaluation at inference time without any extra code in the model.  
   ^[feature-serving-endpoints-databricks-on-aws.md]

## Example: Creating a FeatureSpec that Integrates a Function

```python
from databricks.feature_engineering import (
    FeatureFunction,
    FeatureLookup,
    FeatureEngineeringClient,
)

fe = FeatureEngineeringClient()

features = [
    # Materialized lookup
    FeatureLookup(
        table_name="main.default.customer_profile",
        lookup_key="user_id",
        feature_names=["average_yearly_spend", "country"],
    ),
    # On‑the‑fly function
    FeatureFunction(
        udf_name="main.default.difference",
        output_name="spending_gap",
        input_bindings={
            "num_1": "ytd_spend",
            "num_2": "average_yearly_spend",
        },
    ),
]

fe.create_feature_spec(
    name="main.default.customer_features",
    features=features,
)
```

In this spec, `average_yearly_spend` comes from a lookup, and `spending_gap` is computed by the UDF `difference` that subtracts the second argument from the first. The `ytd_spend` value is provided by the inference request itself.  
^[feature-serving-endpoints-databricks-on-aws.md]

## Deployment as an Endpoint

Once the `FeatureSpec` is created, it can be deployed as a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md):

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import ServedEntityInput, EndpointCoreConfigInput

workspace = WorkspaceClient()

workspace.serving_endpoints.create(
    name="my-serving-endpoint",
    config=EndpointCoreConfigInput(
        served_entities=[
            ServedEntityInput(
                entity_name="main.default.customer_features",
                scale_to_zero_enabled=True,
                workload_size="Small",
            )
        ]
    ),
)
```

The endpoint exposes the combined lookup‑and‑compute logic under a single URL. Callers send a request body with the lookup key and any request‑side inputs, and the endpoint returns the full feature vector.  
^[feature-serving-endpoints-databricks-on-aws.md]

## Requirements for Functions

- The UDF must be created with `unitycatalog.ai.core.databricks.DatabricksFunctionClient` and registered in Unity Catalog.
- The UDF’s return type must match or be castable to the data type expected by the `output_name`.
- `input_bindings` can reference any column that is present in the `FeatureSpec` (whether from a lookup or from the request body).  
^[feature-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [FeatureSpec](/concepts/featurespec.md) – The combined lookup‑and‑function definition object.
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – The REST endpoint that serves the integrated vector.
- [Online Feature Store](/concepts/online-feature-store.md) – The store that holds the materialized lookup tables.
- [Model Serving](/concepts/model-serving.md) – Automatic feature resolution for models that use a `FeatureSpec`.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The `FeatureEngineeringClient` API used to create `FeatureSpecs`.

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
