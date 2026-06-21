---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea4a753070493e269851ce8f7a23e6220cbf6231b096b8fde74090a1c8468af0
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - on-demand-features-databricks
    - OF(
    - On-Demand Features
    - On-demand features
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
title: On-demand features (Databricks)
description: Features computed at inference time using Python UDFs in Unity Catalog, used when feature values depend on request-time inputs.
tags:
  - feature-store
  - inference
  - databricks
timestamp: "2026-06-19T19:49:24.668Z"
---

# On-demand features (Databricks)

**On-demand features** are features whose values are not known ahead of time but are calculated at inference time. In Databricks, they are implemented using Python user-defined functions (UDFs) that are registered in Unity Catalog and automatically evaluated when a model is scored. ^[on-demand-feature-computation-databricks-on-aws.md]

## Prerequisites

- Your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md).
- You must use Databricks Runtime 13.3 LTS ML or above. ^[on-demand-feature-computation-databricks-on-aws.md]

## Workflow

On-demand features are defined by a Python UDF that describes how to compute the feature value. During training, you pass this function along with its input bindings in the `feature_lookups` parameter of the `create_training_set` API. The trained model must be logged using the Feature Store method `log_model`, which ensures that the model automatically evaluates on-demand features when used for inference. For batch scoring, the `score_batch` API calculates and returns all feature values, including on-demand features. When a model is served with [Model Serving](/concepts/model-serving.md), the UDF is invoked for each scoring request. ^[on-demand-feature-computation-databricks-on-aws.md]

## Create a Python UDF

You can create a Python UDF using either SQL or Python code. The function must be registered in Unity Catalog using a three-level namespace (catalog.schema.function_name). ^[on-demand-feature-computation-databricks-on-aws.md]

### Python example

```python
from unitycatalog.ai.core.databricks import DatabricksFunctionClient

client = DatabricksFunctionClient()
CATALOG = "main"
SCHEMA = "default"

def add_numbers(number_1: float, number_2: float) -> float:
    """Adds two floating point numbers."""
    return number_1 + number_2

function_info = client.create_python_function(
    func=add_numbers,
    catalog=CATALOG,
    schema=SCHEMA,
    replace=True
)
```

After creation, you can view the function definition in [Catalog Explorer](/concepts/catalog-explorer.md). ^[on-demand-feature-computation-databricks-on-aws.md]

### Handling missing feature values

When a Python UDF depends on the result of a `FeatureLookup`, the value returned if the lookup key is not found depends on the environment:

- With `score_batch`, the value is `None`.
- With online serving, the value is `float("nan")`.

The following SQL example shows how to handle both cases by returning `0` when the input is missing:

```sql
CREATE OR REPLACE FUNCTION square(x INT)
RETURNS INT
LANGUAGE PYTHON AS
$$
import numpy as np
if x is None or np.isnan(x):
    return 0
return x * x
$$
```

^[on-demand-feature-computation-databricks-on-aws.md]

## Train a model using on-demand features

To train a model, you use a `FeatureFunction` object inside the `feature_lookups` parameter of `create_training_set`. The `FeatureFunction` references the UDF by its three-level name and specifies how input values map to the function’s arguments. ^[on-demand-feature-computation-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.feature_engineering import FeatureFunction, FeatureLookup

fe = FeatureEngineeringClient()

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
```

The `training_set` contains the computed on-demand feature and the label, ready for model fitting. ^[on-demand-feature-computation-databricks-on-aws.md]

## Specify default values

You can use the `default_values` parameter of `FeatureLookup` to provide a fallback when a lookup key is not found. If feature columns are renamed with `rename_outputs`, the keys in `default_values` must match the renamed names. ^[on-demand-feature-computation-databricks-on-aws.md]

```python
FeatureLookup(
    table_name='main.default.table',
    feature_names=['materialized_feature_value'],
    lookup_key='id',
    default_values={"materialized_feature_value": 0}
)
```

## Log the model and register it to Unity Catalog

Models that use on-demand features must be logged with `fe.log_model()` and registered to Unity Catalog. Set the registry URI to `"databricks-uc"` before logging. If the UDF imports additional Python packages, specify them with `extra_pip_requirements`. ^[on-demand-feature-computation-databricks-on-aws.md]

```python
import mlflow

mlflow.set_registry_uri("databricks-uc")

fe.log_model(
    model=model,
    artifact_path="model",
    flavor=mlflow.sklearn,
    training_set=training_set,
    registered_model_name="main.default.recommender_model",
    extra_pip_requirements=["scikit-learn==1.20.3"]
)
```

## Limitations

- On-demand features can output all [data types supported by Feature Store](/concepts/supported-data-types-for-feature-stores.md) except `MapType` and `ArrayType`.
- For `databricks-feature-engineering` versions below 0.14.0, the following Unity Catalog privileges are required to use a UDF for creating a training set or a Feature Serving endpoint:
  - `USE CATALOG` on the `system` catalog
  - `USE SCHEMA` on the `system.information_schema` schema

^[on-demand-feature-computation-databricks-on-aws.md]

## Sources

- on-demand-feature-computation-databricks-on-aws.md

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
