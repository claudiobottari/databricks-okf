---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0b288383bde7f7532f5b4c481eb098c78d13a477cb026dc68f0ffc0729615dc
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-with-on-demand-features
    - MSWOF
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
title: Model serving with on-demand features
description: Workflow for serving models that use on-demand features, covering batch scoring (score_batch) and real-time Model Serving with automatic UDF evaluation.
tags:
  - model-serving
  - inference
  - feature-store
timestamp: "2026-06-19T19:49:33.073Z"
---

# Model Serving with On-Demand Features

**Model serving with on-demand features** refers to the practice of computing feature values at inference time — rather than ahead of time — using Python user-defined functions (UDFs). This approach is used when the value of a feature depends on request-time inputs that are not known until a scoring request arrives. ^[on-demand-feature-computation-databricks-on-aws.md]

## Overview

On-demand features are calculated on the fly when a model is used for inference. In Databricks, they are implemented as [Python UDFs in Unity Catalog](/concepts/python-udfs-in-unity-catalog.md) and are governed by the same three-level namespace as other Unity Catalog objects. The workspace must be enabled for Unity Catalog, and the runtime must be Databricks Runtime 13.3 LTS ML or above. ^[on-demand-feature-computation-databricks-on-aws.md]

## Workflow

The workflow for model serving with on-demand features involves three stages: training, model logging, and inference.

### Training

During training, a `FeatureFunction` object is created that references the Python UDF and specifies how input columns from the training DataFrame are bound to the UDF’s parameters. The `FeatureFunction` is provided to the `create_training_set` API in the `feature_lookups` parameter, alongside any `FeatureLookup` objects that retrieve pre-materialized features. The training set is loaded as a DataFrame, and the model is trained on the resulting feature columns. ^[on-demand-feature-computation-databricks-on-aws.md]

### Model Logging

To ensure that the model automatically evaluates on-demand features when used for inference, the trained model must be logged using the Feature Store method `log_model`. The registry URI must be set to `"databricks-uc"` to register the model in Unity Catalog. If the Python UDF imports any additional packages, the `extra_pip_requirements` argument must specify those dependencies. ^[on-demand-feature-computation-databricks-on-aws.md]

### Inference

- **Batch scoring:** The `score_batch` API automatically calculates and returns all feature values, including on-demand features, when applied to a batch DataFrame. ^[on-demand-feature-computation-databricks-on-aws.md]
- **Real-time serving:** When a model is served via [Model Serving](/concepts/model-serving.md), the system automatically invokes the Python UDF for each scoring request to compute the on-demand features on the fly. ^[on-demand-feature-computation-databricks-on-aws.md]

## Handling Missing Feature Values

When a `FeatureLookup` used by a Python UDF does not find a matching row for the requested key, the returned value depends on the inference environment. For `score_batch`, the value is `None`. For online serving, the value is `float("nan")`. The UDF should handle both cases — for example, by checking `if x is None or np.isnan(x)` and returning a default value. ^[on-demand-feature-computation-databricks-on-aws.md]

## Creating a Python UDF

Python UDFs can be created using the `unitycatalog-ai` Python library or via Databricks SQL. The UDF is registered in a Unity Catalog three-level namespace (catalog, schema, function name). Once registered, it becomes visible in Catalog Explorer and can be reused across experiments and models. ^[on-demand-feature-computation-databricks-on-aws.md]

## Limitations

- On-demand features can output all data types supported by [Feature Store](/concepts/feature-store.md) except MapType and ArrayType. ^[on-demand-feature-computation-databricks-on-aws.md]
- For `databricks-feature-engineering` versions below 0.14.0, additional Unity Catalog permissions are required on the `system` catalog and `system.information_schema` schema to use a UDF when creating a training set or a Feature Serving endpoint. ^[on-demand-feature-computation-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Python UDFs in Unity Catalog](/concepts/python-udfs-in-unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- Batch Scoring
- [Feature Lookup](/concepts/feature-lookup.md)
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [On-demand features](/concepts/on-demand-features-databricks.md)

## Sources

- on-demand-feature-computation-databricks-on-aws.md

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
