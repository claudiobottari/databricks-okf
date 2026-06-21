---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ccfcc9999d7e7e0f7b1b111ad804ac29740c7f8eca9588b462d1f9cc989eaff
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-udfs-in-unity-catalog
    - PUIUC
    - Python UDF in Unity Catalog
    - UDFs in Unity Catalog
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
title: Python UDFs in Unity Catalog
description: Python user-defined functions registered as first-class objects in Unity Catalog's three-level namespace, usable for on-demand feature computation.
tags:
  - unity-catalog
  - udf
  - databricks
timestamp: "2026-06-19T19:50:14.622Z"
---

# Python UDFs in Unity Catalog

**Python UDFs in Unity Catalog** are user-defined functions written in Python that are registered, governed, and discoverable within Unity Catalog on Databricks. They enable on-demand feature computation, where feature values are calculated at inference time rather than being known ahead of time. ^[on-demand-feature-computation-databricks-on-aws.md]

## Overview

Python UDFs allow you to specify how to calculate feature values using Python code. These functions are governed by Unity Catalog and can be discovered through [Catalog Explorer](/concepts/catalog-explorer.md). They are essential for scenarios where feature values depend on request-time inputs and cannot be pre-computed. ^[on-demand-feature-computation-databricks-on-aws.md]

## Requirements

To use Python UDFs in Unity Catalog, your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) and you must use **Databricks Runtime 13.3 LTS ML** or above. ^[on-demand-feature-computation-databricks-on-aws.md]

## Creating a Python UDF

You can create a Python UDF using either SQL or Python code. The function is registered in a three-level namespace (catalog, schema, function name) within Unity Catalog. ^[on-demand-feature-computation-databricks-on-aws.md]

### Using Python

To create a Python UDF using Python, install the `unitycatalog-ai[databricks]` package and use the `DatabricksFunctionClient`:

```python
%pip install unitycatalog-ai[databricks]
dbutils.library.restartPython()

from unitycatalog.ai.core.databricks import DatabricksFunctionClient

client = DatabricksFunctionClient()

def add_numbers(number_1: float, number_2: float) -> float:
    """Adds two floating point numbers and returns the sum."""
    return number_1 + number_2

function_info = client.create_python_function(
    func=add_numbers,
    catalog="main",
    schema="default",
    replace=True
)
```

^[on-demand-feature-computation-databricks-on-aws.md]

### Using Databricks SQL

You can also create a Python UDF using SQL:

```sql
CREATE OR REPLACE FUNCTION square(x INT)
RETURNS INT
LANGUAGE PYTHON
AS $$
import numpy as np
if x is None or np.isnan(x):
    return 0
return x * x
$$
```

^[on-demand-feature-computation-databricks-on-aws.md]

## Handling Missing Feature Values

When a Python UDF depends on a FeatureLookup result, the value returned for a missing lookup key depends on the environment:

- **batch scoring (`score_batch`)**: returns `None`
- **online serving**: returns `float("nan")`

The provided SQL example demonstrates handling both cases by checking for `None` or `np.isnan(x)`. ^[on-demand-feature-computation-databricks-on-aws.md]

## Using On-Demand Features in Model Training

To train a model using on-demand features, you pass a `FeatureFunction` to the `create_training_set` API in the `feature_lookups` parameter. The function uses `input_bindings` to map request-time inputs to UDF parameters. ^[on-demand-feature-computation-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureFunction, FeatureLookup

features = [
    FeatureFunction(
        udf_name="main.default.example_feature",
        input_bindings={
            "x": "new_source_input",
            "y": "materialized_feature_value"
        },
        output_name="on_demand_feature"
    ),
    FeatureLookup(
        table_name='main.default.table',
        feature_names=['materialized_feature_value'],
        lookup_key='id'
    )
]
```

^[on-demand-feature-computation-databricks-on-aws.md]

### Specifying Default Values

You can specify default values for features using the `default_values` parameter in `FeatureLookup`. If feature columns are renamed using `rename_outputs`, the default values must use the renamed names. ^[on-demand-feature-computation-databricks-on-aws.md]

## Logging and Registering Models

Models packaged with feature metadata must be registered to Unity Catalog for automatic on-demand feature evaluation during inference. Use `mlflow.set_registry_uri("databricks-uc")` and `fe.log_model()` with the `training_set` parameter. ^[on-demand-feature-computation-databricks-on-aws.md]

```python
import mlflow
mlflow.set_registry_uri("databricks-uc")

fe.log_model(
    model=model,
    artifact_path="main.default.model",
    flavor=mlflow.sklearn,
    training_set=training_set,
    registered_model_name="main.default.recommender_model"
)
```

If the UDF imports any Python packages, specify them using `extra_pip_requirements`. ^[on-demand-feature-computation-databricks-on-aws.md]

## Limitations

- On-demand features can output all [data types supported by Feature Store](/concepts/supported-data-types-for-feature-stores.md) except **MapType** and **ArrayType**. ^[on-demand-feature-computation-databricks-on-aws.md]
- For `databricks-feature-engineering` versions below **0.14.0**, additional Unity Catalog permissions are required:
  - `USE CATALOG` privilege on the `system` catalog
  - `USE SCHEMA` privilege on `system.information_schema` ^[on-demand-feature-computation-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- On-demand feature computation
- [Feature Store](/concepts/feature-store.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- on-demand-feature-computation-databricks-on-aws.md

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
