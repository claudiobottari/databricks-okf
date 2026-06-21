---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 31c1fdccd4997bd8b2b93fea1456ffedd3258d419765212793fb1cb3e781031e
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-workflow-with-on-demand-features
    - TWWOF
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
title: Training workflow with on-demand features
description: End-to-end process for training ML models that incorporate on-demand features, including create_training_set, log_model, and Unity Catalog registration.
tags:
  - machine-learning
  - training
  - feature-store
timestamp: "2026-06-19T19:49:51.449Z"
---

# Training workflow with on-demand features

**On-demand features** are features whose values are not known ahead of time but are computed at inference time using Python user-defined functions (UDFs). They depend on request-time inputs and are particularly useful when a feature value – such as a real‑time distance or a dynamically aggregated metric – cannot be pre‑materialised. ^[on-demand-feature-computation-databricks-on-aws.md]

## Prerequisites

To use on‑demand features, your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) and you must use Databricks Runtime 13.3 LTS ML or above. ^[on-demand-feature-computation-databricks-on-aws.md]

## Workflow overview

1. **Define a Python UDF** in Unity Catalog that computes the on‑demand feature.
2. **Use the UDF during training** by passing a `FeatureFunction` to the `create_training_set` API.
3. **Log the trained model** with the Feature Store method `log_model` so that the model automatically evaluates the on‑demand feature at inference time.
4. **Use the model for inference**:  
   - For **batch scoring**, the `score_batch` API automatically calculates and returns all feature values, including on‑demand features.  
   - For **real‑time serving** via [Model Serving](/concepts/model-serving.md), the model automatically invokes the Python UDF for each request.

^[on-demand-feature-computation-databricks-on-aws.md]

## Creating a Python UDF

Python UDFs are governed by Unity Catalog and discoverable through [Catalog Explorer](/concepts/catalog-explorer.md). You can create them using Python code (via the `unitycatalog‑ai` package) or SQL. The function must be registered in a three‑level namespace (`catalog.schema.function_name`). ^[on-demand-feature-computation-databricks-on-aws.md]

### Handling missing feature values

When a Python UDF depends on a `FeatureLookup` and the lookup key is not found, the value returned depends on the environment:

- `score_batch` returns `None`.
- Online serving returns `float("nan")`.

The following SQL example handles both cases by checking for `None` or `NaN`:

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

## Training a model using on‑demand features

To train a model, you use the [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) and pass a list of `FeatureLookup` and `FeatureFunction` objects to the `create_training_set` API. The `FeatureFunction` contains:

- `udf_name`: the three‑level name of the registered Python UDF.
- `input_bindings`: a dictionary mapping the UDF’s parameter names to source columns (either from the base DataFrame or from looked‑up feature values).
- `output_name`: the name of the resulting feature column.

In the example below, the on‑demand feature `on_demand_feature` is computed as the sum of a request‑time input (`new_source_input`) and a pre‑materialised feature (`materialized_feature_value`). ^[on-demand-feature-computation-databricks-on-aws.md]

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

training_df = training_set.load_df().toPandas()
# training_df now contains ['on_demand_feature', 'label']
```

### Specifying default values

If a lookup key is not found, you can supply a default value using the `default_values` parameter in `FeatureLookup`. If features are renamed with `rename_outputs`, `default_values` must use the renamed names. ^[on-demand-feature-computation-databricks-on-aws.md]

```python
FeatureLookup(
    table_name='main.default.table',
    feature_names=['materialized_feature_value'],
    lookup_key='id',
    rename_outputs={"materialized_feature_value": "feature_value"},
    default_values={"feature_value": 0}
)
```

## Logging the model and registering to Unity Catalog

Models packaged with feature metadata must be registered to Unity Catalog. You must set the MLflow registry URI and use `fe.log_model()`. If the Python UDF imports any additional Python packages, specify them with the `extra_pip_requirements` argument. ^[on-demand-feature-computation-databricks-on-aws.md]

```python
import mlflow
mlflow.set_registry_uri("databricks-uc")

fe.log_model(
    model=model,
    artifact_path="main.default.model",
    flavor=mlflow.sklearn,
    training_set=training_set,
    registered_model_name="main.default.recommender_model",
    extra_pip_requirements=["scikit-learn==1.20.3"]
)
```

After logging, the model automatically evaluates the on‑demand features during batch or real‑time inference. ^[on-demand-feature-computation-databricks-on-aws.md]

## Limitations

- On‑demand features can output all [Feature Store](/concepts/feature-store.md) supported data types except MapType and ArrayType.
- For `databricks-feature-engineering` versions below 0.14.0, additional Unity Catalog permissions are required on the `system` catalog and `information_schema` schema to create training sets or Feature Serving endpoints.

^[on-demand-feature-computation-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Python UDF
- [Feature Store](/concepts/feature-store.md)
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md)
- [FeatureFunction](/concepts/featurefunction.md)
- [FeatureLookup](/concepts/featurelookup.md)
- [Model Serving](/concepts/model-serving.md)
- Batch scoring
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- on-demand-feature-computation-databricks-on-aws.md

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
