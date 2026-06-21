---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 155d3cfc217cd66f21c357db5ada1ddd0fb1c3a7faf2a12b98ec33f5f4da4569
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featurefunction-api
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
title: FeatureFunction API
description: API construct in Databricks Feature Engineering that binds Python UDF inputs to columns/feature lookups for on-demand feature computation during training and inference.
tags:
  - feature-store
  - api
  - databricks
timestamp: "2026-06-19T19:49:39.064Z"
---

## FeatureFunction API

The **FeatureFunction API** is a component of the Databricks Feature Engineering client (`databricks-feature-engineering`) that enables the computation of on-demand features at inference time. On-demand features are features whose values are not known ahead of time and depend on request-time inputs; they are calculated using Python user-defined functions (UDFs) registered in [Unity Catalog](/concepts/unity-catalog.md). The `FeatureFunction` class is used within the `feature_lookups` parameter of `create_training_set` to bind a Python UDF to specific input columns, producing a new feature column for model training and scoring. ^[on-demand-feature-computation-databricks-on-aws.md]

### Parameters

A `FeatureFunction` object accepts three parameters:

- **`udf_name`** – The fully qualified name of a Python UDF in Unity Catalog, using the three-level namespace (`catalog.schema.function_name`). The UDF must already exist in Unity Catalog. ^[on-demand-feature-computation-databricks-on-aws.md]
- **`input_bindings`** – A dictionary that maps the names of the UDF’s input parameters to the names of columns in the training DataFrame or feature lookup results. For example, `{"x": "new_source_input", "y": "materialized_feature_value"}` means the UDF’s parameter `x` will receive the value from the column `new_source_input`, and parameter `y` will receive the value from the feature lookup result `materialized_feature_value`. ^[on-demand-feature-computation-databricks-on-aws.md]
- **`output_name`** – A string that specifies the name of the new feature column produced by the UDF. This column will be included in the training set and later used by the model. ^[on-demand-feature-computation-databricks-on-aws.md]

### Usage in the Training Workflow

The `FeatureFunction` is passed to the `create_training_set` API along with [FeatureLookup](/concepts/featurelookup.md) objects. Together they define the complete set of features for a training set. The following example demonstrates a typical workflow:

```python
from databricks.feature_engineering import FeatureFunction, FeatureLookup

features = [
    FeatureFunction(
        udf_name="main.default.example_feature",
        input_bindings={
            "x": "new_source_input",
            "y": "materialized_feature_value"
        },
        output_name="on_demand_feature",
    ),
    FeatureLookup(
        table_name='main.default.table',
        feature_names=['materialized_feature_value'],
        lookup_key='id'
    )
]

training_set = fe.create_training_set(
    df=base_df,
    feature_lookups=features,
    label='label',
    exclude_columns=['id', 'new_source_input', 'materialized_feature_value']
)
training_df = training_set.load_df().toPandas()
```

In this example, `on_demand_feature` is computed by the UDF `main.default.example_feature` using the request-time column `new_source_input` and the pre-materialized feature `materialized_feature_value`. ^[on-demand-feature-computation-databricks-on-aws.md]

### Inference Behavior

When a model is logged with `fe.log_model` (ensuring the feature metadata is packaged with the model), the system automatically evaluates on-demand features during inference:

- For **batch scoring** using `score_batch`, the Python UDF is invoked for each row, and missing lookup keys return `None`. ^[on-demand-feature-computation-databricks-on-aws.md]
- For **online serving** using [Model Serving](/concepts/model-serving.md), the UDF is executed per request, and missing lookup keys return `float("nan")`. ^[on-demand-feature-computation-databricks-on-aws.md]

### Limitations

- On-demand features produced by a `FeatureFunction` can output all [Feature Store data types](/concepts/feature-store.md) except `MapType` and `ArrayType`. ^[on-demand-feature-computation-databricks-on-aws.md]
- For versions of `databricks-feature-engineering` below 0.14.0, additional Unity Catalog privileges are required: `USE CATALOG` on the `system` catalog and `USE SCHEMA` on `system.information_schema`. ^[on-demand-feature-computation-databricks-on-aws.md]

### Related Concepts

- On-demand feature computation – Overview of the feature computation paradigm.
- [Python UDF in Unity Catalog](/concepts/python-udfs-in-unity-catalog.md) – How to register and manage user-defined functions.
- [FeatureLookup API](/concepts/featurelookup.md) – API for retrieving pre-materialized features from feature tables.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The main client that orchestrates training set creation and model logging.
- [Model Serving](/concepts/model-serving.md) – Real-time inference endpoint that automatically computes on-demand features.

### Sources

- on-demand-feature-computation-databricks-on-aws.md (Databricks documentation: “On-demand feature computation”)

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
